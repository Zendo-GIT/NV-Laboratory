<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · **Español** · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# guía de instalación

Comience con [Descargas](downloads.md), que registra el estado de la publicación y los nombres exactos de los activos. Estas son herramientas independientes: instale solo las que necesite.

> **Para NVRasterPulse, instale [RTSS de Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) antes de abrir el administrador de perfiles.**
> RTSS debe ejecutarse para aplicar límites; no está incluido en NV Tools.

| Herramienta | Edición instalada | Edición portátil | Requisito previo principal |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extraer el ZIP NVPI completo | Controlador NVIDIA y .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, tiempo de ejecución incluido | Paquete de controlador NVIDIA original compatible para operaciones de instalación |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Extraiga el ZIP NVMFG completo y conserve las subcarpetas | RTX 40, DLSS FG existente, proveedor exacto y ayudantes de .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Extraer el ZIP RP completo | RTSS y .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Descargar, verificar, instalar

1. En la versión publicada elegida, descargue el recurso de aplicación denominado, los avisos ZIP y SHA256SUMS.txt.
2. Utilice [SHA-256 ejemplo](downloads.md#sha-256), con el nombre del archivo descargado real.
3. Para la configuración, siga el instalador normal. Para ZIP portátil, extraiga todo a una nueva carpeta de escritura local; no corras desde el interior del ZIP.
4. Abra el EXE propio de la aplicación. Conserve los archivos de licencia/configuración/datos adjuntos.
5. Lea las instrucciones de uso de esa herramienta antes de habilitar la configuración o las operaciones del sistema.

Los binarios actuales no están firmados. Un hash coincidente confirma los bytes esperados; no es un certificado de seguridad o compatibilidad. No desactive las protecciones de seguridad Windows sólo para suprimir una advertencia.

La instalación de NVDF o su complemento NVPI opcional es independiente de la instalación de un controlador GPU. El complemento NVPI mantiene su nombre de instalación interna existente. Su botón RasterPulse elevado requiere una instalación protegida en todo el sistema; Se pueden abrir otras copias de RP a través de sus propios accesos directos.

NVMFG es experimental y tiene [reserva de licencia NVIDIA SDK documentada](provenance.md). No se incluye ningún controlador NVIDIA, proveedor/modelo NGX ni tiempo de ejecución del juego Streamline. Las descargas y actualizaciones de juegos seleccionadas de SDK son operaciones explícitas e independientes.

<a id="language-and-updates"></a>
## Idioma y actualizaciones

Utilice el selector de 34 idiomas del README para la documentación. NVDF, NVMFG y RP tienen su propia configuración de interfaz de usuario en 34 idiomas; NVPI mantiene el soporte de idiomas existente. Algunas cadenas técnicas del instalador vuelven al inglés.

Mantenga la identidad de instalación de una herramienta al actualizar. Ciérrelo primero y conserve las copias de seguridad. Para NVMFG, cierre los juegos afectados y resuelva la recuperación del perfil pendiente. Para actualizaciones portátiles, utilice una carpeta nueva en lugar de combinar versiones.

<a id="removing-a-tool"></a>
## Quitar una herramienta

Desinstalar una aplicación no significa deshacer automáticamente su configuración.

- **NVPI:** restaure los perfiles/configuraciones de visualización deseados antes de eliminarlos si es necesario.
- **NVDF:** use la recuperación primero si desea restaurar los cambios avanzados/NVENC. Uninstall abandona el controlador de gráficos, la configuración y las copias de seguridad.
- **NVMFG:** cierre los juegos, deshabilite/salga del controlador, resuelva la recuperación de NVIDIA y restaure las copias de seguridad de SDK del juego deseado antes de eliminarlas.
- **RP:** elimine primero las anulaciones del limitador previstas. Uninstall no borra las mayúsculas RTSS guardadas ni elimina RTSS.

Consulte cada [guía del proyecto](../README.md#projects) para conocer las ubicaciones exactas de los datos y sus limitaciones, o [apoyo](support.md) si falla un paso de recuperación.
