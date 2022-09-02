from website import create_app

app = create_app()
# Force file to require being ran directly in order to fuction 
if __name__ == '__main__':
    app.run(debug=True)