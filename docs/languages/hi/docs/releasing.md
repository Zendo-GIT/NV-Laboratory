<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · **हिन्दी** · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> अंग्रेजी से मशीन-सहायता अनुवाद। तकनीकी नाम, आदेश, यूआरएल और मूल कानूनी पाठ संरक्षित हैं। मूल-वक्ता समीक्षा का स्वागत है; यदि शब्दांकन अस्पष्ट है तो अंग्रेजी संदर्भ देखें।
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# प्रकाशन एवं विमोचन

सार्वजनिक भंडार **ज़ेंडो-जीआईटी/एनवी-प्रयोगशाला** है। दस्तावेज़ीकरण परिवर्तनों की समीक्षा, प्रतिबद्ध और अनुरक्षक द्वारा **GitHub Desktop** के साथ की जाती है। एक स्थानीय प्रतिबद्धता फ़ाइलें अपलोड नहीं करती है। बाइनरी पैकेज अलग GitHub रिलीज़ संपत्तियां हैं; वे कभी भी Git परिवर्तन सूची में शामिल नहीं होते हैं।

<a id="documentation-updates"></a>
## दस्तावेज़ीकरण अद्यतन

1. GitHub Desktop में **NV-प्रयोगशाला** फ़ोल्डर खोलें।
2. दस्तावेज़ीकरण, नोटिस, चित्र, JSON मेटाडेटा और दस्तावेज़ सत्यापनकर्ता की समीक्षा करें।
3. उस फ़ोल्डर से `python tools/validate_repository.py` चलाएँ।
4. समीक्षा किए गए परिवर्तन करें, फिर **Push origin** का उपयोग करें। क्रिया परिणाम की जाँच करें.
5. सार्वजनिक लेखक की पहचान **禅堂 Zendo (RevoluSound Team)** और खाते का GitHub `noreply` पता रखें।

कभी भी मूल विकास कार्यक्षेत्र, निजी ऑडिट निर्देशिका या बाइनरी अटैचमेंट निर्देशिका का चयन न करें। [ईमेल गोपनीयता प्रतिबद्ध करें](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## स्वतंत्र आवेदन विज्ञप्ति

| औज़ार | टैग | संस्करण नीति |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | मौजूदा चार-भाग वाला एप्लिकेशन संस्करण; सेटअप संशोधन 2 का अपना फ़ाइल नाम है |
| NVDriverForge | nvdriverforge-v0.1.4 | मौजूदा 0.x योजना; संस्करणित अद्यतन पुराने पैकेजों को सुरक्षित रखते हैं |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | एप्लिकेशन संस्करण 0.2.3; सार्वजनिक 0.1.1 के बाद से संचयी परिवर्तन |
| NVRasterPulse | nvrasterPulse-v0.2 | मौजूदा दो भाग संस्करण |

अनुरक्षक सीधे प्रकाशित कर सकता है या किसी सहायक को लेखापरीक्षित संपत्तियों को प्रकाशित करने के लिए अधिकृत कर सकता है। प्रकाशन स्पष्ट है; कोई भी वर्कफ़्लो प्रत्येक प्रतिबद्धता पर रिलीज़ नहीं बनाता है।

1. वर्तमान प्रीपब्लिकेशन रिपोर्ट, बायनेरिज़ के स्रोत, लाइसेंस और SHA-256 मानों की समीक्षा करें।
2. समीक्षा की गई हब प्रतिबद्धता को लक्षित करते हुए टूल के टैग के लिए एक ड्राफ्ट बनाएं। तैयार संस्करण-विशिष्ट रिलीज़ नोट्स शामिल करें।
3. केवल उस संस्करण की सेटअप/पोर्टेबल संपत्तियां, `Licenses-and-Credits.zip` और `SHA256SUMS.txt` संलग्न करें।
4. अनुकूलता, स्थापना, निर्भरता, परिवर्तन और ज्ञात सीमाओं की जाँच करें। NVRasterPulse के लिए RTSS को प्रमुखता से रखें।
5. प्रकाशित करें, सार्वजनिक संपत्ति यूआरएल, आकार और हैश को सत्यापित करें, और `docs/releases.json` में वास्तविक प्रकाशन तिथि रिकॉर्ड करें।
6. डाउनलोड पृष्ठों और अनुवादों को अद्यतन करें, फिर GitHub Desktop में उनके परिवर्तन प्रतिबद्ध/पुश करें।

प्रति-प्रोजेक्ट टैग लिंक साझा `releases/latest` लिंक के माध्यम से उपयोगकर्ताओं को दूसरे टूल पर भेजने से बचते हैं। GitHub के स्वचालित **Source code** अभिलेखागार में यह दस्तावेज़ीकरण केंद्र शामिल है। एप्लिकेशन स्रोत निजी रहते हैं. मूल घटक नोटिस बरकरार रहते हैं, और एक रिलीज एनवीएमएफजी के दस्तावेजित NVIDIA SDK रिजर्व का समाधान नहीं करता है।


18 सितंबर का अपडेट तीन नए टैग तैयार करता है; मौजूदा Profile Inspector रिलीज़ अपरिवर्तित रहेगी। एप्लिकेशन अपडेट जांच के लिए संपत्ति के नाम, टैग और `SHA256SUMS.txt` सटीक रहने चाहिए। सामान्य रिलीज़ को प्रीरिलीज़ फ़्लैग के बिना प्रकाशित करें ताकि उन्हें स्थिर-रिलीज़ जांच में उजागर किया जा सके; एनवीएमएफजी प्रयोगात्मक बना हुआ है।

<a id="integrity-and-storage"></a>
## अखंडता और भंडारण

कभी भी प्रकाशित बाइनरी बाइट्स को चुपचाप न बदलें। नए स्पष्ट संस्करण या नए हैश के साथ इंस्टॉलर संशोधन का उपयोग करें। कानूनी साइडकार एम्बेडेड नोटिस के पूरक हैं। NVDriverForge 0.1.4 पोर्टेबल 142,017,891 बाइट्स है, जो GitHub की सामान्य 100 MiB Git-फ़ाइल सीमा से ऊपर है। रिलीज़ अटैचमेंट इस हब में बायनेरिज़ या Git LFS डालने से बचें। [GitHub बड़ी फ़ाइल मार्गदर्शन](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

रिपॉजिटरी सुरक्षा सेटिंग्स में निजी भेद्यता रिपोर्टिंग सक्षम की जानी चाहिए। संवेदनशील रिपोर्टों को वहां निर्देशित करने से पहले इसकी उपलब्धता सत्यापित करें; [SECURITY.md](../SECURITY.md) एक फ़ॉलबैक प्रदान करता है जो भेद्यता विवरण को उजागर नहीं करता है।

[कैटलॉग डाउनलोड करें](downloads.md) · [GitHub रिलीज़ दस्तावेज़](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
