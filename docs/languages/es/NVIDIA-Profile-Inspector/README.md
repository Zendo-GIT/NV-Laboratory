<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · **Español** · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Un fork independiente de [NVIDIA Profile Inspector por Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), con controles de visualización agregados.** Nombre anterior del proyecto: **NVPI Custom**.

[Estado de descarga y lanzamiento](../docs/downloads.md#nvidia-profile-inspector) · [Instalación](#installation) · [Upstream y cambios](#upstream-and-changes) · [Licencia](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Descripción general

La aplicación edita los perfiles del controlador NVIDIA, incluida la configuración por aplicación. Este fork también agrega un editor de **Pantalla** para la pantalla Windows activa: resolución, frecuencia de actualización, configuración de color de salida, HDR y asociaciones de perfiles ICC/WCS instaladas.

Existe para incorporar controles de visualización relacionados al editor de perfiles y hacer que los resultados de vista previa, confirmación y restauración sean más claros. No establece nuevas capacidades de hardware.

El primer candidato es **3.0.2.3**, y utiliza la compilación complementaria independiente limpia del 9 de septiembre de 2026. Su ejecutable existente sigue siendo `nvidiaProfileInspector.exe`; el instalador y algunas etiquetas internas todavía dicen `NVPI Custom NV`. El título público anterior identifica fork sin cambiar la identidad de instalación ni pretender que es la versión oficial de Orbmu2k.

<a id="features"></a>
## Características

- Exploración de perfiles ascendentes existentes, asociaciones de aplicaciones, ediciones de configuración e importación/exportación de perfiles.
- **Pantalla** cuadro de diálogo para visualización, modo, Hz, RGB/YCbCr, profundidad de color, rango y colorimetría.
- Control Windows HDR y selección de asociación ICC/WCS instalada.
- Una vista previa de pantalla de 15 segundos con **Mantener** / **Revertir** y restauración del tiempo de espera.
- Lectura de cambios de modo/HDR y fallas de restauración informadas.
- Informes separados de HDR, SDR con ACM/WCG y profundidad de color de la señal.
- Un iniciador NVRasterPulse para una copia elegible instalada por separado.

<a id="compatibility"></a>
## Compatibilidad

| Requisito | Detalles |
| --- | --- |
| Sistema | Windows 10/11 x64 con un controlador NVIDIA compatible |
| Tiempo de ejecución | [Marco .NET 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), suministrado por Windows o instalado por separado |
| Permisos | El editor solicita acceso de administrador cuando se abre |
| Pantallas | Los modos reales y las combinaciones de colores dependen de GPU, el controlador, la pantalla, el cable y las API Windows. |
| Herramientas opcionales | NVRasterPulse para gestión de límites RTSS; ni este ni RTSS son necesarios para el editor de pantalla |
| Idiomas | Configuración: selector de 34 idiomas. El editor conserva el soporte de idiomas existente. |

No existe un mínimo de controlador universal verificado ni una matriz de soporte para cada GPU. Las opciones de bpc disponibles en el cuadro de diálogo son solicitudes, no combinaciones certificadas. Los controles HDR modernos y el antiguo respaldo Windows tienen capacidades diferentes.

<a id="installation"></a>
## Instalación

1. Abra [pagina de descarga](../docs/downloads.md#nvidia-profile-inspector) y verifique el estado de la publicación.
2. Descargue la instalación o el recurso portátil y compare su SHA-256 con el manifiesto de versión.
3. Para la configuración, ejecute `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, seleccione un idioma y siga el instalador. Crea su propio acceso directo y desinstalador.
4. Para portátil, extraiga el ZIP completo en una nueva carpeta grabable. Mantenga `Reference.xml`, la configuración EXE y todos los avisos al lado del ejecutable.
5. Inicie `nvidiaProfileInspector.exe`.

La instalación del editor por sí sola no aplica un perfil ni instala un controlador GPU. El complemento se instala por separado, no se hace cargo de las asociaciones `.nip` y no permite el inicio al iniciar sesión. Los binarios existentes no están firmados.

<a id="usage"></a>
## Uso

**La revisión 2 del instalador** agrega el mismo selector nativo de 34 idiomas que las otras herramientas, con navegación por mouse/teclado, apariencia clara/oscura y cancelación. La elección se aplica a la configuración; no traduce el editor NVPI. Un argumento `/LANG=fr` explícito o un modo silencioso omite la selección de las personas que llaman que ya proporcionan un idioma.

**Perfiles de controlador:** seleccione un perfil, exporte una copia de seguridad, luego edite solo las configuraciones deseadas y aplíquelas. Las asociaciones de aplicaciones determinan qué juego recibe un perfil. Un valor almacenado no es prueba de que todos los controladores o juegos lo utilicen.

**Controles de visualización:** abra **Pantalla**, elija la visualización y los valores solicitados, luego inicie la vista previa. Verifique la imagen antes de elegir **Mantener** dentro de los 15 segundos. Utilice **Revertir**, cierre la confirmación o déjela caducar para solicitar la restauración. Lea cualquier mensaje de error: una llamada API exitosa por sí sola no es prueba de restauración.

Una selección ICC cambia una asociación de perfil instalada; no genera, calibra ni redistribuye un archivo ICC. HDR, ACM/WCG, RGB/YCbCr y bpc describen diferentes aspectos de la canalización. No se proporciona ningún nuevo interruptor ACM independiente.

**NVRasterPulse:** el botón de la barra de herramientas acepta una instalación registrada por separado en todo el sistema debajo de Archivos de programa con propiedad y permisos protegidos. Este lanzador elevado puede rechazar una copia portátil o una ruta vinculada/escribible por el usuario. En ese caso, abra NVRasterPulse usando su propio acceso directo. [Instale RTSS por separado](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) para usar NVRasterPulse.

<a id="screenshots"></a>
## Capturas de pantalla

![NVPI configuración revisión 2 selector de idioma](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Selector de configuración real en francés, capturado durante una prueba aislada y luego cancelado. Esto muestra el instalador; el editor conserva su interfaz y su cuadro de diálogo de pantalla.

<a id="update-and-uninstall"></a>
## Actualizar y desinstalar

Cierre el editor antes de actualizar. Mantenga los perfiles exportados y descargue la nueva versión fork; instálelo sobre la misma identidad complementaria o extraiga archivos portátiles en una carpeta nueva. No mezcle un `Reference.xml` antiguo con un ejecutable nuevo. La supresión de verificación de actualización ascendente incluida pertenece a este fork.

Para obtener una copia instalada, utilice Windows **Installed apps** y su desinstalador. Para portátil, ciérrelo y elimine la carpeta extraída cuando sus exportaciones estén seguras. Eliminar el editor **no** deshace las ediciones del perfil del controlador, las preferencias de visualización, NVRasterPulse o RTSS. Restaure la configuración deseada antes de la eliminación.

<a id="known-limitations"></a>
## Limitaciones conocidas

- La confirmación de 15 segundos no es un mecanismo de vigilancia para cada accidente de conductor, pérdida de energía o apagado forzado.
- Algunas combinaciones de color/profundidad/actualización devuelven `NVAPI_NOT_SUPPORTED`.
- La lectura del software no mide la profundidad de bits del panel, la precisión del color ni la latencia.
- La configuración de la pantalla afecta la pantalla Windows actual; Este cuadro de diálogo no crea ajustes preestablecidos de visualización por juego.
- No hay garantía de rendimiento, anti-trampas o compatibilidad universal HDR.

<a id="troubleshooting"></a>
## Solución de problemas

| Síntoma | acción |
| --- | --- |
| Error de tiempo de ejecución al iniciar | Verifique las actualizaciones de Windows y .NET Framework 4.8; Utilice el paquete completo. |
| Modo de visualización solicitado rechazado | Revierta y pruebe un modo ofrecido por Windows/NVIDIA para esa pantalla. Lea el error exacto y evite repetidos cambios ciegos. |
| HDR o el color vuelve al estado anterior | Verifique si otra operación falló y desencadenó la restauración; distinguir HDR de ACM. |
| NVRasterPulse El botón rechaza una ruta | Inicie su propio atajo; este botón requiere una instalación protegida en todo el sistema. |
| Queda un cambio después de la desinstalación | Restaure el perfil NVIDIA exportado o la configuración de pantalla Windows deseada; La desinstalación no es una reversión de la configuración. |

Consulte [guía de soporte compartido](../docs/support.md) antes de enviar registros.

<a id="faq"></a>
## Preguntas frecuentes

**¿Es este software oficial NVIDIA o la versión oficial de Orbmu2k?** No. Es un fork independiente; el autor original y la licencia MIT permanecen acreditados.

**¿NVDriverForge requiere este editor?** No. El ajuste preestablecido opcional Custom NV de NVDriverForge utiliza su propia integración. Instalar el editor es una opción aparte.

**¿RTSS es obligatorio para este fork?** No. RTSS es obligatorio para el limitador FPS de NVRasterPulse, no para la edición de perfil o pantalla.

**¿Dónde está la fuente?** La fuente de la aplicación modificada se mantiene de forma privada. Se proporcionan el aviso MIT y el repositorio ascendente; MIT no requiere la publicación de la fuente modificada.

<a id="upstream-and-changes"></a>
## Upstream y cambios

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), confirmación de referencia `592d962cca8827efe8859461a84267755595064a`. [Descargas originales](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Heredado: editor de perfiles, interoperabilidad NVAPI, datos de referencia, recursos y temas de UI. 禅堂 Zendo (RevoluSound Team) agregó o adaptó servicios de visualización, transacciones HDR/ICC, confirmación/lectura de 15 segundos, diseño de barra de herramientas y comportamiento de inicio de RasterPulse. El complemento limpio excluye simulacros de desarrollo/puntos de entrada de prueba, utiliza un iniciador externo protegido y proporciona un instalador independiente. El antiguo paquete de desarrollo combinado NVPI/RasterPulse no es el candidato en este centro.

[Procedencia detallada del archivo](../docs/provenance.md) · [Aviso original fork](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Créditos y licencia

Copyright (c) 2016 Orbmu2k. Se conserva el [Licencia MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) suministrado. Adaptaciones y embalaje: 禅堂 Zendo (RevoluSound Team). El instalador utiliza Inno Setup; Windows y .NET Framework siguen siendo externos. [Avisos completos aplicables](LICENSES/README.md).

Independiente, no patrocinado ni respaldado oficialmente por NVIDIA Corporation. Las marcas comerciales permanecen con sus respectivos propietarios.
