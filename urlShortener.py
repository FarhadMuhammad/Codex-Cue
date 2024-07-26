from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

url_mapping = {}

def generate_short_url_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_id = generate_short_url_id()
        url_mapping[short_id] = long_url
        return f'Short URL: {request.host_url}{short_id}'
    
    return '''
        <form method="post">
            <label>Enter Long URL:</label><br>
            <input type="text" name="long_url" required><br>
            <input type="submit" value="Shorten URL">
        </form>
    '''

@app.route('/<short_id>')
def redirect_to_long_url(short_id):
    long_url = url_mapping.get(short_id)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404

if __name__ == '_main_':
    app.run(debug=True)
