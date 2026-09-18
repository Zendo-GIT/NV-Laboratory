<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · **Español** · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Compatibilidad y solución de problemas

Estos son los candidatos preparados, no una matriz de certificación para todas las combinaciones de controlador y juego Windows, GPU.

| Herramienta | Windows/tiempo de ejecución | Hardware/dependencia externa | Operaciones que necesitan atención |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Controlador/pantalla NVIDIA compatible | Escritura de perfiles y visualización de vistas previas |
| NVDriverForge 0.1.4 | Windows 10 compilación 19041+ / 11 x64; .NET/WPF incluido | Paquete de controladores NVIDIA compatible | Instalación elevada, configuración avanzada, opcional NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF incluido, ayudantes de Framework 4.8 | RTX 40, juego DLSS FG elegible y proveedor fijado | Parches nativos en el juego, diario de perfil global, actualizaciones del juego SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS instalado; corriendo por gorras | RTSS cambios de perfil por ejecutable |

No se ha preparado ningún paquete ARM64. La disponibilidad de pantalla/API y las versiones antiguas de Windows pueden limitar las funciones individuales. No se inventa ninguna versión mínima universal NVIDIA o RTSS. El hash exacto del proveedor NVMFG se encuentra en [procedencia](provenance.md).

<a id="before-reporting-a-bug"></a>
## Antes de informar un error

Identifique el ejecutable/versión exacta que abrió. Una copia instalada anteriormente no es necesariamente la versión de un ZIP recién descargado. Registre los pasos de reproducción, el resultado esperado y el resultado real. Para problemas de renderizado/limitación, incluya la versión del juego, la actualización de la pantalla, el estado de FG/V-Sync/VRR y cualquier otro limitador o superposición.

Utilice el [forma de error](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Nunca adjunte una carpeta de desarrollo privada completa, un archivo de controladores, un modelo, una DLL de juego, un volcado de registro o una colección de registros no revisados.

| problema | Primeros controles |
| --- | --- |
| Versión de aplicación incorrecta | Confirmar la identidad EXE y liberar el hash; cierre la copia anterior antes de reemplazarla. |
| Error de tiempo de ejecución/inicio | Instale el Framework 4.8 requerido o conserve todas las subcarpetas portátiles suministradas. |
| UAC cancelado | Vuelva a intentar únicamente la operación prevista; la cancelación no es una instalación exitosa. |
| Discrepancia entre hash y firma | Deje de utilizar ese candidato y obtenga los bytes oficiales esperados. |
| NVPI color/modo rechazado | Revertir y utilizar una combinación compatible con la pantalla/controlador real. |
| NVDF fallo de copia de seguridad o recuperación | Preservar el trabajo protegido y RECOVERY.txt; No borre el diario ni fuerce escrituras contradictorias. |
| Configuración pendiente de NVMFG | Resuelve la recuperación con juegos cerrados, conservando los cambios de otras herramientas. |
| RP límite no tiene ningún efecto | Ejecute RTSS, identifique el EXE del juego real, inspeccione el estado del enlace y los límites de la competencia. |
| RP la tapa persiste después de quitarla | Inspeccionar RTSS Global; La eliminación cambia únicamente las anulaciones del limitador local. |

NVDriverForge ofrece una vista previa del informe JSON local; NVMFG ofrece un diagnóstico en Acerca de. Prefiera estos informes filtrados a un archivo de registro completo e inspecciónelos antes de compartirlos. Un bloqueo de restauración informado en NVMFG 0.1.1 aún no tiene una causa establecida; conservar su diario y registrar cualquier código de error disponible. NVRasterPulse 0.2 ofrece diagnósticos de configuración en su menú de acciones, sin medir FPS.

<a id="logs-and-privacy"></a>
## Registros y privacidad

| Herramienta | Datos locales para revisar, no cargar al por mayor |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; trabajos protegidos `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; copias de seguridad `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` al lado del EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` debajo de él |
| NVPI | Las exportaciones elegidas y el error mostrado; no hay una ruta de registro universal inventada |

Elimine nombres de cuentas, directorios de inicio, rutas de bibliotecas de juegos, identificadores de dispositivos, tokens y ventanas no relacionadas del texto/imágenes que comparte. Guarde los originales en privado para su recuperación. Los asuntos públicos son visibles para todos.

Para una vulnerabilidad, un comportamiento privilegiado peligroso o una operación destructiva no intencionada, siga [SECURITY.md](../SECURITY.md) en lugar de publicar detalles públicamente.

<a id="what-has-been-verified"></a>
## Lo que se ha verificado

Para la preparación del concentrador, se ejecutaron escaneos de carga estática/ZIP/hash/metadatos y verificaciones de documentación. Las pruebas de compilación/unidad/UI de aplicaciones privadas existentes son evidencia histórica y anticuada. Como parte de esta preparación, no se realizó ninguna instalación de controladores, cambios de pantalla, operaciones RTSS en vivo ni pruebas comparativas del juego.

"Detectado", "escrito", "recargado", "capacidad disponible" y "medido en el juego" son resultados diferentes. Informa cuál observaste.
