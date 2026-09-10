<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · **Bahasa Indonesia** · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Arsitektur dan pemeliharaan repositori

NV Laboratory adalah **pusat dokumentasi dan distribusi biner** publik. Itu tidak mengandung sumber aplikasi. Keempat proyek mempertahankan pohon pembangunan, versi, identitas, dan aset rilis yang terpisah. Riwayat pengembangan pribadinya tidak diimpor ke repositori Git ini.

<a id="layout"></a>
## Tata Letak

| Lokasi | Tujuan |
| --- | --- |
| README.md / README.fr.md | Titik masuk Inggris/Prancis |
| Empat folder proyek | Panduan lengkap dan pemberitahuan asli yang berlaku |
| dokumen | Prosedur pengunduhan, kompatibilitas, asal, pengembangan, dan rilis |
| dokumen/releases.json | Metadata, ukuran, dan hash kandidat/rilis yang diaudit |
| dokumen/asal | Perbandingan file/hash; tidak ada kode aplikasi |
| lisensi | Berbagi teks lengkap pihak ketiga dan kredit penerjemah pemasang |
| aset | Pratinjau UI yang sudah ditinjau dan asal usulnya |
| .github | Mengeluarkan formulir dan validasi dokumentasi read-only |
| alat/validate_repository.py | Pemeriksaan batas publikasi dan tautan perpustakaan standar |

Bahasa Inggris tetap menjadi README GitHub default. Tautan `.fr.md` yang berdekatan dan ada tetap valid. Terjemahan tambahan mencerminkan dokumentasi di bawah `docs/languages/<code>`; pemilih bahasa mempertahankan halaman yang sama saat berpindah bahasa. Katalog `docs/languages/catalog.json` mencatat 34 bahasa dan sidik jari sumber. GitHub tidak secara otomatis memilih README berdasarkan bahasa browser. Lihat [indeks bahasa dan kebijakan terjemahan](../../README.md).

<a id="application-technologies"></a>
## Teknologi aplikasi

| Program | Teknologi swasta | Distribusi |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, interop NVAPI/Windows | Lengkapi folder portabel dan pisahkan Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; bootstrap C++ asli; Proses 7-Zip | EXE dan Pengaturan portabel mandiri |
| NVMFG Unlock40 | C#/WPF .NET 8, pembantu Framework 4.8, mesin C++20/MASM/MinHook | Pohon portabel dan Pengaturan |
| NVRasterPulse | Kerangka C#/WPF 4.8; Integrasi profil/muat ulang RTSS; bootstrap asli | Pohon portabel dan Pengaturan |

Pembayaran publik ini tidak dapat membangun kembali aplikasi. Arsip “Source code” otomatis adalah snapshot hub. Tautan sumber hulu tidak mewakili sumber pribadi yang dimodifikasi. CI publik hanya memvalidasi repositori ini.

<a id="local-checks"></a>
## Pemeriksaan lokal

Dari root repositori:

```text
python tools/validate_repository.py
```

Python 3.10 atau yang lebih baru sudah cukup. Pemeriksaan tersebut membaca file, tautan Penurunan harga lokal, pemberitahuan yang diperlukan/tautan RTSS, metadata rilis, dan batasan publikasi. Itu tidak menjalankan perangkat lunak, menginstal dependensi atau menghubungi jaringan.

Alur kerja GitHub menjalankan pemeriksaan yang sama dengan izin konten hanya baca pada permintaan push, pull, atau pengiriman manual. Checkout disematkan ke penerapan yang diaudit dan tidak mempertahankan kredensial. Tidak ada pekerjaan rilis atau penerapan yang dikonfigurasi.

<a id="maintain-the-boundary"></a>
## Pertahankan batasnya

Perbarui referensi bahasa Inggris, panduan bahasa Prancis, dan terjemahan yang terpengaruh secara bersamaan. Pisahkan perubahan substantif dari perbandingan format saja. Catat hash kandidat aktual, referensi dan lisensi penerapan hulu; jangan pernah menyimpulkan lisensi dari popularitas suatu proyek.

Gunakan aset Rilis versi baru dan audit ulang binari, arsip, dan pemberitahuan tersemat yang diubah. Pertahankan cadangan pribadi di luar repositori ini. Jangan gunakan alur kerja publik untuk mengimpor sumber aplikasi pribadi atau folder build lokal.

Pengujian yang sesuai dengan perubahan aplikasi fungsional dijalankan di proyek pribadi. Jangan menjalankan kembali penginstal driver atau menulis profil asli untuk pembaruan dokumentasi. [Prosedur pelepasan manual](releasing.md).
