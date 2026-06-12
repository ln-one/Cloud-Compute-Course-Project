# 边缘计算模拟：K3s + MQTT

本目录用于附加题 C-2。实验用本地 MQTT Broker 模拟边缘侧消息入口，用 Python 传感器脚本持续发布温湿度数据，再由云端桥接脚本订阅消息并写入 CCE 集群中的 Redis。

实际报告中说明：本机环境没有再单独安装完整 K3s 节点时，可将本地 Docker 运行的 Mosquitto 看作边缘节点上的轻量 MQTT 服务；云端 Redis 通过 `kubectl port-forward svc/redis-svc` 暴露给桥接脚本，数据最终仍落在 CCE Redis 中。

运行顺序：

```bash
.venv/bin/pip install -r bonus/edge-mqtt/requirements.txt

docker run --rm -d --name edge-mosquitto -p 1883:1883 eclipse-mosquitto:2 \
  mosquitto -c /mosquitto-no-auth.conf

kubectl --kubeconfig kubeconfig/cloud-compute-cce-kubeconfig.yaml \
  port-forward svc/redis-svc 63790:6379

REDIS_HOST=127.0.0.1 REDIS_PORT=63790 REDIS_PASSWORD=cloudcompute2026 \
  .venv/bin/python bonus/edge-mqtt/cloud_mqtt_bridge.py

.venv/bin/python bonus/edge-mqtt/sensor_publisher.py
```

Redis 验证：

```bash
kubectl --kubeconfig kubeconfig/cloud-compute-cce-kubeconfig.yaml exec deploy/redis -- \
  redis-cli -a cloudcompute2026 LRANGE edge:sensor:latest 0 4
```
