<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Arquitetura e manutenção de repositório

NV Laboratory é um hub público de **documentação e distribuição binária**. Ele não contém fonte de aplicativo. Os quatro projetos mantêm árvores de construção, versões, identidades e ativos de lançamento separados. Seu histórico de desenvolvimento privado não é importado para este repositório Git.

<a id="layout"></a>
## Disposição

| Localização | Objetivo |
| --- | --- |
| README.md / README.fr.md | Pontos de entrada em inglês/francês |
| Quatro pastas de projeto | Guias completos e avisos originais aplicáveis |
| documentos | Downloads, compatibilidade, procedência, desenvolvimento e procedimento de lançamento |
| documentos/releases.json | Metadados, tamanhos e hashes de candidatos/lançamentos auditados |
| documentos/procedência | Comparações de arquivo/hash; nenhum código de aplicativo |
| licenças | Textos completos de terceiros compartilhados e créditos do tradutor do instalador |
| ativos | Pré-visualizações de IU revisadas existentes e sua origem |
| .github | Emissão de formulários e validação de documentação somente leitura |
| ferramentas/validate_repository.py | Limites de publicação da biblioteca padrão e verificações de links |

O inglês continua sendo o README padrão do GitHub. Os links `.fr.md` adjacentes existentes permanecem válidos. Traduções adicionais refletem a documentação em `docs/languages/<code>`; o seletor de idioma mantém a mesma página ao mudar de idioma. O catálogo `docs/languages/catalog.json` registra todos os 34 idiomas e impressões digitais de origem. GitHub não seleciona automaticamente um README por idioma do navegador. Consulte o [índice de idioma e política de tradução](../../README.md).

<a id="application-technologies"></a>
## Tecnologias de aplicação

| Programa | Tecnologia privada | Distribuição |
| --- | --- | --- |
| NVPI fork | Interoperabilidade C#, WPF, .NET Framework 4.8, NVAPI/Windows | Pasta portátil completa e Inno Setup separado |
| NVDriverForge | C#, WPF, .NET 8; inicialização C++ nativa; Processo 7-Zip | EXE portátil independente e configuração |
| NVMFG Unlock40 | C#/WPF .NET 8, auxiliares da estrutura 4.8, mecanismo C++20/MASM/MinHook | Árvore portátil e configuração |
| NVRasterPulse | Estrutura C#/WPF 4.8; Integração de perfil/recarga RTSS; inicialização nativa | Árvore portátil e configuração |

Este checkout público não pode reconstruir os aplicativos. Os arquivos “Source code” automáticos são instantâneos do hub. Os links de origem upstream não representam a fonte modificada privada exata. O IC público valida apenas este repositório.

<a id="local-checks"></a>
## Verificações locais

Da raiz do repositório:

```text
python tools/validate_repository.py
```

Python 3.10 ou mais recente é suficiente. A verificação lê arquivos, links Markdown locais, avisos necessários/links RTSS, metadados de lançamento e limites de publicação. Ele não executa o software, não instala dependências nem entra em contato com uma rede.

O fluxo de trabalho GitHub executa essa mesma verificação com permissão de conteúdo somente leitura em push, pull request ou envio manual. O checkout está fixado em um commit auditado e não mantém credenciais. Nenhum trabalho de liberação ou implantação está configurado.

<a id="maintain-the-boundary"></a>
## Manter o limite

Atualize a referência em inglês, os guias em francês e as traduções afetadas em conjunto. Mantenha as alterações substantivas separadas das comparações apenas de formatação. Registre hashes de candidatos reais, referências de commit upstream e licenças; nunca deduza uma licença da popularidade de um projeto.

Use ativos de versão com nova versão e audite novamente binários, arquivos e avisos incorporados alterados. Preserve backups privados fora deste repositório. Não use um fluxo de trabalho público para importar fontes de aplicativos privadas ou pastas de compilação locais.

Testes apropriados para uma alteração funcional do aplicativo são executados no projeto privado. Não execute novamente os instaladores de driver nem grave perfis reais para uma atualização de documentação. [Procedimento de liberação manual](releasing.md).
