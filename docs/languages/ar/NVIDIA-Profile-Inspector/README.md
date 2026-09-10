<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

**العربية** · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> الترجمة بمساعدة الآلة من الإنجليزية. يتم الاحتفاظ بالأسماء التقنية والأوامر وعناوين URL والنصوص القانونية الأصلية. نرحب بمراجعة المتحدث الأصلي. راجع المرجع الإنجليزي إذا كانت الصياغة غير واضحة.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

** fork مستقل عن [NVIDIA Profile Inspector بواسطة Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector)، مع عناصر تحكم إضافية في العرض. ** اسم المشروع السابق: **NVPI Custom**.

[حالة التنزيل والإصدار](../docs/downloads.md#nvidia-profile-inspector) · [التثبيت](#installation) · [المنبع والتغيرات](#upstream-and-changes) · [الترخيص](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## نظرة عامة

يقوم التطبيق بتحرير ملفات تعريف برنامج التشغيل NVIDIA، بما في ذلك الإعدادات الخاصة بكل تطبيق. يضيف fork أيضًا محرر **شاشة** لشاشة Windows النشطة: الدقة ومعدل التحديث وإعدادات ألوان الإخراج وHDR وارتباطات ملفات تعريف ICC/WCS المثبتة.

إنه موجود لجلب عناصر التحكم في العرض ذات الصلة إلى محرر ملف التعريف ولجعل نتائج المعاينة والتأكيد والاستعادة أكثر وضوحًا. لا ينشئ قدرات الأجهزة الجديدة.

المرشح الأول هو **3.0.2.3**، باستخدام الإصدار المصاحب المستقل المنظف اعتبارًا من 9 سبتمبر 2026. ويظل الملف القابل للتنفيذ الحالي هو `nvidiaProfileInspector.exe`؛ لا يزال برنامج التثبيت وبعض الملصقات الداخلية مكتوبًا بـ `NVPI Custom NV`. يحدد العنوان العام أعلاه fork دون تغيير هوية التثبيت أو التظاهر بأنه الإصدار الرسمي لـ Orbmu2k.

<a id="features"></a>
## الميزات

- تصفح الملف الشخصي الحالي، وارتباطات التطبيق، وإعدادات التحرير واستيراد/تصدير الملف الشخصي.
- **شاشة** مربع حوار للعرض والوضع والهرتز وRGB/YCbCr وعمق الألوان والنطاق وقياس الألوان.
- التحكم Windows HDR وتثبيت اختيار اقتران ICC/WCS.
- معاينة عرض مدتها 15 ثانية مع **Keep** / **Revert** واستعادة المهلة.
- إعادة قراءة تغييرات الوضع/HDR والإبلاغ عن حالات فشل الاستعادة.
- تقارير منفصلة عن HDR وSDR مع ACM/WCG وعمق ألوان الإشارة.
- مشغل NVRasterPulse للحصول على نسخة مؤهلة مثبتة بشكل منفصل.

<a id="compatibility"></a>
## التوافق

| المتطلبات | التفاصيل |
| --- | --- |
| النظام | Windows 10/11 x64 مع برنامج تشغيل NVIDIA متوافق |
| وقت التشغيل | [إطار عمل صافي 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)، يتم توفيره بواسطة Windows أو يتم تثبيته بشكل منفصل |
| الأذونات | يطلب المحرر وصول المسؤول عند فتحه |
| يعرض | تعتمد الأوضاع الفعلية ومجموعات الألوان على GPU وبرنامج التشغيل والشاشة والكابل وواجهات برمجة التطبيقات Windows |
| أدوات اختيارية | NVRasterPulse لإدارة الحدود RTSS؛ ليست هناك حاجة إليه ولا RTSS لمحرر الشاشة |
| اللغات | الإعداد: محدد 34 لغة. يحتفظ المحرر بدعم اللغة الحالي. |

لا يوجد حد أدنى لبرنامج التشغيل العالمي أو مصفوفة دعم تم التحقق منها لكل GPU. إن اختيارات bpc المتوفرة في مربع الحوار هي طلبات، وليست مجموعات معتمدة. تتمتع عناصر التحكم HDR الحديثة والاحتياطي الأقدم Windows بقدرات مختلفة.

<a id="installation"></a>
## التثبيت

1. افتح [صفحة التحميل](../docs/downloads.md#nvidia-profile-inspector) وتحقق من حالة النشر.
2. قم بتنزيل برنامج الإعداد أو الأصل المحمول وقارن SHA-256 ببيان الإصدار.
3. للإعداد، قم بتشغيل `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`، وحدد لغة واتبع برنامج التثبيت. يقوم بإنشاء الاختصار وإلغاء التثبيت الخاص به.
4. بالنسبة للأجهزة المحمولة، قم باستخراج ملف ZIP الكامل إلى مجلد جديد قابل للكتابة. احتفظ بـ `Reference.xml` وتكوين EXE وجميع الإشعارات بجانب الملف القابل للتنفيذ.
5. إطلاق `nvidiaProfileInspector.exe`.

لا يؤدي تثبيت المحرر وحده إلى تطبيق ملف تعريف أو تثبيت برنامج تشغيل GPU. يتم تثبيت البرنامج المصاحب بشكل منفصل، ولا يتولى عمليات اقترانات `.nip` ولا يقوم بتمكين بدء التشغيل عند تسجيل الدخول. الثنائيات الموجودة غير موقعة.

<a id="usage"></a>
## الاستخدام

**تضيف مراجعة المثبت 2** نفس أداة التحديد الأصلية المكونة من 34 لغة مثل الأدوات الأخرى، مع التنقل بالماوس/لوحة المفاتيح، والمظهر الفاتح/الداكن والإلغاء. ينطبق الاختيار على الإعداد؛ ولا يترجم محرر NVPI. تتجاوز وسيطة `/LANG=fr` الصريحة أو الوضع الصامت التحديد للمتصلين الذين يوفرون لغة بالفعل.

**ملفات تعريف السائق:** حدد ملف تعريف، وقم بتصدير نسخة احتياطية، ثم قم بتحرير الإعدادات المقصودة فقط وتطبيقها. تحدد جمعيات التطبيقات اللعبة التي تتلقى ملف تعريف. القيمة المخزنة ليست دليلاً على أن كل برنامج تشغيل أو لعبة تستخدمها.

**عناصر التحكم في العرض:** افتح **الشاشة**، واختر العرض والقيم المطلوبة، ثم ابدأ المعاينة. تحقق من الصورة قبل اختيار **الاحتفاظ بها** خلال 15 ثانية. استخدم **الرجوع**، وأغلق التأكيد أو اتركه حتى تنتهي صلاحيته لطلب الاستعادة. اقرأ أي رسالة فشل: استدعاء واجهة برمجة التطبيقات (API) الناجح وحده ليس دليلاً على الاستعادة.

يؤدي تحديد ICC إلى تغيير اقتران ملف التعريف المثبت؛ ولا يقوم بإنشاء ملف ICC أو معايرته أو إعادة توزيعه. تصف HDR وACM/WCG وRGB/YCbCr وbpc الجوانب المختلفة لخط الأنابيب. لم يتم توفير مفتاح ACM مستقل جديد.

**NVRasterPulse:** يقبل زر شريط الأدوات التثبيت المسجل بشكل منفصل على مستوى النظام أسفل ملفات البرامج مع الملكية والأذونات المحمية. قد يتم رفض نسخة محمولة أو مسار قابل للكتابة/مرتبط بواسطة المستخدم بواسطة هذا المشغل المرتفع. في هذه الحالة، افتح NVRasterPulse باستخدام الاختصار الخاص به. [قم بتثبيت RTSS بشكل منفصل](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) لاستخدام NVRasterPulse.

<a id="screenshots"></a>
## لقطات الشاشة

![مراجعة إعداد NVPI مع محدد لغة 2](../../../../assets/screenshots/nvpi-setup-r2-language.png)

محدد الإعداد الفعلي باللغة الفرنسية، تم التقاطه أثناء اختبار معزول ثم تم إلغاؤه. يظهر هذا المثبت. يحتفظ المحرر بواجهته ومربع حوار الشاشة.

<a id="update-and-uninstall"></a>
## تحديث وإلغاء التثبيت

أغلق المحرر قبل التحديث. احتفظ بالملفات الشخصية التي تم تصديرها وقم بتنزيل إصدار fork الجديد؛ التثبيت على نفس الهوية المصاحبة أو استخراج الملفات المحمولة إلى مجلد جديد. لا تخلط `Reference.xml` القديم مع ملف جديد قابل للتنفيذ. ينتمي منع التحقق من التحديث المنبع المجمع إلى fork.

للحصول على نسخة مثبتة، استخدم Windows Installed apps وأداة إلغاء التثبيت الخاصة به. بالنسبة للملف المحمول، أغلقه وأزل المجلد المستخرج عندما تكون عمليات التصدير الخاصة بك آمنة. لا تؤدي إزالة المحرر إلى التراجع عن تعديلات ملف تعريف السائق أو تفضيلات العرض أو NVRasterPulse أو RTSS. استعادة الإعدادات المطلوبة قبل الإزالة.

<a id="known-limitations"></a>
## القيود المعروفة

- التأكيد لمدة 15 ثانية ليس بمثابة رقابة على كل حادث تصادم للسائق، أو فقدان الطاقة، أو الإغلاق القسري.
- تُرجع بعض مجموعات الألوان/العمق/التحديث `NVAPI_NOT_SUPPORTED`.
- لا تقيس إعادة قراءة البرنامج عمق بت اللوحة أو دقة الألوان أو زمن الوصول.
- تؤثر إعدادات الشاشة على شاشة Windows الحالية؛ لا يؤدي مربع الحوار هذا إلى إنشاء إعدادات عرض مسبقة لكل لعبة.
- لا يوجد ضمان للأداء أو مكافحة الغش أو التوافق العالمي مع HDR.

<a id="troubleshooting"></a>
## استكشاف الأخطاء وإصلاحها

| أعراض | العمل |
| --- | --- |
| خطأ في وقت التشغيل عند الإطلاق | تحقق من تحديثات Windows و.NET Framework 4.8؛ استخدم الحزمة الكاملة. |
| تم رفض وضع العرض المطلوب | قم بالرجوع واختبار الوضع المقدم بواسطة Windows/NVIDIA لهذا العرض. اقرأ الخطأ الدقيق وتجنب التغييرات العمياء المتكررة. |
| HDR أو يعود اللون إلى حالته القديمة | التحقق مما إذا كانت عملية أخرى قد فشلت وتسببت في الاستعادة؛ يميز HDR عن ACM. |
| زر NVRasterPulse يرفض المسار | إطلاق الاختصار الخاص به؛ يتطلب هذا الزر تثبيتًا محميًا على مستوى النظام. |
| يبقى التغيير بعد إلغاء التثبيت | استعادة ملف تعريف NVIDIA الذي تم تصديره أو إعدادات العرض Windows المقصودة؛ إلغاء التثبيت ليس التراجع عن الإعدادات. |

راجع [إرشادات الدعم المشترك](../docs/support.md) قبل إرسال السجلات.

<a id="faq"></a>
## الأسئلة الشائعة

**هل هذا البرنامج الرسمي NVIDIA أم الإصدار الرسمي لـ Orbmu2k؟** لا. إنه fork مستقل؛ ويظل المؤلف الرئيسي وترخيص MIT مسجلين.

**هل يتطلب NVDriverForge هذا المحرر؟** لا. يستخدم الإعداد المسبق الاختياري NVDriverForge الخاص بـ Custom NV التكامل الخاص به. يعد تثبيت المحرر خيارًا منفصلاً.

**هل RTSS إلزامي لـ fork هذا؟** لا. RTSS إلزامي لمحدد NVRasterPulse's FPS، وليس لتحرير الملف الشخصي أو الشاشة.

**أين المصدر؟** يتم الاحتفاظ بمصدر التطبيق المعدل بشكل خاص. يتم توفير إشعار MIT والمستودع الأولي؛ لا يتطلب MIT نشر المصدر المعدل.

<a id="upstream-and-changes"></a>
## المنبع والتغيرات

المنبع: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector)، الالتزام المرجعي `592d962cca8827efe8859461a84267755595064a`. [التنزيلات الأصلية](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

موروث: محرر الملف الشخصي، التشغيل المتداخل NVAPI، البيانات المرجعية، موارد واجهة المستخدم والموضوعات. قام 禅堂 Zendo (RevoluSound Team) بإضافة أو تعديل خدمات العرض، ومعاملات HDR/ICC، والتأكيد/القراءة الخلفية لمدة 15 ثانية، وتخطيط شريط الأدوات، وسلوك تشغيل RasterPulse. يستبعد الرفيق الذي تم تنظيفه نماذج التطوير/نقاط دخول الاختبار، ويستخدم مشغلًا خارجيًا محميًا ويوفر أداة تثبيت منفصلة. حزمة التطوير القديمة المدمجة NVPI/RasterPulse ليست المرشحة في هذا المركز.

[مصدر الملف التفصيلي](../docs/provenance.md) · [إشعار fork الأصلي](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## الاعتمادات والترخيص

حقوق الطبع والنشر (ج) 2016 Orbmu2k. يتم الاحتفاظ بـ [ترخيص MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) المرفق. التكيفات والتعبئة والتغليف: 禅堂 Zendo (RevoluSound Team). يستخدم المثبت Inno Setup؛ يظل Windows و.NET Framework خارجيين. [الإشعارات المعمول بها كاملة](LICENSES/README.md).

مستقلة عن NVIDIA Corporation ولا ترعاها ولا تعتمدها رسميًا. تبقى العلامات التجارية مع أصحابها.

</div>
