<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · **Русский** · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Машинный перевод с английского. Технические названия, команды, URL-адреса и оригинальные юридические тексты сохраняются. Рецензия на языке носителя языка приветствуется; обратитесь к ссылке на английском языке, если формулировка неясна.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Публикация и релизы

Публичный репозиторий: **Zendo-GIT/NV-Laboratory**. Изменения в документации проверяются, фиксируются и отправляются сопровождающим с помощью **GitHub Desktop**. Локальный коммит не загружает файлы. Двоичные пакеты представляют собой отдельные активы выпуска GitHub; они никогда не попадают в список изменений Git.

<a id="documentation-updates"></a>
## Обновления документации

1. Откройте папку **NV-Laboratory** в GitHub Desktop.
2. Просмотрите документацию, уведомления, изображения, метаданные JSON и средство проверки документации.
3. Запустите `python tools/validate_repository.py` из этой папки.
4. Зафиксируйте проверенные изменения, затем используйте **Push origin**. Проверьте результат действий.
5. Сохраните общедоступный идентификатор автора **禅堂 Zendo (RevoluSound Team)** и адрес учетной записи GitHub `noreply`.

Никогда не выбирайте родительскую рабочую область разработки, частный каталог аудита или каталог двоичных вложений. [Обеспечьте конфиденциальность электронной почты](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Независимые выпуски приложений

| Инструмент | Тег | Политика версий |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Существующая версия приложения, состоящая из четырех частей; версия установки 2 имеет собственное имя файла |
| NVDriverForge | nvdriverforge-v0.1.3 | Существующая схема 0.x; Версионные обновления сохраняют более ранние пакеты |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Кандидат UI2 идентифицирован по точным хэшам без изобретения новой версии приложения. |
| NVRasterPulse | nvrasterpulse-v0.1 | Существующая версия, состоящая из двух частей |

Сопровождающий может публиковать проверяемые ресурсы напрямую или уполномочить помощника опубликовать проверяемые ресурсы. Публикация является явной; ни один рабочий процесс не создает релиз для каждого коммита.

1. Просмотрите текущий отчет о предварительной публикации, источники двоичных файлов, лицензии и значения SHA-256.
2. Создайте черновик тега инструмента, ориентируясь на проверенную фиксацию концентратора. Включите подготовленные примечания к выпуску для конкретной версии.
3. Прикрепляйте только установочные/переносимые ресурсы этой версии, `Licenses-and-Credits.zip` и `SHA256SUMS.txt`.
4. Проверьте совместимость, установку, зависимости, изменения и известные ограничения. Оставьте RTSS на видном месте для NVRasterPulse.
5. Опубликуйте, проверьте URL-адреса, размеры и хеши общедоступных ресурсов и запишите фактическую дату публикации в `docs/releases.json`.
6. Обновите страницы загрузки и переводы, затем зафиксируйте/отправьте их изменения в GitHub Desktop.

Ссылки на теги для каждого проекта позволяют избежать перенаправления пользователей на другой инструмент через общую ссылку `releases/latest`. Автоматические архивы **Source code** GitHub содержат этот центр документации. Источники приложений остаются конфиденциальными. Уведомления об исходных компонентах остаются неизменными, и выпуск не устраняет задокументированный NVMFG резерв NVIDIA SDK.

<a id="integrity-and-storage"></a>
## Целостность и хранение

Никогда не заменяйте опубликованные двоичные байты молча. Используйте новую явную версию или версию установщика с новыми хэшами. Юридические сайдкары дополняют встроенные уведомления. Портативный NVDriverForge 0.1.3 имеет размер 141 760 351 байт, что превышает обычный лимит Git-файла GitHub в 100 МБ. При выпуске вложений избегайте размещения двоичных файлов или Git LFS в этом хабе. [Руководство по работе с большими файлами GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Частные отчеты об уязвимостях должны быть включены в настройках безопасности репозитория. Проверьте его доступность, прежде чем направлять туда конфиденциальные отчеты; [SECURITY.md](../SECURITY.md) предоставляет запасной вариант, который не раскрывает подробности уязвимости.

[Скачать каталог](downloads.md) · [Документация по выпуску GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
