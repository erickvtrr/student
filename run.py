from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(dubug=True,  host='0.0.0.0')
