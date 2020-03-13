from web.app import app


@app.route('/')
def home():
    return b'Nothing'
