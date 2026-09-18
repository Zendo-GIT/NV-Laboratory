<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Proveniência, alterações e licenciamento

Esta auditoria descreve os candidatos preparados em **2026-09-18**. As fontes de aplicativos permanecem privadas; os inventários públicos contêm nomes de arquivos e hashes, não código-fonte. Consulte [avisos completos de componentes](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referência: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; versão executável candidata 3.0.2.3. O commit de referência e a versão assembly do fork são identificadores diferentes; nenhuma versão de lançamento upstream é inferida da versão fork.

Os 157 arquivos de origem/recurso do complemento limpo foram comparados com esse commit: 2 bytes idênticos, 134 diferindo apenas em finais de linha ou BOM UTF-8, 11 modificados, 10 ausentes no caminho upstream comparado. “Adicionado” é relativo a esse caminho e não é por si só prova de autoria original.

[Comparação completa de arquivo/hash](../../../provenance/nvpi-source-provenance.json).

| Área | Trabalho herdado | Contribuição Fork |
| --- | --- | --- |
| Editor de perfil | Modelo de perfil, importação/exportação, associações de aplicativos e dados de referência | Integração com Screen e inicializador de ferramentas externo |
| NVAPI | Interoperabilidade DRS do Orbmu2k | Interoperabilidade relacionada a cores/exibição, restrições de carregamento nativo de produção e remoção simulada |
| Exibir serviços | APIs Windows/NVIDIA como interfaces externas | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| IU | Recursos, paletas e ícones upstream do WPF | Diálogos de tela, confirmação de 15 segundos, status/leitura e layout da barra de ferramentas |
| Lançador | Shell de aplicativo existente | Pesquisa e inicialização do RasterPulse instalado separadamente e protegido |
| Embalagem | MIT a montante | Complemento autônomo limpo, instalador/desinstalador separado, avisos retidos |

O mapa de origem pública inclui caminhos de soluções/recursos para rastreabilidade; esses arquivos não são distribuídos como fonte. Testes de desenvolvimento, interfaces simuladas e o antigo binário combinado NVPI/RasterPulse estão excluídos.

<a id="nvdriverforge"></a>
## NVDriverForge

Aplicação C#/.NET 8/WPF independente; o fluxo de trabalho voltado para o usuário é inspirado em parte no NVCleanstall. Nenhuma origem/binário NVCleanstall foi identificada na carga útil de produção. Não é representado como fork desse aplicativo proprietário.

O trabalho original do projeto inclui análise/seleção de componentes, trabalhos de instalação protegidos, backups e recuperação de transações, downloads de catálogo NVIDIA, verificações de atualização, explicações localizadas, fluxos de trabalho avançados/NVENC opcionais e inicialização do instalador.

Componentes herdados/adaptados: quatro paletas de temas NVPI, referência de interface NVAPI DRS estendida e o complemento MIT NVPI opcional separadamente. A UI de seleção da predefinição Custom NV e a integração de transações permitidas pertencem ao NVDriverForge; a predefinição não é uma recomendação oficial do NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 e Inno Setup permanecem componentes externos não modificados usados sob seus próprios termos. keylase Os dados de NVENC não estão incorporados; um commit exato é escolhido e verificado quando o usuário solicita um download compatível. Nenhuma licença de redistribuição foi estabelecida para esses dados upstream.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

O NVMFG Unlock40 foi desenvolvido de forma independente pelo 禅堂 Zendo (RevoluSound Team). O mantenedor usou RTX40MFG-Unlock para comparação e refinamento. O aplicativo como um todo não é apresentado como fork. Esta distinção não remove créditos para componentes compartilhados/adaptados na camada nativa atual.

Referência de comparação: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, commit `4e776d068f91b4a665425542bb005dd57cc3d891`. A árvore privada do mecanismo nativo contém 48 arquivos comparados: 35 diferenças somente de formatação, 4 arquivos modificados e 9 ausentes no caminho de referência. [Comparação completa](../../../provenance/nvmfg-source-provenance.json).

Arquivos herdados modificados: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Caminhos adicionais incluem `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` e uma licença upstream retida.

Unidades de produção C++: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection e vsync_observer; além de montagem entry_detour e buffer/gancho/trampolim MinHook/HDE64. O frontend ReShade herdado, os recursos de shim herdados e os destinos CMake não utilizados não fazem parte desta compilação de produção.

Os componentes correspondentes cobrem a política de patches/provedor e o trabalho temporal; seus avisos de direitos autorais e permissão permanecem intactos. A coordenação central do NGX/bootstrap/controlador, o manuseio do V-Sync por jogo, o diagnóstico de sessão e o fluxo de trabalho do aplicativo Windows/SDK/backup são trabalhos de projeto do 禅堂 Zendo (RevoluSound Team). As contagens acima descrevem arquivos, incluindo arquivos de terceiros e não utilizados, e não uma porcentagem de autoria ou a cronologia da ideia de qualquer projeto.

O auxiliar adapta NvapiDrsWrapper e NativeArrayHelper do NVPI em um conjunto separado, com lógica de perfil de autoria do projeto. O antigo caminho simulado de desenvolvimento foi excluído. As paletas de família compartilhadas são originárias de NVPI.

Referência MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; o subconjunto compilado herdado não possui alterações locais funcionais na comparação. Cabeçalhos de integração Streamline: 2.12; licença de cabeçalho aberto verificada em v2.12.0. Origem do cabeçalho NGX: NVIDIA/DLSS commit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Motor candidato SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Provedor necessário SHA-256 em engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Uma família de provedores 310.9 relatada não é intercambiável com esse hash exato. Nenhuma DLL ou modelo de provedor está incluído.

**Ponto de licenciamento excelente:** a licença completa NVIDIA RTX SDK, versão 14 de março de 2024, contém uma restrição da seção 4(d) relevante para contornar limitações técnicas. A auditoria não estabelece permissão para esse uso. Manter a licença do motor MIT, ser gratuito ou observar outros mods não resolve essa condição separada. A preparação do candidato não é uma autorização legal. O aviso original de cabeçalho curto é complementado com a licença completa; seu texto Windows-1252 também é fornecido como UTF-8 legível, com os bytes originais retidos.

A comparação nativa foi recalculada para 0.2.3: os mesmos 48 arquivos e classificações. Desde a auditoria anterior, `game_selection.cpp`, `game_selection.h` e `patcher.cpp` foram alterados para observações de atividade/capacidade. Os novos fluxos de trabalho de biblioteca, diagnóstico, preferência, atualização e seleção pertencem ao aplicativo mantenedor. As licenças de componentes e o hash do provedor necessário permanecem inalterados.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Gerenciador de perfil independente RTSS desenvolvido no repositório derivado de NVPI. Os recursos/paletas de UI MIT herdados e a origem do projeto permanecem creditados. O aplicativo de produção usa explicitamente a licença MIT fornecida.

Trabalho de projeto: análise/gravação precisa de perfil RTSS e codificação fracionária, backups, remoção de substituição, ponte de recarga, detecção de pré-requisitos, UI compacta, ciclo de vida da bandeja, controles de inicialização e localização. RTSS executa limitação real.

Nenhuma fonte RTSS, DLL de gancho, SDK ou instalador está incluído. A ponte chama a exportação em uma instalação existente do RTSS selecionada pelo usuário. Nenhum pacote de driver NVIDIA, limitador experimental nativo, tempo de execução Framepacer, MinHook, ReShade ou DLSS está neste pacote.

<a id="assets-generated-data-and-tools"></a>
## Ativos, dados gerados e ferramentas

[Créditos de ativos](../assets/README.md) identifica as visualizações de interface existentes e o seletor de configuração NVPI. Os valores fictícios neles são rotulados. Nenhum ativo de jogo/Nexus, perfil pessoal, ICC privado, logotipo corporativo NVIDIA ou arquivo de fonte é copiado.

Os nomes de compatibilidade de jogos gerados herdados no NVMFG são um auxílio à detecção, não uma evidência de teste. Os catálogos do instalador gerados são creditados em [avisos do tradutor](../../../../licenses/INSTALLER-TRANSLATORS.md). Os registros de build gerados com caminhos absolutos permanecem privados.

As ferramentas de compilação privadas incluem scripts de auditoria .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup e Python. Seus compiladores, cabeçalhos, executores de testes e ativos de depuração não são distribuídos. O CRT de versão estática permanece sob os termos aplicáveis ​​do conjunto de ferramentas do Microsoft.

<a id="scope-of-verification"></a>
## Escopo da verificação

A auditoria local inventariau todos os arquivos nas três raízes de desenvolvimento, excluindo bancos de dados de objetos Git e destinos de diretório vinculados. Fontes/documentos ativos foram verificados; construções históricas foram inventariadas e excluídas. ZIPs selecionados e cargas atuais foram verificados e hash; os pacotes .NET foram descompactados para inspeção adicional. Essa auditoria inicial não executou nenhum produto, instalador, jogo, processo RTSS ou driver.

A revisão 2 da configuração NVPI posterior corrige a seleção de idioma independente usando os controles Inno compartilhados e bootstrap. Os equipamentos privados claros/escuros verificaram a navegação do mouse e do teclado e todos os 34 códigos de idioma explícitos. O seletor de configuração real foi aberto em uma área de trabalho privada nunca exibida e cancelado antes da instalação. Seus sete arquivos de aplicativo e ZIP portátil permanecem inalterados. NVDriverForge 0.1.3 inclui o complementar corrigido e ainda encaminha `/LANG`.

NVDriverForge 0.1.3 foi concluído em 10/09/2026. Seu relatório de verificação privado registra 366 testes de aplicativos, 118 verificações complementares, 32 verificações de configuração, 156 comparações nativas e 34 casos de encaminhamento de idioma. A correção de seleção de componente protegido foi reproduzida em um pacote de driver original sem alterar sua carga ou instalar o driver. Estes são resultados desatualizados da equipe de produto, não testes executados novamente por esta atualização de documentação ou prova de uma instalação real de driver bem-sucedida.

Esta atualização do hub não altera nenhum código funcional do aplicativo. Os testes anteriores de construção/unidade/UI de aplicativos permanecem como evidências históricas desatualizadas. Isto não é engenharia reversa completa de todos os binários de terceiros ou uma garantia contra todos os padrões secretos possíveis.

Atualização de 18 de setembro de 2026: NVDriverForge 0.1.4 adiciona verificações de prontidão, backup de perfil nativo, orientação de componentes, preferências e kits, resultados detalhados, relatórios locais e atualizações de aplicativos. NVRasterPulse 0.2 adiciona diagnóstico de configuração, orientação FPS, pausar/retomar, desfazer, perfis `.nvrp` e favoritos/ocultar, sem um novo mecanismo limitador. Guias individuais descrevem o uso e os limites. As verificações estáticas do hub são separadas dos testes de aplicação registrados nos relatórios privados de 18 de setembro; nenhuma instalação de driver, importação de perfil real ou medição de latência foi realizada para este hub.
