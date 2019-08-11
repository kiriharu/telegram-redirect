__author__ = "kiriharu, https://github.com/kiriharu/telegram-redirect"
__copyright__ = "Copyright (C) 2019 kiriharu"
__license__ = "MIT License"
__version__ = "1.0"

from peewee import *

db = SqliteDatabase('adverstiment.sqlite')


class Adverstiment(Model):
    link = TextField()
    picture = TextField()
    show = IntegerField()

    class Meta:
        database = db

    def take(self, advid):
        """Set -1 from show related to id"""
        return self.update(show=Adverstiment.show - 1).where(Adverstiment.id == advid).execute()

    def remove(self, advid):
        """Remove record related to id"""
        return self.delete().where(Adverstiment.id == advid).execute()

    def get_data(self, advid):
        """Return data related to id"""
        query = self.select().where(Adverstiment.id == advid)
        if query.exists():
            query = query.get()
            return dict(id=query.id, link=query.link, picture=query.picture, show=query.show)
        else:
            return

    def get_random(self):
        """Return random id of adverstiment"""
        try:
            return self.select().order_by(fn.Random()).get()
        except Exception as e:
            print("Failed to get random adverstiment")

Adverstiment.create_table()