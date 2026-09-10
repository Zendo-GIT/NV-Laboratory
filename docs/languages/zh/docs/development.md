<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · **简体中文** · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# 存储库架构和维护

NV Laboratory 是一个公共**文档和二进制分发中心**。它不包含应用程序源。这四个项目保留单独的构建树、版本、身份和发布资产。他们的私人开发历史记录不会导入到此 Git 存储库中。

<a id="layout"></a>
## 布局

| 地点 | 目的 |
| --- | --- |
| README.md / README.fr.md | 英语/法语入口点 |
| 四个项目文件夹 | 完整的指南和适用的原始通知 |
| 文档 | 下载、兼容性、出处、开发和发布程序 |
| 文档/releases.json | 审核候选/发布元数据、大小和哈希值 |
| 文档/出处 | 文件/哈希比较；没有申请代码 |
| 许可证 | 共享完整的第三方文本和安装程序翻译人员积分 |
| 资产 | 现有经过审查的 UI 预览及其出处 |
| .github | 签发表格和只读文档验证 |
| 工具/validate_repository.py | 标准库发布边界和链接检查 |

英文版仍然是默认的 GitHub README。现有的相邻 `.fr.md` 链接保持有效。其他翻译反映了 `docs/languages/<code>` 下的文档；切换语言时，语言选择器保持相同页面。目录 `docs/languages/catalog.json` 记录了所有 34 种语言和源指纹。 GitHub 不会按浏览器语言自动选择自述文件。请参阅 [语言索引和翻译政策](../../README.md)。

<a id="application-technologies"></a>
## 应用技术

| 节目 | 私有技术 | 分布 |
| --- | --- | --- |
| NVPI fork | C#、WPF、.NET Framework 4.8、NVAPI/Windows 互操作 | 完整的便携式文件夹和单独的 Inno Setup |
| NVDriverForge | C#、WPF、.NET 8；本机 C++ 引导程序； 7-Zip进程 | 独立的便携式 EXE 和安装程序 |
| NVMFG Unlock40 | C#/WPF .NET 8、框架 4.8 帮助程序、C++20/MASM/MinHook 引擎 | 便携式树和设置 |
| NVRasterPulse | C#/WPF 框架 4.8； RTSS 配置文件/重新加载集成；本机引导程序 | 便携式树和设置 |

此公共结账无法重建应用程序。自动“Source code”存档是中心快照。上游源链接并不代表确切的私有修改源。公共 CI 仅验证此存储库。

<a id="local-checks"></a>
## 本地检查

从存储库根目录：

```text
python tools/validate_repository.py
```

Python 3.10 或更新版本就足够了。检查读取文件、本地 Markdown 链接、所需通知/RTSS 链接、发布元数据和发布边界。它不执行软件、安装依赖项或连接网络。

GitHub 工作流程在推送、拉取请求或手动调度时使用只读内容权限运行相同的检查。签出固定到经过审核的提交，并且不会保留凭据。未配置发布或部署作业。

<a id="maintain-the-boundary"></a>
## 维持边界

一起更新英文参考、法文指南和受影响的翻译。将实质性更改与仅格式化的比较分开。记录实际候选哈希值、上游提交参考和许可证；永远不要从项目的受欢迎程度来推断许可证。

使用新版本的发布资产并重新审核更改的二进制文件、存档和嵌入的通知。在此存储库之外保留私有备份。不要使用公共工作流程导入私有应用程序源或本地构建文件夹。

适合在私有项目中运行的功能应用程序更改的测试。不要重新运行驱动程序安装程序或为文档更新编写真实的配置文件。 [手动释放程序](releasing.md)。
