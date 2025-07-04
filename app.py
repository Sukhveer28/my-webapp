from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my web app deployed with CI/CD!"

if __name__ == '__main__':
    app.run(debug=True)
