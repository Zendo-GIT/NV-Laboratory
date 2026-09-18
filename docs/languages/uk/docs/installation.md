<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · **Українська** · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Машинний переклад з англійської мови. Технічні назви, команди, URL-адреси та оригінальні юридичні тексти збережено. Огляд носія мови вітається; зверніться до посилання англійською мовою, якщо формулювання незрозуміле.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Керівництво по установці

Почніть із [Завантаження](downloads.md), який записує статус публікації та точні назви активів. Це окремі інструменти: встановлюйте лише ті, які вам потрібні.

> **Для NVRasterPulse інсталюйте [RTSS від Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) перед відкриттям менеджера профілів.**
> RTSS потрібно запустити, щоб застосувати обмеження; він не включений у NV Tools.

| Інструмент | Встановлена редакція | Портативне видання | Головна передумова |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Розпакуйте повний архів ZIP NVPI | Драйвер NVIDIA і .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, час виконання включено | Сумісний оригінальний пакет драйверів NVIDIA для операцій встановлення |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Розпакуйте повний ZIP-архів NVMFG, збережіть вкладені папки | RTX 40, існуючий DLSS FG, точний постачальник і помічники .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Розпакуйте повний архів ZIP RP | RTSS і .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Завантажте, перевірте, встановіть

1. У вибраному опублікованому випуску завантажте його названий актив програми, повідомлення ZIP і SHA256SUMS.txt.
2. Використовуйте [Приклад SHA-256](downloads.md#sha-256) із фактичною назвою завантаженого файлу.
3. Для встановлення виконайте звичайний інсталятор. Для портативного ZIP розпакуйте все в нову локальну папку, доступну для запису; не запускайте з ZIP.
4. Відкрийте власний EXE програми. Зберігайте супровідні файли ліцензії/конфігурації/даних.
5. Прочитайте інструкції з використання цього інструменту перед увімкненням налаштувань або системних операцій.

Поточні двійкові файли без знаку. Відповідний хеш підтверджує очікувані байти; це не сертифікат безпеки чи сумісності. Не вимикайте засоби захисту Windows лише для того, щоб придушити попередження.

Встановлення NVDF або його додаткового компаньйона NVPI відбувається окремо від встановлення драйвера GPU. Супутник NVPI зберігає наявну назву внутрішньої інсталяції. Його підвищена кнопка RasterPulse вимагає захищеного встановлення в системі; інші копії RP можна відкрити за допомогою їхніх ярликів.

NVMFG є експериментальним і має [задокументований резерв ліцензування NVIDIA SDK](provenance.md). Немає драйвера NVIDIA, постачальника/моделі NGX або середовища виконання гри Streamline. Вибрані завантаження SDK і оновлення гри є явними окремими операціями.

<a id="language-and-updates"></a>
## Мова та оновлення

Використовуйте 34-мовний селектор README для документації. NVDF, NVMFG і RP мають власні 34-мовні налаштування інтерфейсу користувача; NVPI зберігає наявну підтримку мови. Деякі технічні рядки інсталятора повертаються до англійської мови.

Зберігайте ідентифікатор інсталяції інструменту під час оновлення. Спочатку закрийте його та збережіть резервні копії. Для NVMFG закрийте уражені ігри та вирішіть незавершене відновлення профілю. Для портативних оновлень використовуйте нову папку, а не об’єднуйте випуски.

<a id="removing-a-tool"></a>
## Видалення інструменту

Видалення програми не означає автоматичного скасування її налаштувань.

- **NVPI:** за потреби відновіть потрібні профілі/налаштування дисплея перед видаленням.
- **NVDF:** спочатку скористайтеся відновленням, якщо ви хочете відновити розширені/NVENC зміни. Uninstall залишає графічний драйвер, налаштування та резервні копії.
- **NVMFG:** закрийте ігри, вимкніть/вийдіть з контролера, вирішіть відновлення NVIDIA і відновіть потрібні резервні копії гри SDK перед видаленням.
- **RP:** спочатку видаліть заплановані перевизначення обмежувача. Uninstall не стирає збережені шапки RTSS і не видаляє RTSS.

Перегляньте кожен [керівництво по проекту](../README.md#projects), щоб дізнатися про точне розташування даних і обмеження, або [підтримка](support.md), якщо етап відновлення не вдається.
