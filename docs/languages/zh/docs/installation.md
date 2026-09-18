<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · **简体中文** · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# 安装指南

从 [下载](downloads.md) 开始，它记录发布状态和确切的资产名称。这些是单独的工具：仅安装您需要的工具。

> **对于 NVRasterPulse，请在打开配置文件管理器之前安装 [来自 Guru3D 的 RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)。**
> RTSS 必须运行才能应用限制；它不包含在 NV Tools 中。

| 工具 | 装机版 | 便携版 | 主要先决条件 |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | 提取完整的 NVPI ZIP | NVIDIA 驱动程序和 .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe，包括运行时 | 兼容原装NVIDIA驱动包进行安装操作 |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | 提取完整的 NVMFG ZIP，保留子文件夹 | RTX 40、现有 DLSS FG、精确提供程序和 .NET Framework 4.8 帮助程序 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | 提取完整的 RP ZIP | RTSS 和 .NET Framework 4.8 |

<a id="download-verify-install"></a>
## 下载、验证、安装

1. 在所选的已发布版本上，下载其指定的应用程序资产，注意 ZIP 和 SHA256SUMS.txt。
2. 使用 [SHA-256 示例](downloads.md#sha-256) 和实际下载的文件名。
3. 对于安装程序，请按照正常安装程序进行操作。对于便携式 ZIP，将所有内容提取到新的本地可写文件夹中；不要从 ZIP 内部运行。
4. 打开应用程序自己的 EXE。保留随附的许可证/配置/数据文件。
5. 在启用设置或系统操作之前，请阅读该工具的使用说明。

当前的二进制文件未签名。匹配的哈希值确认了预期的字节；它不是安全或兼容性证书。不要仅仅为了抑制警告而禁用 Windows 安全保护。

安装 NVDF 或其可选的 NVPI 配套产品与安装 GPU 驱动程序是分开的。 NVPI 配套保留其现有的内部安装名称。其升高的 RasterPulse 按钮​​需要受保护的系统范围安装；其他 RP 副本可以通过自己的快捷方式打开。

NVMFG 是实验性的，具有 [记录 NVIDIA SDK 许可保留](provenance.md)。不包含 NVIDIA 驱动程序、NGX 提供程序/模型或游戏 Streamline 运行时。选定的 SDK 下载和游戏更新是明确分开的操作。

<a id="language-and-updates"></a>
## 语言和更新

使用自述文件的 34 种语言选择器来获取文档。 NVDF、NVMFG 和 RP 有自己的 34 种语言 UI 设置； NVPI 保留现有的语言支持。一些安装程序技术字符串会回退为英语。

更新时保留工具的安装标识。首先关闭它并保留备份。对于 NVMFG，关闭受影响的游戏并解决待处理的配置文件恢复问题。对于便携式更新，请使用新文件夹而不是组合版本。

<a id="removing-a-tool"></a>
## 移除工具

卸载应用程序不会自动撤消其设置。

- **NVPI：** 如果需要，在删除之前恢复预期的配置文件/显示设置。
- **NVDF：**如果要恢复高级/NVENC 更改，请先使用恢复。 Uninstall 保留图形驱动程序、设置和备份。
- **NVMFG：** 关闭游戏、禁用/退出控制器、解决 NVIDIA 恢复问题并在删除之前恢复所需的游戏 SDK 备份。
- **RP：** 首先删除预期的限制器覆盖。 Uninstall 不会擦除已保存的 RTSS 上限或删除 RTSS。

请参阅每个 [项目指南](../README.md#projects) 以了解确切的数据位置和限制，如果恢复步骤失败，请参阅 [支持](support.md)。
