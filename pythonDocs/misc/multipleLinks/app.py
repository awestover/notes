from flask import Flask

app = Flask(__name__)

# url patterns flask

#  bhsyearbook.tech?school=arlington
#  bhsyearbook.tech/arlington

@app.route('/converters/')
@app.route('/converters/<int:page>/')
def convertersexample(page=1):
    try:    
        return "Heyo, "+str(page)
    except Exception as e:
        return(str(e))  


if __name__ == "__main__":
    app.run(port="80",debug=True, host="0.0.0.0")



