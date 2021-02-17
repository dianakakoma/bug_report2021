from website import create_app

app = create_app()

if __name__ == '__main__':
#restart the server anytime we make a code to the Python code
    app.run(debug=True)