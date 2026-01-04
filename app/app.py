from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def deploy():
    return 'Hello, This service deployed using GitHub Actions...'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8081)))