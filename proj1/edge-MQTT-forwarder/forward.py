import paho.mqtt.client as mqtt
import sys
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime

credentials = service_account.Credentials.from_service_account_file('thinking-field-287800-1cde00ec739e.json')

LOCAL_MQTT_HOST   = '192.168.2.52'
LOCAL_MQTT_PORT   = 1883
LOCAL_MQTT_TOPIC  = "camera/found_face"

def on_connect_local(client, userdata, flags, rc):
  print("connected to local broker with rc: " + str(rc))
  
def on_message(client,userdata, msg):
  try:
    print("message received")
    print(msg.payload)
    dateTimeObj = datetime.now()
    print(dateTimeObj)

    # Construct a BigQuery client object.
    client = bigquery.Client(credentials=credentials)

    table_id = "thinking-field-287800.ML_CONTROL.timeline"

    rows_to_insert = [{u"insert_time": str(dateTimeObj), u"emotion_int": 1, u"emotion_name": str(msg.payload)},]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
      print("New rows have been added.")
    else:
      print("Encountered errors while inserting rows: {}".format(errors))


  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.on_message = on_message

local_mqttclient.connect(LOCAL_MQTT_HOST,LOCAL_MQTT_PORT,60)
local_mqttclient.subscribe(LOCAL_MQTT_TOPIC,qos=2)

# go into a loop
local_mqttclient.loop_forever()