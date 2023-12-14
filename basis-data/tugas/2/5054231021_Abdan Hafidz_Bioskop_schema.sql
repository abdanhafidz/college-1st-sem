-- README -- 
-- Dml yang saya gunakan adalah SQL server, jadi ada sedikit perbedaan syntax, mohon dimaklumi :)
-- Nama : Abdan Hafidz, NRP : 5054231021


-- database-schema :
CREATE TABLE film(
    id_film BIGINT NOT NULL,
    judul VARCHAR(255) NOT NULL,
    tahun_rilis BIGINT NOT NULL,
    id_genre BIGINT NOT NULL
);
ALTER TABLE
    film ADD CONSTRAINT film_id_film_primary PRIMARY KEY(id_film);
CREATE TABLE kategori(
    id_genre BIGINT NOT NULL,
    genre VARCHAR(255) NOT NULL
);
ALTER TABLE
    kategori ADD CONSTRAINT kategori_id_genre_primary PRIMARY KEY(id_genre);
CREATE TABLE aktor(
    id_aktor BIGINT NOT NULL,
    nama_aktor VARCHAR(255) NOT NULL,
    kota_lahir VARCHAR(255) NULL,
    tahun_lahir BIGINT NULL
);
ALTER TABLE
    aktor ADD CONSTRAINT aktor_id_aktor_primary PRIMARY KEY(id_aktor);
CREATE TABLE aktor_membintangi(
    id_role BIGINT NOT NULL,
    id_film BIGINT NOT NULL,
    id_aktor BIGINT NOT NULL
);
ALTER TABLE
    aktor_membintangi ADD CONSTRAINT aktor_membintangi_id_role_primary PRIMARY KEY(id_role);
ALTER TABLE
    aktor_membintangi ADD CONSTRAINT aktor_membintangi_id_aktor_foreign FOREIGN KEY(id_aktor) REFERENCES aktor(id_aktor);
ALTER TABLE
    film ADD CONSTRAINT film_id_genre_foreign FOREIGN KEY(id_genre) REFERENCES kategori(id_genre);
ALTER TABLE
    aktor_membintangi ADD CONSTRAINT aktor_membintangi_id_film_foreign FOREIGN KEY(id_film) REFERENCES film(id_film);

#database seeder :
-- Seeder for film table
INSERT INTO film (id_film, judul, tahun_rilis, id_genre)
VALUES
  (1, 'Film 1', 2020, 1),
  (2, 'Film 2', 2018, 2),
  (3, 'Film 3', 2019, 3),
  (4, 'Film 4', 2021, 1),
  (5, 'Film 5', 2017, 2),
  (6, 'Film 6', 2016, 3),
  (7, 'Film 7', 2022, 1),
  (8, 'Film 8', 2015, 2),
  (9, 'Film 9', 2014, 3),
  (10, 'Film 10', 2023, 1);

-- Seeder for kategori table
INSERT INTO kategori (id_genre, genre)
VALUES
  (1, 'Action'),
  (2, 'Drama'),
  (3, 'Comedy'),
  (4, 'Science Fiction'),
  (5, 'Horror'),
  (6, 'Romance'),
  (7, 'Thriller'),
  (8, 'Fantasy'),
  (9, 'Adventure'),
  (10, 'Mystery');

-- Seeder for aktor table
INSERT INTO aktor (id_aktor, nama_aktor, kota_lahir, tahun_lahir)
VALUES
  (1, 'Aktor 1', 'Kota 1', 1990),
  (2, 'Aktor 2', 'Kota 2', 1992),
  (3, 'Aktor 3', 'Kota 3', 1988),
  (4, 'Aktor 4', 'Kota 4', 1995),
  (5, 'Aktor 5', 'Kota 5', 1991),
  (6, 'Aktor 6', 'Kota 6', 1993),
  (7, 'Aktor 7', 'Kota 7', 1989),
  (8, 'Aktor 8', 'Kota 8', 1994),
  (9, 'Aktor 9', 'Kota 9', 1996),
  (10, 'Aktor 10', 'Kota 10', 1997);

-- Seeder for aktor_membintangi table
INSERT INTO aktor_membintangi (id_role, id_film, id_aktor)
VALUES
  (1, 1, 1),
  (2, 2, 2),
  (3, 3, 3),
  (4, 4, 4),
  (5, 5, 5),
  (6, 6, 6),
  (7, 7, 7),
  (8, 8, 8),
  (9, 9, 9),
  (10, 10, 10);

-- updating data
-- Variasi 1: Mengubah tahun_rilis film dengan ID film > 5 dan < 10
UPDATE film SET tahun_rilis = 2015 WHERE id_film > 5 AND id_film < 10;

-- Variasi 2: Mengubah judul film dengan ID film > 2 dan < 7
UPDATE film SET judul = 'Judul Film Variasi 2' WHERE id_film > 2 AND id_film < 7;

-- Variasi 3: Mengubah genre film dengan ID film > 8 dan < 12
UPDATE film SET id_genre = 3 WHERE id_film > 8 AND id_film < 12;

-- Variasi 4: Mengubah tahun_rilis film dengan ID film > 1 dan < 6
UPDATE film SET tahun_rilis = 2010 WHERE id_film > 1 AND id_film < 6;

-- Variasi 5: Mengubah judul film dengan ID film > 7 dan < 11
UPDATE film SET judul = 'Judul Film Variasi 5' WHERE id_film > 7 AND id_film < 11;
-- Variasi 6: Mengubah genre film dengan ID 6
UPDATE film SET id_genre = 2 WHERE id_film = 6;

-- Variasi 7: Mengubah judul film dengan ID 7
UPDATE film SET judul = 'Judul Film 7 Baru' WHERE id_film = 7;

-- Variasi 8: Mengubah tahun_rilis film dengan ID 8
UPDATE film SET tahun_rilis = 2016 WHERE id_film = 8;

-- Variasi 9: Mengubah genre film dengan ID 9
UPDATE film SET id_genre = 5 WHERE id_film = 9;

-- Variasi 10: Mengubah judul film dengan ID 10
UPDATE film SET judul = 'Judul Film 10 Baru' WHERE id_film = 10;

-- deleting data
-- Variasi 1: Menghapus film dengan ID film = 1
DELETE FROM film WHERE id_film = 1;

-- Variasi 2: Menghapus film dengan tahun_rilis < 2010
DELETE FROM film WHERE tahun_rilis < 2010;

-- Variasi 3: Menghapus film dengan judul 'Judul Film Variasi 2'
DELETE FROM film WHERE judul = 'Judul Film Variasi 2';

-- Variasi 4: Menghapus film dengan genre = 3
DELETE FROM film WHERE id_genre = 3;

-- Variasi 5: Menghapus film dengan ID film > 7 dan < 11
DELETE FROM film WHERE id_film > 7 AND id_film < 11;
