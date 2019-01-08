import time
import traceback
from app import pg_pool
from app import rdc
from app import ma
from app import logger


# Class model untuk Produk
class Produk(ma.Schema):
    # Subclass untuk keperluan serialisasi/deserialisasi menggunakan marshmallow    
    class Meta:
        # daftar field dari model produk
        fields = ('id', 'nama', 'deskripsi', 'id_kategori', 'qty', 'id_supplier', 'harga', 'created', 'updated', 'isdeleted')

    # methods terkait database
    def get_all(self):
        try:
            logger.debug('get all entry')
            conn = pg_pool.getconn() # ambil koneksi dari 
            cur = conn.cursor(cursor_factory=rdc) # buat kursor, dengan factory real dict cursor
            try:
                cur.execute('select * from produk where isdeleted=false order by created desc')
                schema = Produk(many=True)
                result = schema.dump(cur.fetchall())
                logger.debug(result)
                logger.debug(cur.query)
                cur.close()
                return result.data
            finally:
                pg_pool.putconn(conn) # kembalikan koneksi ke pool, agar bisa dipakai kembali oleh yang lain

        except Exception as e:
            raise RuntimeError('oops kesalahan: '+str(e)) from e

    def get_by_id(self,id):
        try:
            conn = pg_pool.getconn()
            cur = conn.cursor(cursor_factory=rdc)
            try:
                cur.execute('select * from produk where id=%s',(id,))
                schema = Produk()
                result = schema.dump(cur.fetchone())
                cur.close()
            finally:
                pg_pool.putconn(conn)
            return result.data 

        except Exception as e:
            raise RuntimeError('oops on produk: '+str(e)) from e
    
    def insert(self,data):
        try:
            logger.debug(data)
            sql_str = (
                'insert into produk' 
                '(judul,deskripsi)'
                'values'
                '(%s, %s)'
                'returning id'
            )
            val_arr = (data['judul'],data['deskripsi'])
            conn = pg_pool.getconn()
            cur = conn.cursor(cursor_factory=rdc)
            try:
                cur.execute(sql_str,val_arr)
                id = cur.fetchone()['id']
                conn.commit()
                cur.close()
                return Produk().get_by_id(id)
            finally:
                pg_pool.putconn(conn)
        except Exception as e:
            raise RuntimeError('oops on produk: '+str(e)) from e
    
    def update(self,data):
        try:
            sql_str = (
                'update produk ' 
                'set nama=%s,deskripsi=%s '
                'where id = %s'
            )
            val_arr = (data['nama'],data['deskripsi'],data['id'])
            conn = pg_pool.getconn()
            cur = conn.cursor(cursor_factory=rdc)
            try:
                cur.execute(sql_str,val_arr)
                conn.commit()
                cur.close()
                return Produk().get_by_id(data['id'])
            finally:
                pg_pool.putconn(conn)
        except Exception as e:
            raise RuntimeError('oops on produk: '+str(e)) from e

    def delete(self,id):
        try:
            sql_str = 'update produk set isdeleted=true where id=%s'
            conn = pg_pool.getconn()
            cur = conn.cursor(cursor_factory=rdc)
            try:
                cur.execute(sql_str,(id,))
                conn.commit()
                cur.close()
                return True
            finally:
                pg_pool.putconn(conn)
        except Exception as e:
            raise RuntimeError('oops on produk: '+str(e)) from e