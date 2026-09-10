<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · **فارسی** · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ترجمه ماشینی از انگلیسی. نام های فنی، دستورات، URL ها و متون قانونی اصلی حفظ می شوند. بررسی بومی زبان خوش آمدید. اگر جمله بندی نامشخص است به مرجع انگلیسی مراجعه کنید.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="repository-architecture-and-maintenance"></a>
# معماری و نگهداری مخزن

NV Laboratory یک مرکز اسناد عمومی و توزیع باینری  است. این شامل منبع برنامه نیست. این چهار پروژه درخت های ساخت، نسخه ها، هویت ها و دارایی های انتشار جداگانه را حفظ می کنند. تاریخچه توسعه خصوصی آنها به این مخزن Git وارد نمی شود.

<a id="layout"></a>
## طرح بندی

| مکان | هدف |
| --- | --- |
| README.md / README.fr.md | نقاط ورود انگلیسی/فرانسوی |
| چهار پوشه پروژه | راهنماهای کامل و اعلامیه های اصلی قابل اجرا |
| اسناد | دانلودها، سازگاری، منشأ، توسعه و مراحل انتشار |
| docs/releases.json | فراداده‌ها، اندازه‌ها و هش‌های نامزد/انتشار ممیزی شده |
| اسناد/منشا | مقایسه فایل/هش؛ بدون کد برنامه |
| مجوزها | متون کامل شخص ثالث و اعتبار مترجم نصب کننده را به اشتراک گذاشته است |
| دارایی ها | پیش نمایش های UI بررسی شده موجود و منشأ آنها |
| github | فرم‌های صدور و تأیید اسناد فقط خواندنی |
| ابزار/validate_repository.py | استاندارد-کتابخانه انتشارات-مرز و بررسی پیوند |

انگلیسی GitHub README پیش فرض باقی می ماند. پیوندهای `.fr.md` مجاور موجود معتبر می مانند. ترجمه‌های اضافی مستندات را تحت `docs/languages/<code>` منعکس می‌کنند. انتخابگر زبان هنگام تغییر زبان همان صفحه را نگه می دارد. کاتالوگ `docs/languages/catalog.json` تمام 34 زبان و اثر انگشت منبع را ثبت می کند. GitHub به طور خودکار یک README را بر اساس زبان مرورگر انتخاب نمی کند. [فهرست زبان و سیاست ترجمه](../../README.md) را ببینید.

<a id="application-technologies"></a>
## فناوری های کاربردی

| برنامه | تکنولوژی خصوصی | توزیع |
| --- | --- | --- |
| NVPI fork | C#، WPF، NET Framework 4.8، NVAPI/Windows interop | پوشه قابل حمل را کامل کنید و Inno Setup را جدا کنید |
| NVDriverForge | C#، WPF، .NET 8; بوت استرپ بومی C++; فرآیند 7-Zip | EXE و Setup قابل حمل مستقل |
| NVMFG Unlock40 | C#/WPF .NET 8، راهنماهای Framework 4.8، موتور C++20/MASM/MinHook | درخت قابل حمل و راه اندازی |
| NVRasterPulse | C#/WPF Framework 4.8; یکپارچه سازی نمایه/بارگذاری مجدد RTSS؛ بوت استرپ بومی | درخت قابل حمل و راه اندازی |

این تسویه حساب عمومی نمی تواند برنامه ها را بازسازی کند. بایگانی های خودکار "Source code" عکس فوری هاب هستند. پیوندهای منبع بالادست منبع دقیق اصلاح شده خصوصی را نشان نمی دهند. CI عمومی فقط این مخزن را تأیید می کند.

<a id="local-checks"></a>
## چک های محلی

از ریشه مخزن:

```text
python tools/validate_repository.py
```

Python 3.10 یا جدیدتر کافی است. چک فایل‌ها، پیوندهای Markdown محلی، اطلاعیه‌های مورد نیاز/ پیوندهای RTSS، فراداده انتشار و مرزهای انتشار را می‌خواند. این نرم افزار را اجرا نمی کند، وابستگی ها را نصب نمی کند یا با شبکه تماس نمی گیرد.

گردش کار GitHub همین بررسی را با مجوز محتویات فقط خواندنی در درخواست فشار، کشش یا ارسال دستی اجرا می کند. تسویه حساب به یک تعهد حسابرسی شده پین ​​می شود و اعتبارنامه ها را حفظ نمی کند. هیچ کار انتشار یا استقرار پیکربندی نشده است.

<a id="maintain-the-boundary"></a>
## مرز را حفظ کنید

مرجع انگلیسی، راهنماهای فرانسوی و ترجمه های تحت تأثیر را با هم به روز کنید. تغییرات اساسی را از مقایسه های فقط قالب بندی جدا نگه دارید. هش های واقعی نامزدها، مراجع ارتکاب بالادستی و مجوزها را ثبت کنید. هرگز از محبوبیت یک پروژه مجوز دریافت نکنید.

از دارایی‌های انتشار نسخه جدید استفاده کنید و باینری‌ها، بایگانی‌ها و اعلامیه‌های تعبیه‌شده را دوباره ممیزی کنید. پشتیبان های خصوصی را در خارج از این مخزن حفظ کنید. از یک گردش کار عمومی برای وارد کردن منبع برنامه خصوصی یا پوشه های ساخت محلی استفاده نکنید.

تست های مناسب برای تغییر برنامه کاربردی در پروژه خصوصی اجرا می شود. نصب کننده های درایور را دوباره اجرا نکنید یا پروفایل های واقعی را برای به روز رسانی اسناد ننویسید. [روش انتشار دستی](releasing.md).

</div>
