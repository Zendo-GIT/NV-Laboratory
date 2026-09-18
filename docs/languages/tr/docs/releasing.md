<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · **Türkçe** · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> İngilizce'den makine destekli çeviri. Teknik adlar, komutlar, URL'ler ve orijinal yasal metinler korunur. Ana dili konuşanların incelemeleri memnuniyetle karşılanır; ifadeler net değilse İngilizce referansa bakın.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Yayınlama ve sürümler

Halka açık depo **Zendo-GIT/NV-Laboratory**'dir. Belge değişiklikleri bakımcı tarafından **GitHub Desktop** ile incelenir, uygulanır ve iletilir. Yerel bir taahhüt dosya yüklemez. İkili paketler ayrı GitHub Sürüm varlıklarıdır; asla Git değişiklikleri listesine ait değiller.

<a id="documentation-updates"></a>
## Dokümantasyon güncellemeleri

1. GitHub Desktop'te **NV-Laboratory** klasörünü açın.
2. Belgeleri, bildirimleri, görüntüleri, JSON meta verilerini ve belge doğrulayıcıyı inceleyin.
3. `python tools/validate_repository.py`'i bu klasörden çalıştırın.
4. Gözden geçirilen değişiklikleri kaydedin ve ardından **Push origin**'i kullanın. Eylemler sonucunu kontrol edin.
5. Herkese açık yazar kimliğini **禅堂 Zendo (RevoluSound Team)** ve hesabın GitHub `noreply` adresini saklayın.

Hiçbir zaman ana geliştirme çalışma alanını, özel denetim dizinini veya ikili ek dizinini seçmeyin. [E-posta gizliliğini taahhüt edin](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Bağımsız uygulama sürümleri

| Araç | Etiket | Sürüm politikası |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Mevcut dört bölümlü uygulama sürümü; kurulum revizyonu 2'nin kendi dosya adı var |
| NVDriverForge | nvdriverforge-v0.1.4 | Mevcut 0.x şeması; sürümlendirilmiş güncellemeler önceki paketleri korur |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Uygulama sürümü 0.2.3; halka açık 0.1.1'ten bu yana kümülatif değişiklikler |
| NVRasterPulse | nvrasterpulse-v0.2 | Mevcut iki parçalı versiyon |

Bakımcı, denetlenen varlıkları doğrudan yayınlayabilir veya bir asistanı yayınlaması için yetkilendirebilir. Yayın açıktır; hiçbir iş akışı her taahhütte bir Sürüm oluşturmaz.

1. Mevcut yayın öncesi raporunu, ikili dosyaların kaynaklarını, lisansları ve SHA-256 değerlerini inceleyin.
2. Aracın etiketi için, incelenen merkez taahhüdünü hedefleyen bir taslak oluşturun. Hazırlanan sürüme özel sürüm notlarını ekleyin.
3. Yalnızca bu sürümün Kurulum/taşınabilir varlıklarını (`Licenses-and-Credits.zip` ve `SHA256SUMS.txt`) ekleyin.
4. Uyumluluğu, kurulumu, bağımlılıkları, değişiklikleri ve bilinen sınırları kontrol edin. RTSS'i NVRasterPulse için belirgin tutun.
5. Genel varlık URL'lerini, boyutlarını ve karmalarını yayınlayın, doğrulayın ve gerçek yayın tarihini `docs/releases.json`'e kaydedin.
6. İndirme sayfalarını ve çevirileri güncelleyin, ardından değişikliklerini GitHub Desktop'e aktarın/gönderin.

Proje başına etiket bağlantıları, kullanıcıların paylaşılan bir `releases/latest` bağlantısı aracılığıyla başka bir araca gönderilmesini önler. GitHub'in otomatik **Source code** arşivleri bu belge merkezini içerir. Uygulama kaynakları gizli kalır. Orijinal bileşen bildirimleri bozulmadan kalır ve bir sürüm, NVMFG'nin belgelenen NVIDIA SDK rezervini çözümlemez.


18 Eylül güncellemesi üç yeni etiket hazırlıyor; mevcut Profile Inspector Sürümü değişmeden kalır. Uygulama güncelleme kontrolleri için varlık adları, etiketler ve `SHA256SUMS.txt` aynı kalmalıdır. Normal Sürümleri kararlı sürüm kontrollerine tabi tutmak için ön sürüm işareti olmadan yayınlayın; NVMFG deneysel olmaya devam ediyor.

<a id="integrity-and-storage"></a>
## Bütünlük ve depolama

Yayınlanan ikili baytları asla sessizce değiştirmeyin. Yeni karmalarla yeni bir açık sürüm veya yükleyici revizyonu kullanın. Yasal sepetler gömülü bildirimleri tamamlar. NVDriverForge 0.1.4 taşınabilir, GitHub'in normal 100 MiB Git dosyası sınırının üzerinde 142.017.891 bayttır. Sürüm ekleri, ikili dosyaları veya Git LFS'yi bu merkeze koymaktan kaçınır. [GitHub büyük dosya kılavuzu](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Depo güvenliği ayarlarında özel güvenlik açığı raporlaması etkinleştirilmelidir. Hassas raporları oraya yönlendirmeden önce kullanılabilirliğini doğrulayın; [SECURITY.md](../SECURITY.md), güvenlik açığı ayrıntılarını açığa çıkarmayan bir geri dönüş sağlar.

[Kataloğu indir](downloads.md) · [GitHub sürüm belgeleri](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
