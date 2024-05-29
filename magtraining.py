from flask import Flask

app = Flask(__name__)

@app.route('/')
def training():
    name = "Karlo" 
    message = f"<h1>Training 22</h1><p>Hi, my name is Karlo</p>"
    return message

if __name__ == '__main__':
    app.run(debug=True)
