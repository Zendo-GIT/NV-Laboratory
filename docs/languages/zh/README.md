<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · **简体中文** · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools by 禅堂 Zendo (RevoluSound Team)。** 四个独立的 Windows 实用程序，用于 NVIDIA 驱动程序配置文件、驱动程序安装、实验性 Multi Frame Generation 和 RTSS 帧限制。

[获取工具](docs/downloads.md) · [安装](docs/installation.md) · [兼容性和帮助](docs/support.md) · [积分和许可证](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse 需要 RTSS。** 首先安装 [来自 Guru3D 的 RivaTuner Statistics Server](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)。 RTSS 必须运行才能使其 FPS 限制发挥作用。它是单独下载的。

<a id="projects"></a>
## 项目

| 项目 | 目的 | 版本 | 文档 | 下载 |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA 驱动程序配置文件编辑器添加了显示、颜色、HDR 和 ICC/WCS 控件。以前是 NVPI Custom。 | 3.0.2.3 | [指南](NVIDIA-Profile-Inspector/README.md) | [套餐](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | 选择驱动程序组件，查看可选调整并安装原始 NVIDIA 驱动程序包。 | 0.1.3 | [指南](NVDriverForge/README.md) | [套餐](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | 实验性 RTX 40 MFG 工具，具有每个游戏的选择和 Streamline SDK 维护。 | 0.1.1 | [指南](NVMFG-Unlock40/README.md) | [包裹和状态](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | 管理每个可执行文件的 RTSS FPS 限制，包括小数值、备份和托盘访问。 | 0.1 | [指南](NVRasterPulse/README.md) | [套餐](docs/downloads.md#nvrasterpulse) |

**下载：** [下载页面](docs/downloads.md) 列出了每个版本的状态、文件和 SHA-256 值。项目指南中描述了实验功能和兼容性限制。

<a id="start-here"></a>
## 从这里开始

1. 选择上面的一种工具。各自独立工作；无需安装整个套件。
2. 阅读其要求并为已安装的应用程序选择“**安装**”，或为单独的文件夹选择“**便携式**”。
3. 当其版本发布时，下载指定的应用程序资产，阅读随附的通知并比较其 SHA-256。
4. 在更改驱动程序、显示设置、NVIDIA 配置文件或游戏运行时之前保留备份。

通过每个指南顶部的选择器，可以获得与 NV 应用程序相同的 34 种语言的文档。 GitHub 不会按浏览器语言自动选择自述文件。文档语言和应用程序自己的语言设置是分开的。

<a id="provenance-and-ownership"></a>
## 出处和所有权

该中心分发文档和编译的应用程序。应用程序源代码是私人维护的。上游项目保留其作者身份和许可；私人来源分发不会取代这些条款。

- Profile Inspector fork 保留 Orbmu2k 的 MIT 许可证，并明确标识为 fork。
- NVDriverForge 具有自己的二进制分发条款，并包括单独许可的运行时/工具组件。
- NVMFG Unlock40是一款独立开发的应用程序。参考RTX40MFG-Unlock进行比较和细化；共享的本机组件保留其 MIT 积分。 MinHook 和 NVIDIA SDK 术语保持独立。
- NVRasterPulse 保留提供的 MIT 许可证并归功于 Profile Inspector 派生的 UI。 RTSS 是必需的外部程序。

请参阅 [完整的成分表](THIRD_PARTY_NOTICES.md)、[文件来源和更改](docs/provenance.md) 和 [许可范围](../../../LICENSE)。

<a id="other-projects--revolusound-team"></a>
## 其他项目 – RevoluSound Team

这些是单独的音频模组项目，在此处链接可帮助您发现团队的工作。

| 游戏 | 项目 | 关于 |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | 车辆声音变化涵盖发动机、排气、进气和涡轮效果。 |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | 该团队后来的 FH5 车辆音频包。 |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | 早期的 FH5 包；它的 Nexus 页面将访问者引导至上面的后来的团队包。 |

标题位于链接的 Nexus Mods 页面之后。他们的下载、要求、积分和权限保留在 Nexus Mods 上。

<a id="help-and-participation"></a>
## 帮助和参与

[报告错误或建议功能](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [贡献](CONTRIBUTING.md) · [安全报告](SECURITY.md) · [变更日志](CHANGELOG.md)

对于安全问题，请在发布日志或技术详细信息之前阅读 SECURITY.md。存储库发布后，维护者必须启用私人报告。

> **独立社区项目。** NV Laboratory、NV Tools 和这些实用程序不隶属于 NVIDIA Corporation、不受其赞助或正式认可。 NVIDIA、GeForce、RTX、DLSS 和其他产品名称是其各自所有者的商标。名称描述了兼容性和出处，而不是官方认可。
