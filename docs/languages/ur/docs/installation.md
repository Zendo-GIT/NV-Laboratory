<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · **اردو** · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> انگریزی سے مشین کی مدد سے ترجمہ۔ تکنیکی نام، کمانڈ، یو آر ایل اور اصل قانونی متن محفوظ ہیں۔ مقامی بولنے والے کا جائزہ خوش آئند ہے۔ اگر الفاظ واضح نہیں ہیں تو انگریزی حوالہ سے مشورہ کریں۔
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="installation-guide"></a>
# انسٹالیشن گائیڈ

[ڈاؤن لوڈز](downloads.md) کے ساتھ شروع کریں، جو اشاعت کی حیثیت اور اثاثوں کے صحیح ناموں کو ریکارڈ کرتا ہے۔ یہ الگ الگ ٹولز ہیں: صرف وہی انسٹال کریں جن کی آپ کو ضرورت ہے۔

> **NVRasterPulse کے لیے، پروفائل مینیجر کو کھولنے سے پہلے [Guru3D سے RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) انسٹال کریں۔**
> RTSS کو حدود لاگو کرنے کے لیے چلنا چاہیے۔ یہ NV Tools میں شامل نہیں ہے۔

| ٹول | انسٹال شدہ ایڈیشن | پورٹ ایبل ایڈیشن | بنیادی شرط |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | مکمل NVPI ZIP نکالیں۔ | NVIDIA ڈرائیور اور .NET فریم ورک 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe، رن ٹائم شامل ہے۔ | تنصیب کی کارروائیوں کے لیے ہم آہنگ اصل NVIDIA ڈرائیور پیکیج |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | مکمل NVMFG زپ نکالیں، ذیلی فولڈرز کو برقرار رکھیں | RTX 40، موجودہ DLSS FG، عین مطابق فراہم کنندہ اور .NET فریم ورک 4.8 مددگار |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | مکمل RP ZIP نکالیں۔ | RTSS اور .NET فریم ورک 4.8 |

<a id="download-verify-install"></a>
## ڈاؤن لوڈ کریں، تصدیق کریں، انسٹال کریں۔

1. منتخب کردہ شائع شدہ ریلیز پر، اس کا نامزد کردہ ایپلیکیشن اثاثہ، نوٹس زپ اور SHA256SUMS.txt ڈاؤن لوڈ کریں۔
2. [SHA-256 مثال](downloads.md#sha-256) استعمال کریں، اصل ڈاؤن لوڈ کردہ فائل نام کے ساتھ۔
3. سیٹ اپ کے لیے، عام انسٹالر کی پیروی کریں۔ پورٹیبل زپ کے لیے، ہر چیز کو ایک نئے مقامی قابل تحریر فولڈر میں نکالیں۔ زپ کے اندر سے مت بھاگو۔
4. ایپلیکیشن کا اپنا EXE کھولیں۔ لائسنس/کنفیگریشن/ڈیٹا فائلیں ساتھ رکھیں۔
5. ترتیبات یا سسٹم آپریشنز کو فعال کرنے سے پہلے اس ٹول کے استعمال کی ہدایات پڑھیں۔

موجودہ بائنریز غیر دستخط شدہ ہیں۔ ایک مماثل ہیش متوقع بائٹس کی تصدیق کرتا ہے۔ یہ سیکیورٹی یا مطابقت کا سرٹیفکیٹ نہیں ہے۔ صرف انتباہ کو دبانے کے لیے Windows حفاظتی تحفظات کو غیر فعال نہ کریں۔

NVDF یا اس کے اختیاری NVPI ساتھی کو انسٹال کرنا GPU ڈرائیور کو انسٹال کرنے سے الگ ہے۔ NVPI ساتھی اپنا موجودہ اندرونی تنصیب کا نام رکھتا ہے۔ اس کے ایلیویٹڈ RasterPulse بٹن کو پورے نظام میں محفوظ تنصیب کی ضرورت ہے۔ دیگر RP کاپیاں ان کے اپنے شارٹ کٹس کے ذریعے کھولی جا سکتی ہیں۔

NVMFG تجرباتی ہے اور اس میں [دستاویزی NVIDIA SDK لائسنسنگ ریزرو](provenance.md) ہے۔ کوئی NVIDIA ڈرائیور، NGX فراہم کنندہ/ماڈل یا گیم Streamline رن ٹائم شامل نہیں ہے۔ منتخب کردہ SDK ڈاؤن لوڈز اور گیم اپ ڈیٹس واضح طور پر علیحدہ آپریشنز ہیں۔

<a id="language-and-updates"></a>
## زبان اور اپ ڈیٹس

دستاویزات کے لیے README کا 34 زبان کا انتخاب کنندہ استعمال کریں۔ NVDF, NVMFG اور RP کی اپنی 34 زبان کی UI سیٹنگ ہے۔ NVPI اپنی موجودہ زبان کی حمایت کو برقرار رکھتا ہے۔ کچھ انسٹالر تکنیکی تار انگریزی میں واپس آتے ہیں۔

اپ ڈیٹ کرتے وقت ٹول کی انسٹالیشن شناخت رکھیں۔ پہلے اسے بند کریں اور بیک اپ محفوظ کریں۔ NVMFG کے لیے، متاثرہ گیمز کو بند کریں اور زیر التواء پروفائل ریکوری کو حل کریں۔ پورٹیبل اپ ڈیٹس کے لیے، ریلیز کو یکجا کرنے کے بجائے ایک تازہ فولڈر استعمال کریں۔

<a id="removing-a-tool"></a>
## ایک آلے کو ہٹانا

کسی ایپلیکیشن کو ان انسٹال کرنا خود بخود اس کی سیٹنگز کو کالعدم نہیں کرتا ہے۔

- **NVPI:** اگر ضرورت ہو تو ہٹانے سے پہلے مطلوبہ پروفائلز/ڈسپلے سیٹنگز کو بحال کریں۔
- **NVDF:** اگر آپ جدید/NVENC تبدیلیاں بحال کرنا چاہتے ہیں تو پہلے ریکوری کا استعمال کریں۔ Uninstall گرافکس ڈرائیور، سیٹنگز اور بیک اپ کو چھوڑ دیتا ہے۔
- **NVMFG:** گیمز بند کریں، کنٹرولر کو غیر فعال/چھوڑ دیں، NVIDIA ریکوری کو حل کریں اور ہٹانے سے پہلے مطلوبہ گیم SDK بیک اپ بحال کریں۔
- **RP:** پہلے مطلوبہ حد کو ہٹا دیں۔ Uninstall محفوظ کردہ RTSS کیپس کو نہیں مٹاتا ہے اور نہ ہی RTSS کو ہٹاتا ہے۔

درست اعداد و شمار کے مقامات اور حدود کے لیے ہر [پروجیکٹ گائیڈ](../README.md#projects) دیکھیں، یا [حمایت](support.md) اگر بحالی کا مرحلہ ناکام ہو جاتا ہے۔

</div>
