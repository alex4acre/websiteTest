from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #this will rerun the server as soon as we make a change

    