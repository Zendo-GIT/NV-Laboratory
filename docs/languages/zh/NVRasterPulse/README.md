<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · **简体中文** · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**每个应用程序 FPS 到 RivaTuner Statistics Server 的限制。**

> **首先安装 RTSS。** NVRasterPulse 需要 [RivaTuner Statistics Server (RTSS)，从 Guru3D 下载](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)。 RTSS 必须运行才能实施限制。未捆绑 RTSS 安装程序、挂钩 DLL 或 SDK。

[下载 0.1 和状态](../docs/downloads.md#nvrasterpulse) · [安装](#installation) · [限制如何运作](#usage) · [许可证](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## 概述和目的

NVRasterPulse 是一个紧凑的 Windows 接口，用于按可执行文件名称管理 RTSS 帧限制。 RTSS 执行限制。 NVRasterPulse 通过托盘访问和持久选择来管理相应的配置文件值、备份和重新加载请求。

它的存在是为了使每个游戏的精确限制更容易编辑，而无需替换整个 RTSS 配置文件或干扰其覆盖设置。当前 **0.1** 候选版本是 2026 年 9 月 9 日版本，需要进行 RTSS 安装检查。

<a id="features"></a>
## 特点

- 选择正在运行的应用程序或手动添加其可执行文件。
- 保存 FPS 限制范围为 1 到 1000，最多保留三位小数。
- 输入值的精确有理编码：59.94 变为 2997/50。
- 具有主动等待 (`PassiveWait=0`) 的前沿同步配置 (`SyncLimiter=1`)。
- 每个可执行文件的配置文件更新、自动备份和原子写入。
- 删除限制器覆盖，同时保留其他配置文件内容。
- RTSS 安装检测、手动路径选择和显式启动/重新加载。
- 单实例托盘操作，可选安装启动，34种语言和四种主题。
- 单独的正常退出和 **退出 + RTSS** 操作。

<a id="compatibility"></a>
## 兼容性

| 要求 | 详情 |
| --- | --- |
| 系统 | Windows 10/11 x64 |
| 运行时 | [.NET框架4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)，如果需要单独安装 |
| 所需软件 | RTSS 与 `RTSS.exe`、匹配的 `Profiles` 目录和兼容的配置文件/重新加载支持 |
| GPU | RTSS兼容性决定了限制器；此配置文件管理器不需要特定的 RTX 代 |
| 权限 | 当前应用程序请求管理员访问权限；所选的 RTSS 配置文件文件夹必须可访问 |
| 游戏 | 取决于 RTSS 挂钩支持和每个游戏的限制；无反作弊保证 |

此集线器审核尚未针对每项功能认证特定的 RTSS 最低版本。如果配置文件密钥/重新加载不起作用，请使用官方当前发行版并报告确切的版本。已安装但已停止的RTSS通过安装检查；然后必须启动它以进行实际限制。

<a id="installation"></a>
## 安装

1. **[从 Guru3D 下载并安装 RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. 打开 [NVRasterPulse 下载](../docs/downloads.md#nvrasterpulse) 并检查版本可用性。
3. 下载 `NVRasterPulse-0.1-win-x64-Setup.exe` 或 `NVRasterPulse-0.1-win-x64-portable.zip`，以及通知/校验和。
4. 比较 SHA-256。运行安装程序或将整个便携式 ZIP 解压缩到可写的本地文件夹。
5. 打开`NVRasterPulse.exe`。如果缺少 RTSS，请使用 **下载 RTSS**，安装它，然后 **再次检查**，或手动选择 `RTSS.exe`。
6. 使用其正常快捷方式启动 RTSS，如果停止，则使用 NVRasterPulse 的 RTSS 按钮启动它。

关闭可选提醒不会跳过先决条件检查。 Windows 托盘静默启动会等待主窗口打开，然后再显示此检查。该安装程序仅安装 NVRasterPulse。它的 EXE 未签名。

<a id="usage"></a>
## 用途

1. 选择要运行的应用程序或浏览到其游戏 EXE。
2. 输入 1 到 1000 FPS 之间的限制，包括小数值（如果需要）。
3. 保存并检查报告结果。 NVRasterPulse 更新该可执行文件的 RTSS 配置文件并请求重新加载。
4. 确认 RTSS 正在运行并验证预期游戏中的行为。

配置文件由 **可执行文件名称** 键入，例如 `Game.exe.cfg`。包含 `Game.exe` 的两个不同文件夹共享相同的 RTSS 配置文件；存储完整路径并不能消除这种冲突。

保存使用前沿同步和主动等待。主动等待可能会增加 CPU 的使用。备用 `LimitTime` 字段被中和。现有注释、覆盖设置和 `EnableHooking=0` 将被保留。 RTSS 全局配置文件未更改。

使用垃圾操作删除 NVRasterPulse 的限制器覆盖。它不会删除整个 RTSS 配置文件。从 RTSS Global 或其他工具继承的限制此后可能仍然适用。

**关闭和退出：**主窗口可以隐藏到托盘中。正常 **退出** 使 RTSS 保持运行并保存完好的限制。 **退出 + RTSS** 请求正常关闭当前会话中匹配的 RTSS 进程，最多等待八秒，并且不会强制终止它。两种情况下都保留存储的限制。

语言和主题在应用程序中选择。 Windows 登录时启动是可选的，适用于已安装的副本。信息按钮解释了常见操作。

<a id="screenshots"></a>
## 截图

![NVRasterPulse 主窗口预览](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

现有法语 0.1 UI 呈现，带有示例可执行文件名称和 176 FPS 值。 RTSS 显示已停止；这是一个界面插图，而不是运行限制器或延迟测量。 [图片来源](../assets/README.md)。

<a id="update-and-uninstall"></a>
## 更新和卸载

退出 NVRasterPulse，下载并验证新版本，然后运行其安装程序或将便携式设备解压缩到新文件夹中。保留设置和 RTSS 备份。 RTSS 更新是独立的，来自 Guru3D。

要删除已安装的副本，请使用 Windows **Installed apps**。对于便携式设备，请退出，然后在备份安全时删除其提取的文件夹。卸载 NVRasterPulse 不会删除保存的 RTSS 限制：首先删除预期的限制器覆盖。 RTSS 有自己的卸载程序。

本地状态：`%LOCALAPPDATA%\NVRasterPulse`。自动 RTSS 备份：`%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`。可以读取较旧的 `%LOCALAPPDATA%\RTSSProfileBridge` 位置进行迁移。这些文件可以包含个人可执行路径，不应公开发布。

<a id="known-limitations"></a>
## 已知的限制

- RTSS 执行上限。保存的值或成功的重新加载请求不是测量的帧时间结果。
- 同名的可执行文件共享一个配置文件。
- 另一个全局/每场比赛的限制因素可能会影响结果；禁用本地覆盖不会删除继承的上限。
- 故意禁用的 RTSS 挂钩仍保持禁用状态。
- 主动等待需要进行 CPU/功耗权衡。
- 没有通用游戏、反作弊或端到端延迟验证。
- 早期实验性的独立限制器引擎尚未编译或发布。
- 自动备份并不意味着一键式完整备份恢复界面。

<a id="troubleshooting"></a>
## 故障排除

| 症状 | 行动 |
| --- | --- |
| RTSS 先决条件仍然开放 | 选择实际的 `RTSS.exe` 和匹配的 Profiles 文件夹，然后再次检查。 |
| 限制已保存但没有效果 | 启动RTSS；验证正确的游戏 EXE/配置文件、挂钩权限和其他限制器。 |
| 保存失败 | 检查文件夹权限并保留显示的错误/备份。 |
| 移除后仍保留限制 | 检查RTSS Global和其他工具；垃圾操作仅删除本地限制器覆盖。 |
| 两款游戏受到相同的限制 | 检查它们的可执行文件名是否相同。 |
| 退出 + RTSS 让 RTSS 保持打开状态 | 自己正常关闭RTSS；该命令故意避免强制终止。 |

如果手动恢复 RTSS 备份，请先关闭 RTSS 并保留当前配置文件，然后再将其替换为预期备份。这可能会覆盖不相关的配置文件编辑；检查文件和日期。 [共享支持](../docs/support.md)。

<a id="faq"></a>
## 常见问题解答

**我也需要 MSI Afterburner 吗？** NVRasterPulse 需要 RTSS；它不依赖于 Afterburner 应用程序。请遵循 RTSS 经销商的安装选项。

**我可以在不运行 RTSS 的情况下使用它吗？** 一旦检测到安装，您就可以管理配置文件，但必须运行 RTSS 才能进行限制。

**退出或卸载是否会删除上限？** 不会。在删除 NVRasterPulse 之前明确删除所需的限制器覆盖。

**它是fork还是RTSS？** 不是。它是一个独立的配置文件管理器；未合并 RTSS 源或可执行文件。

<a id="upstream-modifications-and-credits"></a>
## 上游、修改和制作人员

开发存储库源自[Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector)。其 MIT 调色板/UI 资源已记入。配置文件管理服务、分数编码、备份、RTSS 重新加载桥、托盘行为、先决条件指南、语言和应用程序特定图标均由 禅堂 Zendo (RevoluSound Team) 开发/改编。

RTSS 由 **Unwinder** 开发，并通过 Guru3D 单独分发。 NVRasterPulse 从所选安装的钩子 DLL 中调用 `UpdateProfiles`；没有重新分发 RTSS SDK 或挂钩二进制文件。安装程序使用未经修改的 Inno Setup 7.1.0 以及经过调整的脚本/翻译和项目引导程序。

[完整出处](../docs/provenance.md) · [第三方表](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## 许可证

该软件包在提供的 [MIT 许可证](../../../../NVRasterPulse/LICENSE) 下明确分发 NVRasterPulse，保留版权所有 (c) 2016 Orbmu2k。应用程序源是私人维护的； MIT 不需要发布修改后的源。 RTSS 和 Windows/.NET 仍保留其自己的条款。 [完整通知](LICENSES/README.md)。

独立于NVIDIA Corporation、MSI和RTSS；未经他们赞助或正式认可。产品名称仍然是其所有者的商标。
