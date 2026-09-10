<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · **Русский** · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Машинный перевод с английского. Технические названия, команды, URL-адреса и оригинальные юридические тексты сохраняются. Рецензия на языке носителя языка приветствуется; обратитесь к ссылке на английском языке, если формулировка неясна.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Руководство по установке

Начните с [Загрузки](downloads.md), который записывает статус публикации и точные имена активов. Это отдельные инструменты: устанавливайте только те, которые вам нужны.

> **Для NVRasterPulse установите [RTSS от Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) перед открытием менеджера профилей.**
> Для применения ограничений необходимо запустить RTSS; он не включен в NV Tools.

| Инструмент | Установленная версия | Портативная версия | Основное условие |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Извлеките полный ZIP-файл NVPI. | Драйвер NVIDIA и .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, среда выполнения включена | Совместимый оригинальный пакет драйверов NVIDIA для операций установки. |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Извлеките полный ZIP-архив NVMFG, сохранив подпапки. | RTX 40, существующий DLSS FG, точный поставщик и вспомогательные средства .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Извлеките полный ZIP-файл RP. | RTSS и .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Загрузите, проверьте, установите

1. В выбранной опубликованной версии загрузите соответствующий ресурс приложения, уведомите ZIP и SHA256SUMS.txt.
2. Используйте [Пример SHA-256](downloads.md#sha-256) с фактическим именем загруженного файла.
3. Для установки следуйте обычному установщику. Для портативного ZIP извлеките все в новую локальную папку, доступную для записи; не запускайте изнутри ZIP.
4. Откройте собственный EXE-файл приложения. Сохраните прилагаемые файлы лицензии/конфигурации/данных.
5. Прочтите инструкции по использованию этого инструмента, прежде чем включать настройки или системные операции.

Текущие двоичные файлы не подписаны. Соответствующий хэш подтверждает ожидаемые байты; это не сертификат безопасности или совместимости. Не отключайте защиту Windows только для того, чтобы подавить предупреждение.

Установка NVDF или его дополнительного компаньона NVPI осуществляется отдельно от установки драйвера GPU. Компаньон NVPI сохраняет существующее внутреннее имя установки. Его повышенная кнопка RasterPulse требует защищенной общесистемной установки; другие копии RP можно открыть с помощью собственных ярлыков.

NVMFG является экспериментальным и имеет [документированный резерв лицензирования NVIDIA SDK](provenance.md). Драйвер NVIDIA, поставщик/модель NGX или среда выполнения игры Streamline не включены. Выбранные загрузки и обновления игр SDK являются отдельными операциями.

<a id="language-and-updates"></a>
## Язык и обновления

Для получения документации используйте переключатель README на 34 языка. NVDF, NVMFG и RP имеют собственные настройки пользовательского интерфейса на 34 языках; NVPI сохраняет существующую языковую поддержку. Некоторые технические строки установщика снова переведены на английский язык.

Сохраняйте идентификационные данные установки инструмента при обновлении. Сначала закройте его и сохраните резервные копии. Для NVMFG закройте затронутые игры и разрешите ожидающее восстановление профиля. Для портативных обновлений используйте новую папку, а не объединяйте выпуски.

<a id="removing-a-tool"></a>
## Удаление инструмента

Удаление приложения не приводит к автоматической отмене его настроек.

- **NVPI:** при необходимости восстановите нужные профили/настройки отображения перед удалением.
- **NVDF:** сначала используйте восстановление, если хотите восстановить расширенные изменения/изменения NVENC. Uninstall оставляет графический драйвер, настройки и резервные копии.
- **NVMFG:** закройте игры, отключите/выйдите из контроллера, разрешите восстановление NVIDIA и восстановите нужные резервные копии игры SDK перед удалением.
- **RP:** сначала удалите намеченные переопределения ограничителя. Uninstall не стирает сохраненные заглушки RTSS и не удаляет RTSS.

См. каждый [руководство по проекту](../README.md#projects) для точного расположения данных и ограничений или [поддержка](support.md), если этап восстановления не удался.
