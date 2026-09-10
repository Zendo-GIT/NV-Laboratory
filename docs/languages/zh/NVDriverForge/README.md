<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · **简体中文** · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**准备 NVIDIA 驱动程序安装，并提供明确的组件选择和可选设置。**

[下载 0.1.3 和状态](../docs/downloads.md#nvdriverforge) · [安装](#installation) · [制作人员](#credits-and-upstream) · [许可证](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## 概述和目的

NVDriverForge 引导您完成原始 NVIDIA 驱动程序包：选择驱动程序，检查其组件，查看可选调整，然后确认安装。它的存在是为了使这些选择易于理解，并将安装、特权操作和恢复信息放在一起。

它是一款独立开发的应用程序，部分灵感来自 NVCleanstall 的工作流程。它不包括 NVCleanstall 或声称完整的功能对等。

<a id="features"></a>
## 特点

- NVIDIA Game Ready / Studio 查找和下载；可选的修补程序发现与手动回退。
- 分析原始包、哈希值、NVIDIA 签名、清单和兼容的 INF 条目。
- 具有依赖关系的组件选择和未知组件的保存。
- 版本 0.1.3 使选定的可选 NVIDIA 组件保持可跳过状态，并仅从发现中排除经过验证的未检查组件。现有的或不适用的可选运行时不再被强制作为关键组件。
- 清晰的安装失败摘要并可访问所有 34 种语言的详细日志。
- 显式安装确认、受保护的暂存和现有驱动程序存储包的导出。
- 可选的高级设置，包括预检检查、日志和冲突感知恢复。
- 可选 **Custom NV** 预设，包含命名选项和说明，包括单独的 SILK 强度选择和兼容性检查。
- 可选的精确版本 NVENC 补丁下载；检查源提交和目标字节。
- 从“工具”屏幕单独、可选地安装 Profile Inspector fork。
- 可选的安装用户更新检查、34 种界面语言和四种主题。

可用的高级选项涉及 MPO、DLSS 指示器、Ansel、NVIDIA 音频睡眠、MSI、中断策略/优先级、HDCP、显示容器启动和合格的传统遥测服务。每个都有其自己的先决条件和效果；这些并不是普遍的性能改进。

<a id="compatibility"></a>
## 兼容性

| 要求 | 详情 |
| --- | --- |
| 系统 | Windows 10 版本 19041 或更高版本 / Windows 11，x64 |
| GPU/驱动程序 | 兼容NVIDIA封装和检测到的硬件；自动目录查找主要涵盖已知的 GeForce 型号 |
| 运行时 | .NET 8 / WPF 8.0.31 包含在准备好的独立包中 |
| 特权 | 正常 UI/每用户设置；驱动程序安装和系统更改需要管理员访问权限 |
| 网络 | 在线 NVIDIA 查找/下载和显式上游 NVENC 请求所需；可选择本地原装驱动 |
| 包含的工具 | 未修改的 7-Zip 26.03、运行时通知、可选 MIT Profile Inspector 配套 |
| 可选同伴 | .NET Framework 4.8 用于单独的 Profile Inspector fork |

没有任意的最低驱动程序版本涵盖所有功能。多次 GPU 查找必须与每个检测到的 GPU 匹配。不受支持的/专业型号可能需要手动选择驱动程序。 NVIDIA 的安装程序仍然具有最终的硬件/操作系统权限。

<a id="installation"></a>
## 安装

1. 访问 [下载](../docs/downloads.md#nvdriverforge) 并确认版本已发布。
2. 选择 `NVDriverForge-Setup.exe` 进行安装，或选择 `NVDriverForge.exe` 进行便携式使用。
3. 将 SHA-256 与该版本的 `SHA256SUMS.txt` 进行比较。
4. 运行针对每用户安装和标准卸载程序的安装程序，或将可移植 EXE 放入可写文件夹中并打开它。

便携式包括其运行时和可选的安装程序。安装 NVDriverForge 不会安装 GPU 驱动程序。其 EXE 当前未签名。

<a id="usage"></a>
## 用途

1. **驱动程序：**从 NVIDIA 下载或选择原始 NVIDIA 安装程序 EXE。让分析结束。
2. **组件：**查看描述和所需的依赖项。未知成分被保留。
3. **调整：** 保留不需要的选项不变。在选择任何东西之前先阅读效果和权衡。
4. **检查：**检查确切的驱动程序、组件和可选操作，然后确认安装。
5. 仅针对您选择的操作接受 UAC。保留受保护作业的恢复说明。
6. 如果新驱动程序需要重新启动，请按照报告的状态进行操作。延迟的操作需要在重新启动后显式恢复。

Custom NV 启动时保持不变。选择单独的命名值或查看提供的预设及其排除项。它的两个信息内部字段不是独立编写的。设置仅应用于经过验证的新驱动程序工作流程，而不会通过打开预览来应用。不需要安装单独的 NVPI 编辑器。

可选的 NVENC 工作从固定的 keylase 提交下载兼容数据。它改变了两个驱动程序 DLL 并使它们的签名无效；它可以被 Windows、编码器、DRM 或反作弊拒绝。 NVDriverForge 中没有嵌入此类数据或 NVIDIA DLL。 [出处和许可限制](../docs/provenance.md)。

首选项控制语言、主题和可选的安装用户更新检查。便携式设备不会创建已安装的后台检查任务。工具和恢复与四个安装步骤是分开的。

<a id="screenshots"></a>
## 截图

![NVDriverForge驱动程序页面预览](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

现有 0.1.2 法语 UI 渲染以及示例数据；保留为界面预览。显示的 699.99 驱动程序是测试夹具，不是可供下载的真实版本。 [图片来源](../assets/README.md)。

<a id="update-and-uninstall"></a>
## 更新和卸载

关闭NVDriverForge，获取下一个官方包并验证其哈希值。对已安装的更新使用相同的安装程序标识；用新的 EXE 替换封闭的便携式 EXE。保留设置和受保护的作业。

Uninstall 与 Windows Installed apps。它会删除应用程序及其更新任务，而不是 NVIDIA 驱动程序。设置、日志和备份仍保留。如果需要，请在删除应用程序之前通过记录的恢复流程恢复高级/NVENC 更改。恢复拒绝来自其他工具的冲突更改。

本地数据在`%LOCALAPPDATA%\NVDriverForge`下；受保护的作业和驱动程序导出位于 `%PROGRAMDATA%\NVDriverForge\Jobs` 下。便携式使用还会创建本地数据。驱动程序存储区导出不是系统映像或完整配置文件备份。

<a id="known-limitations"></a>
## 已知的限制

- 无需添加硬件/INF 编辑、重新生成 NVIDIA 签名、反作弊兼容的辞职或自动接受未签名警告。
- 没有完整的遥测/广告删除、精简包导出或自动完全回滚到以前的驱动程序。
- 驱动程序安装、启动恢复和可选配置文件写入尚未通过集线器审核在真实机器上进行全面验证。
- 注册表回读并不能证明实际的 HDCP、性能或延迟影响。
- 签名检查使用本地可用的Windows信任；不执行在线撤销。
- 存在 34 种语言，但完整的母语/辅助功能测试仍然不完整。

<a id="troubleshooting"></a>
## 故障排除

| 症状 | 行动 |
| --- | --- |
| 在线目录不可用 | 从[NVIDIA驱动程序下载](https://www.nvidia.com/en-us/drivers/)中选择原包。请勿替换相邻的 GPU 型号。 |
| 修补程序查找不可用 | 使用 [NVIDIA 的 Game Ready 驱动程序论坛](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) 并验证实际包。 |
| NVIDIA安装失败 | 阅读故障摘要并打开详细日志。 0.1.3 中现有或不适用的可选组件仍可跳过。失败的安装不会触发可选的调整或成功/重新启动流程。 |
| 签名/哈希/备份失败 | 停止安装并保留错误；如果损坏，请重新获取原始包。 |
| 选项不可用 | 读取其硬件、组件或目标驱动程序原因；保持不变。 |
| 重新启动或作业仍待处理 | 使用工作的恢复说明和明确的简历；不要删除它的日志。 |
| 恢复冲突 | 另一种状态与记录的交易不同。保留它并请求帮助，而不是强制恢复。 |

对于报告，包括所选工具版本、Windows、GPU、驱动程序和可重现步骤；从日志中编辑路径和个人详细信息。 [支持](../docs/support.md)。

<a id="faq"></a>
## 常见问题解答

**安装程序是否安装图形驱动程序？** 不。这需要应用程序单独分析、审查、确认和提升安装过程。

**我需要 NVCleanstall 或 NVPI 吗？** 不需要。NVCleanstall 只是灵感。 Profile Inspector 伴侣是一个独立的可选编辑器。

**它是否会使每个 NVIDIA 驱动程序变得更小或更快？** 不会。所选组件和先决条件决定了可以更改的内容；不承诺测量增益。

**来源在哪里？** 应用程序特定的来源和私有测试是分开维护的。该中心提供归属/许可所需的文档、二进制文件和第三方源链接。

<a id="credits-and-upstream"></a>
## 学分和上游

原始应用程序、工作流程、交易、本地化、引导和改编：禅堂 Zendo (RevoluSound Team)。

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/)：工作流程灵感；没有导入源代码或二进制文件。
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector)：MIT 主题、扩展的 NVAPI 接口参考和单独封装的 fork。
- [7-Zip / Igor Pavlov](https://www.7-zip.org/)：未经修改的提取工具。
- [Microsoft .NET](https://github.com/dotnet/runtime) 和 [WPF](https://github.com/dotnet/wpf)：捆绑运行时。
- [Inno Setup](https://jrsoftware.org/isinfo.php)：原始安装程序引擎和可信翻译。
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch)：外部可选NVENC数据源；未建立再分发许可证。
- [NVIDIA](https://www.nvidia.com/en-us/drivers/)：外部驱动程序下载并安装 NVAPI/NVML 库。

[完整成分表](../THIRD_PARTY_NOTICES.md) · [变化和出处](../docs/provenance.md)

<a id="license"></a>
## 许可证

[现有的二进制分发权限](../../../../NVDriverForge/LICENSE) 允许使用和共享未经修改的官方可执行文件及其通知。保留特定于应用程序的源代码权利。它不限制单独的第三方许可证授予的权利。 [完整通知](LICENSES/README.md)。

独立于NVIDIA Corporation、TechPowerUp和keylase；未经他们赞助或正式认可。产品名称仍然是其所有者的商标。
