<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · **Türkçe** · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Uyumluluk ve sorun giderme

Bunlar, tüm Windows, GPU, sürücü ve oyun kombinasyonları için bir sertifika matrisi değil, hazırlanmış adaylardır.

| Araç | Windows / çalışma zamanı | Donanım / dış bağımlılık | Dikkat gerektiren işlemler |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Çerçevesi 4.8 | Uyumlu NVIDIA sürücüsü/ekran | Profil yazar ve önizlemeleri görüntüler |
| NVDriverForge 0.1.4 | Windows 10 derlemesi 19041+ / 11 x64; .NET/WPF dahil | Uyumlu NVIDIA sürücü paketi | Yükseltilmiş kurulum, gelişmiş ayarlar, isteğe bağlı NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11x64; .NET/WPF dahil, Framework 4.8 yardımcıları | RTX 40, uygun DLSS FG oyunu ve sabitlenmiş sağlayıcı | Yerel oyun içi yama, küresel profil günlüğü, SDK oyun güncellemeleri |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Çerçevesi 4.8 | RTSS yüklü; kapaklar için koşuyorum | RTSS yürütülebilir dosya başına profil değişiklikleri |

ARM64 paketi hazırlanmamıştır. Ekran/API kullanılabilirliği ve eski Windows sürümleri bireysel özellikleri sınırlayabilir. Hiçbir evrensel minimum NVIDIA veya RTSS sürümü icat edilmemiştir. Tam NVMFG sağlayıcı karması [kaynak](provenance.md)'tedir.

<a id="before-reporting-a-bug"></a>
## Bir hatayı bildirmeden önce

Açtığınız yürütülebilir dosyayı/sürümü tam olarak tanımlayın. Daha önce yüklenmiş bir kopyanın mutlaka yeni indirilen ZIP sürümü olması gerekmez. Çoğaltma adımlarını, beklenen sonucu ve gerçek sonucu kaydedin. Oluşturma/sınırlama sorunları için oyun sürümünü, ekran yenilemeyi, FG/V-Sync/VRR durumunu ve diğer sınırlayıcıları veya katmanları ekleyin.

[hata formu](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml)'i kullanın. Hiçbir zaman özel geliştirme klasörünün tamamını, sürücü arşivini, modeli, oyun DLL'sini, kayıt defteri dökümünü veya incelenmemiş günlük koleksiyonunu eklemeyin.

| Sorun | İlk kontroller |
| --- | --- |
| Yanlış uygulama sürümü | EXE kimliğini onaylayın ve karmayı yayınlayın; değiştirmeden önce eski kopyayı kapatın. |
| Çalışma zamanı/başlatma hatası | Gerekli Framework 4.8'i yükleyin veya sağlanan tüm taşınabilir alt klasörleri saklayın. |
| UAC iptal edildi | Yalnızca amaçlanan işlemi yeniden deneyin; iptal başarılı kurulum değildir. |
| Karma/imza uyuşmazlığı | Bu adayı kullanmayı bırakın ve beklenen resmi baytları edinin. |
| NVPI renk/mod reddedildi | Geri dönün ve gerçek ekran/sürücü tarafından desteklenen bir kombinasyonu kullanın. |
| NVDF yedekleme veya kurtarma hatası | Korunan işi ve RECOVERY.txt'i koruyun; Günlüğü silmeyin veya çakışan yazmaya zorlamayın. |
| NVMFG bekleyen ayarlar | Diğer araçlardaki değişiklikleri koruyarak kurtarma işlemini oyunlar kapalıyken gerçekleştirin. |
| RP başlığının etkisi yoktur | RTSS'i çalıştırın, gerçek oyun EXE'sini tanımlayın, kanca durumunu ve rekabet sınırlarını inceleyin. |
| RP kapağı çıkarıldıktan sonra da varlığını sürdürüyor | RTSS Global'i inceleyin; kaldırma işlemi yalnızca yerel sınırlayıcı geçersiz kılmalarını değiştirir. |

NVDriverForge önizlenebilir bir yerel JSON raporu sunar; NVMFG, Hakkında bölümünde bir tanılama sunar. Filtrelenen bu raporları eksiksiz bir günlük arşivine tercih edin ve paylaşmadan önce inceleyin. NVMFG 0.1.1'te bildirilen restorasyon tıkanıklığının hâlâ belirlenmiş bir nedeni yoktur; günlüğünü koruyun ve mevcut hata kodlarını kaydedin. NVRasterPulse 0.2, FPS'i ölçmeden, eylemler menüsünde yapılandırma tanılama olanağı sunar.

<a id="logs-and-privacy"></a>
## Günlükler ve gizlilik

| Araç | İncelenecek yerel veriler, toptan yükleme değil |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; korumalı işler `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`'i yedekler; EXE'nin yanında `Sessions` |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` onun altında |
| NVPI | Seçtiğiniz dışa aktarımlar ve görüntülenen hata; evrensel günlük yolu icat edilmedi |

Paylaştığınız metinlerden/resimlerden hesap adlarını, ana dizinleri, oyun kütüphanesi yollarını, cihaz tanımlayıcılarını, belirteçleri ve ilgisiz pencereleri kaldırın. Kurtarma için orijinalleri özel olarak saklayın. Kamu Sorunları herkes tarafından görülebilir.

Bir güvenlik açığı, tehlikeli ayrıcalıklı davranış veya istenmeyen yıkıcı işlemler için ayrıntıları herkese açık olarak yayınlamak yerine [SECURITY.md](../SECURITY.md)'i izleyin.

<a id="what-has-been-verified"></a>
## Neler doğrulandı

Hub hazırlığı için statik veri/ZIP/hash/meta veri taramaları ve dokümantasyon kontrolleri gerçekleştirildi. Mevcut özel uygulama yapısı/birim/UI testleri tarihsel ve tarihli kanıtlardır. Bu hazırlık kapsamında hiçbir sürücü kurulumu, ekran değişikliği, canlı RTSS işlemi veya oyun kıyaslaması gerçekleştirilmedi.

"Algılandı", "yazıldı", "yeniden yüklendi", "yetenek mevcut" ve "oyunda ölçüldü" farklı sonuçlardır. Hangisini gözlemlediğinizi bildirin.
