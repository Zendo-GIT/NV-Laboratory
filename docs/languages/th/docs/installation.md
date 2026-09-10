<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · **ไทย** · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> เครื่องช่วยแปลจากภาษาอังกฤษ ชื่อทางเทคนิค คำสั่ง URL และข้อความทางกฎหมายต้นฉบับจะยังคงอยู่ ยินดีรับฟังความคิดเห็นจากเจ้าของภาษา ปรึกษาการอ้างอิงภาษาอังกฤษหากถ้อยคำไม่ชัดเจน
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# คู่มือการติดตั้ง

เริ่มต้นด้วย [ดาวน์โหลด](downloads.md) ซึ่งบันทึกสถานะการตีพิมพ์และชื่อเนื้อหาที่แน่นอน เครื่องมือเหล่านี้แยกจากกัน: ติดตั้งเฉพาะเครื่องมือที่คุณต้องการเท่านั้น

> **สำหรับ NVRasterPulse ให้ติดตั้ง [RTSS จาก Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) ก่อนเปิดตัวจัดการโปรไฟล์**
> RTSS ต้องรันเพื่อใช้ขีดจำกัด ไม่รวมอยู่ใน NV Tools

| เครื่องมือ | รุ่นติดตั้ง | รุ่นพกพา | ข้อกำหนดเบื้องต้นหลัก |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | แตกไฟล์ ZIP NVPI ให้สมบูรณ์ | ไดรเวอร์ NVIDIA และ .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe รวมรันไทม์ด้วย | แพ็คเกจไดรเวอร์ NVIDIA ดั้งเดิมที่เข้ากันได้สำหรับการดำเนินการติดตั้ง |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | แตกไฟล์ NVMFG ZIP ให้สมบูรณ์ และเก็บโฟลเดอร์ย่อยไว้ | RTX 40, DLSS FG ที่มีอยู่, ผู้ให้บริการที่แน่นอนและตัวช่วย .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | แตกไฟล์ ZIP RP ให้สมบูรณ์ | RTSS และ .NET Framework 4.8 |

<a id="download-verify-install"></a>
## ดาวน์โหลด ตรวจสอบ ติดตั้ง

1. ในรุ่นที่เผยแพร่ที่เลือก ให้ดาวน์โหลดเนื้อหาแอปพลิเคชันที่มีชื่อ ประกาศ ZIP และ SHA256SUMS.txt
2. ใช้ [ตัวอย่าง SHA-256](downloads.md#sha-256) พร้อมด้วยชื่อไฟล์ที่ดาวน์โหลดจริง
3. สำหรับการตั้งค่า ให้ปฏิบัติตามตัวติดตั้งปกติ สำหรับ ZIP แบบพกพา ให้แตกไฟล์ทุกอย่างลงในโฟลเดอร์ที่สามารถเขียนได้ในเครื่องใหม่ อย่าวิ่งจากภายใน ZIP
4. เปิด EXE ของแอปพลิเคชันเอง เก็บไฟล์ใบอนุญาต/การกำหนดค่า/ข้อมูลที่แนบมาด้วย
5. อ่านคำแนะนำการใช้งานเครื่องมือนั้นก่อนเปิดใช้งานการตั้งค่าหรือการทำงานของระบบ

ไบนารีปัจจุบันไม่ได้ลงนาม แฮชที่ตรงกันจะยืนยันไบต์ที่คาดหวัง ไม่ใช่ใบรับรองความปลอดภัยหรือความเข้ากันได้ อย่าปิดใช้งานการป้องกันความปลอดภัย Windows เพียงเพื่อระงับคำเตือน

การติดตั้ง NVDF หรืออุปกรณ์เสริม NVPI จะแยกจากการติดตั้งไดรเวอร์ GPU ตัวช่วย NVPI จะเก็บชื่อการติดตั้งภายในที่มีอยู่ไว้ ปุ่ม RasterPulse ที่ยกระดับต้องมีการติดตั้งทั่วทั้งระบบที่ได้รับการป้องกัน สำเนา RP อื่นๆ สามารถเปิดได้โดยใช้ทางลัดของตัวเอง

NVMFG อยู่ระหว่างการทดลองและมี [เอกสารสำรองลิขสิทธิ์ NVIDIA SDK](provenance.md) ไม่มีไดรเวอร์ NVIDIA, ผู้ให้บริการ/รุ่น NGX หรือรันไทม์เกม Streamline รวมอยู่ด้วย การดาวน์โหลด SDK และการอัปเดตเกมที่เลือกเป็นการดำเนินการที่แยกจากกันอย่างชัดเจน

<a id="language-and-updates"></a>
## ภาษาและการอัพเดต

ใช้ตัวเลือก 34 ภาษาของ README สำหรับเอกสารประกอบ NVDF, NVMFG และ RP มีการตั้งค่า UI 34 ภาษาของตัวเอง NVPI ยังคงรองรับภาษาที่มีอยู่ สตริงทางเทคนิคของตัวติดตั้งบางตัวจะกลับไปเป็นภาษาอังกฤษ

คงเอกลักษณ์การติดตั้งของเครื่องมือไว้เมื่อทำการอัพเดต ปิดก่อนและสำรองข้อมูลสำรองไว้ สำหรับ NVMFG ให้ปิดเกมที่ได้รับผลกระทบและแก้ไขการกู้คืนโปรไฟล์ที่รอดำเนินการ สำหรับการอัพเดตแบบพกพา ให้ใช้โฟลเดอร์ใหม่แทนการรวมรุ่นต่างๆ

<a id="removing-a-tool"></a>
## การถอดเครื่องมือ

การถอนการติดตั้งแอปพลิเคชันจะไม่ยกเลิกการตั้งค่าโดยอัตโนมัติ

- **NVPI:** คืนค่าโปรไฟล์/การตั้งค่าการแสดงผลที่ต้องการก่อนที่จะลบออก หากจำเป็น
- **NVDF:** ใช้การกู้คืนก่อน หากคุณต้องการกู้คืนการเปลี่ยนแปลงขั้นสูง/NVENC Uninstall ออกจากไดรเวอร์กราฟิก การตั้งค่า และการสำรองข้อมูล
- **NVMFG:** ปิดเกม ปิดการใช้งาน/ออกจากคอนโทรลเลอร์ แก้ไขการกู้คืน NVIDIA และกู้คืนข้อมูลสำรอง SDK ของเกมที่ต้องการก่อนที่จะลบออก
- **RP:** ลบการแทนที่ตัวจำกัดที่ต้องการออกก่อน Uninstall จะไม่ลบแคป RTSS ที่บันทึกไว้หรือลบ RTSS

ดู [คู่มือโครงการ](../README.md#projects) แต่ละตัวเพื่อดูตำแหน่งข้อมูลและข้อจำกัดที่แน่นอน หรือดู [สนับสนุน](support.md) หากขั้นตอนการกู้คืนล้มเหลว
