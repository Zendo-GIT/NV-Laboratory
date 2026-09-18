<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · **Español** · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Experimental NVIDIA Multi Frame Generation para GeForce RTX 40, con un controlador central y opciones por juego.**

[Descargar 0.2.3 y estado](../docs/downloads.md#nvmfg-unlock40) · [Instalación](#installation) · [aguas arriba](#upstream-and-modifications) · [Licencias](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Descripción general y propósito

NVMFG Unlock40 es una aplicación desarrollada independientemente por 禅堂 Zendo (RevoluSound Team). Combina un controlador Windows, una capa nativa, un asistente de perfil y gestión de juegos/Streamline SDK. Está dirigido a juegos que ya integran NVIDIA DLSS Frame Generation y tiempos de ejecución NVIDIA compatibles.

Se consultó a [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) para comparar y perfeccionar el trabajo. La capa nativa actual contiene componentes compartidos y adaptados, acreditados individualmente a continuación. Esta referencia no convierte a toda la aplicación NVMFG en fork de ese proyecto.

Existe para coordinar el comportamiento experimental MFG de forma centralizada, recordar opciones específicas del juego y mantener visibles las actualizaciones y copias de seguridad en tiempo de ejecución. No agrega DLSS Frame Generation a cada juego ni convierte una implementación arbitraria de FSR.

El paquete actual es **0.2.3**. Agrega una biblioteca de juegos persistente, información de actividad y capacidad, diagnósticos locales y comportamiento de selección/progreso corregido. [Descargas](../docs/downloads.md#nvmfg-unlock40) identifica los archivos y hashes exactos.

<a id="features"></a>
## Características

- Control central de activación/desactivación y arranque de bandeja Windows opcional.
- Selección por juego entre Dynamic MFG, la configuración del juego y los multiplicadores fijos admitidos.
- Separe las opciones recordadas para los estados de encendido/apagado de V-Sync observados.
- Dynamic usa el modo NVIDIA; se suspende cuando V-Sync está apagado, con una opción fija/en el juego separada.
- Guía del menú del juego y exclusiones persistentes; Los juegos sin DLSS FG mantienen el control.
- Descubrimiento de juegos, selección de carpetas principales, búsqueda, agrupación y eliminación sin eliminar archivos del juego.
- Streamline SDK descarga/importación, caché local verificada, selección explícita, copia de seguridad y restauración por juego.
- Verificación de proveedor nativo, diagnóstico por sesión, diario de perfil global y recuperación consciente de conflictos.
- 34 idiomas de interfaz y cuatro temas.

Desactivar FG en el juego lo mantiene apagado. Las opciones fijas de 2x a 6x dependen del juego/menú/tiempo de ejecución; no son una promesa de que todas las combinaciones funcionen. El controlador observa V-Sync y no configura V-Sync o VRR para el usuario.

<a id="compatibility"></a>
## Compatibilidad

| Requisito | Detalles |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| GPU | GeForce RTX 40 objetivo; no hay afirmación de compatibilidad universal GPU |
| juego | Integración NVIDIA DLSS Frame Generation existente y tiempo de ejecución compatible; sin certificación de compatibilidad anti-trampas |
| Proveedor | El candidato está anclado al proveedor SHA-256 documentado en [procedencia](../docs/provenance.md); se rechazan los hashes desconocidos |
| Tiempo de ejecución | .NET 8/WPF 8.0.30 incluido para aplicación/agente; .NET Framework 4.8 para ayudantes de perfil |
| Permisos | Acceso de administrador para las operaciones del controlador/perfil |
| Red | Requerido para descargas oficiales SDK seleccionadas; SDKs compatible importado se puede almacenar en caché localmente |
| Binarios externos | El controlador NVIDIA, el proveedor/modelos NGX y los tiempos de ejecución de juegos Streamline no están incluidos |

Una etiqueta de versión por sí sola es insuficiente: el controlador, el hash del proveedor, la integración del juego y los módulos cargados reales son importantes. Los procesos protegidos o incompatibles pueden rechazar el adjunto. La aplicación no está diseñada para evadir las protecciones antitrampas.

<a id="installation"></a>
## Instalación

1. Lea el [estado del candidato y nota de licencia](../docs/downloads.md#nvmfg-unlock40).
2. Descargue `NVMFGUnlock40-0.2.3-Setup-x64.exe` o `NVMFGUnlock40-0.2.3-Portable-x64.zip` cuando su versión esté disponible.
3. Consulte SHA-256 y conserve los avisos adjuntos. Instale .NET Framework 4.8 si Windows aún no lo proporciona.
4. Ejecute el programa de instalación o extraiga el ZIP portátil **completo** en una carpeta local grabable.
5. Inicie `NVMFGUnlock40.exe`; mantenga `agent`, `driver`, `engine` y `Licenses` en el diseño suministrado.

La carpeta denominada `driver` contiene ayudas de espacio de usuario, no un controlador del kernel. No copie solo el EXE principal ni reemplace el hash del proveedor para forzar la compatibilidad. Los EXE actuales no están firmados.

<a id="usage"></a>
## Uso

1. Comience con el controlador desactivado. Agrega un juego o una carpeta principal y elige las instalaciones reales.
2. Revise la configuración MFG de cada juego. Responder qué ofrece su menú; la respuesta se almacena por juego.
3. Elija Dynamic o la configuración del juego globalmente, luego ajuste las opciones elegibles por juego según sea necesario.
4. Habilite el controlador solo cuando desee utilizarlo. Puede cambiar temporalmente seis configuraciones de perfil globales NVIDIA, con un diario de recuperación.
5. Inicie un juego elegible y habilite su propio DLSS Frame Generation. Siga cualquier solicitud para la opción V-Sync-off.
6. Utilice exclusiones para juegos que no desee administrar. Eliminar un juego registra una exclusión y conserva sus archivos/copias de seguridad.
7. Utilice el flujo completo de salida/desactivación y recuperación de la aplicación cuando haya terminado.

Cerrar la ventana principal puede dejar el controlador en la bandeja. Una DLL ya cargada en un juego permanece allí hasta que el juego sale; Desactivar el controlador no es una garantía de descarga. Cierre los juegos afectados antes del mantenimiento o las actualizaciones.

**Streamline SDKs:** en la página NVIDIA SDK, descargue una versión oficial o importe un SDK local compatible. La importación almacena una copia verificada; **Use this version** lo selecciona y **Uninstall** elimina esa copia almacenada en caché. Las DLL Streamline que faltan se pueden complementar desde un NVIDIA SDK oficial, con la fuente que se muestra. Esto no descarga ni reemplaza un modelo NGX. Cierra el juego, selecciona la actualización deseada y conserva su copia de seguridad original. Para revertir archivos del juego, use la restauración de copia de seguridad, no el botón Uninstall del caché.

<a id="library-diagnostics-and-updates"></a>
## Biblioteca, diagnósticos y actualizaciones.

**Biblioteca persistente:** seleccione varias carpetas del juego, incluidas diferentes unidades, antes de iniciar un análisis. El progreso es visible y la cancelación está disponible. Después del primer escaneo, un caché local restaura la biblioteca al iniciarlo sin recorrer todas las carpetas del juego. Actualice para buscar cambios o agregar otra carpeta. Las operaciones de mantenimiento aún revalidan los archivos afectados; el monitoreo de respaldo permanece activo. El caché se almacena en `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Selección:** Ctrl+A selecciona todo y Ctrl+D borra la pestaña Juegos o Copias de seguridad activos. No se selecciona ningún juego automáticamente. Las actualizaciones y actualizaciones de actividades ya no crean selecciones fantasma ni recuentos inconsistentes.

**Actividad y compatibilidad:** la información MFG por juego proviene de observaciones NGX sin una nueva superposición. No es un recuento físico de fotogramas mostrados. La compatibilidad con Dynamic-con-V-Sync proviene de las capacidades de tiempo de ejecución; La capacidad desconocida no se deduce de un número de versión. La aplicación no cambia ni V-Sync ni VRR. Con V-Sync desactivado, Dynamic permanece suspendido; Las opciones fijas o controladas por el juego están separadas.

**Próximo lanzamiento:** la exclusión temporal omite la aplicación de parches en el próximo lanzamiento del juego y restaura la administración normal después de su salida. No puede eliminar una DLL ya cargada en un juego: cierra y reinicia ese juego. Wallpaper Engine se reconoce como una aplicación de escritorio; esta corrección preserva la protección de los juegos reales ignorados.

**Preferencias y soporte:** la importación/exportación de preferencias requiere la reasociación manual de las carpetas del juego. El diagnóstico local en Acerca de filtra información privada e informa los códigos de error NVAPI disponibles o las categorías de conflicto. Revíselo antes de compartirlo; nada se carga automáticamente.

**Actualizaciones de la aplicación:** una verificación opcional muestra las notas de la versión y ofrece la configuración oficial. La descarga explícita se compara con el tamaño GitHub y los metadatos SHA-256; usted mismo inicia la instalación. La versión 0.2.3 también borra los mensajes de progreso completados y al mismo tiempo conserva errores y resultados significativos. Estas adiciones incluyen los cambios desde la versión pública 0.1.1.

<a id="screenshots"></a>
## Capturas de pantalla

![NVMFG SDK-lista de vista previa](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Representación de la interfaz 0.1.1 en inglés existente con un inventario SDK de ejemplo. No es una lista de versiones actuales ni evidencia de un juego en ejecución. [Procedencia de la imagen](../assets/README.md).

<a id="update-and-uninstall"></a>
## Actualizar y desinstalar

Cerrar los juegos afectados. Deshabilite/salga de NVMFG y resuelva cualquier recuperación de configuración de NVIDIA pendiente antes de actualizar. Instale la siguiente configuración con la identidad existente o extraiga el nuevo dispositivo portátil en una carpeta nueva; conservar el estado/copias de seguridad.

Antes de desinstalar, restaure las copias de seguridad SDK del juego deseado y la configuración NVIDIA a través de la aplicación, luego cierre los juegos y salga del controlador. Utilice Windows **Installed apps** para la configuración o elimine la carpeta portátil cerrada después de conservar los archivos necesarios. No elimine manualmente un diario de recuperación activo para desbloquear la instalación.

Las copias de seguridad locales en tiempo de ejecución del juego utilizan `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Configuración MFG/uso de datos SDK `%LOCALAPPDATA%\RtxMfg`; La salida de la sesión se encuentra en `Sessions`, al lado de la aplicación. Estos archivos pueden contener rutas de juego. No los publique sin redactar.

<a id="known-limitations"></a>
## Limitaciones conocidas

- Un bloqueo de activación/restauración/desinstalación de 0.1.1 informado no se reproduce y se desconoce su causa. Esta versión no pretende solucionarlo. Después de una falla, conserve el diario de recuperación e inspeccione el diagnóstico local; no fuerce la eliminación de los datos de recuperación.
- Los parches nativos experimentales pueden provocar fallas o artefactos visuales; un bloqueo Bodycam no resuelto se registra en el historial de desarrollo.
- Las pruebas de renderizado controlado no son una certificación para todos los juegos, controladores o antitrampas.
- Los fotogramas generados no crean nuevas muestras de entrada; Este centro no promete ninguna latencia medida ni ganancia de rendimiento.
- Varias herramientas/superposiciones de generación de fotogramas pueden entrar en conflicto. La aplicación informa los módulos observados sin probar todos los escenarios de coexistencia.
- El manifiesto de compatibilidad es una ayuda para la detección, no una lista de juegos completamente probados.
- Los términos NVIDIA SDK completos y la restricción de limitación técnica no resuelta permanecen documentados en [procedencia](../docs/provenance.md).

<a id="troubleshooting"></a>
## Solución de problemas

| Síntoma | acción |
| --- | --- |
| Proveedor no compatible | Conserve los archivos originales verificados. Informar las versiones del controlador/proveedor y el error; no omita la verificación de hash. |
| No hay DLSS FG en el juego. | Selecciona esa respuesta y deja el juego bajo control; esta herramienta no puede fabricar esa integración. |
| Fallos/artefactos del juego | Salga del juego, desactive NVMFG, use la copia de seguridad del tiempo de ejecución original del juego si se modificó e informe detalles reproducibles. |
| SDK lista o descarga no disponible | Actualiza y consulta la fuente oficial; una versión almacenada en caché/importada aún debe pasar la validación. |
| Pendiente de salida/actualización de bloques de recuperación NVIDIA | Utilice la recuperación y conserve el diario; Los conflictos no deben sobrescribirse a ciegas. |
| Un juego eliminado no se redescubre | Su exclusión es persistente. Agréguelo explícitamente cuando desee que se administre nuevamente. |

[Guía de soporte compartido](../docs/support.md) explica qué incluir en un informe.

<a id="faq"></a>
## Preguntas frecuentes

**¿Incluye DLL o modelos NVIDIA?** No se incluye ningún controlador, proveedor/modelo NGX ni tiempo de ejecución Streamline. Las descargas explícitas de SDK provienen de NVIDIA.

**¿Dynamic funciona con V-Sync apagado?** Está suspendido en ese estado. Elige la configuración del juego o un multiplicador fijo elegible para el estado separado de ese juego.

**¿Es este un paquete ReShade/OptiScaler/FSR?** No. No se compilan ni se envían como parte de este paquete de producción.

**¿Las fuentes modificadas son públicas?** No. Se proporcionan paquetes compilados y créditos/licencias requeridos. Esto no elimina derechos o restricciones de terceros.

<a id="upstream-and-modifications"></a>
## Upstream y modificaciones

Referencia de comparación y componentes nativos compartidos: **RTX40MFG-Unlock por Michael Robles / dashdogy**, referencia confirmada `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Repositorio](https://github.com/dashdogy/RTX40MFG-Unlock) · [Descargas originales](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

La comparación de fuentes identifica parches compartidos, manejo de proveedores/políticas, correcciones temporales y componentes de desvío basados en MinHook. Se conservan sus avisos MIT y BSD. La comparación completa también incluye archivos fuera del objetivo de producción.

La aplicación de escritorio, el controlador y el flujo de trabajo de administración SDK son desarrollados por 禅堂 Zendo (RevoluSound Team). El trabajo del proyecto incluye carga central, integración de arranque NGX, selección de proveedor verificada, coordinación juego/V-Sync y diagnóstico de sesión. La guía de procedencia separa ese trabajo de los componentes compartidos; una comparación de archivos por sí sola no establece cuándo alguno de los autores tuvo la idea.

El asistente de perfil adapta el contenedor MIT NVAPI del Profile Inspector de Orbmu2k. [Procedencia detallada y alcance de los componentes](../docs/provenance.md).

<a id="credits-and-license"></a>
## Créditos y licencia

Michael Robles; Orbmu2k; Colaboradores de Tsuda Kageyu y HDE; NVIDIA Corporation; Microsoft y contribuyentes; Inno Setup autores y traductores. Desarrollo de aplicaciones, integraciones y empaquetado: 禅堂 Zendo (RevoluSound Team).

Se conservan el [permiso existente para compartir paquetes compilados](../../../../NVMFG-Unlock40/LICENSE) y todos los [licencias de componentes](LICENSES/README.md). Los permisos MIT para el código ascendente son distintos de los términos NVIDIA SDK. Ninguna licencia general los reemplaza.

Independiente, no patrocinado ni respaldado oficialmente por NVIDIA Corporation. Todas las marcas comerciales a las que se hace referencia siguen siendo propiedad de sus propietarios.
