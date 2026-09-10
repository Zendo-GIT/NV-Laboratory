<!-- nv-language-navigation:start -->
🌐 [English](../../../SECURITY.md) | [Français](../fr/SECURITY.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/SECURITY.md) · **বাংলা** · [简体中文](../zh/SECURITY.md) · [Čeština](../cs/SECURITY.md) · [Dansk](../da/SECURITY.md) · [Nederlands](../nl/SECURITY.md) · [English](../../../SECURITY.md) · [Filipino](../fil/SECURITY.md) · [Suomi](../fi/SECURITY.md) · [Français](../fr/SECURITY.md) · [Deutsch](../de/SECURITY.md) · [Ελληνικά](../el/SECURITY.md) · [हिन्दी](../hi/SECURITY.md) · [Magyar](../hu/SECURITY.md) · [Bahasa Indonesia](../id/SECURITY.md) · [Italiano](../it/SECURITY.md) · [日本語](../ja/SECURITY.md) · [한국어](../ko/SECURITY.md) · [मराठी](../mr/SECURITY.md) · [فارسی](../fa/SECURITY.md) · [Polski](../pl/SECURITY.md) · [Português](../pt/SECURITY.md) · [ਪੰਜਾਬੀ](../pa/SECURITY.md) · [Română](../ro/SECURITY.md) · [Русский](../ru/SECURITY.md) · [Español](../es/SECURITY.md) · [Kiswahili](../sw/SECURITY.md) · [Svenska](../sv/SECURITY.md) · [தமிழ்](../ta/SECURITY.md) · [ไทย](../th/SECURITY.md) · [Türkçe](../tr/SECURITY.md) · [Українська](../uk/SECURITY.md) · [اردو](../ur/SECURITY.md) · [Tiếng Việt](../vi/SECURITY.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ইংরেজি থেকে মেশিন-সহায়তা অনুবাদ। প্রযুক্তিগত নাম, কমান্ড, URL এবং মূল আইনি পাঠ্য সংরক্ষিত আছে। নেটিভ-স্পিকার পর্যালোচনা স্বাগত; শব্দ অস্পষ্ট হলে ইংরেজি রেফারেন্সের সাথে পরামর্শ করুন।
<!-- nv-translation-notice:end -->

<a id="security"></a>
# নিরাপত্তা

এই নীতি NV Tools অ্যাপ্লিকেশন প্যাকেজ এবং এই বিতরণ হাব কভার করে। রক্ষণাবেক্ষণকারী প্রতিটি টুলের সর্বশেষ প্রকাশিত সংস্করণকে প্রভাবিত করে এমন প্রতিবেদনগুলিকে অগ্রাধিকার দেয়। প্রস্তুত প্রার্থী একটি ঘোষিত সমর্থিত স্থিতিশীল মুক্তি নয়. কোন প্রতিক্রিয়ার সময়সীমা বা নিরাপত্তা শংসাপত্রের প্রতিশ্রুতি নেই।

<a id="report-privately"></a>
## ব্যক্তিগতভাবে রিপোর্ট করুন

দুর্বলতা, অনিরাপদ উন্নত আচরণ, অনিচ্ছাকৃত ধ্বংসাত্মক পরিবর্তন বা সংবেদনশীল ডেটা এক্সপোজারের জন্য, সংগ্রহস্থলের **নিরাপত্তা → Report a vulnerability** বৈশিষ্ট্য **যখন এটি সক্রিয় থাকে**: [ব্যক্তিগত রিপোর্ট](https://github.com/Zendo-GIT/NV-Laboratory/security/advisories/new) ব্যবহার করুন।

**প্রাথমিক সেটআপ:** রক্ষণাবেক্ষণকারীকে অবশ্যই পাবলিক রিপোজিটরি তৈরি করার পরে ব্যক্তিগত দুর্বলতা রিপোর্টিং সক্ষম করতে হবে। এই ফাইলটি এটি সক্ষম করে না, এবং এর আগে কোনও মেলবক্স বা ব্যক্তিগত চ্যানেলের অস্তিত্ব দাবি করা হয়নি৷

বোতামটি অনুপলব্ধ হলে, শুধুমাত্র একটি পাবলিক ইস্যু খুলুন: "[টুল/সংস্করণ] সম্পর্কিত নিরাপত্তা প্রতিবেদনের জন্য আমার একটি ব্যক্তিগত যোগাযোগের চ্যানেল দরকার।" শোষণের বিবরণ, শংসাপত্র, প্রভাবিত পথ, লগ বা সংযুক্তি অন্তর্ভুক্ত করবেন না। সেগুলি ভাগ করার আগে রক্ষণাবেক্ষণকারী একটি ব্যক্তিগত চ্যানেল সরবরাহ করার জন্য অপেক্ষা করুন৷

ব্যক্তিগত প্রতিবেদনে, টুল/সংস্করণ এবং হ্যাশ, Windows/GPU/ড্রাইভার সংস্করণ, প্রভাব, ন্যূনতম নিরাপদ প্রজনন এবং পুনরুদ্ধারের প্রয়োজন আছে কিনা তা অন্তর্ভুক্ত করুন। গোপনীয়তা এবং ব্যক্তিগত তথ্য সংশোধন; স্থানীয় পুনরুদ্ধার ফাইল সংরক্ষণ করুন। মালিকানাধীন ড্রাইভার বা গেম DLL আপলোড করবেন না। রক্ষণাবেক্ষণকারীর সাথে সমন্বিত প্রকাশ; একটি প্যাচ/রিলিজের জন্য পর্যালোচনা প্রয়োজন এবং এটি স্বয়ংক্রিয় নয়।


[GitHub ব্যক্তিগত রিপোর্টিং ডকুমেন্টেশন](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
