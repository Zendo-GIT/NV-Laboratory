<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · **Español** · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Procedencia, cambios y licencias

Esta auditoría describe los candidatos preparados el **2026-09-09**. Las fuentes de las aplicaciones siguen siendo privadas; los inventarios públicos contienen nombres de archivos y hashes, no código fuente. Consulte [avisos de componentes completos](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referencia: Orbmu2k/nvidiaProfileInspector confirma `592d962cca8827efe8859461a84267755595064a`; Versión ejecutable candidata 3.0.2.3. La confirmación de referencia y la versión ensamblada de fork son identificadores diferentes; no se deduce ninguna versión de lanzamiento ascendente de la versión fork.

Los 157 archivos fuente/recursos del complemento limpio se compararon con esa confirmación: 2 bytes idénticos, 134 que difieren solo en los finales de línea o la lista de materiales UTF-8, 11 modificados, 10 ausentes en la ruta ascendente comparada. "Agregado" es relativo a esa ruta y no es por sí solo prueba de la autoría original.

[Comparación completa de archivos/hash](../../../provenance/nvpi-source-provenance.json).

| Área | Trabajo heredado | Fork contribución |
| --- | --- | --- |
| editor de perfil | Modelo de perfil, importación/exportación, asociaciones de aplicaciones y datos de referencia. | Integración con Screen y el lanzador de herramientas externo |
| NVAPI | Interoperabilidad DRS de Orbmu2k | Interoperabilidad relacionada con el color/pantalla, restricciones de carga nativa de producción y eliminación de simulacros |
| Servicios de visualización | API Windows/NVIDIA como interfaces externas | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| interfaz de usuario | Recursos, paletas e íconos WPF ascendentes | Diálogos de pantalla, confirmación de 15 segundos, estado/lectura y diseño de la barra de herramientas |
| Lanzador | Shell de aplicación existente | Búsqueda y lanzamiento protegidos de RasterPulse instalados por separado |
| Embalaje | MIT aguas arriba | Compañero independiente y limpio, instalador/desinstalador independiente, avisos retenidos |

El mapa de fuentes públicas incluye rutas de soluciones/recursos para la trazabilidad; esos archivos no se distribuyen como fuente. Se excluyen las pruebas de desarrollo, las interfaces simuladas y el antiguo binario combinado NVPI/RasterPulse.

<a id="nvdriverforge"></a>
## NVDriverForge

Aplicación independiente C#/.NET 8/WPF; El flujo de trabajo de cara al usuario está inspirado en parte en NVCleanstall. No se identificó ninguna fuente/binario NVCleanstall en la carga útil de producción. No está representado como fork de esa aplicación propietaria.

El trabajo del proyecto original incluye análisis/selección de componentes, trabajos de instalación protegidos, copias de seguridad y recuperación de transacciones, descargas del catálogo NVIDIA, comprobaciones de actualizaciones, explicaciones localizadas, flujos de trabajo avanzados/NVENC opcionales y arranque del instalador.

Componentes heredados/adaptados: cuatro paletas de temas NVPI, referencia de interfaz DRS NVAPI extendida y el complemento MIT NVPI opcional por separado. La interfaz de usuario de selección del valor preestablecido Custom NV y la integración de transacciones permitidas pertenecen a NVDriverForge; el ajuste preestablecido no es una recomendación oficial NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 y Inno Setup siguen siendo componentes externos sin modificar y utilizados según sus propios términos. keylase NVENC los datos no están incrustados; Se elige y verifica una confirmación exacta cuando el usuario solicita una descarga compatible. No se estableció ninguna licencia de redistribución para esos datos ascendentes.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 fue desarrollado de forma independiente por 禅堂 Zendo (RevoluSound Team). El mantenedor utilizó RTX40MFG-Unlock para comparar y refinar. La aplicación en su conjunto no se presenta como fork. Esta distinción no elimina los créditos de los componentes compartidos/adaptados en la capa nativa actual.

Referencia de comparación: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, confirmación `4e776d068f91b4a665425542bb005dd57cc3d891`. El árbol privado del motor nativo contiene 48 archivos comparados: 35 diferencias de solo formato, 4 archivos modificados y 9 ausentes en la ruta de referencia. [Comparación completa](../../../provenance/nvmfg-source-provenance.json).

Archivos heredados modificados: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Las rutas adicionales incluyen `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` y una licencia ascendente retenida.

Unidades de producción C++: parcheador, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection y vsync_observer; además del conjunto entry_detour y el amortiguador/gancho/trampolín/HDE64 MinHook. La interfaz ReShade heredada, los recursos shim heredados y los objetivos CMake no utilizados no forman parte de esta compilación de producción.

Los componentes de emparejamiento cubren la política de parches/proveedores y el trabajo temporal; sus avisos de derechos de autor y permiso permanecen intactos. La coordinación central NGX/bootstrap/controlador, el manejo V-Sync por juego, el diagnóstico de sesión y la aplicación Windows/SDK/flujo de trabajo de respaldo son trabajos de proyecto de 禅堂 Zendo (RevoluSound Team). Los recuentos anteriores describen archivos, incluidos archivos de terceros y no utilizados, no un porcentaje de autoría ni la cronología de la idea de cualquiera de los proyectos.

El asistente adapta NvapiDrsWrapper y NativeArrayHelper de NVPI en un ensamblaje separado, con lógica de perfil creada por el proyecto. Se excluye el antiguo camino simulado de desarrollo. Las paletas familiares compartidas se originan en NVPI.

Referencia MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; el subconjunto compilado heredado no tiene cambios locales funcionales en la comparación. Cabeceras de integración Streamline: 2.12; licencia de encabezado abierto verificada en v2.12.0. Fuente del encabezado NGX: NVIDIA/DLSS confirma `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Motor candidato SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Proveedor requerido SHA-256 en engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Una familia de proveedores 310.9 informada no es intercambiable con este hash exacto. No se incluye ningún DLL ni modelo de proveedor.

**Punto de licencia excepcional:** la licencia completa NVIDIA RTX SDK, versión del 14 de marzo de 2024, contiene una restricción de la sección 4(d) relevante para eludir las limitaciones técnicas. La auditoría no establece permiso para este uso. Conservar la licencia del motor MIT, ser gratuito u observar otras modificaciones no resuelve esa condición separada. La preparación del candidato no es una autorización legal. El aviso de encabezado breve original se complementa con la licencia completa; su texto Windows-1252 también se proporciona como UTF-8 legible, y se conservan los bytes originales.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Administrador de perfiles RTSS independiente desarrollado en el repositorio derivado de NVPI. Los recursos/paletas de UI MIT heredados y el origen del proyecto permanecen acreditados. La aplicación de producción utiliza explícitamente la licencia MIT proporcionada.

Trabajo del proyecto: análisis/escritura precisa del perfil RTSS y codificación fraccionada, copias de seguridad, eliminación de anulaciones, puente de recarga, detección de requisitos previos, interfaz de usuario compacta, ciclo de vida de la bandeja, controles de inicio y localización. RTSS realiza una limitación real.

No se incluye ninguna fuente RTSS, DLL de enlace, SDK ni instalador. El puente llama a la exportación en una instalación RTSS existente seleccionada por el usuario. En este paquete no hay ningún paquete de controlador NVIDIA, limitador experimental nativo, Framepacer, MinHook, ReShade o DLSS runtime.

<a id="assets-generated-data-and-tools"></a>
## Activos, datos generados y herramientas.

[Créditos de activos](../assets/README.md) identifica las vistas previas de la interfaz existente y el selector de configuración NVPI. Los valores ficticios que contienen están etiquetados. No se copia ningún juego/activo Nexus, perfil personal, ICC privado, logotipo corporativo NVIDIA o archivo de fuente.

Los nombres de compatibilidad de juegos generados heredados en NVMFG son una ayuda de detección, no una prueba de prueba. Los catálogos de instalador generados se acreditan en [avisos del traductor](../../../../licenses/INSTALLER-TRANSLATORS.md). Los registros de compilación generados con rutas absolutas permanecen privados.

Las herramientas de compilación privadas incluyen scripts de auditoría .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup y Python. Sus compiladores, encabezados, ejecutores de pruebas y recursos de depuración no se distribuyen. El CRT de versión estática permanece según los términos aplicables de la cadena de herramientas de Microsoft.

<a id="scope-of-verification"></a>
## Alcance de la verificación

La auditoría local hizo un inventario de todos los archivos en las tres raíces de desarrollo y excluyó las bases de datos de objetos Git y los destinos de directorios vinculados. Se escanearon fuentes/documentos activos; Las construcciones históricas fueron inventariadas y excluidas. Los ZIP seleccionados y las cargas útiles actuales se escanearon y aplicaron hash; Los paquetes .NET se descomprimieron para una inspección adicional. Esa auditoría inicial no ejecutó ningún producto, instalador, juego, proceso RTSS o controlador.

La última revisión 2 de la configuración NVPI corrige la selección de idioma independiente utilizando los controles Inno compartidos y el arranque. Los dispositivos privados claros/oscuros verificaron la navegación con el mouse y el teclado y los 34 códigos de idioma explícitos. El selector de configuración real se abrió en un escritorio privado que nunca se muestra y se canceló antes de la instalación. Sus siete archivos de aplicación y su ZIP portátil se mantienen sin cambios. NVDriverForge 0.1.3 incluye el compañero corregido y aún reenvía `/LANG`.

NVDriverForge 0.1.3 se completó el 10 de septiembre de 2026. Su informe de verificación privado registra 366 pruebas de aplicación, 118 comprobaciones complementarias, 32 comprobaciones de configuración, 156 comparaciones nativas y 34 casos de reenvío de idiomas. La corrección de selección de componentes protegidos se reprodujo en un paquete de controlador original sin cambiar su carga útil ni instalar el controlador. Estos son resultados fechados del equipo del producto, no pruebas repetidas por esta actualización de documentación ni prueba de una instalación real exitosa del controlador.

Esta actualización del centro no cambia ningún código de aplicación funcional. Las pruebas anteriores de compilación/unidad/UI de aplicaciones siguen siendo evidencia histórica anticuada. Esto no es ingeniería inversa completa de cada binario de terceros ni una garantía contra todos los patrones secretos posibles.
