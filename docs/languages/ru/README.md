<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · **Русский** · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Машинный перевод с английского. Технические названия, команды, URL-адреса и оригинальные юридические тексты сохраняются. Рецензия на языке носителя языка приветствуется; обратитесь к ссылке на английском языке, если формулировка неясна.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools от 禅堂 Zendo (RevoluSound Team).** Четыре независимых утилиты Windows для профилей драйверов NVIDIA, установки драйверов, экспериментальных ограничений кадров Multi Frame Generation и RTSS.

[Получите инструменты](docs/downloads.md) · [Установка](docs/installation.md) · [Совместимость и помощь](docs/support.md) · [Кредиты и лицензии](THIRD_PARTY_NOTICES.md)

> **Для NVRasterPulse требуется RTSS.** Сначала установите [RivaTuner Statistics Server от Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS должен быть запущен, чтобы ограничения FPS работали. Он скачивается отдельно.

<a id="projects"></a>
## Проекты

| Проект | Цель | Версия | Документация | Скачать |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Редактор профилей драйверов NVIDIA с добавленным дисплеем, цветом, элементами управления HDR и ICC/WCS. Ранее NVPI Custom. | 3.0.2.3 | [Руководство](NVIDIA-Profile-Inspector/README.md) | [Пакеты](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Выберите компоненты драйвера, просмотрите дополнительные настройки и установите оригинальный пакет драйверов NVIDIA. | 0.1.3 | [Руководство](NVDriverForge/README.md) | [Пакеты](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Экспериментальный инструмент RTX 40 MFG с возможностью выбора для каждой игры и обслуживанием Streamline SDK. | 0.1.1 | [Руководство](NVMFG-Unlock40/README.md) | [Пакеты и статус](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Управляйте ограничениями RTSS FPS на каждый исполняемый файл с дробными значениями, резервными копиями и доступом к лотку. | 0.1 | [Руководство](NVRasterPulse/README.md) | [Пакеты](docs/downloads.md#nvrasterpulse) |

**Загрузки:** в [страница загрузки](docs/downloads.md) перечислены состояние каждой версии, файлы и значения SHA-256. Экспериментальные функции и ограничения совместимости описаны в руководствах проекта.

<a id="start-here"></a>
## Начните здесь

1. Выберите один инструмент выше. Каждый работает независимо; установка всего пакета не требуется.
2. Прочтите его требования и выберите **Настройка** для установленного приложения или **переносное** для отдельной папки.
3. После публикации релиза загрузите указанный ресурс приложения, прочтите прилагаемые примечания и сравните его SHA-256.
4. Сохраняйте резервные копии перед изменением драйвера, настроек дисплея, профиля NVIDIA или среды выполнения игры.

Документация доступна на тех же 34 языках, что и приложения NV, через переключатель в верхней части каждого руководства. GitHub не выбирает автоматически README по языку браузера. Язык документации и языковые настройки приложения являются отдельными.

<a id="provenance-and-ownership"></a>
## Происхождение и право собственности

Этот центр распространяет документацию и скомпилированные приложения. Исходный код приложения хранится в частном порядке. Проекты разведки и добычи сохраняют свое авторство и лицензии; Распространение частных источников не заменяет эти условия.

- Profile Inspector fork сохраняет лицензию MIT Orbmu2k и явно идентифицируется как fork.
- NVDriverForge имеет собственные условия распространения в двоичном формате и включает отдельно лицензируемые компоненты среды выполнения и инструментальные средства.
- NVMFG Unlock40 – независимо разработанное приложение. Для сравнения и уточнения использовался RTX40MFG-Unlock; общие собственные компоненты сохраняют свои кредиты MIT. Термины MinHook и NVIDIA SDK остаются отдельными.
- NVRasterPulse сохраняет поставляемую лицензию MIT и использует пользовательский интерфейс, производный от Profile Inspector. RTSS – необходимая внешняя программа.

См. [полная таблица компонентов](THIRD_PARTY_NOTICES.md), [происхождение файла и изменения](docs/provenance.md) и [объем лицензии](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Другие проекты – RevoluSound Team

Это отдельные проекты аудиомодов, ссылки на которые приведены здесь, чтобы помочь вам познакомиться с работой команды.

| Игра | Проект | О |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Изменения звука автомобиля, охватывающие двигатели, выхлопные системы, воздухозаборники и турбо-эффекты. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Более поздний аудиопакет для автомобиля FH5, выпущенный командой. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Более ранний пакет FH5; его страница Nexus направляет посетителей к более позднему пакету команды, указанному выше. |

Заголовки следуют за связанными страницами Nexus Mods. Их загрузки, требования, кредиты и разрешения остаются на Nexus Mods.

<a id="help-and-participation"></a>
## Помощь и участие

[Сообщите об ошибке или предложите функцию](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Содействие](CONTRIBUTING.md) · [Отчеты о безопасности](SECURITY.md) · [Журнал изменений](CHANGELOG.md)

По вопросам безопасности прочитайте SECURITY.md, прежде чем публиковать журналы или технические подробности. После публикации репозитория разработчик должен включить частную отчетность.

> **Независимые общественные проекты.** NV Laboratory, NV Tools и эти утилиты не связаны, не спонсируются и не поддерживаются официально NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS и другие названия продуктов являются торговыми марками соответствующих владельцев. Названия описывают совместимость и происхождение, а не официальное одобрение.
