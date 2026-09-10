<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · **فارسی** · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ترجمه ماشینی از انگلیسی. نام های فنی، دستورات، URL ها و متون قانونی اصلی حفظ می شوند. بررسی بومی زبان خوش آمدید. اگر جمله بندی نامشخص است به مرجع انگلیسی مراجعه کنید.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**یک fork مستقل از [NVIDIA Profile Inspector توسط Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector)، با کنترل‌های نمایشگر اضافه شده.** نام پروژه قبلی: **NVPI Custom**.

[وضعیت دانلود و انتشار](../docs/downloads.md#nvidia-profile-inspector) · [نصب و راه اندازی](#installation) · [بالادست و تغییرات](#upstream-and-changes) · [مجوز](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## نمای کلی

این برنامه پروفایل های درایور NVIDIA را ویرایش می کند، از جمله تنظیمات هر برنامه. این fork همچنین یک ویرایشگر **صفحه** را برای نمایشگر فعال Windows اضافه می کند: وضوح، نرخ تازه سازی، تنظیمات رنگ خروجی، HDR و پیوندهای پروفایل نصب شده ICC/WCS.

برای وارد کردن کنترل‌های نمایش مرتبط به ویرایشگر نمایه و شفاف‌تر کردن نتایج پیش‌نمایش، تأیید و بازیابی وجود دارد. قابلیت های سخت افزاری جدیدی ایجاد نمی کند.

اولین نامزد **3.0.2.3** است که از ساخت همراه مستقل تمیز شده از 9 سپتامبر 2026 استفاده می کند. فایل اجرایی موجود آن `nvidiaProfileInspector.exe` باقی می ماند. نصب کننده و برخی از برچسب های داخلی همچنان `NVPI Custom NV` را نشان می دهند. عنوان عمومی بالا fork را بدون تغییر هویت نصب یا تظاهر به انتشار رسمی Orbmu2k شناسایی می کند.

<a id="features"></a>
## ویژگی ها

- مرور نمایه بالادستی موجود، ارتباط برنامه‌ها، تنظیمات ویرایش و واردات/صادرات نمایه.
- گفتگوی **صفحه نمایش** برای نمایش، حالت، هرتز، RGB/YCbCr، عمق رنگ، محدوده و رنگ سنجی.
- Windows HDR را کنترل و انتخاب ارتباط ICC/WCS را نصب کرد.
- پیش‌نمایش صفحه نمایش 15 ثانیه‌ای با **Keep** / **Revert** و بازیابی مهلت زمانی.
- بازخوانی حالت/تغییرات HDR و گزارش خرابی های بازیابی.
- گزارش جداگانه HDR، SDR با ACM/WCG و عمق رنگ سیگنال.
- یک راه‌انداز NVRasterPulse برای یک نسخه قابل نصب جداگانه.

<a id="compatibility"></a>
## سازگاری

| مورد نیاز | جزئیات |
| --- | --- |
| سیستم | Windows 10/11 x64 با درایور سازگار NVIDIA |
| زمان اجرا | [NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)، عرضه شده توسط Windows یا نصب جداگانه |
| مجوزها | ویرایشگر هنگام باز کردن، دسترسی مدیر را درخواست می کند |
| نمایش می دهد | حالت های واقعی و ترکیب رنگ ها به GPU، درایور، نمایشگر، کابل و Windows API بستگی دارد. |
| ابزار اختیاری | NVRasterPulse برای مدیریت محدودیت RTSS؛ نه آن و نه RTSS برای ویرایشگر صفحه مورد نیاز نیست |
| زبان ها | راه اندازی: انتخابگر 34 زبان. ویرایشگر پشتیبانی زبان موجود خود را حفظ می کند. |

برای هر GPU حداقل درایور جهانی تأیید شده یا ماتریس پشتیبانی وجود ندارد. انتخاب‌های bpc موجود در گفتگو، درخواست‌ها هستند، نه ترکیب‌های تایید شده. کنترل‌های مدرن HDR و Windows قدیمی‌تر دارای قابلیت‌های متفاوتی هستند.

<a id="installation"></a>
## نصب و راه اندازی

1. [صفحه دانلود](../docs/downloads.md#nvidia-profile-inspector) را باز کنید و وضعیت انتشار را بررسی کنید.
2. Setup یا دارایی قابل حمل را دانلود کنید و SHA-256 آن را با مانیفست Release مقایسه کنید.
3. برای راه اندازی، `NVPI-CustomNV-3.0.2.3-Setup-r2.exe` را اجرا کنید، یک زبان را انتخاب کنید و نصب کننده را دنبال کنید. میانبر و حذف کننده خود را ایجاد می کند.
4. برای قابل حمل، ZIP کامل را در یک پوشه قابل نوشتن جدید استخراج کنید. `Reference.xml`، پیکربندی EXE و همه اطلاعیه ها را در کنار فایل اجرایی نگه دارید.
5. `nvidiaProfileInspector.exe` را اجرا کنید.

نصب ویرایشگر به تنهایی یک نمایه را اعمال نمی کند یا یک درایور GPU را نصب نمی کند. همراه به طور جداگانه نصب می‌کند، انجمن‌های `.nip` را در اختیار نمی‌گیرد و راه‌اندازی را در هنگام ورود فعال نمی‌کند. باینری های موجود بدون علامت هستند.

<a id="usage"></a>
## استفاده

**نسخه نصب کننده 2** همان انتخابگر 34 زبانه بومی را مانند سایر ابزارها، با ناوبری ماوس/صفحه کلید، ظاهر روشن/تاریک و لغو اضافه می کند. این انتخاب برای راه اندازی اعمال می شود. ویرایشگر NVPI را ترجمه نمی کند. یک آرگومان صریح `/LANG=fr` یا حالت بی‌صدا، انتخاب تماس‌گیرندگانی را که قبلاً زبان ارائه کرده‌اند دور می‌زند.

**نمایه های درایور:** یک نمایه را انتخاب کنید، یک نسخه پشتیبان صادر کنید، سپس فقط تنظیمات مورد نظر را ویرایش کنید و آنها را اعمال کنید. انجمن های برنامه تعیین می کنند که کدام بازی نمایه دریافت کند. مقدار ذخیره شده دلیلی بر این نیست که هر راننده یا بازی از آن استفاده می کند.

**کنترل های نمایشگر:** **صفحه نمایش** را باز کنید، نمایشگر و مقادیر درخواستی را انتخاب کنید، سپس پیش نمایش را شروع کنید. قبل از انتخاب **Keep** در عرض 15 ثانیه تصویر را بررسی کنید. برای درخواست بازیابی از **بازگرداندن** استفاده کنید، تاییدیه را ببندید یا اجازه دهید منقضی شود. هر پیام خرابی را بخوانید: یک تماس موفق API به تنهایی دلیلی بر بازیابی نیست.

یک انتخاب ICC یک ارتباط پروفایل نصب شده را تغییر می دهد. فایل ICC را تولید، کالیبره یا توزیع مجدد نمی کند. HDR، ACM/WCG، RGB/YCbCr و bpc جنبه های مختلف خط لوله را توصیف می کنند. سوئیچ ACM مستقل جدیدی ارائه نشده است.

**NVRasterPulse:** دکمه نوار ابزار یک نصب جداگانه ثبت شده در سراسر سیستم را در زیر فایل های برنامه با مالکیت و مجوزهای محافظت شده می پذیرد. یک کپی قابل حمل یا یک مسیر قابل نوشتن/پیوند شده توسط کاربر ممکن است توسط این پرتابگر بالا رد شود. در این صورت NVRasterPulse را با استفاده از میانبر خودش باز کنید. [RTSS را جداگانه نصب کنید](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) برای استفاده از NVRasterPulse.

<a id="screenshots"></a>
## اسکرین شات ها

![انتخابگر زبان نسخه 2 راه اندازی NVPI](../../../../assets/screenshots/nvpi-setup-r2-language.png)

انتخابگر راه‌اندازی واقعی به زبان فرانسوی، در طول یک آزمایش مجزا گرفته شده و سپس لغو شد. این نصب کننده را نشان می دهد. ویرایشگر رابط کاربری و گفتگوی صفحه را حفظ می کند.

<a id="update-and-uninstall"></a>
## به روز رسانی و حذف نصب کنید

قبل از به روز رسانی ویرایشگر را ببندید. پروفایل های صادر شده را نگه دارید و نسخه جدید fork را دانلود کنید. روی همان هویت همراه نصب کنید یا فایل های قابل حمل را در یک پوشه تازه استخراج کنید. یک `Reference.xml` قدیمی را با یک فایل اجرایی جدید مخلوط نکنید. حذف بررسی آپدیت بالادستی به این fork تعلق دارد.

برای یک کپی نصب شده، از Windows **Installed apps** و حذف نصب کننده آن استفاده کنید. برای قابل حمل، آن را ببندید و پوشه استخراج شده آن را هنگامی که صادرات شما ایمن است حذف کنید. حذف ویرایشگر ویرایش‌های نمایه راننده، تنظیمات برگزیده نمایش، NVRasterPulse یا RTSS را **نمی‌کند**. قبل از حذف تنظیمات دلخواه را بازیابی کنید.

<a id="known-limitations"></a>
## محدودیت های شناخته شده

- تاییدیه 15 ثانیه ای یک نگهبان برای هر تصادف راننده، قطع برق یا خاموش شدن اجباری نیست.
- برخی از ترکیبات رنگ/عمق/بازسازی `NVAPI_NOT_SUPPORTED` را برمی‌گردانند.
- بازخوانی نرم افزار عمق بیت پانل، دقت رنگ یا تأخیر را اندازه گیری نمی کند.
- تنظیمات صفحه نمایش Windows فعلی را تحت تأثیر قرار می دهد. این گفتگو از پیش تنظیمات نمایش هر بازی را ایجاد نمی کند.
- بدون تضمین عملکرد، ضد تقلب یا سازگاری جهانی HDR.

<a id="troubleshooting"></a>
## عیب یابی

| علامت | اقدام |
| --- | --- |
| خطای زمان اجرا هنگام راه اندازی | به روز رسانی Windows و NET Framework 4.8 را بررسی کنید. از پکیج کامل استفاده کنید |
| حالت نمایش درخواستی رد شد | حالت ارائه شده توسط Windows/NVIDIA را برای آن نمایشگر برگردانید و آزمایش کنید. خطا را دقیق بخوانید و از تغییرات کور مکرر خودداری کنید. |
| HDR یا رنگ به حالت قبلی برمی گردد | بررسی کنید که آیا عملیات دیگری شکست خورده و بازیابی را آغاز کرده است. HDR را از ACM تشخیص دهید. |
| دکمه NVRasterPulse یک مسیر را رد می کند | میانبر خود را راه اندازی کنید. این دکمه نیاز به نصب محافظت شده در سراسر سیستم دارد. |
| تغییر پس از حذف باقی می ماند | نمایه NVIDIA صادر شده یا تنظیمات نمایش Windows مورد نظر را بازیابی کنید. حذف یک بازگشت تنظیمات نیست. |

قبل از ارسال گزارش به [راهنمایی پشتیبانی مشترک](../docs/support.md) مراجعه کنید.

<a id="faq"></a>
## سوالات متداول

**این نرم افزار رسمی NVIDIA است یا ساخت رسمی Orbmu2k؟** خیر. این یک fork مستقل است. نویسنده بالادستی و مجوز MIT همچنان اعتبار دارند.

**آیا NVDriverForge به این ویرایشگر نیاز دارد؟** خیر. از پیش تنظیم اختیاری Custom NV NVDriverForge از یکپارچه سازی خود استفاده می کند. نصب ویرایشگر یک انتخاب جداگانه است.

** هست RTSS برای این امر اجباری است fork?** نه. RTSS برای اجباری است NVRasterPulse's FPS محدود کننده، نه برای ویرایش نمایه یا صفحه.

**منبع کجاست؟** منبع برنامه اصلاح شده به صورت خصوصی نگهداری می شود. اطلاعیه MIT و مخزن بالادستی ارائه شده است. MIT نیازی به انتشار منبع اصلاح شده ندارد.

<a id="upstream-and-changes"></a>
## بالادست و تغییرات

بالادست: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector)، مرجع `592d962cca8827efe8859461a84267755595064a`. [دانلودهای اصلی](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

ارثی: ویرایشگر نمایه، NVAPI interop، داده های مرجع، منابع و مضامین UI. 禅堂 Zendo (RevoluSound Team) خدمات نمایش اضافه یا تطبیق داده شده، تراکنش‌های HDR/ICC، تأیید/خواندن 15 ثانیه، طرح‌بندی نوار ابزار و رفتار راه‌اندازی RasterPulse. همراه پاک شده، نقاط ورود ساختگی/آزمایشی را حذف نمی‌کند، از یک راه‌انداز خارجی محافظت‌شده استفاده می‌کند و یک نصب‌کننده جداگانه ارائه می‌کند. بسته توسعه ترکیبی قدیمی NVPI/RasterPulse کاندیدای این هاب نیست.

[منشأ پرونده تفصیلی](../docs/provenance.md) · [اعلامیه اصلی fork](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## اعتبار و مجوز

حق چاپ (ج) 2016 Orbmu2k. [مجوز MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) ارائه شده حفظ می شود. سازگاری ها و بسته بندی: 禅堂 Zendo (RevoluSound Team). نصب کننده از Inno Setup استفاده می کند. Windows و .NET Framework خارجی باقی می مانند. [اطلاعیه های قابل اجرا کامل](LICENSES/README.md).

مستقل از، توسط NVIDIA Corporation حمایت نشده و به طور رسمی تایید نشده است. علائم تجاری نزد صاحبان مربوطه باقی می ماند.

</div>
