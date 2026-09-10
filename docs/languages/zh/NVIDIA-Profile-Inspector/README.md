<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · **简体中文** · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**[NVIDIA Profile Inspector 由 Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector) 的独立 fork，增加了显示控件。** 原项目名称：**NVPI Custom**。

[下载和发布状态](../docs/downloads.md#nvidia-profile-inspector) · [安装](#installation) · [上游和变化](#upstream-and-changes) · [许可证](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## 概述

该应用程序编辑 NVIDIA 驱动程序配置文件，包括每个应用程序的设置。此 fork 还为活动 Windows 显示器添加了一个**屏幕**编辑器：分辨率、刷新率、输出颜色设置、HDR 和已安装的 ICC/WCS 配置文件关联。

它的存在是为了将相关的显示控件带入配置文件编辑器中，并使预览、确认和恢复结果更加清晰。它没有建立新的硬件功能。

第一个候选是 **3.0.2.3**，使用 2026 年 9 月 9 日起清理后的独立配套版本。其现有可执行文件仍然是 `nvidiaProfileInspector.exe`；安装程序和一些内部标签仍然显示 `NVPI Custom NV`。上面的公共标题标识了 fork，无需更改安装标识或假装它是 Orbmu2k 的正式版本。

<a id="features"></a>
## 特点

- 现有上游配置文件浏览、应用程序关联、设置编辑和配置文件导入/导出。
- **屏幕** 对话框，用于显示、模式、Hz、RGB/YCbCr、颜色深度、范围和色度。
- Windows HDR 控制与已安装的 ICC/WCS 关联选择。
- 带有 **Keep** / **Revert** 和超时恢复功能的 15 秒显示预览。
- 回读模式/HDR 更改并报告恢复失败。
- 单独报告 HDR、带 ACM/WCG 的 SDR 和信号颜色深度。
- 用于符合条件的单独安装副本的 NVRasterPulse 启动器。

<a id="compatibility"></a>
## 兼容性

| 要求 | 详情 |
| --- | --- |
| 系统 | Windows 10/11 x64，带有兼容的 NVIDIA 驱动程序 |
| 运行时 | [.NET框架4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)，由Windows提供或单独安装 |
| 权限 | 编辑器打开时请求管理员访问权限 |
| 显示器 | 实际模式和颜色组合取决于 GPU、驱动程序、显示器、电缆和 Windows API |
| 可选工具 | NVRasterPulse用于RTSS限制管理；屏幕编辑器不需要它或 RTSS |
| 语言 | 设置：34 种语言选择器。编辑器保留其现有的语言支持。 |

对于每个 GPU，没有经过验证的通用驱动程序最低限度或支持矩阵。该对话框的可用 bpc 选择是请求，而不是经过认证的组合。现代 HDR 控件和旧版 Windows 后备控件具有不同的功能。

<a id="installation"></a>
## 安装

1. 打开 [下载页面](../docs/downloads.md#nvidia-profile-inspector) 并检查发布状态。
2. 下载安装程序或便携式资产并将其 SHA-256 与发布清单进行比较。
3. 对于安装程序，运行 `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`，选择一种语言并按照安装程序进行操作。它创建自己的快捷方式和卸载程序。
4. 为了便于携带，请将完整的 ZIP 解压缩到新的可写文件夹中。将 `Reference.xml`、EXE 配置和所有声明保留在可执行文件旁边。
5. 启动 `nvidiaProfileInspector.exe`。

单独安装编辑器不会应用配置文件或安装 GPU 驱动程序。该配套软件单独安装，不会接管 `.nip` 关联，并且不会在登录时启用启动。现有的二进制文件未签名。

<a id="usage"></a>
## 用途

**安装程序修订版 2** 添加了与其他工具相同的本机 34 语言选择器，具有鼠标/键盘导航、浅色/深色外观和取消功能。该选择适用于设置；它不翻译 NVPI 编辑器。显式 `/LANG=fr` 参数或静默模式会绕过已提供语言的调用者的选择。

**驱动程序配置文件：** 选择一个配置文件，导出备份，然后仅编辑所需的设置并应用它们。应用程序关联确定哪个游戏接收配置文件。存储值并不能证明每个驱动程序或游戏都使用它。

**显示控件：**打开**屏幕**，选择显示和请求的值，然后开始预览。请在 15 秒内检查图像，然后选择 **保留**。使用**恢复**，关闭确认或让它过期以请求恢复。阅读任何失败消息：仅成功的 API 调用并不能证明恢复。

ICC 选择会更改已安装的配置文件关联；它不会生成、校准或重新分发 ICC 文件。 HDR、ACM/WCG、RGB/YCbCr 和 bpc 描述了管道的不同方面。没有提供新的独立ACM开关。

**NVRasterPulse：** 工具栏按钮接受在程序文件下单独注册的系统范围安装，并具有受保护的所有权和权限。此提升的启动器可能会拒绝便携式副本或用户可写/链接路径。在这种情况下，使用其自己的快捷方式打开 NVRasterPulse。 [单独安装RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) 使用 NVRasterPulse。

<a id="screenshots"></a>
## 截图

![NVPI 设置修订版 2 语言选择器](../../../../assets/screenshots/nvpi-setup-r2-language.png)

法语的实际设置选择器，在隔离测试期间捕获，然后取消。这显示了安装程序；编辑器保留其界面和屏幕对话框。

<a id="update-and-uninstall"></a>
## 更新和卸载

更新之前关闭编辑器。保留导出的配置文件并下载新的 fork 版本；通过相同的配套身份进行安装或将可移植文件提取到新文件夹中。请勿将旧的 `Reference.xml` 与新的可执行文件混合使用。捆绑的上游更新检查抑制属于此 fork。

对于已安装的副本，请使用 Windows **Installed apps** 及其卸载程序。对于便携式设备，请在导出安全后将其关闭并删除其提取的文件夹。删除编辑器**不会**撤消驱动程序配置文件编辑、显示首选项、NVRasterPulse 或 RTSS。删除之前恢复所需的设置。

<a id="known-limitations"></a>
## 已知的限制

- 15 秒确认并不是对每次驱动程序崩溃、断电或强制关机的监督。
- 某些颜色/深度/刷新组合返回 `NVAPI_NOT_SUPPORTED`。
- 软件回读不测量面板位深度、颜色精度或延迟。
- 屏幕设置影响当前Windows显示；此对话框不会创建每个游戏的显示预设。
- 没有性能、反作弊或通用 HDR 兼容性保证。

<a id="troubleshooting"></a>
## 故障排除

| 症状 | 行动 |
| --- | --- |
| 启动时运行时错误 | 检查 Windows 更新和 .NET Framework 4.8；使用完整的包。 |
| 请求的显示模式被拒绝 | 恢复并测试 Windows/NVIDIA 为该显示器提供的模式。读取准确的错误，避免重复盲目修改。 |
| HDR 或颜色恢复到旧状态 | 检查是否有其他操作失败并触发恢复；区分 HDR 和 ACM。 |
| NVRasterPulse 按钮拒绝路径 | 启动自己的快捷方式；此按钮需要受保护的系统范围安装。 |
| 卸载后仍有更改 | 恢复导出的 NVIDIA 配置文件或预期的 Windows 显示设置；卸载不是设置回滚。 |

发送日志之前请参阅 [共享支持指导](../docs/support.md)。

<a id="faq"></a>
## 常见问题解答

**这是官方的 NVIDIA 软件还是 Orbmu2k 的官方版本？** 不是。它是一个独立的 fork；上游作者和 MIT 许可证仍然记入。

**NVDriverForge 是否需要此编辑器？** 不需要。NVDriverForge 的可选 Custom NV 预设使用其自己的集成。安装编辑器是一个单独的选择。

**RTSS 对于该 fork 是强制的吗？** 否。RTSS 对于 NVRasterPulse 的 FPS 限制器是强制的，不适用于配置文件或屏幕编辑。

**来源在哪里？** 修改后的应用程序来源是私人维护的。提供MIT通知和上游存储库； MIT 不需要发布修改后的源。

<a id="upstream-and-changes"></a>
## 上游和变化

上游：[Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector)，参考提交 `592d962cca8827efe8859461a84267755595064a`。 [原创下载](https://github.com/Orbmu2k/nvidiaProfileInspector/releases)。

继承：配置文件编辑器、NVAPI 互操作、参考数据、UI 资源和主题。 禅堂 Zendo (RevoluSound Team) 添加或调整了显示服务、HDR/ICC 事务、15 秒确认/回读、工具栏布局和 RasterPulse 启动行为。清理后的伴侣排除了开发模拟/测试入口点，使用受保护的外部启动器并提供单独的安装程序。旧的 NVPI/RasterPulse 组合开发包不适合此中心。

[详细的文件来源](../docs/provenance.md) · [原始fork通知](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## 学分和许可

版权所有 (c) 2016 Orbmu2k。保留提供的 [MIT 许可证](../../../../NVIDIA-Profile-Inspector/LICENSE)。适配和包装：禅堂 Zendo (RevoluSound Team)。安装程序使用Inno Setup； Windows 和 .NET Framework 仍然是外部的。 [完整适用的通知](LICENSES/README.md)。

独立于 NVIDIA Corporation，不受 NVIDIA Corporation 赞助，也未得到 NVIDIA Corporation 的正式认可。商标仍归其各自所有者所有。
