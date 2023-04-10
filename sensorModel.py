from pymongo import MongoClient
from bson.objectid import ObjectId

class SensorModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_sensor(self, name: str, value: int, unity: str, alarm: bool) -> str:
        try:
            result = self.collection.insert_one({"nomeSensor": name, "valorSensor": value, "unidadeMedida" : unity, "sensorAlarmado": alarm})
            sensor_id = str(result.inserted_id)
            print(f"Sensor {name} created with id: {sensor_id}")
            return sensor_id
        except Exception as error:
            print(f"An error occurred while creating sensor: {error}")
            return None

    def read_sensorValue_by_id(self, sensor_id: str) -> int:
        try:
            sensor = self.collection.find_one({"_id": ObjectId(sensor_id)})

            value = sensor["valorSensor"]
            if sensor:
                return value
            else:
                print(f"No sensor found with id {sensor_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading sensor: {error}")
            return None

    def read_sensorAlarm_by_id(self, sensor_id: str) -> bool:
        try:
            sensor = self.collection.find_one({"_id": ObjectId(sensor_id), "sensorAlarmado": True})
            if sensor:
                return True
            else:
                return False
        except Exception as error:
            print(f"An error occurred while reading sensor: {error}")
            return None

    def update_sensorValue(self, sensor_id: str, newValue: int) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(sensor_id)}, {"$set": {"valorSensor": newValue}})
            sensor = self.collection.find_one({"_id": ObjectId(sensor_id)})
            name = sensor["nomeSensor"]
            value = sensor["valorSensor"]

            if result.modified_count:
                print(f"Sensor {name} temperature: {value}")
            else:
                print(f"No sensor found with id {sensor_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating sensor: {error}")
            return None

    def update_sensorAlarm(self, sensor_id: str, setAlarm: bool) -> bool:
        try:
            result = self.collection.update_one({"_id": ObjectId(sensor_id)}, {"$set": {"sensorAlarmado": setAlarm}})
            sensor = self.collection.find_one({"_id": ObjectId(sensor_id)})
            name = sensor["nomeSensor"]
            set = sensor["sensorAlarmado"]
            if result.modified_count:
                print(f"Sensor {name} alarm set: {set}")
            else:
                print(f"No sensor found with id {name}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating sensor: {error}")
            return None

