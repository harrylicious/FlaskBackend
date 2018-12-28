import logging
from flask import Flask # dari modul flask, import class Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

app = Flask(__name__) # inisiasi flask instance
api = Api(app) # dari flask-restful, library untuk membuat REST API menggunakan flask
ma = Marshmallow(app) # marshmallow adalah library untuk melakukan serialisasi/deserialisasi object
rdc = RealDictCursor

# pool koneksi ke postgresql
pg_pool = pool.ThreadedConnectionPool(3, 20, database='agromina', user='agro', password='replacewithpassword', host='localhost')

# siapkan logger untuk mencatat log pada kejadian tertentu
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from app import handler # REST handler
from app import routes # API route endpoints
