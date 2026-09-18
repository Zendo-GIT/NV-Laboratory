<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · **Türkçe** · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**FPS, RivaTuner Statistics Server aracılığıyla uygulama başına sınırlar.**

> **Önce RTSS'i yükleyin.** NVRasterPulse, [RivaTuner Statistics Server (RTSS), Guru3D'den indirildi](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)'i gerektirir. Sınırları uygulamak için RTSS çalışıyor olmalıdır. Hiçbir RTSS yükleyicisi, kanca DLL'si veya SDK paketlenmemiştir.

[0.2'i ve durumu indirin](../docs/downloads.md#nvrasterpulse) · [Kurulum](#installation) · [Limitler nasıl çalışır?](#usage) · [Lisans](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Genel bakış ve amaç

NVRasterPulse, RTSS çerçeve sınırlarını yürütülebilir adla yönetmek için kullanılan kompakt bir Windows arabirimidir. RTSS sınırlamayı gerçekleştirir. NVRasterPulse, tepsi erişimi ve kalıcı seçeneklerle ilgili profil değerlerini, yedeklemeleri ve yeniden yükleme isteklerini yönetir.

RTSS profilinin tamamını değiştirmeden veya katman ayarlarını bozmadan oyun başına kesin limitlerin düzenlenmesini kolaylaştırmak için mevcuttur. Sürüm **0.2**, yapılandırma tanılamayı, bir FPS yardımcısını, duraklatmayı, geri almayı ve profil paylaşımını ekler.

<a id="features"></a>
## Özellikler

- Çalışan bir uygulamayı seçin veya yürütülebilir dosyasını manuel olarak ekleyin.
- Üç ondalık basamağa kadar FPS sınırlarını 1'den 1000'e kadar kaydedin.
- Girilen değerlerin tam olarak rasyonel kodlanması: 59.94, 2997/50 olur.
- Etkin bekleme (`PassiveWait=0`) ile Front Edge Sync yapılandırması (`SyncLimiter=1`).
- Yürütülebilir profil güncellemeleri, otomatik yedeklemeler ve atomik yazmalar.
- Diğer profil içeriğini korurken sınırlayıcı geçersiz kılmaların kaldırılması.
- RTSS kurulum tespiti, manuel yol seçimi ve açık başlatma/yeniden yükleme.
- Tek örnekli tepsi işlemi, isteğe bağlı yüklü başlatma, 34 dil ve dört tema.
- Normal çıkış ve **Çık + RTSS** işlemlerini ayırın.

<a id="compatibility"></a>
## Uyumluluk

| Gereksinim | Ayrıntılar |
| --- | --- |
| Sistem | Windows 10/11 x64 |
| Çalışma zamanı | [.NET Çerçevesi 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), gerekirse ayrı olarak kurulur |
| Gerekli yazılım | `RTSS.exe` ile RTSS, eşleşen bir `Profiles` dizini ve uyumlu profil/yeniden yükleme desteği |
| GPU | RTSS uyumluluğu sınırlayıcıyı belirler; bu profil yöneticisi belirli bir RTX nesli gerektirmez |
| İzinler | Mevcut uygulama yönetici erişimi talep ediyor; seçilen RTSS profil klasörüne erişilebilir olmalıdır |
| Oyunlar | RTSS kancalama desteğine ve her oyunun kısıtlamalarına bağlıdır; hile önleme garantisi yok |

Bu merkez denetimi tarafından her işlev için belirli bir RTSS minimum sürümü onaylanmamıştır. Resmi güncel dağıtımı kullanın ve profil anahtarı/yeniden yükleme çalışmıyorsa tam sürümü bildirin. Kurulu ancak durdurulmuş RTSS kurulum denetimini geçer; daha sonra gerçek sınırlama için başlatılmalıdır.

<a id="installation"></a>
## Kurulum

1. **[RTSS'i Guru3D'den indirip yükleyin](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. [NVRasterPulse indirmeleri](../docs/downloads.md#nvrasterpulse)'i açın ve Sürüm kullanılabilirliğini kontrol edin.
3. `NVRasterPulse-0.2-win-x64-Setup.exe` veya `NVRasterPulse-0.2-win-x64-portable.zip`'i ve ayrıca bildirimleri/sağlama toplamlarını indirin.
4. SHA-256'i karşılaştırın. Kurulumu çalıştırın veya taşınabilir ZIP'in tamamını yazılabilir bir yerel klasöre çıkarın.
5. `NVRasterPulse.exe`'i açın. RTSS eksikse **RTSS'i indirin** seçeneğini kullanın, yükleyin, ardından **Tekrar kontrol edin** veya `RTSS.exe`'i manuel olarak seçin.
6. RTSS'i normal kısayolunu veya durdurulmuşsa NVRasterPulse'in RTSS düğmesini kullanarak başlatın.

İsteğe bağlı hatırlatıcının kapatılması önkoşul kontrolünü atlamaz. Sessiz bir Windows tepsi başlatma işlemi, bu kontrolü görüntülemeden önce ana pencere açılana kadar bekler. Kurulum yalnızca NVRasterPulse'i yükler. EXE'leri imzasızdır.

<a id="usage"></a>
## Kullanım

1. Çalıştırılması amaçlanan uygulamayı seçin veya oyunun EXE dosyasına göz atın.
2. Gerekirse kesirli bir değer de dahil olmak üzere 1 ile 1000 FPS arasında bir sınır girin.
3. Bildirilen sonucu kaydedin ve kontrol edin. NVRasterPulse, yürütülebilir dosyanın RTSS profilini günceller ve yeniden yükleme isteğinde bulunur.
4. RTSS'in çalıştığını doğrulayın ve amaçlanan oyundaki davranışı doğrulayın.

Profiller, `Game.exe.cfg` gibi **yürütülebilir dosya adına** göre anahtarlanır. `Game.exe`'i içeren iki farklı klasör aynı RTSS profilini paylaşır; tam yolu saklamak bu çarpışmayı ortadan kaldırmaz.

Kaydetme, Front Edge Sync'i ve etkin beklemeyi kullanır. Etkin bekleme, CPU kullanımını artırabilir. Alternatif `LimitTime` alanları etkisiz hale getirildi. Mevcut yorumlar, yer paylaşımı ayarları ve `EnableHooking=0` korunur. RTSS Genel profili değişmedi.

NVRasterPulse'in sınırlayıcı geçersiz kılmalarını kaldırmak için çöp kutusu eylemini kullanın. RTSS profilinin tamamını silmez. RTSS Global'den veya başka bir araçtan devralınan bir sınır daha sonra da geçerli olabilir.

**Kapatma ve çıkma:** ana pencere tepsiye gizlenebilir. Normal **Çık**, RTSS'i çalışır durumda ve kaydedilen limitleri olduğu gibi bırakır. **Çık + RTSS** geçerli oturumda eşleşen RTSS işleminin normal şekilde kapatılmasını ister, sekiz saniyeye kadar bekler ve onu zorla sonlandırmaz. Her iki durumda da kayıtlı limitler kalır.

Uygulamada dil ve tema seçilir. Windows oturum açma işleminde başlatma isteğe bağlıdır ve yüklü bir kopya için tasarlanmıştır. Bilgi düğmesi ortak eylemleri açıklar.

<a id="diagnostics-and-profile-tools"></a>
## Teşhis ve profil araçları

Ek araçlar için eylemler menüsünü açın. RTSS Global'i, yer paylaşımı ayarlarını ve hariç tutmaları korurlar.

**Teşhis:** yerel/etkili sınırları denetleme, durdurulan RTSS, eksik bir yürütülebilir dosya, algılanan pencere yok, devre dışı bırakılan kancalama, devralma, duraklatılmış sınırlar, rekabet eden ayarlar ve yinelenen yürütülebilir dosya adları. Bu salt okunur denetim, yapılandırmayı açıklar; bir oyunun RTSS'e bağlandığını veya FPS'ini ölçtüğünü kanıtlamaz.

**FPS yardımcısı:** ekranı seçin ve VRR/G-Sync, V-Sync, Reflex ve Frame Generation'i kendiniz bildirin. Yuvarlatılmış yenileme sıklığı Windows'ten gelir. Reflex veya Frame Generation etkinse veya bilinmiyorsa otomatik sınır sunulmaz. V-Sync açık ve Reflex/FG kapalıyken VRR için buluşsal yöntem en az 3 FPS veya yenileme hızının yaklaşık %2'sini çıkarır. Bu ölçülen bir optimum değildir. Önerinin uygulanması taslağı doldurur; **Kaydet** ayrı bir işlem olarak kalır.

**Duraklat ve devam ettir:** seçilen programın sınırını askıya alın, ardından önceki sınırlayıcı alanlarını geri yükleyin. Başka bir araç tarafından yapılan çakışan değişiklikler belirsiz bir özgeçmişi önler. Bir girişin gizlenmesi girişin sınırını duraklatmaz.

**Geri al:** söz konusu program için altı yönetilen sınırlayıcı alanda yapılan son değişikliği geri yükleyin. Bir seviye var; bu, RTSS'in tamamını geri yüklemez. Çakışan dış değişiklikler reddedilir. Dosya yedeklemeleri ayrı kalır.

**Profilleri paylaş:** Seçilen profilleri bir `.nvrp` dosyasına aktarın. İçe aktarma bir önizleme gösterir ve mevcut sınırları varsayılan olarak işaretlenmemiş halde bırakır. Dosya, mutlak yollar veya komut dosyaları olmaksızın yalnızca yürütülebilir adları, sınırları ve durumları içerir. Seçiminizi gözden geçirin ve başvurun. Bir G/Ç hatası bazı profillerin zaten uygulanmış halde kalmasına neden olabilir; sonuç onları tanımlar ve her biri kendi geri alma işlemini sürdürür. Aynı yürütülebilir dosya adları hâlâ aynı RTSS profilini adresliyor.

**Favoriler ve gizli girişler:** Önce yararlı programları sabitleyin, istenmeyen girişleri gizleyin ve bunları özel iletişim kutusunda geri yükleyin. Bu seçimler devam ediyor. Kapalı bir sık ​​kullanılan, çalışan bir uygulama olarak görünmez.

<a id="screenshots"></a>
## Ekran görüntüleri

![NVRasterPulse ana pencere önizlemesi](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Örnek yürütülebilir adlar ve 176 FPS değeriyle mevcut Fransız 0.1 kullanıcı arayüzü oluşturma. RTSS durdurulmuş olarak gösteriliyor; bu bir arayüz çizimidir, çalışan bir sınırlayıcı veya gecikme ölçümü değildir. [Görüntü kaynağı](../assets/README.md).

<a id="update-and-uninstall"></a>
## Güncelleme ve kaldırma

NVRasterPulse'ten çıkın, yeni sürümü indirip doğrulayın, ardından Kurulumu çalıştırın veya taşınabiliri yeni bir klasöre çıkarın. Ayarları ve RTSS yedeklemelerini koruyun. RTSS güncellemeleri ayrıdır ve Guru3D'den gelir.

Yüklü bir kopyayı kaldırmak için Windows **Installed apps** kullanın. Taşınabilir için, yedeklemeleriniz güvende olduğunda çıkın ve çıkarılan klasörü kaldırın. Kaydedilen RTSS sınırları, NVRasterPulse kaldırıldığında kaldırılmaz: önce amaçlanan sınırlayıcı geçersiz kılmalarını kaldırın. RTSS'in kendi kaldırıcısı vardır.

Yerel durum: `%LOCALAPPDATA%\NVRasterPulse`. Otomatik RTSS yedeklemeleri: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Geçiş için daha eski bir `%LOCALAPPDATA%\RTSSProfileBridge` konumu okunabilir. Bu dosyalar kişisel yürütülebilir yollar içerebilir ve herkese açık olarak yayınlanmamalıdır.

<a id="known-limitations"></a>
## Bilinen sınırlamalar

- RTSS sınırlamayı gerçekleştirir. Kaydedilen bir değer veya başarılı bir yeniden yükleme isteği, ölçülen bir kare süresi sonucu değildir.
- Aynı isimli yürütülebilir dosyalar bir profili paylaşır.
- Başka bir genel/oyun başına sınırlayıcı, sonucu etkileyebilir; yerel geçersiz kılmanın devre dışı bırakılması devralınan sınırı kaldırmaz.
- Kasıtlı olarak devre dışı bırakılan bir RTSS kancası devre dışı kalır.
- Aktif beklemede CPU/güç dengesi vardır.
- Evrensel oyun, hile önleme veya uçtan uca gecikme doğrulaması yok.
- Daha önceki deneysel bağımsız sınırlayıcı motor derlenmedi veya gönderilmedi.
- Otomatik yedeklemeler, tek tıklamayla tam yedekleme-geri yükleme arayüzü anlamına gelmez.

<a id="troubleshooting"></a>
## Sorun giderme

| Belirti | Eylem |
| --- | --- |
| RTSS önkoşulu açık kalıyor | Gerçek `RTSS.exe`'i ve eşleşen Profiller klasörünü seçin, ardından tekrar kontrol edin. |
| Sınır kaydedildi ancak etkisi yok | RTSS'i başlatın; Doğru oyun EXE/profilini, kanca izinlerini ve diğer sınırlayıcıları doğrulayın. |
| Kaydetme başarısız oluyor | Klasör izinlerini kontrol edin ve görüntülenen hatayı/yedeği koruyun. |
| Sınır kaldırıldıktan sonra kalır | RTSS Global ve diğer araçları inceleyin; çöp kutusu eylemi yalnızca yerel sınırlayıcı geçersiz kılmalarını kaldırır. |
| İki oyun aynı limiti alıyor | Yürütülebilir dosya adlarının aynı olup olmadığını kontrol edin. |
| Çık + RTSS, RTSS'i açık bırakır | RTSS'i normal şekilde kendiniz kapatın; bu komut kasıtlı olarak zorla sonlandırmayı önler. |

Bir RTSS yedeklemesini manuel olarak geri yüklüyorsanız, önce RTSS'i kapatın ve amaçlanan yedeklemeyle değiştirmeden önce mevcut profili koruyun. Bu, ilgisiz profil düzenlemelerinin üzerine yazılabilir; dosyayı ve tarihi inceleyin. [Paylaşılan destek](../docs/support.md).

<a id="faq"></a>
## SSS

**MSI Afterburner'a da ihtiyacım var mı?** NVRasterPulse, RTSS'i gerektirir; Afterburner uygulamasına bağlı değildir. RTSS distribütörünün kurulum seçeneklerini takip edin.

**Bunu RTSS çalışmadan kullanabilir miyim?** Bir yükleme algılandıktan sonra profilleri yönetebilirsiniz, ancak sınırlama için RTSS'in çalışması gerekir.

**Bırakmak veya kaldırmak, sınırları kaldırır mı?** Hayır. NVRasterPulse'i kaldırmadan önce istenen sınırlayıcı geçersiz kılmalarını açıkça kaldırın.

**RTSS'in fork'i mi?** Hayır. Bağımsız bir profil yöneticisidir; hiçbir RTSS kaynağı veya yürütülebilir dosyası dahil edilmemiştir.

<a id="upstream-modifications-and-credits"></a>
## Yukarı akış, değişiklikler ve krediler

Geliştirme deposu [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector)'ten kaynaklanır. MIT paletleri/UI kaynakları kredilendirilmiştir. Profil yönetimi hizmetleri, kesir kodlaması, yedeklemeler, RTSS yeniden yükleme köprüsü, tepsi davranışı, önkoşul kılavuzu, diller ve uygulamaya özel simge 禅堂 Zendo (RevoluSound Team) tarafından geliştirilmiş/uyarlanmıştır.

RTSS, **Unwinder** tarafından geliştirilmiş ve Guru3D aracılığıyla ayrı olarak dağıtılmıştır. NVRasterPulse, seçili yüklü kanca DLL'sinden `UpdateProfiles`'i çağırır; hiçbir RTSS SDK veya kanca ikili dosyası yeniden dağıtılmaz. Yükleyici, uyarlanmış komut dosyaları/çeviriler ve bir proje önyüklemesi ile değiştirilmemiş Inno Setup 7.1.0'i kullanır.

[Tam kaynak](../docs/provenance.md) · [Üçüncü taraf tablosu](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Lisans

Paket, NVRasterPulse'i, sağlanan [MIT lisansı](../../../../NVRasterPulse/LICENSE) kapsamında açıkça dağıtır ve Telif Hakkı (c) 2016 Orbmu2k'i saklı tutar. Uygulama kaynağı özel olarak korunur; MIT, değiştirilmiş kaynağın yayınlanmasını gerektirmez. RTSS ve Windows/.NET kendi koşulları altında kalır. [Tam bildirimler](LICENSES/README.md).

NVIDIA Corporation, MSI ve RTSS'ten bağımsız; onlar tarafından desteklenmiyor veya resmi olarak onaylanmıyor. Ürün adları sahiplerinin ticari markaları olmaya devam etmektedir.
