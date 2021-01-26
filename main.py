from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/sm64")
def sm64():
    return render_template("sm64.html")


@app.route("/mariosunshine")
def mariosunshine():
    return render_template("mariosunshine.html")


@app.route("/galaxy")
def galaxy():
    return render_template("galaxy.html")


@app.route("/odyssey")
def odyssey():
    return render_template("odyssey.html")

@app.route('/joke', methods=['GET','POST'])
def joke():
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    response = requests.get(url)
    # formatting variables from return
    setup = response.json()[0]['setup']
    punchline = response.json()[0]['punchline']
    return render_template("joke.html", setup=setup, punchline=punchline)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5001')

#test