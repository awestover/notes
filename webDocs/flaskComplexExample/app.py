from flask import Flask, render_template, request
import json
app = Flask(__name__)

acceptingBuzzes = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/buzz', methods=['POST'])
def buzz():
    global acceptingBuzzes
    name = request.form['name']
    if name == "master":
        acceptingBuzzes = True
        return json.dumps(True)
    if acceptingBuzzes:
        print("{} buzzed".format(name))
        acceptingBuzzes = False
        with open('buzzLog.txt', 'a') as f:
            f.write("{} buzzed\n".format(name))
        return json.dumps(True)
    else:
        return json.dumps(False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
