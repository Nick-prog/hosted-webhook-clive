import flask
from flask import Flask, request, abort

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def get_webhook():
    if request.method == 'POST':
       return request.json
    else:
        abort(400)
        
if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem','publickey.pem'))
    app.run()
