<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

**العربية** · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> الترجمة بمساعدة الآلة من الإنجليزية. يتم الاحتفاظ بالأسماء التقنية والأوامر وعناوين URL والنصوص القانونية الأصلية. نرحب بمراجعة المتحدث الأصلي. راجع المرجع الإنجليزي إذا كانت الصياغة غير واضحة.
<!-- nv-translation-notice:end -->

<div dir="rtl">

<a id="publishing-and-releases"></a>
# النشر والإصدارات

المستودع العام هو **Zendo-GIT/NV-Laboratory**. تتم مراجعة تغييرات التوثيق والالتزام بها ودفعها بواسطة المشرف باستخدام **GitHub Desktop**. الالتزام المحلي لا يقوم بتحميل الملفات. الحزم الثنائية هي أصول إصدار GitHub منفصلة؛ لا ينتمون أبدًا إلى قائمة تغييرات Git.

<a id="documentation-updates"></a>
## تحديثات التوثيق

1. افتح المجلد **NV-Laboratory** في GitHub Desktop.
2. قم بمراجعة الوثائق والإشعارات والصور والبيانات التعريفية لـ JSON ومدقق التوثيق.
3. قم بتشغيل `python tools/validate_repository.py` من هذا المجلد.
4. قم بإجراء التغييرات التي تمت مراجعتها، ثم استخدم **Push origin**. التحقق من نتيجة الإجراءات.
5. احتفظ بهوية المؤلف العامة **禅堂 Zendo (RevoluSound Team)** وعنوان GitHub `noreply` للحساب.

لا تقم مطلقًا بتحديد مساحة عمل التطوير الأصلي أو دليل التدقيق الخاص أو دليل المرفقات الثنائية. [الالتزام بخصوصية البريد الإلكتروني](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## إصدارات التطبيقات المستقلة

| أداة | علامة | سياسة الإصدار |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | إصدار التطبيق الحالي المكون من أربعة أجزاء؛ مراجعة الإعداد 2 لها اسم ملف خاص بها |
| NVDriverForge | nvdriverforge-v0.1.4 | مخطط 0.x الموجود؛ تحافظ التحديثات ذات الإصدار على الحزم السابقة |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | إصدار التطبيق 0.2.3؛ التغييرات التراكمية منذ 0.1.1 العام |
| NVRasterPulse | nvrasterpulse-v0.2 | النسخة الموجودة من جزأين |

يمكن للمشرف النشر مباشرة أو تفويض مساعد لنشر الأصول التي تم تدقيقها. النشر صريح؛ لا يوجد سير عمل ينشئ إصدارًا عند كل التزام.

1. قم بمراجعة تقرير النشر المسبق الحالي ومصادر الثنائيات والتراخيص وقيم SHA-256.
2. أنشئ مسودة لعلامة الأداة، مستهدفة التزام المركز الذي تمت مراجعته. قم بتضمين ملاحظات الإصدار المعدة مسبقًا الخاصة بالإصدار.
3. أرفق فقط أصول الإعداد/المحمولة لهذا الإصدار، `Licenses-and-Credits.zip` و`SHA256SUMS.txt`.
4. تحقق من التوافق والتثبيت والتبعيات والتغييرات والحدود المعروفة. أبقِ RTSS بارزًا في NVRasterPulse.
5. قم بالنشر والتحقق من عناوين URL للأصول العامة وأحجامها وتجزئةها، ثم قم بتسجيل تاريخ النشر الفعلي في `docs/releases.json`.
6. قم بتحديث صفحات التنزيل والترجمات، ثم قم بتنفيذ/دفع التغييرات في GitHub Desktop.

تتجنب روابط علامات كل مشروع إرسال المستخدمين إلى أداة أخرى من خلال رابط `releases/latest` مشترك. تحتوي أرشيفات GitHub التلقائية **Source code** على مركز التوثيق هذا. تبقى مصادر التطبيق خاصة. تظل إشعارات المكونات الأصلية سليمة، ولا يحل الإصدار احتياطي NVMFG الموثق NVIDIA SDK.


يقوم تحديث 18 سبتمبر بإعداد ثلاث علامات جديدة؛ يبقى إصدار Profile Inspector الحالي دون تغيير. يجب أن تظل أسماء الأصول والعلامات و`SHA256SUMS.txt` دقيقة لعمليات التحقق من تحديث التطبيق. نشر الإصدارات العادية بدون علامة الإصدار التجريبي لتعريضها لعمليات فحص الإصدار المستقر؛ يظل NVMFG تجريبيًا.

<a id="integrity-and-storage"></a>
## النزاهة والتخزين

لا تقم مطلقًا باستبدال وحدات البايت الثنائية المنشورة بصمت. استخدم إصدارًا صريحًا جديدًا أو مراجعة المثبت مع تجزئات جديدة. تكمل السيارات الجانبية القانونية الإشعارات المضمنة. يبلغ حجم NVDriverForge 0.1.4 المحمول 142,017,891 بايت، وهو أعلى من الحد العادي لملف Git الذي يبلغ 100 ميجابايت في GitHub. تتجنب مرفقات الإصدار وضع الثنائيات أو Git LFS في هذا المحور. [GitHub توجيه الملفات الكبيرة](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

يجب تمكين الإبلاغ عن الثغرات الأمنية الخاصة في إعدادات أمان المستودع. التحقق من توفرها قبل توجيه التقارير الحساسة إليها؛ يوفر [SECURITY.md](../SECURITY.md) حلاً احتياطيًا لا يكشف عن تفاصيل الثغرة الأمنية.

[تحميل الكتالوج](downloads.md) · [وثائق إصدار GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

</div>
