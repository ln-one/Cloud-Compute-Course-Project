import json
import os
import time

import paho.mqtt.client as mqtt
import redis


MQTT_HOST = os.getenv("MQTT_HOST", "127.0.0.1")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "edge/sensor/#")

REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", "63790"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD") or None


rdb = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True,
)


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"connected mqtt reason={reason_code}")
    client.subscribe(MQTT_TOPIC, qos=1)


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    data = json.loads(payload)
    rdb.lpush("edge:sensor:latest", json.dumps(data, ensure_ascii=False))
    rdb.ltrim("edge:sensor:latest", 0, 19)
    rdb.hset("edge:sensor:last", mapping={
        "topic": message.topic,
        "device_id": data.get("device_id", ""),
        "seq": data.get("seq", 0),
        "temperature": data.get("temperature", 0),
        "humidity": data.get("humidity", 0),
        "timestamp": data.get("timestamp", ""),
    })
    print(f"stored topic={message.topic} seq={data.get('seq')}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, keepalive=30)
    client.loop_start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
