#coding=utf-8
from flask import request, jsonify
from . import main
# from flask_restful import Resourced
from config import config
import pandas,json
from app import pydb
from ..models.UploadHistory import UploadHistory
from datetime import *

@main.route('/')
def test():
    return 'hello'
    
@main.route('/upload',methods=['GET','POST'])
def upload():
    #pandas 计算行数
    type = request.args.get('type')
    file = request.files.get('file')
    upload_file_type = config.UPLOAD_FILE_TYPE
    if type in upload_file_type and file:
        today = date.today
        upload_history = UploadHistory.objects.get(upload_date=today)
        if not upload_history:
            upload_history = UploadHistory()
        if type == 'patent':
            df = pandas.read_excel(file)
            patent_count = df.shape[0]
            df['type'] = 'patent'
            df['upload_date'] = upload_history.upload_date
            df['datetime'] = datetime.now()
            pydb['base'].insert(json.loads(df.T.to_json()).values())
            upload_history.patent_count = upload_history.patent_count + patent_count
            upload_history.save()
            return jsonify({'code':0,'msg':'上传专利成功'})
        elif type == 'cnki':
            df = pandas.read_excel(file)
            cnki_count = df.shape[0]
            df['type'] = 'cnki'
            df['upload_date'] = upload_history.upload_date
            df['datetime'] = datetime.now()
            pydb['base'].insert(json.loads(df.T.to_json()).values())
            upload_history.cnki_count = upload_history.cnki_count + cnki_count
            upload_history.save()
            return jsonify({'code':0,'msg':'上传期刊成功'})
        elif type == 'publicnet':
            df = pandas.read_excel(file)
            publicnet_count = df.shape[0]
            df['type'] = 'publicnet'
            df['upload_date'] = upload_history.upload_date
            df['datetime'] = datetime.now()
            pydb['base'].insert(json.loads(df.T.to_json()).values())
            upload_history.publicnet_count = upload_history.publicnet_count + publicnet_count
            upload_history.save()
            return jsonify({'code':0,'msg':'上传公网成功'})
    else:
        return jsonify({'code':-1,'msg':'上传失败'})

@main.route('/upload_history',methods=['GET','POST'])
def upload_history():
    upload_history = UploadHistory.objects.order_by('-upload_date')
    upload_history = [i.to_dict() for i in upload_history]
    total = pydb['base'].find()
    data = dict(totla=total,history=upload_history)
    return jsonify({'code':0,'msg':'','data':data})

