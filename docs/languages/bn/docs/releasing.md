<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · **বাংলা** · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> ইংরেজি থেকে মেশিন-সহায়তা অনুবাদ। প্রযুক্তিগত নাম, কমান্ড, URL এবং মূল আইনি পাঠ্য সংরক্ষিত আছে। নেটিভ-স্পিকার পর্যালোচনা স্বাগত; শব্দ অস্পষ্ট হলে ইংরেজি রেফারেন্সের সাথে পরামর্শ করুন।
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# প্রকাশনা ও প্রকাশ

পাবলিক রিপোজিটরি হল **জেন্ডো-জিআইটি/এনভি-ল্যাবরেটরি**। ডকুমেন্টেশন পরিবর্তনগুলি **GitHub Desktop** দিয়ে রক্ষণাবেক্ষণকারী দ্বারা পর্যালোচনা, প্রতিশ্রুতিবদ্ধ এবং পুশ করা হয়। একটি স্থানীয় কমিট ফাইল আপলোড করে না। বাইনারি প্যাকেজ হল পৃথক GitHub রিলিজ সম্পদ; তারা কখনই গিট পরিবর্তনের তালিকার অন্তর্ভুক্ত নয়।

<a id="documentation-updates"></a>
## ডকুমেন্টেশন আপডেট

1. GitHub Desktop-এ **NV-ল্যাবরেটরি** ফোল্ডারটি খুলুন।
2. ডকুমেন্টেশন, নোটিশ, ছবি, JSON মেটাডেটা এবং ডকুমেন্টেশন যাচাইকারী পর্যালোচনা করুন।
3. সেই ফোল্ডার থেকে `python tools/validate_repository.py` চালান।
4. পর্যালোচনা করা পরিবর্তনগুলি করুন, তারপর **Push origin** ব্যবহার করুন৷ কর্ম ফলাফল পরীক্ষা করুন.
5. সর্বজনীন লেখকের পরিচয় **禅堂 Zendo (RevoluSound Team)** এবং অ্যাকাউন্টের GitHub `noreply` ঠিকানা রাখুন।

কখনই প্যারেন্ট ডেভেলপমেন্ট ওয়ার্কস্পেস, প্রাইভেট অডিট ডিরেক্টরি বা বাইনারি অ্যাটাচমেন্ট ডিরেক্টরি নির্বাচন করবেন না। [ইমেল গোপনীয়তা কমিট](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)।

<a id="independent-application-releases"></a>
## স্বাধীন অ্যাপ্লিকেশন রিলিজ

| টুল | ট্যাগ | সংস্করণ নীতি |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | বিদ্যমান চার অংশের অ্যাপ্লিকেশন সংস্করণ; সেটআপ রিভিশন 2 এর নিজস্ব ফাইলের নাম রয়েছে |
| NVDriverForge | nvdriverforge-v0.1.3 | বিদ্যমান 0.x স্কিম; সংস্করণযুক্ত আপডেটগুলি আগের প্যাকেজগুলিকে সংরক্ষণ করে |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2 প্রার্থী একটি নতুন অ্যাপ্লিকেশন সংস্করণ উদ্ভাবন ছাড়াই সঠিক হ্যাশ দ্বারা চিহ্নিত |
| NVRasterPulse | nvrasterpulse-v0.1 | বিদ্যমান দুই-অংশের সংস্করণ |

রক্ষণাবেক্ষণকারী সরাসরি প্রকাশ করতে পারে বা নিরীক্ষিত সম্পদ প্রকাশ করার জন্য একজন সহকারীকে অনুমোদন করতে পারে। প্রকাশনা সুস্পষ্ট; কোন ওয়ার্কফ্লো প্রতিটি প্রতিশ্রুতিতে একটি রিলিজ তৈরি করে না।

1. বর্তমান পূর্বপ্রকাশনা প্রতিবেদন, বাইনারিগুলির উত্স, লাইসেন্স এবং SHA-256 মান পর্যালোচনা করুন।
2. পর্যালোচনা করা হাব প্রতিশ্রুতি লক্ষ্য করে টুলের ট্যাগের জন্য একটি খসড়া তৈরি করুন। প্রস্তুত সংস্করণ-নির্দিষ্ট রিলিজ নোট অন্তর্ভুক্ত করুন।
3. শুধুমাত্র সেই সংস্করণের সেটআপ/পোর্টেবল সম্পদ, `Licenses-and-Credits.zip` এবং `SHA256SUMS.txt` সংযুক্ত করুন।
4. সামঞ্জস্য, ইনস্টলেশন, নির্ভরতা, পরিবর্তন এবং পরিচিত সীমা পরীক্ষা করুন। NVRasterPulse এর জন্য RTSS বিশিষ্ট রাখুন।
5. প্রকাশ করুন, সর্বজনীন সম্পদের URL, আকার এবং হ্যাশ যাচাই করুন এবং `docs/releases.json`-এ প্রকৃত প্রকাশনার তারিখ রেকর্ড করুন।
6. ডাউনলোড পৃষ্ঠা এবং অনুবাদগুলি আপডেট করুন, তারপর GitHub Desktop-এ তাদের পরিবর্তনগুলি কমিট/পুশ করুন৷

প্রতি-প্রকল্প ট্যাগ লিঙ্কগুলি একটি শেয়ার করা `releases/latest` লিঙ্কের মাধ্যমে ব্যবহারকারীদের অন্য টুলে পাঠানো এড়ায়। GitHub-এর স্বয়ংক্রিয় **Source code** সংরক্ষণাগারগুলিতে এই ডকুমেন্টেশন হাব রয়েছে৷ আবেদনের উৎস গোপন থাকে। মূল উপাদান নোটিশ অক্ষত থাকে, এবং একটি রিলিজ NVMFG এর নথিভুক্ত NVIDIA SDK রিজার্ভের সমাধান করে না।

<a id="integrity-and-storage"></a>
## সততা এবং স্টোরেজ

প্রকাশিত বাইনারি বাইটগুলি কখনই নীরবে প্রতিস্থাপন করবেন না। নতুন হ্যাশ সহ একটি নতুন স্পষ্ট সংস্করণ বা ইনস্টলার সংশোধন ব্যবহার করুন। আইনি সাইডকারগুলি এমবেডেড নোটিশের পরিপূরক। NVDriverForge 0.1.3 পোর্টেবল হল 141,760,351 বাইট, GitHub এর সাধারণ 100 MiB গিট-ফাইল সীমার উপরে। রিলিজ সংযুক্তিগুলি এই হাবে বাইনারি বা গিট এলএফএস স্থাপন করা এড়ায়। [GitHub বড়-ফাইল নির্দেশিকা](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)।

ব্যক্তিগত দুর্বলতা প্রতিবেদন সংগ্রহস্থল নিরাপত্তা সেটিংস সক্রিয় করা উচিত. সেখানে সংবেদনশীল প্রতিবেদন পাঠানোর আগে এর প্রাপ্যতা যাচাই করুন; [SECURITY.md](../SECURITY.md) একটি ফলব্যাক প্রদান করে যা দুর্বলতার বিবরণ প্রকাশ করে না।

[ক্যাটালগ ডাউনলোড করুন](downloads.md) · [GitHub রিলিজ ডকুমেন্টেশন](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
