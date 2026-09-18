<!-- nv-language-navigation:start -->
🌐 [English](../../../THIRD_PARTY_NOTICES.md) | [Français](../fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/THIRD_PARTY_NOTICES.md) · [বাংলা](../bn/THIRD_PARTY_NOTICES.md) · **简体中文** · [Čeština](../cs/THIRD_PARTY_NOTICES.md) · [Dansk](../da/THIRD_PARTY_NOTICES.md) · [Nederlands](../nl/THIRD_PARTY_NOTICES.md) · [English](../../../THIRD_PARTY_NOTICES.md) · [Filipino](../fil/THIRD_PARTY_NOTICES.md) · [Suomi](../fi/THIRD_PARTY_NOTICES.md) · [Français](../fr/THIRD_PARTY_NOTICES.md) · [Deutsch](../de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](../el/THIRD_PARTY_NOTICES.md) · [हिन्दी](../hi/THIRD_PARTY_NOTICES.md) · [Magyar](../hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](../id/THIRD_PARTY_NOTICES.md) · [Italiano](../it/THIRD_PARTY_NOTICES.md) · [日本語](../ja/THIRD_PARTY_NOTICES.md) · [한국어](../ko/THIRD_PARTY_NOTICES.md) · [मराठी](../mr/THIRD_PARTY_NOTICES.md) · [فارسی](../fa/THIRD_PARTY_NOTICES.md) · [Polski](../pl/THIRD_PARTY_NOTICES.md) · [Português](../pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](../pa/THIRD_PARTY_NOTICES.md) · [Română](../ro/THIRD_PARTY_NOTICES.md) · [Русский](../ru/THIRD_PARTY_NOTICES.md) · [Español](../es/THIRD_PARTY_NOTICES.md) · [Kiswahili](../sw/THIRD_PARTY_NOTICES.md) · [Svenska](../sv/THIRD_PARTY_NOTICES.md) · [தமிழ்](../ta/THIRD_PARTY_NOTICES.md) · [ไทย](../th/THIRD_PARTY_NOTICES.md) · [Türkçe](../tr/THIRD_PARTY_NOTICES.md) · [Українська](../uk/THIRD_PARTY_NOTICES.md) · [اردو](../ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](../vi/THIRD_PARTY_NOTICES.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="third-party-notices-and-credits"></a>
# 第三方通知和信用

初次审核：2026-09-09；当前包装和出处审查：2026-09-18。 NVDriverForge 0.1.4、NVMFG Unlock40 0.2.3 和 NVRasterPulse 0.2 保留现有组件许可证。 Profile Inspector 3.0.2.3/setup-r2 保持不变。 **组件的许可证涵盖该组件，而不是整个套件。**应用程序源保持私有。版权和许可通知均逐字保留；该表是一个索引，而不是它们的替代品。 “外部”是指不分布在应用程序资产中。

| 组件/原始项目 | 作者 | 官方网站、存储库或下载 | 许可/通知 | 在 NV Tools 中使用 | 修改 |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k；版权所有2016 | [存储库](https://github.com/Orbmu2k/nvidiaProfileInspector), [下载](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](../../../NVIDIA-Profile-Inspector/LICENSE) | 整个 NVPI fork； NVDF主题/扩展接口参考； NVMFG 包装器/样式； RP UI 资源 | Fork 显示服务、交易和启动器；主题/控制集成和包装改编 |
| RTX40MFG-Unlock | Michael Robles / dashdogy；版权所有 2026 | [存储库](https://github.com/dashdogy/RTX40MFG-Unlock), [下载](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](../../../NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | 比较/细化参考和共享/改编的NVMFG原生组件；自主开发的应用程序 | 中央加载、NGX/控制器协调、每游戏/V-Sync 集成和诊断 |
| MinHook，固定 8fda4f5 | Tsuda Kageyu；版权所有 2009–2017 | [存储库](https://github.com/TsudaKageyu/minhook), [固定来源](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2 条款通知](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | 静态编译成NVMFG引擎 | 除了针对继承副本的文本格式之外，包含的子集保持不变 |
| Hacker Disassembler Engine (HDE64) | Vyacheslav Patkov；版权所有 2008–2009 | [MinHook的源码合集](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [完整的 MinHook/HDE 通知](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | NVMFG 中的 MinHook 解码器 | 未发现功能变化；尽管生产使用 HDE64，但仍保留 HDE32 通知 |
| Streamline 2.12 集成接头连接器 | NVIDIA Corporation；版权所有 2023 | [存储库](https://github.com/NVIDIA-RTX/Streamline), [下载](https://github.com/NVIDIA-RTX/Streamline/releases) | [MIT 适用于符合条件的标头](../../../NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | 编译 NVMFG Streamline 集成 | 标题未修改；应用程序包中没有运行时DLL |
| NVIDIA NGX / DLSS SDK 标头 | NVIDIA Corporation | [固定存储库](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [NVIDIA RTX SDK 条款](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [标题通知](../../../NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | 编译 NVMFG NGX 集成 | 标题未修改；未捆绑 NGX 型号/提供商；未解决的限制如下所述 |
| .NET 运行时 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET 基金会、Microsoft 和贡献者 | [来源](https://github.com/dotnet/runtime), [下载](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-NET-LICENSE.txt) 和 [完整的第三方通知](../../../licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | 独立的 NVDF 和 NVMFG 应用程序/代理 | 运行时未修改 |
| WPF / Windows Desktop Runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET 基金会、Microsoft 和贡献者 | [来源](https://github.com/dotnet/wpf), [下载](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-WPF-LICENSE.txt)，上面的运行时通知 | NVDF 和 NVMFG 用户界面 | 框架未修改；应用程序 UI 单独编写/改编 |
| .NET框架4.8 | Microsoft | [官方运行时下载](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | Microsoft 平台/运行时术语；外部的 | NVPI、RP 和 NVMFG 配置文件助手 | 无；该集线器没有重新分发安装程序或框架 DLL |
| 7-Zip 26.03 x64 | Igor Pavlov；版权所有 1999–2026 | [网站/下载](https://www.7-zip.org/download.html), [确切的源存档](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | [完整通知](../../../licenses/third-party/7-Zip.txt)、[LGPL 2.1-or-later](../../../licenses/third-party/LGPL-2.1.txt)、BSD 部分和 unRAR 限制 | NVDF 嵌入未修改的 7z.exe/7z.dll 并将 CLI 作为单独的进程运行 | 无修改 |
| Inno Setup 7.1.0 | Jordan Russell、Martijn Laan 和贡献者 | [网站/下载](https://jrsoftware.org/isinfo.php), [来源](https://github.com/jrsoftware/issrc) | [原始 Inno Setup 许可证](../../../licenses/third-party/Inno-Setup.txt) | 安装程序引擎和生成的卸载程序 | 引擎/编译器未修改；项目脚本、品牌和本地焦点处理经过调整 |
| Inno Setup 翻译目录 | 指定原译者 | [官方收藏](https://jrsoftware.org/files/istrans/) | Inno/目录通知和 [完整的标题学分](../../../licenses/INSTALLER-TRANSLATORS.md) | 所有四个安装程序共享 34 种语言目录，包括 NVPI 安装修订版 2 | 按键、ID、字体、技术英语后备；根据需要提供项目创作的预览目录 |
| Microsoft Visual C++ 运行时/Windows SDK 支持 | Microsoft | [可视化Studio工具](https://visualstudio.microsoft.com/downloads/), [再分配条件指数](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft 工具链/运行时术语；此表不是 MIT | 本机引擎/引导程序二进制文件中的静态释放 CRT；已安装 Windows API | 没有运行时源更改；没有分布式编译器、SDK 或调试运行时 |
| RivaTuner Statistics Server (RTSS) | Unwinder | [官方Guru3D下载](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | 供应商条款；没有从“免费软件”推断出重新分发许可 | RP 所需的外部限制器；安装 UpdateProfiles 导出 | 未修改或捆绑 RTSS 代码/二进制文件； RP 写入选定的配置文件密钥 |
| NVIDIA 驱动程序 / NVAPI / NVML | NVIDIA Corporation | [驱动程序下载](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA 驱动程序/SDK 条款；外部的 | 安装的本机接口和显式的原始驱动程序下载 | 集线器资产中没有 NVIDIA DLL； NVDF的可选NVENC操作修改用户选择的安装的DLL |
| NVIDIA NGX 提供程序/模型和 Streamline 运行时 | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Streamline 发布](https://github.com/NVIDIA-RTX/Streamline/releases) | 组件特定的 NVIDIA 术语，与 MIT 标头不同 | NVMFG 使用的外部游戏/驱动程序组件；仅根据请求获取 SDK | NVMFG 应用实验性内存中行为变化； SDK 游戏副本可以通过备份进行更新 |
| keylase/nvidia-patch | keylase 和贡献者 | [存储库](https://github.com/keylase/nvidia-patch), [Windows数据](https://github.com/keylase/nvidia-patch/tree/master/win) | 本次审核未建立再分发许可证 | 外部可选 NVDF NVENC 目录/补丁数据，从每个选择的一个固定提交中获取 | 没有将上游源、修补程序或修补程序数据复制到集线器/应用程序资产中 |
| NVCleanstall | TechPowerUp | [官方页面/下载](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | 专有分销；未推断出源代码/二进制重新分发权限 | NVDF 的工作流程和选项灵感 | 没有导入源代码或二进制文件；不是 fork 或运行时依赖项 |

<a id="obligations-and-boundaries"></a>
## 义务和界限

**MIT 组件：** 保留版权、许可文本和免责声明及其副本。他们的许可证不要求发布修改后的源代码。即使应用程序源是私下维护的，原始作者身份也会得到保留。

**MinHook/HDE：** 在二进制文档中保留通知、条件和免责声明。提供完整的合并通知。

**7-Zip：** 保留 LGPL/BSD/unRAR 通知并提供对确切的未修改源的访问。上面链接了源存档以及完整的 LGPL。 unRAR限制适用于相关解压代码；这不是一揽子 MIT 依赖项。参见作者的[分销常见问题解答](https://www.7-zip.org/faq.html)。

**Inno Setup：** 保留所需的引擎版权/网站声明并在适用的情况下标记源更改。未经修改的引擎的积分仍保留在安装程序中。改编后的目录保留原始来源声明；名称已在此处建立索引。

**NVIDIA 材料：** Streamline 集成标头的 MIT 许可证并不涵盖每个 SDK 文件。其通知明确区分了 Nsight Perf SDK 材料；该生产目标中未使用该材料。 NGX 标头遵循 NVIDIA 的专有 RTX SDK 条款。他们的全文已添加，并带有 [原始字节副本](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt)。第 4(d) 节有关 NVMFG 使用技术限制的限制仍未得到解决。没有从另一个模组的存在中推断出肯定的许可。

**外部未知/专有组件：** RTSS、NVCleanstall、NVIDIA 驱动程序、模型和 keylase 补丁数据未捆绑在准备好的集线器资产中。链接可识别其实际所有者。用户触发的下载不会重新许可组件。

这些工具使用 Windows 提供的 API 和字体。没有 Windows SDK/compiler/font 文件复制到此 Git 存储库中。构建工具和私有测试不在分发范围内。运行时内部组件通知保留在完整的 Microsoft 通知文件中，而不是重新分配给发布者。

<a id="publisher-contributions"></a>
## 出版商的贡献

禅堂 Zendo (RevoluSound Team) 保留了 [出处指南](docs/provenance.md) 中描述的原始应用程序工作、改编和文档。 [NVPI](NVIDIA-Profile-Inspector/README.md)、[NVDF](NVDriverForge/README.md)、[NVMFG](NVMFG-Unlock40/README.md) 和 [RP](NVRasterPulse/README.md) 分别区分继承的工作和更改。

独立项目；不暗示与 NVIDIA Corporation 或列出的上游作者有任何隶属关系、赞助或官方认可。
