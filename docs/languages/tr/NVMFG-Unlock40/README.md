<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · **Türkçe** · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**GeForce RTX 40 için merkezi denetleyici ve oyun başına seçeneklerle deneysel NVIDIA Multi Frame Generation.**

[0.1.1'i ve durumu indirin](../docs/downloads.md#nvmfg-unlock40) · [Kurulum](#installation) · [Yukarı akış](#upstream-and-modifications) · [Lisanslar](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Genel bakış ve amaç

NVMFG Unlock40, 禅堂 Zendo (RevoluSound Team) tarafından bağımsız olarak geliştirilmiş bir uygulamadır. Windows denetleyiciyi, yerel katmanı, profil yardımcısını ve oyun/Streamline SDK yönetimini birleştirir. Zaten NVIDIA DLSS Frame Generation ve uyumlu NVIDIA çalışma zamanlarını entegre eden oyunları hedefler.

Çalışmayı karşılaştırmak ve iyileştirmek için [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock)'e danışıldı. Geçerli yerel katman, aşağıda ayrı ayrı belirtilen, paylaşılan ve uyarlanmış bileşenleri içerir. Bu referans, NVMFG uygulamasının tamamını söz konusu projenin fork'i yapmaz.

Deneysel MFG davranışını merkezi olarak koordine etmek, oyuna özel seçenekleri hatırlamak ve çalışma zamanı güncellemelerini ve yedeklemelerini görünür tutmak için mevcuttur. DLSS Frame Generation'i her oyuna eklemez veya rastgele bir FSR uygulamasını dönüştürmez.

Hazırlanan aday, dahili olarak UI2 olarak kaydedilen SDK listesi görsel düzeltmesini de içeren **0.1.1**'tir. Genel sürüm 0.1.1 olarak kalır; tam karmaları bu adayı eski yerel yapılardan ayırıyor.

<a id="features"></a>
## Özellikler

- Merkezi etkinleştirme/devre dışı bırakma kontrolü ve isteğe bağlı Windows tepsi başlatma.
- Dynamic MFG arasında oyun başına seçim, oyunun ayarı ve desteklenen sabit çarpanlar.
- Gözlemlenen V-Sync açık/kapalı durumları için ayrı hatırlanan seçenekler.
- Dynamic, NVIDIA'in modunu kullanır; V-Sync kapalıyken ayrı bir oyun içi/sabit seçenekle askıya alınır.
- Oyun menüsü rehberliği ve kalıcı hariç tutmalar; DLSS FG'siz oyunlar kontrolde kalır.
- Oyun dosyalarını silmeden oyun keşfi, ana klasör seçimi, arama, gruplama ve kaldırma.
- Streamline SDK indirme/içe aktarma, doğrulanmış yerel önbellek, açık seçim, oyun başına yedekleme ve geri yükleme.
- Yerel sağlayıcı doğrulaması, oturum başına teşhis, küresel profil günlüğü ve çatışmaya duyarlı kurtarma.
- 34 arayüz dili ve dört tema.

Oyunda FG'yi kapatmak onu kapalı tutar. 2x'ten 6x'e kadar olan sabit seçimler oyuna/menüye/çalışma zamanına bağlıdır; her kombinasyonun işe yarayacağının garantisi değiller. Denetleyici V-Sync'i gözlemler ve kullanıcı için V-Sync veya VRR'i ayarlamaz.

<a id="compatibility"></a>
## Uyumluluk

| Gereksinim | Ayrıntılar |
| --- | --- |
| Sistem | Windows 10/11 x64 |
| GPU | GeForce RTX 40 hedef; evrensel GPU uyumluluk iddiası yok |
| Oyun | Mevcut NVIDIA DLSS Frame Generation entegrasyonu ve desteklenen çalışma zamanı; Hile karşıtı uyumluluk sertifikası yok |
| sağlayıcı | Aday, [kaynak](../docs/provenance.md)'te belgelenen SHA-256 sağlayıcısına sabitlenir; bilinmeyen karmalar reddedildi |
| Çalışma zamanı | Uygulama/aracı için birlikte verilen .NET 8/WPF 8.0.30; Profil yardımcıları için .NET Framework 4.8 |
| İzinler | Denetleyici/profil işlemleri için yönetici erişimi |
| Ağ | Seçilen resmi SDK indirmeleri için gereklidir; içe aktarılan uyumlu SDKs yerel olarak önbelleğe alınabilir |
| Harici ikili dosyalar | NVIDIA sürücüsü, NGX sağlayıcısı/modelleri ve Streamline oyun çalışma süreleri paket halinde değildir |

Sürüm etiketi tek başına yeterli değildir: sürücü, sağlayıcı karması, oyun entegrasyonu ve gerçek yüklü modüller önemlidir. Korunan veya uyumsuz işlemler eklenmeyi reddedebilir. Uygulama hile karşıtı korumalardan kaçınmak için tasarlanmamıştır.

<a id="installation"></a>
## Kurulum

1. [aday durumu ve lisans notu](../docs/downloads.md#nvmfg-unlock40)'i okuyun.
2. Sürümü mevcut olduğunda `NVMFGUnlock40-0.1.1-Setup-x64.exe` veya `NVMFGUnlock40-0.1.1-Portable-x64.zip`'i indirin.
3. SHA-256'i kontrol edin ve beraberindeki bildirimleri saklayın. Windows zaten sağlamıyorsa .NET Framework 4.8'i yükleyin.
4. Kurulumu çalıştırın veya **tamamen** taşınabilir ZIP'i yazılabilir bir yerel klasöre çıkarın.
5. `NVMFGUnlock40.exe`'i başlatın; `agent`, `driver`, `engine` ve `Licenses`'i sağlanan düzende tutun.

`driver` adlı klasör, çekirdek sürücüsünü değil, kullanıcı alanı yardımcılarını içerir. Uyumluluğu zorlamak için yalnızca ana EXE dosyasını kopyalamayın veya sağlayıcı karmasını değiştirmeyin. Mevcut EXE'ler imzasız.

<a id="usage"></a>
## Kullanım

1. Denetleyici devre dışı bırakılarak başlayın. Bir oyun veya ana klasör ekleyin ve gerçek kurulumları seçin.
2. Her oyunun MFG ayarlarını inceleyin. Menüsünün neler sunduğuna cevap verin; Cevap oyun başına saklanır.
3. Genel olarak Dynamic'i veya oyun içi ayarı seçin, ardından oyun başına uygun seçenekleri gerektiği gibi ayarlayın.
4. Denetleyiciyi yalnızca kullanmayı planladığınızda etkinleştirin. Bir kurtarma günlüğüyle altı genel NVIDIA profil ayarını geçici olarak değiştirebilir.
5. Uygun bir oyun başlatın ve kendi DLSS Frame Generation'ini etkinleştirin. V-Sync-kapalı seçeneği için tüm istekleri takip edin.
6. Yönetilmesini istemediğiniz oyunlar için hariç tutmaları kullanın. Bir oyunun kaldırılması, hariç tutma işlemini kaydeder ve dosyalarını/yedeklerini korur.
7. Tamamlandığında uygulamanın tam kapatma/devre dışı bırakma ve kurtarma akışını kullanın.

Ana pencerenin kapatılması denetleyicinin tepside kalmasına neden olabilir. Zaten oyuna yüklenmiş bir DLL, oyundan çıkana kadar orada kalır; denetleyicinin devre dışı bırakılması, yükün boşaltılacağı garantisi değildir. Bakım veya güncelleme öncesinde etkilenen oyunları kapatın.

**Streamline SDKs:** NVIDIA SDK sayfasında resmi sürümü indirin veya uyumlu bir yerel SDK'i içe aktarın. İçe aktarma, doğrulanmış bir kopyayı saklar; **Use this version** bunu seçer ve **Uninstall** önbelleğe alınan kopyayı kaldırır. Eksik Streamline DLL'leri, gösterilen kaynakla birlikte resmi bir NVIDIA SDK'ten tamamlanabilir. Bu, bir NGX modelini indirmez/değiştirmez. Oyunu kapatın, amaçlanan oyun güncellemesini seçin ve orijinal yedeğini koruyun. Oyun dosyalarını geri döndürmek için önbelleğin Uninstall düğmesini değil, yedekleme geri yüklemesini kullanın.

<a id="screenshots"></a>
## Ekran görüntüleri

![NVMFG SDK listesi önizlemesi](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Mevcut İngilizce 0.1.1 arayüzünün örnek bir SDK envanteriyle oluşturulması. Güncel bir sürüm listesi veya çalışan bir oyunun kanıtı değildir. [Görüntü kaynağı](../assets/README.md).

<a id="update-and-uninstall"></a>
## Güncelleme ve kaldırma

Etkilenen oyunları kapatın. Güncellemeden önce NVMFG'yi devre dışı bırakın/çıkarın ve bekleyen NVIDIA ayarlarının kurtarılmasını çözümleyin. Sonraki Kurulumu mevcut kimlikle yükleyin veya yeni taşınabiliri yeni bir klasöre çıkarın; durumu/yedekleri koruyun.

Kaldırmadan önce uygulama aracılığıyla istediğiniz oyun SDK yedeklemelerini ve NVIDIA ayarlarını geri yükleyin, ardından oyunları kapatın ve denetleyiciden çıkın. Kurulum için Windows **Installed apps** kullanın veya gerekli dosyaları koruduktan sonra kapalı taşınabilir klasörü kaldırın. Kurulumun engelini kaldırmak için etkin bir kurtarma günlüğünü el ile silmeyin.

Yerel oyun çalışma zamanı yedeklemeleri `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`'i kullanır. MFG ayarları/SDK verileri `%LOCALAPPDATA%\RtxMfg`'i kullanır; oturum çıktısı uygulamanın yanında `Sessions` altındadır. Bu dosyalar oyun yollarını içerebilir. Bunları düzeltmeden göndermeyin.

<a id="known-limitations"></a>
## Bilinen sınırlamalar

- Deneysel yerel yamalar çökmelere veya görsel bozulmalara neden olabilir; Geliştirme geçmişine çözülmemiş bir Bodycam çökmesi kaydedildi.
- Kontrollü oluşturucu testleri her oyun, sürücü veya hile karşıtı sertifikasyon değildir.
- Oluşturulan çerçeveler yeni girdi örnekleri oluşturmaz; Bu merkez tarafından ölçülmüş bir gecikme veya performans artışı vaat edilmemektedir.
- Çoklu çerçeve oluşturma araçları/katmanları çakışabilir. Uygulama, her bir birlikte varoluş senaryosunu kanıtlamadan gözlemlenen modülleri rapor eder.
- Uyumluluk bildirimi, tamamen test edilmiş oyunların bir listesi değil, bir tespit yardımcısıdır.
- NVIDIA SDK koşullarının tamamı ve çözümlenmemiş teknik sınırlama kısıtlaması, [kaynak](../docs/provenance.md)'te belgelenmeye devam etmektedir.

<a id="troubleshooting"></a>
## Sorun giderme

| Belirti | Eylem |
| --- | --- |
| Sağlayıcı desteklenmiyor | Orijinal doğrulanmış dosyaları saklayın. Sürücü/sağlayıcı sürümlerini ve hatayı bildirin; karma kontrolünü atlamayın. |
| Oyunda DLSS FG yok | Bu cevabı seçin ve kontrolü oyunu bırakın; bu araç bu entegrasyonu sağlayamaz. |
| Oyun çökmeleri/yapılar | Oyundan çıkın, NVMFG'yi devre dışı bırakın, değiştirilmişse oyunun orijinal çalışma zamanı yedeğini kullanın ve tekrarlanabilir ayrıntıları bildirin. |
| SDK listesi veya indirme kullanılamıyor | Resmi kaynağı yenileyin ve kontrol edin; önbelleğe alınmış/içe aktarılmış bir sürümün yine de doğrulamayı geçmesi gerekir. |
| Bekleyen NVIDIA kurtarma çıkışı/güncellemeyi engelliyor | Kurtarmayı kullanın ve günlüğü koruyun; çatışmaların üzerine körü körüne yazılmamalıdır. |
| Kaldırılan bir oyun yeniden keşfedilmez | Dışlanması kalıcıdır. Tekrar yönetilmesini istediğinizde açıkça ekleyin. |

[Paylaşılan destek kılavuzu](../docs/support.md) bir rapora nelerin dahil edileceğini açıklar.

<a id="faq"></a>
## SSS

**NVIDIA DLL'lerini veya modellerini içeriyor mu?** Sürücü, NGX sağlayıcısı/modeli veya Streamline çalışma zamanı dahil değildir. Açık SDK indirmeleri NVIDIA'ten gelir.

**Dynamic, V-Sync kapalıyken çalışır mı?** Bu durumda askıya alınır. Oyunun ayrı durumu için oyun içi ayarı veya uygun bir sabit çarpanı seçin.

**Bu bir ReShade/OptiScaler/FSR paketi mi?** Hayır. Bunlar, bu üretim paketinin parçası olarak derlenmez veya gönderilmez.

**Değiştirilen kaynaklar halka açık mı?** Hayır. Derlenmiş paketler ve gerekli krediler/lisanslar sağlanmaktadır. Bu, üçüncü tarafların haklarını veya kısıtlamalarını ortadan kaldırmaz.

<a id="upstream-and-modifications"></a>
## Yukarı akış ve değişiklikler

Karşılaştırma referansı ve paylaşılan yerel bileşenler: **RTX40MFG-Unlock, Michael Robles / dashdogy**, referans taahhüdü `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Depo](https://github.com/dashdogy/RTX40MFG-Unlock) · [Orijinal indirmeler](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Kaynak karşılaştırması, paylaşılan yama uygulamasını, sağlayıcı/politika yönetimini, geçici düzeltmeleri ve MinHook tabanlı sapma bileşenlerini tanımlar. MIT ve BSD bildirimleri korunur. Tam karşılaştırma aynı zamanda üretim hedefinin dışındaki dosyaları da içerir.

Masaüstü uygulaması, denetleyici ve SDK yönetimi iş akışı, 禅堂 Zendo (RevoluSound Team) tarafından geliştirilmiştir. Proje çalışması, merkezi yükleme, NGX önyükleme entegrasyonu, doğrulanmış sağlayıcı seçimi, oyun/V-Sync koordinasyonu ve oturum teşhisini içerir. Kaynak kılavuzu bu çalışmayı paylaşılan bileşenlerden ayırır; Tek başına bir dosya karşılaştırması, her iki yazarın da bu fikre ne zaman sahip olduğunu belirlemez.

Profil yardımcısı, MIT NVAPI sarmalayıcısını Orbmu2k'in Profile Inspector'inden uyarlar. [Ayrıntılı kaynak ve bileşen kapsamı](../docs/provenance.md).

<a id="credits-and-license"></a>
## Krediler ve lisans

Michael Robles; Orbmu2k; Tsuda Kageyu ve HDE'ye katkıda bulunanlar; NVIDIA Corporation; Microsoft ve katkıda bulunanlar; Inno Setup yazarları ve çevirmenleri. Uygulama geliştirme, entegrasyonlar ve paketleme: 禅堂 Zendo (RevoluSound Team).

[mevcut derlenmiş paket paylaşım izni](../../../../NVMFG-Unlock40/LICENSE) ve tüm [bileşen lisansları](LICENSES/README.md) korunur. Yukarı akış kodu için MIT izinleri, NVIDIA SDK koşullarından farklıdır. Hiçbir genel lisans bunların yerini almaz.

NVIDIA Corporation'ten bağımsızdır, NVIDIA Corporation tarafından desteklenmez ve resmi olarak onaylanmaz. Referans verilen tüm ticari markalar sahiplerinin mülkiyetinde kalır.
