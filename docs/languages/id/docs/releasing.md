<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · **Bahasa Indonesia** · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Terjemahan dengan bantuan mesin dari bahasa Inggris. Nama teknis, perintah, URL, dan teks hukum asli dipertahankan. Ulasan penutur asli diterima; lihat referensi bahasa Inggris jika kata-katanya tidak jelas.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Penerbitan dan rilis

Repositori publiknya adalah **Zendo-GIT/NV-Laboratory**. Perubahan dokumentasi ditinjau, diterapkan, dan didorong oleh pengelola dengan **GitHub Desktop**. Komit lokal tidak mengunggah file. Paket biner adalah aset Rilis GitHub yang terpisah; mereka tidak pernah termasuk dalam daftar perubahan Git.

<a id="documentation-updates"></a>
## Pembaruan dokumentasi

1. Buka folder **NV-Laboratorium** di GitHub Desktop.
2. Tinjau dokumentasi, pemberitahuan, gambar, metadata JSON, dan validator dokumentasi.
3. Jalankan `python tools/validate_repository.py` dari folder itu.
4. Terapkan perubahan yang telah ditinjau, lalu gunakan **Push origin**. Periksa hasil Tindakan.
5. Simpan identitas penulis publik **禅堂 Zendo (RevoluSound Team)** dan alamat GitHub `noreply` akun.

Jangan pernah memilih ruang kerja pengembangan induk, direktori audit pribadi, atau direktori lampiran biner. [Komit privasi email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Rilis aplikasi independen

| Alat | Menandai | Kebijakan versi |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Versi aplikasi empat bagian yang ada; setup revisi 2 memiliki nama file sendiri |
| NVDriverForge | nvdriverforge-v0.1.3 | Skema 0.x yang ada; pembaruan berversi mempertahankan paket sebelumnya |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Kandidat UI2 diidentifikasi dengan hash yang tepat tanpa membuat versi aplikasi baru |
| NVRasterPulse | nvrasterpulse-v0.1 | Versi dua bagian yang ada |

Pengelola dapat mempublikasikan secara langsung atau memberi wewenang kepada asisten untuk mempublikasikan aset yang diaudit. Publikasi bersifat eksplisit; tidak ada alur kerja yang membuat Rilis pada setiap penerapan.

1. Tinjau laporan prapublikasi saat ini, sumber biner, lisensi, dan nilai SHA-256.
2. Buat draf untuk tag alat, dengan menargetkan penerapan hub yang ditinjau. Sertakan catatan rilis khusus versi yang telah disiapkan.
3. Lampirkan hanya Setup/aset portabel versi tersebut, `Licenses-and-Credits.zip` dan `SHA256SUMS.txt`.
4. Periksa kompatibilitas, instalasi, ketergantungan, perubahan dan batasan yang diketahui. Pertahankan RTSS menonjol untuk NVRasterPulse.
5. Publikasikan, verifikasi URL aset publik, ukuran dan hash, dan catat tanggal publikasi sebenarnya di `docs/releases.json`.
6. Perbarui halaman unduhan dan terjemahannya, lalu komit/dorong perubahannya di GitHub Desktop.

Tautan tag per proyek menghindari pengiriman pengguna ke alat lain melalui tautan `releases/latest` bersama. Arsip otomatis **Source code** GitHub berisi hub dokumentasi ini. Sumber aplikasi tetap bersifat pribadi. Pemberitahuan komponen asli tetap utuh, dan rilis tidak menyelesaikan cadangan NVIDIA SDK yang didokumentasikan NVMFG.

<a id="integrity-and-storage"></a>
## Integritas dan penyimpanan

Jangan pernah mengganti byte biner yang dipublikasikan secara diam-diam. Gunakan versi eksplisit baru atau revisi penginstal dengan hash baru. Sidecars hukum melengkapi pemberitahuan yang tertanam. NVDriverForge 0.1.3 portabel berukuran 141.760.351 byte, di atas batas file Git GitHub biasa yaitu 100 MiB. Rilis lampiran menghindari penempatan biner atau Git LFS di hub ini. [Panduan file besar GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Pelaporan kerentanan pribadi harus diaktifkan di pengaturan keamanan repositori. Verifikasi ketersediaannya sebelum mengarahkan laporan sensitif ke sana; [SECURITY.md](../SECURITY.md) menyediakan cadangan yang tidak memaparkan rincian kerentanan.

[Unduh katalog](downloads.md) · [Dokumentasi rilis GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
