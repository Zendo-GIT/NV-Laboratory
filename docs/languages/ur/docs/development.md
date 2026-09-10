<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · **اردو** · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> انگریزی سے مشین کی مدد سے ترجمہ۔ تکنیکی نام، کمانڈ، یو آر ایل اور اصل قانونی متن محفوظ ہیں۔ مقامی بولنے والے کا جائزہ خوش آئند ہے۔ اگر الفاظ واضح نہیں ہیں تو انگریزی حوالہ سے مشورہ کریں۔
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="repository-architecture-and-maintenance"></a>
# مخزن کا فن تعمیر اور دیکھ بھال

NV Laboratory ایک عوامی **دستاویزات اور بائنری ڈسٹری بیوشن ہب** ہے۔ اس میں درخواست کا ذریعہ نہیں ہے۔ چار منصوبے الگ الگ تعمیراتی درخت، ورژن، شناخت اور ریلیز اثاثے کو برقرار رکھتے ہیں۔ ان کی نجی ترقی کی تاریخ اس Git ذخیرہ میں درآمد نہیں کی گئی ہے۔

<a id="layout"></a>
## لے آؤٹ

| مقام | مقصد |
| --- | --- |
| README.md / README.fr.md | انگریزی/فرانسیسی انٹری پوائنٹس |
| چار پروجیکٹ فولڈر | مکمل گائیڈز اور قابل اطلاق اصل نوٹس |
| دستاویزات | ڈاؤن لوڈ، مطابقت، اصل، ترقی اور رہائی کا طریقہ کار |
| docs/releases.json | آڈٹ شدہ امیدوار/ریلیز میٹا ڈیٹا، سائز اور ہیش |
| docs/provenance | فائل/ہیش موازنہ؛ کوئی درخواست کوڈ نہیں۔ |
| لائسنس | تیسرے فریق کے مکمل متن اور انسٹالر ٹرانسلیٹر کریڈٹس کا اشتراک کیا گیا۔ |
| اثاثے | موجودہ نظرثانی شدہ UI پیش نظارہ اور ان کی اصل |
| .github | ایشو فارمز اور صرف پڑھنے کے لیے دستاویزات کی توثیق |
| ٹولز/validate_repository.py | معیاری لائبریری پبلیکیشن باؤنڈری اور لنک چیک |

انگریزی پہلے سے طے شدہ GitHub README ہے۔ موجودہ ملحقہ `.fr.md` لنکس درست رہتے ہیں۔ اضافی ترجمے `docs/languages/<code>` کے تحت دستاویزات کی عکاسی کرتے ہیں۔ زبانوں کو تبدیل کرتے وقت زبان کا انتخاب کرنے والا ایک ہی صفحہ رکھتا ہے۔ کیٹلاگ `docs/languages/catalog.json` تمام 34 زبانوں اور ماخذ فنگر پرنٹس کو ریکارڈ کرتا ہے۔ GitHub خود بخود براؤزر کی زبان کے ذریعہ README کا انتخاب نہیں کرتا ہے۔ [زبان کا اشاریہ اور ترجمہ کی پالیسی](../../README.md) دیکھیں۔

<a id="application-technologies"></a>
## ایپلی کیشن ٹیکنالوجیز

| پروگرام | نجی ٹیکنالوجی | تقسیم |
| --- | --- | --- |
| NVPI fork | C#, WPF, NET Framework 4.8, NVAPI/Windows انٹراپ | پورٹیبل فولڈر کو مکمل کریں اور Inno Setup کو الگ کریں۔ |
| NVDriverForge | C#, WPF, .NET 8; مقامی C++ بوٹسٹریپ؛ 7-Zip عمل | خود پر مشتمل پورٹیبل EXE اور سیٹ اپ |
| NVMFG Unlock40 | C#/WPF .NET 8، فریم ورک 4.8 مددگار، C++20/MASM/MinHook انجن | پورٹیبل درخت اور سیٹ اپ |
| NVRasterPulse | C#/WPF فریم ورک 4.8؛ RTSS پروفائل/ری لوڈ انضمام؛ مقامی بوٹسٹریپ | پورٹیبل درخت اور سیٹ اپ |

یہ عوامی چیک آؤٹ ایپلیکیشنز کو دوبارہ نہیں بنا سکتا۔ خودکار "Source code" آرکائیوز حب سنیپ شاٹس ہیں۔ اپ اسٹریم سورس لنکس بالکل پرائیویٹ ترمیم شدہ سورس کی نمائندگی نہیں کرتے ہیں۔ عوامی CI صرف اس ذخیرہ کی توثیق کرتا ہے۔

<a id="local-checks"></a>
## مقامی چیک

ذخیرہ کی جڑ سے:

```text
python tools/validate_repository.py
```

Python 3.10 یا اس سے نیا کافی ہے۔ چیک فائلوں، مقامی مارک ڈاؤن لنکس، مطلوبہ نوٹسز/RTSS لنکس، ریلیز میٹا ڈیٹا اور اشاعت کی حدود کو پڑھتا ہے۔ یہ سافٹ ویئر پر عمل درآمد نہیں کرتا، انحصار کو انسٹال کرتا ہے یا کسی نیٹ ورک سے رابطہ نہیں کرتا ہے۔

GitHub ورک فلو پش، پل ریکوئسٹ یا مینوئل ڈسپیچ پر صرف پڑھنے کے مواد کی اجازت کے ساتھ یہی چیک چلاتا ہے۔ چیک آؤٹ کو ایک آڈٹ شدہ کمٹ پر پن کیا جاتا ہے اور اسناد برقرار نہیں رہتی ہیں۔ کوئی ریلیز یا تعیناتی جاب کنفیگر نہیں ہے۔

<a id="maintain-the-boundary"></a>
## حد کو برقرار رکھیں

انگریزی حوالہ، فرانسیسی گائیڈز اور متاثرہ تراجم کو ایک ساتھ اپ ڈیٹ کریں۔ بنیادی تبدیلیوں کو صرف فارمیٹنگ کے موازنہ سے الگ رکھیں۔ اصل امیدوار ہیشز، اپ اسٹریم کمٹ حوالہ جات اور لائسنس ریکارڈ کریں۔ کسی پروجیکٹ کی مقبولیت سے کبھی بھی لائسنس کا اندازہ نہ لگائیں۔

تازہ ورژن والے ریلیز اثاثوں کا استعمال کریں اور تبدیل شدہ بائنریز، آرکائیوز اور ایمبیڈڈ نوٹس کا دوبارہ آڈٹ کریں۔ اس ذخیرہ کے باہر نجی بیک اپ محفوظ کریں۔ پرائیویٹ ایپلیکیشن سورس یا لوکل بلڈ فولڈرز درآمد کرنے کے لیے پبلک ورک فلو استعمال نہ کریں۔

پرائیویٹ پروجیکٹ میں چلائے جانے والے ایک فنکشنل ایپلیکیشن تبدیلی کے لیے موزوں ٹیسٹ۔ ڈرائیور انسٹالرز کو دوبارہ نہ چلائیں یا دستاویزات کی تازہ کاری کے لیے حقیقی پروفائلز نہ لکھیں۔ [دستی رہائی کا طریقہ کار](releasing.md)۔

</div>
