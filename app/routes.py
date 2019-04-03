from app import app

 # use decorators as callback/route functions
@app.route('/')
@app.route('/index')
def index():
    return "hello, world!"