<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · **हिन्दी** · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> अंग्रेजी से मशीन-सहायता अनुवाद। तकनीकी नाम, आदेश, यूआरएल और मूल कानूनी पाठ संरक्षित हैं। मूल-वक्ता समीक्षा का स्वागत है; यदि शब्दांकन अस्पष्ट है तो अंग्रेजी संदर्भ देखें।
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# इंस्टालेशन गाइड

[डाउनलोड](downloads.md) से प्रारंभ करें, जो प्रकाशन स्थिति और सटीक संपत्ति नाम रिकॉर्ड करता है। ये अलग-अलग उपकरण हैं: केवल वही इंस्टॉल करें जिनकी आपको आवश्यकता है।

> **NVRasterPulse के लिए, प्रोफ़ाइल प्रबंधक खोलने से पहले [Guru3D से RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) इंस्टॉल करें।**
> सीमाएं लागू करने के लिए RTSS को चलना चाहिए; यह NV Tools में शामिल नहीं है।

| औज़ार | स्थापित संस्करण | पोर्टेबल संस्करण | मुख्य शर्त |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | संपूर्ण NVPI ज़िप निकालें | NVIDIA ड्राइवर और .NET फ्रेमवर्क 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, रनटाइम शामिल | स्थापना संचालन के लिए संगत मूल NVIDIA ड्राइवर पैकेज |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | पूर्ण NVMFG ज़िप निकालें, सबफ़ोल्डर बनाए रखें | RTX 40, मौजूदा DLSS FG, सटीक प्रदाता और .NET फ्रेमवर्क 4.8 सहायक |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | संपूर्ण RP ज़िप निकालें | RTSS और .NET फ्रेमवर्क 4.8 |

<a id="download-verify-install"></a>
## डाउनलोड करें, सत्यापित करें, इंस्टॉल करें

1. चुनी गई प्रकाशित रिलीज़ पर, इसकी नामित एप्लिकेशन संपत्ति, नोटिस ज़िप और SHA256SUMS.txt डाउनलोड करें।
2. वास्तविक डाउनलोड किए गए फ़ाइल नाम के साथ [SHA-256 उदाहरण](downloads.md#sha-256) का उपयोग करें।
3. सेटअप के लिए, सामान्य इंस्टॉलर का पालन करें। पोर्टेबल ज़िप के लिए, सब कुछ एक नए स्थानीय लिखने योग्य फ़ोल्डर में निकालें; ज़िप के अंदर से न भागें.
4. एप्लिकेशन का अपना EXE खोलें. संलग्न लाइसेंस/कॉन्फ़िगरेशन/डेटा फ़ाइलें रखें।
5. सेटिंग्स या सिस्टम संचालन सक्षम करने से पहले उस टूल के उपयोग निर्देश पढ़ें।

वर्तमान बायनेरिज़ अहस्ताक्षरित हैं. एक मिलान हैश अपेक्षित बाइट्स की पुष्टि करता है; यह कोई सुरक्षा या अनुकूलता प्रमाणपत्र नहीं है. केवल चेतावनी को दबाने के लिए Windows सुरक्षा सुरक्षा को अक्षम न करें।

NVDF या इसके वैकल्पिक NVPI साथी को स्थापित करना GPU ड्राइवर को स्थापित करने से अलग है। NVPI साथी अपना मौजूदा आंतरिक इंस्टॉलेशन नाम रखता है। इसके उन्नत RasterPulse बटन को एक संरक्षित सिस्टम-वाइड इंस्टॉलेशन की आवश्यकता होती है; अन्य RP प्रतियां उनके अपने शॉर्टकट के माध्यम से खोली जा सकती हैं।

NVMFG प्रायोगिक है और इसमें [प्रलेखित NVIDIA SDK लाइसेंसिंग रिजर्व](provenance.md) है। कोई NVIDIA ड्राइवर, NGX प्रदाता/मॉडल या गेम Streamline रनटाइम शामिल नहीं है। चयनित SDK डाउनलोड और गेम अपडेट स्पष्ट रूप से अलग-अलग ऑपरेशन हैं।

<a id="language-and-updates"></a>
## भाषा और अद्यतन

दस्तावेज़ीकरण के लिए README के 34-भाषा चयनकर्ता का उपयोग करें। NVDF, NVMFG और RP की अपनी 34-भाषा यूआई सेटिंग है; NVPI अपना मौजूदा भाषा समर्थन बरकरार रखता है। कुछ इंस्टॉलर तकनीकी तार अंग्रेजी में वापस आ जाते हैं।

अपडेट करते समय टूल की इंस्टॉलेशन पहचान बनाए रखें। पहले इसे बंद करें और बैकअप सुरक्षित रखें। एनवीएमएफजी के लिए, प्रभावित गेम बंद करें और लंबित प्रोफ़ाइल पुनर्प्राप्ति का समाधान करें। पोर्टेबल अपडेट के लिए, रिलीज़ को संयोजित करने के बजाय एक ताज़ा फ़ोल्डर का उपयोग करें।

<a id="removing-a-tool"></a>
## एक उपकरण हटाना

किसी एप्लिकेशन को अनइंस्टॉल करना उसकी सेटिंग्स को स्वचालित रूप से पूर्ववत करना नहीं है।

- **NVPI:** यदि आवश्यक हो तो हटाने से पहले इच्छित प्रोफाइल/डिस्प्ले सेटिंग्स को पुनर्स्थापित करें।
- **NVDF:** यदि आप उन्नत/NVENC परिवर्तनों को पुनर्स्थापित करना चाहते हैं तो पहले पुनर्प्राप्ति का उपयोग करें। Uninstall ग्राफ़िक्स ड्राइवर, सेटिंग्स और बैकअप छोड़ देता है।
- **एनवीएमएफजी:** गेम बंद करें, कंट्रोलर को अक्षम करें/छोड़ें, NVIDIA पुनर्प्राप्ति का समाधान करें और हटाने से पहले वांछित गेम SDK बैकअप पुनर्स्थापित करें।
- **RP:** पहले इच्छित लिमिटर ओवरराइड को हटा दें। Uninstall सहेजे गए RTSS कैप्स को मिटाता नहीं है या RTSS को नहीं हटाता है।

सटीक डेटा स्थानों और सीमाओं के लिए प्रत्येक [प्रोजेक्ट गाइड](../README.md#projects) देखें, या पुनर्प्राप्ति चरण विफल होने पर [समर्थन](support.md) देखें।
