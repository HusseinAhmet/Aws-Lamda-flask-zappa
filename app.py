from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
 return '<h1>Yeah, that is Zappa! Zappa! Zap! Zap!</h1>'

@app.route('/y')
def yaw():
 return '<h1>Haaaaaaaaaaaaaaaaw</h1>'
@app.route('/Hello')
def Hello():
 return '<h1>Hell guys</h1>'
# We only need this for local development.
if __name__ == '__main__':
 app.run()