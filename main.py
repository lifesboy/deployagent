from web.app import app


def run():
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=2000)
    return app


run()
