# 截图清单

## 第一部分

1. `docker compose up --build` 本地运行截图，包含前端页面和后端日志。
2. SWR 镜像列表截图，包含 `backend:v1`、`frontend:v1`。
3. `kubectl get nodes -o wide` 截图，两个节点 `Ready`，版本 `v1.34.6-r0-34.0.23`。
4. `kubectl get pods -o wide` 截图，所有 Pod `Running`。
5. 浏览器或 curl 访问 `/api/ping` 返回 JSON。
6. `kubectl get pvc` 截图，`redis-data-pvc` 为 `Bound`。
7. Redis 写入、删除 Pod、重建后读取 `testkey` 的三张截图。
8. `cat /etc/nginx/conf.d/default.conf` 验证 ConfigMap Volume 更新截图。
9. HPA 扩容、缩容截图。

## 第二部分 MPI

1. MPI Operator 安装截图。
2. MPIJob Launcher 日志截图，包含数值积分估算的 pi。
3. 串行版和并行版结果一致截图。
4. 1/2/4 进程三次运行统计表和加速比图。
5. 阻塞版 vs 非阻塞版 4 进程时间对比截图。

