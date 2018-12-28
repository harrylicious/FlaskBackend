from flask_restful import Resource
from flask import request

from app.models import Demo
from app import logger

class HelloWorldHandler(Resource): # REST request handler
    def get(self):
        return {'hello': 'world'}

class PerkalianHandler(Resource):
    def get(self,bil1,bil2):
        bil3 = bil1 * bil2
        return {'hasil': bil3}
    
    def post(self):
        try:
            data = request.get_json(force=True)
            bil1 = data['bil1']
            bil2 = data['bil2']
            bil3 = int(bil1) * int(bil2)
            return {'hasil': bil3}
        except Exception as e:
            pesan_error = 'Ooops, ada yang salah ' + str(e)
            return {'pesan':pesan_error}, 400 


class DemoCrudHandler(Resource):
    model = Demo() # siapkan model dari class Demo
    def get(self, id=0):
        # jika id = 0, diterjemahkan menjadi mengambil semua data 
        # jika id > 0, akan diload data sesuai id yang bersangkutan 
        try:
            if id > 0:
                obj = self.model.get_by_id(id)
                return obj
            else:
                objs = self.model.get_all()
                return objs

        except Exception as e:
            pesan_error = 'Ooops, ada yang salah ' + str(e)
            return {'pesan':pesan_error}, 400 

    def post(self):
        try:
            # data yang diterima dikirim dalam format 'application/json'
            data = request.get_json(force=True)
            obj = self.model.insert(data)
            return obj
        except Exception as e:
            pesan_error = 'Ooops, ada yang salah ' + str(e)
            return {'pesan':pesan_error}, 400

    def put(self):
        try:
            # data yang diterima dikirim dalam format 'application/json'
            data = request.get_json(force=True)
            obj = self.model.update(data)
            return obj
        except Exception as e:
            pesan_error = 'Ooops, ada yang salah ' + str(e)
            return {'pesan':pesan_error}, 400 

    def delete(self):
        try:     
            data = request.get_json(force=True)
            id = data['id']
            obj = self.model.delete(id)
            return obj
        except Exception as e:
            pesan_error = 'Ooops, ada yang salah ' + str(e)
            return {'pesan':pesan_error}, 400 

