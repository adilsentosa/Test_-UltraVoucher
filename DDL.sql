--membuat TABLE nama
CREATE TABLE nama (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES nama(id)
);
--memasukan data kedalam TABLE nama
INSERT INTO nama (id, name) VALUES
(1, 'Zaki'),
(2, 'Ilham'),
(3, 'Irwan'),
(4, 'Arka');
--mengupdate data pada TABLE nama (meambahkan parrent_id)
UPDATE nama SET parent_id = 2 WHERE id = 1;
UPDATE nama SET parent_id = 2 WHERE id = 3;
UPDATE nama SET parent_id = 3 WHERE id = 4;
--menampilkan data dengan LEFT JOIN
SELECT t1.id, t1.name, t2.name AS parent_name FROM nama t1 LEFT JOIN nama t2 ON t1.parent_id = t2.id;