<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · **日本語** · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# インストールガイド

[ダウンロード](downloads.md) から始めます。これは、公開ステータスと正確なアセット名を記録します。これらは別個のツールです。必要なものだけをインストールしてください。

> **NVRasterPulse の場合は、プロファイル マネージャーを開く前に [Guru3D の RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) をインストールしてください。**
> 制限を適用するには、RTSS を実行する必要があります。 NV Tools には含まれていません。

| ツール | インストールされているエディション | ポータブル版 | 主な前提条件 |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | 完全な NVPI ZIP を抽出します | NVIDIA ドライバーと .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe、ランタイム付属 | インストール操作用の互換性のあるオリジナルの NVIDIA ドライバー パッケージ |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | 完全な NVMFG ZIP を抽出し、サブフォルダーを保持します | RTX 40、既存の DLSS FG、正確なプロバイダーおよび .NET Framework 4.8 ヘルパー |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | 完全な RP ZIP を抽出します | RTSS および .NET Framework 4.8 |

<a id="download-verify-install"></a>
## ダウンロード、確認、インストール

1. 選択した公開リリースで、その名前付きアプリケーション アセットをダウンロードすると、ZIP と SHA256SUMS.txt が表示されます。
2. 実際にダウンロードしたファイル名を指定して [SHA-256 の例](downloads.md#sha-256) を使用します。
3. セットアップについては、通常のインストーラーに従ってください。ポータブル ZIP の場合は、すべてを新しいローカルの書き込み可能なフォルダーに抽出します。 ZIP 内からは実行しないでください。
4. アプリケーション自体の EXE を開きます。付属のライセンス/構成/データ ファイルは保管しておいてください。
5. 設定やシステム操作を有効にする前に、そのツールの使用説明をお読みください。

現在のバイナリは署名されていません。一致するハッシュにより、予期されるバイトが確認されます。これはセキュリティまたは互換性の証明書ではありません。警告を抑制するためだけに Windows セキュリティ保護を無効にしないでください。

NVDF またはそのオプションの NVPI コンパニオンのインストールは、GPU ドライバーのインストールとは別です。 NVPI コンパニオンは、既存の内部インストール名を保持します。その昇格された RasterPulse ボタンには、システム全体で保護されたインストールが必要です。他の RP コピーは、独自のショートカットを使用して開くことができます。

NVMFG は実験的であり、[文書化された NVIDIA SDK ライセンス予約](provenance.md) を備えています。 NVIDIA ドライバー、NGX プロバイダー/モデル、またはゲームの Streamline ランタイムは含まれません。選択した SDK のダウンロードとゲームのアップデートは、明示的に別個の操作です。

<a id="language-and-updates"></a>
## 言語と最新情報

ドキュメントには README の 34 言語セレクターを使用してください。 NVDF、NVMFG、および RP には、独自の 34 言語の UI 設定があります。 NVPI は、既存の言語サポートを維持します。一部のインストーラの技術文字列は英語に戻ります。

更新時にツールのインストール ID を維持します。まず閉じて、バックアップを保存してください。 NVMFG の場合は、影響を受けるゲームを終了し、保留中のプロファイルの回復を解決します。ポータブル アップデートの場合は、リリースを結合するのではなく、新しいフォルダーを使用してください。

<a id="removing-a-tool"></a>
## ツールの削除

アプリケーションをアンインストールしても、その設定は自動的に元に戻りません。

- **NVPI:** 必要に応じて、削除する前に意図したプロファイル/表示設定を復元します。
- **NVDF:** 高度な変更/NVENC の変更を復元する場合は、最初にリカバリを使用してください。 Uninstall は、グラフィックス ドライバー、設定、およびバックアップを残します。
- **NVMFG:** ゲームを閉じ、コントローラーを無効化/終了し、NVIDIA リカバリを解決し、削除する前に必要なゲームの SDK バックアップを復元します。
- **RP:** まず、目的のリミッター オーバーライドを削除してください。 Uninstall は、保存された RTSS の上限を消去したり、RTSS を削除したりしません。

正確なデータの場所と制限については各 [プロジェクトガイド](../README.md#projects) を参照し、リカバリ手順が失敗した場合は [サポート](support.md) を参照してください。
