create database agromina;
create user agro with encrypted password 'replacewithpassword';
alter database agromina owner to agro;
CREATE TABLE demo
(
  id serial,
  judul character varying(100),
  deskripsi text,
  created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
  updated timestamp without time zone,
  isdeleted boolean DEFAULT false
);
INSERT INTO demo(
            judul, deskripsi)
    VALUES ('Coba 1', 'Ini adalah demo untuk record percobaan');

agromina=# create table pembeli (
agromina(# id int primary key,
agromina(# nama_lengkap varchar(100),
agromina(# gender varchar(20),
agromina(# alamat text,
agromina(# desa varchar(50),
agromina(# kecamatan varchar(50),
agromina(# kabupaten varchar(50),
agromina(# telp varchar(20),
agromina(# email varchar(30),
agromina(# created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
agromina(# updated timestamp without time zone,
agromina(# isdeleted boolean DEFAULT false);

 create table barang (
agromina(# id int primary key,
agromina(# nama varchar(50),
agromina(# deskripsi text,
agromina(# id_supplier int,
agromina(# qty int,
agromina(# satuan varchar(30),
agromina(# harga int,
agromina(# status varchar(30),
agromina(# created timestamp without time zone DEFAULT CURRENT_TIMESTAMP, 
agromina(# updated timestamp without time zone,
agromina(# isdeleted boolean DEFAULT false);

