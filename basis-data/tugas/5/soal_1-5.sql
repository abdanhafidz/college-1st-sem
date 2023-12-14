---1. Tampilkan seluruh transaksi yang terjadi dari tanggal 10 Oktober 2023 hingga 20 Oktober
-- 2023! Tampilkan seluruh kolom dari tabel transaksi. ---
USE pendahuluan;
SELECT*FROM transaksi WHERE 
tanggal_transaksi >= DATE('2023-10-10') 
AND tanggal_transaksi <= DATE('2023-10-20')

-- 2.Hitunglah total harga dari setiap transaksi. Tampilkan id transaksi dan total harga yang
-- berkesesuaian. Untuk mempermudah Mbak Nuri memahami hasil kueri, maka ubahlah
-- tampilkan total harga dengan nama ‘TOTAL_HARGA’!
SELECT t.ID_transaksi, SUM(m.harga_minuman * tm.jumlah_minuman) AS TOTAL_HARGA
FROM Transaksi t
JOIN Transaksi_minuman tm ON t.ID_transaksi = tm.tm_transaksi_id
JOIN Menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
GROUP BY t.ID_transaksi;

-- 3.Hitung total biaya yang pernah dikeluarkan oleh setiap cutsomer pada dari tanggal 3
-- Oktober 2023 hingga 22 Oktober 2023, tampilkan semua kolom dari tabel customer dan
-- total biaya dengan tampilan nama kolom “Total_Belanja”. Urutkan berdasarkan nama
-- customer dari A ke Z.
SELECT c.*, SUM(m.harga_minuman * tm.jumlah_minuman) AS Total_Belanja
FROM Customer c
JOIN transaksi t ON c.id_customer = t.customer_id_customer
JOIN transaksi_minuman tm ON t.id_transaksi = tm.tm_transaksi_id
JOIN menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
WHERE t.tanggal_transaksi BETWEEN '2023-10-03' AND '2023-10-22'
GROUP BY c.ID_customer
ORDER BY c.nama_customer ASC;

-- 4.Mbak Nuri ingin mengetahui data pegawai yang pernah melayani customer dengan nama
-- Davi Liam, Sisil Triana, atau Hendra Asto
SELECT c.nama_customer AS Customer, p.nama_pegawai FROM pegawai p
JOIN transaksi t ON p.nik = t.pegawai_nik
JOIN customer c ON t.customer_id_customer = c.id_customer
WHERE c.nama_customer IN ('Davi Liam', 'Sisil Triana', 'Hendra Astro');

-- 5. Hitunglah jumlah cup yang terjual pada Kopi Nuri setiap bulannya (perhatikan bulan dan
-- tahunnya)! Tampilkan kolom bulan, tahun, dan jumlah cup dengan nama ‘BULAN’,
-- ‘TAHUN’, ‘JUMLAH_CUP’. Urutkan berdasarkan tahun dari yang terbesar dan bulan
-- yang terkecil.
SELECT YEAR(t.tanggal_transaksi) AS TAHUN, MONTH(t.tanggal_transaksi) AS BULAN,
SUM(tm.jumlah_minuman) AS JUMLAH_CUP
FROM transaksi t
JOIN transaksi_minuman tm ON t.id_transaksi = tm.tm_transaksi_id
JOIN menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
GROUP BY TAHUN, BULAN
ORDER BY TAHUN DESC, BULAN ASC;

-- 6.Berapa nilai rata-rata total belanja transaksi seluruh customer?
SELECT AVG(total_belanja) AS RATA_RATA_TOTAL_BELANJA
FROM (SELECT  c.id_customer, SUM(m.harga_minuman * tm.jumlah_minuman) AS total_belanja, m.harga_minuman, tm.jumlah_minuman
FROM customer c
JOIN membership mb ON c.id_customer = mb.m_id_customer
JOIN transaksi t ON c.id_customer = t.customer_id_customer
JOIN transaksi_minuman tm ON t.id_transaksi = tm.tm_transaksi_id
JOIN menu_minuman m ON tm.tm_menu_minuman_id = m.id_minuman
WHERE (m.harga_minuman * tm.jumlah_minuman) > 0
GROUP BY c.id_customer, t.id_transaksi) AS total_belanja_per_customer




