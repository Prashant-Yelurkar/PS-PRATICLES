from flask import Flask, render_template, request
# Import Flask class and other necessary modules from the flask package

app = Flask(__name__)
# Create an instance of the Flask class for your web application

@app.route('/register', methods=["GET", "POST"])
# Define the route for the URL '/register'. This route can handle both GET and POST requests.
def register():
    # Define the view function for the '/register' route
    if request.method == "POST":
        # Check if the request method is POST (i.e., form submission)
        user = {
            'name': request.form.get("name"),
            'email': request.form.get("email"),
            'password': request.form.get("password")
        }
        # Create a dictionary named 'user' with keys 'name', 'email', and 'password'
        # and assign them the values from the form input fields
        return render_template('success.html', name=user['name'])
        # Render the 'success.html' template, passing the 'user' dictionary within another dictionary under the key 'data'
    return render_template('registrationForm.html')
    # If the request method is GET, render the 'registrationForm.html' template

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
    # If this script is run directly, start the Flask development server
    # Enable debug mode and set the server to listen on all public IPs on port 3000
