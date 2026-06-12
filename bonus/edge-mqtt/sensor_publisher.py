import json
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


BROKER_HOST = "127.0.0.1"
BROKER_PORT = 1883
TOPIC = "edge/sensor/room-a"


def build_payload(seq):
    return {
        "device_id": "edge-room-a-01",
        "seq": seq,
        "temperature": round(24.0 + random.random() * 3.0, 2),
        "humidity": round(45.0 + random.random() * 10.0, 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER_HOST, BROKER_PORT, keepalive=30)
    for seq in range(1, 11):
        payload = build_payload(seq)
        client.publish(TOPIC, json.dumps(payload, ensure_ascii=False), qos=1)
        print(f"published {TOPIC} {payload}")
        time.sleep(0.5)
    client.disconnect()


if __name__ == "__main__":
    main()
