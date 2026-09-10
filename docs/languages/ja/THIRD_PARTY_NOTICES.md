<!-- nv-language-navigation:start -->
🌐 [English](../../../THIRD_PARTY_NOTICES.md) | [Français](../fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/THIRD_PARTY_NOTICES.md) · [বাংলা](../bn/THIRD_PARTY_NOTICES.md) · [简体中文](../zh/THIRD_PARTY_NOTICES.md) · [Čeština](../cs/THIRD_PARTY_NOTICES.md) · [Dansk](../da/THIRD_PARTY_NOTICES.md) · [Nederlands](../nl/THIRD_PARTY_NOTICES.md) · [English](../../../THIRD_PARTY_NOTICES.md) · [Filipino](../fil/THIRD_PARTY_NOTICES.md) · [Suomi](../fi/THIRD_PARTY_NOTICES.md) · [Français](../fr/THIRD_PARTY_NOTICES.md) · [Deutsch](../de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](../el/THIRD_PARTY_NOTICES.md) · [हिन्दी](../hi/THIRD_PARTY_NOTICES.md) · [Magyar](../hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](../id/THIRD_PARTY_NOTICES.md) · [Italiano](../it/THIRD_PARTY_NOTICES.md) · **日本語** · [한국어](../ko/THIRD_PARTY_NOTICES.md) · [मराठी](../mr/THIRD_PARTY_NOTICES.md) · [فارسی](../fa/THIRD_PARTY_NOTICES.md) · [Polski](../pl/THIRD_PARTY_NOTICES.md) · [Português](../pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](../pa/THIRD_PARTY_NOTICES.md) · [Română](../ro/THIRD_PARTY_NOTICES.md) · [Русский](../ru/THIRD_PARTY_NOTICES.md) · [Español](../es/THIRD_PARTY_NOTICES.md) · [Kiswahili](../sw/THIRD_PARTY_NOTICES.md) · [Svenska](../sv/THIRD_PARTY_NOTICES.md) · [தமிழ்](../ta/THIRD_PARTY_NOTICES.md) · [ไทย](../th/THIRD_PARTY_NOTICES.md) · [Türkçe](../tr/THIRD_PARTY_NOTICES.md) · [Українська](../uk/THIRD_PARTY_NOTICES.md) · [اردو](../ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](../vi/THIRD_PARTY_NOTICES.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="third-party-notices-and-credits"></a>
# サードパーティの通知とクレジット

初回監査: 2026-09-09; NVDriverForge 0.1.3 および来歴の更新: 2026-09-10。 **コンポーネントのライセンスは、スイート全体ではなく、そのコンポーネントをカバーします。** アプリケーションのソースは非公開のままです。著作権および許可通知はそのまま保持されます。このテーブルはインデックスであり、テーブルの代替ではありません。 「外部」とは、アプリケーション資産に分散されていないことを意味します。

| コンポーネント / オリジナルプロジェクト | 著者 | 公式サイト、リポジトリ、またはダウンロード | ライセンス/通知 | NV Toolsで使用 | 修正 |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k;著作権 2016 | [リポジトリ](https://github.com/Orbmu2k/nvidiaProfileInspector), [ダウンロード](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](../../../NVIDIA-Profile-Inspector/LICENSE) | NVPI fork 全体。 NVDF テーマ/拡張インターフェイスのリファレンス。 NVMFG ラッパー/スタイル。 RP UI リソース | Fork サービス、トランザクション、およびランチャーを表示します。テーマ/コントロールの統合とラッパーの適応 |
| RTX40MFG-Unlock | Michael Robles / dashdogy;著作権 2026 | [リポジトリ](https://github.com/dashdogy/RTX40MFG-Unlock), [ダウンロード](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](../../../NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | 比較/改良リファレンスと共有/適応された NVMFG ネイティブ コンポーネント。独自に開発したアプリケーション | 集中読み込み、NGX/コントローラー調整、ゲームごと/V-Sync の統合と診断 |
| MinHook、8fda4f5 で固定 | Tsuda Kageyu;著作権 2009–2017 | [リポジトリ](https://github.com/TsudaKageyu/minhook), [ピン留めされたソース](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2 条項の通知](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | NVMFG エンジンに静的にコンパイルされる | 継承されたコピーに対するテキストの書式設定を除いて、含まれるサブセットは変更されません |
| Hacker Disassembler Engine (HDE64) | Vyacheslav Patkov;著作権 2008–2009 | [MinHook のソースコレクション](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [MinHook/HDE に関する完全な通知](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | NVMFG の MinHook デコーダ | 機能的な変更は確認されていません。実稼働環境では HDE64 が使用されているにもかかわらず、HDE32 通知が保持される |
| Streamline 2.12 統合ヘッダー | NVIDIA Corporation;著作権 2023 | [リポジトリ](https://github.com/NVIDIA-RTX/Streamline), [ダウンロード](https://github.com/NVIDIA-RTX/Streamline/releases) | [対象となるヘッダーの場合は MIT](../../../NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | NVMFG Streamline 統合をコンパイルします | ヘッダーは変更されていません。アプリケーション パッケージにランタイム DLL がありません |
| NVIDIA NGX / DLSS SDK ヘッダー | NVIDIA Corporation | [固定されたリポジトリ](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [NVIDIA RTX SDK 用語](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [ヘッダー通知](../../../NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | NVMFG NGX 統合をコンパイルします | ヘッダーは変更されていません。 NGX モデル/プロバイダーはバンドルされていません。以下に説明する未解決の制限 |
| .NET ランタイム 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation、Microsoft、および貢献者 | [ソース](https://github.com/dotnet/runtime), [ダウンロード](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-NET-LICENSE.txt) および [完全なサードパーティ通知](../../../licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | 自己完結型の NVDF および NVMFG アプリ/エージェント | ランタイムは変更されていません |
| WPF / Windows Desktop Runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation、Microsoft、および貢献者 | [ソース](https://github.com/dotnet/wpf), [ダウンロード](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-WPF-LICENSE.txt)、上記のランタイム通知 | NVDF および NVMFG ユーザー インターフェイス | フレームワークは変更されていません。アプリケーション UI は個別に作成/調整される |
| .NET フレームワーク 4.8 | Microsoft | [公式ランタイムのダウンロード](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | Microsoft プラットフォーム/ランタイム条件。外部 | NVPI、RP、および NVMFG プロファイル ヘルパー | なし。このハブによって再配布されるインストーラーまたはフレームワーク DLL はありません |
| 7-Zip 26.03 x64 | Igor Pavlov;著作権 1999–2026 | [サイト/ダウンロード](https://www.7-zip.org/download.html), [正確なソースアーカイブ](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | [完全な通知](../../../licenses/third-party/7-Zip.txt)、[LGPL 2.1-or-later](../../../licenses/third-party/LGPL-2.1.txt)、BSD 部分および unRAR 制限 | NVDF は未変更の 7z.exe/7z.dll を埋め込み、CLI を別のプロセスとして実行します | 変更なし |
| Inno Setup 7.1.0 | Jordan Russell、Martijn Laan および貢献者 | [サイト/ダウンロード](https://jrsoftware.org/isinfo.php), [ソース](https://github.com/jrsoftware/issrc) | [オリジナルのInno Setupライセンス](../../../licenses/third-party/Inno-Setup.txt) | インストーラー エンジンと生成されたアンインストーラー | エンジン/コンパイラは未修正。プロジェクト スクリプト、ブランディング、ネイティブ フォーカス処理を適応 |
| Inno Setup 翻訳カタログ | 指名されたオリジナルの翻訳者 | [公式コレクション](https://jrsoftware.org/files/istrans/) | Inno/カタログ通知および[完全なヘッダークレジット](../../../licenses/INSTALLER-TRANSLATORS.md) | NVPI セットアップ リビジョン 2 を含む、4 つのインストーラーすべての 34 言語の共有カタログ | キー、ID、フォント、技術的な英語フォールバック。必要に応じて、プロジェクトが作成したプレビュー カタログ |
| Microsoft Visual C++ ランタイム / Windows SDK サポート | Microsoft | [ビジュアルStudioツール](https://visualstudio.microsoft.com/downloads/), [再配布条件インデックス](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft ツールチェーン/ランタイム条件。このテーブルでは MIT ではありません | ネイティブ エンジン/ブートストラップ バイナリの静的リリース CRT。インストールされた Windows API | ランタイムソースは変更されません。コンパイラなし、SDK またはデバッグ ランタイム配布なし |
| RivaTuner Statistics Server (RTSS) | Unwinder | [公式 Guru3D ダウンロード](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | ベンダー規約。 「フリーウェア」から推測される再配布許可なし | RP には外部リミッターが必要です。 UpdateProfiles エクスポートがインストールされました | RTSS コード/バイナリは変更またはバンドルされていません。 RP は選択されたプロファイル キーを書き込みます |
| NVIDIA ドライバー / NVAPI / NVML | NVIDIA Corporation | [ドライバーのダウンロード](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA ドライバー/SDK 用語。外部の | インストールされたネイティブ インターフェイスと明示的なオリジナル ドライバーのダウンロード | ハブ資産に NVIDIA DLL はありません。 NVDF のオプションの NVENC 操作は、ユーザーが選択したインストール済み DLL を変更します |
| NVIDIA NGX プロバイダー/モデルおよび Streamline ランタイム | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Streamline リリース](https://github.com/NVIDIA-RTX/Streamline/releases) | MIT ヘッダーとは異なる、コンポーネント固有の NVIDIA 用語 | NVMFG によって使用される外部ゲーム/ドライバー コンポーネント。 SDK はリクエスト時にのみフェッチされます | NVMFG は実験的なメモリ内動作の変更を適用します。 SDK ゲームのコピーはバックアップを使用して更新できます |
| keylase/nvidia-patch | keylase と貢献者 | [リポジトリ](https://github.com/keylase/nvidia-patch), [Windows データ](https://github.com/keylase/nvidia-patch/tree/master/win) | 再配布ライセンスはこの監査によって確立されませんでした | 外部オプションの NVDF NVENC カタログ/パッチ データ、選択ごとに 1 つの固定コミットから取得 | アップストリームのソース、パッチャー、またはパッチ データがハブ/アプリケーション アセットにコピーされない |
| NVCleanstall | TechPowerUp | [公式ページ・ダウンロード](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | 独自の配布。ソース/バイナリの再配布許可が推測されません | NVDF のワークフローとオプションのインスピレーション | インポートされたソースまたはバイナリはありません。 fork またはランタイム依存関係ではない |

<a id="obligations-and-boundaries"></a>
## 義務と境界

**MIT コンポーネント:** 著作権、許可文および免責事項はコピーとともに保持されます。彼らのライセンスでは、変更されたソースの公開は必要ありません。アプリケーションのソースが非公開で維持されている場合でも、元の作成者は保持されます。

**MinHook/HDE:** 通知、条件、免責事項をバイナリ ドキュメントに保存します。完全に組み合わされた通知が提供されます。

**7-Zip:** LGPL/BSD/unRAR 通知を保存し、変更されていない正確なソースへのアクセスを提供します。ソース アーカイブは完全な LGPL とともに上にリンクされています。 unRAR 制限は、関連する解凍コードに適用されます。これは、包括的な MIT 依存関係ではありません。著者の [配布に関するよくある質問](https://www.7-zip.org/faq.html) を参照してください。

**Inno Setup:** 必要なエンジンの著作権/Web サイトの通知を保持し、該当する場合はソースの変更をマークします。変更されていないエンジンのクレジットはインストーラーに残ります。適応されたカタログには、元の情報源の通知が保持されます。名前はここにインデックスされています。

**NVIDIA の内容:** Streamline 統合ヘッダーの MIT ライセンスは、すべての SDK ファイルをカバーするわけではありません。その通知では、Nsight Perf SDK マテリアルを明示的に分離しています。その材料はこの生産目標には使用されていません。 NGX ヘッダーには、NVIDIA 独自の RTX SDK 条件が適用されます。全文が [元のバイトのコピー](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt) とともに追加されました。技術的制限に関するセクション 4(d) の制限は、NVMFG の使用に関して未解決のままです。他の MOD の存在からは積極的な許可が推測されません。

**外部の未知/独自コンポーネント:** RTSS、NVCleanstall、NVIDIA ドライバー、モデル、および keylase パッチ データは、準備されたハブ アセットにバンドルされていません。リンクは実際の所有者を識別します。ユーザーがトリガーしたダウンロードでは、コンポーネントのライセンスが再取得されません。

このツールは、Windows が提供する API とフォントを使用します。 Windows SDK/compiler/font ファイルはこの Git リポジトリにコピーされません。ビルド ツールとプライベート テストは外部配布です。ランタイム内部コンポーネントの通知は、発行者に再割り当てされるのではなく、完全な Microsoft 通知ファイルに残ります。

<a id="publisher-contributions"></a>
## 出版社の寄稿

禅堂 Zendo (RevoluSound Team) は、[来歴ガイド](docs/provenance.md) で説明されている元のアプリケーションの作業、適応、およびドキュメントを維持します。 [NVPI](NVIDIA-Profile-Inspector/README.md)、[NVDF](NVDriverForge/README.md)、[NVMFG](NVMFG-Unlock40/README.md)、および [RP](NVRasterPulse/README.md) はそれぞれ、継承された作業と変更を区別します。

独立したプロジェクト。 NVIDIA Corporation またはリストされた上流の著者との提携、スポンサーシップ、または公式の承認は黙示されません。
