<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · **ไทย** · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> เครื่องช่วยแปลจากภาษาอังกฤษ ชื่อทางเทคนิค คำสั่ง URL และข้อความทางกฎหมายต้นฉบับจะยังคงอยู่ ยินดีรับฟังความคิดเห็นจากเจ้าของภาษา ปรึกษาการอ้างอิงภาษาอังกฤษหากถ้อยคำไม่ชัดเจน
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools โดย 禅堂 Zendo (RevoluSound Team)** ยูทิลิตี้ Windows อิสระสี่รายการสำหรับโปรไฟล์ไดรเวอร์ NVIDIA การติดตั้งไดรเวอร์ ขีดจำกัดเฟรม Multi Frame Generation และ RTSS รุ่นทดลอง

[รับเครื่องมือ](docs/downloads.md) · [การติดตั้ง](docs/installation.md) · [ความเข้ากันได้และความช่วยเหลือ](docs/support.md) · [เครดิตและใบอนุญาต](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse ต้องใช้ RTSS** ติดตั้ง [RivaTuner Statistics Server จาก Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) ก่อน RTSS ต้องทำงานอยู่เพื่อให้ขีดจำกัดของ FPS ทำงานได้ มันถูกดาวน์โหลดแยกต่างหาก

<a id="projects"></a>
## โครงการ

| โครงการ | วัตถุประสงค์ | เวอร์ชัน | เอกสารประกอบ | ดาวน์โหลด |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | ตัวแก้ไขโปรไฟล์ไดรเวอร์ NVIDIA พร้อมเพิ่มจอแสดงผล สี การควบคุม HDR และ ICC/WCS ชื่อเดิม NVPI Custom. | 3.0.2.3 | [คู่มือ](NVIDIA-Profile-Inspector/README.md) | [แพ็คเกจ](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | เลือกส่วนประกอบไดรเวอร์ ตรวจสอบการปรับแต่งเพิ่มเติม และติดตั้งแพ็คเกจไดรเวอร์ NVIDIA ดั้งเดิม | 0.1.3 | [คู่มือ](NVDriverForge/README.md) | [แพ็คเกจ](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | เครื่องมือ RTX รุ่นทดลอง 40 MFG พร้อมตัวเลือกต่อเกมและการบำรุงรักษา Streamline SDK | 0.1.1 | [คู่มือ](NVMFG-Unlock40/README.md) | [แพ็คเกจและสถานะ](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | จัดการขีดจำกัด RTSS FPS ต่อการดำเนินการด้วยค่าเศษส่วน การสำรองข้อมูล และการเข้าถึงถาด | 0.1 | [คู่มือ](NVRasterPulse/README.md) | [แพ็คเกจ](docs/downloads.md#nvrasterpulse) |

**การดาวน์โหลด:** [หน้าดาวน์โหลด](docs/downloads.md) แสดงรายการสถานะ ไฟล์ และค่า SHA-256 ของแต่ละเวอร์ชัน คุณลักษณะการทดลองและขีดจำกัดความเข้ากันได้อธิบายไว้ในคู่มือโครงการ

<a id="start-here"></a>
## เริ่มที่นี่

1. เลือกเครื่องมือหนึ่งรายการด้านบน แต่ละงานทำงานอย่างอิสระ ไม่จำเป็นต้องติดตั้งทั้งชุด
2. อ่านข้อกำหนดและเลือก **ตั้งค่า** สำหรับแอปที่ติดตั้ง หรือ **พกพา** สำหรับโฟลเดอร์แยกต่างหาก
3. เมื่อมีการเผยแพร่การเผยแพร่ ให้ดาวน์โหลดเนื้อหาแอปพลิเคชันที่มีชื่อ อ่านประกาศที่แนบมา และเปรียบเทียบ SHA-256
4. เก็บข้อมูลสำรองก่อนที่จะเปลี่ยนไดรเวอร์ การตั้งค่าการแสดงผล โปรไฟล์ NVIDIA หรือรันไทม์ของเกม

เอกสารประกอบมีให้บริการใน 34 ภาษาเดียวกับการสมัคร NV ผ่านตัวเลือกที่ด้านบนของแต่ละคู่มือ GitHub จะไม่เลือก README ตามภาษาของเบราว์เซอร์โดยอัตโนมัติ ภาษาเอกสารและการตั้งค่าภาษาของแอปพลิเคชันจะแยกจากกัน

<a id="provenance-and-ownership"></a>
## แหล่งที่มาและความเป็นเจ้าของ

ฮับนี้แจกจ่ายเอกสารและแอปพลิเคชันที่คอมไพล์แล้ว ซอร์สโค้ดของแอปพลิเคชันได้รับการดูแลแบบส่วนตัว โครงการต้นน้ำยังคงรักษาการประพันธ์และใบอนุญาต การเผยแพร่แหล่งส่วนตัวไม่ได้แทนที่ข้อกำหนดเหล่านั้น

- Profile Inspector fork ยังคงสิทธิ์การใช้งาน MIT ของ Orbmu2k และได้รับการระบุอย่างชัดเจนว่าเป็น fork
- NVDriverForge มีข้อกำหนดการจำหน่ายไบนารีของตัวเอง และรวมถึงรันไทม์/ส่วนประกอบเครื่องมือที่ได้รับลิขสิทธิ์แยกต่างหาก
- NVMFG Unlock40 เป็นแอปพลิเคชันที่พัฒนาขึ้นอย่างอิสระ RTX40MFG-Unlock ได้รับการปรึกษาเพื่อการเปรียบเทียบและการปรับแต่ง ส่วนประกอบดั้งเดิมที่ใช้ร่วมกันจะรักษาเครดิต MIT ไว้ เงื่อนไขของ MinHook และ NVIDIA SDK ยังคงแยกจากกัน
- NVRasterPulse ยังคงสิทธิ์การใช้งาน MIT ที่ให้มา และให้เครดิต UI ที่ได้รับจาก Profile Inspector RTSS เป็นโปรแกรมภายนอกที่จำเป็น

ดู [ตารางส่วนประกอบที่สมบูรณ์](THIRD_PARTY_NOTICES.md), [แหล่งที่มาของไฟล์และการเปลี่ยนแปลง](docs/provenance.md) และ [ขอบเขตใบอนุญาต](../../../LICENSE)

<a id="other-projects--revolusound-team"></a>
## โครงการอื่นๆ – RevoluSound Team

โปรเจ็กต์ม็อดเสียงเหล่านี้เป็นโปรเจ็กต์ม็อดเสียงที่แยกจากกัน ซึ่งมีลิงก์อยู่ที่นี่เพื่อช่วยให้คุณค้นพบผลงานของทีม

| เกม | โครงการ | เกี่ยวกับ |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | การเปลี่ยนแปลงเสียงของยานพาหนะครอบคลุมถึงเครื่องยนต์ ไอเสีย ไอดี และเอฟเฟกต์เทอร์โบ |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | ชุดเครื่องเสียงติดรถยนต์ FH5 รุ่นต่อมาของทีม |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | แพ็ค FH5 รุ่นก่อนหน้า; หน้า Nexus นำผู้เยี่ยมชมไปยังชุดทีมในภายหลังด้านบน |

ชื่อเรื่องเป็นไปตามหน้า Nexus Mods ที่ลิงก์ไว้ การดาวน์โหลด ข้อกำหนด เครดิต และการอนุญาตยังคงอยู่ใน Nexus Mods

<a id="help-and-participation"></a>
## ความช่วยเหลือและการมีส่วนร่วม

[รายงานข้อบกพร่องหรือแนะนำคุณสมบัติ](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [มีส่วนร่วม](CONTRIBUTING.md) · [รายงานความปลอดภัย](SECURITY.md) · [บันทึกการเปลี่ยนแปลง](CHANGELOG.md)

สำหรับปัญหาด้านความปลอดภัย โปรดอ่าน SECURITY.md ก่อนที่จะโพสต์บันทึกหรือรายละเอียดทางเทคนิค ผู้ดูแลจะต้องเปิดใช้งานการรายงานส่วนตัวหลังจากการเผยแพร่ที่เก็บข้อมูล

> **โครงการชุมชนอิสระ** NV Laboratory, NV Tools และสาธารณูปโภคเหล่านี้ไม่มีส่วนเกี่ยวข้องกับ สนับสนุนโดย หรือรับรองอย่างเป็นทางการโดย NVIDIA Corporation NVIDIA, GeForce, RTX, DLSS และชื่อผลิตภัณฑ์อื่นๆ เป็นเครื่องหมายการค้าของเจ้าของที่เกี่ยวข้อง ชื่ออธิบายถึงความเข้ากันได้และที่มา ไม่ใช่การรับรองอย่างเป็นทางการ
