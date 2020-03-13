from web.app import app


@app.route('/ping', methods=['HEAD', 'GET', 'POST'])
def ping():
    return b'pong'
