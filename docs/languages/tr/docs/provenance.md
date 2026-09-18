<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · **Türkçe** · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Kaynak, değişiklikler ve lisanslama

Bu denetim **2026-09-18** tarihinde hazırlanan adayları açıklamaktadır. Uygulama kaynakları gizli kalır; halka açık envanterler kaynak kodunu değil dosya adlarını ve karmaları içerir. Bkz. [tam bileşen bildirimleri](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referans: Orbmu2k/nvidiaProfileInspector `592d962cca8827efe8859461a84267755595064a`'i taahhüt eder; aday yürütülebilir sürüm 3.0.2.3. Referans taahhüdü ve fork'in derleme sürümü farklı tanımlayıcılardır; fork sürümünden herhangi bir yukarı akış sürümü çıkarılmaz.

Temiz yardımcının 157 kaynak/kaynak dosyası bu taahhütle karşılaştırıldı: 2 bayt aynı, 134'ü yalnızca satır sonları veya UTF-8 BOM açısından farklı, 11'i değiştirilmiş, 10'u karşılaştırılan yukarı akış yolunda yok. "Eklendi" bu yolla ilişkilidir ve tek başına orijinal yazarlığın kanıtı değildir.

[Tam dosya/karma karşılaştırması](../../../provenance/nvpi-source-provenance.json).

| Alan | Devralınan çalışma | Fork katkısı |
| --- | --- | --- |
| Profil düzenleyici | Profil modeli, içe/dışa aktarma, uygulama ilişkileri ve referans verileri | Ekran ve harici araç başlatıcıyla entegrasyon |
| NVAPI | Orbmu2k'in DRS birlikte çalışması | Renk/ekranla ilgili birlikte çalışma, üretim yerel yükleme kısıtlamaları ve taklit kaldırma |
| Görüntüleme hizmetleri | Harici arayüzler olarak Windows/NVIDIA API'leri | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| kullanıcı arayüzü | Yukarı akış WPF kaynakları, paletleri ve simgeleri | Ekran diyalogları, 15 saniyelik onay, durum/geri okuma ve araç çubuğu düzeni |
| Başlatıcı | Mevcut uygulama kabuğu | Korumalı, ayrı olarak yüklenmiş RasterPulse arama ve başlatma |
| Ambalaj | MIT yukarı akış | Temiz bağımsız yardımcı, ayrı yükleyici/kaldırıcı, saklanan bildirimler |

Genel kaynak haritası, izlenebilirlik için çözüm/kaynak yollarını içerir; bu dosyalar kaynak olarak dağıtılmaz. Geliştirme testleri, sahte arayüzler ve eski birleştirilmiş NVPI/RasterPulse ikili dosyası hariçtir.

<a id="nvdriverforge"></a>
## NVDriverForge

Bağımsız C#/.NET 8/WPF uygulaması; kullanıcıya yönelik iş akışı kısmen NVCleanstall'ten ilham almıştır. Üretim verisinde hiçbir NVCleanstall kaynağı/ikili dosyası tanımlanmadı. Söz konusu tescilli uygulamanın fork'i olarak temsil edilmez.

Orijinal proje çalışması; bileşen analizi/seçimi, korumalı yükleme işleri, yedeklemeler ve işlem kurtarma, NVIDIA katalog indirmeleri, güncelleme kontrolleri, yerelleştirilmiş açıklamalar, isteğe bağlı gelişmiş/NVENC iş akışları ve yükleyici önyüklemesini içerir.

Devralınan/uyarlanan bileşenler: dört NVPI tema paleti, genişletilmiş NVAPI DRS arabirimi referansı ve ayrı olarak isteğe bağlı MIT NVPI tamamlayıcısı. Custom NV ön ayarının seçim kullanıcı arayüzü ve izin verilenler listesindeki işlem entegrasyonu NVDriverForge'e aittir; ön ayar resmi bir NVIDIA önerisi değildir.

7-Zip 26.03, .NET/WPF 8.0.31 ve Inno Setup, kendi koşulları altında kullanılan, değiştirilmemiş harici bileşenler olarak kalır. keylase NVENC verileri gömülü değil; Kullanıcı uyumlu bir indirme talebinde bulunduğunda tam bir taahhüt seçilir ve kontrol edilir. Bu yukarı akış verileri için herhangi bir yeniden dağıtım lisansı oluşturulmamıştır.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40, 禅堂 Zendo (RevoluSound Team) tarafından bağımsız olarak geliştirildi. Bakımcı, karşılaştırma ve iyileştirme için RTX40MFG-Unlock'i kullandı. Uygulama bir bütün olarak fork olarak sunulmuyor. Bu ayrım, geçerli yerel katmandaki paylaşılan/uyarlanmış bileşenlere ilişkin kredileri kaldırmaz.

Karşılaştırma referansı: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, `4e776d068f91b4a665425542bb005dd57cc3d891`'i taahhüt edin. Özel yerel motor ağacı 48 adet karşılaştırılan dosya içerir: 35 adet yalnızca biçimlendirme farklılığı, 4 adet değiştirilmiş dosya ve 9 adet referans yolunda eksik. [Tam karşılaştırma](../../../provenance/nvmfg-source-provenance.json).

Değiştirilen devralınan dosyalar: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Ek yollar arasında `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` ve tutulan yukarı akış lisansı bulunur.

Üretim C++ birimleri: yama aracı, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection ve vsync_observer; artı entry_detour düzeneği ve MinHook tampon/kanca/trambolin/HDE64. Devralınan ReShade ön ucu, eski dolgu kaynakları ve kullanılmayan CMake hedefleri bu üretim derlemesinin parçası değildir.

Eşleşen bileşenler yama/sağlayıcı politikasını ve geçici çalışmayı kapsar; telif hakkı ve izin bildirimleri bozulmadan kalır. Merkezi NGX/önyükleme/denetleyici koordinasyonu, oyun başına V-Sync işleme, oturum tanılama ve Windows uygulaması/SDK/yedekleme iş akışı, 禅堂 Zendo (RevoluSound Team)'in proje çalışmasıdır. Yukarıdaki sayımlar, üçüncü taraf ve kullanılmayan dosyalar da dahil olmak üzere dosyaları tanımlar; yazarlık yüzdesini veya her iki projenin fikrinin kronolojisini değil.

Yardımcı, NVPI'in NvapiDrsWrapper ve NativeArrayHelper'lerini proje tarafından yazılan profil mantığıyla ayrı bir montaja uyarlar. Eski geliştirme sahte yolu hariç tutulmuştur. Paylaşılan aile paletleri NVPI'ten kaynaklanır.

MinHook referansı: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; devralınan derlenmiş alt kümenin karşılaştırmada hiçbir işlevsel yerel değişikliği yoktur. Streamline entegrasyon başlıkları: 2.12; açık başlık lisansı v2.12.0'te doğrulandı. NGX başlık kaynağı: NVIDIA/DLSS, `a291cc7d2cc642a51566f3dfd5376f635cd1b284`'i taahhüt eder.

Aday motor SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

engine.json'te gerekli sağlayıcı SHA-256: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Bildirilen bir 310.9 sağlayıcı ailesi, tam olarak bu karma değeriyle değiştirilemez. Hiçbir sağlayıcı DLL'si veya modeli dahil değildir.

**Olağanüstü lisanslama noktası:** NVIDIA RTX SDK lisansının tamamı, 14 Mart 2024 sürümü, teknik sınırlamaların atlanmasına ilişkin bir bölüm 4(d) kısıtlaması içerir. Denetim bu kullanıma izin vermez. MIT motor lisansını muhafaza etmek, ücretsiz olmak veya diğer modları gözlemlemek bu ayrı durumu çözmez. Aday hazırlığı yasal bir izin değildir. Orijinal kısa başlık bildirimi tam lisansla desteklenmiştir; Windows-1252 metni de orijinal baytlar korunarak okunabilir UTF-8 olarak sağlanır.

Yerel karşılaştırma 0.2.3 için yeniden hesaplandı: aynı 48 dosya ve sınıflandırma. Önceki denetimden bu yana, etkinlik/yetenek gözlemleri için `game_selection.cpp`, `game_selection.h` ve `patcher.cpp` değişti. Yeni kitaplık, teşhis, tercih, güncelleme ve seçim iş akışları bakımcı uygulamasına aittir. Bileşen lisansları ve gerekli sağlayıcı karması değişmedi.

<a id="nvrasterpulse"></a>
## NVRasterPulse

NVPI'ten türetilen depoda geliştirilen bağımsız RTSS profil yöneticisi. Devralınan MIT kullanıcı arayüzü kaynakları/paletleri ve proje kaynağı kredili olarak kalır. Üretim uygulaması, sağlanan MIT lisansını açıkça kullanır.

Proje çalışması: hassas RTSS profil ayrıştırma/yazma ve kesirli kodlama, yedeklemeler, geçersiz kılma kaldırma, yeniden yükleme köprüsü, önkoşul algılama, kompakt kullanıcı arayüzü, tepsi yaşam döngüsü, başlatma kontrolleri ve yerelleştirme. RTSS gerçek sınırlamayı gerçekleştirir.

Hiçbir RTSS kaynağı, kanca DLL'si, SDK veya yükleyici paketlenmemiştir. Köprü, mevcut kullanıcı tarafından seçilen RTSS kurulumunda dışa aktarma işlemini çağırır. Bu pakette NVIDIA sürücü paketi, yerel deneysel sınırlayıcı, Framepacer, MinHook, ReShade veya DLSS çalışma zamanı yoktur.

<a id="assets-generated-data-and-tools"></a>
## Varlıklar, oluşturulan veriler ve araçlar

[Varlık kredileri](../assets/README.md), mevcut arayüz önizlemelerini ve NVPI kurulum seçiciyi tanımlar. İçlerindeki kurgusal değerler etiketlenmiştir. Hiçbir oyun/Nexus varlığı, kişisel profil, özel ICC, kurumsal NVIDIA logosu veya yazı tipi dosyası kopyalanmaz.

NVMFG'de devralınan oluşturulan oyun uyumluluğu adları, test kanıtı değil, tespit yardımcısıdır. Oluşturulan yükleyici katalogları [çevirmen bildirimleri](../../../../licenses/INSTALLER-TRANSLATORS.md)'te belirtilir. Mutlak yollara sahip oluşturulan derleme kayıtları özel kalır.

Özel derleme araçları arasında .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup ve Python denetim komut dosyaları bulunur. Derleyicileri, başlıkları, test çalıştırıcıları ve hata ayıklama varlıkları dağıtılmaz. Statik sürüm CRT'si, Microsoft'in geçerli takım zinciri koşulları kapsamında kalır.

<a id="scope-of-verification"></a>
## Doğrulamanın kapsamı

Yerel denetim, Git nesne veritabanlarını ve bağlantılı dizin hedeflerini hariç tutarken üç geliştirme kökündeki tüm dosyaların envanterini çıkardı. Aktif kaynak/belgeler tarandı; tarihi yapıların envanteri çıkarıldı ve hariç tutuldu. Seçilen ZIP'ler ve mevcut veriler tarandı ve hashing uygulandı; .NET paketlerinin sıkıştırması ek inceleme için açıldı. Bu ilk denetimde herhangi bir ürün, yükleyici, oyun, RTSS işlemi veya sürücü çalıştırılmadı.

Daha sonraki NVPI kurulum revizyonu 2, paylaşılan Inno kontrollerini ve önyüklemeyi kullanarak bağımsız dil seçimini düzeltir. Açık/koyu özel donanımlar, fare ve klavye navigasyonunu ve 34 açık dil kodunun tamamını doğruladı. Gerçek kurulum seçici, hiçbir zaman görüntülenmeyen özel bir masaüstünde açıldı ve kurulumdan önce iptal edildi. Yedi uygulama dosyası ve taşınabilir ZIP'i değişmedi. NVDriverForge 0.1.3, düzeltilmiş tamamlayıcıyı içerir ve yine de `/LANG`'i iletir.

NVDriverForge 0.1.3, 2026-09-10'da tamamlandı. Özel doğrulama raporu, 366 uygulama testini, 118 tamamlayıcı kontrolü, 32 kurulum kontrolünü, 156 yerel karşılaştırmayı ve 34 dil iletme durumunu kaydeder. Korumalı bileşen seçimi düzeltmesi, yükü değiştirilmeden veya sürücü yüklenmeden orijinal sürücü paketinde yeniden oynatıldı. Bunlar tarihli ürün ekibi sonuçlarıdır; bu belge güncellemesiyle yeniden yürütülen testler veya başarılı bir gerçek sürücü kurulumunun kanıtı değildir.

Bu hub güncellemesi hiçbir işlevsel uygulama kodunu değiştirmez. Daha önceki uygulama derlemesi/birim/UI testleri, eski tarihsel kanıtlar olmaya devam ediyor. Bu, her üçüncü taraf ikili dosyanın tam tersine mühendisliği veya olası her gizli kalıba karşı bir garanti değildir.

18 Eylül 2026 güncellemesi: NVDriverForge 0.1.4, hazırlık kontrolleri, yerel profil yedekleme, bileşen kılavuzu, tercihler ve kitler, ayrıntılı sonuçlar, yerel raporlama ve uygulama güncellemeleri ekler. NVRasterPulse 0.2, yeni bir sınırlayıcı motor olmadan yapılandırma tanılama, FPS rehberliği, duraklatma/devam ettirme, geri alma, `.nvrp` profilleri ve sık kullanılanlar/gizleme özelliklerini ekler. Bireysel kılavuzlar kullanımı ve sınırları açıklar. Statik hub kontrolleri, 18 Eylül özel raporlarında kaydedilen uygulama testlerinden ayrıdır; bu hub için herhangi bir sürücü kurulumu, gerçek profil içe aktarımı veya gecikme ölçümü gerçekleştirilmedi.
