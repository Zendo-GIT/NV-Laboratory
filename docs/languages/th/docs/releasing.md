<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · **ไทย** · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> เครื่องช่วยแปลจากภาษาอังกฤษ ชื่อทางเทคนิค คำสั่ง URL และข้อความทางกฎหมายต้นฉบับจะยังคงอยู่ ยินดีรับฟังความคิดเห็นจากเจ้าของภาษา ปรึกษาการอ้างอิงภาษาอังกฤษหากถ้อยคำไม่ชัดเจน
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# การเผยแพร่และการเผยแพร่

พื้นที่เก็บข้อมูลสาธารณะคือ **Zendo-GIT/NV-Laboratory** การเปลี่ยนแปลงเอกสารจะได้รับการตรวจสอบ กระทำ และผลักดันโดยผู้ดูแลด้วย **GitHub Desktop** คอมมิตท้องถิ่นไม่ได้อัปโหลดไฟล์ แพ็คเกจไบนารีเป็นสินทรัพย์ที่เผยแพร่ GitHub แยกกัน ไม่เคยอยู่ในรายการการเปลี่ยนแปลง Git

<a id="documentation-updates"></a>
## การปรับปรุงเอกสาร

1. เปิดโฟลเดอร์ **NV-Laboratory** ใน GitHub Desktop
2. ตรวจสอบเอกสาร ประกาศ รูปภาพ ข้อมูลเมตา JSON และผู้ตรวจสอบเอกสาร
3. เรียกใช้ `python tools/validate_repository.py` จากโฟลเดอร์นั้น
4. ยอมรับการเปลี่ยนแปลงที่ตรวจสอบแล้ว จากนั้นใช้ **Push origin** ตรวจสอบผลการดำเนินการ
5. รักษาข้อมูลประจำตัวผู้เขียนสาธารณะ **禅堂 Zendo (RevoluSound Team)** และที่อยู่ GitHub `noreply` ของบัญชี

อย่าเลือกพื้นที่ทำงานการพัฒนาพาเรนต์ ไดเร็กทอรีการตรวจสอบส่วนตัว หรือไดเร็กทอรีไฟล์แนบแบบไบนารี [ยืนยันความเป็นส่วนตัวของอีเมล](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## การเปิดตัวแอปพลิเคชันอิสระ

| เครื่องมือ | แท็ก | นโยบายเวอร์ชัน |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | เวอร์ชันแอปพลิเคชันสี่ส่วนที่มีอยู่ การตั้งค่าการแก้ไข 2 มีชื่อไฟล์ของตัวเอง |
| NVDriverForge | nvdriverforge-v0.1.3 | รูปแบบ 0.x ที่มีอยู่ การอัปเดตเวอร์ชันจะรักษาแพ็คเกจก่อนหน้านี้ |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | ผู้สมัคร UI2 ระบุด้วยแฮชที่แน่นอนโดยไม่ต้องสร้างแอปพลิเคชันเวอร์ชันใหม่ |
| NVRasterPulse | nvrasterpulse-v0.1 | รุ่นสองส่วนที่มีอยู่ |

ผู้ดูแลสามารถเผยแพร่โดยตรงหรืออนุญาตให้ผู้ช่วยเผยแพร่สินทรัพย์ที่ได้รับการตรวจสอบได้ สิ่งพิมพ์มีความชัดเจน ไม่มีเวิร์กโฟลว์สร้าง Release ในแต่ละคอมมิต

1. ตรวจสอบรายงานการเผยแพร่ล่วงหน้าปัจจุบัน แหล่งที่มาของไบนารี ใบอนุญาต และค่า SHA-256
2. สร้างแบบร่างสำหรับแท็กของเครื่องมือ โดยกำหนดเป้าหมายไปที่คอมมิตฮับที่ได้รับการตรวจสอบ รวมบันทึกประจำรุ่นเฉพาะเวอร์ชันที่เตรียมไว้
3. แนบเฉพาะเนื้อหาการตั้งค่า/พกพาของเวอร์ชันนั้น `Licenses-and-Credits.zip` และ `SHA256SUMS.txt`
4. ตรวจสอบความเข้ากันได้ การติดตั้ง การขึ้นต่อกัน การเปลี่ยนแปลง และขีดจำกัดที่ทราบ ให้ RTSS โดดเด่นสำหรับ NVRasterPulse
5. เผยแพร่ ตรวจสอบ URL ของสินทรัพย์สาธารณะ ขนาด และแฮช และบันทึกวันที่เผยแพร่จริงใน `docs/releases.json`
6. อัปเดตหน้าดาวน์โหลดและการแปล จากนั้นยอมรับ/พุชการเปลี่ยนแปลงใน GitHub Desktop

ลิงก์แท็กต่อโปรเจ็กต์หลีกเลี่ยงการส่งผู้ใช้ไปยังเครื่องมืออื่นผ่านลิงก์ `releases/latest` ที่ใช้ร่วมกัน ไฟล์เก็บถาวร **Source code** อัตโนมัติของ GitHub มีฮับเอกสารนี้ แหล่งที่มาของแอปพลิเคชันยังคงเป็นส่วนตัว ประกาศส่วนประกอบดั้งเดิมยังคงไม่เสียหาย และการเผยแพร่ไม่สามารถแก้ไขการสำรอง NVIDIA SDK ที่เป็นเอกสารของ NVMFG

<a id="integrity-and-storage"></a>
## ความสมบูรณ์และการเก็บรักษา

อย่าแทนที่ไบต์ไบนารีที่เผยแพร่อย่างเงียบๆ ใช้เวอร์ชันที่ชัดเจนหรือการแก้ไขตัวติดตั้งใหม่พร้อมแฮชใหม่ รถเทียมข้างรถจักรยานยนต์ทางกฎหมายเสริมประกาศที่ฝังอยู่ NVDriverForge 0.1.3 แบบพกพามีขนาด 141,760,351 ไบต์ ซึ่งสูงกว่าขีดจำกัดไฟล์ Git 100 MiB ทั่วไปของ GitHub ปล่อยไฟล์แนบหลีกเลี่ยงการใส่ไบนารีหรือ Git LFS ในฮับนี้ [คำแนะนำเกี่ยวกับไฟล์ขนาดใหญ่ GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

ควรเปิดใช้งานการรายงานช่องโหว่ส่วนตัวในการตั้งค่าความปลอดภัยของพื้นที่เก็บข้อมูล ตรวจสอบความพร้อมใช้งานก่อนที่จะส่งรายงานที่ละเอียดอ่อนไปที่นั่น [SECURITY.md](../SECURITY.md) จัดเตรียมทางเลือกสำรองที่ไม่เปิดเผยรายละเอียดเกี่ยวกับช่องโหว่

[ดาวน์โหลดแคตตาล็อก](downloads.md) · [เอกสารการเปิดตัว GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
