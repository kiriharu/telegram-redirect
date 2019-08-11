__author__ = "kiriharu, https://github.com/kiriharu/telegram-redirect"
__copyright__ = "Copyright (C) 2019 kiriharu"
__license__ = "MIT License"
__version__ = "1.0"

from flask import render_template, request
from app import app


@app.route('/<string:username>')
def redirect_username(username):
    return render_template("redirect.html", link=f"resolve?domain={username}")


@app.route('/addstickers/<string:stickerset>')
def redirect_stickers(stickerset):
    return render_template("redirect.html", link=f"addstickers?set={stickerset}")


@app.route('/joinchat/<string:chat>')
def redirect_joinchat(chat):
    return render_template("redirect.html", link=f"join?invite={chat}")


@app.route('/proxy')
def redirect_proxy():

    server = request.args.get('server')
    port = request.args.get('port')
    secret = request.args.get('secret')
    return render_template("redirect.html", link=f"proxy?server={server}&port={port}&secret={secret}")


@app.route('/socks')
def redirect_socks():
    server = request.args.get('server')
    port = request.args.get('port')
    user = request.args.get('user')
    password = request.args.get('pass')
    if not password:
        return render_template("redirect.html", link=f"socks?server={server}&port={port}&user={user}")
    return render_template("redirect.html", link=f"socks?server={server}&port={port}&user={user}&pass={password}")


@app.route('/banned')
def banned():
    return render_template("banned.html",)


@app.route('/')
def index():
    return render_template("index.html",)
