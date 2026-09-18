<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · **日本語** · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# 来歴、変更、ライセンス

この監査では、**2026-09-18** に準備された候補者について説明します。アプリケーションのソースは非公開のままです。パブリック インベントリには、ソース コードではなく、ファイル名とハッシュが含まれます。 [フルコンポーネントの通知](../THIRD_PARTY_NOTICES.md)を参照してください。

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

参照: Orbmu2k/nvidiaProfileInspector コミット `592d962cca8827efe8859461a84267755595064a`;候補実行可能バージョン 3.0.2.3。参照コミットと fork のアセンブリ バージョンは異なる識別子です。 fork バージョンからは、アップストリーム リリース バージョンは推測されません。

クリーン コンパニオンの 157 個のソース/リソース ファイルがそのコミットと比較されました。2 バイトが同一、134 個は行末または UTF-8 BOM のみが異なり、11 個は変更され、10 個は比較されたアップストリーム パスに存在しません。 「追加」はそのパスに関連するものであり、それ自体がオリジナルの作者であることを証明するものではありません。

[完全なファイル/ハッシュ比較](../../../provenance/nvpi-source-provenance.json).

| エリア | 受け継がれた仕事 | Fork の貢献 |
| --- | --- | --- |
| プロフィールエディタ | プロファイル モデル、インポート/エクスポート、アプリケーションの関連付け、および参照データ | Screen および外部ツール ランチャーとの統合 |
| NVAPI | Orbmu2k の DRS 相互運用性 | 色/ディスプレイ関連の相互運用性、実稼働環境のネイティブ読み込み制限、およびモックの削除 |
| ディスプレイサービス | 外部インターフェイスとしての Windows/NVIDIA API | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | アップストリーム WPF リソース、パレット、アイコン | 画面ダイアログ、15 秒間の確認、ステータス/リードバック、およびツールバーのレイアウト |
| ランチャー | 既存のアプリシェル | 個別にインストールされた保護された RasterPulse ルックアップと起動 |
| 包装 | MIT アップストリーム | クリーンなスタンドアロン コンパニオン、個別のインストーラー/アンインストーラー、保持される通知 |

公開ソース マップには、トレーサビリティのためのソリューション/リソース パスが含まれています。これらのファイルはソースとして配布されません。開発テスト、モック インターフェイス、および古い組み合わせの NVPI/RasterPulse バイナリは除外されます。

<a id="nvdriverforge"></a>
## NVDriverForge

独立した C#/.NET 8/WPF アプリケーション。ユーザー向けのワークフローは、部分的に NVCleanstall からインスピレーションを受けています。実稼働ペイロードでは NVCleanstall ソース/バイナリが識別されませんでした。これは、その独自アプリケーションの fork としては表されません。

元のプロジェクトの作業には、コンポーネントの分析/選択、保護されたインストール ジョブ、バックアップとトランザクションの回復、NVIDIA カタログのダウンロード、更新チェック、ローカライズされた説明、オプションの高度な/NVENC ワークフロー、およびインストーラー ブートストラップが含まれます。

継承/適応されたコンポーネント: 4 つの NVPI テーマ パレット、拡張 NVAPI DRS インターフェイス リファレンス、および個別にオプションの MIT NVPI コンパニオン。 Custom NV プリセットの選択 UI と許可リストに登録されたトランザクション統合は NVDriverForge に属します。このプリセットは NVIDIA の公式推奨ではありません。

7-Zip 26.03、.NET/WPF 8.0.31 および Inno Setup は、独自の条件で使用される未変更の外部コンポーネントのままです。 keylase NVENC データは埋め込まれていません。ユーザーが互換性のあるダウンロードを要求すると、1 つの正確なコミットが選択され、チェックされます。そのアップストリーム データに対して再配布ライセンスは確立されていませんでした。

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 は、禅堂 Zendo (RevoluSound Team) によって独自に開発されました。メンテナは比較と改良のために RTX40MFG-Unlock を使用しました。アプリケーション全体が fork として表示されるわけではありません。この区別によって、現在のネイティブ層の共有/適応コンポーネントのクレジットが削除されるわけではありません。

比較参照: dashdogy/RTX40MFG-Unlock、Michael Robles、MIT、コミット `4e776d068f91b4a665425542bb005dd57cc3d891`。プライベート ネイティブ エンジン ツリーには 48 個の比較ファイルが含まれています。そのうち 35 個はフォーマットのみの相違点、4 個は変更されたファイル、9 個は参照パスに存在しません。 [完全な比較](../../../provenance/nvmfg-source-provenance.json)。

変更された継承ファイル: `entry_detour.h`、`patcher.cpp`、`temporal_interval_trace.cpp`、`temporal_interval_trace.h`。追加のパスには、`game_selection.*`、`ngx_bootstrap.*`、`ngx_capability.h`、`presentation_tracker.h`、`vsync_observer.*`、および保持されたアップストリーム ライセンスが含まれます。

プロダクション C++ ユニット: パッチャー、midpoint_fix、dlssg_provider_policy、entry_detour、nvidia_mfg_policy、temporal_interval_trace、ngx_bootstrap、game_selection、および vsync_observer。さらに、entry_detour アセンブリと MinHook バッファ/フック/トランポリン/HDE64。継承された ReShade フロントエンド、レガシー shim リソース、および未使用の CMake ターゲットは、この運用コンパイルの一部ではありません。

一致するコンポーネントは、パッチ適用/プロバイダー ポリシーと一時的な作業をカバーします。著作権と許可通知はそのまま残ります。中央の NGX/ブートストラップ/コントローラー調整、ゲームごとの V-Sync 処理、セッション診断および Windows アプリケーション/SDK/バックアップ ワークフローは、禅堂 Zendo (RevoluSound Team) によるプロジェクト作業です。上記の数は、サードパーティのファイルや未使用のファイルを含むファイルを表しており、いずれかのプロジェクトのアイデアの著者の割合や年表ではありません。

ヘルパーは、プロジェクトが作成したプロファイル ロジックを使用して、NVPI の NvapiDrsWrapper および NativeArrayHelper を別のアセンブリに適合させます。古い開発モック パスは除外されます。共有ファミリ パレットは NVPI から始まります。

MinHook 参照: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`;継承されたコンパイル済みサブセットには、比較において機能的なローカルな変更はありません。 Streamline 統合ヘッダー: 2.12;オープン ヘッダー ライセンスは v2.12.0 で検証されました。 NGX ヘッダー ソース: NVIDIA/DLSS コミット `a291cc7d2cc642a51566f3dfd5376f635cd1b284`。

候補エンジン SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`。

engine.json の必須プロバイダー SHA-256: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`。報告された 310.9 プロバイダー ファミリは、この正確なハッシュと互換性がありません。プロバイダー DLL やモデルは含まれません。

**優れたライセンス ポイント:** 完全な NVIDIA RTX SDK ライセンス (バージョン 2024 年 3 月 14 日) には、技術的制限の回避に関連するセクション 4(d) の制限が含まれています。監査では、この使用に対する許可は確立されません。 MIT エンジン ライセンスを保持したり、無料で使用したり、他の MOD を観察したりしても、その個別の条件は解決されません。候補者の準備は法的な許可ではありません。オリジナルの短いヘッダー通知には完全なライセンスが補足されています。 Windows-1252 テキストも、元のバイトが保持された、読み取り可能な UTF-8 として提供されます。

ネイティブ比較は、同じ 48 個のファイルと分類の 0.2.3 に対して再計算されました。前回の監査以降、アクティビティ/機能の観察のために `game_selection.cpp`、`game_selection.h`、および `patcher.cpp` が変更されました。新しいライブラリ、診断、設定、更新、および選択のワークフローは、メンテナ アプリケーションに属します。コンポーネント ライセンスと必要なプロバイダー ハッシュは変更されません。

<a id="nvrasterpulse"></a>
## NVRasterPulse

NVPI 派生リポジトリで開発された独立した RTSS プロファイル マネージャー。継承された MIT UI リソース/パレットおよびプロジェクトの原点はクレジットされたままになります。実稼働アプリは、提供された MIT ライセンスを明示的に使用します。

プロジェクトの作業: RTSS プロファイルの正確な解析/書き込みと部分エンコーディング、バックアップ、オーバーライドの削除、ブリッジのリロード、前提条件の検出、コンパクトな UI、トレイのライフサイクル、起動制御とローカリゼーション。 RTSS は実際の制限を実行します。

RTSS ソース、フック DLL、SDK、インストーラーはバンドルされていません。ブリッジは、ユーザーが選択した既存の RTSS インストールでエクスポートを呼び出します。このパッケージには、NVIDIA ドライバー パッケージ、ネイティブの実験的リミッター、Framepacer、MinHook、ReShade、または DLSS ランタイムは含まれていません。

<a id="assets-generated-data-and-tools"></a>
## アセット、生成されたデータ、ツール

[アセットクレジット](../assets/README.md) は、既存のインターフェイス プレビューと NVPI セットアップ セレクターを識別します。それらの架空の値にはラベルが付けられています。ゲーム/Nexus アセット、個人プロファイル、プライベート ICC、企業 NVIDIA ロゴ、またはフォント ファイルはコピーされません。

NVMFG に継承され、生成されたゲーム互換性名は検出補助であり、テストの証拠ではありません。生成されたインストーラー カタログは、[翻訳者の通知](../../../../licenses/INSTALLER-TRANSLATORS.md) にクレジットされます。絶対パスを含む生成されたビルド レコードは非公開のままです。

プライベート ビルド ツールには、.NET SDK/MSBuild、Visual Studio C++/MASM、Windows SDK、PowerShell、Inno Setup、および Python 監査スクリプトが含まれます。コンパイラ、ヘッダー、テスト ランナー、およびデバッグ アセットは配布されていません。静的リリース CRT は、引き続き Microsoft の該当するツールチェーン条件に基づいて適用されます。

<a id="scope-of-verification"></a>
## 検証範囲

ローカル監査では、Git オブジェクト データベースとリンクされたディレクトリ ターゲットを除き、3 つの開発ルートにあるすべてのファイルのインベントリを作成しました。アクティブなソース/ドキュメントがスキャンされました。歴史的なビルドはインベントリに登録され、除外されました。選択した ZIP と現在のペイロードがスキャンされ、ハッシュ化されました。 .NET バンドルは追加の検査のために解凍されました。その初期監査では、製品、インストーラー、ゲーム、RTSS プロセス、ドライバーは実行されませんでした。

新しい NVPI セットアップ リビジョン 2 では、共有 Inno コントロールとブートストラップを使用したスタンドアロン言語選択が修正されています。明暗の専用器具により、マウスとキーボードのナビゲーションと 34 の明示的な言語コードすべてが検証されました。実際のセットアップ セレクターは、決して表示されないプライベート デスクトップで開かれ、インストール前にキャンセルされました。 7 つのアプリケーション ファイルとポータブル ZIP は変更されていません。 NVDriverForge 0.1.3 には修正されたコンパニオンが含まれており、依然として `/LANG` を転送します。

NVDriverForge 0.1.3 は 2026 年 9 月 10 日に完了しました。その非公開検証レポートには、366 件のアプリケーション テスト、118 件のコンパニオン チェック、32 件のセットアップ チェック、156 件のネイティブ比較、および 34 件の言語転送ケースが記録されています。保護されたコンポーネント選択の修正は、ペイロードの変更やドライバーのインストールを行わずに、元のドライバー パッケージに対して再実行されました。これらは古い製品チームの結果であり、このドキュメントの更新によって再実行されたテストや、実際のドライバーのインストールが成功したことを証明するものではありません。

このハブの更新では、機能するアプリケーション コードは変更されません。以前のアプリケーションのビルド/ユニット/UI テストは古い歴史的証拠として残っています。これは、すべてのサードパーティ バイナリの完全なリバース エンジニアリングではなく、すべての考えられる秘密のパターンに対する保証でもありません。

2026 年 9 月 18 日更新: NVDriverForge 0.1.4 は、準備状況チェック、ネイティブ プロファイルのバックアップ、コンポーネント ガイダンス、基本設定とキット、詳細な結果、ローカル レポート、およびアプリケーションの更新を追加します。 NVRasterPulse 0.2 は、新しいリミッター エンジンを使用せずに、構成診断、FPS ガイダンス、一時停止/再開、元に戻す、`.nvrp` プロファイル、お気に入り/非表示を追加します。個別のガイドでは、使用方法と制限について説明します。静的ハブのチェックは、9 月 18 日の非公開レポートに記録されたアプリケーション テストとは別のものです。このハブに対してドライバーのインストール、実際のプロファイルのインポート、遅延測定は実行されませんでした。
