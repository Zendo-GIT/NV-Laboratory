<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · **Español** · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Prepare una instalación del controlador NVIDIA con opciones claras de componentes y configuraciones opcionales.**

[Descargar 0.1.3 y estado](../docs/downloads.md#nvdriverforge) · [Instalación](#installation) · [Créditos](#credits-and-upstream) · [Licencia](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Descripción general y propósito

NVDriverForge lo guía a través de un paquete de controladores NVIDIA original: elija el controlador, inspeccione sus componentes, revise los ajustes opcionales y luego confirme la instalación. Existe para hacer que esas opciones sean comprensibles y mantener juntas la instalación, las operaciones privilegiadas y la información de recuperación.

Es una aplicación desarrollada de forma independiente inspirada en parte en el flujo de trabajo de NVCleanstall. No incluye NVCleanstall ni reclama la paridad completa de funciones.

<a id="features"></a>
## Características

- NVIDIA Game Ready / Studio búsquedas y descargas; descubrimiento de revisiones opcional con respaldo manual.
- Análisis del paquete original, hashes, firmas NVIDIA, manifiestos y entradas INF compatibles.
- Selección de componentes con dependencias y preservación de componentes desconocidos.
- La versión 0.1.3 mantiene los componentes NVIDIA opcionales seleccionados que se pueden omitir y excluye del descubrimiento solo los componentes verificados y no verificados. Los tiempos de ejecución opcionales ya actuales o inaplicables ya no se fuerzan como componentes críticos.
- Borre resúmenes de errores de instalación y acceda a registros detallados en los 34 idiomas.
- Confirmación de instalación explícita, puesta en escena protegida y exportación de paquetes de almacenamiento de controladores existentes.
- Configuraciones avanzadas opcionales, con comprobaciones previas, diarios y recuperación consciente de conflictos.
- Preajuste opcional **Custom NV** con opciones nombradas y explicaciones, incluida una selección de intensidad SILK independiente y comprobaciones de compatibilidad.
- Descargas opcionales del parche NVENC de la versión exacta; Se verifican los bytes de confirmación de origen y de destino.
- Una instalación opcional separada de Profile Inspector fork desde la pantalla Herramientas.
- Comprobaciones opcionales de actualización del usuario instalado, 34 idiomas de interfaz y cuatro temas.

Las opciones avanzadas disponibles incluyen MPO, el indicador DLSS, Ansel, suspensión de audio NVIDIA, MSI, política/prioridad de interrupción, HDCP, inicio del contenedor de pantalla y un servicio de telemetría heredado elegible. Cada uno tiene sus propios requisitos previos y efectos; Estas no son mejoras de rendimiento universales.

<a id="compatibility"></a>
## Compatibilidad

| Requisito | Detalles |
| --- | --- |
| Sistema | Windows 10 compilación 19041 o posterior / Windows 11, x64 |
| GPU/controlador | Paquete NVIDIA compatible y hardware detectado; La búsqueda automática en el catálogo cubre principalmente los modelos GeForce conocidos. |
| Tiempo de ejecución | .NET 8 / WPF 8.0.31 incluido en el paquete autónomo preparado |
| Privilegios | Configuración normal de UI/por usuario; La instalación del controlador y los cambios del sistema solicitan acceso de administrador. |
| Red | Requerido para búsquedas/descargas de NVIDIA en línea y solicitudes explícitas de NVENC ascendentes; Se puede seleccionar un controlador original local. |
| Herramientas incluidas | 7-Zip 26.03 sin modificar, avisos de tiempo de ejecución, compañero MIT Profile Inspector opcional |
| Acompañante opcional | .NET Framework 4.8 para el Profile Inspector fork separado |

Ninguna versión mínima arbitraria del controlador cubre todas las funciones. La búsqueda de múltiples GPU debe coincidir con cada GPU detectado. Los modelos no compatibles/profesionales pueden requerir la selección manual del controlador. El instalador de NVIDIA sigue siendo la autoridad final sobre hardware/SO.

<a id="installation"></a>
## Instalación

1. Visite [descargas](../docs/downloads.md#nvdriverforge) y confirme que la versión esté publicada.
2. Elija `NVDriverForge-Setup.exe` para instalación o `NVDriverForge.exe` para uso portátil.
3. Compare SHA-256 con `SHA256SUMS.txt` de la versión.
4. Ejecute el programa de instalación para una instalación por usuario y un desinstalador estándar, o coloque el EXE portátil en una carpeta grabable y ábralo.

El portátil incluye su tiempo de ejecución y su instalador opcional. La instalación de NVDriverForge no instala un controlador GPU. Sus EXE actualmente no están firmados.

<a id="usage"></a>
## Uso

1. **Controlador:** descárguelo desde NVIDIA o seleccione un EXE de instalación NVIDIA original. Dejemos que termine el análisis.
2. **Componentes:** revise las descripciones y las dependencias requeridas. Se conservan los componentes desconocidos.
3. **Ajustes:** deja las opciones no deseadas sin cambios. Lea los efectos y las compensaciones antes de seleccionar cualquier cosa.
4. **Revisión:** verifique el controlador exacto, los componentes y las operaciones opcionales, luego confirme la instalación.
5. Acepte UAC solo para la operación que elija. Guarde las instrucciones de recuperación del trabajo protegido.
6. Si el nuevo controlador necesita reiniciarse, siga el estado informado. Las operaciones diferidas requieren una reanudación explícita después de ese reinicio.

Custom NV comienza sin cambios. Elija valores con nombre individuales o revise el ajuste preestablecido proporcionado y sus exclusiones. Sus dos campos internos informativos no están escritos de forma independiente. La configuración se aplica solo en el flujo de trabajo verificado del nuevo controlador, nunca al abrir una vista previa. No es necesario instalar el editor NVPI independiente.

El trabajo opcional NVENC descarga datos compatibles desde una confirmación keylase fijada. Altera dos DLL de controladores e invalida sus firmas; Windows, codificadores, DRM o anti-trampas pueden rechazarlo. No hay datos de este tipo ni la DLL NVIDIA está integrada en NVDriverForge. [Límites de procedencia y licencia](../docs/provenance.md).

Las preferencias controlan el idioma, el tema y las comprobaciones opcionales de actualización del usuario instalado. El dispositivo portátil no crea la tarea de verificación de antecedentes instalada. Las herramientas y la recuperación están separadas de los cuatro pasos de instalación.

<a id="screenshots"></a>
## Capturas de pantalla

![NVDriverForge vista previa de la página del controlador](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Representación de la interfaz de usuario en francés 0.1.2 existente con datos de ejemplo; retenido como una vista previa de la interfaz. El controlador 699.99 que se muestra es un dispositivo de prueba, no una versión real para descargar. [Procedencia de la imagen](../assets/README.md).

<a id="update-and-uninstall"></a>
## Actualizar y desinstalar

Cierre NVDriverForge, obtenga el siguiente paquete oficial y verifique su hash. Utilice la misma identidad de instalación para una actualización instalada; reemplace un EXE portátil cerrado por uno nuevo. Mantenga la configuración y los trabajos protegidos.

Uninstall de Windows **Installed apps**. Elimina la aplicación y su tarea de actualización, no el controlador NVIDIA. La configuración, los registros y las copias de seguridad permanecen. Si lo desea, restaure los cambios avanzados/NVENC a través del flujo de recuperación documentado **antes** de eliminar la aplicación. Restaurar rechaza cambios conflictivos de otra herramienta.

Los datos locales están bajo `%LOCALAPPDATA%\NVDriverForge`; Los empleos protegidos y las exportaciones de conductores están bajo `%PROGRAMDATA%\NVDriverForge\Jobs`. El uso portátil también crea datos locales. Una exportación del almacén de controladores no es una imagen del sistema ni una copia de seguridad del perfil completo.

<a id="known-limitations"></a>
## Limitaciones conocidas

- Sin adiciones de hardware/edición INF, firmas NVIDIA regeneradas, renuncia compatible con anti-trampas o aceptación automática de advertencias sin firmar.
- Sin eliminación completa de telemetría/publicidad, exportación de paquetes delgados o reversión automática completa al controlador anterior.
- La auditoría del concentrador no ha validado exhaustivamente la instalación de controladores, la recuperación de arranque y las escrituras de perfiles opcionales en máquinas reales.
- La lectura del registro no es prueba de los efectos reales de HDCP, rendimiento o latencia.
- Las comprobaciones de firmas utilizan la confianza Windows disponible localmente; La revocación en línea no se realiza.
- Hay 34 idiomas presentes, pero las pruebas completas de accesibilidad y hablantes nativos siguen incompletas.

<a id="troubleshooting"></a>
## Solución de problemas

| Síntoma | acción |
| --- | --- |
| Catálogo en línea no disponible | Seleccione un paquete original de [Descargas del controlador NVIDIA](https://www.nvidia.com/en-us/drivers/). No sustituya un modelo GPU vecino. |
| Búsqueda de revisiones no disponible | Utilice [Foro del controlador Game Ready de NVIDIA](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) y verifique el paquete real. |
| La instalación de NVIDIA falla | Lea el resumen de fallas y abra los registros detallados. Los componentes opcionales ya actuales o no aplicables se pueden omitir en 0.1.3. Las instalaciones fallidas no activan ajustes opcionales ni un flujo de éxito/reinicio. |
| Fallo de firma/hash/copia de seguridad | Detenga esa instalación y conserve el error; Obtenga el paquete original nuevamente si está dañado. |
| Opción no disponible | Leer su motivo de hardware, componente o controlador de destino; manténgalo sin cambios. |
| Reinicio o trabajo aún pendiente | Utilice las instrucciones de recuperación del trabajo y el currículum vitae explícito; no borre su diario. |
| Restaurar conflicto | Otro estado difiere de la transacción registrada. Consérvelo y solicite ayuda en lugar de forzar una restauración. |

Para informes, incluya la versión de la herramienta seleccionada, Windows, GPU, el controlador y los pasos reproducibles; Redactar rutas y detalles personales de los registros. [Soporte](../docs/support.md).

<a id="faq"></a>
## Preguntas frecuentes

**¿El programa de instalación instala un controlador de gráficos?** No. Eso requiere un análisis, revisión, confirmación y un proceso de instalación elevado por separado de la aplicación.

**¿Necesito NVCleanstall o NVPI?** No. NVCleanstall es solo inspiración. El compañero Profile Inspector es un editor opcional independiente.

**¿Hace que cada controlador NVIDIA sea más pequeño o más rápido?** No. Los componentes y requisitos previos seleccionados determinan qué se puede cambiar; no se promete ninguna ganancia medida.

**¿Dónde están las fuentes?** Las pruebas privadas y de fuentes específicas de la aplicación se mantienen por separado. Este centro proporciona documentación, archivos binarios y enlaces de fuentes de terceros necesarios para la atribución/licencia.

<a id="credits-and-upstream"></a>
## Créditos y upstream

Aplicación original, flujo de trabajo, transacciones, localización, bootstrap y adaptaciones: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspiración del flujo de trabajo; no se importa ninguna fuente ni binario.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): temas MIT, referencia de interfaz NVAPI extendida y fork empaquetado por separado.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): herramientas de extracción sin modificar.
- [Microsoft .NET](https://github.com/dotnet/runtime) y [WPF](https://github.com/dotnet/wpf): tiempo de ejecución incluido.
- [Inno Setup](https://jrsoftware.org/isinfo.php): motor de instalación original y traducciones acreditadas.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): fuente de datos externa opcional NVENC; Licencia de redistribución no establecida.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): descargas de controladores externos y bibliotecas NVAPI/NVML instaladas.

[Tabla de componentes completa](../THIRD_PARTY_NOTICES.md) · [Cambios y procedencia](../docs/provenance.md)

<a id="license"></a>
## Licencia

[Permiso de distribución binaria existente](../../../../NVDriverForge/LICENSE) permite el uso y el intercambio de ejecutables oficiales no modificados con sus avisos. Los derechos de origen específicos de la aplicación están reservados. No restringe los derechos otorgados por las licencias independientes de terceros. [Avisos completos](LICENSES/README.md).

Independiente de NVIDIA Corporation, TechPowerUp y keylase; no patrocinado ni respaldado oficialmente por ellos. Los nombres de los productos siguen siendo marcas comerciales de sus propietarios.
