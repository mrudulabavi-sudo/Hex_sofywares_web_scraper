from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []

    if request.method == 'POST':
        url = request.form['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.find_all('h2'):
            data.append(item.text)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
