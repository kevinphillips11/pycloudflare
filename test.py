from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

# Other app configuration and route definitions go here

#run_with_ngrok(app)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=5000)  # If address is in use, may need to terminate other sessions:
               # Runtime > Manage Sessions > Terminate Other Sessions