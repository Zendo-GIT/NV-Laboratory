<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · **Українська** · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Машинний переклад з англійської мови. Технічні назви, команди, URL-адреси та оригінальні юридичні тексти збережено. Огляд носія мови вітається; зверніться до посилання англійською мовою, якщо формулювання незрозуміле.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Видання та релізи

Загальнодоступним репозиторієм є **Zendo-GIT/NV-Laboratory**. Зміни в документації переглядаються, фіксуються та надсилаються супроводжувачем за допомогою **GitHub Desktop**. Локальний комміт не завантажує файли. Двійкові пакети є окремими ресурсами випуску GitHub; вони ніколи не належать до списку змін Git.

<a id="documentation-updates"></a>
## Оновлення документації

1. Відкрийте папку **NV-Laboratory** у GitHub Desktop.
2. Перегляньте документацію, повідомлення, зображення, метадані JSON і засіб перевірки документації.
3. Запустіть `python tools/validate_repository.py` із цієї папки.
4. Зафіксуйте переглянуті зміни, а потім використовуйте **Push origin**. Перевірте результат Дії.
5. Зберігайте публічну особу автора **禅堂 Zendo (RevoluSound Team)** і адресу GitHub `noreply` облікового запису.

Ніколи не вибирайте батьківську робочу область розробки, каталог приватного аудиту або каталог бінарних вкладень. [Дотримання конфіденційності електронної пошти](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Незалежні випуски програм

| Інструмент | Тег | Політика версій |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Існуюча версія програми з чотирьох частин; версія 2 налаштування має власну назву файлу |
| NVDriverForge | nvdriverforge-v0.1.4 | Існуюча схема 0.x; версійні оновлення зберігають попередні пакунки |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Версія програми 0.2.3; сукупні зміни після публічного 0.1.1 |
| NVRasterPulse | nvrasterpulse-v0.2 | Існуюча версія з двох частин |

Супроводжувач може публікувати безпосередньо або уповноважити помічника публікувати перевірені активи. Публікація є явною; жоден робочий процес не створює Release для кожного коміту.

1. Перегляньте поточний звіт перед публікацією, джерела двійкових файлів, ліцензії та значення SHA-256.
2. Створіть чернетку для тегу інструменту, орієнтуючись на перевірений комміт концентратора. Додайте підготовлені примітки до випуску для певної версії.
3. Додайте лише налаштування/переносні ресурси цієї версії, `Licenses-and-Credits.zip` і `SHA256SUMS.txt`.
4. Перевірте сумісність, встановлення, залежності, зміни та відомі обмеження. Тримайте RTSS помітним для NVRasterPulse.
5. Опублікуйте, перевірте загальнодоступні URL-адреси активів, розміри та хеші та запишіть фактичну дату публікації в `docs/releases.json`.
6. Оновіть сторінки завантаження та переклади, а потім зафіксуйте/введіть їх зміни в GitHub Desktop.

Посилання тегів для кожного проекту не надсилають користувачів до іншого інструменту через спільне посилання `releases/latest`. Автоматичні архіви GitHub **Source code** містять цей центр документації. Джерела програм залишаються приватними. Повідомлення про оригінальні компоненти залишаються недоторканими, а випуск не усуває задокументований резерв NVMFG NVIDIA SDK.


Оновлення від 18 вересня готує три нові теги; існуючий випуск Profile Inspector залишається без змін. Назви активів, теги та `SHA256SUMS.txt` мають залишатися точними для перевірки оновлень програми. Публікуйте звичайні випуски без позначки попереднього випуску, щоб піддавати їх перевірці стабільного випуску; NVMFG залишається експериментальним.

<a id="integrity-and-storage"></a>
## Цілісність і зберігання

Ніколи мовчки не замінюйте опубліковані двійкові байти. Використовуйте нову явну версію або редакцію інсталятора з новими хешами. Юридичні коляски доповнюють вбудовані повідомлення. NVDriverForge 0.1.4 portable становить 142 017 891 байт, що перевищує звичайний ліміт Git-файлу GitHub у 100 МіБ. Уникайте розміщення двійкових файлів або Git LFS у цьому хабі. [Керівництво по великому файлу GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Приватні звіти про вразливості слід увімкнути в налаштуваннях безпеки сховища. Перевірте його наявність, перш ніж направляти туди конфіденційні звіти; [SECURITY.md](../SECURITY.md) забезпечує резервний варіант, який не розкриває деталі вразливості.

[Завантажити каталог](downloads.md) · [Документація до випуску GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
