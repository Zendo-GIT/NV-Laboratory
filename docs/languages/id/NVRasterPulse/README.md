<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · **Bahasa Indonesia** · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Batas FPS per aplikasi melalui RivaTuner Statistics Server.**

> **Instal RTSS terlebih dahulu.** NVRasterPulse memerlukan [RivaTuner Statistics Server (RTSS), diunduh dari Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS harus dijalankan untuk menerapkan batasan. Tidak ada penginstal RTSS, hook DLL, atau SDK yang disertakan.

[Unduh 0.1 & status](../docs/downloads.md#nvrasterpulse) · [Instalasi](#installation) · [Bagaimana batasan bekerja](#usage) · [Lisensi](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Ikhtisar dan tujuan

NVRasterPulse adalah antarmuka Windows yang ringkas untuk mengelola batas bingkai RTSS berdasarkan nama yang dapat dieksekusi. RTSS melakukan pembatasan. NVRasterPulse mengelola nilai profil yang sesuai, permintaan pencadangan dan muat ulang, dengan akses baki dan pilihan tetap.

Itu ada untuk membuat batas tepat per game lebih mudah diedit tanpa mengganti seluruh profil RTSS atau mengganggu pengaturan overlaynya. Kandidat **0.1** saat ini adalah build 9 September 2026 dengan pemeriksaan instalasi RTSS yang diperlukan.

<a id="features"></a>
## Fitur

- Pilih aplikasi yang sedang berjalan atau tambahkan aplikasi yang dapat dieksekusi secara manual.
- Simpan batas FPS dari 1 hingga 1000, hingga tiga tempat desimal.
- Pengkodean rasional yang tepat dari nilai yang dimasukkan: 59.94 menjadi 2997/50.
- Konfigurasi Sinkronisasi Tepi Depan (`SyncLimiter=1`) dengan tunggu aktif (`PassiveWait=0`).
- Pembaruan profil per-eksekusi, pencadangan otomatis, dan penulisan atom.
- Penghapusan pengesampingan pembatas sambil tetap mempertahankan konten profil lainnya.
- Deteksi instalasi RTSS, pemilihan jalur manual dan peluncuran/muat ulang secara eksplisit.
- Pengoperasian baki instans tunggal, startup terinstal opsional, 34 bahasa dan empat tema.
- Pisahkan tindakan keluar normal dan **Keluar + RTSS**.

<a id="compatibility"></a>
## Kompatibilitas

| Persyaratan | Detail |
| --- | --- |
| Sistem | Windows 10/11 x64 |
| Waktu proses | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), dipasang secara terpisah jika diperlukan |
| Perangkat lunak yang diperlukan | RTSS dengan `RTSS.exe`, direktori `Profiles` yang cocok dan dukungan profil/muat ulang yang kompatibel |
| GPU | Kompatibilitas RTSS menentukan pembatas; pengelola profil ini tidak memerlukan generasi RTX tertentu |
| Izin | Aplikasi saat ini meminta akses administrator; folder profil RTSS yang dipilih harus dapat diakses |
| Permainan | Tergantung pada dukungan hooking RTSS dan batasan setiap game; tidak ada jaminan anti-cheat |

Tidak ada versi minimum RTSS spesifik yang telah disertifikasi untuk setiap fungsi oleh audit hub ini. Gunakan distribusi resmi saat ini dan laporkan versi persisnya jika kunci profil/muat ulang tidak berfungsi. RTSS yang diinstal tetapi dihentikan lolos pemeriksaan instalasi; itu kemudian harus dimulai untuk pembatasan sebenarnya.

<a id="installation"></a>
## Instalasi

1. **[Unduh dan instal RTSS dari Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Buka [Unduhan NVRasterPulse](../docs/downloads.md#nvrasterpulse) dan periksa ketersediaan Rilis.
3. Unduh `NVRasterPulse-0.1-win-x64-Setup.exe` atau `NVRasterPulse-0.1-win-x64-portable.zip`, ditambah pemberitahuan/checksum.
4. Bandingkan SHA-256. Jalankan Setup atau ekstrak seluruh ZIP portabel ke folder lokal yang dapat ditulis.
5. Buka `NVRasterPulse.exe`. Jika RTSS hilang, gunakan **Unduh RTSS**, instal, lalu **Periksa lagi**, atau pilih `RTSS.exe` secara manual.
6. Mulai RTSS menggunakan pintasan normalnya atau tombol NVRasterPulse RTSS jika dihentikan.

Menonaktifkan pengingat opsional tidak melewatkan pemeriksaan prasyarat. Startup baki Windows yang senyap menunggu hingga jendela utama terbuka sebelum menampilkan pemeriksaan ini. Pengaturan hanya menginstal NVRasterPulse. EXE-nya tidak ditandatangani.

<a id="usage"></a>
## Penggunaan

1. Pilih aplikasi yang ingin dijalankan atau telusuri game EXE-nya.
2. Masukkan batas antara 1 dan 1000 FPS, termasuk nilai pecahan jika diperlukan.
3. Simpan dan periksa hasil yang dilaporkan. NVRasterPulse memperbarui profil RTSS yang dapat dieksekusi dan meminta memuat ulang.
4. Konfirmasikan RTSS sedang berjalan dan verifikasi perilaku dalam game yang dimaksud.

Profil dikunci berdasarkan **nama yang dapat dieksekusi**, seperti `Game.exe.cfg`. Dua folder berbeda yang berisi `Game.exe` berbagi profil RTSS yang sama; menyimpan jalur lengkap tidak menghilangkan tabrakan ini.

Menyimpan menggunakan Front Edge Sync dan menunggu aktif. Tunggu aktif dapat meningkatkan penggunaan CPU. Bidang `LimitTime` alternatif dinetralkan. Komentar yang ada, pengaturan overlay, dan `EnableHooking=0` dipertahankan. Profil Global RTSS tidak diubah.

Gunakan tindakan sampah untuk menghapus penggantian pembatas NVRasterPulse. Itu tidak menghapus seluruh profil RTSS. Batasan yang diwarisi dari RTSS Global atau alat lain mungkin masih berlaku setelahnya.

**Menutup dan keluar:** jendela utama dapat disembunyikan di baki. **Keluar** yang normal membuat RTSS tetap berjalan dan batas yang disimpan tetap utuh. **Quit + RTSS** meminta penutupan normal proses RTSS yang cocok di sesi saat ini, menunggu hingga delapan detik dan tidak mematikannya secara paksa. Batasan yang tersimpan tetap ada dalam kedua kasus tersebut.

Bahasa dan tema dipilih di aplikasi. Memulai saat masuk Windows bersifat opsional dan ditujukan untuk salinan yang diinstal. Tombol informasi menjelaskan tindakan umum.

<a id="screenshots"></a>
## Tangkapan layar

![Pratinjau jendela utama NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

UI 0.1 Prancis yang ada dirender dengan contoh nama yang dapat dieksekusi dan nilai 176 FPS. RTSS ditampilkan berhenti; ini adalah ilustrasi antarmuka, bukan pembatas atau pengukuran latensi yang berjalan. [Asal gambar](../assets/README.md).

<a id="update-and-uninstall"></a>
## Perbarui dan hapus instalan

Keluar dari NVRasterPulse, unduh dan verifikasi versi baru, lalu jalankan Pengaturannya atau ekstrak portabel ke folder baru. Pertahankan pengaturan dan cadangan RTSS. Pembaruan RTSS terpisah dan berasal dari Guru3D.

Untuk menghapus salinan yang diinstal, gunakan Windows **Installed apps**. Untuk portabel, keluar lalu hapus folder hasil ekstraknya saat cadangan Anda aman. Batas RTSS yang disimpan tidak dihapus dengan menghapus instalasi NVRasterPulse: hapus terlebih dahulu pengesampingan pembatas yang dimaksud. RTSS memiliki uninstallernya sendiri.

Negara bagian lokal: `%LOCALAPPDATA%\NVRasterPulse`. Pencadangan RTSS otomatis: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Lokasi `%LOCALAPPDATA%\RTSSProfileBridge` yang lebih lama dapat dibaca untuk migrasi. File-file ini dapat berisi jalur pribadi yang dapat dieksekusi dan tidak boleh diposting secara publik.

<a id="known-limitations"></a>
## Keterbatasan yang diketahui

- RTSS melakukan pembatasan. Nilai yang disimpan atau permintaan muat ulang yang berhasil bukanlah hasil waktu bingkai yang diukur.
- Eksekusi dengan nama yang sama berbagi profil.
- Pembatas global/per game lainnya dapat memengaruhi hasil; menonaktifkan penggantian lokal tidak menghilangkan batasan yang diwariskan.
- Kait RTSS yang sengaja dinonaktifkan tetap dinonaktifkan.
- Penantian aktif memiliki trade-off CPU/daya.
- Tidak ada validasi latensi game universal, anti-cheat, atau end-to-end.
- Mesin pembatas independen eksperimental sebelumnya tidak dikompilasi atau dikirimkan.
- Pencadangan otomatis tidak berarti antarmuka pemulihan pencadangan penuh sekali klik.

<a id="troubleshooting"></a>
## Pemecahan masalah

| Gejala | Tindakan |
| --- | --- |
| Prasyarat RTSS tetap terbuka | Pilih `RTSS.exe` yang sebenarnya dan folder Profil yang cocok, lalu Periksa lagi. |
| Batas disimpan tetapi tidak berpengaruh | Mulai RTSS; verifikasi EXE/profil game yang benar, izin kait, dan pembatas lainnya. |
| Simpan gagal | Periksa izin folder dan pertahankan kesalahan/cadangan yang ditampilkan. |
| Batas tetap ada setelah penghapusan | Periksa RTSS Global dan alat lainnya; tindakan sampah hanya menghapus pengesampingan pembatas lokal. |
| Dua permainan menerima batas yang sama | Periksa apakah nama file yang dapat dieksekusi sama. |
| Keluar + RTSS membiarkan RTSS terbuka | Tutup RTSS secara normal; perintah ini sengaja menghindari penghentian paksa. |

Jika memulihkan cadangan RTSS secara manual, tutup RTSS terlebih dahulu dan pertahankan profil saat ini sebelum menggantinya dengan cadangan yang dimaksudkan. Tindakan ini dapat menimpa pengeditan profil yang tidak terkait; periksa file dan tanggalnya. [Dukungan bersama](../docs/support.md).

<a id="faq"></a>
## Pertanyaan Umum

**Apakah saya memerlukan MSI Afterburner juga?** NVRasterPulse memerlukan RTSS; itu tidak tergantung pada aplikasi Afterburner. Ikuti opsi instalasi distributor RTSS.

**Dapatkah saya menggunakan ini tanpa menjalankan RTSS?** Anda dapat mengelola profil setelah instalasi terdeteksi, namun RTSS harus dijalankan untuk membatasi.

**Apakah berhenti atau mencopot pemasangan akan menghapus batasannya?** Tidak. Hapus penggantian pembatas yang diinginkan secara eksplisit sebelum menghapus NVRasterPulse.

**Apakah ini fork dari RTSS?** Tidak. Ini adalah pengelola profil independen; tidak ada sumber atau executable RTSS yang dimasukkan.

<a id="upstream-modifications-and-credits"></a>
## Hulu, modifikasi dan kredit

Repositori pengembangan berasal dari [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Palet MIT/sumber daya UI-nya dikreditkan. Layanan manajemen profil, pengkodean pecahan, pencadangan, jembatan muat ulang RTSS, perilaku baki, panduan prasyarat, bahasa dan ikon khusus aplikasi dikembangkan/diadaptasi oleh 禅堂 Zendo (RevoluSound Team).

RTSS dikembangkan oleh **Unwinder** dan didistribusikan secara terpisah melalui Guru3D. NVRasterPulse memanggil `UpdateProfiles` dari DLL kait terpasang yang dipilih; tidak ada RTSS SDK atau biner kait yang didistribusikan ulang. Penginstal menggunakan Inno Setup 7.1.0 yang tidak dimodifikasi dengan skrip/terjemahan yang disesuaikan dan bootstrap proyek.

[Asal penuh](../docs/provenance.md) · [Meja pihak ketiga](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Lisensi

Paket ini secara eksplisit mendistribusikan NVRasterPulse di bawah [Lisensi MIT](../../../../NVRasterPulse/LICENSE) yang disediakan, dengan tetap mempertahankan Hak Cipta (c) 2016 Orbmu2k. Sumber aplikasi dikelola secara pribadi; MIT tidak memerlukan publikasi sumber yang dimodifikasi. RTSS dan Windows/.NET tetap berdasarkan ketentuannya masing-masing. [Pemberitahuan lengkap](LICENSES/README.md).

Independen dari NVIDIA Corporation, MSI dan RTSS; tidak disponsori atau didukung secara resmi oleh mereka. Nama produk tetap menjadi merek dagang pemiliknya.
