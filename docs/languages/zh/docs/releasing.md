<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · **简体中文** · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 机器辅助英语翻译。保留技术名称、命令、URL 和原始法律文本。欢迎母语人士审阅；如果措辞不清楚，请查阅英文参考资料。
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# 出版与发行

公共存储库是 **Zendo-GIT/NV-Laboratory**。文档更改由维护人员使用 **GitHub Desktop** 进行审查、提交和推送。本地提交不上传文件。二进制包是单独的 GitHub 发布资产；它们从不属于 Git 更改列表。

<a id="documentation-updates"></a>
## 文档更新

1. 打开 GitHub Desktop 中的 **NV-Laboratory** 文件夹。
2. 查看文档、通知、图像、JSON 元数据和文档验证器。
3. 从该文件夹运行 `python tools/validate_repository.py`。
4. 提交已审核的更改，然后使用 **Push origin**。检查操作结果。
5. 保留公共作者身份 **禅堂 Zendo (RevoluSound Team)** 和帐户的 GitHub `noreply` 地址。

切勿选择父开发工作区、私有审核目录或二进制附件目录。 [承诺电子邮件隐私](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)。

<a id="independent-application-releases"></a>
## 独立应用发布

| 工具 | 标签 | 版本政策 |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | 现有的四部分应用程序版本；安装程序修订版 2 有自己的文件名 |
| NVDriverForge | nvdriverforge-v0.1.4 | 现有0.x方案；版本化更新保留早期的包 |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | 应用程序版本0.2.3；自公开 0.1.1 以来的累积变化 |
| NVRasterPulse | nvrasterpulse-v0.2 | 现有的两部分版本 |

维护者可以直接发布或授权助手发布审计后的资产。公开内容明确；没有工作流程会在每次提交时创建一个发布。

1. 查看当前的预发布报告、二进制文件来源、许可证和 SHA-256 值。
2. 针对已审核的中心提交，为工具的标签创建草稿。包括准备好的特定于版本的发行说明。
3. 仅附加该版本的安装程序/便携式资产 `Licenses-and-Credits.zip` 和 `SHA256SUMS.txt`。
4. 检查兼容性、安装、依赖性、更改和已知限制。使 RTSS 保持在 NVRasterPulse 的显着位置。
5. 发布，验证公共资产 URL、大小和哈希，并在 `docs/releases.json` 中记录实际发布日期。
6. 更新下载页面和翻译，然后在 GitHub Desktop 中提交/推送其更改。

每个项目标签链接避免通过共享 `releases/latest` 链接将用户发送到另一个工具。 GitHub 的自动 **Source code** 存档包含此文档中心。应用程序源保持私密。原始组件通知保持不变，并且版本不会解决 NVMFG 记录的 NVIDIA SDK 保留。


9月18日更新准备了三个新标签；现有 Profile Inspector 版本保持不变。资产名称、标签和 `SHA256SUMS.txt` 必须保持准确，以便进行应用程序更新检查。发布不带预发布标志的正常版本，以将其暴露给稳定版本检查； NVMFG 仍处于实验阶段。

<a id="integrity-and-storage"></a>
## 完整性和存储

切勿默默地替换已发布的二进制字节。使用具有新哈希值的新显式版本或安装程序修订版。法律边车补充了嵌入式通知。 NVDriverForge 0.1.4 可移植为 142,017,891 字节，高于 GitHub 的普通 100 MiB Git 文件限制。发布附件避免将二进制文件或 Git LFS 放入此中心。 [GitHub大文件指导](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。

应在存储库安全设置中启用私有漏洞报告。在将敏感报告发送到那里之前验证其可用性； [SECURITY.md](../SECURITY.md) 提供了一个不会暴露漏洞详细信息的后备方案。

[下载目录](downloads.md) · [GitHub 发布文档](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
