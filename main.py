from flask import Flask, request, jsonify

app = Flask(__name__)

# HTML form to collect the data
@app.route('/my-form')
def my_form():
    return '''
        <form method="POST" action="/process-data">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
  
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
  
            <button type="submit">Submit</button>
        </form>
    '''

# Flask route to receive and process the form data
@app.route('/process-data', methods=['POST'])
def process_data():
    name = request.form['name']
    email = request.form['email']
    
    # perform any necessary processing or database operations here
    
    # return a JSON response
    return jsonify({'message': 'Data processed successfully.'})
