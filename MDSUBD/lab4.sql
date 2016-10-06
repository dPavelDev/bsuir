-- 1.1 Добавить новую организацию с названием «ОАО Белвест»
-- 1.2 Назначить Руководителем «ОАО Белвест» Смирнова В.Л.

INSERT INTO Organizations(taxNumber, name, boss, adress, phone) VALUES (1536006897, "OAO Belwest", "Smirnov V.L.", "Ul. Pushkina, dom Kolotushkina", 234011);

-- 1.3	Добавить на склад 5 единиц товара с названием «Сапоги меховые»

INSERT INTO Goods(name) VALUES ("Sapogi mehovye");
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("Obuv", 1150000, 5, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye"));

-- 1.4	Создать две произвольные организации, одна из которых будет поставщиком, а вторая клиетом

INSERT INTO Organizations(taxNumber, name, boss, adress, phone) VALUES (2097856845, "PinskDrev", "Ivanov I.I.", "Ul. Suvorova 16/2", 235695);
INSERT INTO Organizations(taxNumber, name, boss, adress, phone) VALUES (2300472337, "Srednjaja shkola 3", "Romanchuk A.M.", "Ul. Sovetskaja 13", 245520);
INSERT INTO Suppliers(manager, phone, fax, organizationId) VALUES ("Kuzemin S.P.", 235690, 2359423, (SELECT organizationId FROM Organizations WHERE name = "PinskDrev"));
INSERT INTO Clients(manager, phone, fax, organizationId) VALUES ("Sirut A.D.", 245525, 2342103, (SELECT organizationId FROM Organizations WHERE name = "Srednjaja shkola 3"));

-- 1.5	Сформировать два заказа на товар «Сапоги меховые»
INSERT INTO Clients(manager, phone, fax, organizationId) VALUES ("Kozheckij P. V.", 205985, 3895265, (SELECT organizationId FROM Organizations WHERE name = "OAO Belwest"));

INSERT INTO OrdersStatus(status) VALUES ("Ne sformirovan");
INSERT INTO OrdersStatus(status) VALUES ("Sformirovan");
INSERT INTO OrdersStatus(status) VALUES ("Otpravlen");

INSERT INTO Employees(name, position, phone) VALUES ("Sosnov", "deliveryman", 5429238);
INSERT INTO Employees(name, position, phone) VALUES ("Valjuk", "deliveryman", 5429238);

 -- Первый заказ

INSERT INTO Orders(invoiceNumber, orderDate, totalAmount, shipmentDate, comments, managerClientId, statusId, employeeId) VALUES (532823123, "2015-10-24", 0, "2015-10-25", "Zakaz dostavjat vo vtoroj polovine dnja", (SELECT managerClientId FROM Clients WHERE manager = "Kozheckij P. V."), (SELECT statusId FROM OrdersStatus WHERE status = "Ne sformirovan"), (SELECT employeeId FROM Employees WHERE name = "Sosnov"));

INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 532823123), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye") * 1.15));


UPDATE Orders SET totalAmount = (SELECT sum(amount * sellingPrice) FROM StockOrders WHERE StockOrders.orderId = Orders.orderId), statusId = (SELECT statusId FROM OrdersStatus WHERE status = "Sformirovan") WHERE invoiceNumber = 532823123;


UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 532823123)) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye");

			-- Второй заказ

INSERT INTO Orders(invoiceNumber, orderDate, totalAmount, shipmentDate, comments, managerClientId, statusId, employeeId) VALUES (1023003123, "2015-10-26", 0, "2015-10-28", "Zakaz dostavjat v pervoj polovine dnja", (SELECT managerClientId FROM Clients WHERE manager = "Kozheckij P. V."), (SELECT statusId FROM OrdersStatus WHERE status = "Ne sformirovan"), (SELECT employeeId FROM Employees WHERE name = "Valjuk"));

INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 1023003123), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye")), 3, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye") * 1.15));

UPDATE Orders SET totalAmount = (SELECT sum(amount * sellingPrice) FROM StockOrders), statusId = (SELECT statusId FROM OrdersStatus WHERE status = "Sformirovan") WHERE invoiceNumber = 1023003123;

UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 1023003123)) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Sapogi mehovye");

-- 1.6	Удалить все заказы
DELETE FROM StockOrders;
DELETE FROM Stock;
DELETE FROM Goods;
DELETE FROM Orders;

-- 1.7	Наполнить таблицы таким образом, чтобы в базе данных находилось не менее трех заказов, включающих в себя не менее четырех товаров каждый

INSERT INTO Goods(name) VALUES ("Shoes");
INSERT INTO Goods(name) VALUES ("Shorts");
INSERT INTO Goods(name) VALUES ("Tights");
INSERT INTO Goods(name) VALUES ("Jakets");
INSERT INTO Goods(name) VALUES ("Socks");
INSERT INTO Goods(name) VALUES ("Gloves");
INSERT INTO Goods(name) VALUES ("T Shorts");
INSERT INTO Goods(name) VALUES ("Tops");
INSERT INTO Goods(name) VALUES ("Head Wear");

INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("EN435-32", 2310000, 25, "Ul. Shirokaya 14", (SELECT goodId FROM Goods WHERE name = "Shoes"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("120ND-3", 875000, 15, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Shorts"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("4B32-32C", 1110000, 12, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Tights"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("UD2318", 950000, 5, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Jakets"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("II3212-5", 85000, 18, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Socks"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("8231A3F", 765000, 4, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Gloves"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("PAP352", 1200000, 32, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "T Shorts"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("ZX32M3", 850000, 10, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Tops"));
INSERT INTO Stock(spec, price, residue, place, goodId) VALUES ("MX932-1", 324000, 22, "Ul. Kalinovskogo 28", (SELECT goodId FROM Goods WHERE name = "Head Wear"));


-- Формируем первый заказ

INSERT INTO Orders(invoiceNumber, orderDate, totalAmount, shipmentDate, comments, managerClientId, statusId, employeeId) VALUES (57319523, "2015-10-20", 0, "2015-10-29", "The next time you purchase a 10% discount", (SELECT managerClientId FROM Clients WHERE manager = "Sirut A.D."), (SELECT statusId FROM OrdersStatus WHERE status = "Ne sformirovan"), (SELECT employeeId FROM Employees WHERE name = "Valjuk"));

INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 57319523), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 57319523), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Tights")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Tights") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 57319523), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts")), 2, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 57319523), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves") * 1.15));

UPDATE Orders SET totalAmount = (SELECT sum(amount * sellingPrice) FROM StockOrders WHERE StockOrders.orderId = Orders.orderId), statusId = (SELECT statusId FROM OrdersStatus WHERE status = "Sformirovan") WHERE invoiceNumber = 57319523;

UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Tights");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves");


-- Формируем второй заказ

INSERT INTO Orders(invoiceNumber, orderDate, totalAmount, shipmentDate, comments, managerClientId, statusId, employeeId) VALUES (8429001, "2015-09-12", 0, "2015-10-5", "Shipping is free", (SELECT managerClientId FROM Clients WHERE manager = "Sirut A.D."), (SELECT statusId FROM OrdersStatus WHERE status = "Ne sformirovan"), (SELECT employeeId FROM Employees WHERE name = "Sosnov"));

INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 8429001), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes")), 2, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 8429001), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Socks")), 4, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Socks") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 8429001), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts")), 2, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 8429001), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves")), 2, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 8429001), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Jakets")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Jakets") * 1.15));

UPDATE Orders SET totalAmount = (SELECT sum(amount * sellingPrice) FROM StockOrders WHERE StockOrders.orderId = Orders.orderId), statusId = (SELECT statusId FROM OrdersStatus WHERE status = "Sformirovan") WHERE invoiceNumber = 8429001;

UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 8429001) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 8429001) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Socks");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 8429001) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 8429001) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 8429001) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Jakets");


-- Формируем третий заказ

INSERT INTO Orders(invoiceNumber, orderDate, totalAmount, shipmentDate, comments, managerClientId, statusId, employeeId) VALUES (11042321, "2015-09-25", 0, "2015-10-15", "Shipping $10", (SELECT managerClientId FROM Clients WHERE manager = "Kozheckij P. V."), (SELECT statusId FROM OrdersStatus WHERE status = "Ne sformirovan"), (SELECT employeeId FROM Employees WHERE name = "Valjuk"));

INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 11042321), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 11042321), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Socks")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Socks") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 11042321), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 11042321), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Tops")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves") * 1.15));
INSERT INTO StockOrders(orderId, stockId, amount, sellingPrice) VALUES ((SELECT orderId FROM Orders WHERE invoiceNumber = 11042321), (SELECT stockId FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Jakets")), 1, (SELECT price FROM Stock WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Jakets") * 1.15));

UPDATE Orders SET totalAmount = (SELECT sum(amount * sellingPrice) FROM StockOrders WHERE StockOrders.orderId = Orders.orderId), statusId = (SELECT statusId FROM OrdersStatus WHERE status = "Sformirovan") WHERE invoiceNumber = 11042321;

UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 11042321) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Shoes");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 11042321) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Socks");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 11042321) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "T Shorts");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 11042321) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Gloves");
UPDATE Stock SET residue = residue - (SELECT amount FROM StockOrders WHERE orderId = (SELECT orderId FROM Orders WHERE invoiceNumber = 11042321) AND StockOrders.stockId = Stock.stockId) WHERE goodId = (SELECT goodId FROM Goods WHERE name = "Jakets");
