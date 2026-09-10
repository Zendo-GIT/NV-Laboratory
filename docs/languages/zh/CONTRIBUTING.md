<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · **简体中文** · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# 贡献

NV Laboratory 由 禅堂 Zendo (RevoluSound Team) 维护。维护者决定接受和发布什么。提出问题或拉取请求并不意味着贡献被接受或授权分发。

使用错误或功能表格并识别程序/版本。首先搜索现有问题。在准备重大贡献之前讨论重大变化。对于安全问题，请遵循 [SECURITY.md](SECURITY.md)。

该公共中心包含文档、通知、发布元数据和存储库验证。应用程序源和测试是私人维护的。请勿提交反编译代码、私人源代码、凭据、用户配置文件或可执行有效负载。

文档 PR 应保持 34 种语言对应项和导航一致，保留命令/文件/产品名称，并描述实际行为。新的屏幕截图必须是您自己的、经过版本识别且不含个人详细信息的；合成数据必须被标记。为每个新的第三方资产提供来源和许可。

使用 UTF-8、LF、可读的 Markdown 和小的重点更改。 Python 验证器仅使用标准库。匹配其现有样式，避免不必要的依赖，然后运行：

```text
python tools/validate_repository.py
```

对于发布元数据更改，请包括经过审核的二进制文件中的确切版本/标签、文件大小和 SHA-256，并保持下载页面一致。应用程序更改需要适合受影响行为的私有构建/测试；文档检查不是应用程序测试。切勿捏造历史测试结果或收益。

通过贡献原始集线器材料，即表示您同意 [许可证](../../../LICENSE) 中的范围 MIT 许可证。保留第三方通知并识别您的更改；不要更换上游许可证。接受和发布仍然是维护者的决定。
