<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · **简体中文** · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**用于 GeForce RTX 40 的实验性 NVIDIA Multi Frame Generation，带有中央控制器和每个游戏的选择。**

[下载 0.2.3 和状态](../docs/downloads.md#nvmfg-unlock40) · [安装](#installation) · [上游](#upstream-and-modifications) · [许可证](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## 概述和目的

NVMFG Unlock40是禅堂 Zendo (RevoluSound Team)独立开发的应用程序。它结合了 Windows 控制器、本机层、配置文件帮助程序和游戏/Streamline SDK 管理。它针对已集成 NVIDIA DLSS Frame Generation 和兼容的 NVIDIA 运行时的游戏。

咨询了 [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) 来比较和完善工作。当前的本机层包含共享和改编的组件，下面分别列出。此参考不会使整个 NVMFG 应用程序成为该项目的 fork。

它的存在是为了集中协调实验性 MFG 行为，记住特定于游戏的选择，并保持运行时更新和备份可见。它不会将 DLSS Frame Generation 添加到每个游戏中或转换任意 FSR 实现。

当前软件包是**0.2.3**。它添加了持久的游戏库、活动和功能信息、本地诊断和更正的选择/进度行为。 [下载](../docs/downloads.md#nvmfg-unlock40) 识别确切的文件和哈希值。

<a id="features"></a>
## 特点

- 中央启用/禁用控制和可选的 Windows 托盘启动。
- 每个游戏在 Dynamic MFG、游戏设置和支持的固定乘数之间进行选择。
- 观察到的 V-Sync 开/关状态的单独记忆选择。
- Dynamic使用NVIDIA的模式；当 V-Sync 关闭时，它会暂停，并有单独的游戏内/固定选择。
- 游戏菜单指导和持续排除；没有 DLSS FG 的游戏仍能保持控制。
- 游戏发现、父文件夹选择、搜索、分组和删除，无需删除游戏文件。
- Streamline SDK 下载/导入、验证本地缓存、显式选择、每游戏备份和恢复。
- 本机提供程序验证、每次会话诊断、全局配置文件日志和冲突感知恢复。
- 34 种界面语言和四种主题。

在游戏中关闭FG就可以让它关闭。从 2x 到 6x 的固定选择取决于游戏/菜单/运行时；它们并不保证每种组合都有效。控制器观察 V-Sync，并且不会为用户设置 V-Sync 或 VRR。

<a id="compatibility"></a>
## 兼容性

| 要求 | 详情 |
| --- | --- |
| 系统 | Windows 10/11 x64 |
| GPU | GeForce RTX 40 目标；无通用 GPU 兼容性声明 |
| 游戏 | 现有 NVIDIA DLSS Frame Generation 集成和支持的运行时；无反作弊兼容性认证 |
| 提供者 | 候选人被固定到 [出处](../docs/provenance.md) 中记录的提供者 SHA-256；未知的哈希值被拒绝 |
| 运行时 | 用于应用程序/代理的捆绑 .NET 8/WPF 8.0.30；用于配置文件助手的.NET Framework 4.8 |
| 权限 | 控制器/配置文件操作的管理员访问权限 |
| 网络 | 特定官方 SDK 下载所需；导入兼容SDKs可本地缓存 |
| 外部二进制文件 | NVIDIA 驱动程序、NGX 提供程序/模型和 Streamline 游戏运行时未捆绑 |

仅有版本标签是不够的：驱动程序、提供商哈希、游戏集成和实际加载的模块都很重要。受保护或不兼容的进程可以拒绝附加。该应用程序并非旨在逃避反作弊保护。

<a id="installation"></a>
## 安装

1. 阅读 [候选人状态和许可说明](../docs/downloads.md#nvmfg-unlock40)。
2. 当 `NVMFGUnlock40-0.2.3-Setup-x64.exe` 或 `NVMFGUnlock40-0.2.3-Portable-x64.zip` 版本可用时，下载该版本。
3. 检查 SHA-256 并保留随附的通知。如果 Windows 尚未提供，请安装 .NET Framework 4.8。
4. 运行安装程序，或将**整个**可移植 ZIP 解压缩到可写的本地文件夹。
5. 推出`NVMFGUnlock40.exe`；将 `agent`、`driver`、`engine` 和 `Licenses` 保留在提供的布局中。

名为 `driver` 的文件夹包含用户空间帮助程序，而不是内核驱动程序。不要仅复制主 EXE 或替换提供程序哈希以强制兼容。当前的 EXE 未签名。

<a id="usage"></a>
## 用途

1. 从控制器禁用开始。添加游戏或父文件夹并选择实际安装。
2. 检查每个游戏的 MFG 设置。回答其菜单提供什么；答案按游戏存储。
3. 全局选择 Dynamic 或游戏内设置，然后根据需要调整符合条件的每个游戏选择。
4. 仅当您打算使用控制器时才启用它。它可以通过恢复日志临时更改六个全局 NVIDIA 配置文件设置。
5. 启动符合条件的游戏并启用其自己的 DLSS Frame Generation。遵循 V-Sync-off 选择的任何请求。
6. 对您不想管理的游戏使用排除项。删除游戏会记录排除并保留其文件/备份。
7. 完成后使用应用程序的完全退出/禁用和恢复流程。

关闭主窗口可以将控制器留在托盘中。已经加载到游戏中的 DLL 会保留在那里，直到游戏退出；禁用控制器并不能保证卸载。在维护或更新之前关闭受影响的游戏。

**Streamline SDKs：**在NVIDIA SDK页面，下载官方版本或导入兼容的本地SDK。导入存储经过验证的副本； **Use this version** 选择它，**Uninstall** 删除该缓存副本。缺少的 Streamline DLL 可以通过官方 NVIDIA SDK 进行补充，并显示源代码。这不会下载/替换 NGX 模型。关闭游戏，选择想要的游戏更新，并保留其原始备份。要恢复游戏文件，请使用其备份恢复，而不是缓存的 Uninstall 按钮。

<a id="library-diagnostics-and-updates"></a>
## 库、诊断和更新

**永久库：**在开始一次扫描之前选择多个游戏文件夹，包括不同的驱动器。进度是可见的并且可以取消。第一次扫描后，本地缓存会在启动时恢复库，而无需遍历每个游戏文件夹。刷新以查找更改或添加另一个文件夹。维护操作仍会重新验证受影响的文件；备份监控保持活动状态。缓存存储在 `%LOCALAPPDATA%\RtxMfg\library-cache.json`。

**选择：** Ctrl+A 选择全部，Ctrl+D 清除活动的游戏或备份选项卡。不会自动选择任何游戏。活动更新和刷新不再创建幽灵选择或不一致的计数。

**活动和兼容性：** 每场比赛的 MFG 信息来自 NGX 观察结果，没有新的覆盖。它不是显示帧的物理计数。 Dynamic-with-V-Sync 支持来自运行时功能；未知功能不是从版本号推断出来的。应用程序既不更改 V-Sync 也不更改 VRR。当 V-Sync 关闭时，Dynamic 保持暂停状态；固定或游戏控制的选择是分开的。

**下次启动：**临时排除在下次游戏启动时跳过修补，并在退出后恢复正常管理。它无法删除游戏中已加载的 DLL：关闭并重新启动该游戏。 Wallpaper Engine被识别为桌面应用程序；此修正保留了对实际被忽略的游戏的保护。

**首选项和支持：**首选项导入/导出需要手动重新关联游戏文件夹。关于中的本地诊断会过滤私人信息并报告可用的 NVAPI 错误代码或冲突类别。分享前先回顾一下；没有任何内容会自动上传。

**应用程序更新：** 可选检查显示发行说明并提供官方安装程序。根据 GitHub 大小和 SHA-256 元数据检查显式下载；您自己启动安装。版本 0.2.3 还清除已完成的进度消息，同时保留有意义的错误和结果。这些新增内容包括自公共版本 0.1.1 以来的更改。

<a id="screenshots"></a>
## 截图

![NVMFG SDK-列表预览](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

现有英文 0.1.1 界面呈现为示例 SDK 库存。它不是当前版本列表或正在运行的游戏的证据。 [图片来源](../assets/README.md)。

<a id="update-and-uninstall"></a>
## 更新和卸载

关闭受影响的游戏。在更新之前禁用/退出 NVMFG 并解决任何挂起的 NVIDIA 设置恢复问题。使用现有标识安装下一个安装程序，或将新的便携式程序解压缩到新文件夹中；保留状态/备份。

卸载之前，通过应用程序恢复所需的游戏 SDK 备份和 NVIDIA 设置，然后关闭游戏并退出控制器。使用 Windows **Installed apps** 进行安装，或在保留所需文件后删除关闭的便携式文件夹。请勿手动删除活动恢复日志来解锁安装程序。

本地游戏运行时备份使用 `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`。 MFG设置/SDK数据使用`%LOCALAPPDATA%\RtxMfg`；会话输出位于应用程序旁边的 `Sessions` 下。这些文件可以包含游戏路径。不要发布未经编辑的内容。

<a id="known-limitations"></a>
## 已知的限制

- 报告的 0.1.1 激活/恢复/卸载阻塞仍未重现，其原因未知。此版本并未声称修复该问题。发生故障后，保留恢复日志并检查本地诊断；不要强制删除恢复数据。
- 实验性本机补丁可能会导致崩溃或视觉伪影；开发历史记录中记录了未解决的 Bodycam 崩溃。
- 受控渲染器测试并不是针对每个游戏、驱动程序或反作弊的认证。
- 生成的帧不会创建新的输入样本；该集线器不承诺测量延迟或性能增益。
- 多个帧生成工具/叠加可能会发生冲突。该应用程序报告观察到的模块，但不证明每个共存场景。
- 兼容性清单是一种检测辅助工具，而不是经过全面测试的游戏列表。
- 完整的 NVIDIA SDK 术语和未解决的技术限制仍记录在 [出处](../docs/provenance.md) 中。

<a id="troubleshooting"></a>
## 故障排除

| 症状 | 行动 |
| --- | --- |
| 不支持提供商 | 保留原始验证文件。报告驱动程序/提供商版本和错误；不要绕过哈希检查。 |
| 游戏中没有DLSS FG | 选择答案并让游戏由你掌控；该工具无法实现这种集成。 |
| 游戏崩溃/伪影 | 退出游戏，禁用 NVMFG，使用游戏的原始运行时备份（如果已更改），并报告可重现的详细信息。 |
| SDK 列表或下载不可用 | 刷新查看官方源码；缓存/导入的版本仍必须通过验证。 |
| 挂起的 NVIDIA 恢复阻止退出/更新 | 使用恢复并保存日志；不能盲目地去掩盖矛盾。 |
| 已删除的游戏不会被重新发现 | 它的排斥是持久的。当您希望再次管理它时，明确添加它。 |

[共享支持指导](../docs/support.md) 解释了报告中应包含的内容。

<a id="faq"></a>
## 常见问题解答

**它是否包含 NVIDIA DLL 或模型？** 不包含驱动程序、NGX 提供程序/模型或 Streamline 运行时。显式 SDK 下载来自 NVIDIA。

**Dynamic 是否在 V-Sync 关闭的情况下工作？** 它在该状态下暂停。为该游戏的单独状态选择游戏内设置或符合条件的固定乘数。

**这是 ReShade/OptiScaler/FSR 软件包吗？** 否。这些不是作为此生产软件包的一部分进行编译或提供的。

**修改后的源是否公开？** 否。提供了编译的软件包和所需的积分/许可证。这并不消除第三方的权利或限制。

<a id="upstream-and-modifications"></a>
## 上游和修改

比较参考和共享本机组件：**RTX40MFG-Unlock by Michael Robles / dashdogy**，参考提交 `4e776d068f91b4a665425542bb005dd57cc3d891`、MIT。 [存储库](https://github.com/dashdogy/RTX40MFG-Unlock)·[原创下载](https://github.com/dashdogy/RTX40MFG-Unlock/releases)。

源比较确定了共享补丁、提供商/策略处理、时间校正和基于 MinHook 的绕行组件。他们的 MIT 和 BSD 通知将被保留。完整的比较还包括生产目标之外的文件。

桌面应用程序、控制器和 SDK 管理工作流程由 禅堂 Zendo (RevoluSound Team) 开发。项目工作包括中央加载、NGX 引导集成、经过验证的提供商选择、游戏/V-Sync 协调和会话诊断。出处指南将该工作与共享组件分开；仅通过文件比较并不能确定任何一位作者何时有这个想法。

配置文件帮助程序改编自 Orbmu2k 的 Profile Inspector 的 MIT NVAPI 包装器。 [详细的出处和组件范围](../docs/provenance.md)。

<a id="credits-and-license"></a>
## 学分和许可

Michael Robles； Orbmu2k； Tsuda Kageyu 和 HDE 贡献者； NVIDIA Corporation； Microsoft 和贡献者； Inno Setup 作者和译者。应用程序开发、集成和打包：禅堂 Zendo (RevoluSound Team)。

[现有编译包共享权限](../../../../NVMFG-Unlock40/LICENSE) 和所有 [组件许可证](LICENSES/README.md) 均被保留。上游代码的 MIT 权限与 NVIDIA SDK 术语不同。没有一揽子许可证可以取代它们。

独立于 NVIDIA Corporation，不受 NVIDIA Corporation 赞助，也未得到 NVIDIA Corporation 的正式认可。所有引用的商标仍然是其所有者的财产。
