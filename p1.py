# def print_name(name):
#     print("The given name is ",name)

# def sum(x,y=0,z=0):
#     print(x+y+z)
 
# def toCaps(name):
#     print(name.upper())

# name=input()
# print_name(name)
# toCaps(name)
# sum(1,2,4)

# class Main:
#     def sum(x,y):
#         return x+y
#     def sub(x,y):
#         return x-y
#     def pro(x,y):
#         return x*y
#     def div(x,y):
#         return x/y

   
#     print(sum(1,2))
#     print(sub(4,2))
#     print(pro(2,4))
#     print(div(6,3))


# class Main:
#     def animal(self,name,age):
#         self.name=name 
#         self.age=age
#     def sound(self,sound):
#         self.sound=sound

# class Jungle:
#     m=Main()
#     name_of_animal=m.name="sanjay"
#     age_of_animal=m.age=69
#     sound_of_animal=m.sound="aaaaaa"
#     print(name_of_animal,age_of_animal,sound_of_animal)

# with open("example.txt",'w') as file:
#     file.write("hiii")
# with open('example.txt','r') as file:
#     content=file.read()
# print(content)
# with open ('example.txt','a') as file:
#     file.write('vanakooo') 
# with open('example.txt','r') as file:
#     file.seek(1)
#     content=file.read()
# print(content)

# import json
# data={'name':'pk','age':18}
# json_string=json.dumps(data)
# print(json_string)
# Json='{"name":"vijay","age":"96"}'
# data_json=json.loads(Json)
# print(data_json)
# with open('out.json','w') as file:
#     json.dump(data,file)
# with open('out.json','r') as file:
#     content=json.load(file)
# print(content)

# import requests


# url = 'https://jsonplaceholder.typicode.com/posts'


# data = {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1
# }


# response = requests.post(url, json=data)


# if response.status_code == 201:  
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")


# url = 'https://jsonplaceholder.typicode.com/posts'

# data = {
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1
# }


# response = requests.post(url, json=data)

# if response.status_code == 201:  
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")
#msg even handling using mqtt

# import paho.mqtt.client as mqtt
# import datetime as dt

# # events to handle the different callbacks
# def on_connect(client, user_data, flag, rc):
#     # counter = 0
#     mqttc.subscribe('mqtt_practice',0)
#     mqttc.publish('mqtt_practice',"Connection Successful..",0)
#     # counter += 1
   
# def on_message(client, user_data, message):
#     print(f"{message.payload} : is published on {message.topic}\n") # to format the string f-string is used here

# def on_subscribe(client, obj, mid, granted_qos):
#     print(f"Subscribed: {mid} {granted_qos}")

# def on_publish(client, user_data, message_id):
#     print(f"publishing message with id: {message_id}")

# mqttc = mqtt.Client('mqtt_practice' + str(dt.datetime.now())) # str() is used to create a new string object here as every mqtt client needs a unique name.

# # First event is on_connect callback function
# mqttc.on_connect = on_connect

# # Once the connection is successful then the following callbacks will get triggered
# mqttc.on_subscribe = on_subscribe
# mqttc.on_publish = on_publish  
# mqttc.on_message = on_message

# # Connecting the mqtt client
# x = mqttc.connect('20.219.125.196', 1883) # here using connect method that takes IP address/website address and PORT number
# print(x)

# if x == 0:
#     print("success")
# else:
#     print("Failed")
# mqttc.loop_forever()

# while loop for iterating the loop forever

# while rc == 0:
#    print("connection is successfully established")
#    rc = mqttc.loop_forever()
   

# ultra sonic sensor
# import paho.mqtt.client as mqtt  
# import datetime as dt

# #Events
# def on_message_distance(edge, userdata, msg):
#    #   global counter
#    #   counter+=1
#     print('Received a new distance_value data:' + str(msg.payload.decode('utf-8')))

# def on_subscribe_success(mosq, obj, mid,granted_qos):
#     edge.on_publish = on_publish_stp_success
#     edge.publish('UTEST4/BOOT','IN:ULT:00004:CM:STP')  

# def on_publish_stp_success(mosq, obj, mid):
   
#    edge.on_publish = on_publish_srt_success
#    edge.publish('UTEST4/BOOT','IN:ULT:00004:CM:SRT')

# def on_publish_srt_success(mosq, obj, mid):
#    print("mid: " + str(mid))

# def on_connect(edge, userdata, flags, rc):
#     if rc == 0:
#        print("Connected to MQTT Broker!")
#        edge.message_callback_add('UTEST4/IN/ULT:00004', on_message_distance)
#        edge.on_subscribe = on_subscribe_success
#        edge.subscribe('UTEST4/IN/ULT:00004')
#     else:
#        print("Failed to connect, return code %d\n", rc)

# # Starting Point
# edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))  
# edge.on_connect = on_connect  
# edge.connect('20.219.125.196', 1883)                
# edge.loop_forever()

# import paho.mqtt.client as mqtt
# import datetime as dt


# def on_message_TOUCH_SENSOR(edge, userdata, msg):
   
#     print('Received a new WEIGTH data:' + str(msg.payload.decode('utf-8')))

# def on_subscribe_success(mosq, obj, mid, granted_qos):
#     edge.on_publish = on_publish_stp_success
#     edge.publish('LOAD CELL1/BOOT', 'IN:LDC:00019:KG:STP')

# def on_publish_stp_success(mosq, obj, mid):
#     edge.on_publish = on_publish_srt_success
#     edge.publish('LOAD CELL1/BOOT', 'IN:LDC:00019:KG:SRT')

# def on_publish_srt_success(mosq, obj, mid):
#     print("mid: " + str(mid))

# def on_connect(edge, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to MQTT Broker!")
#         edge.message_callback_add('LOAD CELL1/IN/LDC:00019', on_message_TOUCH_SENSOR)
#         edge.on_subscribe = on_subscribe_success
#         edge.subscribe('LOAD CELL1/IN/LDC:00019')
#     else:
#         print("Failed to connect, return code %d\n" % rc)

# # Starting Point
# edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
# edge.on_connect = on_connect
# edge.connect('20.219.125.196', 1883)
# edge.loop_forever()


# import paho.mqtt.client as mqtt
# import datetime as dt
# import re

# counter = 1


# def on_message_MOIST(edge, userdata, msg):
#     global counter
#     a = str(msg.payload.decode('utf-8'))
#     data = a.split(":")
#     dis = re.findall("\d+", data[3])

#     if len(dis) <= 0:
#         dis = -1  # Set to -1 or another value representing no data
#     else:
#         dis = int(dis[0])

#     if counter % 10 == 0:
#         if dis >= 0:
#             lcd_message = f" Moisture:LCD:00016:N/A:{dis}"
#             edge.publish('LT3/OUT/LCD:00016', lcd_message)

#     counter += 1




# def on_subscribe_success(mosq, obj, mid, granted_qos):
#     edge.on_publish = on_publish_stp_success
#     edge.publish('IOTKIT026/BOOT', 'IN:MOIS:00001:N/A:STP')
#     edge.publish('LT3/BOOT','OUT:LCD:00016:N/A:STP')
# def on_publish_stp_success(mosq, obj, mid):
#     edge.on_publish = on_publish_srt_success
#     edge.publish('IOTKIT026/BOOT', 'IN:MOIS:00001:N/A:SRT')
#     edge.publish('LT2/BOOT','OUT:LCD:00016:N/A:SRT')

# def on_publish_srt_success(mosq, obj, mid):
#     print("mid: " + str(mid))

# def on_connect(edge, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to MQTT Broker!")
#         edge.message_callback_add('IOTKIT026/IN/MOIS:00001', on_message_MOIST)
#         edge.on_subscribe = on_subscribe_success
#         edge.subscribe('IOTKIT026/IN/MOIS:00001')
#     else:
#         print("Failed to connect, return code %d\n" % rc)

# # Starting Point
# edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
# edge.on_connect = on_connect
# edge.connect('20.219.125.196', 1883)
# edge.loop_forever()


# import paho.mqtt.client as mqtt
# import datetime as dt
# import re

# counter_moisture = 1
# counter_temperature = 1
# counter_humidity = 1

# def on_message_moisture(edge, userdata, msg):
#     global counter_moisture
#     handle_sensor_data(edge, msg, 'MOIS', counter_moisture)
#     counter_moisture += 1

# def on_message_temperature(edge, userdata, msg):
#     global counter_temperature
#     handle_sensor_data(edge, msg, 'TEMP', counter_temperature)
#     counter_temperature += 1

# def on_message_humidity(edge, userdata, msg):
#     global counter_humidity
#     handle_sensor_data(edge, msg, 'HMD', counter_humidity)
#     counter_humidity += 1

# def handle_sensor_data(edge, msg, sensor_type, counter):
#     data = str(msg.payload.decode('utf-8')).split(":")
#     value = extract_numeric_value(data[3])

#     if counter % 10 == 0:
#         if value >= 0:
#             lcd_message = f" {sensor_type.capitalize()}:LCD:00016:N/A:{value}"
#             edge.publish('LT2/OUT/LCD:00016', lcd_message)

# def extract_numeric_value(data):
#     numeric_value = re.findall("\d+", data)
#     return int(numeric_value[0]) if numeric_value else -1

# def on_subscribe_success(mosq, obj, mid, granted_qos):
#     edge.on_publish = on_publish_stp_success
#     edge.publish('IOTKIT026/BOOT', 'IN:MOIS:00001:N/A:STP')
#     edge.publish('TSTEST2/BOOT', 'IN:TEMP:00008:N/A:STP')
#     edge.publish('T3-TMKSMK/BOOT', 'IN:HMD:00016:N/A:STP')

#     edge.publish('LT2/BOOT', 'OUT:LCD:00016:N/A:STP')

# def on_publish_stp_success(mosq, obj, mid):
#     edge.on_publish = on_publish_srt_success
#     edge.publish('IOTKIT026/BOOT', 'IN:MOIS:00001:N/A:SRT')
#     edge.publish('T3-TMKSMK/BOOT', 'IN:TEMP:00008:N/A:SRT')
#     edge.publish('T3-TMKSMK/BOOT', 'IN:HMD:000016:N/A:SRT')
#     edge.publish('LT2/BOOT', 'OUT:LCD:00016:N/A:SRT')

# def on_publish_srt_success(mosq, obj, mid):
#     print("mid: " + str(mid))

# def on_connect(edge, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to MQTT Broker!")
#         edge.message_callback_add('IOTKIT026/IN/MOIS:00001', on_message_moisture)
#         edge.message_callback_add('T3-TMKSMK/IN/TEMP:00008', on_message_temperature)
#         edge.message_callback_add('T3-TMKSMK/IN/HMD:00016', on_message_humidity)
#         edge.on_subscribe = on_subscribe_success
#         edge.subscribe('IOTKIT026/IN/MOIS:00001')
#         edge.subscribe('T3-TMKSMK/IN/TEMP:00008')
#         edge.subscribe('T3-TMKSMK/IN/HMD:00016')
#     else:
#         print("Failed to connect, return code %d\n" % rc)

# # Starting Point
# edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
# edge.on_connect = on_connect
# edge.connect('20.219.125.196', 1883)
# edge.loop_forever()



import paho.mqtt.client as mqtt
import datetime as dt
import re

counter_moisture = 1
counter_temperature = 1
counter_humidity = 1

def on_message_moisture(edge, userdata, msg):
    global counter_moisture
    handle_sensor_data(edge, msg, 'MOIS', counter_moisture)
    counter_moisture += 1

def on_message_temperature(edge, userdata, msg):
    global counter_temperature
    handle_sensor_data(edge, msg, 'TEMP', counter_temperature)
    counter_temperature += 1

# def on_message_humidity(edge, userdata, msg):
#     global counter_humidity
#     handle_sensor_data(edge, msg, 'HMD', counter_humidity)
#     counter_humidity += 1

def handle_sensor_data(edge, msg, sensor_type, counter):
    data = str(msg.payload.decode('utf-8')).split(":")
    value = extract_numeric_value(data[3])

    if counter % 10 == 0:
        if value >= 0:
            lcd_message = f" {sensor_type.capitalize()}:LCD:00016:N/A:{value}"
            edge.publish('LT3/OUT/LCD:00016', lcd_message)

def extract_numeric_value(data):
    numeric_value = re.findall("\d+", data)
    return int(numeric_value[0]) if numeric_value else -1

# def determine_weather(moisture, temperature, humidity):
#     if moisture < 20:
#         return "Dry Weather"
#     elif temperature > 25 and humidity < 50:
#         return "Hot and Dry Weather"
#     elif temperature > 25 and humidity >= 50:
#         return "Hot and Humid Weather"
#     elif temperature <= 25 and humidity < 50:
#         return "Mild Weather"
#     elif temperature <= 25 and humidity >= 50:
#         return "Mild and Humid Weather"
#     else:
#         return "Weather Condition Unknown"

def on_subscribe_success(mosq, obj, mid, granted_qos):
    edge.on_publish = on_publish_stp_success
    edge.publish('IOTKIT028/BOOT', 'IN:MOIS:00001:N/A:STP')
    edge.publish('TSTEST2/BOOT', 'IN:TEMP:00008:N/A:STP')
    # edge.publish('TSTEST2/BOOT', 'IN:HMD:00008:N/A:STP')
    edge.publish('LT3/BOOT', 'OUT:LCD:00016:N/A:STP')

def on_publish_stp_success(mosq, obj, mid):
    edge.on_publish = on_publish_srt_success
    edge.publish('IOTKIT028/BOOT', 'IN:MOIS:00001:N/A:SRT')
    edge.publish('TSTEST2/BOOT', 'IN:TEMP:00008:N/A:SRT')
    # edge.publish('TSTEST2/BOOT', 'IN:HMD:00008:N/A:SRT')
    edge.publish('LT3/BOOT', 'OUT:LCD:00016:N/A:SRT')

def on_publish_srt_success(mosq, obj, mid):
    print("mid: " + str(mid))

def on_connect(edge, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        edge.message_callback_add('IOTKIT028/IN/MOIS:00001', on_message_moisture)
        edge.message_callback_add('TSTEST2/IN/TEMP:00008', on_message_temperature)
        # edge.message_callback_add('TSTEST2/IN/HMD:00008', on_message_humidity)
        edge.on_subscribe = on_subscribe_success
        edge.subscribe('IOTKIT028/IN/MOIS:00001')
        edge.subscribe('TSTEST2/IN/TEMP:00008')
        # edge.subscribe('TSTEST2/IN/HMD:00008')5
    else:
        print("Failed to connect, return code %d\n" % rc)

# Starting Point
edge = mqtt.Client('eds_demoiot1' + str(dt.datetime.now()))
edge.on_connect = on_connect
edge.connect('20.219.125.196', 1883)
edge.loop_forever()





