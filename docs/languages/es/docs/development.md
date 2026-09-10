<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · **Español** · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducción asistida por máquina del inglés. Se conservan los nombres técnicos, comandos, URL y textos legales originales. Se aceptan reseñas de hablantes nativos; consulte la referencia en inglés si la redacción no está clara.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Arquitectura y mantenimiento del repositorio.

NV Laboratory es un **centro de documentación y distribución binaria** público. No contiene la fuente de la aplicación. Los cuatro proyectos conservan árboles de construcción, versiones, identidades y activos de lanzamiento separados. Su historial de desarrollo privado no se importa a este repositorio de Git.

<a id="layout"></a>
## Diseño

| Ubicación | Propósito |
| --- | --- |
| README.md / README.fr.md | Puntos de entrada inglés/francés |
| Cuatro carpetas de proyectos | Guías completas y avisos originales aplicables. |
| documentos | Descargas, compatibilidad, procedencia, desarrollo y procedimiento de lanzamiento. |
| documentos/releases.json | Metadatos, tamaños y hashes de lanzamiento/candidato auditados |
| documentos/procedencia | Comparaciones de archivos/hash; sin código de aplicación |
| licencias | Textos completos compartidos de terceros y créditos del traductor del instalador. |
| activos | Vistas previas de UI revisadas existentes y su procedencia |
| .github | Formularios de emisión y validación de documentación de solo lectura |
| herramientas/validate_repository.py | Comprobaciones de enlaces y límites de publicación de bibliotecas estándar |

El inglés sigue siendo el valor predeterminado GitHub README. Los enlaces `.fr.md` adyacentes existentes siguen siendo válidos. Traducciones adicionales reflejan la documentación bajo `docs/languages/<code>`; el selector de idioma mantiene la misma página al cambiar de idioma. El catálogo `docs/languages/catalog.json` registra los 34 idiomas y las huellas digitales de origen. GitHub no selecciona automáticamente un archivo README por idioma del navegador. Consulte [índice de idiomas y política de traducción](../../README.md).

<a id="application-technologies"></a>
## Tecnologías de aplicación

| Programa | Tecnología privada | Distribución |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interoperabilidad | Carpeta portátil completa y separada Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; arranque nativo de C++; Proceso 7-Zip | EXE y configuración portátil autónomo |
| NVMFG Unlock40 | C#/WPF .NET 8, ayudantes de Framework 4.8, motor C++20/MASM/MinHook | Árbol portátil y configuración. |
| NVRasterPulse | Marco C#/WPF 4.8; RTSS integración de perfil/recarga; arranque nativo | Árbol portátil y configuración. |

Este pago público no puede reconstruir las aplicaciones. Los archivos automáticos “Source code” son instantáneas del concentrador. Los enlaces de fuentes ascendentes no representan la fuente privada modificada exacta. El CI público valida únicamente este repositorio.

<a id="local-checks"></a>
## controles locales

Desde la raíz del repositorio:

```text
python tools/validate_repository.py
```

Python 3.10 o más reciente es suficiente. La verificación lee archivos, enlaces de Markdown locales, avisos requeridos/enlaces RTSS, metadatos de lanzamiento y límites de publicación. No ejecuta el software, no instala dependencias ni contacta con una red.

El flujo de trabajo GitHub ejecuta esta misma verificación con permiso de contenido de solo lectura en push, pull request o envío manual. El proceso de pago está anclado a una confirmación auditada y no conserva las credenciales. No hay ningún trabajo de lanzamiento o implementación configurado.

<a id="maintain-the-boundary"></a>
## Mantener el límite

Actualice juntas la referencia en inglés, las guías en francés y las traducciones afectadas. Mantenga los cambios sustanciales separados de las comparaciones de formato únicamente. Registre hashes de candidatos reales, referencias de compromisos ascendentes y licencias; Nunca infieras una licencia a partir de la popularidad de un proyecto.

Utilice activos de versión con versiones nuevas y vuelva a auditar los binarios, archivos y avisos integrados modificados. Conserve las copias de seguridad privadas fuera de este repositorio. No utilice un flujo de trabajo público para importar fuentes de aplicaciones privadas o carpetas de compilación locales.

Pruebas apropiadas para un cambio de aplicación funcional ejecutadas en el proyecto privado. No vuelva a ejecutar los instaladores de controladores ni escriba perfiles reales para una actualización de la documentación. [Procedimiento de liberación manual](releasing.md).
