<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · **Español** · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publicaciones y lanzamientos

El repositorio público es **Zendo-GIT/NV-Laboratory**. Los cambios en la documentación son revisados, confirmados e impulsados ​​por el responsable del mantenimiento con **GitHub Desktop**. Una confirmación local no carga archivos. Los paquetes binarios son activos de versión GitHub separados; nunca pertenecen a la lista de cambios de Git.

<a id="documentation-updates"></a>
## Actualizaciones de documentación

1. Abra la carpeta **NV-Laboratory** en GitHub Desktop.
2. Revisar documentación, avisos, imágenes, metadatos JSON y el validador de documentación.
3. Ejecute `python tools/validate_repository.py` desde esa carpeta.
4. Confirme los cambios revisados y luego use **Push origin**. Verifique el resultado de las acciones.
5. Mantenga la identidad pública del autor **禅堂 Zendo (RevoluSound Team)** y la dirección GitHub `noreply` de la cuenta.

Nunca seleccione el espacio de trabajo de desarrollo principal, el directorio de auditoría privada o el directorio de archivos adjuntos binarios. [Comprometer la privacidad del correo electrónico](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Lanzamientos de aplicaciones independientes

| Herramienta | Etiqueta | Política de versión |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Versión existente de la aplicación de cuatro partes; La revisión de configuración 2 tiene su propio nombre de archivo. |
| NVDriverForge | nvdriverforge-v0.1.4 | Esquema 0.x existente; las actualizaciones versionadas conservan los paquetes anteriores |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Versión de la aplicación 0.2.3; cambios acumulativos desde público 0.1.1 |
| NVRasterPulse | nvrasterpulse-v0.2 | Versión existente de dos partes |

El mantenedor puede publicar directamente o autorizar a un asistente a publicar los activos auditados. La publicación es explícita; ningún flujo de trabajo crea una versión en cada confirmación.

1. Revise el informe previo a la publicación actual, las fuentes de los archivos binarios, las licencias y los valores SHA-256.
2. Cree un borrador para la etiqueta de la herramienta, dirigido a la confirmación del centro revisada. Incluya las notas de la versión específicas de la versión preparadas.
3. Adjunte solo los activos portátiles/de configuración de esa versión, `Licenses-and-Credits.zip` y `SHA256SUMS.txt`.
4. Consulta compatibilidad, instalación, dependencias, cambios y límites conocidos. Mantenga RTSS destacado para NVRasterPulse.
5. Publique, verifique las URL, los tamaños y los hashes de los activos públicos, y registre la fecha de publicación real en `docs/releases.json`.
6. Actualice las páginas de descarga y las traducciones, luego confirme/envíe sus cambios en GitHub Desktop.

Los enlaces de etiquetas por proyecto evitan enviar a los usuarios a otra herramienta a través de un enlace `releases/latest` compartido. Los archivos automáticos **Source code** de GitHub contienen este centro de documentación. Las fuentes de las aplicaciones permanecen privadas. Los avisos de componentes originales permanecen intactos y una versión no resuelve la reserva NVIDIA SDK documentada de NVMFG.


La actualización del 18 de septiembre prepara tres nuevas etiquetas; la versión Profile Inspector existente permanece sin cambios. Los nombres de los activos, las etiquetas y `SHA256SUMS.txt` deben permanecer exactos para las comprobaciones de actualización de la aplicación. Publicar versiones normales sin el indicador de versión preliminar para exponerlas a comprobaciones de versión estable; NVMFG sigue siendo experimental.

<a id="integrity-and-storage"></a>
## Integridad y almacenamiento

Nunca reemplace silenciosamente los bytes binarios publicados. Utilice una nueva versión explícita o revisión del instalador con nuevos hashes. Los complementos legales complementan los avisos integrados. NVDriverForge 0.1.4 portátil tiene 142,017,891 bytes, por encima del límite normal de archivos Git de 100 MiB de GitHub. Los archivos adjuntos de liberación evitan colocar archivos binarios o Git LFS en este centro. [GitHub guía de archivos grandes](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Los informes de vulnerabilidad privados deben habilitarse en la configuración de seguridad del repositorio. Verifique su disponibilidad antes de dirigir informes confidenciales allí; [SECURITY.md](../SECURITY.md) proporciona un recurso alternativo que no expone detalles de vulnerabilidad.

[Descargar catálogo](downloads.md) · [Documentación de lanzamiento de GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
