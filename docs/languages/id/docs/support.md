<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · **Bahasa Indonesia** · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatibilitas dan pemecahan masalah

Ini adalah kandidat yang telah disiapkan, bukan matriks sertifikasi untuk semua kombinasi Windows, GPU, driver, dan game.

| Alat | Windows/waktu proses | Ketergantungan perangkat keras / eksternal | Operasi memerlukan perawatan |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Driver/layar NVIDIA yang kompatibel | Penulisan profil dan pratinjau tampilan |
| NVDriverForge 0.1.4 | Windows 10 membangun 19041+ / 11x64; .NET/WPF disertakan | Paket driver NVIDIA yang kompatibel | Instalasi yang ditingkatkan, pengaturan lanjutan, NVENC opsional |
| NVMFG Unlock40 0.2.3 | Windows 10/11x64; Termasuk .NET/WPF, pembantu Framework 4.8 | RTX 40, game FG DLSS yang memenuhi syarat dan penyedia yang disematkan | Patching asli dalam game, jurnal profil global, pembaruan game SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS diinstal; berlari untuk topi | RTSS perubahan profil per-eksekusi |

Tidak ada paket ARM64 yang disiapkan. Ketersediaan tampilan/API dan versi Windows yang lama dapat membatasi fitur individual. Tidak ada versi NVIDIA atau RTSS minimum universal yang ditemukan. Hash penyedia NVMFG yang tepat ada di [asal](provenance.md).

<a id="before-reporting-a-bug"></a>
## Sebelum melaporkan bug

Identifikasi executable/versi persis yang Anda buka. Salinan yang diinstal sebelumnya belum tentu merupakan versi ZIP yang baru diunduh. Catat langkah-langkah reproduksi, hasil yang diharapkan dan hasil aktual. Untuk masalah rendering/pembatasan, sertakan versi game, penyegaran tampilan, status FG/V-Sync/VRR, dan pembatas atau overlay lainnya.

Gunakan [bentuk bug](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Jangan pernah melampirkan seluruh folder pengembangan pribadi, arsip driver, model, DLL game, dump registri, atau kumpulan log yang belum ditinjau.

| Masalah | Pemeriksaan pertama |
| --- | --- |
| Versi aplikasi salah | Konfirmasikan identitas EXE dan rilis hash; tutup salinan lama sebelum penggantian. |
| Kesalahan waktu proses/penyalaan | Instal Framework 4.8 yang diperlukan atau simpan semua subfolder portabel yang disediakan. |
| UAC dibatalkan | Coba lagi hanya operasi yang dimaksudkan; pembatalan instalasi tidak berhasil. |
| Ketidakcocokan hash/tanda tangan | Berhenti menggunakan kandidat itu dan dapatkan byte resmi yang diharapkan. |
| Warna/mode NVPI ditolak | Kembalikan dan gunakan kombinasi yang didukung oleh tampilan/driver sebenarnya. |
| Kegagalan pencadangan atau pemulihan NVDF | Pertahankan pekerjaan yang dilindungi dan RECOVERY.txt; jangan menghapus jurnal atau memaksakan penulisan yang bertentangan. |
| Pengaturan NVMFG tertunda | Selesaikan pemulihan dengan game ditutup, pertahankan perubahan dari alat lain. |
| Batas RP tidak berpengaruh | Jalankan RTSS, identifikasi EXE game sebenarnya, periksa status hook dan batas persaingan. |
| Tutup RP tetap ada setelah dilepas | Periksa RTSS Global; penghapusan hanya mengubah pengesampingan pembatas lokal saja. |

NVDriverForge menawarkan laporan JSON lokal yang dapat dipratinjau; NVMFG menawarkan diagnostik di Tentang. Pilih laporan yang difilter ini daripada arsip log lengkap dan periksa sebelum dibagikan. Penyumbatan restorasi yang dilaporkan pada NVMFG 0.1.1 masih belum diketahui penyebabnya; simpan jurnalnya dan catat kode kesalahan yang ada. NVRasterPulse 0.2 menawarkan diagnostik konfigurasi dalam menu tindakannya, tanpa mengukur FPS.

<a id="logs-and-privacy"></a>
## Log dan privasi

| Alat | Data lokal untuk ditinjau, bukan diunggah secara grosir |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; pekerjaan yang dilindungi `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; cadangan `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` di samping EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` di bawahnya |
| NVPI | Ekspor pilihan Anda dan kesalahan yang ditampilkan; tidak ada jalur log universal yang ditemukan |

Hapus nama akun, direktori home, jalur perpustakaan game, pengidentifikasi perangkat, token, dan jendela yang tidak terkait dari teks/gambar yang Anda bagikan. Simpan dokumen asli secara pribadi untuk pemulihan. Masalah Publik dapat dilihat oleh semua orang.

Untuk kerentanan, perilaku istimewa yang berbahaya, atau operasi destruktif yang tidak disengaja, ikuti [SECURITY.md](../SECURITY.md) daripada memposting detail secara publik.

<a id="what-has-been-verified"></a>
## Apa yang telah diverifikasi

Untuk persiapan hub, pemindaian payload/ZIP/hash/metadata statis dan pemeriksaan dokumentasi dijalankan. Pengujian build/unit/UI aplikasi pribadi yang ada merupakan bukti historis dan tertanggal. Tidak ada pemasangan driver, perubahan tampilan, pengoperasian RTSS langsung, atau benchmark game yang dilakukan sebagai bagian dari persiapan ini.

“Terdeteksi”, “tertulis”, “dimuat ulang”, “kemampuan tersedia” dan “diukur dalam game” adalah hasil yang berbeda. Laporkan yang mana yang Anda amati.
