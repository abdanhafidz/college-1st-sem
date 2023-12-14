--Soal : Kita ingin mengetahui informasi tentang karyawan yang memiliki 
-- gaji di atas rata-rata gaji departemennya. Dalam hal ini, 
-- kita akan menggunakan nested query dengan subquery dalam pernyataan SELECT utama.



-- Membuat tabel Departements
CREATE TABLE Departments (
  DepartmentID INT PRIMARY KEY,
  DepartmentName VARCHAR(255) NOT NULL
);

-- Membuat tabel Employees
CREATE TABLE Employees (
  EmployeeID INT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  DepartmentID INT,
  Salary DECIMAL(10, 2),
  FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Menambahkan beberapa data ke tabel Departments
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT');

-- Menambahkan beberapa data ke tabel Employees
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID, Salary) VALUES
(1, 'John', 'Doe', 1, 50000),
(2, 'Jane', 'Smith', 1, 55000),
(3, 'Bob', 'Johnson', 2, 60000),
(4, 'Alice', 'Williams', 2, 62000),
(5, 'Charlie', 'Brown', 3, 70000),
(6, 'David', 'Jones', 3, 75000);



-- Query untuk mendapatkan karyawan dengan gaji di atas rata-rata gaji departemennya
SELECT
  e.EmployeeID,
  e.FirstName,
  e.LastName,
  e.Salary,
  e.DepartmentID
FROM
  Employees e
WHERE
  e.Salary > (
    SELECT
      AVG(e2.Salary)
    FROM
      Employees e2
    WHERE
      e2.DepartmentID = e.DepartmentID
  );