<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · **Türkçe** · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Kurulum kılavuzu

Yayın durumunu ve tam varlık adlarını kaydeden [İndirilenler](downloads.md) ile başlayın. Bunlar ayrı araçlardır: yalnızca ihtiyacınız olanları yükleyin.

> **NVRasterPulse için profil yöneticisini açmadan önce [Guru3D'den RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)'i yükleyin.**
> Sınırların uygulanması için RTSS'in çalışması gerekir; NV Tools'e dahil değildir.

| Araç | Yüklü sürüm | Taşınabilir sürüm | Ana önkoşul |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | NVPI ZIP'in tamamını çıkarın | NVIDIA sürücüsü ve .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, çalışma zamanı dahil | Kurulum işlemleri için uyumlu orijinal NVIDIA sürücü paketi |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | NVMFG ZIP'in tamamını çıkarın, alt klasörleri koruyun | RTX 40, mevcut DLSS FG, tam sağlayıcı ve .NET Framework 4.8 yardımcıları |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | RP ZIP'in tamamını çıkarın | RTSS ve .NET Framework 4.8 |

<a id="download-verify-install"></a>
## İndirin, doğrulayın, yükleyin

1. Seçilen yayınlanmış Sürümde, adlandırılmış uygulama varlığını indirin, ZIP ve SHA256SUMS.txt bildirimlerini alın.
2. İndirilen gerçek dosya adıyla [SHA-256 örneği](downloads.md#sha-256)'i kullanın.
3. Kurulum için normal yükleyiciyi takip edin. Taşınabilir ZIP için her şeyi yeni bir yerel yazılabilir klasöre çıkarın; ZIP'in içinden çalıştırmayın.
4. Uygulamanın kendi EXE'sini açın. Ekteki lisans/yapılandırma/veri dosyalarını saklayın.
5. Ayarları veya sistem işlemlerini etkinleştirmeden önce bu aracın kullanım talimatlarını okuyun.

Mevcut ikili dosyalar imzasızdır. Eşleşen bir karma, beklenen baytları doğrular; bir güvenlik veya uyumluluk sertifikası değildir. Yalnızca bir uyarıyı bastırmak için Windows güvenlik korumalarını devre dışı bırakmayın.

NVDF'i veya isteğe bağlı NVPI tamamlayıcısını yüklemek, GPU sürücüsünü yüklemekten farklıdır. NVPI tamamlayıcısı mevcut dahili kurulum adını korur. Yükseltilmiş RasterPulse düğmesi, sistem çapında korumalı bir kurulum gerektirir; diğer RP kopyaları kendi kısayollarıyla açılabilir.

NVMFG deneyseldir ve [belgelenmiş NVIDIA SDK lisans rezervi](provenance.md)'e sahiptir. NVIDIA sürücüsü, NGX sağlayıcısı/modeli veya oyun Streamline çalışma zamanı dahil değildir. Seçilen SDK indirmeleri ve oyun güncellemeleri açıkça ayrı işlemlerdir.

<a id="language-and-updates"></a>
## Dil ve güncellemeler

Dokümantasyon için README'nin 34 dil seçicisini kullanın. NVDF, NVMFG ve RP'in kendi 34 dilli kullanıcı arayüzü ayarları vardır; NVPI mevcut dil desteğini koruyor. Bazı kurulumcu teknik dizeleri İngilizce'ye dayanmaktadır.

Güncelleme sırasında bir aracın kurulum kimliğini koruyun. Önce onu kapatın ve yedekleri koruyun. NVMFG için etkilenen oyunları kapatın ve bekleyen profil kurtarma sorununu çözün. Taşınabilir güncellemeler için sürümleri birleştirmek yerine yeni bir klasör kullanın.

<a id="removing-a-tool"></a>
## Bir aletin çıkarılması

Bir uygulamanın kaldırılması, ayarlarının otomatik olarak geri alınması anlamına gelmez.

- **NVPI:** Gerekirse kaldırmadan önce amaçlanan profilleri/görüntü ayarlarını geri yükleyin.
- **NVDF:** Gelişmiş/NVENC değişikliklerini geri yüklemek istiyorsanız önce kurtarmayı kullanın. Uninstall grafik sürücüsünü, ayarları ve yedeklemeleri bırakır.
- **NVMFG:** oyunları kapatın, denetleyiciyi devre dışı bırakın/çıkarın, NVIDIA kurtarma işlemini çözün ve kaldırmadan önce istenen oyun SDK yedeklerini geri yükleyin.
- **RP:** öncelikle amaçlanan sınırlayıcı geçersiz kılmalarını kaldırın. Uninstall, kayıtlı RTSS büyük harflerini silmez veya RTSS'i kaldırmaz.

Kesin veri konumları ve sınırlamalar için her bir [proje rehberi](../README.md#projects)'e veya bir kurtarma adımı başarısız olursa [destek](support.md)'e bakın.
