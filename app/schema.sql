DROP TABLE IF EXISTS collectionlist;
DROP TABLE IF EXISTS wishlist;

CREATE TABLE collectionlist (
	funkoname TEXT NOT NULL PRIMARY KEY,
	funkonum INTEGER NOT NULL PRIMARY KEY,
	funkoseries TEXT NOT NULL PRIMARY KEY,
	store TEXT
);

CREATE TABLE wishlist (
	funkoname TEXT NOT NULL PRIMARY KEY,
	funkonum INTEGER NOT NULL PRIMARY KEY,
	funkoseries TEXT NOT NULL PRIMARY KEY,
	price DECIMAL(5, 2),
	store TEXT
);

INSERT INTO collectionlist (funkoname, funkonum, funkoseries, store, price) values ('Sailor Moon (w/ Moon Stick & Luna)', 90, 'Pop! Animation: Sailor Moon', 12.00, 'Hot Topic');
INSERT INTO collectionlist (funkoname, funkonum, funkoseries, store, price) values ('Sailor Mercury', 91, 'Pop! Animation: Sailor Moon', 10.00, 'Gamestop');
