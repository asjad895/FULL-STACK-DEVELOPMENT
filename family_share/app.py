from flask import Flask, render_template, request, redirect, url_for, request, flash, session
import mysql.connector
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

# Initialize CSRF protection
csrf = CSRFProtect(app)
# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="data895@AS",
  database="FAMILY_SHARE"
)
@app.route('/')
def login():
    return render_template('login.html')

# Define the route to handle the login form submission
@app.route('/login_submit', methods=['GET', 'POST'])
def login_submit():
    if request.method == 'POST':
        csrf_token = request.form.get('csrf_token')
        print(csrf_token)
        # Retrieve the user input from the request object
        username = request.form['username']
        password = request.form['password']

        # Check the user's credentials against the MySQL database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_info WHERE user_name = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user is not None:
            session['username'] = user[0]
            session['password'] = user[1]
            # Redirect the user to a secure page
            return redirect(url_for('secure'))

    # If the user's credentials are invalid or the request is not a POST request,
    # redirect them to the login page
        # If the user's credentials are invalid, flash an error message
        else:
            flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html')


# Define a secure page that requires authentication
@app.route('/secure')
def secure():
    # Verify authentication by checking session variables
    if 'username' in session and 'email' in session:
        return render_template('home.html')
    else:
        return render_template('home.html')


# signup
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_submit', methods=['GET', 'POST'])
def signup_submit():
    if request.method == 'POST':
        csrf_token = request.form.get('csrf_token')
        print(csrf_token)
        # Extract data from the form
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mob = request.form['mob_no']
        user_name = request.form['user_name']
        password = request.form['password']
        print(password)

        # Construct the SQL query
        query = "INSERT INTO user_info (fname, lname, email, mob, user_name, password) VALUES (%s, %s, %s, %s, %s, %s)"
        values =(fname, lname, email, mob, user_name, password)
        try:
            # Execute the query and commit the changes
            cursor=db.cursor()
            cursor.execute(query, values)
            db.commit()
            print("sucess")
            # Set a flash message to display to the user on the next request
            flash('Account created successfully. Please log in.')
            # Redirect to login page on success
            return redirect(url_for('login'))
        except mysql.connector.Error as error:
            # Display error message and return signup page
            # Print error message and traceback
            import traceback
            traceback.print_exc()
            error_msg = f"Error inserting user info: {error}"
            db.rollback()
            return render_template('signup.html', error=error_msg)
    # Render the signup page for GET requests
    else:
        return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

# search query handling
@app.route('/search')
def search():
    query = request.args.get('query')
    # results = search_files(query)
    results="sucess full query passed to the backend"
    return render_template('home.html',)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # # Store the file in MongoDB
        # file_data = file.read()
        # filename = file.filename
        # upload_time = datetime.utcnow()
        # # books_col.insert_one({
        #     'filename': filename,
        #     'file_data': file_data,
        #     'upload_time': upload_time
        # })
        return render_template('home.html', message='File uploaded successfully')
    else:
        return render_template('home.html', error='No file selected')



if __name__ == '__main__':
    app.run(debug=True)
