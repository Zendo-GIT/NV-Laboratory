<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · **日本語** · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# リポジトリのアーキテクチャとメンテナンス

NV Laboratory は、パブリック **ドキュメントおよびバイナリ配布ハブ**です。アプリケーションのソースは含まれません。 4 つのプロジェクトは、個別のビルド ツリー、バージョン、ID、およびリリース アセットを保持します。彼らのプライベートな開発履歴は、この Git リポジトリにはインポートされません。

<a id="layout"></a>
## レイアウト

| 場所 | 目的 |
| --- | --- |
| README.md / README.fr.md | 英語/フランス語のエントリーポイント |
| 4 つのプロジェクト フォルダー | 完全なガイドと該当する独自の通知 |
| ドキュメント | ダウンロード、互換性、来歴、開発およびリリース手順 |
| ドキュメント/releases.json | 監査済みの候補/リリースのメタデータ、サイズ、ハッシュ |
| ドキュメント/来歴 | ファイル/ハッシュの比較。アプリケーションコードがありません |
| ライセンス | サードパーティの完全なテキストとインストーラー翻訳者のクレジットを共有 |
| 資産 | 既存のレビュー済み UI プレビューとその来歴 |
| .github | 発行フォームと読み取り専用ドキュメントの検証 |
| ツール/validate_repository.py | 標準ライブラリの出版境界とリンクのチェック |

デフォルトの GitHub README は英語のままです。既存の隣接する `.fr.md` リンクは引き続き有効です。追加の翻訳は、`docs/languages/<code>` のドキュメントを反映しています。言語セレクターは、言語を切り替えるときに同じページを維持します。カタログ `docs/languages/catalog.json` には、34 言語すべてとソースのフィンガープリントが記録されます。 GitHub は、ブラウザ言語ごとに README を自動的に選択しません。 [言語インデックスと翻訳ポリシー](../../README.md)を参照してください。

<a id="application-technologies"></a>
## 応用技術

| プログラム | 民間技術 | 配布 |
| --- | --- | --- |
| NVPI fork | C#、WPF、.NET Framework 4.8、NVAPI/Windows 相互運用 | 完全なポータブル フォルダーと個別の Inno Setup |
| NVDriverForge | C#、WPF、.NET 8;ネイティブ C++ ブートストラップ。 7-Zipプロセス | 自己完結型のポータブル EXE とセットアップ |
| NVMFG Unlock40 | C#/WPF .NET 8、フレームワーク 4.8 ヘルパー、C++20/MASM/MinHook エンジン | ポータブルツリーとセットアップ |
| NVRasterPulse | C#/WPF フレームワーク 4.8; RTSS プロファイル/リロードの統合。ネイティブブートストラップ | ポータブルツリーとセットアップ |

このパブリック チェックアウトではアプリケーションを再構築できません。自動「Source code」アーカイブはハブ スナップショットです。上流のソース リンクは、プライベートで変更されたソースを正確に表すものではありません。パブリック CI はこのリポジトリのみを検証します。

<a id="local-checks"></a>
## ローカルチェック

リポジトリのルートから:

```text
python tools/validate_repository.py
```

Python 3.10 以降で十分です。このチェックでは、ファイル、ローカルの Markdown リンク、必須の通知/RTSS リンク、リリース メタデータ、およびパブリケーションの境界を読み取ります。ソフトウェアの実行、依存関係のインストール、ネットワークへの接続は行いません。

GitHub ワークフローは、プッシュ、プル リクエスト、または手動ディスパッチ時に、読み取り専用コンテンツ権限を使用してこれと同じチェックを実行します。チェックアウトは監査されたコミットに固定されており、資格情報は保持されません。リリースまたは展開ジョブは構成されていません。

<a id="maintain-the-boundary"></a>
## 境界線を維持する

英語のリファレンス、フランス語のガイド、および影響を受ける翻訳をまとめて更新します。実質的な変更は、書式設定のみの比較とは別にしてください。実際の候補ハッシュ、上流のコミット参照およびライセンスを記録します。プロジェクトの人気からライセンスを推測しないでください。

新しいバージョンのリリース資産を使用し、変更されたバイナリ、アーカイブ、埋め込まれた通知を再監査します。プライベート バックアップをこのリポジトリの外部に保存します。プライベート アプリケーション ソースまたはローカル ビルド フォルダーをインポートするためにパブリック ワークフローを使用しないでください。

アプリケーションの機能変更に適したテストは、プライベート プロジェクトで実行されます。ドライバー インストーラーを再実行したり、ドキュメントの更新用に実際のプロファイルを書き込んだりしないでください。 [手動解除手順](releasing.md)。
