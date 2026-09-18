<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · **فارسی** · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ترجمه ماشینی از انگلیسی. نام های فنی، دستورات، URL ها و متون قانونی اصلی حفظ می شوند. بررسی بومی زبان خوش آمدید. اگر جمله بندی نامشخص است به مرجع انگلیسی مراجعه کنید.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="publishing-and-releases"></a>
# انتشار و انتشار

مخزن عمومی **Zendo-GIT/NV-Laboratory** است. تغییرات اسناد توسط نگهدارنده با **GitHub Desktop** بازبینی، تعهد و فشار داده می‌شوند. یک commit محلی فایل ها را آپلود نمی کند. بسته های باینری دارایی های جداگانه GitHub Release هستند. آنها هرگز به لیست تغییرات Git تعلق ندارند.

<a id="documentation-updates"></a>
## به روز رسانی اسناد

1. پوشه **NV-Laboratory** را در GitHub Desktop باز کنید.
2. اسناد، اعلامیه‌ها، تصاویر، ابرداده‌های JSON و اعتبارسنجی اسناد را بررسی کنید.
3. `python tools/validate_repository.py` را از آن پوشه اجرا کنید.
4. تغییرات بررسی شده را انجام دهید، سپس از **Push origin** استفاده کنید. نتیجه Actions را بررسی کنید.
5. هویت نویسنده عمومی **禅堂 Zendo (RevoluSound Team)** و آدرس GitHub `noreply` حساب را حفظ کنید.

هرگز فضای کاری توسعه والد، دایرکتوری حسابرسی خصوصی یا دایرکتوری پیوست باینری را انتخاب نکنید. [حفظ حریم خصوصی ایمیل](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## انتشار برنامه های مستقل

| ابزار | برچسب بزنید | خط مشی نسخه |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | نسخه برنامه چهار قسمتی موجود. تنظیم نسخه 2 نام فایل خود را دارد |
| NVDriverForge | nvdriverforge-v0.1.4 | طرح 0.x موجود؛ به روز رسانی های نسخه شده بسته های قبلی را حفظ می کنند |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | نسخه برنامه 0.2.3; تغییرات تجمعی از 0.1.1 عمومی |
| NVRasterPulse | nvrasterpulse-v0.2 | نسخه دو قسمتی موجود |

نگهدار می تواند مستقیماً منتشر کند یا به دستیار اجازه دهد تا دارایی های حسابرسی شده را منتشر کند. انتشار صریح است؛ هیچ گردش کاری در هر commit یک Release ایجاد نمی کند.

1. گزارش پیش از انتشار فعلی، منابع باینری ها، مجوزها و مقادیر SHA-256 را مرور کنید.
2. یک پیش نویس برای تگ ابزار ایجاد کنید و commit بررسی شده هاب را هدف قرار دهید. یادداشت‌های انتشار ویژه نسخه آماده شده را اضافه کنید.
3. فقط دارایی های راه اندازی/قابل حمل آن نسخه، `Licenses-and-Credits.zip` و `SHA256SUMS.txt` را پیوست کنید.
4. سازگاری، نصب، وابستگی ها، تغییرات و محدودیت های شناخته شده را بررسی کنید. RTSS را برای NVRasterPulse برجسته نگه دارید.
5. نشانی‌های وب، اندازه‌ها و هش‌های دارایی عمومی را منتشر کنید، تأیید کنید و تاریخ انتشار واقعی را در `docs/releases.json` ثبت کنید.
6. صفحات دانلود و ترجمه ها را به روز کنید، سپس تغییرات آنها را در GitHub Desktop انجام دهید/فشار دهید.

پیوندهای برچسب هر پروژه از ارسال کاربران به ابزار دیگری از طریق پیوند مشترک `releases/latest` جلوگیری می کنند. آرشیوهای خودکار **Source code** GitHub حاوی این مرکز اسناد هستند. منابع برنامه خصوصی می مانند. اعلان‌های مؤلفه اصلی دست نخورده باقی می‌مانند و انتشار، ذخیره مستند NVIDIA SDK NVMFG را برطرف نمی‌کند.


آپدیت 18 سپتامبر سه تگ جدید را آماده می کند. نسخه موجود Profile Inspector بدون تغییر باقی می ماند. نام دارایی‌ها، برچسب‌ها و `SHA256SUMS.txt` باید برای بررسی‌های به‌روزرسانی برنامه دقیق باقی بماند. انتشارهای معمولی را بدون پرچم قبل از انتشار منتشر کنید تا آنها را در معرض بررسی های انتشار پایدار قرار دهید. NVMFG تجربی باقی می ماند.

<a id="integrity-and-storage"></a>
## یکپارچگی و ذخیره سازی

هرگز بی صدا بایت های باینری منتشر شده را جایگزین نکنید. از نسخه صریح جدید یا ویرایش نصب کننده با هش جدید استفاده کنید. اخطارهای تعبیه شده مکمل خودروهای جانبی قانونی. NVDriverForge 0.1.4 قابل حمل 142,017,891 بایت است که بالاتر از حد مجاز فایل Git 100 مگابایتی GitHub است. از قرار دادن فایل های باینری یا Git LFS در این هاب پرهیز کنید. [راهنمای فایل بزرگ GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

گزارش آسیب پذیری خصوصی باید در تنظیمات امنیتی مخزن فعال شود. قبل از ارسال گزارش های حساس به آنجا، در دسترس بودن آن را بررسی کنید. [SECURITY.md](../SECURITY.md) بازگشتی را ارائه می دهد که جزئیات آسیب پذیری را آشکار نمی کند.

[دانلود کاتالوگ](downloads.md) · [اسناد انتشار GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

</div>
