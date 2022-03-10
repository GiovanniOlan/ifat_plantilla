from app.app import app

HOSTS='localhost'
PORT=5000
DEBUG=True

#This initialize the app web
if __name__ == '__main__':
    app.run(HOSTS,PORT,DEBUG)