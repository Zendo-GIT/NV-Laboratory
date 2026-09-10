<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · **اردو** · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> انگریزی سے مشین کی مدد سے ترجمہ۔ تکنیکی نام، کمانڈ، یو آر ایل اور اصل قانونی متن محفوظ ہیں۔ مقامی بولنے والے کا جائزہ خوش آئند ہے۔ اگر الفاظ واضح نہیں ہیں تو انگریزی حوالہ سے مشورہ کریں۔
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="publishing-and-releases"></a>
# اشاعت اور ریلیز

عوامی ذخیرہ **Zendo-GIT/NV-Laboratory** ہے۔ **GitHub Desktop** کے ساتھ دیکھ بھال کرنے والے کی طرف سے دستاویزی تبدیلیوں کا جائزہ لیا جاتا ہے، عزم کیا جاتا ہے اور آگے بڑھایا جاتا ہے۔ مقامی کمٹ فائلیں اپ لوڈ نہیں کرتا ہے۔ بائنری پیکجز علیحدہ GitHub ریلیز اثاثے ہیں۔ وہ کبھی بھی گٹ تبدیلیوں کی فہرست میں شامل نہیں ہیں۔

<a id="documentation-updates"></a>
## دستاویزی اپ ڈیٹس

1. GitHub Desktop میں **NV-Laboratory** فولڈر کھولیں۔
2. دستاویزات، نوٹسز، تصاویر، JSON میٹا ڈیٹا اور دستاویزات کی توثیق کرنے والے کا جائزہ لیں۔
3. اس فولڈر سے `python tools/validate_repository.py` چلائیں۔
4. نظرثانی شدہ تبدیلیوں کا ارتکاب کریں، پھر **Push origin** استعمال کریں۔ اعمال کا نتیجہ چیک کریں۔
5. عوامی مصنف کی شناخت **禅堂 Zendo (RevoluSound Team)** اور اکاؤنٹ کا GitHub `noreply` پتہ رکھیں۔

پیرنٹ ڈیولپمنٹ ورک اسپیس، پرائیویٹ آڈٹ ڈائرکٹری یا بائنری اٹیچمنٹ ڈائرکٹری کو کبھی بھی منتخب نہ کریں۔ [ای میل کی رازداری کا عہد کریں۔](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)۔

<a id="independent-application-releases"></a>
## آزاد درخواست کی ریلیز

| ٹول | ٹیگ | ورژن کی پالیسی |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | موجودہ چار حصوں کا ایپلیکیشن ورژن؛ سیٹ اپ ریویژن 2 کا اپنا فائل نام ہے۔ |
| NVDriverForge | nvdriverforge-v0.1.3 | موجودہ 0.x اسکیم؛ ورژن شدہ اپ ڈیٹس پہلے کے پیکجوں کو محفوظ رکھتی ہیں۔ |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2 امیدوار کی شناخت ایک نیا ایپلیکیشن ورژن ایجاد کیے بغیر عین ہیش کے ذریعے کی گئی۔ |
| NVRasterPulse | nvrasterpulse-v0.1 | موجودہ دو حصوں والا ورژن |

دیکھ بھال کرنے والا براہ راست شائع کر سکتا ہے یا کسی معاون کو آڈٹ شدہ اثاثوں کو شائع کرنے کی اجازت دے سکتا ہے۔ اشاعت واضح ہے؛ کوئی ورک فلو ہر کمٹ پر ریلیز نہیں بناتا ہے۔

1. موجودہ پری اشاعت رپورٹ، بائنریز کے ذرائع، لائسنس اور SHA-256 اقدار کا جائزہ لیں۔
2. ٹول کے ٹیگ کے لیے ایک مسودہ بنائیں، نظرثانی شدہ حب کمٹ کو نشانہ بناتے ہوئے۔ تیار کردہ ورژن کے لیے مخصوص ریلیز نوٹس شامل کریں۔
3. صرف اس ورژن کے سیٹ اپ/پورٹ ایبل اثاثے، `Licenses-and-Credits.zip` اور `SHA256SUMS.txt` منسلک کریں۔
4. مطابقت، تنصیب، انحصار، تبدیلیاں اور معلوم حدود کی جانچ کریں۔ RTSS کو NVRasterPulse کے لیے نمایاں رکھیں۔
5. شائع کریں، عوامی اثاثوں کے URLs، سائز اور ہیشز کی تصدیق کریں، اور `docs/releases.json` میں اشاعت کی اصل تاریخ ریکارڈ کریں۔
6. ڈاؤن لوڈ صفحات اور ترجمے کو اپ ڈیٹ کریں، پھر GitHub Desktop میں ان کی تبدیلیوں کا ارتکاب/پش کریں۔

فی پروجیکٹ ٹیگ لنکس مشترکہ `releases/latest` لنک کے ذریعے صارفین کو دوسرے ٹول پر بھیجنے سے گریز کرتے ہیں۔ GitHub کے خودکار **Source code** آرکائیوز اس دستاویزی مرکز پر مشتمل ہیں۔ درخواست کے ذرائع نجی رہیں۔ اصل اجزاء کے نوٹس برقرار ہیں، اور ایک ریلیز NVMFG کے دستاویزی NVIDIA SDK ریزرو کو حل نہیں کرتی ہے۔

<a id="integrity-and-storage"></a>
## سالمیت اور اسٹوریج

کبھی بھی خاموشی سے شائع شدہ بائنری بائٹس کو تبدیل نہ کریں۔ نئی ہیشز کے ساتھ ایک نیا واضح ورژن یا انسٹالر ریویژن استعمال کریں۔ قانونی سائڈ کارس ایمبیڈڈ نوٹسز کی تکمیل کرتے ہیں۔ NVDriverForge 0.1.3 پورٹیبل 141,760,351 بائٹس ہے، GitHub کی عام 100 MiB گٹ فائل کی حد سے زیادہ۔ ریلیز منسلکات اس حب میں بائنریز یا Git LFS ڈالنے سے گریز کریں۔ [GitHub بڑی فائل گائیڈنس](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)۔

ریپوزٹری سیکیورٹی سیٹنگز میں پرائیویٹ ویلنریبلٹی رپورٹنگ کو فعال کیا جانا چاہیے۔ حساس رپورٹوں کو وہاں بھیجنے سے پہلے اس کی دستیابی کی تصدیق کریں۔ [SECURITY.md](../SECURITY.md) ایک فال بیک فراہم کرتا ہے جو خطرے کی تفصیلات کو ظاہر نہیں کرتا ہے۔

[کیٹلاگ ڈاؤن لوڈ کریں۔](downloads.md) · [GitHub ریلیز دستاویزات](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

</div>
