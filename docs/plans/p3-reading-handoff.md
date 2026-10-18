# P3 阅读导出与合法全文交接

## 范围

P3 只处理已保存且校验过的 Research Search Package，或调用方显式提供的 paper records。实现是离线元数据交接与阅读材料导出：

- 不访问网络，不下载 PDF，不登录，不绕过付费墙，不解析/解决访问权限。
- `open_access_url` 只在输入原始记录同时明确给出公开可用断言时保留；不会从 DOI、PMID 或 `source_url` 猜测全文地址。
- 默认每项都需要人工后续获取。`availability` 为 `metadata_only`、`open_access_candidate` 或 `user_supplied_fulltext`。
- 每个队列项保留 `paper_id`、DOI、PMID、来源 URL、候选公开 URL（如输入明确提供）和 provenance。

## CLI 集成公开方法

导入：

```python
from research_search.acquisition_handoff import acquisition_handoff
from research_search.reading_export import export_reading, open_obsidian
```

### `acquisition_handoff`

```python
acquisition_handoff(
    source=None,
    output_path=None,
    *,
    papers=None,
) -> dict
```

- `source` 可以是 package 目录、显式 JSON/JSONL 文件、显式 records 数组或 `{ "papers": [...] }` 映射。
- `papers` 是显式 records 的便捷写法；不能和 `source` 同时传入。
- `output_path=None`：只返回 queue，不写文件。
- 指定 `output_path`：创建一个新的 JSON handoff；目标已存在时抛 `FileExistsError`，不覆盖。
- 输入无效时先校验再创建输出，失败不会留下目标父目录。
- 返回 queue 顶层包含 `schema_version`、`items`、`policy`。`policy.network_calls=0`、`downloads=False`、`login=False`、`paywall_bypass=False`。

### `export_reading`

```python
export_reading(
    source,
    output_dir,
    *,
    papers=None,
    old_manifest=None,
    metadata_formats=(),
) -> dict
```

`export_reading` 是 `export_reading_material` 的 CLI 别名，返回 manifest 字典。`output_dir` 必须是新目录；已存在目录（包括旧导出目录/Vault）直接抛 `FileExistsError`，不覆盖。

输出：

```text
<output_dir>/
├── index.md
├── papers/<safe-title>--<sha256(paper_id)>.md
├── handoff.json
├── manifest.json
├── metadata.jsonl   # 仅 metadata_formats 包含 jsonl 时
└── metadata.csv     # 仅 metadata_formats 包含 csv 时
```

- 主要交付物是 `index.md` 与 `papers/*.md`。
- frontmatter 使用 stdlib JSON（JSON 是 YAML 1.2 的兼容子集），特殊 HTML 字符 Unicode 转义；正文不自动生成 HTML/脚本。
- 缺失摘要写为“未提供”，不补写摘要。
- 翻译与创新点写为未分析/空白；阅读状态默认 `待确认`，人工可改为 `待读` / `已读`。
- 模型相关性单独保留，不自动成为人工相关性。
- 引用 URL 与 evidence 原样作为可追溯元数据保留，不访问 URL。
- 可选 JSONL/CSV 只导出安全 metadata；CSV 对 `= + - @` 公式前缀加单引号；不加载 xlsx。

### `open_obsidian`

```python
open_obsidian(export_dir) -> dict
```

这是明确的“不开启应用”边界方法：

- 只验证指定导出目录的 `manifest.json`、文件 inventory 和 SHA-256。
- 返回 `status="manual_import_required"`、`opened=False`、`vault_scanned=False`、`vault_written=False`。
- 不启动 Obsidian，不发 `obsidian://`，不猜 Vault 路径，不扫描或写用户 Vault。
- 调用方需要时由用户自行选择 Vault 并人工复制/导入已确认笔记。

## manifest 与增量语义

`manifest.json` 的 `files` 是所有导出产物的相对路径到 SHA-256 映射，但排除 `manifest.json` 自身，便于验证。manifest 还包含：

- `papers[paper_id].metadata_sha256`：只对源论文 metadata/access assertion 计算，和用户阅读字段分离。
- `papers[paper_id].note_sha256`：本次生成笔记的 SHA-256。
- `incremental.added` / `updated` / `unchanged` / `removed_candidates`：按稳定 `paper_id` 比较。
- `user_note_changes.modified` / `missing` / `not_checked`：明确区分用户编辑检查状态。

`removed_candidates` 只报告，不删除任何旧文件。给出旧 manifest 路径时，仅读取 manifest 明确列出的旧 note path；不扫描目录。检测到旧笔记被用户修改时，将其逐字节保留为新导出中的 `preserved-user-notes/*.md.txt`，不覆盖旧笔记，也不自动把用户正文合并进新 source metadata 笔记。

## 可验证事实

- P3 专项测试：`37 passed`；两个新增模块 `py_compile` 通过。
- 测试覆盖：路径遍历、重名 hash、引号/换行、引用 URL、原始 package 未变、manifest SHA-256、已存在目录拒绝覆盖、缺失摘要、不猜公开全文、增量 added/updated/unchanged/removed、旧笔记不删、用户编辑保留、invalid 输入无残留、CSV 公式字段、无网络调用。
- 本次按 P3 范围运行了两个专项测试文件；未对其他阶段模块做修改。
