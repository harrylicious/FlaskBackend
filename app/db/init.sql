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
