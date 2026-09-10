<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · **বাংলা** · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ইংরেজি থেকে মেশিন-সহায়তা অনুবাদ। প্রযুক্তিগত নাম, কমান্ড, URL এবং মূল আইনি পাঠ্য সংরক্ষিত আছে। নেটিভ-স্পিকার পর্যালোচনা স্বাগত; শব্দ অস্পষ্ট হলে ইংরেজি রেফারেন্সের সাথে পরামর্শ করুন।
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# অবদান

NV Laboratory 禅堂 Zendo (RevoluSound Team) দ্বারা রক্ষণাবেক্ষণ করা হয়। রক্ষণাবেক্ষণকারী সিদ্ধান্ত নেয় কী গ্রহণ করা হবে এবং মুক্তি দেওয়া হবে। একটি ইস্যু বা পুল অনুরোধ খোলার অর্থ এই নয় যে একটি অবদান গ্রহণ করা হয়েছে বা বিতরণের জন্য অনুমোদিত৷

বাগ বা বৈশিষ্ট্য ফর্ম ব্যবহার করুন এবং প্রোগ্রাম/সংস্করণ সনাক্ত করুন. আগে বিদ্যমান সমস্যা অনুসন্ধান করুন. একটি বড় অবদান প্রস্তুত করার আগে উল্লেখযোগ্য পরিবর্তন আলোচনা করুন. নিরাপত্তা সংক্রান্ত বিষয়ে, [SECURITY.md](SECURITY.md) অনুসরণ করুন।

এই পাবলিক হাবটিতে ডকুমেন্টেশন, নোটিশ, রিলিজ মেটাডেটা এবং সংগ্রহস্থলের বৈধতা রয়েছে। আবেদনের উত্স এবং পরীক্ষাগুলি ব্যক্তিগতভাবে রক্ষণাবেক্ষণ করা হয়। ডিকম্পাইল করা কোড, প্রাইভেট সোর্স, ক্রেডেনশিয়াল, ইউজার প্রোফাইল বা এক্সিকিউটেবল পেলোড জমা দেবেন না।

ডকুমেন্টেশন PR-এর উচিত 34টি ভাষার প্রতিরূপ এবং নেভিগেশন সারিবদ্ধ রাখা, কমান্ড/ফাইল/পণ্যের নাম সংরক্ষণ করা এবং প্রকৃত আচরণ বর্ণনা করা। নতুন স্ক্রিনশটগুলি অবশ্যই আপনার নিজস্ব, সংস্করণ-পরিচিত এবং ব্যক্তিগত বিবরণ মুক্ত হতে হবে; সিন্থেটিক ডেটা লেবেল করা আবশ্যক। প্রতিটি নতুন তৃতীয়-পক্ষের সম্পদের জন্য উদ্ভব এবং অনুমতি প্রদান করুন।

UTF-8, LF, পঠনযোগ্য মার্কডাউন এবং ছোট ফোকাসড পরিবর্তন ব্যবহার করুন। Python যাচাইকারী শুধুমাত্র স্ট্যান্ডার্ড লাইব্রেরি ব্যবহার করে। এর বিদ্যমান শৈলীর সাথে মিল করুন, অপ্রয়োজনীয় নির্ভরতা এড়ান এবং চালান:

```text
python tools/validate_repository.py
```

রিলিজ মেটাডেটা পরিবর্তনের জন্য, নিরীক্ষিত বাইনারি থেকে সঠিক সংস্করণ/ট্যাগ, ফাইলের আকার এবং SHA-256 অন্তর্ভুক্ত করুন এবং ডাউনলোড পৃষ্ঠাগুলি সারিবদ্ধ রাখুন। অ্যাপ্লিকেশন পরিবর্তনের জন্য প্রভাবিত আচরণের জন্য উপযুক্ত ব্যক্তিগত বিল্ড/পরীক্ষা প্রয়োজন; একটি ডকুমেন্টেশন চেক একটি আবেদন পরীক্ষা নয়. কখনই ঐতিহাসিক পরীক্ষার ফলাফল বা লাভ আবিষ্কার করবেন না।

মূল হাব উপাদান অবদানের মাধ্যমে, আপনি [লাইসেন্স](../../../LICENSE)-এ এর ব্যাপ্ত MIT লাইসেন্সে সম্মত হন। তৃতীয় পক্ষের নোটিশ রাখুন এবং আপনার পরিবর্তনগুলি চিহ্নিত করুন; একটি আপস্ট্রিম লাইসেন্স প্রতিস্থাপন করবেন না। গ্রহণ এবং প্রকাশনা রক্ষণাবেক্ষণকারী সিদ্ধান্ত অবশেষ.
