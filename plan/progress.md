# Progress

## 2026-06-12

- 已阅读课程设计任务书和项目现有报告。
- 已完成 CCE 公网 kubeconfig 配置，本机可访问集群。
- 已部署第一部分 K8s 资源，推送 backend/frontend 镜像到 SWR。
- 已验证 Pod Running、PVC Bound、后端公网 API 和前端反向代理 API 均返回 `status=ok`。
- 当前报告整理阶段：S4 Drafting / S5 Review。


### Capability-use audit
- Required skills: using-research-writing, paper-orchestration, writing-core, doc, pdf, verification-before-completion.
- Skills actually used: using-research-writing, paper-orchestration, writing-core, doc, pdf, verification-before-completion.
- Inputs consumed: 课程任务书 Markdown、现有报告、K8s YAML、后端/MPI 代码、真实 kubectl/curl 验证输出、Ghostty 截图文件。
- Inputs not used and why: CompoundBreaker 未使用，因为本机未找到可执行命令、应用或可加载工具；后续若提供路径可切换。
- Artifacts produced: `report/course-report.md`, `report/云计算技术课程设计报告.docx`, `report/云计算技术课程设计报告.pdf`, `report/screenshot-commands.md`, `report/evidence/*`.
- Verification run: `pandoc` 生成 DOCX，LibreOffice 转 PDF，`pdfinfo` 确认 PDF 9 页；此前已运行单元测试和公网 API 验证。
- Remaining risk: HPA 压测、Redis 删除重建、MPIJob 与性能数据尚未实际完成，报告中保留截图占位和待测表格，不能作为最终满分版本直接提交。
