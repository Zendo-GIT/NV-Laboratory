<!-- nv-language-navigation:start -->
🌐 [English](../../../SECURITY.md) | [Français](../fr/SECURITY.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/SECURITY.md) · [বাংলা](../bn/SECURITY.md) · [简体中文](../zh/SECURITY.md) · [Čeština](../cs/SECURITY.md) · [Dansk](../da/SECURITY.md) · [Nederlands](../nl/SECURITY.md) · [English](../../../SECURITY.md) · [Filipino](../fil/SECURITY.md) · [Suomi](../fi/SECURITY.md) · [Français](../fr/SECURITY.md) · [Deutsch](../de/SECURITY.md) · [Ελληνικά](../el/SECURITY.md) · [हिन्दी](../hi/SECURITY.md) · [Magyar](../hu/SECURITY.md) · [Bahasa Indonesia](../id/SECURITY.md) · [Italiano](../it/SECURITY.md) · [日本語](../ja/SECURITY.md) · [한국어](../ko/SECURITY.md) · [मराठी](../mr/SECURITY.md) · [فارسی](../fa/SECURITY.md) · [Polski](../pl/SECURITY.md) · [Português](../pt/SECURITY.md) · [ਪੰਜਾਬੀ](../pa/SECURITY.md) · [Română](../ro/SECURITY.md) · [Русский](../ru/SECURITY.md) · [Español](../es/SECURITY.md) · [Kiswahili](../sw/SECURITY.md) · [Svenska](../sv/SECURITY.md) · [தமிழ்](../ta/SECURITY.md) · **ไทย** · [Türkçe](../tr/SECURITY.md) · [Українська](../uk/SECURITY.md) · [اردو](../ur/SECURITY.md) · [Tiếng Việt](../vi/SECURITY.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> เครื่องช่วยแปลจากภาษาอังกฤษ ชื่อทางเทคนิค คำสั่ง URL และข้อความทางกฎหมายต้นฉบับจะยังคงอยู่ ยินดีรับฟังความคิดเห็นจากเจ้าของภาษา ปรึกษาการอ้างอิงภาษาอังกฤษหากถ้อยคำไม่ชัดเจน
<!-- nv-translation-notice:end -->

<a id="security"></a>
# ความปลอดภัย

นโยบายนี้ครอบคลุมแพ็คเกจแอปพลิเคชัน NV Tools และฮับการจัดจำหน่ายนี้ ผู้ดูแลจัดลำดับความสำคัญของรายงานที่ส่งผลต่อเวอร์ชันที่เผยแพร่ล่าสุดของแต่ละเครื่องมือ ผู้สมัครที่เตรียมไว้ไม่ใช่รุ่นเสถียรที่ประกาศรองรับ ไม่มีกำหนดเวลาตอบกลับหรือการรับรองความปลอดภัย

<a id="report-privately"></a>
## รายงานเป็นการส่วนตัว

สำหรับช่องโหว่ พฤติกรรมระดับสูงที่ไม่ปลอดภัย การเปลี่ยนแปลงแบบทำลายโดยไม่ตั้งใจ หรือการเปิดเผยข้อมูลที่ละเอียดอ่อน ให้ใช้ฟีเจอร์ **ความปลอดภัย → Report a vulnerability** ของพื้นที่เก็บข้อมูล **เมื่อเปิดใช้งาน**: [รายงานส่วนตัว](https://github.com/Zendo-GIT/NV-Laboratory/security/advisories/new)

**การตั้งค่าเริ่มต้น:** ผู้ดูแลต้องเปิดใช้งานการรายงานช่องโหว่ส่วนตัวหลังจากสร้างพื้นที่เก็บข้อมูลสาธารณะ ไฟล์นี้ไม่ได้เปิดใช้งาน และไม่มีกล่องจดหมายหรือช่องทางส่วนตัวที่อ้างว่ามีอยู่ก่อนหน้านั้น

หากปุ่มไม่พร้อมใช้งาน ให้เปิดปัญหาสาธารณะที่มีเฉพาะ: “ฉันต้องการช่องทางการติดต่อส่วนตัวสำหรับรายงานความปลอดภัยที่เกี่ยวข้องกับ [เครื่องมือ/เวอร์ชัน]” อย่าใส่รายละเอียดการหาประโยชน์ ข้อมูลประจำตัว เส้นทางที่ได้รับผลกระทบ บันทึก หรือไฟล์แนบ รอให้ผู้ดูแลระบุช่องส่วนตัวก่อนจะแชร์

ในรายงานส่วนตัว ให้ระบุเครื่องมือ/เวอร์ชันและแฮช เวอร์ชัน Windows/GPU/ไดรเวอร์ ผลกระทบ การสร้างความปลอดภัยขั้นต่ำ และจำเป็นต้องกู้คืนหรือไม่ ปกปิดความลับและข้อมูลส่วนบุคคล รักษาไฟล์การกู้คืนในเครื่อง อย่าอัปโหลดไดรเวอร์ที่เป็นกรรมสิทธิ์หรือ DLLs ของเกม ประสานงานการเปิดเผยข้อมูลกับผู้ดูแล แพตช์/รีลีสต้องมีการตรวจสอบและจะไม่เกิดขึ้นโดยอัตโนมัติ


[เอกสารการรายงานส่วนตัว GitHub](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
