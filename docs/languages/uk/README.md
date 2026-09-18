<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · **Українська** · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Машинний переклад з англійської мови. Технічні назви, команди, URL-адреси та оригінальні юридичні тексти збережено. Огляд носія мови вітається; зверніться до посилання англійською мовою, якщо формулювання незрозуміле.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools від 禅堂 Zendo (RevoluSound Team).** Чотири незалежні утиліти Windows для профілів драйверів NVIDIA, встановлення драйверів, експериментальних обмежень кадрів Multi Frame Generation і RTSS.

[Отримайте інструменти](docs/downloads.md) · [монтаж](docs/installation.md) · [Сумісність і допомога](docs/support.md) · [Подяки та ліцензії](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse вимагає RTSS.** Спочатку встановіть [RivaTuner Statistics Server від Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS має бути запущено, щоб його обмеження FPS працювали. Завантажується окремо.

<a id="projects"></a>
## Проекти

| Проект | призначення | Версія | Документація | Завантажити |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Редактор профілю драйвера NVIDIA із доданими елементами керування дисплеєм, кольором, HDR і ICC/WCS. Раніше NVPI Custom. | 3.0.2.3 | [Гід](NVIDIA-Profile-Inspector/README.md) | [пакети](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Підготуйте та встановіть оригінальний драйвер NVIDIA із покроковим вибором, резервним копіюванням і відновленням. | 0.1.4 | [Гід](NVDriverForge/README.md) | [пакети](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Експериментальний RTX 40 MFG, постійна бібліотека ігор, діагностика та обслуговування Streamline SDK. | 0.2.3 | [Гід](NVMFG-Unlock40/README.md) | [Пакети та статус](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Керуйте обмеженнями RTSS FPS для кожної програми: діагностика, пропозиції, призупинення, скасування та спільний доступ до профілю. | 0.2 | [Гід](NVRasterPulse/README.md) | [пакети](docs/downloads.md#nvrasterpulse) |

**Завантаження:** [сторінка завантаження](docs/downloads.md) перераховує стан кожної версії, файли та значення SHA-256. Експериментальні функції та обмеження сумісності описані в посібниках проекту.

<a id="start-here"></a>
## Почніть тут

1. Виберіть один інструмент вище. Кожен працює незалежно; встановлювати весь комплект не потрібно.
2. Прочитайте його вимоги та виберіть **Налаштування** для встановленої програми або **переносний** для окремої папки.
3. Коли його випуск буде опубліковано, завантажте названий ресурс програми, прочитайте супровідні повідомлення та порівняйте його SHA-256.
4. Зберігайте резервні копії перед зміною драйвера, параметрів дисплея, профілю NVIDIA або середовища виконання гри.

Документація доступна тими ж 34 мовами, що й додатки NV, через селектор у верхній частині кожного посібника. GitHub не вибирає файл README автоматично за мовою браузера. Мова документації та власні налаштування мови програми є різними.

<a id="provenance-and-ownership"></a>
## Походження та право власності

Цей центр розповсюджує документацію та скомпільовані програми. Вихідний код програми зберігається конфіденційно. Проекти Upstream зберігають своє авторство та ліцензії; приватне розповсюдження не замінює ці терміни.

- Profile Inspector fork зберігає ліцензію Orbmu2k MIT і явно ідентифікується як fork.
- NVDriverForge має власні двійкові умови розповсюдження та включає окремо ліцензовані компоненти середовища виконання/інструменти.
- NVMFG Unlock40 – це програма, розроблена незалежною компанією. RTX40MFG-Unlock було використано для порівняння та уточнення; спільні рідні компоненти зберігають свої кредити MIT. Терміни MinHook і NVIDIA SDK залишаються окремими.
- NVRasterPulse зберігає надану ліцензію MIT і зазначає інтерфейс користувача, отриманий від Profile Inspector. RTSS є необхідною зовнішньою програмою.

Див. [повна таблиця компонентів](THIRD_PARTY_NOTICES.md), [походження файлу та зміни](docs/provenance.md) і [обсяг ліцензії](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Інші проекти – RevoluSound Team

Це окремі проекти модифікації аудіо, посилання на які тут, щоб допомогти вам дізнатися про роботу команди.

| Гра | Проект | про |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Зміни звуку автомобіля, що охоплюють двигуни, вихлопи, впуски та турбо-ефекти. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Пізніший автомобільний аудіопакет команди FH5. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Раніший пакет FH5; його сторінка Nexus спрямовує відвідувачів до пізнішого командного набору вище. |

Заголовки слідують за пов’язаними сторінками Nexus Mods. Їх завантаження, вимоги, кредити та дозволи залишаються на Nexus Mods.

<a id="help-and-participation"></a>
## Допомога та участь

[Повідомте про помилку або запропонуйте функцію](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Сприяння](CONTRIBUTING.md) · [Звіти безпеки](SECURITY.md) · [Журнал змін](CHANGELOG.md)

З питань безпеки прочитайте SECURITY.md перед публікацією журналів або технічних деталей. Після публікації репозиторію супроводжувач має ввімкнути приватне звітування.

> **Незалежні проекти спільноти.** NV Laboratory, NV Tools і ці утиліти не пов’язані з NVIDIA Corporation, не спонсоруються та офіційно не схвалені. NVIDIA, GeForce, RTX, DLSS та інші назви продуктів є товарними знаками відповідних власників. Імена описують сумісність і походження, а не офіційне схвалення.
