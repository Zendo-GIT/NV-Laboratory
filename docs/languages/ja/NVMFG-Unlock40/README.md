<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · **日本語** · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**実験的な NVIDIA Multi Frame Generation、GeForce RTX 40 用。中央コントローラーとゲームごとの選択肢が付いています。**

[0.1.1 とステータスをダウンロード](../docs/downloads.md#nvmfg-unlock40) · [インストール](#installation) · [上流](#upstream-and-modifications) · [ライセンス](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## 概要と目的

NVMFG Unlock40 は、禅堂 Zendo (RevoluSound Team) が独自に開発したアプリケーションです。 Windows コントローラー、ネイティブ レイヤー、プロファイル ヘルパー、およびゲーム/Streamline SDK 管理を組み合わせています。すでに NVIDIA DLSS Frame Generation および互換性のある NVIDIA ランタイムを統合しているゲームを対象としています。

作業を比較し、改良するために [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) が参考になりました。現在のネイティブ レイヤーには、共有および適応されたコンポーネントが含まれており、以下に個別にクレジットされています。この参照によって、NVMFG アプリケーション全体がそのプロジェクトの fork になるわけではありません。

これは、実験的な MFG の動作を一元的に調整し、ゲーム固有の選択を記憶し、ランタイムの更新とバックアップを表示し続けるために存在します。すべてのゲームに DLSS Frame Generation を追加したり、任意の FSR 実装を変換したりするわけではありません。

準備された候補は **0.1.1** で、内部的に UI2 として記録される SDK リストの視覚補正が含まれます。パブリック バージョンは 0.1.1 のままです。その正確なハッシュにより、この候補と古いローカル ビルドが区別されます。

<a id="features"></a>
## 特長

- 中央の有効化/無効化制御とオプションの Windows トレイ起動。
- Dynamic MFG、ゲームの設定、サポートされている固定乗数の間でゲームごとに選択します。
- 観察された V-Sync のオン/オフ状態について記憶される選択肢を分けます。
- Dynamic は NVIDIA のモードを使用します。 V-Sync がオフの場合は一時停止され、ゲーム内/固定の別の選択が行われます。
- ゲームメニューのガイダンスと永続的な除外。 DLSS FG のないゲームは引き続き制御されます。
- ゲーム ファイルを削除せずに、ゲームの検出、親フォルダーの選択、検索、グループ化、削除を実行します。
- Streamline SDK ダウンロード/インポート、検証済みローカル キャッシュ、明示的な選択、ゲームごとのバックアップと復元。
- ネイティブプロバイダーの検証、セッションごとの診断、グローバルプロファイルジャーナル、競合を認識したリカバリ。
- 34 のインターフェイス言語と 4 つのテーマ。

ゲーム内で FG をオフにすると、オフのままになります。 2x から 6x までの固定選択肢は、ゲーム/メニュー/ランタイムによって異なります。すべての組み合わせが機能することを保証するものではありません。コントローラーは V-Sync を監視し、ユーザーに対して V-Sync または VRR を設定しません。

<a id="compatibility"></a>
## 互換性

| 要件 | 詳細 |
| --- | --- |
| システム | Windows 10/11 x64 |
| GPU | GeForce RTX 40 ターゲット。 GPU のユニバーサル互換性に関する主張はありません |
| ゲーム | 既存の NVIDIA DLSS Frame Generation 統合とサポートされるランタイム。アンチチート互換性認定なし |
| プロバイダー | 候補者は、[来歴](../docs/provenance.md) に記載されているプロバイダー SHA-256 に固定されます。不明なハッシュは拒否されます |
| ランタイム | アプリ/エージェント用にバンドルされた .NET 8/WPF 8.0.30。プロファイル ヘルパー用の .NET Framework 4.8 |
| 権限 | コントローラー/プロファイル操作のための管理者アクセス |
| ネットワーク | 一部の公式 SDK ダウンロードに必要です。インポートされた互換性のある SDKs はローカルにキャッシュ可能 |
| 外部バイナリ | NVIDIA ドライバー、NGX プロバイダー/モデル、および Streamline ゲーム ランタイムはバンドルされていません |

バージョン ラベルだけでは不十分です。ドライバー、プロバイダー ハッシュ、ゲームの統合、実際にロードされたモジュールが重要です。保護されたプロセスまたは互換性のないプロセスは、接続を拒否する可能性があります。このアプリケーションは、不正行為防止保護を回避するように設計されていません。

<a id="installation"></a>
## インストール

1. [候補者のステータスとライセンスノート](../docs/downloads.md#nvmfg-unlock40) を読み取ります。
2. `NVMFGUnlock40-0.1.1-Setup-x64.exe` または `NVMFGUnlock40-0.1.1-Portable-x64.zip` のリリースが利用可能になったら、ダウンロードします。
3. SHA-256 を確認し、付随する通知を保管してください。 Windows がまだ提供していない場合は、.NET Framework 4.8 をインストールします。
4. セットアップを実行するか、**全体**のポータブル ZIP を書き込み可能なローカル フォルダーに抽出します。
5. `NVMFGUnlock40.exe` を起動します。 `agent`、`driver`、`engine`、`Licenses` は提供されたレイアウトのままにしてください。

`driver` という名前のフォルダーには、カーネル ドライバーではなくユーザー空間ヘルパーが含まれています。メイン EXE のみをコピーしたり、互換性を強制するためにプロバイダー ハッシュを置き換えたりしないでください。現在の EXE は署名されていません。

<a id="usage"></a>
## 使用法

1. コントローラーを無効にした状態で開始します。ゲームまたは親フォルダーを追加し、実際のインストールを選択します。
2. 各ゲームの MFG 設定を確認します。そのメニューが何であるかを答えてください。答えはゲームごとに保存されます。
3. Dynamic またはゲーム内設定をグローバルに選択し、必要に応じて対象となるゲームごとの選択肢を調整します。
4. コントローラーを使用する場合にのみ、コントローラーを有効にしてください。リカバリジャーナルを使用して、6 つのグローバル NVIDIA プロファイル設定を一時的に変更できます。
5. 対象となるゲームを起動し、独自の DLSS Frame Generation を有効にします。 V-Sync-off を選択するための要求に従います。
6. 管理したくないゲームには除外を使用します。ゲームを削除すると除外が記録され、そのファイル/バックアップが保存されます。
7. 終了したら、アプリケーションの完全な終了/無効化および回復フローを使用します。

メイン ウィンドウを閉じると、コントローラがトレイに残ったままになる場合があります。すでにゲームにロードされている DLL は、ゲームが終了するまでそこに残ります。コントローラーを無効にしても、アンロードは保証されません。メンテナンスやアップデートの前に、影響を受けるゲームを閉じてください。

**Streamline SDKs:** NVIDIA SDK ページで、正式バージョンをダウンロードするか、互換性のあるローカル SDK をインポートします。インポートでは検証済みのコピーが保存されます。 **Use this version** はそれを選択し、**Uninstall** はそのキャッシュされたコピーを削除します。欠落している Streamline DLL は、ソースが示されている公式の NVIDIA SDK から補充できます。これは、NGX モデルをダウンロード/置換しません。ゲームを閉じ、目的のゲームのアップデートを選択し、元のバックアップを保持します。ゲームファイルを元に戻すには、キャッシュの Uninstall ボタンではなく、バックアップ復元を使用します。

<a id="screenshots"></a>
## スクリーンショット

![NVMFG SDK リストのプレビュー](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

既存の英語版 0.1.1 インターフェイスは、SDK インベントリの例でレンダリングされます。これは、現在のバージョンのリストやゲームが実行されている証拠ではありません。 [画像の出所](../assets/README.md)。

<a id="update-and-uninstall"></a>
## アップデートとアンインストール

影響を受けるゲームを終了します。更新する前に、NVMFG を無効化/終了し、保留中の NVIDIA 設定の回復を解決してください。既存の ID を使用して次のセットアップをインストールするか、新しいポータブルを新しいフォルダーに抽出します。状態/バックアップを保持します。

アンインストールする前に、アプリケーションを通じて目的のゲームの SDK バックアップと NVIDIA 設定を復元し、ゲームを閉じてコントローラーを終了します。セットアップに Windows **Installed apps** を使用するか、必要なファイルを保存した後、閉じたポータブル フォルダーを削除します。セットアップのブロックを解除するために、アクティブなリカバリ ジャーナルを手動で削除しないでください。

ローカル ゲーム ランタイム バックアップは `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups` を使用します。 MFG 設定/SDK データは `%LOCALAPPDATA%\RtxMfg` を使用します。セッション出力は、アプリケーションの横の `Sessions` の下にあります。これらのファイルにはゲームのパスを含めることができます。編集せずに投稿しないでください。

<a id="known-limitations"></a>
## 既知の制限事項

- 実験的なネイティブ パッチはクラッシュや視覚的なアーティファクトを引き起こす可能性があります。未解決の Bodycam クラッシュが開発履歴に記録されます。
- コントロールド レンダラー テストは、すべてのゲーム、ドライバー、またはアンチチートの認定ではありません。
- 生成されたフレームは新しい入力サンプルを作成しません。このハブでは、測定された遅延やパフォーマンスの向上は保証されません。
- 複数のフレーム生成ツール/オーバーレイが競合する可能性があります。アプリケーションは、すべての共存シナリオを証明することなく、観察されたモジュールを報告します。
- 互換性マニフェストは検出を補助するものであり、完全にテストされたゲームのリストではありません。
- NVIDIA SDK の完全な条項と未解決の技術的制限は、[来歴](../docs/provenance.md) に文書化されたままです。

<a id="troubleshooting"></a>
## トラブルシューティング

| 症状 | アクション |
| --- | --- |
| プロバイダーがサポートされていません | 検証済みの元のファイルは保管しておいてください。ドライバー/プロバイダーのバージョンとエラーを報告します。ハッシュチェックをバイパスしないでください。 |
| ゲームにDLSS FGはありません | その答えを選択して、ゲームをコントロールしたままにしてください。このツールではその統合を行うことはできません。 |
| ゲームのクラッシュ/アーティファクト | ゲームを終了し、NVMFG を無効にし、変更されている場合はゲームの元のランタイム バックアップを使用し、再現可能な詳細を報告します。 |
| SDK リストまたはダウンロードは利用できません | 公式ソースを更新して確認してください。キャッシュ/インポートされたバージョンは検証に合格する必要があります。 |
| 保留中の NVIDIA リカバリにより終了/更新がブロックされる | リカバリを使用してジャーナルを保存します。競合をむやみに上書きしないでください。 |
| 削除されたゲームは再検出されません | その除外は永続的です。再度管理する場合は、明示的に追加します。 |

[共有サポート ガイダンス](../docs/support.md) は、レポートに何を含めるべきかを説明します。

<a id="faq"></a>
## よくある質問

**NVIDIA DLL またはモデルは含まれていますか?** ドライバー、NGX プロバイダー/モデル、または Streamline ランタイムは含まれません。明示的な SDK ダウンロードは NVIDIA から行われます。

**Dynamic は V-Sync がオフのときに動作しますか?** その状態ではサスペンドされます。ゲーム内設定またはそのゲームの個別の状態に適した固定乗数を選択します。

**これは ReShade/OptiScaler/FSR パッケージですか?** いいえ。これらは、この製品パッケージの一部としてコンパイルまたは出荷されません。

**変更されたソースは公開されていますか?** いいえ。コンパイルされたパッケージと必要なクレジット/ライセンスが提供されます。これは第三者の権利や制限を除去するものではありません。

<a id="upstream-and-modifications"></a>
## 上流と変更

比較リファレンスおよび共有ネイティブ コンポーネント: **RTX40MFG-Unlock by Michael Robles / dashdogy**、リファレンス コミット `4e776d068f91b4a665425542bb005dd57cc3d891`、MIT。 [リポジトリ](https://github.com/dashdogy/RTX40MFG-Unlock)・[オリジナルのダウンロード](https://github.com/dashdogy/RTX40MFG-Unlock/releases)。

ソース比較により、共有パッチ適用、プロバイダー/ポリシー処理、一時的な修正、MinHook ベースの迂回コンポーネントが特定されます。 MIT および BSD 通知は保持されます。完全な比較には、運用ターゲット外のファイルも含まれます。

デスクトップ アプリケーション、コントローラー、および SDK 管理ワークフローは、禅堂 Zendo (RevoluSound Team) によって開発されています。プロジェクトの作業には、集中読み込み、NGX ブートストラップの統合、検証されたプロバイダーの選択、ゲーム/V-Sync の調整、およびセッション診断が含まれます。来歴ガイドは、その作業を共有コンポーネントから分離します。ファイルの比較だけでは、どちらの作成者がいつアイデアを思いついたのかを証明することはできません。

プロファイル ヘルパーは、Orbmu2k の Profile Inspector から MIT NVAPI ラッパーを適応させます。 [詳細な来歴とコンポーネントの範囲](../docs/provenance.md)。

<a id="credits-and-license"></a>
## クレジットとライセンス

Michael Robles; Orbmu2k; Tsuda Kageyu および HDE の貢献者。 NVIDIA Corporation; Microsoft と寄稿者。 Inno Setup の著者および翻訳者。アプリケーションの開発、統合、およびパッケージ化: 禅堂 Zendo (RevoluSound Team)。

[既存のコンパイル済みパッケージの共有権限](../../../../NVMFG-Unlock40/LICENSE) とすべての [コンポーネントライセンス](LICENSES/README.md) は保持されます。アップストリーム コードの MIT 権限は、NVIDIA SDK の条件とは異なります。これらに代わる包括的ライセンスはありません。

NVIDIA Corporation から独立しており、NVIDIA Corporation のスポンサーではなく、正式に承認されていません。参照されているすべての商標は、その所有者の財産のままです。
