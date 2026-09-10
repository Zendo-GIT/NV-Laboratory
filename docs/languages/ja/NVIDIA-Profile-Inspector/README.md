<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · **日本語** · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**表示コントロールが追加された、[NVIDIA Profile Inspector by Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector) から独立した fork。** 以前のプロジェクト名: **NVPI Custom**。

[ダウンロード＆リリース状況](../docs/downloads.md#nvidia-profile-inspector) · [インストール](#installation) · [上流と変更](#upstream-and-changes) · [ライセンス](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## 概要

アプリケーションは、アプリケーションごとの設定を含む NVIDIA ドライバー プロファイルを編集します。この fork は、アクティブな Windows ディスプレイ用の **画面** エディター (解像度、リフレッシュ レート、出力カラー設定、HDR、およびインストールされている ICC/WCS プロファイルの関連付け) も追加します。

これは、関連する表示コントロールをプロファイル エディターに組み込み、プレビュー、確認、復元の結果をより明確にするために存在します。新しいハードウェア機能を確立するものではありません。

最初の候補は **3.0.2.3** で、2026 年 9 月 9 日のクリーンアップされたスタンドアロン コンパニオン ビルドを使用します。その既存の実行可能ファイルは `nvidiaProfileInspector.exe` のままです。インストーラーと一部の内部ラベルには依然として `NVPI Custom NV` と表示されます。上記の公開タイトルは、インストール ID を変更したり、Orbmu2k の公式リリースであるかのように装ったりすることなく、fork を識別します。

<a id="features"></a>
## 特長

- 既存のアップストリーム プロファイルの参照、アプリケーションの関連付け、設定の編集、プロファイルのインポート/エクスポート。
- **画面** ディスプレイ、モード、Hz、RGB/YCbCr、色深度、範囲、測色用ダイアログ。
- Windows HDR コントロールとインストールされた ICC/WCS の関連付けの選択。
- **Keep** / **Revert** およびタイムアウト時の復元を備えた 15 秒間の表示プレビュー。
- モード/HDR の変更をリードバックし、復元の失敗が報告されました。
- HDR、ACM/WCG を使用した SDR、および信号の色深度を個別にレポートします。
- 個別にインストールされた適格なコピー用の NVRasterPulse ランチャー。

<a id="compatibility"></a>
## 互換性

| 要件 | 詳細 |
| --- | --- |
| システム | 互換性のある NVIDIA ドライバーを備えた Windows 10/11 x64 |
| ランタイム | [.NET フレームワーク 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)、Windows によって提供されるか、個別にインストールされます |
| 権限 | エディターを開くと管理者アクセスが要求される |
| ディスプレイ | 実際のモードと色の組み合わせは、GPU、ドライバー、ディスプレイ、ケーブル、および Windows API によって異なります。 |
| オプションのツール | RTSS 制限管理の場合は NVRasterPulse。スクリーンエディタにはそれも RTSS も必要ありません |
| 言語 | セットアップ: 34 言語セレクター。エディターは既存の言語サポートを維持します。 |

すべての GPU について検証されたユニバーサル ドライバーの最小値やサポート マトリックスはありません。ダイアログで使用できる bpc の選択肢はリクエストであり、認定された組み合わせではありません。最新の HDR コントロールと古い Windows フォールバックには、異なる機能があります。

<a id="installation"></a>
## インストール

1. [ダウンロードページ](../docs/downloads.md#nvidia-profile-inspector) を開いて公開ステータスを確認します。
2. セットアップまたはポータブル アセットをダウンロードし、その SHA-256 をリリース マニフェストと比較します。
3. セットアップでは、`NVPI-CustomNV-3.0.2.3-Setup-r2.exe` を実行し、言語を選択し、インストーラーの指示に従います。独自のショートカットとアンインストーラーを作成します。
4. ポータブルの場合は、完全な ZIP を新しい書き込み可能なフォルダーに抽出します。 `Reference.xml`、EXE 構成、およびすべての通知を実行可能ファイルの横に保管してください。
5. `nvidiaProfileInspector.exe`を起動します。

エディターを単独でインストールしても、プロファイルの適用や GPU ドライバーのインストールは行われません。コンパニオンは個別にインストールされ、`.nip` の関連付けは引き継がれず、サインイン時の起動も有効になりません。既存のバイナリは署名されていません。

<a id="usage"></a>
## 使用法

**インストーラー リビジョン 2** では、他のツールと同じネイティブ 34 言語セレクターが追加され、マウス/キーボード ナビゲーション、明/暗の外観、およびキャンセルが追加されます。選択はセットアップに適用されます。 NVPI エディタは変換されません。明示的な `/LANG=fr` 引数またはサイレント モードは、すでに言語を提供している呼び出し元の選択をバイパスします。

**ドライバー プロファイル:** プロファイルを選択し、バックアップをエクスポートし、目的の設定のみを編集して適用します。アプリケーションの関連付けによって、どのゲームがプロファイルを受け取るかが決まります。保存された値は、すべてのドライバーまたはゲームがその値を使用していることを証明するものではありません。

**表示コントロール:** **画面**を開き、表示と要求された値を選択して、プレビューを開始します。 15 秒以内に画像を確認してから、**Keep** を選択してください。 **元に戻す**を使用し、確認を閉じるか、期限切れにして復元をリクエストしてください。失敗メッセージを読みます。API 呼び出しが成功しただけでは、復元の証拠にはなりません。

ICC を選択すると、インストールされているプロファイルの関連付けが変更されます。 ICC ファイルの生成、調整、再配布は行いません。 HDR、ACM/WCG、RGB/YCbCr、および bpc は、パイプラインのさまざまな側面を説明します。新しい独立した ACM スイッチは提供されません。

**NVRasterPulse:** ツールバー ボタンは、保護された所有権と権限を持つ Program Files の下に個別に登録されたシステム全体のインストールを受け入れます。ポータブル コピーまたはユーザーが書き込み可能な/リンクされたパスは、この昇格されたランチャーによって拒否される場合があります。その場合は、独自のショートカットを使用して NVRasterPulse を開きます。 [RTSSを別途インストールする](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) は NVRasterPulse を使用します。

<a id="screenshots"></a>
## スクリーンショット

![NVPI セットアップ リビジョン 2 言語セレクター](../../../../assets/screenshots/nvpi-setup-r2-language.png)

フランス語の実際のセットアップ セレクター。単独のテスト中にキャプチャされ、その後キャンセルされました。これはインストーラーを示しています。エディターはそのインターフェースと画面ダイアログを保持します。

<a id="update-and-uninstall"></a>
## アップデートとアンインストール

更新する前にエディタを閉じてください。エクスポートしたプロファイルを保持し、新しい fork リリースをダウンロードします。同じコンパニオン ID 上にインストールするか、ポータブル ファイルを新しいフォルダーに抽出します。古い `Reference.xml` と新しい実行可能ファイルを混合しないでください。バンドルされたアップストリーム更新チェック抑制は、この fork に属します。

インストールされたコピーの場合は、Windows Installed apps とそのアンインストーラーを使用します。ポータブルの場合は、エクスポートが安全になったら、それを閉じて、抽出されたフォルダーを削除します。エディターを削除しても、ドライバー プロファイルの編集、表示設定、NVRasterPulse または RTSS は元に戻されません。削除する前に必要な設定を復元します。

<a id="known-limitations"></a>
## 既知の制限事項

- 15 秒間の確認は、すべてのドライバーの衝突、電源喪失、または強制シャットダウンを監視するものではありません。
- 一部の色/深度/リフレッシュの組み合わせでは、`NVAPI_NOT_SUPPORTED` が返されます。
- ソフトウェアのリードバックでは、パネルのビット深度、色の精度、遅延は測定されません。
- 画面設定は現在の Windows ディスプレイに影響します。このダイアログでは、ゲームごとの表示プリセットは作成されません。
- パフォーマンス、アンチチート、またはユニバーサル HDR 互換性の保証はありません。

<a id="troubleshooting"></a>
## トラブルシューティング

| 症状 | アクション |
| --- | --- |
| 起動時のランタイムエラー | Windows 更新プログラムと .NET Framework 4.8 を確認します。完全なパッケージを使用してください。 |
| 要求された表示モードが拒否されました | そのディスプレイに対して Windows/NVIDIA によって提供されるモードを元に戻してテストします。正確なエラーを読み取り、盲目的な変更を繰り返すことを避けてください。 |
| HDR または色が古い状態に戻る | 別の操作が失敗して復元がトリガーされたかどうかを確認します。 HDR と ACM を区別します。 |
| NVRasterPulse ボタンがパスを拒否します | 独自のショートカットを起動します。このボタンには、システム全体で保護されたインストールが必要です。 |
| アンインストール後も変更が残る | エクスポートされた NVIDIA プロファイルまたは目的の Windows ディスプレイ設定を復元します。アンインストールは設定のロールバックではありません。 |

ログを送信する前に、[共有サポート ガイダンス](../docs/support.md) を参照してください。

<a id="faq"></a>
## よくある質問

**これは公式の NVIDIA ソフトウェアですか、それとも Orbmu2k の公式ビルドですか?** いいえ、独立した fork です。上流の作成者と MIT ライセンスはクレジットされたままになります。

**NVDriverForge にはこのエディタが必要ですか?** いいえ、NVDriverForge のオプションの Custom NV プリセットは独自の統合を使用します。エディターのインストールは別の選択です。

**この fork には RTSS は必須ですか?** いいえ、RTSS は、プロファイルや画面編集ではなく、NVRasterPulse の FPS リミッターに必須です。

**ソースはどこですか?** 変更されたアプリケーションのソースは非公開で管理されています。 MIT 通知とアップストリーム リポジトリが提供されます。 MIT では、変更されたソースを公開する必要はありません。

<a id="upstream-and-changes"></a>
## 上流と変更

アップストリーム: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector)、参照コミット `592d962cca8827efe8859461a84267755595064a`。 [オリジナルのダウンロード](https://github.com/Orbmu2k/nvidiaProfileInspector/releases)。

継承: プロファイル エディター、NVAPI 相互運用性、参照データ、UI リソースおよびテーマ。 禅堂 Zendo (RevoluSound Team) は、表示サービス、HDR/ICC トランザクション、15 秒の確認/リードバック、ツールバー レイアウト、および RasterPulse 起動動作を追加または調整しました。クリーンアップされたコンパニオンは、開発モック/テスト エントリ ポイントを除外し、保護された外部ランチャーを使用し、別個のインストーラーを提供します。 NVPI/RasterPulse を組み合わせた古い開発パッケージは、このハブの候補ではありません。

[詳細なファイルの出所](../docs/provenance.md) · [オリジナルの fork 通知](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## クレジットとライセンス

著作権 (c) 2016 Orbmu2k。提供された [MITライセンス](../../../../NVIDIA-Profile-Inspector/LICENSE) は保持されます。適応・梱包：禅堂 Zendo (RevoluSound Team)。インストーラは Inno Setup を使用します。 Windows と .NET Framework は外部のままです。 [該当する完全な通知](LICENSES/README.md)。

NVIDIA Corporation から独立しており、NVIDIA Corporation のスポンサーではなく、正式に承認されていません。商標はそれぞれの所有者に帰属します。
