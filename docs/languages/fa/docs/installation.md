<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · **فارسی** · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ترجمه ماشینی از انگلیسی. نام های فنی، دستورات، URL ها و متون قانونی اصلی حفظ می شوند. بررسی بومی زبان خوش آمدید. اگر جمله بندی نامشخص است به مرجع انگلیسی مراجعه کنید.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="installation-guide"></a>
# راهنمای نصب

با [دانلودها](downloads.md) شروع کنید که وضعیت انتشار و نام دقیق دارایی ها را ثبت می کند. اینها ابزارهای جداگانه ای هستند: فقط آنهایی را که نیاز دارید نصب کنید.

> **برای NVRasterPulse، [RTSS از Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) را قبل از باز کردن مدیر نمایه نصب کنید.**
> RTSS باید برای اعمال محدودیت اجرا شود. در NV Tools گنجانده نشده است.

| ابزار | نسخه نصب شده | نسخه قابل حمل | پیش نیاز اصلی |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | NVPI ZIP کامل را استخراج کنید | درایور NVIDIA و NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe، زمان اجرا گنجانده شده است | بسته درایور اصلی NVIDIA برای عملیات نصب سازگار است |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | NVMFG ZIP کامل را استخراج کنید، زیرپوشه ها را حفظ کنید | RTX 40، DLSS FG موجود، ارائه‌دهنده دقیق و NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | RP ZIP کامل را استخراج کنید | RTSS و NET Framework 4.8 |

<a id="download-verify-install"></a>
## دانلود، تایید، نصب کنید

1. در نسخه منتشر شده انتخابی، دارایی برنامه نامگذاری شده آن، اطلاعیه های ZIP و SHA256SUMS.txt را دانلود کنید.
2. از [مثال SHA-256](downloads.md#sha-256) با نام فایل دانلود شده واقعی استفاده کنید.
3. برای راه اندازی، نصب کننده معمولی را دنبال کنید. برای ZIP قابل حمل، همه چیز را در یک پوشه قابل نوشتن محلی جدید استخراج کنید. از داخل ZIP اجرا نکنید.
4. EXE خود برنامه را باز کنید. مجوز/پیکربندی/فایل های داده همراه را نگه دارید.
5. قبل از فعال کردن تنظیمات یا عملیات سیستم، دستورالعمل‌های استفاده از آن ابزار را بخوانید.

باینری های فعلی بدون علامت هستند. یک هش مطابق بایت های مورد انتظار را تایید می کند. این یک گواهی امنیتی یا سازگاری نیست. حفاظت های امنیتی Windows را فقط برای سرکوب یک هشدار غیرفعال نکنید.

نصب NVDF یا همراه اختیاری NVPI آن جدا از نصب درایور GPU است. همراه NVPI نام نصب داخلی موجود خود را حفظ می کند. دکمه RasterPulse آن نیاز به نصب محافظت شده در سراسر سیستم دارد. سایر کپی های RP را می توان از طریق میانبرهای خود باز کرد.

NVMFG آزمایشی است و دارای [ذخیره مجوز NVIDIA SDK مستند](provenance.md) است. بدون درایور NVIDIA، ارائه دهنده/مدل NGX یا زمان اجرا Streamline بازی گنجانده شده است. دانلودهای انتخابی SDK و به‌روزرسانی‌های بازی، عملیات جداگانه‌ای هستند.

<a id="language-and-updates"></a>
## زبان و به روز رسانی

از انتخابگر 34 زبانی README برای مستندسازی استفاده کنید. NVDF، NVMFG و RP تنظیمات UI 34 زبانه خود را دارند. NVPI پشتیبانی زبان موجود خود را حفظ می کند. برخی از رشته های فنی نصب کننده به انگلیسی باز می گردند.

هنگام به‌روزرسانی، هویت نصب ابزار را حفظ کنید. ابتدا آن را ببندید و نسخه های پشتیبان را حفظ کنید. برای NVMFG، بازی‌های آسیب‌دیده را ببندید و بازیابی نمایه در انتظار را حل کنید. برای به‌روزرسانی‌های قابل حمل، به جای ترکیب کردن نسخه‌ها، از یک پوشه تازه استفاده کنید.

<a id="removing-a-tool"></a>
## حذف یک ابزار

حذف نصب یک برنامه به طور خودکار تنظیمات آن را لغو نمی کند.

- **NVPI:** نمایه ها/تنظیمات نمایشی مورد نظر را در صورت نیاز قبل از حذف بازیابی کنید.
- **NVDF:** اگر می‌خواهید تغییرات پیشرفته/NVENC را بازیابی کنید، ابتدا از بازیابی استفاده کنید. Uninstall درایور گرافیک، تنظیمات و پشتیبان‌گیری را ترک می‌کند.
- **NVMFG:** بازی ها را ببندید، کنترلر را غیرفعال یا ترک کنید، بازیابی NVIDIA را حل کنید و نسخه های پشتیبان بازی مورد نظر SDK را قبل از حذف بازیابی کنید.
- **RP:** ابتدا نادیده گرفتن محدود کننده های مورد نظر را حذف کنید. Uninstall سرپوش های ذخیره شده RTSS را پاک نمی کند یا RTSS را حذف نمی کند.

هر [راهنمای پروژه](../README.md#projects) را برای مکان‌ها و محدودیت‌های داده دقیق یا [پشتیبانی کنید](support.md) را در صورت شکست مرحله بازیابی مشاهده کنید.

</div>
