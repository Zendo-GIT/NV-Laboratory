<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · **বাংলা** · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ইংরেজি থেকে মেশিন-সহায়তা অনুবাদ। প্রযুক্তিগত নাম, কমান্ড, URL এবং মূল আইনি পাঠ্য সংরক্ষিত আছে। নেটিভ-স্পিকার পর্যালোচনা স্বাগত; শব্দ অস্পষ্ট হলে ইংরেজি রেফারেন্সের সাথে পরামর্শ করুন।
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# ইনস্টলেশন গাইড

[ডাউনলোড](downloads.md) দিয়ে শুরু করুন, যা প্রকাশনার স্থিতি এবং সঠিক সম্পদের নাম রেকর্ড করে। এইগুলি পৃথক সরঞ্জাম: শুধুমাত্র আপনার প্রয়োজন একটি ইনস্টল করুন.

> **NVRasterPulse-এর জন্য, প্রোফাইল ম্যানেজার খোলার আগে [Guru3D থেকে RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) ইনস্টল করুন।**
> সীমা প্রয়োগ করতে RTSS চালাতে হবে; এটি NV Tools-এ অন্তর্ভুক্ত নয়।

| টুল | ইনস্টল করা সংস্করণ | পোর্টেবল সংস্করণ | প্রধান পূর্বশর্ত |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | সম্পূর্ণ NVPI জিপ বের করুন | NVIDIA ড্রাইভার এবং .NET ফ্রেমওয়ার্ক 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, রানটাইম অন্তর্ভুক্ত | ইনস্টলেশন অপারেশনের জন্য সামঞ্জস্যপূর্ণ মূল NVIDIA ড্রাইভার প্যাকেজ |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | সম্পূর্ণ NVMFG জিপ বের করুন, সাবফোল্ডার ধরে রাখুন | RTX 40, বিদ্যমান DLSS FG, সঠিক প্রদানকারী এবং .NET ফ্রেমওয়ার্ক 4.8 সহায়ক |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | সম্পূর্ণ RP জিপ বের করুন | RTSS এবং .NET ফ্রেমওয়ার্ক 4.8 |

<a id="download-verify-install"></a>
## ডাউনলোড করুন, যাচাই করুন, ইনস্টল করুন

1. নির্বাচিত প্রকাশিত রিলিজে, এর নামকৃত অ্যাপ্লিকেশন সম্পদ, নোটিশ ZIP এবং SHA256SUMS.txt ডাউনলোড করুন।
2. প্রকৃত ডাউনলোড করা ফাইলের নাম সহ [SHA-256 উদাহরণ](downloads.md#sha-256) ব্যবহার করুন।
3. সেটআপের জন্য, সাধারণ ইনস্টলার অনুসরণ করুন। পোর্টেবল জিপের জন্য, একটি নতুন স্থানীয় লিখনযোগ্য ফোল্ডারে সবকিছু বের করুন; জিপের ভিতর থেকে দৌড়াবেন না।
4. অ্যাপ্লিকেশনটির নিজস্ব EXE খুলুন। সহগামী লাইসেন্স/কনফিগারেশন/ডেটা ফাইল রাখুন।
5. সেটিংস বা সিস্টেম অপারেশন সক্ষম করার আগে সেই টুলের ব্যবহারের নির্দেশাবলী পড়ুন।

বর্তমান বাইনারিগুলি স্বাক্ষরবিহীন। একটি ম্যাচিং হ্যাশ প্রত্যাশিত বাইট নিশ্চিত করে; এটি একটি নিরাপত্তা বা সামঞ্জস্যের শংসাপত্র নয়। শুধুমাত্র একটি সতর্কতা দমন করার জন্য Windows নিরাপত্তা সুরক্ষা নিষ্ক্রিয় করবেন না।

NVDF বা এর ঐচ্ছিক NVPI সঙ্গী ইনস্টল করা একটি GPU ড্রাইভার ইনস্টল করা থেকে আলাদা। NVPI সঙ্গী তার বিদ্যমান অভ্যন্তরীণ ইনস্টলেশন নাম রাখে। এর এলিভেটেড RasterPulse বোতামের জন্য একটি সুরক্ষিত সিস্টেম-ব্যাপী ইনস্টলেশন প্রয়োজন; অন্যান্য RP কপি তাদের নিজস্ব শর্টকাটের মাধ্যমে খোলা যেতে পারে।

NVMFG পরীক্ষামূলক এবং [নথিভুক্ত NVIDIA SDK লাইসেন্সিং রিজার্ভ](provenance.md) আছে। কোন NVIDIA ড্রাইভার, NGX প্রদানকারী/মডেল বা গেম Streamline রানটাইম অন্তর্ভুক্ত নেই। নির্বাচিত SDK ডাউনলোড এবং গেম আপডেটগুলি স্পষ্ট পৃথক অপারেশন।

<a id="language-and-updates"></a>
## ভাষা এবং আপডেট

ডকুমেন্টেশনের জন্য README এর 34-ভাষা নির্বাচক ব্যবহার করুন। NVDF, NVMFG এবং RP তাদের নিজস্ব 34-ভাষা UI সেটিং আছে; NVPI তার বিদ্যমান ভাষা সমর্থন রাখে। কিছু ইনস্টলার প্রযুক্তিগত স্ট্রিং ইংরেজিতে ফিরে আসে।

আপডেট করার সময় একটি টুলের ইনস্টলেশন পরিচয় রাখুন। প্রথমে এটি বন্ধ করুন এবং ব্যাকআপ সংরক্ষণ করুন। NVMFG-এর জন্য, প্রভাবিত গেমগুলি বন্ধ করুন এবং মুলতুবি প্রোফাইল পুনরুদ্ধারের সমাধান করুন। পোর্টেবল আপডেটের জন্য, রিলিজ একত্রিত করার পরিবর্তে একটি নতুন ফোল্ডার ব্যবহার করুন।

<a id="removing-a-tool"></a>
## একটি টুল অপসারণ

একটি অ্যাপ্লিকেশন আনইনস্টল করা স্বয়ংক্রিয়ভাবে সেটিংস পূর্বাবস্থায় ফেরানো নয়৷

- **NVPI:** প্রয়োজনে অপসারণের আগে উদ্দিষ্ট প্রোফাইল/ডিসপ্লে সেটিংস পুনরুদ্ধার করুন।
- **NVDF:** আপনি যদি উন্নত/NVENC পরিবর্তনগুলি পুনরুদ্ধার করতে চান তবে প্রথমে পুনরুদ্ধার ব্যবহার করুন। Uninstall গ্রাফিক্স ড্রাইভার, সেটিংস এবং ব্যাকআপ ছেড়ে দেয়।
- **NVMFG:** গেম বন্ধ করুন, কন্ট্রোলার অক্ষম/প্রস্থান করুন, NVIDIA পুনরুদ্ধার সমাধান করুন এবং অপসারণের আগে পছন্দসই গেম SDK ব্যাকআপগুলি পুনরুদ্ধার করুন।
- **RP:** প্রথমে ইচ্ছাকৃত লিমিটার ওভাররাইডগুলি সরিয়ে দিন। Uninstall সংরক্ষিত RTSS ক্যাপ মুছে দেয় না বা RTSS মুছে দেয় না।

সঠিক ডেটা অবস্থান এবং সীমাবদ্ধতার জন্য প্রতিটি [প্রকল্প নির্দেশিকা](../README.md#projects) দেখুন, অথবা একটি পুনরুদ্ধারের পদক্ষেপ ব্যর্থ হলে [সমর্থন](support.md) দেখুন।
