<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · **日本語** · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**アプリケーションごとの FPS から RivaTuner Statistics Server までの制限。**

> **最初に RTSS をインストールします。** NVRasterPulse には [RivaTuner Statistics Server (RTSS)、Guru3D からダウンロード](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) が必要です。制限を適用するには、RTSS が実行されている必要があります。 RTSS インストーラー、フック DLL、または SDK はバンドルされていません。

[0.2 とステータスをダウンロード](../docs/downloads.md#nvrasterpulse) · [インストール](#installation) · [制限の仕組み](#usage) · [ライセンス](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## 概要と目的

NVRasterPulse は、実行可能ファイル名によって RTSS フレーム制限を管理するためのコンパクトな Windows インターフェイスです。 RTSS は制限を実行します。 NVRasterPulse は、トレイ アクセスと永続的な選択肢を使用して、対応するプロファイル値、バックアップ、リロード リクエストを管理します。

これは、RTSS プロファイル全体を置き換えたり、そのオーバーレイ設定を妨げたりすることなく、正確なゲームごとの制限を編集しやすくするために存在します。バージョン **0.2** では、構成診断、FPS ヘルパー、一時停止、元に戻す、プロファイル共有が追加されています。

<a id="features"></a>
## 特長

- 実行中のアプリケーションを選択するか、その実行可能ファイルを手動で追加します。
- FPS の制限を 1 ～ 1000 (小数点以下 3 桁まで) で保存します。
- 入力された値の正確な有理エンコーディング: 59.94 は 2997/50 になります。
- アクティブ待機 (`PassiveWait=0`) を備えたフロント エッジ同期構成 (`SyncLimiter=1`)。
- 実行可能プロファイルごとの更新、自動バックアップ、アトミック書き込み。
- 他のプロファイル コンテンツを保持しながら、リミッター オーバーライドを削除します。
- RTSS インストールの検出、手動パス選択、および明示的な起動/リロード。
- 単一インスタンスのトレイ操作、オプションでインストールされたスタートアップ、34 言語、4 つのテーマ。
- 通常の終了アクションと **終了 + RTSS** アクションを分離します。

<a id="compatibility"></a>
## 互換性

| 要件 | 詳細 |
| --- | --- |
| システム | Windows 10/11 x64 |
| ランタイム | [.NET フレームワーク 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)、必要に応じて個別にインストール |
| 必要なソフトウェア | RTSS と `RTSS.exe`、一致する `Profiles` ディレクトリおよび互換性のあるプロファイル/リロードのサポート |
| GPU | RTSS の互換性によってリミッターが決まります。このプロファイル マネージャーは、特定の RTX 世代を必要としません。 |
| 権限 | 現在のアプリケーションは管理者アクセスを要求しています。選択した RTSS プロファイル フォルダーにアクセスできる必要があります |
| ゲーム | RTSS フッキングのサポートと各ゲームの制限によって異なります。アンチチート保証はありません |

このハブ監査では、すべての機能について特定の RTSS 最小バージョンが認定されていません。公式の現在のディストリビューションを使用し、プロファイル キー/リロードが機能しない場合は正確なバージョンを報告してください。インストールされているが停止している RTSS はインストール チェックに合格します。その後、実際に制限を行うために開始する必要があります。

<a id="installation"></a>
## インストール

1. **[Guru3D から RTSS をダウンロードしてインストールします](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. [NVRasterPulse ダウンロード](../docs/downloads.md#nvrasterpulse) を開いて、リリースの可用性を確認します。
3. `NVRasterPulse-0.2-win-x64-Setup.exe` または `NVRasterPulse-0.2-win-x64-portable.zip` と通知/チェックサムをダウンロードします。
4. SHA-256と比較してください。セットアップを実行するか、ポータブル ZIP 全体を書き込み可能なローカル フォルダーに抽出します。
5. `NVRasterPulse.exe` を開きます。 RTSS が見つからない場合は、**RTSS** をダウンロードしてインストールし、**もう一度確認する**を使用するか、`RTSS.exe` を手動で選択します。
6. RTSS を通常のショートカットを使用して起動するか、停止している場合は NVRasterPulse の RTSS ボタンを使用します。

オプションのリマインダーをオフにしても、前提条件のチェックはスキップされません。 Windows トレイのサイレント起動は、メイン ウィンドウが開くまで待機してから、このチェックが表示されます。セットアップでは NVRasterPulse のみがインストールされます。そのEXEは署名されていません。

<a id="usage"></a>
## 使用法

1. 目的の実行アプリケーションを選択するか、そのゲーム EXE を参照します。
2. 1 ～ 1000 FPS の制限を入力します。必要に応じて小数点以下の値も入力します。
3. 報告された結果を保存して確認します。 NVRasterPulse は、その実行可能ファイルの RTSS プロファイルを更新し、リロードを要求します。
4. RTSS が実行されていることを確認し、目的のゲームでの動作を確認します。

プロファイルは、`Game.exe.cfg` など、**実行可能ファイル名** によってキー付けされます。 `Game.exe` を含む 2 つの異なるフォルダーは、同じ RTSS プロファイルを共有します。フルパスを保存しても、この衝突は解消されません。

保存には、Front Edge Sync とアクティブ待機を使用します。アクティブな待機により、CPU の使用が増加する可能性があります。代替の `LimitTime` フィールドは無効化されます。既存のコメント、オーバーレイ設定、`EnableHooking=0` は保持されます。 RTSS グローバル プロファイルは変更されません。

ゴミ箱アクションを使用して、NVRasterPulse のリミッター オーバーライドを削除します。 RTSS プロファイル全体は削除されません。 RTSS Global または別のツールから継承された制限は、その後も適用される可能性があります。

**閉じて終了:** メイン ウィンドウをトレイに隠すことができます。通常の **終了** では、RTSS は実行されたままになり、保存された制限はそのまま残ります。 **Quit + RTSS** は、現在のセッション内の一致する RTSS プロセスの通常の終了を要求し、最大 8 秒間待機し、強制終了しません。どちらの場合も、保存された制限は残ります。

言語とテーマはアプリで選択します。 Windows サインイン時の起動はオプションであり、インストールされたコピーを対象としています。情報ボタンでは一般的なアクションについて説明します。

<a id="diagnostics-and-profile-tools"></a>
## 診断およびプロファイルツール

追加ツールのアクション メニューを開きます。 RTSS グローバル、オーバーレイ設定および除外を保持します。

**診断:** ローカル/有効な制限、停止した RTSS、実行可能ファイルの欠落、ウィンドウの検出なし、無効なフック、継承、一時停止された制限、競合する設定、および重複した実行可能ファイル名を検査します。この読み取り専用チェックは構成について説明します。ゲームが RTSS によってフックされていることを証明したり、FPS を測定したりするものではありません。

**FPS ヘルパー:** ディスプレイを選択し、VRR/G-Sync、V-Sync、Reflex、および Frame Generation を自分で宣言します。丸められたリフレッシュ頻度は Windows から取得されます。 Reflex または Frame Generation がアクティブであるか不明な場合、自動上限は提供されません。 V-Sync がオン、Reflex/FG がオフの VRR の場合、ヒューリスティックは少なくとも 3 FPS、つまりリフレッシュ レートの約 2% を減算します。これは測定された最適値ではありません。提案を適用すると、ドラフトが完成します。 **保存** は別個のアクションのままです。

**一時停止と再開:** 選択したプログラムの上限を一時停止し、以前のリミッター フィールドを復元します。別のツールによる競合する変更により、あいまいな履歴書が作成されるのを防ぎます。エントリを非表示にしても、その上限は一時停止されません。

**元に戻す:** そのプログラムの 6 つの管理対象リミッター フィールドに対する最後の変更を復元します。レベルは 1 つあります。これでは、RTSS のすべてが復元されるわけではありません。矛盾する外部変更は拒否されます。ファイルのバックアップは別個のままになります。

**プロファイルの共有:** 選択したプロファイルを `.nvrp` ファイルにエクスポートします。インポートではプレビューが表示され、デフォルトでは既存のキャップはオフのままになります。ファイルには実行可能ファイルの名前、制限、状態のみが含まれており、絶対パスやスクリプトは含まれません。選択内容を確認して申請してください。 I/O エラーにより、一部のプロファイルがすでに適用されたままになる場合があります。結果によってそれらが識別され、それぞれが元に戻す操作を保持します。同じ実行可能ファイル名でも、同じ RTSS プロファイルをアドレス指定します。

**お気に入りと非表示のエントリ:** 有用なプログラムを最初に固定し、不要なエントリを非表示にして、専用のダイアログで復元します。これらの選択は存続します。閉じたお気に入りは、実行中のアプリケーションとして表示されません。

<a id="screenshots"></a>
## スクリーンショット

![NVRasterPulse メイン ウィンドウのプレビュー](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

既存のフランス語 0.1 UI は、実行可能ファイル名と 176 FPS 値の例を使用してレンダリングされます。 RTSS は停止していると表示されます。これはインターフェイスの図であり、実行中のリミッターや遅延の測定ではありません。 [画像の出所](../assets/README.md)。

<a id="update-and-uninstall"></a>
## アップデートとアンインストール

NVRasterPulse を終了し、新しいバージョンをダウンロードして確認し、セットアップを実行するか、ポータブルを新しいフォルダーに抽出します。設定と RTSS バックアップを保存します。 RTSS アップデートは別のもので、Guru3D から提供されます。

インストールされたコピーを削除するには、Windows **Installed apps** を使用します。ポータブルの場合は、バックアップが安全になったら終了し、抽出されたフォルダーを削除します。保存された RTSS 制限は、NVRasterPulse をアンインストールしても削除されません。最初に目的のリミッター オーバーライドを削除してください。 RTSS には独自のアンインストーラーがあります。

ローカル状態: `%LOCALAPPDATA%\NVRasterPulse`。自動 RTSS バックアップ: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`。古い `%LOCALAPPDATA%\RTSSProfileBridge` の場所が移行のために読み取られる可能性があります。これらのファイルには個人的な実行可能パスが含まれる可能性があるため、公開しないでください。

<a id="known-limitations"></a>
## 既知の制限事項

- RTSS はキャップを実行します。保存された値または成功したリロード要求は、測定されたフレーム時間の結果ではありません。
- 同じ名前の実行可能ファイルはプロファイルを共有します。
- 別のグローバル/ゲームごとのリミッターが結果に影響を与える可能性があります。ローカル オーバーライドを無効にしても、継承された上限は削除されません。
- 意図的に無効化された RTSS フックは無効のままになります。
- アクティブ待機には、CPU と電力のトレードオフがあります。
- ユニバーサル ゲーム、アンチチート、エンドツーエンドの遅延検証はありません。
- 以前の実験的な独立したリミッター エンジンはコンパイルも出荷もされていません。
- 自動バックアップは、ワンクリックの完全バックアップ/復元インターフェイスを意味するものではありません。

<a id="troubleshooting"></a>
## トラブルシューティング

| 症状 | アクション |
| --- | --- |
| RTSS 前提条件は未解決のままです | 実際の `RTSS.exe` と一致する Profiles フォルダーを選択し、再度確認します。 |
| 制限は保存されましたが効果はありません | RTSS を開始します。正しいゲーム EXE/プロファイル、フック権限、その他のリミッターを確認してください。 |
| 保存に失敗する | フォルダーのアクセス許可を確認し、表示されたエラー/バックアップを保存します。 |
| 削除後に残る制限 | RTSS Global およびその他のツールを検査します。ゴミ箱アクションはローカル リミッター オーバーライドのみを削除します。 |
| 2 つのゲームが同じ制限を受ける | 実行可能ファイル名が同一かどうかを確認してください。 |
| 終了 + RTSS は RTSS を開いたままにします | RTSS を通常どおり自分で閉じます。このコマンドは意図的に強制終了を回避します。 |

RTSS バックアップを手動で復元する場合は、まず RTSS を閉じ、現在のプロファイルを保存してから、目的のバックアップに置き換えます。これにより、無関係なプロファイル編集が上書きされる可能性があります。ファイルと日付を調べます。 [共有サポート](../docs/support.md)。

<a id="faq"></a>
## よくある質問

**MSI アフターバーナーも必要ですか?** NVRasterPulse には RTSS が必要です。 Afterburner アプリケーションには依存しません。 RTSS ディストリビュータのインストール オプションに従ってください。

**RTSS を実行していなくてもこれを使用できますか?** インストールが検出されたらプロファイルを管理できますが、制限のために RTSS を実行する必要があります。

**終了またはアンインストールすると上限は削除されますか?** いいえ。NVRasterPulse を削除する前に、必要なリミッター オーバーライドを明示的に削除します。

**これは fork または RTSS ですか?** いいえ。これは独立したプロファイル マネージャーです。 RTSS ソースまたは実行可能ファイルは組み込まれていません。

<a id="upstream-modifications-and-credits"></a>
## アップストリーム、変更、クレジット

開発リポジトリは [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector) から始まります。 MIT パレット/UI リソースがクレジットされています。プロファイル管理サービス、部分エンコーディング、バックアップ、RTSS リロード ブリッジ、トレイ動作、前提条件ガイド、言語、およびアプリケーション固有のアイコンは、禅堂 Zendo (RevoluSound Team) によって開発/適応されました。

RTSS は **Unwinder** によって開発され、Guru3D を通じて個別に配布されます。 NVRasterPulse は、選択したインストール済みフック DLL から `UpdateProfiles` を呼び出します。 RTSS SDK またはフック バイナリは再配布されません。インストーラーは、修正されていない Inno Setup 7.1.0 を、調整されたスクリプト/翻訳およびプロジェクト ブートストラップとともに使用します。

[完全な出所](../docs/provenance.md) · [サードパーティのテーブル](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## ライセンス

このパッケージは、提供された [MITライセンス](../../../../NVRasterPulse/LICENSE) の下で NVRasterPulse を明示的に配布し、著作権 (c) 2016 Orbmu2k を保持します。アプリケーションのソースは非公開で維持されます。 MIT では、変更されたソースの公開は必要ありません。 RTSS および Windows/.NET には、引き続き独自の条件が適用されます。 [完全な通知](LICENSES/README.md)。

NVIDIA Corporation、MSI、RTSS から独立。彼らによって後援または公式に承認されていません。製品名は所有者の商標のままです。
