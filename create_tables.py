import pymysql

db=pymysql.connect("localhost","mangcambien-user","123456","mangcambien")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS sensors")

sql ="""create table sensors(
	id int(10) primary key auto_increment,
	sensorID char(10) not null,
	Temperature int(10) not null,
	Humidity int(3) not null,
	Date_and_Time char(30) not null)"""
cursor.execute(sql)
db.close()
