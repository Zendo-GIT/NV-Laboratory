<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · **मराठी** · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> इंग्रजीतून मशीन-सहाय्यित भाषांतर. तांत्रिक नावे, आदेश, URL आणि मूळ कायदेशीर मजकूर जतन केले आहेत. नेटिव्ह-स्पीकर पुनरावलोकन स्वागतार्ह आहे; शब्द अस्पष्ट असल्यास इंग्रजी संदर्भ पहा.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# स्थापना मार्गदर्शक

[डाउनलोड](downloads.md) सह प्रारंभ करा, जे प्रकाशन स्थिती आणि अचूक मालमत्तेची नावे नोंदवते. ही स्वतंत्र साधने आहेत: आपल्याला आवश्यक असलेली फक्त स्थापित करा.

> **NVRasterPulse साठी, प्रोफाइल व्यवस्थापक उघडण्यापूर्वी [Guru3D कडून RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) स्थापित करा.**
> मर्यादा लागू करण्यासाठी RTSS चालवणे आवश्यक आहे; ते NV Tools मध्ये समाविष्ट केलेले नाही.

| साधन | स्थापित संस्करण | पोर्टेबल आवृत्ती | मुख्य पूर्व शर्त |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | पूर्ण NVPI झिप काढा | NVIDIA ड्राइव्हर आणि .NET फ्रेमवर्क 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, रनटाइम समाविष्ट आहे | इंस्टॉलेशन ऑपरेशन्ससाठी सुसंगत मूळ NVIDIA ड्राइव्हर पॅकेज |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | पूर्ण NVMFG झिप काढा, सबफोल्डर ठेवा | RTX 40, विद्यमान DLSS FG, अचूक प्रदाता आणि .NET फ्रेमवर्क 4.8 मदतनीस |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | पूर्ण RP झिप काढा | RTSS आणि .NET फ्रेमवर्क 4.8 |

<a id="download-verify-install"></a>
## डाउनलोड करा, सत्यापित करा, स्थापित करा

1. निवडलेल्या प्रकाशित रिलीझवर, त्याची नामांकित ॲप्लिकेशन मालमत्ता, नोटिस ZIP आणि SHA256SUMS.txt डाउनलोड करा.
2. [SHA-256 उदाहरण](downloads.md#sha-256) वापरा, वास्तविक डाउनलोड केलेल्या फाइलनावासह.
3. सेटअपसाठी, सामान्य इंस्टॉलरचे अनुसरण करा. पोर्टेबल झिपसाठी, नवीन स्थानिक लेखन करण्यायोग्य फोल्डरमध्ये सर्वकाही काढा; झिपच्या आतून धावू नका.
4. अनुप्रयोगाचे स्वतःचे EXE उघडा. परवाना/कॉन्फिगरेशन/डेटा फाइल्स सोबत ठेवा.
5. सेटिंग्ज किंवा सिस्टम ऑपरेशन्स सक्षम करण्यापूर्वी त्या टूलच्या वापराच्या सूचना वाचा.

वर्तमान बायनरी स्वाक्षरी नसलेल्या आहेत. जुळणारे हॅश अपेक्षित बाइट्सची पुष्टी करते; हे सुरक्षा किंवा सुसंगतता प्रमाणपत्र नाही. फक्त चेतावणी दडपण्यासाठी Windows सुरक्षा संरक्षण अक्षम करू नका.

NVDF किंवा त्याचा पर्यायी NVPI सहचर स्थापित करणे GPU ड्राइव्हर स्थापित करण्यापेक्षा वेगळे आहे. NVPI सहचर त्याचे विद्यमान अंतर्गत प्रतिष्ठापन नाव ठेवते. त्याच्या एलिव्हेटेड रास्टरपल्स बटणासाठी संरक्षित सिस्टम-व्यापी स्थापना आवश्यक आहे; इतर RP कॉपी त्यांच्या स्वतःच्या शॉर्टकटद्वारे उघडल्या जाऊ शकतात.

NVMFG प्रायोगिक आहे आणि त्यात [दस्तऐवजीकरण NVIDIA SDK परवाना राखीव](provenance.md) आहे. कोणताही NVIDIA ड्राइव्हर, NGX प्रदाता/मॉडेल किंवा गेम Streamline रनटाइम समाविष्ट केलेला नाही. निवडलेले SDK डाउनलोड आणि गेम अपडेट्स स्पष्टपणे स्वतंत्र ऑपरेशन्स आहेत.

<a id="language-and-updates"></a>
## भाषा आणि अद्यतने

दस्तऐवजीकरणासाठी README चे 34-भाषा निवडक वापरा. NVDF, NVMFG आणि RP ची स्वतःची 34-भाषा UI सेटिंग आहे; NVPI त्याचे विद्यमान भाषा समर्थन ठेवते. काही इंस्टॉलर तांत्रिक स्ट्रिंग इंग्रजीमध्ये परत येतात.

अपडेट करताना टूलची इन्स्टॉलेशन ओळख ठेवा. प्रथम ते बंद करा आणि बॅकअप जतन करा. NVMFG साठी, प्रभावित गेम बंद करा आणि प्रलंबित प्रोफाइल पुनर्प्राप्तीचे निराकरण करा. पोर्टेबल अपडेटसाठी, रिलीझ एकत्र करण्याऐवजी नवीन फोल्डर वापरा.

<a id="removing-a-tool"></a>
## एक साधन काढत आहे

ॲप्लिकेशन अनइन्स्टॉल केल्याने त्याची सेटिंग्ज आपोआप पूर्ववत होत नाहीत.

- **NVPI:** आवश्यक असल्यास काढून टाकण्यापूर्वी इच्छित प्रोफाइल/डिस्प्ले सेटिंग्ज पुनर्संचयित करा.
- **NVDF:** तुम्हाला प्रगत/NVENC बदल पुनर्संचयित करायचे असल्यास प्रथम पुनर्प्राप्ती वापरा. Uninstall ग्राफिक्स ड्रायव्हर, सेटिंग्ज आणि बॅकअप सोडते.
- **NVMFG:** गेम बंद करा, कंट्रोलर अक्षम करा/बाहेर पडा, NVIDIA पुनर्प्राप्तीचे निराकरण करा आणि काढून टाकण्यापूर्वी इच्छित गेम SDK बॅकअप पुनर्संचयित करा.
- **RP:** प्रथम इच्छित लिमिटर ओव्हरराइड काढून टाका. Uninstall जतन केलेल्या RTSS कॅप्स मिटवत नाही किंवा RTSS काढून टाकत नाही.

अचूक डेटा स्थाने आणि मर्यादांसाठी प्रत्येक [प्रकल्प मार्गदर्शक](../README.md#projects) किंवा पुनर्प्राप्ती चरण अयशस्वी झाल्यास [समर्थन](support.md) पहा.
