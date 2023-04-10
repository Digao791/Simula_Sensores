from database import Database
from random import randint
import sensorModel
import threading
import time

bancoit = Database(database="bancoit", collection="sensores")
bancoit.resetDatabase()


Sensor_Model = sensorModel.SensorModel(bancoit)

sensor1_id = Sensor_Model.create_sensor("Sensor_1", 0, "celcius", False)
sensor2_id = Sensor_Model.create_sensor("Sensor_2", 0, "celcius", False)
sensor3_id = Sensor_Model.create_sensor("Sensor_3", 0, "celcius", False)

def Primeiro_Sensor(id, tempo):
    while not(Sensor_Model.read_sensorAlarm_by_id(id)):
        newValue = randint(30,40)
        Sensor_Model.update_sensorValue(id,newValue)
        time.sleep(tempo)

        if Sensor_Model.read_sensorValue_by_id(id) > 38:
            Sensor_Model.update_sensorAlarm(id,True)

    while True:
        print("Atenção! Temperatura muito alta! Verificar Sensor 1!")
        time.sleep(10)


def Segundo_Sensor(id, tempo):
    while not(Sensor_Model.read_sensorAlarm_by_id(id)):
        newValue = randint(30, 40)
        Sensor_Model.update_sensorValue(id, newValue)
        time.sleep(tempo)

        if Sensor_Model.read_sensorValue_by_id(id) > 38:
            Sensor_Model.update_sensorAlarm(id, True)

    while True:
        print("Atenção! Temperatura muito alta! Verificar Sensor 2!")
        time.sleep(10)


def Terceiro_Sensor(id, tempo):
    while not(Sensor_Model.read_sensorAlarm_by_id(id)):
        newValue = randint(30, 40)
        Sensor_Model.update_sensorValue(id, newValue)
        time.sleep(tempo)

        if Sensor_Model.read_sensorValue_by_id(id) > 38:
            Sensor_Model.update_sensorAlarm(id, True)

    while True:
        print("Atenção! Temperatura muito alta! Verificar Sensor 3!")
        time.sleep(10)








first_sensor = threading.Thread(target=Primeiro_Sensor, args=(sensor1_id, 5))
first_sensor.start()

second_sensor = threading.Thread(target=Segundo_Sensor, args=(sensor2_id, 3))
second_sensor.start()

third_sensor = threading.Thread(target=Terceiro_Sensor, args=(sensor3_id, 8))
third_sensor.start()






