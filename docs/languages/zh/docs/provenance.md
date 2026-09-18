<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · **简体中文** · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# 出处、变更和许可

此审核描述了 **2026-09-18** 准备的候选人。应用程序来源保持私密；公共清单包含文件名和哈希值，而不是源代码。请参阅 [完整组件通知](../THIRD_PARTY_NOTICES.md)。

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

参考：Orbmu2k/nvidiaProfileInspector提交`592d962cca8827efe8859461a84267755595064a`；候选可执行版本 3.0.2.3。参考提交和fork的程序集版本是不同的标识符；没有从 fork 版本推断出上游发行版本。

干净伴侣的 157 个源/资源文件与该提交进行了比较：2 个字节相同，134 个仅行结尾或 UTF-8 BOM 不同，11 个已修改，10 个在比较的上游路径中不存在。 “添加”是相对于该路径而言的，其本身并不能证明原作者身份。

[完整的文件/哈希比较](../../../provenance/nvpi-source-provenance.json).

| 面积 | 传承之作 | Fork 贡献 |
| --- | --- | --- |
| 个人资料编辑器 | 配置文件模型、导入/导出、应用程序关联和参考数据 | 与 Screen 和外部工具启动器集成 |
| NVAPI | Orbmu2k 的 DRS 互操作 | 颜色/显示相关的互操作、生产本机加载限制和模拟删除 |
| 显示服务 | Windows/NVIDIA API 作为外部接口 | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| 用户界面 | 上游 WPF 资源、调色板和图标 | 屏幕对话框、15 秒确认、状态/回读和工具栏布局 |
| 启动器 | 现有的应用程序外壳 | 受保护的单独安装的 RasterPulse 查找和启动 |
| 包装 | MIT上游 | 干净的独立伴侣，单独的安装程序/卸载程序，保留通知 |

公共源图包括用于可追溯的解决方案/资源路径；这些文件不作为源文件分发。开发测试、模拟接口和旧的组合 NVPI/RasterPulse 二进制文件不包括在内。

<a id="nvdriverforge"></a>
## NVDriverForge

独立的C#/.NET 8/WPF应用程序；面向用户的工作流程部分受到 NVCleanstall 的启发。在生产负载中未识别出 NVCleanstall 源/二进制文件。它不表示为该专有应用程序的 fork。

原始项目工作包括组件分析/选择、受保护的安装作业、备份和事务恢复、NVIDIA 目录下载、更新检查、本地化说明、可选高级/NVENC 工作流程和安装程序引导。

继承/改编的组件：四个 NVPI 主题调色板、扩展的 NVAPI DRS 接口参考以及单独可选的 MIT NVPI 配套组件。 Custom NV 预设的选择 UI 和白名单交易集成属于 NVDriverForge；该预设不是 NVIDIA 官方推荐。

7-Zip 26.03、.NET/WPF 8.0.31 和 Inno Setup 仍然按照自己的条款使用未修改的外部组件。 keylase NVENC 数据未嵌入；当用户请求兼容下载时，会选择并检查一个确切的提交。没有为该上游数据建立再分发许可证。

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40是由禅堂 Zendo (RevoluSound Team)独立开发的。维护人员使用RTX40MFG-Unlock进行比较和细化。该应用程序作为一个整体并不显示为其 fork。这种区别不会消除当前本机层中共享/改编组件的功劳。

比较参考：dashdogy/RTX40MFG-Unlock、Michael Robles、MIT、提交`4e776d068f91b4a665425542bb005dd57cc3d891`。私有本机引擎树包含 48 个比较文件：35 个仅格式差异、4 个修改文件和 9 个不在参考路径中。 [完整对比](../../../provenance/nvmfg-source-provenance.json)。

修改继承文件：`entry_detour.h`、`patcher.cpp`、`temporal_interval_trace.cpp`、`temporal_interval_trace.h`。其他路径包括 `game_selection.*`、`ngx_bootstrap.*`、`ngx_capability.h`、`presentation_tracker.h`、`vsync_observer.*` 和保留的上游许可证。

生产 C++ 单元：修补程序、midpoint_fix、dlssg_provider_policy、entry_detour、nvidia_mfg_policy、temporal_interval_trace、ngx_bootstrap、game_selection 和 vsync_observer；加上 entry_detour 组件和 MinHook 缓冲器/挂钩/蹦床/HDE64。继承的 ReShade 前端、遗留 shim 资源和未使用的 CMake 目标不属于此生产编译的一部分。

匹配组件涵盖修补/提供商策略和临时工作；他们的版权和许可声明保持不变。中央 NGX/引导程序/控制器协调、每游戏 V-Sync 处理、会话诊断和 Windows 应用程序/SDK/备份工作流程是 禅堂 Zendo (RevoluSound Team) 的项目工作。上面的计数描述了文件，包括第三方和未使用的文件，而不是作者百分比或任一项目想法的时间顺序。

该帮助程序将 NVPI 的 NvapiDrsWrapper 和 NativeArrayHelper 改编为单独的程序集，并具有项目编写的配置文件逻辑。旧的开发模拟路径被排除。共享系列调色板源自 NVPI。

MinHook参考：`8fda4f5481fed5797dc2651cd91e238e9b3928c6`；继承的编译子集在比较中没有功能性局部变化。 Streamline 集成接头：2.12；开放标头许可证已在 v2.12.0 上验证。 NGX 标头来源：NVIDIA/DLSS 提交 `a291cc7d2cc642a51566f3dfd5376f635cd1b284`。

候选引擎 SHA-256：`C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`。

engine.json 中所需的提供程序 SHA-256：`C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`。报告的 310.9 提供程序系列不能与此确切的哈希值互换。不包含提供程序 DLL 或模型。

**突出的许可点：** 完整的 NVIDIA RTX SDK 许可证（2024 年 3 月 14 日版本）包含与绕过技术限制相关的第 4(d) 节限制。审计并未授予此用途的许可。保留 MIT 引擎许可证、免费或遵守其他模组并不能解决该单独的情况。候选人准备不是法律许可。原来的短标题通知补充有完整的许可证；其 Windows-1252 文本也以可读的 UTF-8 形式提供，并保留原始字节。

针对 0.2.3 重新计算了本机比较：相同的 48 个文件和分类。自上次审核以来，`game_selection.cpp`、`game_selection.h` 和 `patcher.cpp` 的活动/能力观察发生了变化。新库、诊断、首选项、更新和选择工作流程属于维护者应用程序。组件许可证和所需的提供商哈希值保持不变。

<a id="nvrasterpulse"></a>
## NVRasterPulse

在 NVPI 派生存储库中开发的独立 RTSS 配置文件管理器。继承的 MIT UI 资源/调色板和项目来源仍然保留。生产应用程序明确使用提供的 MIT 许可证。

项目工作：精确的 RTSS 配置文件解析/写入和分数编码、备份、覆盖删除、重新加载桥、先决条件检测、紧凑的 UI、托盘生命周期、启动控制和本地化。 RTSS 执行实际限制。

未捆绑 RTSS 源、挂钩 DLL、SDK 或安装程序。该桥在现有的用户选择的 RTSS 安装中调用导出。此软件包中没有 NVIDIA 驱动程序包、本机实验限制器、Framepacer、MinHook、ReShade 或 DLSS 运行时。

<a id="assets-generated-data-and-tools"></a>
## 资产、生成的数据和工具

[资产信用](../assets/README.md) 识别现有界面预览和 NVPI 设置选择器。其中的虚构值已被标记。不会复制任何游戏/Nexus 资产、个人资料、私人 ICC、公司 NVIDIA 徽标或字体文件。

NVMFG 中继承的生成的游戏兼容性名称是一种检测辅助工具，而不是测试证据。生成的安装程序目录记入 [译者须知](../../../../licenses/INSTALLER-TRANSLATORS.md)。生成的带有绝对路径的构建记录保持私有。

私有构建工具包括.NET SDK/MSBuild、Visual Studio C++/MASM、Windows SDK、PowerShell、Inno Setup 和 Python 审核脚本。它们的编译器、标头、测试运行器和调试资产都没有分发。静态释放 CRT 仍遵循 Microsoft 的适用工具链条款。

<a id="scope-of-verification"></a>
## 验证范围

本地审计清点了三个开发根目录中的所有文件，但排除了 Git 对象数据库和链接目录目标。扫描了活动源/文档；历史版本已被清点并排除。扫描并散列选定的 ZIP 和当前有效负载； .NET 包已解压缩以进行额外检查。初次审核未运行任何产品、安装程序、游戏、RTSS 进程或驱动程序。

稍后的 NVPI 设置修订版 2 使用共享 Inno 控件和引导程序修复了独立语言选择。明/暗专用设备验证了鼠标和键盘导航以及所有 34 种显式语言代码。实际的安装选择器在从未显示的私人桌面上打开，并在安装前取消。其七个应用程序文件和便携式 ZIP 未更改。 NVDriverForge 0.1.3 包括更正的同伴，并且仍然转发 `/LANG`。

NVDriverForge 0.1.3于2026年9月10日完成。其私人验证报告记录了 366 项应用程序测试、118 项配套检查、32 项设置检查、156 项本机比较和 34 项语言转发案例。受保护的组件选择修复针对原始驱动程序包进行了重播，而无需更改其有效负载或安装驱动程序。这些是过时的产品团队结果，而不是通过此文档更新重新运行的测试或成功的实际驱动程序安装的证明。

此中心更新没有更改功能应用程序代码。早期的应用程序构建/单元/UI 测试仍然是过时的历史证据。这并不是对每个第三方二进制文件进行完全逆向工程，也不是针对每种可能的秘密模式的保证。

2026 年 9 月 18 日更新：NVDriverForge 0.1.4 添加了就绪检查、本机配置文件备份、组件指南、首选项和套件、详细结果、本地报告和应用程序更新。 NVRasterPulse 0.2 添加了配置诊断、FPS 指导、暂停/恢复、撤消、`.nvrp` 配置文件和收藏夹/隐藏，无需新的限制器引擎。单独的指南描述了用法和限制。静态集线器检查与 9 月 18 日私人报告中记录的应用程序测试是分开的；未为此集线器执行驱动程序安装、真实配置文件导入或延迟测量。
