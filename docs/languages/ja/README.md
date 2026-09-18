<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · **日本語** · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 英語からの機械翻訳。技術名、コマンド、URL、および元の法的文書は保存されます。ネイティブスピーカーによるレビューは歓迎です。表現が不明瞭な場合は、英語のリファレンスを参照してください。
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools by 禅堂 Zendo (RevoluSound Team)。** NVIDIA ドライバー プロファイル、ドライバーのインストール、実験的な Multi Frame Generation および RTSS フレーム制限用の 4 つの独立した Windows ユーティリティ。

[ツールを入手する](docs/downloads.md) · [インストール](docs/installation.md) · [互換性とヘルプ](docs/support.md) · [クレジットとライセンス](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse には RTSS が必要です。** 最初に [Guru3D の RivaTuner Statistics Server](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) をインストールしてください。 FPS の制限が機能するには、RTSS が実行されている必要があります。別途ダウンロードされます。

<a id="projects"></a>
## プロジェクト

| プロジェクト | 目的 | バージョン | ドキュメント | ダウンロード |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA ドライバー プロファイル エディターには、ディスプレイ、カラー、HDR および ICC/WCS コントロールが追加されました。以前は NVPI Custom。 | 3.0.2.3 | [ガイド](NVIDIA-Profile-Inspector/README.md) | [パッケージ](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | ガイド付きの選択、バックアップ、リカバリを使用して、オリジナルの NVIDIA ドライバーを準備してインストールします。 | 0.1.4 | [ガイド](NVDriverForge/README.md) | [パッケージ](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | 実験的な RTX 40 MFG、永続的なゲーム ライブラリ、診断、および Streamline SDK メンテナンス。 | 0.2.3 | [ガイド](NVMFG-Unlock40/README.md) | [パッケージとステータス](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | プログラムごとの RTSS FPS 制限を管理します: 診断、提案、一時停止、元に戻す、プロファイル共有。 | 0.2 | [ガイド](NVRasterPulse/README.md) | [パッケージ](docs/downloads.md#nvrasterpulse) |

**ダウンロード:** [ダウンロードページ](docs/downloads.md) には、各バージョンのステータス、ファイル、および SHA-256 値がリストされています。実験的な機能と互換性の制限については、プロジェクト ガイドに記載されています。

<a id="start-here"></a>
## ここから始めましょう

1. 上のツールを 1 つ選択してください。それぞれが独立して動作します。スイート全体をインストールする必要はありません。
2. 要件を読み、インストールされているアプリの場合は **セットアップ**、別のフォルダーの場合は **ポータブル** を選択します。
3. リリースが公開されたら、指定されたアプリケーション アセットをダウンロードし、付随する通知を読み、その SHA-256 を比較してください。
4. ドライバー、ディスプレイ設定、NVIDIA プロファイル、またはゲーム ランタイムを変更する前にバックアップを作成してください。

ドキュメントは、各ガイドの上部にあるセレクターを使用して、NV アプリケーションと同じ 34 言語で利用できます。 GitHub は、ブラウザ言語ごとに README を自動的に選択しません。ドキュメントの言語とアプリケーション自体の言語設定は別のものです。

<a id="provenance-and-ownership"></a>
## 出所と所有権

このハブはドキュメントとコンパイルされたアプリケーションを配布します。アプリケーションのソースコードは非公開で管理されます。上流プロジェクトはその著作者とライセンスを保持します。プライベート ソースの配布はこれらの用語に置き換わるものではありません。

- Profile Inspector fork は、Orbmu2k の MIT ライセンスを保持しており、fork として明示的に識別されます。
- NVDriverForge には独自のバイナリ配布条件があり、別途ライセンスが必要なランタイム/ツール コンポーネントが含まれています。
- NVMFG Unlock40 は独自に開発されたアプリケーションです。比較と改良のために RTX40MFG-Unlock が参照されました。共有ネイティブ コンポーネントは、MIT クレジットを保持します。 MinHook と NVIDIA SDK の用語は別個のままです。
- NVRasterPulse は、提供された MIT ライセンスを保持し、Profile Inspector 派生の UI をクレジットします。 RTSS は必須の外部プログラムです。

[完全なコンポーネント表](THIRD_PARTY_NOTICES.md)、[ファイルの出所と変更点](docs/provenance.md)、および [ライセンスの範囲](../../../LICENSE) を参照してください。

<a id="other-projects--revolusound-team"></a>
## その他のプロジェクト – RevoluSound Team

これらは別個のオーディオ MOD プロジェクトであり、チームの作業を見つけるのに役立つようにここにリンクされています。

| ゲーム | プロジェクト | について |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | エンジン、排気、吸気、ターボ効果をカバーする車両サウンドの変化。 |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | チームの後期 FH5 車両オーディオ パック。 |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | 以前の FH5 パック。その Nexus ページは、訪問者を上記の後のチーム パックに誘導します。 |

タイトルはリンク先の Nexus Mods ページに従います。ダウンロード、要件、クレジット、許可は Nexus Mods に残ります。

<a id="help-and-participation"></a>
## お手伝いと参加

[バグを報告するか、機能を提案してください](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [貢献する](CONTRIBUTING.md) · [セキュリティレポート](SECURITY.md) · [変更履歴](CHANGELOG.md)

セキュリティの問題については、ログや技術的な詳細を投稿する前に SECURITY.md をお読みください。プライベート レポートは、リポジトリ公開後にメンテナによって有効化される必要があります。

> **独立したコミュニティ プロジェクト。** NV Laboratory、NV Tools、およびこれらのユーティリティは、NVIDIA Corporation と提携、後援、または正式に承認されていません。 NVIDIA、GeForce、RTX、DLSS およびその他の製品名は、それぞれの所有者の商標です。名前は互換性と由来を説明するものであり、公式の承認を示すものではありません。
