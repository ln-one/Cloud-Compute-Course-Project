import os
from datetime import datetime, timezone

import redis
import requests
from flask import Flask, jsonify

app = Flask(__name__)


def redis_client():
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", "6379"))
    password = os.getenv("REDIS_PASSWORD") or None
    return redis.Redis(host=host, port=port, password=password, decode_responses=True)


@app.get("/api/ping")
def ping():
    payload = {
        "status": "ok",
        "student": "2023112573 张春冉",
        "time": datetime.now(timezone.utc).isoformat(),
    }
    try:
        redis_client().incr("ping_count")
        payload["redis"] = "connected"
    except Exception as exc:
        payload["redis"] = "unavailable"
        payload["redis_error"] = exc.__class__.__name__
    return jsonify(payload)


@app.get("/api/count")
def count():
    value = redis_client().get("ping_count") or "0"
    return jsonify({"ping_count": int(value)})


@app.get("/api/httpbin")
def httpbin():
    response = requests.get("https://httpbin.org/status/204", timeout=3)
    return jsonify({"status_code": response.status_code})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

