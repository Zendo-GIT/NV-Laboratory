<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · **Türkçe** · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Anlaşılır bileşen seçenekleri ve isteğe bağlı ayarlarla bir NVIDIA sürücü kurulumu hazırlayın.**

[0.1.3'i ve durumu indirin](../docs/downloads.md#nvdriverforge) · [Kurulum](#installation) · [Kredi](#credits-and-upstream) · [Lisans](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Genel bakış ve amaç

NVDriverForge, orijinal NVIDIA sürücü paketinde size yol gösterir: sürücüyü seçin, bileşenlerini inceleyin, isteğe bağlı ayarları gözden geçirin ve ardından kurulumu onaylayın. Bu seçimleri anlaşılır kılmak ve kurulum, ayrıcalıklı işlemler ve kurtarma bilgilerini bir arada tutmak için vardır.

Kısmen NVCleanstall'in iş akışından esinlenerek bağımsız olarak geliştirilmiş bir uygulamadır. NVCleanstall'i içermez veya tam özellik eşliği talebinde bulunmaz.

<a id="features"></a>
## Özellikler

- NVIDIA Game Ready / Studio arama ve indirmeler; manuel geri dönüş ile isteğe bağlı düzeltme keşfi.
- Orijinal paketin, karmaların, NVIDIA imzalarının, bildirimlerin ve uyumlu INF girişlerinin analizi.
- Bağımlılıklarla bileşen seçimi ve bilinmeyen bileşenlerin korunması.
- Sürüm 0.1.3, seçilen isteğe bağlı NVIDIA bileşenlerini atlanabilir halde tutar ve yalnızca doğrulanmış denetlenmeyen bileşenleri keşif dışında bırakır. Halihazırda geçerli olan veya uygulanamayan isteğe bağlı çalışma süreleri artık kritik bileşenler olarak zorunlu tutulmuyor.
- Kurulum hatası özetlerini temizleyin ve 34 dilin tamamında ayrıntılı günlüklere erişin.
- Açık kurulum onayı, korumalı aşamalandırma ve mevcut sürücü deposu paketlerinin dışa aktarımı.
- Ön kontrol kontrolleri, günlükler ve çatışmaya duyarlı kurtarma ile isteğe bağlı gelişmiş ayarlar.
- Ayrı bir SILK güç seçimi ve uyumluluk kontrolleri de dahil olmak üzere, adlandırılmış seçenekler ve açıklamalar içeren isteğe bağlı **Custom NV** ön ayarı.
- İsteğe bağlı tam sürüm NVENC yama indirmeleri; kaynak taahhüdü ve hedef baytlar kontrol edilir.
- Profile Inspector fork'in Araçlar ekranından ayrı, isteğe bağlı kurulumu.
- İsteğe bağlı kurulu kullanıcı güncelleme kontrolleri, 34 arayüz dili ve dört tema.

Mevcut gelişmiş seçenekler; MPO, DLSS göstergesi, Ansel, NVIDIA ses uyku, MSI, kesme politikası/önceliği, HDCP, ekran kapsayıcı başlatma ve uygun bir eski telemetri hizmetiyle ilgilidir. Her birinin kendi önkoşulları ve etkileri vardır; bunlar evrensel performans iyileştirmeleri değildir.

<a id="compatibility"></a>
## Uyumluluk

| Gereksinim | Ayrıntılar |
| --- | --- |
| Sistem | Windows 10 derlemesi 19041 veya daha yenisi / Windows 11, x64 |
| GPU/sürücü | Uyumlu NVIDIA paketi ve algılanan donanım; otomatik katalog araması öncelikle bilinen GeForce modellerini kapsar |
| Çalışma zamanı | .NET 8 / WPF 8.0.31 hazırlanan müstakil pakete dahildir |
| Ayrıcalıklar | Normal kullanıcı arayüzü/kullanıcı başına kurulum; sürücü kurulumu ve sistem değişiklikleri yönetici erişimi talep ediyor |
| Ağ | Çevrimiçi NVIDIA arama/indirme işlemleri ve açık yukarı akışlı NVENC istekleri için gereklidir; yerel bir orijinal sürücü seçilebilir |
| Dahil edilen araçlar | Değiştirilmemiş 7-Zip 26.03, çalışma zamanı bildirimleri, isteğe bağlı MIT Profile Inspector tamamlayıcısı |
| İsteğe bağlı tamamlayıcı | Ayrı Profile Inspector fork için .NET Framework 4.8 |

Hiçbir rastgele minimum sürücü sürümü tüm özellikleri kapsamaz. Çoklu GPU araması, algılanan her GPU ile eşleşmelidir. Desteklenmeyen/profesyonel modeller manuel sürücü seçimi gerektirebilir. NVIDIA'in yükleyicisi, nihai donanım/işletim sistemi yetkilisi olmaya devam ediyor.

<a id="installation"></a>
## Kurulum

1. [indirmeler](../docs/downloads.md#nvdriverforge)'i ziyaret edin ve Sürümün yayınlandığını onaylayın.
2. Kurulum için `NVDriverForge-Setup.exe`'i veya taşınabilir kullanım için `NVDriverForge.exe`'i seçin.
3. SHA-256'i Sürümün `SHA256SUMS.txt`'i ile karşılaştırın.
4. Kullanıcı başına kurulum ve standart kaldırıcı için Kurulumu çalıştırın veya taşınabilir EXE'yi yazılabilir bir klasöre yerleştirip açın.

Taşınabilir, çalışma zamanını ve isteğe bağlı yükleyicisini içerir. NVDriverForge'in yüklenmesi, GPU sürücüsünün yüklenmesini sağlamaz. EXE'leri şu anda imzasız.

<a id="usage"></a>
## Kullanım

1. **Sürücü:** NVIDIA'ten indirin veya orijinal bir NVIDIA yükleyici EXE'sini seçin. Analiz bitsin.
2. **Bileşenler:** inceleme açıklamaları ve gerekli bağımlılıklar. Bilinmeyen bileşenler korunur.
3. **İncelemeler:** istenmeyen seçenekleri değiştirmeden bırakın. Herhangi bir şeyi seçmeden önce efektleri ve değiş tokuşları okuyun.
4. **İnceleme:** tam sürücüyü, bileşenleri ve isteğe bağlı işlemleri kontrol edin, ardından kurulumu onaylayın.
5. UAC'i yalnızca seçtiğiniz işlem için kabul edin. Korunan işin kurtarma talimatlarını saklayın.
6. Yeni sürücünün yeniden başlatılması gerekiyorsa bildirilen durumu izleyin. Ertelenen işlemler, yeniden başlatmanın ardından açık bir şekilde devam edilmesini gerektirir.

Custom NV değişmeden başlar. Tek tek adlandırılmış değerleri seçin veya sağlanan ön ayarı ve hariç tutulanları inceleyin. İki bilgilendirici iç alanı bağımsız olarak yazılmamıştır. Ayarlar yalnızca doğrulanmış yeni sürücü iş akışında uygulanır; asla bir önizleme açılarak uygulanmaz. Ayrı NVPI düzenleyicisinin kurulmasına gerek yoktur.

İsteğe bağlı NVENC çalışması, sabitlenmiş bir keylase kaydından uyumlu verileri indirir. İki sürücü DLL'sini değiştirir ve imzalarını geçersiz kılar; Windows, kodlayıcılar, DRM veya hile önleme tarafından reddedilebilir. NVDriverForge'te böyle bir veri veya NVIDIA DLL'i yerleşik değil. [Kaynak ve lisans sınırları](../docs/provenance.md).

Tercihler dili, temayı ve isteğe bağlı yüklü kullanıcı güncelleme kontrollerini kontrol eder. Taşınabilir, yüklü arka plan kontrolü görevini oluşturmaz. Araçlar ve kurtarma, dört kurulum adımından ayrıdır.

<a id="screenshots"></a>
## Ekran görüntüleri

![NVDriverForge sürücü sayfası önizlemesi](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Örnek verilerle mevcut 0.1.2 Fransızca kullanıcı arayüzü oluşturma; arayüz önizlemesi olarak tutuldu. Görüntülenen 699.99 sürücüsü, indirilecek gerçek bir sürüm değil, bir test donanımıdır. [Görüntü kaynağı](../assets/README.md).

<a id="update-and-uninstall"></a>
## Güncelleme ve kaldırma

NVDriverForge'i kapatın, bir sonraki resmi paketi edinin ve karmasını doğrulayın. Yüklü bir güncelleştirme için aynı Kurulum kimliğini kullanın; kapalı bir taşınabilir EXE'yi yenisiyle değiştirin. Ayarları ve korunan işleri koruyun.

Windows'ten Uninstall **Installed apps**. NVIDIA sürücüsünü değil, uygulamayı ve güncelleme görevini kaldırır. Ayarlar, günlükler ve yedeklemeler kalır. İstenirse, uygulamayı kaldırmadan **önce** belgelenen kurtarma akışı yoluyla gelişmiş/NVENC değişikliklerini geri yükleyin. Geri yükleme, başka bir araçtan yapılan çakışan değişiklikleri reddeder.

Yerel veriler `%LOCALAPPDATA%\NVDriverForge` altındadır; korunan işler ve sürücü aktarımları `%PROGRAMDATA%\NVDriverForge\Jobs` kapsamındadır. Taşınabilir kullanım aynı zamanda yerel veriler de oluşturur. Sürücü deposunun dışa aktarımı bir sistem görüntüsü veya tam profil yedeği değildir.

<a id="known-limitations"></a>
## Bilinen sınırlamalar

- Donanım eklemesi yok/INF düzenlemesi yok, yeniden oluşturulmuş NVIDIA imzaları, hile karşıtı uyumlu istifa veya otomatik imzasız uyarı kabulü yok.
- Telemetri/reklamın tamamının kaldırılması, ince paket aktarımı veya önceki sürücüye otomatik tam geri dönüş yoktur.
- Sürücü kurulumu, önyükleme kurtarma ve isteğe bağlı profil yazma işlemleri, hub denetimi tarafından gerçek makinelerde kapsamlı bir şekilde doğrulanmadı.
- Kayıt defterinin geri okunması, gerçek HDCP'in, performansın veya gecikme etkilerinin kanıtı değildir.
- İmza kontrolleri yerel olarak mevcut Windows güvenini kullanır; online iptal işlemi yapılmamaktadır.
- 34 dil mevcut ancak tam anadil/erişilebilirlik testleri henüz tamamlanmadı.

<a id="troubleshooting"></a>
## Sorun giderme

| Belirti | Eylem |
| --- | --- |
| Çevrimiçi katalog kullanılamıyor | [NVIDIA sürücü indirmeleri](https://www.nvidia.com/en-us/drivers/)'ten orijinal bir paket seçin. Komşu bir GPU modelini değiştirmeyin. |
| Düzeltme araması kullanılamıyor | [NVIDIA'in Game Ready sürücü forumu](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/)'i kullanın ve gerçek paketi doğrulayın. |
| NVIDIA kurulumu başarısız oluyor | Arıza özetini okuyun ve ayrıntılı günlükleri açın. Halihazırda geçerli olan veya uygulanamayan isteğe bağlı bileşenler, 0.1.3'te atlanabilir durumda kalır. Başarısız kurulumlar, isteğe bağlı ayarlamaları veya başarı/yeniden başlatma akışını tetiklemez. |
| İmza/karma/yedekleme hatası | Bu kurulumu durdurun ve hatayı koruyun; Bozulmuşsa orijinal paketi tekrar edinin. |
| Seçenek kullanılamıyor | Donanımını, bileşenini veya hedef sürücüsünün nedenini okuyun; değişmeden saklayın. |
| Yeniden başlat veya iş hâlâ beklemede | İşin kurtarma talimatlarını ve açık özgeçmişini kullanın; günlüğünü silmeyin. |
| Çatışmayı geri yükle | Başka bir durum, kaydedilen işlemden farklıdır. Onu koruyun ve geri yüklemeye zorlamak yerine yardım isteyin. |

Raporlar için seçilen araç sürümünü, Windows, GPU'i, sürücüyü ve tekrarlanabilir adımları ekleyin; Günlüklerden yolları ve kişisel ayrıntıları çıkarın. [Destek](../docs/support.md).

<a id="faq"></a>
## SSS

**Kurulum bir grafik sürücüsü yüklüyor mu?** Hayır. Bu, uygulamanın ayrı olarak analiz edilmesini, incelenmesini, onaylanmasını ve yükseltilmiş kurulum sürecini gerektirir.

**NVCleanstall veya NVPI'e ihtiyacım var mı?** Hayır. NVCleanstall yalnızca ilham kaynağıdır. Profile Inspector tamamlayıcısı bağımsız, isteğe bağlı bir düzenleyicidir.

**Her NVIDIA sürücüsünü daha küçük veya daha hızlı hale getiriyor mu?** Hayır. Nelerin değişebileceğini seçilen bileşenler ve önkoşullar belirler; ölçülmüş bir kazanç vaat edilmez.

**Kaynaklar nerede?** Uygulamaya özel kaynak ve özel testler ayrı ayrı tutulur. Bu merkez, atıf/lisanslama için gerekli belgeleri, ikili dosyaları ve üçüncü taraf kaynak bağlantılarını sağlar.

<a id="credits-and-upstream"></a>
## Krediler ve yukarı akış

Orijinal uygulama, iş akışı, işlemler, yerelleştirme, önyükleme ve uyarlamalar: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): iş akışı ilhamı; kaynak veya içe aktarılan ikili kod yok.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT temaları, genişletilmiş NVAPI arayüz referansı ve ayrı olarak paketlenmiş fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): değiştirilmemiş çıkarma araçları.
- [Microsoft .NET](https://github.com/dotnet/runtime) ve [WPF](https://github.com/dotnet/wpf): paket çalışma zamanı.
- [Inno Setup](https://jrsoftware.org/isinfo.php): orijinal yükleyici motoru ve itibarlı çeviriler.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): harici isteğe bağlı NVENC veri kaynağı; yeniden dağıtım lisansı oluşturulmadı.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): harici sürücü indirmeleri ve yüklü NVAPI/NVML kitaplıkları.

[Tam bileşen tablosu](../THIRD_PARTY_NOTICES.md) · [Değişiklikler ve köken](../docs/provenance.md)

<a id="license"></a>
## Lisans

[Mevcut ikili dağıtım izni](../../../../NVDriverForge/LICENSE), değiştirilmemiş resmi yürütülebilir dosyaların bildirimleriyle birlikte kullanılmasına ve paylaşılmasına izin verir. Uygulamaya özel kaynak hakları saklıdır. Ayrı üçüncü taraf lisansları tarafından verilen hakları kısıtlamaz. [Tam bildirimler](LICENSES/README.md).

NVIDIA Corporation, TechPowerUp ve keylase'ten bağımsız; onlar tarafından desteklenmiyor veya resmi olarak onaylanmıyor. Ürün adları sahiplerinin ticari markaları olmaya devam etmektedir.
