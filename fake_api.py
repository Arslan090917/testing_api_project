from app import app

if __name__ == '__main__':
    app.run(
        debug=True,
        use_debugger=False,
        use_reloader=False,
        passthrough_errors=True,
        host='127.0.0.1',
        port=55677
    )