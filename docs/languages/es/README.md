<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · **Español** · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools por 禅堂 Zendo (RevoluSound Team).** Cuatro utilidades Windows independientes para perfiles de controlador NVIDIA, instalación de controladores, límites de marco experimentales Multi Frame Generation y RTSS.

[Consigue las herramientas](docs/downloads.md) · [Instalación](docs/installation.md) · [Compatibilidad y ayuda](docs/support.md) · [Créditos y licencias](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse requiere RTSS.** Instale [RivaTuner Statistics Server de Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) primero. RTSS debe estar ejecutándose para que funcionen sus límites FPS. Se descarga por separado.

<a id="projects"></a>
## Proyectos

| Proyecto | Propósito | Versión | Documentación | Descargar |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Editor de perfiles de controlador NVIDIA con pantalla, color y controles HDR y ICC/WCS agregados. Anteriormente NVPI Custom. | 3.0.2.3 | [Guía](NVIDIA-Profile-Inspector/README.md) | [Paquetes](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Prepare e instale un controlador NVIDIA original con opciones guiadas, copias de seguridad y recuperación. | 0.1.4 | [Guía](NVDriverForge/README.md) | [Paquetes](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Experimental RTX 40 MFG, biblioteca de juegos persistente, diagnóstico y mantenimiento Streamline SDK. | 0.2.3 | [Guía](NVMFG-Unlock40/README.md) | [Paquetes y estado](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Administre los límites RTSS FPS por programa: diagnóstico, sugerencias, pausa, deshacer y compartir perfil. | 0.2 | [Guía](NVRasterPulse/README.md) | [Paquetes](docs/downloads.md#nvrasterpulse) |

**Descargas:** [pagina de descarga](docs/downloads.md) enumera el estado, los archivos y los valores de SHA-256 de cada versión. Las características experimentales y los límites de compatibilidad se describen en las guías del proyecto.

<a id="start-here"></a>
## Empieza aquí

1. Elija una de las herramientas de arriba. Cada uno trabaja de forma independiente; No es necesario instalar toda la suite.
2. Lea sus requisitos y elija **Configuración** para una aplicación instalada o **portátil** para una carpeta separada.
3. Cuando se publique su versión, descargue el recurso de aplicación mencionado, lea los avisos adjuntos y compare su SHA-256.
4. Mantenga copias de seguridad antes de cambiar un controlador, configuración de pantalla, perfil NVIDIA o tiempo de ejecución del juego.

La documentación está disponible en los mismos 34 idiomas que las aplicaciones NV a través del selector en la parte superior de cada guía. GitHub no selecciona automáticamente un archivo README por idioma del navegador. El idioma de la documentación y la configuración de idioma propia de la aplicación son independientes.

<a id="provenance-and-ownership"></a>
## Procedencia y propiedad

Este centro distribuye documentación y aplicaciones compiladas. El código fuente de la aplicación se mantiene de forma privada. Los proyectos upstream conservan su autoría y licencias; la distribución de fuente privada no reemplaza esos términos.

- Profile Inspector fork conserva la licencia Orbmu2k MIT y se identifica explícitamente como fork.
- NVDriverForge tiene sus propios términos de distribución binaria e incluye componentes de herramienta/tiempo de ejecución con licencia independiente.
- NVMFG Unlock40 es una aplicación desarrollada de forma independiente. Se consultó RTX40MFG-Unlock para comparar y perfeccionar; Los componentes nativos compartidos conservan sus créditos MIT. Los términos MinHook y NVIDIA SDK permanecen separados.
- NVRasterPulse conserva la licencia MIT proporcionada y acredita la interfaz de usuario derivada de Profile Inspector. RTSS es un programa externo requerido.

Consulte [tabla de componentes completa](THIRD_PARTY_NOTICES.md), [procedencia del archivo y cambios](docs/provenance.md) y [alcance de la licencia](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Otros proyectos – RevoluSound Team

Estos son proyectos de modificación de audio separados, vinculados aquí para ayudarlo a descubrir el trabajo del equipo.

| juego | Proyecto | Acerca de |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Cambios de sonido del vehículo que cubren motores, escapes, tomas y efectos turbo. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | El paquete de audio del vehículo FH5 posterior del equipo. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Paquete FH5 anterior; su página Nexus dirige a los visitantes al último paquete de equipo anterior. |

Los títulos siguen las páginas Nexus Mods vinculadas. Sus descargas, requisitos, créditos y permisos permanecen en Nexus Mods.

<a id="help-and-participation"></a>
## Ayuda y participación

[Informar un error o sugerir una característica](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Contribuyendo](CONTRIBUTING.md) · [Informes de seguridad](SECURITY.md) · [Registro de cambios](CHANGELOG.md)

Por un problema de seguridad, lea SECURITY.md antes de publicar registros o detalles técnicos. El responsable del mantenimiento debe habilitar los informes privados después de la publicación del repositorio.

> **Proyectos comunitarios independientes.** NV Laboratory, NV Tools y estas utilidades no están afiliadas, patrocinadas ni respaldadas oficialmente por NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS y otros nombres de productos son marcas comerciales de sus respectivos propietarios. Los nombres describen compatibilidad y procedencia, no respaldo oficial.
