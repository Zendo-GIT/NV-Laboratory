<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · **日本語** · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# 出版とリリース

パブリック リポジトリは **Zendo-GIT/NV-Laboratory** です。ドキュメントの変更は、**GitHub Desktop** を使用してメンテナによってレビュー、コミット、プッシュされます。ローカルコミットではファイルはアップロードされません。バイナリ パッケージは個別の GitHub リリース アセットです。これらは Git 変更リストには決して含まれません。

<a id="documentation-updates"></a>
## ドキュメントの更新

1. GitHub Desktop の **NV-Laboratory** フォルダーを開きます。
2. ドキュメント、通知、画像、JSON メタデータ、およびドキュメント検証ツールを確認します。
3. そのフォルダーから `python tools/validate_repository.py` を実行します。
4. 確認した変更をコミットし、**Push origin** を使用します。アクションの結果を確認します。
5. 公開作成者 ID **禅堂 Zendo (RevoluSound Team)** とアカウントの GitHub `noreply` アドレスを保持します。

親開発ワークスペース、プライベート監査ディレクトリ、またはバイナリ添付ディレクトリは決して選択しないでください。 [電子メールのプライバシーを守る](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)。

<a id="independent-application-releases"></a>
## 独立したアプリケーションのリリース

| ツール | タグ | バージョンポリシー |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | 既存の 4 部構成のアプリケーション バージョン。セットアップ リビジョン 2 には独自のファイル名があります |
| NVDriverForge | nvdriverforge-v0.1.3 | 既存の 0.x スキーム。バージョン管理された更新では以前のパッケージが保持されます |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2 候補は、新しいアプリケーション バージョンを作成せずに正確なハッシュによって特定される |
| NVRasterPulse | nvrasterpulse-v0.1 | 既存の 2 部構成バージョン |

メンテナは直接公開することも、アシスタントに監査済みのアセットを公開する権限を与えることもできます。出版は明示的です。コミットごとにリリースを作成するワークフローはありません。

1. 現在の公開前レポート、バイナリのソース、ライセンス、および SHA-256 値を確認します。
2. レビュー済みのハブ コミットを対象として、ツールのタグのドラフトを作成します。準備されたバージョン固有のリリース ノートを含めます。
3. そのバージョンのセットアップ/ポータブル アセット、`Licenses-and-Credits.zip` および `SHA256SUMS.txt` のみを接続します。
4. 互換性、インストール、依存関係、変更、既知の制限を確認します。 RTSS を NVRasterPulse に対して目立つようにします。
5. 公開し、公開アセットの URL、サイズ、ハッシュを確認し、実際の公開日を `docs/releases.json` に記録します。
6. ダウンロード ページと翻訳を更新し、GitHub Desktop で変更をコミット/プッシュします。

プロジェクトごとのタグ リンクにより、共有 `releases/latest` リンクを通じてユーザーが別のツールに送信されることが回避されます。 GitHub の自動 **Source code** アーカイブには、このドキュメント ハブが含まれています。アプリケーションのソースは非公開のままです。元のコンポーネントの通知はそのまま残り、リリースでは NVMFG の文書化された NVIDIA SDK 予約は解決されません。

<a id="integrity-and-storage"></a>
## 完全性と保管

パブリッシュされたバイナリ バイトをサイレントに置き換えないでください。新しいハッシュを含む新しい明示的なバージョンまたはインストーラー リビジョンを使用します。合法的なサイドカーは埋め込み通知を補足します。 NVDriverForge 0.1.3 ポータブルは 141,760,351 バイトで、GitHub の通常の 100 MiB Git ファイル制限を超えています。添付ファイルをリリースすると、このハブにバイナリまたは Git LFS を配置することがなくなります。 [GitHub 大きなファイルのガイダンス](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。

プライベート脆弱性レポートは、リポジトリのセキュリティ設定で有効にする必要があります。機密レポートを送信する前に、その可用性を確認してください。 [SECURITY.md](../SECURITY.md) は、脆弱性の詳細を公開しないフォールバックを提供します。

[カタログダウンロード](downloads.md) · [GitHub リリース ドキュメント](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
