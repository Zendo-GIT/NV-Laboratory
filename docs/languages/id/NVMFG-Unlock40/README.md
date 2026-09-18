<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · **Bahasa Indonesia** · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**NVIDIA Multi Frame Generation eksperimental untuk GeForce RTX 40, dengan pengontrol pusat dan pilihan per game.**

[Unduh 0.2.3 & status](../docs/downloads.md#nvmfg-unlock40) · [Instalasi](#installation) · [Hulu](#upstream-and-modifications) · [Lisensi](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Ikhtisar dan tujuan

NVMFG Unlock40 adalah aplikasi yang dikembangkan secara independen oleh 禅堂 Zendo (RevoluSound Team). Ini menggabungkan pengontrol Windows, lapisan asli, pembantu profil, dan manajemen game/Streamline SDK. Ini menargetkan game yang sudah mengintegrasikan NVIDIA DLSS Frame Generation dan runtime NVIDIA yang kompatibel.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) dikonsultasikan untuk membandingkan dan menyempurnakan pekerjaan. Lapisan asli saat ini berisi komponen yang dibagikan dan diadaptasi, yang diberi kredit satu per satu di bawah. Referensi ini tidak menjadikan seluruh aplikasi NVMFG sebagai fork dari proyek tersebut.

Itu ada untuk mengoordinasikan perilaku eksperimental MFG secara terpusat, mengingat pilihan spesifik game, dan menjaga pembaruan runtime dan cadangan tetap terlihat. Itu tidak menambahkan DLSS Frame Generation ke setiap game atau mengonversi implementasi FSR secara sewenang-wenang.

Paket saat ini adalah **0.2.3**. Ia menambahkan perpustakaan permainan yang persisten, informasi aktivitas dan kemampuan, diagnostik lokal, dan koreksi perilaku seleksi/kemajuan. [Unduhan](../docs/downloads.md#nvmfg-unlock40) mengidentifikasi file dan hash yang tepat.

<a id="features"></a>
## Fitur

- Kontrol aktifkan/nonaktifkan pusat dan pengaktifan baki Windows opsional.
- Pilihan per game antara Dynamic MFG, pengaturan game dan pengganda tetap yang didukung.
- Pisahkan pilihan yang diingat untuk status hidup/mati V-Sync yang diamati.
- Dynamic menggunakan mode NVIDIA; itu ditangguhkan ketika V-Sync mati, dengan pilihan dalam game/tetap yang terpisah.
- Panduan menu permainan dan pengecualian terus-menerus; game tanpa DLSS FG tetap memegang kendali.
- Penemuan game, pemilihan folder induk, pencarian, pengelompokan, dan penghapusan tanpa menghapus file game.
- Unduh/impor Streamline SDK, cache lokal terverifikasi, pemilihan eksplisit, pencadangan dan pemulihan per game.
- Verifikasi penyedia asli, diagnostik per sesi, jurnal profil global, dan pemulihan sadar konflik.
- 34 bahasa antarmuka dan empat tema.

Mematikan FG dalam game akan membuatnya tetap mati. Pilihan tetap dari 2x hingga 6x bergantung pada game/menu/runtime; itu bukanlah janji bahwa setiap kombinasi akan berhasil. Pengontrol mengamati V-Sync dan tidak mengatur V-Sync atau VRR untuk pengguna.

<a id="compatibility"></a>
## Kompatibilitas

| Persyaratan | Detail |
| --- | --- |
| Sistem | Windows 10/11 x64 |
| GPU | GeForce RTX 40 sasaran; tidak ada klaim kompatibilitas GPU universal |
| Permainan | Integrasi NVIDIA DLSS Frame Generation yang ada dan runtime yang didukung; tidak ada sertifikasi kompatibilitas anti-cheat |
| Penyedia | Kandidat disematkan ke penyedia SHA-256 yang didokumentasikan dalam [asal](../docs/provenance.md); hash yang tidak diketahui ditolak |
| Waktu proses | Paket .NET 8/WPF 8.0.30 untuk aplikasi/agen; .NET Framework 4.8 untuk pembantu profil |
| Izin | Akses administrator untuk operasi pengontrol/profil |
| Jaringan | Diperlukan untuk unduhan resmi SDK terpilih; SDKs yang kompatibel dan diimpor dapat di-cache secara lokal |
| Biner eksternal | Driver NVIDIA, penyedia/model NGX, dan runtime game Streamline tidak dibundel |

Label versi saja tidak cukup: driver, hash penyedia, integrasi game, dan modul yang dimuat sebenarnya penting. Proses yang dilindungi atau tidak kompatibel dapat menolak lampiran. Aplikasi ini tidak dirancang untuk menghindari perlindungan anti-cheat.

<a id="installation"></a>
## Instalasi

1. Baca [status kandidat dan catatan lisensi](../docs/downloads.md#nvmfg-unlock40).
2. Unduh `NVMFGUnlock40-0.2.3-Setup-x64.exe` atau `NVMFGUnlock40-0.2.3-Portable-x64.zip` saat Rilisnya tersedia.
3. Periksa SHA-256 dan simpan pemberitahuan yang menyertainya. Instal .NET Framework 4.8 jika Windows belum menyediakannya.
4. Jalankan Penyiapan, atau ekstrak ZIP portabel **seluruh** ke folder lokal yang dapat ditulis.
5. Luncurkan `NVMFGUnlock40.exe`; pertahankan `agent`, `driver`, `engine` dan `Licenses` dalam tata letak yang disediakan.

Folder bernama `driver` berisi pembantu ruang pengguna, bukan driver kernel. Jangan hanya menyalin EXE utama atau mengganti hash penyedia untuk memaksakan kompatibilitas. EXE saat ini tidak ditandatangani.

<a id="usage"></a>
## Penggunaan

1. Mulailah dengan pengontrol dinonaktifkan. Tambahkan game atau folder induk dan pilih instalasi sebenarnya.
2. Tinjau pengaturan MFG setiap game. Jawab apa yang ditawarkan menunya; jawabannya disimpan per game.
3. Pilih Dynamic atau pengaturan dalam game secara global, lalu sesuaikan pilihan per game yang memenuhi syarat sesuai kebutuhan.
4. Aktifkan pengontrol hanya jika Anda ingin menggunakannya. Ini untuk sementara dapat mengubah enam pengaturan profil NVIDIA global, dengan jurnal pemulihan.
5. Luncurkan game yang memenuhi syarat dan aktifkan DLSS Frame Generation-nya sendiri. Ikuti permintaan apa pun untuk pilihan nonaktif V-Sync.
6. Gunakan pengecualian untuk game yang tidak ingin Anda kelola. Menghapus game mencatat pengecualian dan mempertahankan file/cadangannya.
7. Gunakan alur penghentian/penonaktifan dan pemulihan penuh aplikasi setelah selesai.

Menutup jendela utama dapat meninggalkan pengontrol di baki. DLL yang sudah dimuat ke dalam game akan tetap berada di sana hingga game tersebut keluar; menonaktifkan pengontrol bukan merupakan jaminan pembongkaran. Tutup game yang terpengaruh sebelum pemeliharaan atau pembaruan.

**Streamline SDKs:** di halaman NVIDIA SDK, unduh versi resmi atau impor SDK lokal yang kompatibel. Impor menyimpan salinan terverifikasi; **Use this version** memilihnya, dan **Uninstall** menghapus salinan cache tersebut. DLL Streamline yang hilang dapat dilengkapi dari NVIDIA SDK resmi, dengan sumber yang ditunjukkan. Ini tidak mengunduh/mengganti model NGX. Tutup game, pilih pembaruan game yang diinginkan, dan simpan cadangan aslinya. Untuk mengembalikan file game, gunakan pemulihan cadangannya, bukan tombol Uninstall cache.

<a id="library-diagnostics-and-updates"></a>
## Perpustakaan, diagnostik, dan pembaruan

**Perpustakaan persisten:** pilih beberapa folder game, termasuk drive yang berbeda, sebelum memulai satu pemindaian. Kemajuan terlihat dan pembatalan tersedia. Setelah pemindaian pertama, cache lokal memulihkan perpustakaan saat peluncuran tanpa menelusuri setiap folder game. Segarkan untuk menemukan perubahan atau menambahkan folder lain. Operasi pemeliharaan masih memvalidasi ulang file yang terpengaruh; pemantauan cadangan tetap aktif. Cache disimpan di `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Pilihan:** Ctrl+A memilih semua dan Ctrl+D menghapus tab Game atau Cadangan yang aktif. Tidak ada permainan yang dipilih secara otomatis. Pembaruan dan penyegaran aktivitas tidak lagi menghasilkan pilihan bayangan atau penghitungan yang tidak konsisten.

**Aktivitas dan kompatibilitas:** Informasi MFG per game berasal dari observasi NGX tanpa overlay baru. Ini bukan hitungan fisik dari frame yang ditampilkan. Dukungan Dynamic-dengan-V-Sync berasal dari kemampuan runtime; kemampuan yang tidak diketahui tidak disimpulkan dari nomor versi. Aplikasi tidak mengubah V-Sync atau VRR. Dengan V-Sync dinonaktifkan, Dynamic tetap ditangguhkan; pilihan tetap atau yang dikendalikan permainan terpisah.

**Peluncuran berikutnya:** pengecualian sementara melewatkan patching pada peluncuran game berikutnya dan memulihkan pengelolaan normal setelah keluar. Itu tidak dapat menghapus DLL yang sudah dimuat dalam game: tutup dan mulai ulang game itu. Wallpaper Engine dikenali sebagai aplikasi desktop; koreksi ini mempertahankan perlindungan untuk game yang sebenarnya diabaikan.

**Preferensi dan dukungan:** preferensi impor/ekspor memerlukan pengaitan ulang folder game secara manual. Diagnostik lokal di Tentang memfilter informasi pribadi dan melaporkan kode kesalahan NVAPI yang tersedia atau kategori konflik. Tinjau sebelum berbagi; tidak ada yang diunggah secara otomatis.

**Pembaruan aplikasi:** pemeriksaan opsional menampilkan catatan rilis dan menawarkan Penyiapan resmi. Unduhan eksplisit diperiksa berdasarkan ukuran GitHub dan metadata SHA-256; Anda memulai instalasi sendiri. Versi 0.2.3 juga menghapus pesan kemajuan yang telah selesai sambil mempertahankan kesalahan dan hasil yang berarti. Penambahan ini mencakup perubahan sejak 0.1.1 versi publik.

<a id="screenshots"></a>
## Tangkapan layar

![Pratinjau daftar NVMFG SDK](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Antarmuka 0.1.1 bahasa Inggris yang ada dirender dengan contoh inventaris SDK. Ini bukan daftar versi saat ini atau bukti permainan yang sedang berjalan. [Asal gambar](../assets/README.md).

<a id="update-and-uninstall"></a>
## Perbarui dan hapus instalan

Tutup game yang terpengaruh. Nonaktifkan/keluar dari NVMFG dan selesaikan pemulihan pengaturan NVIDIA yang tertunda sebelum memperbarui. Instal Setup berikutnya dengan identitas yang ada, atau ekstrak portable baru ke dalam folder baru; mempertahankan status/cadangan.

Sebelum mencopot pemasangan, pulihkan cadangan SDK game yang diinginkan dan pengaturan NVIDIA melalui aplikasi, lalu tutup game dan keluar dari pengontrol. Gunakan Windows **Installed apps** untuk Penyiapan, atau hapus folder portabel tertutup setelah menyimpan file yang diperlukan. Jangan menghapus jurnal pemulihan aktif secara manual untuk membuka blokir Penyiapan.

Pencadangan runtime game lokal menggunakan `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Pengaturan MFG/data SDK menggunakan `%LOCALAPPDATA%\RtxMfg`; output sesi berada di bawah `Sessions` di samping aplikasi. File-file ini mungkin berisi jalur permainan. Jangan mempostingnya tanpa disunting.

<a id="known-limitations"></a>
## Keterbatasan yang diketahui

- Penyumbatan aktivasi/pemulihan/pencopotan instalasi 0.1.1 yang dilaporkan masih belum tereproduksi dan penyebabnya tidak diketahui. Rilis ini tidak mengklaim dapat memperbaikinya. Setelah kegagalan, simpan jurnal pemulihan dan periksa diagnostik lokal; jangan paksa penghapusan data pemulihan.
- Patch asli eksperimental dapat menyebabkan error atau artefak visual; kerusakan Bodycam yang belum terselesaikan dicatat dalam riwayat pengembangan.
- Tes penyaji terkontrol bukanlah sertifikasi untuk setiap game, driver, atau anti-cheat.
- Bingkai yang dihasilkan tidak membuat sampel masukan baru; tidak ada latensi terukur atau peningkatan kinerja yang dijanjikan oleh hub ini.
- Beberapa alat/overlay pembuatan bingkai mungkin bertentangan. Aplikasi melaporkan modul yang diamati tanpa membuktikan setiap skenario koeksistensi.
- Manifes kompatibilitas adalah alat bantu pendeteksian, bukan daftar game yang telah diuji sepenuhnya.
- Persyaratan NVIDIA SDK lengkap dan batasan batasan teknis yang belum terselesaikan tetap didokumentasikan di [asal](../docs/provenance.md).

<a id="troubleshooting"></a>
## Pemecahan masalah

| Gejala | Tindakan |
| --- | --- |
| Penyedia tidak didukung | Simpan file asli yang terverifikasi. Laporkan versi driver/penyedia dan kesalahannya; jangan melewati pemeriksaan hash. |
| Tidak ada DLSS FG di dalam game | Pilih jawaban itu dan biarkan permainan terkendali; alat ini tidak dapat membuat integrasi itu. |
| Game mogok/artefak | Keluar dari game, nonaktifkan NVMFG, gunakan cadangan runtime asli game jika diubah, dan laporkan detail yang dapat direproduksi. |
| Daftar atau unduhan SDK tidak tersedia | Refresh dan periksa sumber resmi; versi yang di-cache/diimpor masih harus lulus validasi. |
| Pemulihan NVIDIA yang tertunda memblokir keluar/pembaruan | Gunakan pemulihan dan simpan jurnal; konflik tidak boleh ditimpa begitu saja. |
| Game yang dihapus tidak ditemukan kembali | Pengecualian ini bersifat terus-menerus. Tambahkan secara eksplisit bila Anda ingin mengelolanya lagi. |

[Panduan dukungan bersama](../docs/support.md) menjelaskan apa yang harus disertakan dalam laporan.

<a id="faq"></a>
## Pertanyaan Umum

**Apakah ini termasuk DLL atau model NVIDIA?** Tidak ada driver, penyedia/model NGX, atau runtime Streamline yang disertakan. Unduhan SDK eksplisit berasal dari NVIDIA.

**Apakah Dynamic berfungsi dengan V-Sync nonaktif?** Dynamic ditangguhkan dalam kondisi tersebut. Pilih pengaturan dalam game atau pengganda tetap yang memenuhi syarat untuk status terpisah game tersebut.

**Apakah ini paket ReShade/OptiScaler/FSR?** Tidak. Paket tersebut tidak dikompilasi atau dikirimkan sebagai bagian dari paket produksi ini.

**Apakah sumber yang dimodifikasi bersifat publik?** Tidak. Paket yang dikompilasi dan kredit/lisensi yang diperlukan disediakan. Hal ini tidak menghilangkan hak atau batasan pihak ketiga.

<a id="upstream-and-modifications"></a>
## Hulu dan modifikasi

Referensi perbandingan dan komponen asli bersama: **RTX40MFG-Unlock oleh Michael Robles / dashdogy**, referensi komit `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Gudang](https://github.com/dashdogy/RTX40MFG-Unlock) · [Unduhan asli](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Perbandingan sumber mengidentifikasi patching bersama, penanganan penyedia/kebijakan, koreksi sementara, dan komponen jalan memutar berbasis MinHook. Pemberitahuan MIT dan BSD mereka dipertahankan. Perbandingan lengkapnya juga mencakup file di luar target produksi.

Aplikasi desktop, pengontrol, dan alur kerja manajemen SDK dikembangkan oleh 禅堂 Zendo (RevoluSound Team). Pekerjaan proyek mencakup pemuatan pusat, integrasi bootstrap NGX, pemilihan penyedia terverifikasi, koordinasi game/V-Sync, dan diagnostik sesi. Panduan asal memisahkan karya tersebut dari komponen bersama; perbandingan file saja tidak menentukan kapan salah satu penulis mempunyai ide tersebut.

Pembantu profil mengadaptasi pembungkus MIT NVAPI dari Profile Inspector Orbmu2k. [Asal rinci dan cakupan komponen](../docs/provenance.md).

<a id="credits-and-license"></a>
## Kredit dan lisensi

Michael Robles; Orbmu2k; Kontributor Tsuda Kageyu dan HDE; NVIDIA Corporation; Microsoft dan kontributor; Inno Setup penulis dan penerjemah. Pengembangan aplikasi, integrasi dan pengemasan: 禅堂 Zendo (RevoluSound Team).

[izin berbagi paket terkompilasi yang ada](../../../../NVMFG-Unlock40/LICENSE) dan semua [lisensi komponen](LICENSES/README.md) dipertahankan. Izin MIT untuk kode upstream berbeda dari persyaratan NVIDIA SDK. Tidak ada lisensi menyeluruh yang dapat menggantikannya.

Independen, tidak disponsori oleh, dan tidak didukung secara resmi oleh NVIDIA Corporation. Semua merek dagang yang direferensikan tetap menjadi milik pemiliknya.
