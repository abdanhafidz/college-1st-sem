-- 7.Dapatkan data customer dengan rata-rata total belanja lebih dari rata-rata total belanja
-- seluruh customer. Tampilkan kolom id customer, nama customer, dan total belanja!
SELECT * FROM;
-- 8.Tampilkan data customer yang tidak terdaftar sebagai membership!
SELECT cus.id_customer
FROM customer cus
WHERE cus.id_customer NOT IN (SELECT m.m_id_customer FROM membership m);

-- 9.Berapakah jumlah customer yang pernah memesan minuman Latte?
SELECT COUNT(DISTINCT nama_customer) AS JUMLAH_CUSTOMER_LATTE
FROM (SELECT *
FROM customer
JOIN transaksi ON (id_customer = customer_id_customer)
JOIN transaksi_minuman ON (id_transaksi = tm_transaksi_id)
JOIN menu_minuman ON (tm_menu_minuman_id = id_minuman)) AS TABEL_MERGER
WHERE nama_minuman IN ('Latte')

-- 10.
SELECT nama_customer, GROUP_CONCAT(nama_minuman SEPARATOR '.') AS MENU_MINUMAN, SUM(jumlah_minuman)
FROM customer
JOIN transaksi ON (id_customer = customer_id_customer)
JOIN transaksi_minuman ON (id_transaksi = tm_transaksi_id)
JOIN menu_minuman ON (tm_menu_minuman_id = id_minuman)
WHERE nama_customer LIKE 'S%'
GROUP BY nama_customer