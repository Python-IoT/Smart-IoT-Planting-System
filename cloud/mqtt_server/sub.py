#!/usr/bin/env python
import logging
import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1, QOS_2

async def sub_test():
  C = MQTTClient()
  await C.connect('mqtt://192.168.0.4:1883/')
  await C.subscribe([
          ('server', QOS_1),
          ('gateway', QOS_2),
       ])

  print('topic  |  message')
  print('-----  |  -------------------')
  try:
    while True:
      message = await C.deliver_message()
      packet = message.publish_packet
      print("%s => %s" % (packet.variable_header.topic_name, packet.payload.data.decode()))
    await C.unsubscribe(['server', 'gateway'])
    await C.disconnect()
  except ClientException as ce:
    logger.error("Client exception: %s" % ce)

if __name__ == '__main__':
  asyncio.get_event_loop().run_until_complete(sub_test())
