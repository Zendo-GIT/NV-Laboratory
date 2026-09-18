<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · **日本語** · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# 互換性とトラブルシューティング

これらは準備された候補であり、すべての Windows、GPU、ドライバー、およびゲームの組み合わせの認定マトリックスではありません。

| ツール | Windows / ランタイム | ハードウェア/外部依存関係 | 注意が必要な手術 |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64、.NET フレームワーク 4.8 | 互換性のあるNVIDIAドライバー/ディスプレイ | プロファイルの書き込みとプレビューの表示 |
| NVDriverForge 0.1.4 | Windows 10 ビルド 19041+ / 11 x64; .NET/WPFが含まれています | 互換性のあるNVIDIAドライバーパッケージ | 昇格されたインストール、詳細設定、オプションの NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF が含まれ、フレームワーク 4.8 ヘルパー | RTX 40、対象となる DLSS FG ゲームおよび固定プロバイダー | ネイティブゲーム内パッチ適用、グローバルプロファイルジャーナル、SDK ゲームアップデート |
| NVRasterPulse 0.2 | Windows 10/11 x64、.NET フレームワーク 4.8 | RTSS がインストールされています。キャップを目指して走っています | RTSS 実行可能ファイルごとのプロファイルの変更 |

ARM64パッケージは用意されていません。ディスプレイ/API の可用性と古い Windows バージョンにより、個々の機能が制限される場合があります。汎用の最小 NVIDIA または RTSS バージョンは作成されていません。正確な NVMFG プロバイダーのハッシュは [来歴](provenance.md) にあります。

<a id="before-reporting-a-bug"></a>
## バグを報告する前に

開いた正確な実行可能ファイル/バージョンを特定します。以前にインストールされたコピーが、新しくダウンロードされた ZIP のバージョンであるとは限りません。再現手順、期待される結果、実際の結果を記録します。レンダリング/制限の問題については、ゲームのバージョン、表示の更新、FG/V-Sync/VRR の状態、その他のリミッターまたはオーバーレイを含めます。

[バグフォーム](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml)を使用してください。プライベート開発フォルダー全体、ドライバー アーカイブ、モデル、ゲーム DLL、レジストリ ダンプ、または未レビューのログ コレクションを決して添付しないでください。

| 問題 | 最初のチェック |
| --- | --- |
| アプリケーションのバージョンが間違っています | EXE ID とリリースハッシュを確認します。置き換える前に古いコピーを閉じてください。 |
| 実行時/起動エラー | 必要なフレームワーク 4.8 をインストールするか、付属のポータブル サブフォルダーをすべて保持します。 |
| UAC キャンセルされました | 意図した操作のみを再試行してください。キャンセルするとインストールは成功しません。 |
| ハッシュ/署名の不一致 | その候補の使用を中止し、期待される公式バイトを取得してください。 |
| NVPI カラー/モードが拒否されました | 実際のディスプレイ/ドライバーでサポートされている組み合わせを元に戻して使用します。 |
| NVDF バックアップまたはリカバリの失敗 | 保護されたジョブと RECOVERY.txt を保持します。ジャーナルを消去したり、競合する書き込みを強制したりしないでください。 |
| NVMFG保留中の設定 | ゲームを閉じた状態でリカバリを解決し、他のツールからの変更を保持します。 |
| RP キャップは効果がありません | RTSS を実行し、実際のゲーム EXE を特定し、フックの状態と競合する制限を検査します。 |
| RP キャップは取り外しても残ります | RTSS グローバルを検査します。削除すると、ローカル リミッター オーバーライドのみが変更されます。 |

NVDriverForge は、プレビュー可能なローカル JSON レポートを提供します。 NVMFG は「About」で診断を提供します。これらのフィルタリングされたレポートを完全なログ アーカイブよりも優先し、共有する前に検査してください。 NVMFG 0.1.1 で報告された復元のブロックには、まだ原因が確立されていません。ジャーナルを保存し、入手可能なエラー コードを記録します。 NVRasterPulse 0.2 は、FPS を測定せずに、アクション メニューで構成診断を提供します。

<a id="logs-and-privacy"></a>
## ログとプライバシー

| ツール | ローカルデータはレビューするためのものであり、大量にアップロードするものではありません |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`;保護されたジョブ `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`;バックアップ `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; EXE の横にある `Sessions` |
| RP | `%LOCALAPPDATA%\NVRasterPulse`;その下の`Backups\RTSS` |
| NVPI | 選択したエクスポートと表示されたエラー。ユニバーサルログパスが発明されていない |

共有するテキスト/画像からアカウント名、ホーム ディレクトリ、ゲーム ライブラリのパス、デバイス識別子、トークン、無関係なウィンドウを削除します。復元のためにオリジナルを個人的に保管してください。公開問題は誰でも見ることができます。

脆弱性、危険な特権動作、または意図しない破壊的な操作については、詳細を公開する代わりに [SECURITY.md](../SECURITY.md) に従ってください。

<a id="what-has-been-verified"></a>
## 検証されたこと

ハブの準備として、静的ペイロード/ZIP/ハッシュ/メタデータのスキャンとドキュメントのチェックが実行されました。既存のプライベート アプリケーションのビルド/ユニット/UI テストは、歴史的な古い証拠です。この準備の一環として、ドライバーのインストール、ディスプレイの変更、RTSS のライブ操作、ゲーム ベンチマークは実行されませんでした。

「検出された」、「書き込まれた」、「リロードされた」、「利用可能な機能」、および「ゲーム内で測定された」は異なる結果です。どれを観察したか報告してください。
