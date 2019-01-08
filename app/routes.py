from app import api
from app.handler import HelloWorldHandler,PerkalianHandler,DemoCrudHandler,PembeliHandler,ProdukHandler

api.add_resource(HelloWorldHandler,'/')
api.add_resource(PerkalianHandler,'/kali','/kali/<int:bil1>/<int:bil2>')
api.add_resource(DemoCrudHandler,'/demo','/demo/<int:id>')
api.add_resource(PembeliHandler,'/pembeli','/pembeli/<int:id>')
api.add_resource(ProdukHandler,'/produk','/produk/<int:id>')
