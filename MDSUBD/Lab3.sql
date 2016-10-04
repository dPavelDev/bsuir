CREATE TABLE Organizations (
	organizationId int AUTO_INCREMENT,
	taxNumber int(15) NOT NULL,
	name varchar(20) NOT NULL,
	boss varchar(20) NOT NULL,
	adress varchar(80) NOT NULL,
	phone int(10) NOT NULL,
	PRIMARY KEY (organizationId)
);

CREATE TABLE Clients (
	managerClientId int AUTO_INCREMENT,
	manager varchar(20) NOT NULL,
	phone int(10) NOT NULL,
	fax int(15) NOT NULL,
	organizationId int NOT NULL,
	PRIMARY KEY (managerClientId),
	FOREIGN KEY (organizationId) REFERENCES Organizations (organizationId)
);

CREATE TABLE OrdersStatus (
	statusId int AUTO_INCREMENT,
	status varchar(20) NOT NULL,
	PRIMARY KEY (statusId)
);

CREATE TABLE Employees (
	employeeId int AUTO_INCREMENT,
	name varchar(20) NOT NULL,
	position varchar(15) NOT NULL,
	phone int(10) NOT NULL,
	PRIMARY KEY (employeeId)
);

CREATE TABLE Orders (
	orderId int AUTO_INCREMENT,
	invoiceNumber int(15) NOT NULL,
	orderDate date NOT NULL,
	totalAmount int NOT NULL,
	shipmentDate date NOT NULL,
	comments text,
	managerClientId int NOT NULL,
	statusId int NOT NULL,
	employeeId int NOT NULL,
	PRIMARY KEY (orderId),
	FOREIGN KEY (managerClientId) REFERENCES Clients (managerClientId),
	FOREIGN KEY (statusId) REFERENCES OrdersStatus (statusId),
	FOREIGN KEY (employeeId) REFERENCES Employees (employeeId)
);

CREATE TABLE Goods (
	goodId int AUTO_INCREMENT,
	name varchar(20) NOT NULL,
	PRIMARY KEY (goodId)
);

CREATE TABLE Stock (
	stockId int AUTO_INCREMENT,
	spec varchar(20) NOT NULL,
	price int(15) NOT NULL,
	residue int(15) NOT NULL,
	place varchar(20) NOT NULL,
	goodId int NOT NULL,
	PRIMARY KEY (stockId),
	FOREIGN KEY (goodId) REFERENCES Goods (goodId)
);

CREATE TABLE StockOrders (
	orderId int NOT NULL,
	stockId int NOT NULL,
	amount int NOT NULL,
	sellingPrice int(15) NOT NULL,
	FOREIGN KEY (orderId) REFERENCES Orders (orderId),
	FOREIGN KEY (stockId) REFERENCES Stock (stockId),
	PRIMARY KEY (orderId, stockId)
);

CREATE TABLE Suppliers (
	managerSupplierId int AUTO_INCREMENT,
	manager varchar(20) NOT NULL,
	phone int(10) NOT NULL,
	fax int(15) NOT NULL,
	organizationId int NOT NULL,
	PRIMARY KEY (managerSupplierId),
	FOREIGN KEY (organizationId) REFERENCES Organizations (organizationId)
);

CREATE TABLE ArriveStock (
	stockId int NOT NULL,
	arriveDate date NOT NULL,
	managerSupplierId int NOT NULL,
	invoiceNumber int NOT NULL,
	amount int NOT NULL,
	price int(15) NOT NULL,
	inspector varchar(20) NOT NULL,
	FOREIGN KEY (stockId) REFERENCES Stock (stockId),
	PRIMARY KEY (stockId, arriveDate)
);
