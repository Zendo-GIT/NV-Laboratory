<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · **ไทย** · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> เครื่องช่วยแปลจากภาษาอังกฤษ ชื่อทางเทคนิค คำสั่ง URL และข้อความทางกฎหมายต้นฉบับจะยังคงอยู่ ยินดีรับฟังความคิดเห็นจากเจ้าของภาษา ปรึกษาการอ้างอิงภาษาอังกฤษหากถ้อยคำไม่ชัดเจน
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# มีส่วนร่วม

NV Laboratory ได้รับการดูแลโดย 禅堂 Zendo (RevoluSound Team) ผู้ดูแลเป็นผู้ตัดสินใจว่าจะยอมรับและปล่อยสิ่งใด การเปิดประเด็นหรือดึงคำขอไม่ได้หมายความว่าการบริจาคจะได้รับการยอมรับหรือได้รับอนุญาตให้แจกจ่าย

ใช้แบบฟอร์มข้อบกพร่องหรือคุณลักษณะและระบุโปรแกรม/เวอร์ชัน ค้นหาปัญหาที่มีอยู่ก่อน หารือเกี่ยวกับการเปลี่ยนแปลงที่สำคัญก่อนเตรียมการสนับสนุนครั้งใหญ่ สำหรับเรื่องความปลอดภัย ให้ปฏิบัติตาม [SECURITY.md](SECURITY.md)

ฮับสาธารณะนี้ประกอบด้วยเอกสาร ประกาศ เมตาดาต้าที่เผยแพร่ และการตรวจสอบความถูกต้องของที่เก็บข้อมูล แหล่งที่มาของแอปพลิเคชันและการทดสอบจะได้รับการดูแลแบบส่วนตัว อย่าส่งโค้ดที่คอมไพล์แล้ว แหล่งที่มาส่วนตัว ข้อมูลประจำตัว โปรไฟล์ผู้ใช้ หรือเพย์โหลดที่ปฏิบัติการได้

ประชาสัมพันธ์ด้านเอกสารควรรักษาภาษาทั้ง 34 ภาษาและการนำทางให้สอดคล้องกัน รักษาชื่อคำสั่ง/ไฟล์/ผลิตภัณฑ์ และอธิบายพฤติกรรมที่แท้จริง ภาพหน้าจอใหม่ต้องเป็นของคุณเอง มีการระบุเวอร์ชัน และไม่มีรายละเอียดส่วนบุคคล ข้อมูลสังเคราะห์จะต้องมีป้ายกำกับ ระบุแหล่งที่มาและการอนุญาตสำหรับเนื้อหาใหม่ของบุคคลที่สามทั้งหมด

ใช้ UTF-8, LF, Markdown ที่อ่านได้ และการเปลี่ยนแปลงที่เน้นเล็กน้อย เครื่องมือตรวจสอบ Python ใช้เฉพาะไลบรารีมาตรฐานเท่านั้น จับคู่สไตล์ที่มีอยู่ หลีกเลี่ยงการพึ่งพาที่ไม่จำเป็น และรัน:

```text
python tools/validate_repository.py
```

สำหรับการเปลี่ยนแปลงเมตาดาต้าที่เผยแพร่ ให้รวมเวอร์ชัน/แท็ก ขนาดไฟล์ และ SHA-256 ที่แน่นอนจากไบนารีที่ได้รับการตรวจสอบ และจัดหน้าดาวน์โหลดให้สอดคล้องกัน การเปลี่ยนแปลงแอปพลิเคชันจำเป็นต้องมีการสร้าง/การทดสอบส่วนตัวที่เหมาะสมกับพฤติกรรมที่ได้รับผลกระทบ การตรวจสอบเอกสารไม่ใช่การทดสอบแอปพลิเคชัน อย่าคิดค้นผลการทดสอบในอดีตหรือผลกำไร

โดยการบริจาคสื่อฮับดั้งเดิม แสดงว่าคุณยอมรับใบอนุญาต MIT ที่มีขอบเขตใน [ใบอนุญาต](../../../LICENSE) เก็บประกาศของบุคคลที่สามและระบุการเปลี่ยนแปลงของคุณ อย่าแทนที่ใบอนุญาตอัปสตรีม การยอมรับและการเผยแพร่ยังคงเป็นการตัดสินใจของผู้ดูแล
