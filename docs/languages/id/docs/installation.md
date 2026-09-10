<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · **Bahasa Indonesia** · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Panduan instalasi

Mulailah dengan [Unduhan](downloads.md), yang mencatat status publikasi dan nama aset sebenarnya. Ini adalah alat yang terpisah: instal hanya alat yang Anda perlukan.

> **Untuk NVRasterPulse, instal [RTSS dari Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) sebelum membuka pengelola profil.**
> RTSS harus dijalankan untuk menerapkan batasan; itu tidak termasuk dalam NV Tools.

| Alat | Edisi terinstal | Edisi portabel | Prasyarat utama |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Ekstrak ZIP NVPI lengkap | Driver NVIDIA dan .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, termasuk waktu proses | Paket driver NVIDIA asli yang kompatibel untuk operasi instalasi |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Ekstrak ZIP NVMFG lengkap, simpan subfoldernya | RTX 40, DLSS FG yang ada, penyedia yang tepat dan pembantu .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Ekstrak ZIP RP lengkap | RTSS dan .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Unduh, verifikasi, instal

1. Pada Rilis terbitan yang dipilih, unduh aset aplikasi bernama, pemberitahuan ZIP dan SHA256SUMS.txt.
2. Gunakan [Contoh SHA-256](downloads.md#sha-256), dengan nama file unduhan sebenarnya.
3. Untuk Pengaturan, ikuti penginstal normal. Untuk ZIP portabel, ekstrak semuanya ke folder lokal baru yang dapat ditulisi; jangan dijalankan dari dalam ZIP.
4. Buka EXE aplikasi itu sendiri. Simpan file lisensi/konfigurasi/data yang menyertainya.
5. Baca petunjuk penggunaan alat tersebut sebelum mengaktifkan pengaturan atau pengoperasian sistem.

Biner saat ini tidak ditandatangani. Hash yang cocok mengonfirmasi byte yang diharapkan; ini bukan sertifikat keamanan atau kompatibilitas. Jangan nonaktifkan perlindungan keamanan Windows hanya untuk menyembunyikan peringatan.

Menginstal NVDF atau pendamping opsional NVPI terpisah dari menginstal driver GPU. Pendamping NVPI tetap menggunakan nama instalasi internal yang ada. Tombol RasterPulse yang ditinggikan memerlukan instalasi seluruh sistem yang dilindungi; salinan RP lainnya dapat dibuka melalui pintasannya sendiri.

NVMFG bersifat eksperimental dan memiliki [cadangan lisensi NVIDIA SDK yang terdokumentasi](provenance.md). Tidak ada driver NVIDIA, penyedia/model NGX, atau runtime game Streamline yang disertakan. Pengunduhan SDK dan pembaruan game tertentu merupakan operasi terpisah yang eksplisit.

<a id="language-and-updates"></a>
## Bahasa dan pembaruan

Gunakan pemilih 34 bahasa README untuk dokumentasi. NVDF, NVMFG dan RP memiliki pengaturan UI 34 bahasanya sendiri; NVPI mempertahankan dukungan bahasa yang ada. Beberapa string teknis penginstal kembali ke bahasa Inggris.

Simpan identitas instalasi alat saat memperbarui. Tutup terlebih dahulu dan simpan cadangannya. Untuk NVMFG, tutup game yang terpengaruh dan selesaikan pemulihan profil yang tertunda. Untuk pembaruan portabel, gunakan folder baru daripada menggabungkan rilis.

<a id="removing-a-tool"></a>
## Menghapus alat

Mencopot pemasangan aplikasi tidak secara otomatis membatalkan pengaturannya.

- **NVPI:** memulihkan profil/pengaturan tampilan yang diinginkan sebelum penghapusan jika diperlukan.
- **NVDF:** gunakan pemulihan terlebih dahulu jika Anda ingin memulihkan perubahan lanjutan/NVENC. Uninstall meninggalkan driver grafis, pengaturan dan cadangan.
- **NVMFG:** menutup game, menonaktifkan/keluar dari pengontrol, menyelesaikan pemulihan NVIDIA dan memulihkan cadangan SDK game yang diinginkan sebelum penghapusan.
- **RP:** hapus penggantian pembatas yang dimaksudkan terlebih dahulu. Uninstall tidak menghapus batas RTSS yang disimpan atau menghapus RTSS.

Lihat setiap [panduan proyek](../README.md#projects) untuk lokasi dan batasan data yang tepat, atau [dukungan](support.md) jika langkah pemulihan gagal.
