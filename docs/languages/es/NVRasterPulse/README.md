<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · **Español** · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Límites FPS por aplicación hasta RivaTuner Statistics Server.**

> **Instale RTSS primero.** NVRasterPulse requiere [RivaTuner Statistics Server (RTSS), descargado de Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS debe estar ejecutándose para hacer cumplir los límites. No se incluye ningún instalador RTSS, DLL de enlace o SDK.

[Descargar 0.1 y estado](../docs/downloads.md#nvrasterpulse) · [Instalación](#installation) · [Cómo funcionan los límites](#usage) · [Licencia](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Descripción general y propósito

NVRasterPulse es una interfaz Windows compacta para administrar los límites de trama RTSS por nombre ejecutable. RTSS realiza la limitación. NVRasterPulse gestiona los valores de perfil correspondientes, copias de seguridad y solicitudes de recarga, con acceso a bandeja y opciones persistentes.

Existe para facilitar la edición de los límites exactos por juego sin reemplazar un perfil RTSS completo ni alterar su configuración de superposición. El candidato actual **0.1** es la compilación del 9 de septiembre de 2026 con una verificación de instalación requerida de RTSS.

<a id="features"></a>
## Características

- Seleccione una aplicación en ejecución o agregue su ejecutable manualmente.
- Guarde los límites FPS de 1 a 1000, con hasta tres decimales.
- Codificación racional exacta de los valores ingresados: 59.94 se convierte en 2997/50.
- Configuración de Front Edge Sync (`SyncLimiter=1`) con espera activa (`PassiveWait=0`).
- Actualizaciones de perfil por ejecutable, copias de seguridad automáticas y escrituras atómicas.
- Eliminación de anulaciones de limitadores manteniendo otro contenido del perfil.
- RTSS Detección de instalación, selección de ruta manual e inicio/recarga explícito.
- Operación de bandeja de instancia única, inicio instalado opcional, 34 idiomas y cuatro temas.
- Separe las acciones normales para salir y **Salir + RTSS**.

<a id="compatibility"></a>
## Compatibilidad

| Requisito | Detalles |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| Tiempo de ejecución | [Marco .NET 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), instalado por separado si es necesario |
| Software requerido | RTSS con `RTSS.exe`, un directorio `Profiles` coincidente y soporte de perfil/recarga compatible |
| GPU | La compatibilidad RTSS determina el limitador; este administrador de perfiles no requiere una generación RTX particular |
| Permisos | La aplicación actual solicita acceso de administrador; la carpeta de perfil RTSS seleccionada debe ser accesible |
| Juegos | Depende del soporte de enganche RTSS y de las restricciones de cada juego; sin garantía anti-trampas |

Esta auditoría del concentrador no ha certificado ninguna versión mínima específica de RTSS para cada función. Utilice la distribución oficial actual e informe la versión exacta si una clave/recarga de perfil no funciona. RTSS instalado pero detenido pasa la verificación de instalación; luego debe iniciarse para la limitación real.

<a id="installation"></a>
## Instalación

1. **[Descargue e instale RTSS desde Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Abra [Descargas NVRasterPulse](../docs/downloads.md#nvrasterpulse) y verifique la disponibilidad de la versión.
3. Descargue `NVRasterPulse-0.1-win-x64-Setup.exe` o `NVRasterPulse-0.1-win-x64-portable.zip`, además de los avisos/sumas de verificación.
4. Comparar SHA-256. Ejecute el programa de instalación o extraiga todo el ZIP portátil en una carpeta local grabable.
5. Abra `NVRasterPulse.exe`. Si falta RTSS, use **Descargar RTSS**, instálelo y luego **Comprobar nuevamente**, o seleccione `RTSS.exe` manualmente.
6. Inicie RTSS usando su acceso directo normal o el botón RTSS de NVRasterPulse si está detenido.

Desactivar el recordatorio opcional no omite la verificación de requisitos previos. Un inicio silencioso de la bandeja Windows espera hasta que se abra la ventana principal antes de mostrar esta verificación. La configuración instala NVRasterPulse únicamente. Sus EXE no están firmados.

<a id="usage"></a>
## Uso

1. Seleccione la aplicación en ejecución deseada o busque el EXE del juego.
2. Introduzca un límite entre 1 y 1000 FPS, incluido un valor fraccionario si es necesario.
3. Guarde y verifique el resultado informado. NVRasterPulse actualiza el perfil RTSS de ese ejecutable y solicita una recarga.
4. Confirme que RTSS se esté ejecutando y verifique el comportamiento en el juego deseado.

Los perfiles están codificados por **nombre ejecutable**, como `Game.exe.cfg`. Dos carpetas diferentes que contienen `Game.exe` comparten el mismo perfil RTSS; almacenar la ruta completa no elimina esta colisión.

Para guardar se utiliza Front Edge Sync y espera activa. La espera activa puede aumentar el uso de CPU. Los campos alternativos `LimitTime` están neutralizados. Se conservan los comentarios existentes, la configuración de superposición y `EnableHooking=0`. El perfil global RTSS no se modifica.

Utilice la acción de la papelera para eliminar las anulaciones del limitador de NVRasterPulse. No elimina todo el perfil RTSS. Es posible que aún se aplique un límite heredado de RTSS Global u otra herramienta después.

**Cerrar y salir:** la ventana principal se puede ocultar en la bandeja. Normal **Salir** deja RTSS en ejecución y los límites guardados intactos. **Quit + RTSS** solicita un cierre normal del proceso RTSS coincidente en la sesión actual, espera hasta ocho segundos y no lo fuerza a finalizar. Los límites almacenados permanecen en ambos casos.

El idioma y el tema se seleccionan en la aplicación. El inicio en el inicio de sesión Windows es opcional y está diseñado para una copia instalada. El botón de información explica acciones comunes.

<a id="screenshots"></a>
## Capturas de pantalla

![NVRasterPulse vista previa de la ventana principal](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Representación de la interfaz de usuario 0.1 en francés existente con nombres de ejecutables de ejemplo y un valor 176 FPS. RTSS se muestra detenido; Esta es una ilustración de la interfaz, no un limitador de ejecución ni una medición de latencia. [Procedencia de la imagen](../assets/README.md).

<a id="update-and-uninstall"></a>
## Actualizar y desinstalar

Salga de NVRasterPulse, descargue y verifique la nueva versión, luego ejecute su configuración o extraiga el portátil en una nueva carpeta. Preservar la configuración y las copias de seguridad RTSS. Las actualizaciones RTSS son independientes y provienen de Guru3D.

Para eliminar una copia instalada, utilice Windows **Installed apps**. Para portátil, salga y luego elimine la carpeta extraída cuando sus copias de seguridad estén seguras. Los límites RTSS guardados no se eliminan al desinstalar NVRasterPulse: elimine primero las anulaciones del limitador previstas. RTSS tiene su propio desinstalador.

Estado local: `%LOCALAPPDATA%\NVRasterPulse`. Copias de seguridad automáticas RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Es posible que se lea una ubicación `%LOCALAPPDATA%\RTSSProfileBridge` anterior para la migración. Estos archivos pueden contener rutas ejecutables personales y no deben publicarse públicamente.

<a id="known-limitations"></a>
## Limitaciones conocidas

- RTSS realiza el límite. Un valor guardado o una solicitud de recarga exitosa no es un resultado de tiempo de fotograma medido.
- Los ejecutables del mismo nombre comparten un perfil.
- Otro limitador global/por juego puede afectar el resultado; Deshabilitar la anulación local no elimina un límite heredado.
- Un gancho RTSS deliberadamente deshabilitado permanece deshabilitado.
- La espera activa tiene una compensación CPU/potencia.
- Sin juego universal, anti-trampas o validación de latencia de extremo a extremo.
- El motor limitador independiente experimental anterior no está compilado ni enviado.
- Las copias de seguridad automáticas no implican una interfaz completa de copia de seguridad y restauración con un solo clic.

<a id="troubleshooting"></a>
## Solución de problemas

| Síntoma | acción |
| --- | --- |
| El requisito previo RTSS permanece abierto | Seleccione el `RTSS.exe` real y la carpeta de perfiles correspondiente, luego verifique nuevamente. |
| Límite guardado pero sin efecto | Inicie RTSS; verifique el perfil/EXE del juego correcto, los permisos de enlace y otros limitadores. |
| Guardar falla | Verifique los permisos de la carpeta y conserve el error/copia de seguridad mostrado. |
| El límite permanece después de la eliminación | Inspeccione RTSS Global y otras herramientas; la acción de basura solo elimina las anulaciones del limitador local. |
| Dos juegos reciben el mismo límite | Compruebe si sus nombres de archivos ejecutables son idénticos. |
| Salir + RTSS deja RTSS abierto | Cierre RTSS normalmente usted mismo; este comando evita deliberadamente la terminación forzada. |

Si restaura manualmente una copia de seguridad RTSS, primero cierre RTSS y conserve el perfil actual antes de reemplazarlo con la copia de seguridad deseada. Esto puede sobrescribir ediciones de perfil no relacionadas; inspeccionar el archivo y la fecha. [Apoyo compartido](../docs/support.md).

<a id="faq"></a>
## Preguntas frecuentes

**¿Necesito también MSI Afterburner?** NVRasterPulse requiere RTSS; no depende de la aplicación Afterburner. Siga las opciones de instalación del distribuidor RTSS.

**¿Puedo usar esto sin ejecutar RTSS?** Puede administrar perfiles una vez que se detecta una instalación, pero RTSS debe ejecutarse para limitarlo.

**¿Al salir o desinstalar se eliminan las mayúsculas?** No. Elimine explícitamente las anulaciones del limitador deseado antes de eliminar NVRasterPulse.

**¿Es un fork o un RTSS?** No. Es un gestor de perfiles independiente; no se incorpora ninguna fuente o ejecutable RTSS.

<a id="upstream-modifications-and-credits"></a>
## Upstream, modificaciones y créditos

El repositorio de desarrollo se origina en [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Se acreditan sus paletas/recursos de interfaz de usuario MIT. 禅堂 Zendo (RevoluSound Team) desarrolló/adaptó los servicios de administración de perfiles, codificación de fracciones, copias de seguridad, puente de recarga RTSS, comportamiento de la bandeja, guía de requisitos previos, idiomas e íconos específicos de la aplicación.

RTSS es desarrollado por **Unwinder** y distribuido por separado a través de Guru3D. NVRasterPulse llama a `UpdateProfiles` desde la DLL de enlace instalada seleccionada; no se redistribuye RTSS SDK ni binario de gancho. El instalador utiliza Inno Setup 7.1.0 sin modificar con scripts/traducciones adaptados y un arranque del proyecto.

[Procedencia completa](../docs/provenance.md) · [Mesa de terceros](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licencia

El paquete distribuye explícitamente NVRasterPulse bajo el [Licencia MIT](../../../../NVRasterPulse/LICENSE) suministrado, conservando Copyright (c) 2016 Orbmu2k. La fuente de la aplicación se mantiene de forma privada; MIT no requiere la publicación de la fuente modificada. RTSS y Windows/.NET permanecen bajo sus propios términos. [Avisos completos](LICENSES/README.md).

Independiente de NVIDIA Corporation, MSI y RTSS; no patrocinado ni respaldado oficialmente por ellos. Los nombres de los productos siguen siendo marcas comerciales de sus propietarios.
