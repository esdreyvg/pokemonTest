from app import app
from config import DEBUG, SERVER

config = SERVER

port = config['port']
host = config['host']
debug = DEBUG

try:

    app.run(host=host, port=port, debug=debug)

    print('Server is running on  http://'+host+':'+port)

except Exception as ex:
    print(ex)
