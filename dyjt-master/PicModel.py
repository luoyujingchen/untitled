from sqlalchemy import Column, Integer, String

from app import db


class Picture(db.Model):
    __tablename__ = 'Picture'

    id = Column(Integer, primary_key=True)
    come_from = Column(String(80), unique=True)
    content_other = Column(String(300), unique=True)
    content_zh = Column(String(300), unique=True)
    url = Column(String(300), unique=True)

    def __init__(self, come_from=None, content_other=None, content_zh=None, url=None):
        self.come_from = come_from
        self.content_other = content_other
        self.content_zh = content_zh
        self.url = url

    # def format(self):
    #     return dict(id=self.id, come_from=self.come_from, content_other=self.content_other, content_zh=self.content_zh,
    #                 url=self.url)
    #
    def __repr__(self):
        return {'id': self.id, 'come_from': self.come_from, 'content_other': self.content_other,
                'content_zh': self.content_zh,'url':self.url}

    @property
    def serialize(self):
        return {
            'id':self.id,
            'come_from': self.come_from,
            'content_other': self.content_other,
            'content_zh': self.content_zh,
            'url': self.url
        }