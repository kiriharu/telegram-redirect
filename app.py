__author__ = "kiriharu, https://github.com/kiriharu/telegram-redirect"
__copyright__ = "Copyright (C) 2019 kiriharu"
__license__ = "MIT License"
__version__ = "1.0"

from flask import Flask, redirect, url_for, template_rendered
from config import banlist, inject, adverstiment_active, adv_templates
from models import Adverstiment
app = Flask(__name__)
adv_db = Adverstiment()
from views import *


@app.context_processor
def inject_vars(**args):
    """Inject vars to app context processor"""
    inject.update(args)
    return inject


@app.before_request
def banlist_check():
    """This function check username/stickerset/chat/server ip for being in banlist.

    @:return banned - banpage
    """
    banned = redirect((url_for("banned")))

    if request.view_args:
        if "username" in request.view_args:
            if request.view_args["username"] in banlist["username"]:
                return banned
        if "stickerset" in request.view_args:
            if request.view_args["stickerset"] in banlist["stickers"]:
                return banned
        if "chat" in request.view_args:
            if request.view_args["chat"] in banlist["joinchat"]:
                return banned
    if request.args.get('server'):
        if request.args.get('server') in banlist['ip']:
            return banned


if adverstiment_active:
    @app.before_request
    def set_adv():
        """Get random adv and set variables to context processor"""
        try:
            data = adv_db.get_data(adv_db.get_random())
            if data['show'] < 1:
                adv_db.remove(data['id'])
            inject_vars(adv_id=data['id'], adv_link=data['link'], adv_pic=data['picture'])
        except TypeError:
            print("Object is not subscriptable, maybe you dont have ads?")
            off_adv()

    @template_rendered.connect_via(app)
    def when_template_rendered(sender, template, context, **extra):
        """Checks if template with adverstiment rendered"""
        try:
            if template.name in adv_templates:
                adv_db.take(inject['adv_id'])
        except KeyError:
            print("Key error ocurred, maybe you don't have ads?")

    def off_adv():
        """Disable ads"""
        print("Off adv, app dont have ads. If you add new ads, pls restart.")
        app.before_request_funcs[None].remove(set_adv)
        template_rendered.disconnect(when_template_rendered, app)
        inject_vars(adverstiment_active=False)

if __name__ == '__main__':
    app.run()
