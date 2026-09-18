<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · **मराठी** · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> इंग्रजीतून मशीन-सहाय्यित भाषांतर. तांत्रिक नावे, आदेश, URL आणि मूळ कायदेशीर मजकूर जतन केले आहेत. नेटिव्ह-स्पीकर पुनरावलोकन स्वागतार्ह आहे; शब्द अस्पष्ट असल्यास इंग्रजी संदर्भ पहा.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# प्रकाशन आणि प्रकाशन

सार्वजनिक भांडार **झेंडो-जीआयटी/एनव्ही-प्रयोगशाळा** आहे. **GitHub Desktop** सह मेंटेनरद्वारे दस्तऐवजीकरणातील बदलांचे पुनरावलोकन, वचनबद्ध आणि पुश केले जाते. स्थानिक कमिट फाइल अपलोड करत नाही. बायनरी पॅकेजेस स्वतंत्र GitHub रिलीझ मालमत्ता आहेत; ते कधीही Git बदलांच्या यादीत नाहीत.

<a id="documentation-updates"></a>
## दस्तऐवजीकरण अद्यतने

1. GitHub Desktop मध्ये **NV-Laboratory** फोल्डर उघडा.
2. दस्तऐवजीकरण, सूचना, प्रतिमा, JSON मेटाडेटा आणि दस्तऐवजीकरण प्रमाणीकरणाचे पुनरावलोकन करा.
3. त्या फोल्डरमधून `python tools/validate_repository.py` चालवा.
4. पुनरावलोकन केलेले बदल करा, नंतर **Push origin** वापरा. क्रिया परिणाम तपासा.
5. सार्वजनिक लेखकाची ओळख **禅堂 Zendo (RevoluSound Team)** आणि खात्याचा GitHub `noreply` पत्ता ठेवा.

पालक विकास कार्यक्षेत्र, खाजगी ऑडिट निर्देशिका किंवा बायनरी संलग्नक निर्देशिका कधीही निवडू नका. [ईमेल गोपनीयता वचनबद्ध](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## स्वतंत्र अनुप्रयोग प्रकाशन

| साधन | टॅग करा | आवृत्ती धोरण |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | विद्यमान चार-भाग अनुप्रयोग आवृत्ती; सेटअप पुनरावृत्ती 2 चे स्वतःचे फाइलनाव आहे |
| NVDriverForge | nvdriverforge-v0.1.4 | विद्यमान 0.x योजना; आवृत्ती केलेले अद्यतने पूर्वीचे पॅकेज संरक्षित करतात |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | ऍप्लिकेशन आवृत्ती 0.2.3; सार्वजनिक 0.1.1 पासून एकत्रित बदल |
| NVRasterPulse | nvrasterpulse-v0.2 | विद्यमान दोन-भाग आवृत्ती |

देखरेख करणारा थेट प्रकाशित करू शकतो किंवा लेखापरीक्षित मालमत्ता प्रकाशित करण्यासाठी सहाय्यकाला अधिकृत करू शकतो. प्रकाशन स्पष्ट आहे; कोणताही वर्कफ्लो प्रत्येक कमिटवर रिलीझ तयार करत नाही.

1. वर्तमान पूर्वप्रकाशन अहवाल, बायनरींचे स्रोत, परवाने आणि SHA-256 मूल्यांचे पुनरावलोकन करा.
2. पुनरावलोकन केलेल्या हब कमिटला लक्ष्य करून टूलच्या टॅगसाठी मसुदा तयार करा. तयार आवृत्ती-विशिष्ट प्रकाशन नोट्स समाविष्ट करा.
3. फक्त त्या आवृत्तीचे सेटअप/पोर्टेबल मालमत्ता, `Licenses-and-Credits.zip` आणि `SHA256SUMS.txt` संलग्न करा.
4. सुसंगतता, स्थापना, अवलंबित्व, बदल आणि ज्ञात मर्यादा तपासा. NVRasterPulse साठी RTSS प्रमुख ठेवा.
5. सार्वजनिक मालमत्ता URL, आकार आणि हॅश प्रकाशित करा, सत्यापित करा आणि `docs/releases.json` मध्ये वास्तविक प्रकाशन तारीख रेकॉर्ड करा.
6. डाउनलोड पृष्ठे आणि भाषांतरे अद्यतनित करा, नंतर GitHub Desktop मध्ये त्यांचे बदल कमिट/पुश करा.

प्रति-प्रोजेक्ट टॅग लिंक्स वापरकर्त्यांना सामायिक केलेल्या `releases/latest` लिंकद्वारे दुसऱ्या टूलवर पाठवणे टाळतात. GitHub च्या स्वयंचलित **Source code** संग्रहांमध्ये हे दस्तऐवजीकरण हब आहे. अर्जाचे स्रोत खाजगी राहतात. मूळ घटक सूचना अबाधित राहतील, आणि प्रकाशन NVMFG च्या दस्तऐवजीकरण केलेल्या NVIDIA SDK रिझर्व्हचे निराकरण करत नाही.


18 सप्टेंबरचे अपडेट तीन नवीन टॅग तयार करते; विद्यमान Profile Inspector रिलीझ अपरिवर्तित राहते. ॲप्लिकेशन अपडेट तपासणीसाठी मालमत्तेची नावे, टॅग आणि `SHA256SUMS.txt` अचूक असणे आवश्यक आहे. प्री-रिलीझ ध्वजशिवाय सामान्य प्रकाशन प्रकाशित करा त्यांना स्थिर-रिलीझ चेकमध्ये उघड करण्यासाठी; NVMFG प्रायोगिक राहते.

<a id="integrity-and-storage"></a>
## अखंडता आणि स्टोरेज

प्रकाशित बायनरी बाइट्स कधीही शांतपणे बदलू नका. नवीन हॅशसह नवीन स्पष्ट आवृत्ती किंवा इंस्टॉलर पुनरावृत्ती वापरा. कायदेशीर साइडकार एम्बेड केलेल्या नोटिसांना पूरक आहेत. NVDriverForge 0.1.4 पोर्टेबल 142,017,891 बाइट्स आहे, GitHub च्या सामान्य 100 MiB Git-फाइल मर्यादेपेक्षा जास्त आहे. रिलीझ अटॅचमेंट या हबमध्ये बायनरी किंवा Git LFS टाकणे टाळतात. [GitHub मोठ्या-फाइल मार्गदर्शन](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

रेपॉजिटरी सुरक्षा सेटिंग्जमध्ये खाजगी असुरक्षा अहवाल सक्षम केले जावे. तेथे संवेदनशील अहवाल निर्देशित करण्यापूर्वी त्याची उपलब्धता सत्यापित करा; [SECURITY.md](../SECURITY.md) एक फॉलबॅक प्रदान करते जे भेद्यतेचे तपशील उघड करत नाही.

[कॅटलॉग डाउनलोड करा](downloads.md) · [GitHub प्रकाशन दस्तऐवजीकरण](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
