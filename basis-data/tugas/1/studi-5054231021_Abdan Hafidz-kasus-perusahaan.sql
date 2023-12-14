CREATE TABLE Dept( 
    dno integer primary key, 
    dname varchar(20) NOT NULL, 
    dloc varchar(20) 
);

SELECT * FROM Dept;

INSERT INTO Dept VALUES (1,'Finance', 'main office');

SELECT * FROM Dept;

INSERT INTO Dept VALUES (2,'Sales', 'main office');

INSERT INTO Dept VALUES (3,'', 'main office');

INSERT INTO Dept VALUES (4,'Sales', 'main office');

SELECT * FROM Dept;

ALTER TABLE Dept
    ADD job_id integer;

SELECT * FROM Dept;

ALTER TABLE Dept 
    DROP COLUMN job_id;

ALTER TABLE Dept 
    ADD job_id integer;

ALTER TABLE Dept 
    MODIFY job_id char(1);

SELECT * FROM Dept;

INSERT INTO Dept VALUES (5,'Human Resource', 'branch 1', 'A');

SELECT * FROM Dept;

CREATE TABLE Employee( 
    empid char(2), 
    empname varchar(20), 
    primary key(empid) 
);

CREATE TABLE Dependent( 
    dp_id integer, 
    dp_name varchar(20) 
);

ALTER TABLE Dependent 
    Add constraint pk_dp Primary key (dp_id);

ALTER TABLE Employee 
    Add d_dno integer;

ALTER TABLE Employee 
    Add CONSTRAINT fk_dno FOREIGN KEY (d_dno) REFERENCES Dept(dno);

INSERT INTO Employee VALUES ('ab', 'Surya',1);

SELECT * FROM Employee;

SELECT Employee.empid, Employee.empname, Dept.dname  
FROM Employee, Dept 
WHERE Employee.d_dno = Dept.dno;

SELECT Employee.empname, Dept.dname  
FROM Employee, Dept 
WHERE Employee.d_dno = Dept.dno AND Employee.empname LIKE '%Surya%';

SELECT Employee.empname, Dept.dname  
FROM Employee, Dept 
WHERE Employee.d_dno = Dept.dno;

# Membuat tabel baru jenjang pendidikan
CREATE TABLE jenjang(
    kode_jenjang char(1) primary key,
    nama_jenjang varchar(20)
)
SELECT * FROM Employee
# Menambahkan atribut baru kode_jenjang pada data employee
ALTER TABLE Employee
    Add kode_jenjang integer;
ALTER TABLE Employee
    Add CONSTRAINT fk_kode_jenjang FOREIGN KEY (kode_jenjang) REFERENCES jenjang(kode_jenjang)