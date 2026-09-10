<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · **Bahasa Indonesia** · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**fork independen dari [NVIDIA Profile Inspector oleh Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), dengan kontrol tampilan tambahan.** Nama proyek sebelumnya: **NVPI Custom**.

[Unduh & rilis status](../docs/downloads.md#nvidia-profile-inspector) · [Instalasi](#installation) · [Hulu dan perubahan](#upstream-and-changes) · [Lisensi](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Ikhtisar

Aplikasi mengedit profil driver NVIDIA, termasuk pengaturan per aplikasi. fork ini juga menambahkan editor **Layar** untuk tampilan Windows yang aktif: resolusi, kecepatan refresh, pengaturan warna keluaran, HDR dan asosiasi profil ICC/WCS yang diinstal.

Itu ada untuk menghadirkan kontrol tampilan terkait ke dalam editor profil dan untuk membuat pratinjau, konfirmasi, dan hasil pemulihan lebih jelas. Itu tidak menetapkan kemampuan perangkat keras baru.

Kandidat pertama adalah **3.0.2.3**, menggunakan build pendamping mandiri yang telah dibersihkan mulai 9 September 2026. Eksekusi yang sudah ada tetap `nvidiaProfileInspector.exe`; penginstal dan beberapa label internal masih bertuliskan `NVPI Custom NV`. Judul publik di atas mengidentifikasi fork tanpa mengubah identitas instalasi atau berpura-pura bahwa itu adalah rilis resmi Orbmu2k.

<a id="features"></a>
## Fitur

- Penjelajahan profil hulu yang ada, asosiasi aplikasi, pengeditan pengaturan, dan impor/ekspor profil.
- Dialog **Layar** untuk tampilan, mode, Hz, RGB/YCbCr, kedalaman warna, rentang, dan kolorimetri.
- Kontrol Windows HDR dan memasang pilihan asosiasi ICC/WCS.
- Pratinjau tampilan 15 detik dengan **Keep** / **Revert** dan pemulihan batas waktu.
- Baca kembali perubahan mode/HDR dan kegagalan restorasi yang dilaporkan.
- Pelaporan terpisah HDR, SDR dengan ACM/WCG dan kedalaman warna sinyal.
- Peluncur NVRasterPulse untuk salinan terpasang terpisah yang memenuhi syarat.

<a id="compatibility"></a>
## Kompatibilitas

| Persyaratan | Detail |
| --- | --- |
| Sistem | Windows 10/11 x64 dengan driver NVIDIA yang kompatibel |
| Waktu proses | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), dipasok oleh Windows atau dipasang secara terpisah |
| Izin | Editor meminta akses administrator ketika dibuka |
| Menampilkan | Mode aktual dan kombinasi warna bergantung pada GPU, driver, layar, kabel, dan API Windows |
| Alat opsional | NVRasterPulse untuk manajemen batas RTSS; baik itu maupun RTSS tidak diperlukan untuk editor Layar |
| Bahasa | Pengaturan: pemilih 34 bahasa. Editor mempertahankan dukungan bahasa yang ada. |

Tidak ada matriks minimum atau dukungan driver universal yang terverifikasi untuk setiap GPU. Pilihan bpc yang tersedia dalam dialog adalah permintaan, bukan kombinasi tersertifikasi. Kontrol HDR modern dan fallback Windows yang lebih lama memiliki kemampuan yang berbeda.

<a id="installation"></a>
## Instalasi

1. Buka [halaman unduhan](../docs/downloads.md#nvidia-profile-inspector) dan periksa status publikasi.
2. Unduh aset Setup atau portabel dan bandingkan SHA-256 dengan manifes Rilis.
3. Untuk Penyiapan, jalankan `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, pilih bahasa dan ikuti penginstal. Itu membuat pintasan dan uninstallernya sendiri.
4. Untuk portabel, ekstrak ZIP lengkap ke folder baru yang dapat ditulisi. Simpan `Reference.xml`, konfigurasi EXE dan semua pemberitahuan di samping file yang dapat dieksekusi.
5. Luncurkan `nvidiaProfileInspector.exe`.

Menginstal editor saja tidak menerapkan profil atau menginstal driver GPU. Pendamping menginstal secara terpisah, tidak mengambil alih asosiasi `.nip` dan tidak mengaktifkan startup saat masuk. Biner yang ada tidak ditandatangani.

<a id="usage"></a>
## Penggunaan

**Revisi penginstal 2** menambahkan pemilih 34 bahasa asli yang sama dengan alat lainnya, dengan navigasi mouse/keyboard, tampilan terang/gelap, dan pembatalan. Pilihannya berlaku untuk pengaturan; itu tidak menerjemahkan editor NVPI. Argumen `/LANG=fr` yang eksplisit atau mode senyap melewati pilihan untuk penelepon yang sudah menyediakan bahasa.

**Profil pengemudi:** pilih profil, ekspor cadangan, lalu edit hanya pengaturan yang diinginkan dan terapkan. Asosiasi aplikasi menentukan game mana yang menerima profil. Nilai yang tersimpan bukanlah bukti bahwa setiap driver atau game menggunakannya.

**Kontrol tampilan:** buka **Layar**, pilih tampilan dan nilai yang diminta, lalu mulai pratinjau. Periksa gambar sebelum memilih **Simpan** dalam 15 detik. Gunakan **Kembalikan**, tutup konfirmasi atau biarkan masa berlakunya habis untuk meminta pemulihan. Baca pesan kegagalan apa pun: panggilan API yang berhasil saja bukanlah bukti pemulihan.

Pilihan ICC mengubah asosiasi profil yang diinstal; itu tidak menghasilkan, mengkalibrasi atau mendistribusikan ulang file ICC. HDR, ACM/WCG, RGB/YCbCr dan bpc menjelaskan berbagai aspek pipeline. Tidak ada saklar ACM independen baru yang disediakan.

**NVRasterPulse:** tombol toolbar menerima instalasi seluruh sistem yang terdaftar secara terpisah di bawah Program Files dengan kepemilikan dan izin yang dilindungi. Salinan portabel atau jalur yang dapat ditulis/ditautkan pengguna mungkin ditolak oleh peluncur yang ditinggikan ini. Dalam hal ini buka NVRasterPulse menggunakan pintasannya sendiri. [Instal RTSS secara terpisah](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) untuk menggunakan NVRasterPulse.

<a id="screenshots"></a>
## Tangkapan layar

![NVPI mengatur revisi 2 pemilih bahasa](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Pemilih pengaturan sebenarnya dalam bahasa Prancis, diambil selama pengujian terisolasi dan kemudian dibatalkan. Ini menunjukkan penginstal; editor mempertahankan antarmuka dan dialog Layarnya.

<a id="update-and-uninstall"></a>
## Perbarui dan hapus instalan

Tutup editor sebelum memperbarui. Simpan profil yang diekspor dan unduh Rilis fork baru; instal dengan identitas pendamping yang sama atau ekstrak file portabel ke folder baru. Jangan gabungkan `Reference.xml` lama dengan executable baru. Penindasan pemeriksaan pembaruan upstream yang dibundel adalah milik fork ini.

Untuk salinan yang diinstal, gunakan Windows **Installed apps** dan uninstallernya. Untuk portabel, tutup dan hapus folder hasil ekstraknya saat ekspor Anda aman. Menghapus editor **tidak** membatalkan pengeditan profil driver, preferensi tampilan, NVRasterPulse atau RTSS. Kembalikan pengaturan yang diinginkan sebelum penghapusan.

<a id="known-limitations"></a>
## Keterbatasan yang diketahui

- Konfirmasi 15 detik bukanlah pengawas untuk setiap kecelakaan pengemudi, pemadaman listrik, atau pematian paksa.
- Beberapa kombinasi warna/kedalaman/penyegaran menghasilkan `NVAPI_NOT_SUPPORTED`.
- Pembacaan kembali perangkat lunak tidak mengukur kedalaman bit panel, akurasi warna, atau latensi.
- Pengaturan layar mempengaruhi tampilan Windows saat ini; dialog ini tidak membuat preset tampilan per game.
- Tidak ada jaminan kinerja, anti-cheat, atau kompatibilitas universal HDR.

<a id="troubleshooting"></a>
## Pemecahan masalah

| Gejala | Tindakan |
| --- | --- |
| Kesalahan runtime saat peluncuran | Periksa pembaruan Windows dan .NET Framework 4.8; gunakan paket lengkap. |
| Mode tampilan yang diminta ditolak | Kembalikan dan uji mode yang ditawarkan oleh Windows/NVIDIA untuk tampilan itu. Baca kesalahan sebenarnya dan hindari perubahan buta yang berulang. |
| HDR atau warna kembali ke keadaan lama | Periksa apakah operasi lain gagal dan memicu pemulihan; membedakan HDR dari ACM. |
| Tombol NVRasterPulse menolak jalur | Luncurkan pintasannya sendiri; tombol ini memerlukan instalasi seluruh sistem yang dilindungi. |
| Perubahan tetap ada setelah uninstall | Memulihkan profil NVIDIA yang diekspor atau pengaturan tampilan Windows yang diinginkan; uninstall bukanlah pengembalian pengaturan. |

Lihat [panduan dukungan bersama](../docs/support.md) sebelum mengirim log.

<a id="faq"></a>
## Pertanyaan Umum

**Apakah ini perangkat lunak NVIDIA resmi atau versi resmi Orbmu2k?** Tidak. Ini adalah fork independen; penulis hulu dan lisensi MIT tetap dikreditkan.

**Apakah NVDriverForge memerlukan editor ini?** Tidak. Prasetel opsional NVDriverForge Custom NV menggunakan integrasinya sendiri. Menginstal editor adalah pilihan tersendiri.

**Apakah RTSS wajib untuk fork ini?** Tidak. RTSS wajib untuk pembatas FPS NVRasterPulse, bukan untuk pengeditan profil atau Layar.

**Di mana sumbernya?** Sumber aplikasi yang dimodifikasi dikelola secara pribadi. Pemberitahuan MIT dan repositori upstream disediakan; MIT tidak memerlukan penerbitan sumber yang dimodifikasi.

<a id="upstream-and-changes"></a>
## Hulu dan perubahan

Hulu: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referensi melakukan `592d962cca8827efe8859461a84267755595064a`. [Unduhan asli](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Diwarisi: editor profil, interop NVAPI, data referensi, sumber daya UI, dan tema. 禅堂 Zendo (RevoluSound Team) menambahkan atau mengadaptasi layanan tampilan, transaksi HDR/ICC, konfirmasi/baca kembali 15 detik, tata letak toolbar, dan perilaku peluncuran RasterPulse. Pendamping yang dibersihkan tidak termasuk tiruan pengembangan/titik masuk pengujian, menggunakan peluncur eksternal yang dilindungi dan menyediakan penginstal terpisah. Paket pengembangan gabungan NVPI/RasterPulse yang lama bukanlah kandidat di hub ini.

[Asal file terperinci](../docs/provenance.md) · [Pemberitahuan fork asli](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Kredit dan lisensi

Hak Cipta (c) 2016 Orbmu2k. [Lisensi MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) yang disertakan dipertahankan. Adaptasi dan pengemasan: 禅堂 Zendo (RevoluSound Team). Pemasang menggunakan Inno Setup; Windows dan .NET Framework tetap bersifat eksternal. [Pemberitahuan lengkap yang berlaku](LICENSES/README.md).

Independen, tidak disponsori oleh, dan tidak didukung secara resmi oleh NVIDIA Corporation. Merek dagang tetap menjadi milik pemiliknya masing-masing.
