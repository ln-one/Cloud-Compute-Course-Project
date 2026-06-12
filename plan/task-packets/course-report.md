## Task Packet

- Scope: 根据课程设计任务书和当前真实部署结果，整理 `report/course-report.md`。
- Files to read: `MinerU_markdown_课程设计任务书-final_2065348158734295040.md`, `report/course-report.md`, `report/evidence/*`, `k8s/*.yaml`, `backend/app.py`, `mpi/*.py`。
- Files allowed to edit: `report/course-report.md`, `plan/*.md`, `report/evidence/*`。
- Required skills: using-research-writing, paper-orchestration, writing-core, verification-before-completion。
- Evidence/data inputs: CCE 节点、Pod、Service、PVC、HPA、curl `/api/ping`、本地单元测试输出。
- Required artifacts: 完整报告草稿、证据索引、Ghostty 终端截图。
- Rejection checks: 不伪造未运行的 HPA/MPI/Redis 删除重建截图；不把占位数据写成实测结果；报告需说明当前已验证项和待补项。
- Validation commands: `python3 -m unittest discover -s backend/tests` 或 `.venv/bin/python -m unittest discover -s backend/tests`; `kubectl get pods -o wide`; `curl http://<IP>/api/ping`。

