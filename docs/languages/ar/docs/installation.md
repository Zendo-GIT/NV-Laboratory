<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

**العربية** · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> الترجمة بمساعدة الآلة من الإنجليزية. يتم الاحتفاظ بالأسماء التقنية والأوامر وعناوين URL والنصوص القانونية الأصلية. نرحب بمراجعة المتحدث الأصلي. راجع المرجع الإنجليزي إذا كانت الصياغة غير واضحة.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="installation-guide"></a>
# دليل التثبيت

ابدأ بـ [التنزيلات](downloads.md)، الذي يسجل حالة النشر وأسماء الأصول الدقيقة. هذه أدوات منفصلة: قم بتثبيت الأدوات التي تحتاجها فقط.

> **بالنسبة لـ NVRasterPulse، قم بتثبيت [RTSS من Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) قبل فتح مدير الملفات الشخصية.**
> يجب تشغيل RTSS لتطبيق الحدود؛ لم يتم تضمينه في NV Tools.

| أداة | الطبعة المثبتة | طبعة محمولة | الشرط الرئيسي |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | قم باستخراج NVPI ZIP بالكامل | برنامج تشغيل NVIDIA و.NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe، يتضمن وقت التشغيل | حزمة برنامج التشغيل NVIDIA الأصلية المتوافقة لعمليات التثبيت |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | قم باستخراج NVMFG ZIP بالكامل، واحتفظ بالمجلدات الفرعية | RTX 40، DLSS FG الحالي، الموفر الدقيق ومساعدي .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | قم باستخراج RP ZIP بالكامل | RTSS و.NET Framework 4.8 |

<a id="download-verify-install"></a>
## التنزيل والتحقق والتثبيت

1. في الإصدار المنشور المختار، قم بتنزيل أصول التطبيق المسماة، والإشعارات ZIP وSHA256SUMS.txt.
2. استخدم [مثال SHA-256](downloads.md#sha-256)، مع اسم الملف الفعلي الذي تم تنزيله.
3. للإعداد، اتبع المثبت العادي. بالنسبة إلى ملف ZIP المحمول، قم باستخراج كل شيء إلى مجلد محلي جديد قابل للكتابة؛ لا تقم بتشغيل من داخل ZIP.
4. افتح ملف EXE الخاص بالتطبيق. احتفظ بملفات الترخيص/التكوين/البيانات المصاحبة.
5. اقرأ تعليمات استخدام هذه الأداة قبل تمكين الإعدادات أو عمليات النظام.

الثنائيات الحالية غير موقعة. تؤكد التجزئة المطابقة البايتات المتوقعة؛ وهي ليست شهادة أمان أو توافق. لا تقم بتعطيل الحماية الأمنية Windows فقط لمنع التحذير.

يعد تثبيت NVDF أو المرافق الاختياري NVPI منفصلاً عن تثبيت برنامج التشغيل GPU. يحتفظ البرنامج المرافق NVPI باسم التثبيت الداخلي الحالي الخاص به. يتطلب زر RasterPulse المرتفع تثبيتًا محميًا على مستوى النظام؛ يمكن فتح نسخ RP الأخرى من خلال الاختصارات الخاصة بها.

NVMFG تجريبي ولديه [احتياطي ترخيص NVIDIA SDK الموثق](provenance.md). لا يتم تضمين برنامج تشغيل NVIDIA أو موفر/طراز NGX أو وقت تشغيل اللعبة Streamline. تعتبر تنزيلات SDK المحددة وتحديثات اللعبة بمثابة عمليات منفصلة صريحة.

<a id="language-and-updates"></a>
## اللغة والتحديثات

استخدم محدد اللغة الخاص بـ README المكون من 34 لغة للتوثيق. تتمتع NVDF وNVMFG وRP بإعدادات واجهة مستخدم خاصة بها مكونة من 34 لغة؛ يحتفظ NVPI بدعم اللغة الحالي. تعود بعض السلاسل الفنية لبرنامج التثبيت إلى اللغة الإنجليزية.

احتفظ بهوية تثبيت الأداة عند التحديث. أغلقه أولاً واحتفظ بالنسخ الاحتياطية. بالنسبة إلى NVMFG، أغلق الألعاب المتأثرة وحل مشكلة استرداد الملف الشخصي المعلقة. بالنسبة للتحديثات المحمولة، استخدم مجلدًا جديدًا بدلاً من دمج الإصدارات.

<a id="removing-a-tool"></a>
## إزالة أداة

لا تؤدي إزالة تثبيت أحد التطبيقات إلى التراجع عن إعداداته تلقائيًا.

- **NVPI:** قم باستعادة ملفات التعريف/إعدادات العرض المقصودة قبل الإزالة إذا لزم الأمر.
- **NVDF:** استخدم الاسترداد أولاً إذا كنت تريد استعادة التغييرات المتقدمة/NVENC. يترك Uninstall برنامج تشغيل الرسومات والإعدادات والنسخ الاحتياطية.
- **NVMFG:** أغلق الألعاب، وقم بتعطيل/إنهاء وحدة التحكم، وحل استرداد NVIDIA واستعادة النسخ الاحتياطية للعبة SDK المطلوبة قبل الإزالة.
- **RP:** قم بإزالة تجاوزات المحدد المقصود أولاً. لا يقوم Uninstall بمسح أحرف RTSS المحفوظة أو إزالة RTSS.

راجع كل [دليل المشروع](../README.md#projects) لمعرفة مواقع البيانات والقيود الدقيقة، أو [الدعم](support.md) إذا فشلت خطوة الاسترداد.

</div>
