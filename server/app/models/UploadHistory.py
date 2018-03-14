from app import db
from datetime import datetime
from datetime import date

class UploadHistory(db.Document):
    '''
    上传历史记录
    '''
    upload_date = db.DatetimeField(default=date.today)
    # date = db.DatetimeField(default=datetime.now)
    patent_count = db.IntField(default=0)
    cnki_count = db.IntField(default=0)
    publicnet_count = db.IntField(default=0)

    def to_dict(self):
        d = {}
        d['upload_date'] = self.upload_date.strptime(str,'%Y-%m-%d')
        d['patent_count'] = self.patent_count
        d['cnki_count'] = self.cnki_count
        d['publicnet_count'] = self.publicnet_count
        return d
