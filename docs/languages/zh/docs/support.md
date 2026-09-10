<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · **简体中文** · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# 兼容性和故障排除

这些是准备好的候选者，而不是所有 Windows、GPU、驱动程序和游戏组合的认证矩阵。

| 工具 | Windows / 运行时 | 硬件/外部依赖 | 需要护理的操作 |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64，.NET Framework 4.8 | 兼容的 NVIDIA 驱动程序/显示器 | 配置文件写入并显示预览 |
| NVDriverForge 0.1.2 | Windows 10 版本 19041+ / 11 x64；包含.NET/WPF | 兼容的NVIDIA驱动包 | 高架安装，高级设置，可选NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64；包含 .NET/WPF，框架 4.8 帮助程序 | RTX 40，合格的 DLSS FG 游戏和固定提供商 | 本机游戏内补丁、全局档案日志、SDK 游戏更新 |
| NVRasterPulse 0.1 | Windows 10/11 x64，.NET Framework 4.8 | RTSS已安装；争夺帽子 | RTSS 每个可执行配置文件更改 |

没有准备ARM64包。显示/API 可用性和旧的 Windows 版本可能会限制个别功能。没有发明通用的最低 NVIDIA 或 RTSS 版本。确切的 NVMFG 提供程序哈希位于 [出处](provenance.md) 中。

<a id="before-reporting-a-bug"></a>
## 报告错误之前

确定您打开的确切可执行文件/版本。以前安装的副本不一定是新下载的 ZIP 的版本。记录重现步骤、预期结果和实际结果。对于渲染/限制问题，包括游戏版本、显示刷新、FG/V-Sync/VRR 状态以及任何其他限制器或覆盖。

使用 [错误形式](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml)。切勿附加整个私有开发文件夹、驱动程序存档、模型、游戏 DLL、注册表转储或未经审查的日志集合。

| 问题 | 首先检查 |
| --- | --- |
| 应用程序版本错误 | 确认EXE身份并发布哈希值；替换之前关闭旧副本。 |
| 运行时/启动错误 | 安装所需的框架 4.8 或保留所有提供的便携式子文件夹。 |
| UAC 已取消 | 仅重试预期的操作；取消是指安装不成功。 |
| 哈希/签名不匹配 | 停止使用该候选者并获取预期的官方字节。 |
| NVPI 颜色/模式被拒绝 | 恢复并使用实际显示器/驱动程序支持的组合。 |
| NVDF 备份或恢复失败 | 保留受保护的工作和 RECOVERY.txt；不要擦除日志或强制执行冲突的写入。 |
| NVMFG 待定设置 | 解决游戏关闭时的恢复问题，保留其他工具的更改。 |
| RP 上限无效 | 运行RTSS，识别真实游戏EXE，检查钩子状态和竞争限制。 |
| RP 盖子在移除后仍然存在 | 检查RTSS全局；删除仅更改本地限制器覆盖。 |

<a id="logs-and-privacy"></a>
## 日志和隐私

| 工具 | 本地数据供审核，不批量上传 |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`；受保护的作业 `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`；备份`%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`； EXE 旁边的 `Sessions` |
| RP | `%LOCALAPPDATA%\NVRasterPulse`； `Backups\RTSS` 下面 |
| NVPI | 您选择的导出和显示的错误；没有发明通用日志路径 |

从您共享的文本/图像中删除帐户名称、主目录、游戏库路径、设备标识符、令牌和不相关的窗口。将原件保密以便恢复。公共问题对每个人来说都是可见的。

对于漏洞、危险的特权行为或意外的破坏性操作，请关注 [SECURITY.md](../SECURITY.md)，而不是公开发布详细信息。

<a id="what-has-been-verified"></a>
## 已验证什么

对于集线器准备，运行了静态有效负载/ZIP/哈希/元数据扫描和文档检查。现有的私有应用程序构建/单元/UI 测试是历史的、过时的证据。在此准备过程中，未执行驱动程序安装、显示更改、实时 RTSS 操作或游戏基准测试。

“检测到”、“写入”、“重新加载”、“可用能力”和“在游戏中测量”是不同的结果。报告您观察到的情况。
