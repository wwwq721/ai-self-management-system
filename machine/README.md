# machine/ —— 机器事实索引

> 本目录登记治理体系里全部**机器特化事实**。结构是**双轴**：先按主机分（`_host/<机器标识名>/`，每台电脑一个文件夹），再按软件分（`<软件>/common.md`，跨机器共通）。
> 本文件是**索引**，只列清单与识别特征；读取规则见根 [../MACHINE.md](../MACHINE.md) 的「解析规则」节。
> **`_host/` 未随公开仓上传**：本文件里指向 `_host/…` 的链接，在公开仓内指向不存在的文件（清单与识别特征仍保留，便于公开仓读者理解结构）。

## 怎么读（解析规则）

1. **判本机是哪台**：取本机 Windows 用户名（bash `$USERNAME`、Python `os.environ['USERNAME']`；Python 取法最稳——**PowerShell 通道可能不回显 stdout**），在下方「机器清单」按识别特征匹配，得到**机器标识名**（形式 `pc-<用户名>`，ASCII 部分小写）。**用户名撞车时用主机名兜底**：若匹配到多行（`Administrator` 是 Windows 默认管理员名，尤易撞），取主机名（Python `socket.gethostname()` 或 `hostname`），与各候选机器的 `_host/<标识名>/host.md` 里登记的主机名比对（主机名不在本表，登记在该文件）。
2. **机器级事实**：读 `_host/<机器标识名>/host.md`。
3. **某软件的事实**：读 `<软件>/common.md`（跨机器共通）＋ `_host/<机器标识名>/<软件>.md`（本机特化）。**后者不存在即表示该软件在本机未装。**
4. **只读本机那份**；其他主机文件夹里的文件不加载——它们是档案，不是当前事实。

## 机器清单

| 机器标识名 | 识别特征 | 平台 | 主机文件夹 | 采集日期 |
|---|---|---|---|---|
| `pc-administrator` | `$USERNAME` = `Administrator` | win32 | [_host/pc-administrator/host.md](_host/pc-administrator/host.md) | 2026-09-28 |
| `pc-纳` | `$USERNAME` = `纳` | win32 | [_host/pc-纳/host.md](_host/pc-纳/host.md) | 2026-08-22 起至 2026-09-22 多次记录；此后未重采 |

> 本表的识别特征只登记**用户名**；主机名登记在各机 `_host/<标识名>/host.md`，不写进本表（本表会随公开仓上传，主机名属本机事实）。用户名单独用时重名风险高（`Administrator` 是 Windows 默认管理员名），撞车时按上面第 1 条去该文件比对兜底。

## 软件矩阵

单元格＝该软件在本机的特化文件链接（在主机文件夹内）；`—` = 该机未装（**无该文件**）。

| 软件 | 跨机器共通 | pc-administrator | pc-纳 |
|---|---|---|---|
| WorkBuddy 桌面版 | [workbuddy/common.md](workbuddy/common.md) | [_host/pc-administrator/workbuddy.md](_host/pc-administrator/workbuddy.md) | [_host/pc-纳/workbuddy.md](_host/pc-纳/workbuddy.md) |
| ZCode | [zcode/common.md](zcode/common.md) | — | [_host/pc-纳/zcode.md](_host/pc-纳/zcode.md) |
| Codex 桌面版 | [codex/common.md](codex/common.md) | — | — |
| CodeBuddy Code（CLI） | [codebuddy/common.md](codebuddy/common.md) | — | — |

> WorkBuddy 三份由原 `machine/workbuddy.md`（316 行）按「跨机器共通 vs 机器特化」拆出，已完成。原 `machine/{workbuddy,zcode,codex,codebuddy}.md` 四份旧文件已移入 `.trash/`（2026-09-28）。
> 2026-10-02 主机轴重构：取消「机器×软件」交叉文件——`machine/<软件>/` 只留 `common.md`；每台主机一个文件夹 `_host/<机器标识名>/`，该机全部特化事实（`host.md` ＋ 各软件 `<软件>.md`）收进这个文件夹。

## 约定

- **每台机器只写自己那个主机文件夹**：`_host/<本机标识名>/` 下的 `host.md` 与各软件特化文件（`<软件>.md`）。共通文件（各 `common.md`、本文件）两边都能改，靠合并。
- **新增软件**：建 `<软件>/common.md` ＋ 在本表登记一行；装到某台机器时再建该机的 `_host/<机器标识名>/<软件>.md`；**未装的软件不建本机文件**。
- **新增机器**：建 `_host/<新标识名>/host.md` ＋ 在本表登记一行（含识别特征）。
- **换环境**：本机文件重采，**旧值不沿用、不迁移**（依据根 [../MACHINE.md](../MACHINE.md)「迁移流程」）。
- 各软件目录内的 `README.md`（若有）只描述该目录自身，不重复本文件的清单。
