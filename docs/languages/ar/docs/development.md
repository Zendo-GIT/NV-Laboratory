<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

**العربية** · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> الترجمة بمساعدة الآلة من الإنجليزية. يتم الاحتفاظ بالأسماء التقنية والأوامر وعناوين URL والنصوص القانونية الأصلية. نرحب بمراجعة المتحدث الأصلي. راجع المرجع الإنجليزي إذا كانت الصياغة غير واضحة.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="repository-architecture-and-maintenance"></a>
# بنية المستودع وصيانته

NV Laboratory هو مركز عام للتوثيق والتوزيع الثنائي. لا يحتوي على مصدر التطبيق. تحتفظ المشاريع الأربعة بأشجار بناء وإصدارات وهويات وأصول إصدار منفصلة. لا يتم استيراد تاريخ التطوير الخاص بهم إلى مستودع Git هذا.

<a id="layout"></a>
## التخطيط

| الموقع | الغرض |
| --- | --- |
| README.md / README.fr.md | نقاط الدخول الإنجليزية/الفرنسية |
| أربعة مجلدات المشروع | الأدلة الكاملة والإشعارات الأصلية المعمول بها |
| مستندات | إجراءات التنزيل والتوافق والمصدر والتطوير والإصدار |
| مستندات/releases.json | البيانات الوصفية والأحجام والتجزئة التي تم تدقيقها للمرشح/الإصدار |
| المستندات/المصدر | مقارنات الملفات/التجزئة؛ لا يوجد رمز التطبيق |
| التراخيص | تمت مشاركة نصوص الطرف الثالث الكاملة واعتمادات المترجم المثبت |
| الأصول | معاينات واجهة المستخدم الحالية التي تمت مراجعتها ومصدرها |
| .جيثب | إصدار النماذج والتحقق من صحة الوثائق للقراءة فقط |
| أدوات/validate_repository.py | حدود النشر والارتباطات في المكتبة القياسية |

تظل اللغة الإنجليزية هي الملف التمهيدي الافتراضي لـ GitHub. تظل روابط `.fr.md` المجاورة الحالية صالحة. تعكس الترجمات الإضافية الوثائق الموجودة تحت `docs/languages/<code>`؛ يحتفظ محدد اللغة بنفس الصفحة عند تبديل اللغات. يسجل كتالوج `docs/languages/catalog.json` جميع اللغات الـ 34 وبصمات الأصابع المصدر. لا يقوم GitHub تلقائيًا بتحديد ملف README حسب لغة المتصفح. انظر [فهرس اللغة وسياسة الترجمة](../../README.md).

<a id="application-technologies"></a>
## تقنيات التطبيق

| البرنامج | التكنولوجيا الخاصة | التوزيع |
| --- | --- | --- |
| NVPI fork | C#، WPF، .NET Framework 4.8، NVAPI/Windows | استكمال المجلد المحمول وفصل Inno Setup |
| NVDriverForge | C#، WPF، .NET 8؛ تمهيد C++ الأصلي؛ عملية 7-Zip | EXE المحمول القائم بذاته والإعداد |
| NVMFG Unlock40 | C#/WPF .NET 8، مساعدي Framework 4.8، محرك C++20/MASM/MinHook | الشجرة المحمولة والإعداد |
| NVRasterPulse | إطار عمل C#/WPF 4.8; ملف تعريف RTSS/تكامل إعادة التحميل؛ التمهيد الأصلي | الشجرة المحمولة والإعداد |

لا يمكن لهذا الخروج العام إعادة بناء التطبيقات. تعتبر أرشيفات "Source code" التلقائية بمثابة لقطات مركزية. لا تمثل روابط المصدر الأولية المصدر الخاص المعدل بالضبط. يتحقق CI العام من صحة هذا المستودع فقط.

<a id="local-checks"></a>
## الشيكات المحلية

من جذر المستودع:

```text
python tools/validate_repository.py
```

Python 3.10 أو الأحدث يكفي. يقرأ الفحص الملفات وروابط Markdown المحلية والإشعارات المطلوبة/روابط RTSS وبيانات تعريف الإصدار وحدود النشر. ولا يقوم بتنفيذ البرنامج أو تثبيت التبعيات أو الاتصال بالشبكة.

يقوم سير العمل GitHub بتشغيل هذا الفحص نفسه مع إذن المحتويات للقراءة فقط عند الدفع أو طلب السحب أو الإرسال اليدوي. يتم تثبيت Checkout على التزام مدقق ولا يحتفظ ببيانات الاعتماد. لم يتم تكوين أي مهمة إصدار أو نشر.

<a id="maintain-the-boundary"></a>
## الحفاظ على الحدود

قم بتحديث المرجع الإنجليزي والأدلة الفرنسية والترجمات المتأثرة معًا. احتفظ بالتغييرات الجوهرية منفصلة عن مقارنات التنسيق فقط. تسجيل تجزئات المرشح الفعلية، ومراجع الالتزام الأولية والتراخيص؛ لا تستنتج أبدًا الترخيص من شعبية المشروع.

استخدم أصول الإصدار الحديثة وأعد تدقيق الثنائيات والأرشيفات والإشعارات المضمنة التي تم تغييرها. احتفظ بنسخ احتياطية خاصة خارج هذا المستودع. لا تستخدم سير عمل عام لاستيراد مصدر التطبيق الخاص أو مجلدات البناء المحلية.

يتم تشغيل الاختبارات المناسبة لتغيير التطبيق الوظيفي في المشروع الخاص. لا تقم بإعادة تشغيل برامج التثبيت أو كتابة ملفات تعريف حقيقية لتحديث الوثائق. [إجراء الإصدار اليدوي](releasing.md).

</div>
