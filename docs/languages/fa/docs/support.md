<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · **فارسی** · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ترجمه ماشینی از انگلیسی. نام های فنی، دستورات، URL ها و متون قانونی اصلی حفظ می شوند. بررسی بومی زبان خوش آمدید. اگر جمله بندی نامشخص است به مرجع انگلیسی مراجعه کنید.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="compatibility-and-troubleshooting"></a>
# سازگاری و عیب یابی

اینها نامزدهای آماده شده هستند، نه یک ماتریس گواهی برای همه ترکیبات Windows، GPU، درایور و بازی.

| ابزار | Windows / زمان اجرا | سخت افزار / وابستگی خارجی | عملیات نیاز به مراقبت |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64، .NET Framework 4.8 | درایور/نمایشگر سازگار NVIDIA | نمایه می نویسد و پیش نمایش ها را نمایش می دهد |
| NVDriverForge 0.1.2 | Windows 10 ساخت 19041+ / 11 x64; NET/WPF گنجانده شده است | بسته درایور سازگار NVIDIA | نصب بالا، تنظیمات پیشرفته، اختیاری NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; شامل NET/WPF، راهنماهای Framework 4.8 | RTX 40، بازی واجد شرایط DLSS FG و ارائه دهنده پین شده | وصله داخلی درون بازی، ژورنال پروفایل جهانی، به‌روزرسانی‌های بازی SDK |
| NVRasterPulse 0.1 | Windows 10/11 x64، .NET Framework 4.8 | RTSS نصب شده است. دویدن برای کلاه | RTSS در هر نمایه اجرایی تغییر می کند |

پکیج ARM64 تهیه نشده است. در دسترس بودن Display/API و نسخه های قدیمی Windows می تواند ویژگی های فردی را محدود کند. حداقل نسخه جهانی NVIDIA یا RTSS اختراع نشده است. هش دقیق ارائه دهنده NVMFG در [منشأ](provenance.md) است.

<a id="before-reporting-a-bug"></a>
## قبل از گزارش یک اشکال

فایل اجرایی/نسخه ای را که باز کرده اید، شناسایی کنید. یک کپی نصب شده قبلی لزوماً نسخه یک ZIP تازه دانلود شده نیست. مراحل تولید مثل، نتیجه مورد انتظار و نتیجه واقعی را ثبت کنید. برای مشکلات رندر/محدود کردن، نسخه بازی، بازخوانی نمایشگر، وضعیت FG/V-Sync/VRR و هر محدود کننده یا پوشش دیگری را در نظر بگیرید.

از [فرم اشکال](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml) استفاده کنید. هرگز یک کل پوشه توسعه خصوصی، بایگانی درایور، مدل، DLL بازی، روگرفت رجیستری یا مجموعه گزارش بررسی نشده را پیوست نکنید.

| مشکل | اولین چک ها |
| --- | --- |
| نسخه برنامه اشتباه است | هویت EXE را تأیید کنید و هش را آزاد کنید. کپی قدیمی را قبل از تعویض ببندید. |
| خطای زمان اجرا/راه اندازی | Framework مورد نیاز 4.8 را نصب کنید یا همه زیرپوشه های قابل حمل ارائه شده را حفظ کنید. |
| UAC لغو شد | فقط عملیات مورد نظر را دوباره امتحان کنید. لغو نصب موفقیت آمیز نیست. |
| عدم تطابق هش/امضا | استفاده از آن نامزد را متوقف کنید و بایت های رسمی مورد انتظار را بدست آورید. |
| رنگ/حالت NVPI رد شد | برگردانید و از ترکیبی استفاده کنید که توسط نمایشگر/درایور واقعی پشتیبانی می‌شود. |
| پشتیبان گیری یا بازیابی NVDF شکست خورد | حفظ کار محافظت شده و RECOVERY.txt. ژورنال را پاک نکنید یا نوشته های متناقض را مجبور نکنید. |
| تنظیمات در انتظار NVMFG | بازیابی را با بازی های بسته، حفظ تغییرات از ابزارهای دیگر حل کنید. |
| درپوش RP هیچ تاثیری ندارد | RTSS را اجرا کنید، EXE بازی واقعی را شناسایی کنید، وضعیت هوک و محدودیت های رقابتی را بررسی کنید. |
| درپوش RP پس از برداشتن باقی می ماند | RTSS Global را بازرسی کنید. حذف تغییرات محدود کننده محلی فقط لغو می شود. |

<a id="logs-and-privacy"></a>
## گزارش‌ها و حریم خصوصی

| ابزار | داده های محلی برای بررسی، نه آپلود عمده |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; مشاغل محافظت شده `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; پشتیبان گیری از `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`؛ `Sessions` در کنار EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` زیر آن |
| NVPI | صادرات انتخابی شما و خطای نمایش داده شده؛ هیچ مسیر ثبت جهانی اختراع نشده است |

نام حساب‌ها، فهرست‌های اصلی، مسیرهای کتابخانه بازی، شناسه‌های دستگاه، نشانه‌ها و پنجره‌های نامرتبط را از متن/تصاویری که به اشتراک می‌گذارید حذف کنید. نسخه اصلی را برای بازیابی خصوصی نگه دارید. مسائل عمومی برای همه قابل مشاهده است.

برای آسیب‌پذیری، رفتار ممتاز خطرناک یا عملیات مخرب ناخواسته، به‌جای ارسال عمومی جزئیات، [SECURITY.md](../SECURITY.md) را دنبال کنید.

<a id="what-has-been-verified"></a>
## آنچه تایید شده است

برای آماده سازی هاب، اسکن بار استاتیک/زیپ/هش/فراداده و بررسی اسناد اجرا شد. آزمایش‌های ساخت/واحد/UI برنامه خصوصی موجود، شواهد تاریخی و دارای تاریخ هستند. هیچ نصب درایور، تغییر نمایشگر، عملیات زنده RTSS یا معیار بازی به عنوان بخشی از این آماده سازی انجام نشده است.

"کشف"، "نوشته شده"، "بارگذاری مجدد"، "قابلیت موجود" و "اندازه گیری شده در بازی" نتایج متفاوتی هستند. گزارش دهید که کدام یک را مشاهده کرده اید.

</div>
