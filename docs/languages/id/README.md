<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · **Bahasa Indonesia** · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools oleh 禅堂 Zendo (RevoluSound Team).** Empat utilitas Windows independen untuk profil driver NVIDIA, instalasi driver, batas bingkai Multi Frame Generation eksperimental dan RTSS.

[Dapatkan alatnya](docs/downloads.md) · [Instalasi](docs/installation.md) · [Kompatibilitas & bantuan](docs/support.md) · [Kredit & lisensi](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse memerlukan RTSS.** Instal [RivaTuner Statistics Server dari Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) terlebih dahulu. RTSS harus berjalan agar batas FPS dapat berfungsi. Itu diunduh secara terpisah.

<a id="projects"></a>
## Proyek

| Proyek | Tujuan | Versi | Dokumentasi | Unduh |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Editor profil driver NVIDIA dengan tampilan tambahan, warna, kontrol HDR dan ICC/WCS. Sebelumnya NVPI Custom. | 3.0.2.3 | [Panduan](NVIDIA-Profile-Inspector/README.md) | [Paket](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Pilih komponen driver, tinjau penyesuaian opsional dan instal paket driver NVIDIA asli. | 0.1.3 | [Panduan](NVDriverForge/README.md) | [Paket](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Alat eksperimental RTX 40 MFG dengan pilihan per game dan pemeliharaan Streamline SDK. | 0.1.1 | [Panduan](NVMFG-Unlock40/README.md) | [Paket & status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Kelola batas RTSS FPS per executable, dengan nilai pecahan, cadangan, dan akses baki. | 0.1 | [Panduan](NVRasterPulse/README.md) | [Paket](docs/downloads.md#nvrasterpulse) |

**Unduhan:** [halaman unduhan](docs/downloads.md) mencantumkan status, file, dan nilai SHA-256 setiap versi. Fitur eksperimental dan batas kompatibilitas dijelaskan dalam panduan proyek.

<a id="start-here"></a>
## Mulai di sini

1. Pilih salah satu alat di atas. Masing-masing bekerja secara independen; menginstal seluruh rangkaian tidak diperlukan.
2. Baca persyaratannya dan pilih **Penyiapan** untuk aplikasi yang diinstal, atau **portabel** untuk folder terpisah.
3. Ketika Rilisnya dipublikasikan, unduh aset aplikasi bernama, baca pemberitahuan yang menyertainya dan bandingkan SHA-256-nya.
4. Simpan cadangan sebelum mengubah driver, pengaturan tampilan, profil NVIDIA, atau waktu proses game.

Dokumentasi tersedia dalam 34 bahasa yang sama dengan aplikasi NV melalui pemilih di bagian atas setiap panduan. GitHub tidak secara otomatis memilih README berdasarkan bahasa browser. Bahasa dokumentasi dan pengaturan bahasa aplikasi terpisah.

<a id="provenance-and-ownership"></a>
## Asal dan kepemilikan

Hub ini mendistribusikan dokumentasi dan aplikasi yang dikompilasi. Kode sumber aplikasi dikelola secara pribadi. Proyek-proyek hulu tetap mempertahankan kepemilikan dan lisensinya; distribusi sumber swasta tidak menggantikan istilah-istilah tersebut.

- Profile Inspector fork mempertahankan lisensi MIT Orbmu2k dan secara eksplisit diidentifikasi sebagai fork.
- NVDriverForge memiliki ketentuan distribusi binernya sendiri dan mencakup komponen runtime/alat yang dilisensikan secara terpisah.
- NVMFG Unlock40 adalah aplikasi yang dikembangkan secara independen. RTX40MFG-Unlock dikonsultasikan untuk perbandingan dan penyempurnaan; komponen asli bersama mempertahankan kredit MIT mereka. Ketentuan MinHook dan NVIDIA SDK tetap terpisah.
- NVRasterPulse mempertahankan lisensi MIT yang disediakan dan mengkredit UI turunan Profile Inspector. RTSS adalah program eksternal yang diperlukan.

Lihat [tabel komponen lengkap](THIRD_PARTY_NOTICES.md), [asal file dan perubahannya](docs/provenance.md), dan [ruang lingkup lisensi](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Proyek lainnya – RevoluSound Team

Ini adalah proyek mod audio terpisah, ditautkan di sini untuk membantu Anda menemukan pekerjaan tim.

| Permainan | Proyek | Tentang |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Perubahan suara kendaraan meliputi mesin, knalpot, intake dan efek turbo. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Paket audio kendaraan FH5 tim selanjutnya. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Paket FH5 sebelumnya; halaman Nexus-nya mengarahkan pengunjung ke paket tim selanjutnya di atas. |

Judul mengikuti halaman Nexus Mods yang tertaut. Unduhan, persyaratan, kredit, dan izinnya tetap ada di Nexus Mods.

<a id="help-and-participation"></a>
## Bantuan dan partisipasi

[Laporkan bug atau sarankan fitur](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Berkontribusi](CONTRIBUTING.md) · [Laporan keamanan](SECURITY.md) · [log perubahan](CHANGELOG.md)

Untuk masalah keamanan, baca SECURITY.md sebelum memposting log atau detail teknis. Pelaporan pribadi harus diaktifkan oleh pengelola setelah publikasi repositori.

> **Proyek komunitas independen.** NV Laboratory, NV Tools dan utilitas ini tidak berafiliasi, disponsori oleh, atau didukung secara resmi oleh NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS dan nama produk lainnya adalah merek dagang dari pemiliknya masing-masing. Nama menggambarkan kompatibilitas dan asal, bukan dukungan resmi.
