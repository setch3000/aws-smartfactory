# OPC-UA Client with GreenGrass from Dongwoo John Ku
import logging
import platform
import sys
import greengrasssdk
import time
import configparser
from opcua import Client

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client("iot-data")

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

# Creating a OPC UA client and acquire setting values from communication.conf file
# OPC-UA Connection information should have been written on the file be before running this program.
config = configparser.ConfigParser()
config.read('./communication.conf')
end_point = config.get('MAIN', 'opcua_server_endpoint')
logging_interval = int(config.get('MAIN', 'logging_interval'))
opc_nodeid = config.get('MAIN', 'opc_nodeid')
opcua_client = Client(end_point)


def greengrass_opcua_run():
    while True:
        try:
            logger.info('connection tried')
            client.publish(topic="turck/log", queueFullPolicy="AllOrException", payload='connection tried',)
            opcua_client.connect()
        except:
            logger.error('connection failed')
            time.sleep(logging_interval)
        else:
            try:
                opcua_client.load_type_definitions()  # load definition of server specific structures/extension objects
                stationList = opcua_client.get_node(opc_nodeid).get_children()

                for station in stationList:
                    # get station name
                    topicStation = str(station.get_browse_name()).split(":")[1][:-1]
                    # get station's children which are variables
                    varList = station.get_children()
                    mqttMessage =''
                    for var in varList :
                        # get tag name and tag value
                        tagName =str(var.get_browse_name()).split(":")[1][:-1]
                        tagValue =str(var.get_value())
                        logData = ([tagName, tagValue])

                        # make mqtt message format
                        if var != varList[-1]:
                            logData = ":".join(logData) + ', '
                            mqttMessage += logData
                        else:
                            logData = ":".join(logData)
                            mqttMessage += logData
                            mqttMessage = '{' + mqttMessage + '}'

                            try:
                                client.publish(
                                    topic="turck/" + topicStation ,
                                    queueFullPolicy="AllOrException",
                                    payload=mqttMessage,
                                )
                            except Exception as e:
                                logger.error("Failed to publish message: " + repr(e))
                            else:
                                logger.info("Successed to published message of " + topicStation)
            except:
                logger.info('opc-ua error occur while connection')
                client.publish(topic="turck/log", queueFullPolicy="AllOrException", payload='opc-ua error occur while connection',)
            else:
                logger.info('MQTT publishing is succeed')
                client.publish(topic="turck/log", queueFullPolicy="AllOrException", payload='MQTT publishing is succeed', )
            finally:
                time.sleep(logging_interval / 1000)

# Start executing the function above
greengrass_opcua_run()

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    logger.info('function handler')
    client.publish(topic="turck/log", queueFullPolicy="AllOrException", payload='function handler', )
    return
