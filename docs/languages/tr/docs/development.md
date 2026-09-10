<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · **Türkçe** · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Depo mimarisi ve bakımı

NV Laboratory halka açık bir **dokümantasyon ve ikili dağıtım merkezidir**. Uygulama kaynağı içermez. Dört proje ayrı yapı ağaçlarını, versiyonlarını, kimliklerini ve yayın varlıklarını korur. Özel geliştirme geçmişleri bu Git deposuna aktarılmaz.

<a id="layout"></a>
## Düzen

| Konum | Amaç |
| --- | --- |
| README.md / README.fr.md | İngilizce/Fransızca giriş noktaları |
| Dört proje klasörü | Eksiksiz kılavuzlar ve geçerli orijinal bildirimler |
| dokümanlar | İndirmeler, uyumluluk, kaynak, geliştirme ve sürüm prosedürü |
| dokümanlar/releases.json | Denetlenen aday/sürüm meta verileri, boyutları ve karmaları |
| dokümanlar/kaynak | Dosya/karma karşılaştırmaları; uygulama kodu yok |
| lisanslar | Paylaşılan tam üçüncü taraf metinleri ve yükleyici çevirmen kredileri |
| varlıklar | Mevcut incelenen kullanıcı arayüzü önizlemeleri ve bunların kaynağı |
| .github | Formları ve salt okunur belgeleri doğrulamayı düzenleyin |
| araçlar/validate_repository.py | Standart kütüphane yayın sınırı ve bağlantı kontrolleri |

İngilizce varsayılan GitHub README olarak kalır. Mevcut bitişik `.fr.md` bağlantıları geçerli kalır. Ek çeviriler `docs/languages/<code>` kapsamındaki belgeleri yansıtmaktadır; dil seçici, dilleri değiştirirken aynı sayfayı korur. `docs/languages/catalog.json` kataloğu 34 dilin tamamını ve kaynak parmak izlerini kaydeder. GitHub, tarayıcı diline göre BENİOKU'yu otomatik olarak seçmez. [dil dizini ve çeviri politikası](../../README.md)'e bakın.

<a id="application-technologies"></a>
## Uygulama teknolojileri

| programı | Özel teknoloji | Dağıtım |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows birlikte çalışma | Komple taşınabilir klasör ve ayrı Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; yerel C++ önyüklemesi; 7-Zip işlemi | Bağımsız taşınabilir EXE ve Kurulum |
| NVMFG Unlock40 | C#/WPF .NET 8, Çerçeve 4.8 yardımcıları, C++20/MASM/MinHook motoru | Taşınabilir ağaç ve Kurulum |
| NVRasterPulse | C#/WPF Çerçevesi 4.8; RTSS profili/yeniden yükleme entegrasyonu; yerel önyükleme | Taşınabilir ağaç ve Kurulum |

Bu genel ödeme, uygulamaları yeniden oluşturamaz. Otomatik “Source code” arşivleri hub anlık görüntüleridir. Yukarı akış kaynak bağlantıları, özel olarak değiştirilmiş kaynağı tam olarak temsil etmez. Genel CI yalnızca bu depoyu doğrular.

<a id="local-checks"></a>
## Yerel kontroller

Depo kökünden:

```text
python tools/validate_repository.py
```

Python 3.10 veya daha yenisi yeterlidir. Denetim, dosyaları, yerel Markdown bağlantılarını, gerekli bildirimleri/RTSS bağlantılarını, sürüm meta verilerini ve yayın sınırlarını okur. Yazılımı çalıştırmaz, bağımlılıkları yüklemez veya bir ağla bağlantı kurmaz.

GitHub iş akışı aynı kontrolü, push, pull request veya manuel gönderimde salt okunur içerik izniyle çalıştırır. Ödeme, denetlenen bir işleme sabitlenir ve kimlik bilgilerini sürdürmez. Hiçbir sürüm veya dağıtım işi yapılandırılmadı.

<a id="maintain-the-boundary"></a>
## Sınırı koruyun

İngilizce referansı, Fransızca kılavuzları ve etkilenen çevirileri birlikte güncelleyin. Önemli değişiklikleri yalnızca biçimlendirme karşılaştırmalarından ayrı tutun. Gerçek aday karmalarını, yukarı akış taahhüt referanslarını ve lisanslarını kaydedin; Asla bir projenin popülaritesinden lisans çıkarımı yapmayın.

Yeni sürüme sahip Sürüm varlıklarını kullanın ve değiştirilen ikili dosyaları, arşivleri ve yerleşik bildirimleri yeniden denetleyin. Özel yedeklemeleri bu havuzun dışında saklayın. Özel uygulama kaynağını veya yerel derleme klasörlerini içe aktarmak için genel iş akışını kullanmayın.

Özel projede yürütülen işlevsel bir uygulama değişikliğine uygun testler. Sürücü yükleyicilerini yeniden çalıştırmayın veya belge güncellemesi için gerçek profiller yazmayın. [Manuel serbest bırakma prosedürü](releasing.md).
