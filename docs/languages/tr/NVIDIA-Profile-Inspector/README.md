<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · **Türkçe** · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Ek ekran kontrolleriyle [NVIDIA Profile Inspector, Orbmu2k tarafından](https://github.com/Orbmu2k/nvidiaProfileInspector)'in bağımsız bir fork'i.** Eski proje adı: **NVPI Custom**.

[İndirme ve yayınlama durumu](../docs/downloads.md#nvidia-profile-inspector) · [Kurulum](#installation) · [Yukarı akış ve değişiklikler](#upstream-and-changes) · [Lisans](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Genel Bakış

Uygulama, uygulamaya özel ayarlar da dahil olmak üzere NVIDIA sürücü profillerini düzenler. Bu fork ayrıca aktif Windows ekranı için bir **Ekran** düzenleyicisi ekler: çözünürlük, yenileme hızı, çıktı rengi ayarları, HDR ve yüklü ICC/WCS profil ilişkileri.

İlgili ekran kontrollerini profil düzenleyiciye getirmek ve önizleme, onay ve geri yükleme sonuçlarını daha net hale getirmek için mevcuttur. Yeni donanım yetenekleri oluşturmaz.

İlk aday, 9 Eylül 2026'dan itibaren temizlenmiş bağımsız tamamlayıcı yapıyı kullanan **3.0.2.3**'tir. Mevcut yürütülebilir dosyası `nvidiaProfileInspector.exe` olarak kalır; yükleyici ve bazı dahili etiketlerde hâlâ `NVPI Custom NV` yazıyor. Yukarıdaki genel başlık, kurulum kimliğini değiştirmeden veya Orbmu2k'in resmi sürümü olduğunu iddia etmeden fork'i tanımlar.

<a id="features"></a>
## Özellikler

- Mevcut yukarı akış profiline göz atma, uygulama ilişkilendirmeleri, ayar düzenlemeleri ve profil içe/dışa aktarma.
- Ekran, mod, Hz, RGB/YCbCr, renk derinliği, aralık ve renk ölçümü için **Ekran** iletişim kutusu.
- Windows HDR kontrolü ve yüklü ICC/WCS ilişkilendirme seçimi.
- **Tut** / **Geri Döndür** ve zaman aşımı geri yüklemesi ile 15 saniyelik ekran önizlemesi.
- Mod/HDR değişikliklerinin tekrar okunması ve bildirilen geri yükleme hataları.
- HDR, SDR'nin ACM/WCG ve sinyal renk derinliği ile ayrı raporlanması.
- Ayrı olarak yüklenmiş uygun bir kopya için bir NVRasterPulse başlatıcısı.

<a id="compatibility"></a>
## Uyumluluk

| Gereksinim | Ayrıntılar |
| --- | --- |
| Sistem | Uyumlu bir NVIDIA sürücüsü ile Windows 10/11 x64 |
| Çalışma zamanı | [.NET Çerçevesi 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), Windows tarafından sağlanır veya ayrı olarak kurulur |
| İzinler | Düzenleyici açıldığında yönetici erişimi ister |
| Gösterimler | Gerçek modlar ve renk kombinasyonları GPU'e, sürücüye, ekrana, kabloya ve Windows API'lerine bağlıdır |
| İsteğe bağlı araçlar | RTSS limit yönetimi için NVRasterPulse; Ekran düzenleyici için ne buna ne de RTSS'e gerek yoktur |
| Diller | Kurulum: 34 dil seçici. Editör mevcut dil desteğini korur. |

Her GPU için doğrulanmış bir evrensel sürücü minimum veya destek matrisi yoktur. İletişim kutusunun mevcut bpc seçenekleri, sertifikalı kombinasyonlar değil, isteklerdir. Modern HDR kontrolleri ve eski Windows geri dönüşü farklı yeteneklere sahiptir.

<a id="installation"></a>
## Kurulum

1. [indirme sayfası](../docs/downloads.md#nvidia-profile-inspector)'i açın ve yayın durumunu kontrol edin.
2. Kurulumu veya taşınabilir varlığı indirin ve SHA-256'i Sürüm bildirimiyle karşılaştırın.
3. Kurulum için `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`'i çalıştırın, bir dil seçin ve yükleyiciyi takip edin. Kendi kısayolunu ve kaldırıcısını oluşturur.
4. Taşınabilir olması için ZIP'in tamamını yeni bir yazılabilir klasöre çıkarın. `Reference.xml`'i, EXE yapılandırmasını ve yürütülebilir dosyanın yanındaki tüm bildirimleri saklayın.
5. `nvidiaProfileInspector.exe`'i başlatın.

Düzenleyiciyi tek başına yüklemek, bir profilin uygulanmasını veya bir GPU sürücüsünün kurulmasını sağlamaz. Yardımcı program ayrı olarak yüklenir, `.nip` ilişkilerini devralmaz ve oturum açma sırasında başlatmayı etkinleştirmez. Mevcut ikili dosyalar imzasızdır.

<a id="usage"></a>
## Kullanım

**Yükleyici revizyonu 2**, fare/klavye navigasyonu, açık/koyu görünüm ve iptal özellikleriyle diğer araçlarla aynı yerel 34 dil seçiciyi ekler. Seçim kurulum için geçerlidir; NVPI düzenleyicisini çevirmez. Açık bir `/LANG=fr` bağımsız değişkeni veya sessiz modu, halihazırda bir dil sağlayan arayanlar için seçimi atlar.

**Sürücü profilleri:** bir profil seçin, bir yedeği dışa aktarın, ardından yalnızca amaçlanan ayarları düzenleyip uygulayın. Uygulama ilişkilendirmeleri hangi oyunun profil alacağını belirler. Saklanan bir değer, her sürücünün veya oyunun onu kullandığının kanıtı değildir.

**Ekran kontrolleri:** **Ekran**'ı açın, ekranı ve istenen değerleri seçin, ardından önizlemeyi başlatın. 15 saniye içinde **Sakla** seçeneğini seçmeden önce resmi kontrol edin. **Geri Döndür** seçeneğini kullanın, onayı kapatın veya geri yükleme isteğinde bulunmak için süresinin dolmasına izin verin. Herhangi bir hata mesajını okuyun: Başarılı bir API çağrısı tek başına geri yüklemenin kanıtı değildir.

ICC seçimi, yüklü bir profil ilişkisini değiştirir; ICC dosyasını oluşturmaz, kalibre etmez veya yeniden dağıtmaz. HDR, ACM/WCG, RGB/YCbCr ve bpc, üretim hattının farklı yönlerini açıklar. Yeni bağımsız ACM anahtarı sağlanmamıştır.

**NVRasterPulse:** araç çubuğu düğmesi, korumalı mülkiyet ve izinlerle Program Dosyaları altında sistem çapında ayrı olarak kaydedilen kurulumu kabul eder. Taşınabilir bir kopya veya kullanıcı tarafından yazılabilen/bağlantılı bir yol, bu yükseltilmiş başlatıcı tarafından reddedilebilir. Bu durumda NVRasterPulse'i kendi kısayolunu kullanarak açın. NVRasterPulse'i kullanmak için [RTSS'i ayrı olarak yükleyin](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).

<a id="screenshots"></a>
## Ekran görüntüleri

![NVPI kurulum revizyonu 2 dil seçici](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Fransızca dilindeki gerçek kurulum seçici, yalıtılmış bir test sırasında yakalandı ve ardından iptal edildi. Bu yükleyiciyi gösterir; editör arayüzünü ve Ekran iletişim kutusunu korur.

<a id="update-and-uninstall"></a>
## Güncelleme ve kaldırma

Güncellemeden önce düzenleyiciyi kapatın. Dışa aktarılan profilleri saklayın ve yeni fork Sürümünü indirin; aynı tamamlayıcı kimlik üzerinden yükleyin veya taşınabilir dosyaları yeni bir klasöre çıkarın. Eski bir `Reference.xml`'i yeni bir yürütülebilir dosyayla karıştırmayın. Paketlenmiş yukarı akış güncelleme kontrolü engellemesi bu fork'e aittir.

Yüklü bir kopya için Windows **Installed apps** ve kaldırıcısını kullanın. Taşınabilir olarak, dışa aktarımlarınız güvenli olduğunda kapatın ve çıkartılan klasörü kaldırın. Düzenleyicinin kaldırılması sürücü profili düzenlemelerini, ekran tercihlerini, NVRasterPulse veya RTSS'i geri **geri almaz**. Kaldırmadan önce istediğiniz ayarları geri yükleyin.

<a id="known-limitations"></a>
## Bilinen sınırlamalar

- 15 saniyelik onay, her sürücü kazası, güç kaybı veya zorla kapanma için bir bekçi köpeği değildir.
- Bazı renk/derinlik/yenileme birleşimleri `NVAPI_NOT_SUPPORTED` değerini döndürür.
- Yazılım geri okuması panel bit derinliğini, renk doğruluğunu veya gecikmeyi ölçmez.
- Ekran ayarları geçerli Windows ekranını etkiler; bu iletişim kutusu oyun başına ekran ön ayarları oluşturmaz.
- Performans, hile önleme veya evrensel HDR uyumluluk garantisi yoktur.

<a id="troubleshooting"></a>
## Sorun giderme

| Belirti | Eylem |
| --- | --- |
| Başlatma sırasında çalışma zamanı hatası | Windows güncellemelerini ve .NET Framework 4.8'i kontrol edin; paketin tamamını kullanın. |
| İstenen görüntüleme modu reddedildi | Söz konusu ekran için Windows/NVIDIA tarafından sunulan modu geri alın ve test edin. Hatayı tam olarak okuyun ve tekrarlanan kör değişikliklerden kaçının. |
| HDR veya renk eski durumuna döner | Başka bir işlemin başarısız olup olmadığını ve geri yüklemeyi tetikleyip tetiklemediğini kontrol edin; HDR'i ACM'den ayırın. |
| NVRasterPulse düğmesi bir yolu reddediyor | Kendi kısayolunu başlatın; bu düğme sistem çapında korumalı bir kurulum gerektirir. |
| Kaldırma işleminden sonra bir değişiklik kalıyor | Dışa aktarılan NVIDIA profilini veya amaçlanan Windows ekran ayarlarını geri yükleyin; kaldırma, ayarların geri alınması değildir. |

Günlükleri göndermeden önce [paylaşılan destek rehberliği](../docs/support.md)'e bakın.

<a id="faq"></a>
## SSS

**Bu resmi NVIDIA yazılımı mı yoksa Orbmu2k'in resmi yapısı mı?** Hayır. Bağımsız bir fork'tir; yukarı akış yazarı ve MIT lisansı kredili olarak kalır.

**NVDriverForge bu düzenleyiciyi gerektiriyor mu?** Hayır. NVDriverForge'in isteğe bağlı Custom NV ön ayarı kendi entegrasyonunu kullanır. Düzenleyiciyi yüklemek ayrı bir seçimdir.

**Bu fork için RTSS zorunlu mudur?** Hayır. RTSS, NVRasterPulse'in FPS sınırlayıcısı için zorunludur, profil veya Ekran düzenleme için zorunlu değildir.

**Kaynak nerede?** Değiştirilen uygulama kaynağı özel olarak korunur. MIT bildirimi ve yukarı akış deposu sağlanmıştır; MIT, değiştirilmiş kaynağın yayınlanmasını gerektirmez.

<a id="upstream-and-changes"></a>
## Yukarı akış ve değişiklikler

Yukarı akış: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referans taahhüdü `592d962cca8827efe8859461a84267755595064a`. [Orijinal indirmeler](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Devralınan: profil düzenleyici, NVAPI birlikte çalışma, referans verileri, kullanıcı arayüzü kaynakları ve temalar. 禅堂 Zendo (RevoluSound Team) eklendi veya uyarlanmış görüntüleme hizmetleri, HDR/ICC işlemleri, 15 saniyelik onay/geri okuma, araç çubuğu düzeni ve RasterPulse başlatma davranışı. Temizlenen yardımcı, geliştirme taklitlerini/test giriş noktalarını hariç tutar, korumalı bir harici başlatıcı kullanır ve ayrı bir yükleyici sağlar. Eski birleşik NVPI/RasterPulse geliştirme paketi bu merkeze aday değil.

[Ayrıntılı dosya kaynağı](../docs/provenance.md) · [Orijinal fork bildirimi](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Krediler ve lisans

Telif Hakkı (c) 2016 Orbmu2k. Sağlanan [MIT lisansı](../../../../NVIDIA-Profile-Inspector/LICENSE) korunur. Uyarlamalar ve paketleme: 禅堂 Zendo (RevoluSound Team). Yükleyici Inno Setup'i kullanır; Windows ve .NET Framework harici kalır. [Geçerli bildirimlerin tamamı](LICENSES/README.md).

NVIDIA Corporation'ten bağımsızdır, NVIDIA Corporation tarafından desteklenmez ve resmi olarak onaylanmaz. Ticari markalar ilgili sahiplerinde kalır.
