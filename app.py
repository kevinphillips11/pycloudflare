from flask import Flask
from flask_cloudflared import run_with_cloudflared

app = Flask(__name__)
run_with_cloudflared(app)  # Open a Cloudflare Tunnel when app is run
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route("/")
def home(): 
    return "Hello!"

if __name__ == '__main__':
    '''for rule in app.url_map.iter_rules():
        print(rule)'''
    app.run()
