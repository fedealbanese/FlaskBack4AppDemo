from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper :)"
    
@app.route("/Hi/<name>")
def hello_1name(name):
    return f"Hello {name}"

@app.route("/var")
def hello_var():
    return f"Hello {EXAMPLE_123}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
