<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · **Bahasa Indonesia** · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Asal, perubahan dan perizinan

Audit ini menjelaskan kandidat yang dipersiapkan pada **09-09-2026**. Sumber aplikasi tetap bersifat pribadi; inventaris publik berisi nama file dan hash, bukan kode sumber. Lihat [pemberitahuan komponen lengkap](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referensi: Orbmu2k/nvidiaProfileInspector melakukan `592d962cca8827efe8859461a84267755595064a`; kandidat versi yang dapat dieksekusi 3.0.2.3. Komit referensi dan versi perakitan fork adalah pengidentifikasi yang berbeda; tidak ada versi rilis upstream yang disimpulkan dari versi fork.

157 file sumber/sumber daya pendamping yang bersih dibandingkan dengan komit tersebut: 2 byte identik, 134 hanya berbeda di akhir baris atau UTF-8 BOM, 11 dimodifikasi, 10 tidak ada di jalur hulu yang dibandingkan. “Ditambahkan” bersifat relatif terhadap jalur tersebut dan bukan merupakan bukti penulis asli.

[Perbandingan file/hash lengkap](../../../provenance/nvpi-source-provenance.json).

| Daerah | Pekerjaan yang diwariskan | Kontribusi Fork |
| --- | --- | --- |
| Editor profil | Model profil, impor/ekspor, asosiasi aplikasi, dan data referensi | Integrasi dengan Layar dan peluncur alat eksternal |
| NVAPI | Interop DRS Orbmu2k | Interop terkait warna/tampilan, pembatasan pemuatan asli produksi, dan penghapusan tiruan |
| Layanan tampilan | API Windows/NVIDIA sebagai antarmuka eksternal | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Sumber daya, palet, dan ikon WPF hulu | Dialog layar, konfirmasi 15 detik, status/baca kembali, dan tata letak toolbar |
| Peluncur | Shell aplikasi yang ada | Pencarian dan peluncuran RasterPulse yang diinstal secara terpisah dan dilindungi |
| Pengemasan | MIT hulu | Bersihkan pendamping mandiri, penginstal/uninstaller terpisah, pemberitahuan yang disimpan |

Peta sumber publik mencakup jalur solusi/sumber daya untuk ketertelusuran; file-file itu tidak didistribusikan sebagai sumber. Tes pengembangan, antarmuka tiruan, dan biner gabungan NVPI/RasterPulse yang lama tidak termasuk.

<a id="nvdriverforge"></a>
## NVDriverForge

Aplikasi C#/.NET 8/WPF independen; alur kerja yang dihadapi pengguna sebagian terinspirasi oleh NVCleanstall. Tidak ada sumber/biner NVCleanstall yang diidentifikasi dalam muatan produksi. Itu tidak direpresentasikan sebagai fork dari aplikasi berpemilik tersebut.

Pekerjaan proyek asli mencakup analisis/pemilihan komponen, pekerjaan pemasangan yang dilindungi, pencadangan dan pemulihan transaksi, pengunduhan katalog NVIDIA, pemeriksaan pembaruan, penjelasan yang dilokalkan, alur kerja lanjutan/NVENC opsional, dan bootstrap penginstal.

Komponen yang diwarisi/diadaptasi: empat palet tema NVPI, referensi antarmuka DRS NVAPI yang diperluas, dan pendamping MIT NVPI opsional secara terpisah. UI pilihan preset Custom NV dan integrasi transaksi yang diizinkan adalah milik NVDriverForge; preset tersebut bukan merupakan rekomendasi resmi NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 dan Inno Setup tetap merupakan komponen eksternal yang tidak dimodifikasi dan digunakan berdasarkan ketentuannya sendiri. Data keylase NVENC tidak tertanam; satu penerapan yang tepat dipilih dan diperiksa ketika pengguna meminta unduhan yang kompatibel. Tidak ada izin redistribusi yang ditetapkan untuk data hulu tersebut.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 dikembangkan secara independen oleh 禅堂 Zendo (RevoluSound Team). Pengelola menggunakan RTX40MFG-Unlock untuk perbandingan dan penyempurnaan. Aplikasi secara keseluruhan tidak disajikan sebagai fork-nya. Perbedaan ini tidak menghapus kredit untuk komponen bersama/diadaptasi di lapisan asli saat ini.

Referensi perbandingan: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, melakukan `4e776d068f91b4a665425542bb005dd57cc3d891`. Pohon mesin asli pribadi berisi 48 file yang dibandingkan: 35 perbedaan format saja, 4 file dimodifikasi dan 9 tidak ada di jalur referensi. [Perbandingan lengkap](../../../provenance/nvmfg-source-provenance.json).

File warisan yang dimodifikasi: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Jalur tambahan mencakup `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` dan lisensi upstream yang dipertahankan.

Unit C++ produksi: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection dan vsync_observer; ditambah perakitan entry_detour dan buffer/hook/trampolin/HDE64 MinHook. Frontend ReShade yang diwarisi, sumber daya shim lama, dan target CMake yang tidak digunakan bukan bagian dari kompilasi produksi ini.

Komponen yang cocok mencakup kebijakan patching/penyedia dan pekerjaan sementara; pemberitahuan hak cipta dan izinnya tetap utuh. Koordinasi pusat NGX/bootstrap/pengontrol, penanganan V-Sync per game, diagnostik sesi, dan alur kerja aplikasi Windows/SDK/cadangan adalah pekerjaan proyek oleh 禅堂 Zendo (RevoluSound Team). Hitungan di atas menjelaskan file, termasuk file pihak ketiga dan file yang tidak digunakan, bukan persentase kepengarangan atau kronologi ide proyek mana pun.

Helper mengadaptasi NvapiDrsWrapper dan NativeArrayHelper NVPI ke dalam rakitan terpisah, dengan logika profil yang dibuat oleh proyek. Jalur tiruan pengembangan lama dikecualikan. Palet keluarga bersama berasal dari NVPI.

Referensi MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; subset kompilasi yang diwarisi tidak memiliki perubahan lokal fungsional dalam perbandingannya. Header integrasi Streamline: 2.12; lisensi header terbuka diverifikasi di v2.12.0. Sumber header NGX: NVIDIA/DLSS melakukan `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Mesin kandidat SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Penyedia yang diperlukan SHA-256 di engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Keluarga penyedia 310.9 yang dilaporkan tidak dapat dipertukarkan dengan hash persis ini. Tidak ada penyedia DLL atau model yang disertakan.

**Poin lisensi yang luar biasa:** lisensi lengkap NVIDIA RTX SDK, versi 14 Maret 2024, berisi batasan bagian 4(d) yang relevan untuk melewati batasan teknis. Audit tidak memberikan izin untuk penggunaan ini. Mempertahankan lisensi mesin MIT, gratis, atau mengikuti mod lain tidak menyelesaikan kondisi terpisah tersebut. Persiapan kandidat bukanlah izin hukum. Pemberitahuan tajuk singkat asli dilengkapi dengan lisensi penuh; teks Windows-1252-nya juga disediakan sebagai UTF-8 yang dapat dibaca, dengan byte asli dipertahankan.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Manajer profil RTSS independen dikembangkan di repositori turunan NVPI. Sumber daya/palet UI MIT yang diwarisi dan asal proyek tetap dikreditkan. Aplikasi produksi secara eksplisit menggunakan lisensi MIT yang disediakan.

Pekerjaan proyek: penguraian/penulisan profil RTSS yang tepat dan pengkodean fraksional, pencadangan, penghapusan override, memuat ulang jembatan, deteksi prasyarat, UI ringkas, siklus hidup baki, kontrol pengaktifan, dan pelokalan. RTSS melakukan pembatasan aktual.

Tidak ada sumber RTSS, hook DLL, SDK atau penginstal yang disertakan. Bridge memanggil ekspor dalam instalasi RTSS yang dipilih pengguna. Tidak ada paket driver NVIDIA, pembatas eksperimental asli, Framepacer, MinHook, ReShade atau runtime DLSS ada dalam paket ini.

<a id="assets-generated-data-and-tools"></a>
## Aset, data dan alat yang dihasilkan

[Kredit aset](../assets/README.md) mengidentifikasi pratinjau antarmuka yang ada dan pemilih pengaturan NVPI. Nilai-nilai fiksi di dalamnya diberi label. Tidak ada aset game/Nexus, profil pribadi, ICC pribadi, logo NVIDIA perusahaan, atau file font yang disalin.

Nama kompatibilitas game yang dihasilkan yang diwarisi di NVMFG adalah alat bantu deteksi, bukan bukti pengujian. Katalog pemasang yang dihasilkan dikreditkan dalam [pemberitahuan penerjemah](../../../../licenses/INSTALLER-TRANSLATORS.md). Catatan pembangunan yang dihasilkan dengan jalur absolut tetap bersifat pribadi.

Alat build pribadi mencakup skrip audit .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup, dan Python. Kompiler, header, test runner, dan aset debugnya tidak didistribusikan. CRT rilis statis tetap berada di bawah ketentuan rantai alat Microsoft yang berlaku.

<a id="scope-of-verification"></a>
## Ruang lingkup verifikasi

Audit lokal menginventarisasi semua file di tiga akar pengembangan dan mengecualikan database objek Git dan target direktori tertaut. Sumber/dokumen aktif dipindai; bangunan bersejarah diinventarisasi dan dikecualikan. ZIP yang dipilih dan muatan saat ini dipindai dan di-hash; bundel .NET didekompresi untuk pemeriksaan tambahan. Audit awal tersebut tidak menjalankan produk, penginstal, game, proses RTSS, atau driver.

Revisi 2 pengaturan NVPI yang lebih baru memperbaiki pemilihan bahasa mandiri menggunakan kontrol Inno dan bootstrap bersama. Perlengkapan pribadi terang/gelap memverifikasi navigasi mouse dan keyboard serta 34 kode bahasa eksplisit. Pemilih pengaturan sebenarnya dibuka pada desktop pribadi yang tidak pernah ditampilkan dan dibatalkan sebelum instalasi. Tujuh file aplikasi dan ZIP portabelnya tidak berubah. NVDriverForge 0.1.3 menyertakan pendamping yang dikoreksi dan masih meneruskan `/LANG`.

NVDriverForge 0.1.3 selesai pada 10-09-2026. Laporan verifikasi pribadinya mencatat 366 pengujian aplikasi, 118 pemeriksaan pendamping, 32 pemeriksaan pengaturan, 156 perbandingan asli, dan 34 kasus penerusan bahasa. Perbaikan pemilihan komponen yang dilindungi diputar ulang terhadap paket driver asli tanpa mengubah muatannya atau menginstal driver. Ini adalah hasil tim produk yang tertanggal, bukan tes yang dijalankan ulang oleh pembaruan dokumentasi ini atau bukti instalasi driver nyata yang berhasil.

Pembaruan hub ini tidak mengubah kode aplikasi fungsional. Pengujian build/unit/UI aplikasi sebelumnya tetap menjadi bukti sejarah yang tertanggal. Ini bukan rekayasa balik penuh dari setiap biner pihak ketiga atau jaminan terhadap setiap kemungkinan pola rahasia.
