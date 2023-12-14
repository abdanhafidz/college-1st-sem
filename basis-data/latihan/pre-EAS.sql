-- Active: 1701418525680@@127.0.0.1@3306@pendahuluan

SELECT id_customer AS Kode_Customer, nama_customer AS Nama_Customer FROM customer;

SELECT COUNT(*) AS Jumlah_Minuman FROM menu_minuman;

SELECT tm.tm_transaksi_id,mm.nama_minuman FROM transaksi_minuman tm 
INNER JOIN menu_minuman mm ON tm.tm_menu_minuman_id = mm.id_minuman;

SELECT tm.tm_transaksi_id,mm.nama_minuman FROM transaksi_minuman tm 
LEFT JOIN menu_minuman mm ON tm.tm_menu_minuman_id = mm.id_minuman;

SELECT tm.tm_transaksi_id,mm.nama_minuman FROM transaksi_minuman tm 
RIGHT JOIN menu_minuman mm ON tm.tm_menu_minuman_id = mm.id_minuman;

SELECT COUNT(tm.tm_transaksi_id) AS JUMLAH_TRANSAKSI, tm.tm_menu_minuman_id AS ID_MINUMAN 
FROM transaksi_minuman tm
GROUP BY tm.tm_menu_minuman_id 
ORDER BY COUNT(tm.tm_transaksi_id);


SELECT COUNT(tm.tm_menu_minuman_id) AS JUMLAH_MINUMAN_DIBELI, tm.tm_transaksi_id AS ID_TRANSAKSI 
FROM transaksi_minuman tm
GROUP BY tm.tm_transaksi_id

SELECT tm.tm_transaksi_id,SUM(mm.harga_minuman) AS TOTAL_HARGA FROM transaksi_minuman tm 
INNER JOIN menu_minuman mm ON tm.tm_menu_minuman_id = mm.id_minuman
GROUP BY tm.tm_transaksi_id 
 ;