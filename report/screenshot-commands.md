# Ghostty 截图命令清单

以下命令建议在 Ghostty 中逐段运行并截图。截图插入 `report/course-report.md` 中对应的“截图占位”位置即可。

## 图 1：节点 Ready

```bash
cd /Users/ln1/Projects/Cloud-Compute
KCFG=/Users/ln1/Projects/Cloud-Compute/kubeconfig/cloud-compute-cce-kubeconfig.yaml
kubectl --kubeconfig "$KCFG" get nodes -o wide
```

## 图 5：Pod Running

```bash
kubectl --kubeconfig "$KCFG" get pods -o wide
```

## 图 6：Service 公网地址

```bash
kubectl --kubeconfig "$KCFG" get svc
```

## 图 7：后端公网 API

```bash
NO_PROXY=119.3.252.161,1.92.103.90 no_proxy=119.3.252.161,1.92.103.90 \
curl http://1.92.103.90/api/ping
```

## 图 8：前端公网 API 代理

```bash
NO_PROXY=119.3.252.161,1.92.103.90 no_proxy=119.3.252.161,1.92.103.90 \
curl http://119.3.252.161/api/ping
```

浏览器页面截图访问：

```text
http://119.3.252.161/
```

## 图 9：PVC Bound

```bash
kubectl --kubeconfig "$KCFG" get pvc
```

## 图 10-12：Redis 持久化验证

```bash
REDIS_POD=$(kubectl --kubeconfig "$KCFG" get pod -l app=redis -o jsonpath='{.items[0].metadata.name}')
kubectl --kubeconfig "$KCFG" exec "$REDIS_POD" -- redis-cli -a cloudcompute2026 SET testkey hello
kubectl --kubeconfig "$KCFG" exec "$REDIS_POD" -- redis-cli -a cloudcompute2026 GET testkey
kubectl --kubeconfig "$KCFG" delete pod "$REDIS_POD"
kubectl --kubeconfig "$KCFG" get pods -w
```

新 Pod Running 后按 `Ctrl+C` 停止 watch，再执行：

```bash
NEW_REDIS_POD=$(kubectl --kubeconfig "$KCFG" get pod -l app=redis -o jsonpath='{.items[0].metadata.name}')
kubectl --kubeconfig "$KCFG" exec "$NEW_REDIS_POD" -- redis-cli -a cloudcompute2026 GET testkey
```

## 图 13-14：ConfigMap Volume 挂载

```bash
FRONT_POD=$(kubectl --kubeconfig "$KCFG" get pod -l app=frontend -o jsonpath='{.items[0].metadata.name}')
kubectl --kubeconfig "$KCFG" exec "$FRONT_POD" -- cat /etc/nginx/conf.d/default.conf
```

如需演示配置更新，可修改 `k8s/04-frontend.yaml` 中 ConfigMap 的端口文字后：

```bash
kubectl --kubeconfig "$KCFG" apply -f k8s/04-frontend.yaml
kubectl --kubeconfig "$KCFG" exec "$FRONT_POD" -- cat /etc/nginx/conf.d/default.conf
```

## 图 15-18：HPA 压测

```bash
kubectl --kubeconfig "$KCFG" top nodes
kubectl --kubeconfig "$KCFG" top pods
kubectl --kubeconfig "$KCFG" get hpa
```

压测窗口：

```bash
ab -n 10000 -c 200 http://1.92.103.90/api/ping
```

观察窗口：

```bash
kubectl --kubeconfig "$KCFG" get pods -w
```

## 图 19-23：MPI

```bash
kubectl --kubeconfig "$KCFG" apply -f mpi-operator.yaml
kubectl --kubeconfig "$KCFG" apply -f mpi/mpijob.yaml
kubectl --kubeconfig "$KCFG" get pods
kubectl --kubeconfig "$KCFG" logs <launcher-pod-name>
```

