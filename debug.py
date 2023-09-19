from flask import Flask
import ipdb

# Create a Flask application
app = Flask(__name__)

# Define routes and their associated views
@app.route('/')
def home():
    ipdb.set_trace()  # Add a breakpoint here
    return 'Welcome to the home page'

@app.route('/about')
def about():
    ipdb.set_trace()  # Add a breakpoint here
    return 'This is the about page'

@app.route('/contact')
def contact():
    ipdb.set_trace()  # Add a breakpoint here
    return 'You can contact us at contact@example.com'

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)




# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)