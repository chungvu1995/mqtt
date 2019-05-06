import pymysql
import json

def Sensor(jsonData)
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict('sensorID')
	Date_Time = json_Dict('Date_and_Time')
	Temperature = json_Dict('Temperature')
	Humidity = json_Dict('Humidity')

	db=pymysql.connect("localhost","mangcambien-user","123456","mangcambien")

	cursor = db.cursor()

	sql="""insert into sensors(SensorID,Date_time,Temperature,Humidity)
			values (%s,%s,%s,%s)"""

	val = (SensorID,Date_time,Temperature,Humidity)
	cursor.execute(sql,val)
	db.commit()
	print("sensor create new values")
	print("------------")

	db.close()
	
