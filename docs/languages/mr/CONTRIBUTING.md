<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · **मराठी** · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> इंग्रजीतून मशीन-सहाय्यित भाषांतर. तांत्रिक नावे, आदेश, URL आणि मूळ कायदेशीर मजकूर जतन केले आहेत. नेटिव्ह-स्पीकर पुनरावलोकन स्वागतार्ह आहे; शब्द अस्पष्ट असल्यास इंग्रजी संदर्भ पहा.
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# योगदान देत आहे

NV Laboratory ची देखभाल 禅堂 Zendo (RevoluSound Team) द्वारे केली जाते. काय स्वीकारले आणि सोडले जाईल हे मेंटेनर ठरवतो. इश्यू किंवा पुल रिक्वेस्ट उघडण्याचा अर्थ असा नाही की योगदान स्वीकारले आहे किंवा वितरणासाठी अधिकृत आहे.

बग किंवा वैशिष्ट्य फॉर्म वापरा आणि प्रोग्राम/आवृत्ती ओळखा. प्रथम विद्यमान समस्या शोधा. मोठे योगदान तयार करण्यापूर्वी महत्त्वपूर्ण बदलांची चर्चा करा. सुरक्षिततेच्या बाबींसाठी, [SECURITY.md](SECURITY.md) चे अनुसरण करा.

या सार्वजनिक हबमध्ये दस्तऐवजीकरण, सूचना, रिलीझ मेटाडेटा आणि रेपॉजिटरी प्रमाणीकरण समाविष्ट आहे. अर्ज स्त्रोत आणि चाचण्या खाजगीरित्या ठेवल्या जातात. विघटित कोड, खाजगी स्त्रोत, क्रेडेन्शियल, वापरकर्ता प्रोफाइल किंवा एक्झिक्युटेबल पेलोड सबमिट करू नका.

डॉक्युमेंटेशन पीआरने 34 भाषा समकक्ष आणि नेव्हिगेशन संरेखित ठेवले पाहिजे, कमांड/फाइल/उत्पादन नावे जतन केली पाहिजे आणि वास्तविक वर्तनाचे वर्णन केले पाहिजे. नवीन स्क्रीनशॉट तुमचे स्वतःचे, आवृत्ती-ओळखलेले आणि वैयक्तिक तपशील मुक्त असले पाहिजेत; सिंथेटिक डेटा लेबल करणे आवश्यक आहे. प्रत्येक नवीन तृतीय-पक्ष मालमत्तेसाठी मूळ आणि परवानगी प्रदान करा.

UTF-8, LF, वाचनीय मार्कडाउन आणि लहान फोकस केलेले बदल वापरा. Python व्हॅलिडेटर फक्त मानक लायब्ररी वापरतो. त्याची विद्यमान शैली जुळवा, अनावश्यक अवलंबित्व टाळा आणि चालवा:

```text
python tools/validate_repository.py
```

रिलीझ मेटाडेटा बदलांसाठी, ऑडिट केलेल्या बायनरींमधून अचूक आवृत्ती/टॅग, फाइल आकार आणि SHA-256 समाविष्ट करा आणि डाउनलोड पृष्ठे संरेखित ठेवा. अनुप्रयोगातील बदलांसाठी प्रभावित वर्तनासाठी योग्य खाजगी बिल्ड/चाचण्या आवश्यक आहेत; कागदपत्र तपासणी ही अर्जाची चाचणी नाही. कधीही ऐतिहासिक चाचणी परिणाम किंवा नफ्याचा शोध लावू नका.

मूळ हब सामग्रीचे योगदान देऊन, तुम्ही [परवाना](../../../LICENSE) मधील त्याच्या व्याप्तीच्या MIT परवान्याला सहमती देता. तृतीय-पक्षाच्या सूचना ठेवा आणि तुमचे बदल ओळखा; अपस्ट्रीम परवाना बदलू नका. स्वीकृती आणि प्रकाशन हे मेंटेनरचे निर्णय राहतात.
