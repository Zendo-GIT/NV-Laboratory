<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · **हिन्दी** · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> अंग्रेजी से मशीन-सहायता अनुवाद। तकनीकी नाम, आदेश, यूआरएल और मूल कानूनी पाठ संरक्षित हैं। मूल-वक्ता समीक्षा का स्वागत है; यदि शब्दांकन अस्पष्ट है तो अंग्रेजी संदर्भ देखें।
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# योगदान दे रहे हैं

NV Laboratory का रखरखाव 禅堂 Zendo (RevoluSound Team) द्वारा किया जाता है। अनुरक्षक यह तय करता है कि क्या स्वीकार किया जाए और क्या जारी किया जाए। किसी इश्यू या पुल अनुरोध को खोलने का मतलब यह नहीं है कि योगदान स्वीकार कर लिया गया है या वितरण के लिए अधिकृत कर दिया गया है।

बग या फीचर फॉर्म का उपयोग करें और प्रोग्राम/संस्करण की पहचान करें। पहले मौजूदा मुद्दे खोजें. एक बड़ा योगदान तैयार करने से पहले महत्वपूर्ण बदलावों पर चर्चा करें। सुरक्षा मामलों के लिए, [SECURITY.md](SECURITY.md) का पालन करें।

इस सार्वजनिक हब में दस्तावेज़ीकरण, नोटिस, रिलीज़ मेटाडेटा और रिपॉजिटरी सत्यापन शामिल हैं। एप्लिकेशन स्रोत और परीक्षण निजी तौर पर बनाए रखे जाते हैं। विघटित कोड, निजी स्रोत, क्रेडेंशियल, उपयोगकर्ता प्रोफ़ाइल या निष्पादन योग्य पेलोड सबमिट न करें।

दस्तावेज़ीकरण पीआर को 34 भाषा समकक्षों और नेविगेशन को संरेखित रखना चाहिए, कमांड/फ़ाइल/उत्पाद नामों को संरक्षित करना चाहिए और वास्तविक व्यवहार का वर्णन करना चाहिए। नए स्क्रीनशॉट आपके स्वयं के, संस्करण-पहचान वाले और व्यक्तिगत विवरण से मुक्त होने चाहिए; सिंथेटिक डेटा को लेबल किया जाना चाहिए। प्रत्येक नई तृतीय-पक्ष संपत्ति के लिए उत्पत्ति और अनुमति प्रदान करें।

यूटीएफ-8, एलएफ, पठनीय मार्कडाउन और छोटे केंद्रित परिवर्तनों का उपयोग करें। Python सत्यापनकर्ता केवल मानक लाइब्रेरी का उपयोग करता है। इसकी मौजूदा शैली से मेल करें, अनावश्यक निर्भरताओं से बचें और चलाएँ:

```text
python tools/validate_repository.py
```

रिलीज़ मेटाडेटा परिवर्तनों के लिए, ऑडिट किए गए बायनेरिज़ से सटीक संस्करण/टैग, फ़ाइल आकार और SHA-256 शामिल करें, और डाउनलोड पृष्ठों को संरेखित रखें। एप्लिकेशन परिवर्तनों के लिए प्रभावित व्यवहार के लिए उपयुक्त निजी निर्माण/परीक्षण की आवश्यकता होती है; दस्तावेज़ीकरण जाँच कोई एप्लिकेशन परीक्षण नहीं है. कभी भी ऐतिहासिक परीक्षण परिणाम या लाभ का आविष्कार न करें।

मूल हब सामग्री का योगदान करके, आप [लाइसेंस](../../../LICENSE) में इसके दायरे वाले MIT लाइसेंस से सहमत होते हैं। तृतीय-पक्ष नोटिस रखें और अपने परिवर्तनों की पहचान करें; अपस्ट्रीम लाइसेंस को प्रतिस्थापित न करें. स्वीकृति और प्रकाशन अनुरक्षक निर्णय बने रहते हैं।
