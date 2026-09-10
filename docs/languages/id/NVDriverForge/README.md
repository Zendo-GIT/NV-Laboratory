<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · **Bahasa Indonesia** · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Siapkan instalasi driver NVIDIA dengan pilihan komponen yang jelas dan pengaturan opsional.**

[Unduh 0.1.3 & status](../docs/downloads.md#nvdriverforge) · [Instalasi](#installation) · [Kredit](#credits-and-upstream) · [Lisensi](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Ikhtisar dan tujuan

NVDriverForge memandu Anda melalui paket driver NVIDIA asli: pilih driver, periksa komponennya, tinjau penyesuaian opsional, lalu konfirmasikan pemasangan. Itu ada untuk membuat pilihan-pilihan tersebut dapat dimengerti dan menjaga instalasi, operasi istimewa, dan informasi pemulihan tetap bersamaan.

Ini adalah aplikasi yang dikembangkan secara independen yang sebagian terinspirasi oleh alur kerja NVCleanstall. Ini tidak termasuk NVCleanstall atau mengklaim paritas fitur lengkap.

<a id="features"></a>
## Fitur

- NVIDIA Game Ready / Studio pencarian dan unduhan; penemuan hotfix opsional dengan fallback manual.
- Analisis paket asli, hash, tanda tangan NVIDIA, manifes, dan entri INF yang kompatibel.
- Pemilihan komponen dengan ketergantungan dan pelestarian komponen yang tidak diketahui.
- Versi 0.1.3 membuat komponen NVIDIA opsional yang dipilih dapat dilewati dan hanya mengecualikan komponen terverifikasi yang tidak dicentang dari penemuan. Runtime opsional yang sudah ada atau tidak dapat diterapkan tidak lagi dipaksakan sebagai komponen penting.
- Hapus ringkasan kegagalan instalasi dan akses ke log terperinci dalam 34 bahasa.
- Konfirmasi instalasi eksplisit, staging yang dilindungi, dan ekspor paket penyimpanan driver yang ada.
- Pengaturan lanjutan opsional, dengan pemeriksaan sebelum penerbangan, jurnal, dan pemulihan sadar konflik.
- Opsional **Custom NV** prasetel dengan pilihan dan penjelasan bernama, termasuk pemilihan kekuatan SILK terpisah dan pemeriksaan kompatibilitas.
- Unduhan patch NVENC versi tepat opsional; komit sumber dan byte target diperiksa.
- Instalasi opsional Profile Inspector fork yang terpisah dari layar Alat.
- Pemeriksaan pembaruan pengguna yang diinstal opsional, 34 bahasa antarmuka dan empat tema.

Opsi lanjutan yang tersedia berkaitan dengan MPO, indikator DLSS, Ansel, tidur audio NVIDIA, MSI, kebijakan/prioritas interupsi, HDCP, pengaktifan wadah tampilan, dan layanan telemetri lama yang memenuhi syarat. Masing-masing memiliki prasyarat dan dampaknya sendiri; ini bukanlah peningkatan kinerja universal.

<a id="compatibility"></a>
## Kompatibilitas

| Persyaratan | Detail |
| --- | --- |
| Sistem | Windows 10 build 19041 atau lebih baru / Windows 11, x64 |
| GPU/pengemudi | Paket NVIDIA yang kompatibel dan perangkat keras yang terdeteksi; pencarian katalog otomatis terutama mencakup model GeForce yang dikenal |
| Waktu proses | .NET 8 / WPF 8.0.31 disertakan dalam paket mandiri yang disiapkan |
| Hak istimewa | Pengaturan UI/per pengguna normal; instalasi driver dan perubahan sistem meminta akses administrator |
| Jaringan | Diperlukan untuk pencarian/pengunduhan NVIDIA online dan permintaan NVENC upstream yang eksplisit; driver asli lokal dapat dipilih |
| Alat yang disertakan | 7-Zip 26.03 yang tidak dimodifikasi, pemberitahuan runtime, pendamping MIT Profile Inspector opsional |
| Pendamping opsional | .NET Framework 4.8 untuk Profile Inspector fork terpisah |

Tidak ada versi driver minimum yang mencakup semua fitur. Pencarian multi-GPU harus cocok dengan setiap GPU yang terdeteksi. Model yang tidak didukung/profesional mungkin memerlukan pemilihan driver manual. Penginstal NVIDIA tetap menjadi otoritas perangkat keras/OS terakhir.

<a id="installation"></a>
## Instalasi

1. Kunjungi [unduhan](../docs/downloads.md#nvdriverforge) dan konfirmasikan Rilis telah dipublikasikan.
2. Pilih `NVDriverForge-Setup.exe` untuk instalasi, atau `NVDriverForge.exe` untuk penggunaan portabel.
3. Bandingkan SHA-256 dengan `SHA256SUMS.txt` Rilis.
4. Jalankan Setup untuk instalasi per pengguna dan uninstaller standar, atau letakkan EXE portabel di folder yang dapat ditulisi dan buka.

Perangkat portabel ini mencakup runtime dan penginstal opsionalnya. Menginstal NVDriverForge tidak menginstal driver GPU. EXE-nya saat ini tidak ditandatangani.

<a id="usage"></a>
## Penggunaan

1. **Driver:** unduh dari NVIDIA atau pilih EXE penginstal NVIDIA asli. Biarkan analisis selesai.
2. **Komponen:** meninjau deskripsi dan dependensi yang diperlukan. Komponen yang tidak diketahui dipertahankan.
3. **Tweaks:** biarkan opsi yang tidak diinginkan tidak berubah. Baca efek dan trade-off sebelum memilih apa pun.
4. **Ulasan:** periksa driver, komponen, dan operasi opsional yang sebenarnya, lalu konfirmasikan pemasangan.
5. Terima UAC hanya untuk operasi yang Anda pilih. Simpan instruksi pemulihan pekerjaan yang dilindungi.
6. Jika driver baru perlu dimulai ulang, ikuti status yang dilaporkan. Operasi yang ditangguhkan memerlukan resume eksplisit setelah restart tersebut.

Custom NV dimulai tanpa perubahan. Pilih nilai bernama individual atau tinjau preset yang disediakan dan pengecualiannya. Dua bidang informasi internalnya tidak ditulis secara independen. Pengaturan hanya diterapkan dalam alur kerja driver baru yang terverifikasi, tidak pernah dengan membuka pratinjau. Menginstal editor NVPI terpisah tidak diperlukan.

Pekerjaan NVENC opsional mengunduh data yang kompatibel dari komitmen keylase yang disematkan. Ini mengubah dua DLL driver dan membuat tanda tangannya tidak valid; dapat ditolak dengan Windows, encoder, DRM atau anti-cheat. Tidak ada data atau DLL NVIDIA yang tertanam di NVDriverForge. [Batasan asal dan perizinan](../docs/provenance.md).

Preferensi mengontrol bahasa, tema, dan pemeriksaan pembaruan opsional pengguna yang diinstal. Perangkat portabel tidak membuat tugas pemeriksaan latar belakang yang diinstal. Alat dan pemulihan terpisah dari empat langkah instalasi.

<a id="screenshots"></a>
## Tangkapan layar

![Pratinjau halaman driver NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Render UI Prancis 0.1.2 yang ada dengan data contoh; dipertahankan sebagai pratinjau antarmuka. Driver 699.99 yang ditampilkan adalah perlengkapan uji, bukan versi nyata untuk diunduh. [Asal gambar](../assets/README.md).

<a id="update-and-uninstall"></a>
## Perbarui dan hapus instalan

Tutup NVDriverForge, dapatkan paket resmi berikutnya dan verifikasi hashnya. Gunakan identitas penataan yang sama untuk pembaruan yang diinstal; ganti EXE portabel yang tertutup dengan yang baru. Simpan pengaturan dan pekerjaan yang dilindungi.

Uninstall dari Windows **Installed apps**. Ini menghapus aplikasi dan tugas pembaruannya, bukan driver NVIDIA. Pengaturan, log, dan cadangan tetap ada. Jika diinginkan, pulihkan perubahan tingkat lanjut/NVENC melalui alur pemulihan yang terdokumentasi **sebelum** menghapus aplikasi. Pemulihan menolak perubahan yang bertentangan dari alat lain.

Data lokal berada di bawah `%LOCALAPPDATA%\NVDriverForge`; pekerjaan yang dilindungi dan ekspor pengemudi berada di bawah `%PROGRAMDATA%\NVDriverForge\Jobs`. Penggunaan portabel juga menghasilkan data lokal. Ekspor penyimpanan driver bukanlah citra sistem atau cadangan profil lengkap.

<a id="known-limitations"></a>
## Keterbatasan yang diketahui

- Tidak ada penambahan perangkat keras/pengeditan INF, pembuatan ulang tanda tangan NVIDIA, pengunduran diri yang kompatibel dengan anti-cheat, atau penerimaan peringatan otomatis yang tidak ditandatangani.
- Tidak ada penghapusan telemetri/iklan lengkap, ekspor paket ramping, atau pengembalian penuh otomatis ke driver sebelumnya.
- Instalasi driver, pemulihan boot, dan penulisan profil opsional belum divalidasi secara komprehensif pada mesin nyata oleh audit hub.
- Pembacaan kembali registri bukanlah bukti efek HDCP, kinerja, atau latensi yang sebenarnya.
- Pemeriksaan tanda tangan menggunakan kepercayaan Windows yang tersedia secara lokal; pencabutan online tidak dilakukan.
- Terdapat 34 bahasa, namun pengujian penutur asli/aksesibilitas lengkap masih belum lengkap.

<a id="troubleshooting"></a>
## Pemecahan masalah

| Gejala | Tindakan |
| --- | --- |
| Katalog online tidak tersedia | Pilih paket asli dari [Unduhan driver NVIDIA](https://www.nvidia.com/en-us/drivers/). Jangan mengganti model GPU tetangga. |
| Pencarian perbaikan terbaru tidak tersedia | Gunakan [Forum driver Game Ready NVIDIA](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) dan verifikasi paket sebenarnya. |
| Instalasi NVIDIA gagal | Baca ringkasan kegagalan dan buka log terperinci. Komponen opsional yang sudah ada atau tidak dapat diterapkan tetap dapat dilewati di 0.1.3. Penginstalan yang gagal tidak memicu penyesuaian opsional atau alur sukses/mulai ulang. |
| Kegagalan tanda tangan/hash/cadangan | Hentikan instalasi itu dan pertahankan kesalahannya; dapatkan kembali paket aslinya jika rusak. |
| Opsi tidak tersedia | Baca alasan perangkat keras, komponen, atau driver targetnya; tetap tidak berubah. |
| Mulai ulang atau pekerjaan masih tertunda | Gunakan instruksi pemulihan pekerjaan dan resume eksplisit; jangan hapus jurnalnya. |
| Pulihkan konflik | Keadaan lain berbeda dengan transaksi yang tercatat. Pertahankan dan minta bantuan alih-alih memaksakan pemulihan. |

Untuk laporan, sertakan versi alat yang dipilih, Windows, GPU, driver dan langkah-langkah yang dapat direproduksi; menyunting jalur dan detail pribadi dari log. [Dukungan](../docs/support.md).

<a id="faq"></a>
## Pertanyaan Umum

**Apakah Penyiapan menginstal driver grafis?** Tidak. Hal ini memerlukan analisis, peninjauan, konfirmasi, dan proses instalasi lanjutan yang terpisah dari aplikasi.

**Apakah saya memerlukan NVCleanstall atau NVPI?** Tidak. NVCleanstall hanyalah inspirasi. Pendamping Profile Inspector adalah editor opsional independen.

**Apakah ini membuat setiap driver NVIDIA lebih kecil atau lebih cepat?** Tidak. Komponen dan prasyarat yang dipilih menentukan apa yang dapat berubah; tidak ada keuntungan terukur yang dijanjikan.

**Di mana sumbernya?** Sumber khusus aplikasi dan pengujian pribadi dikelola secara terpisah. Hub ini menyediakan dokumentasi, biner, dan tautan sumber pihak ketiga yang diperlukan untuk atribusi/lisensi.

<a id="credits-and-upstream"></a>
## Kredit dan hulu

Aplikasi asli, alur kerja, transaksi, lokalisasi, bootstrap dan adaptasi: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspirasi alur kerja; tidak ada sumber atau biner yang diimpor.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): Tema MIT, referensi antarmuka NVAPI yang diperluas dan fork yang dikemas secara terpisah.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): alat ekstraksi yang tidak dimodifikasi.
- [Microsoft .NET](https://github.com/dotnet/runtime) dan [WPF](https://github.com/dotnet/wpf): runtime yang dibundel.
- [Inno Setup](https://jrsoftware.org/isinfo.php): mesin pemasang asli dan terjemahan yang dikreditkan.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): sumber data NVENC opsional eksternal; izin redistribusi tidak ditetapkan.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): pengunduhan driver eksternal dan instalasi pustaka NVAPI/NVML.

[Tabel komponen lengkap](../THIRD_PARTY_NOTICES.md) · [Perubahan dan asal usulnya](../docs/provenance.md)

<a id="license"></a>
## Lisensi

[Izin distribusi biner yang ada](../../../../NVDriverForge/LICENSE) mengizinkan penggunaan dan berbagi file executable resmi yang tidak dimodifikasi dengan pemberitahuannya. Hak sumber khusus aplikasi dilindungi undang-undang. Ini tidak membatasi hak yang diberikan oleh lisensi pihak ketiga yang terpisah. [Pemberitahuan lengkap](LICENSES/README.md).

Independen dari NVIDIA Corporation, TechPowerUp dan keylase; tidak disponsori atau didukung secara resmi oleh mereka. Nama produk tetap menjadi merek dagang pemiliknya.
