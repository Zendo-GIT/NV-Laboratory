<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**NVIDIA Multi Frame Generation experimental para GeForce RTX 40, com um controlador central e opções por jogo.**

[Baixe 0.2.3 e status](../docs/downloads.md#nvmfg-unlock40) · [Instalação](#installation) · [A montante](#upstream-and-modifications) · [Licenças](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Visão geral e propósito

NVMFG Unlock40 é um aplicativo desenvolvido de forma independente pela 禅堂 Zendo (RevoluSound Team). Ele combina um controlador Windows, uma camada nativa, um auxiliar de perfil e gerenciamento de jogo/Streamline SDK. Destina-se a jogos que já integram NVIDIA DLSS Frame Generation e tempos de execução NVIDIA compatíveis.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) foi consultado para comparar e refinar o trabalho. A camada nativa atual contém componentes compartilhados e adaptados, creditados individualmente abaixo. Esta referência não torna todo o aplicativo NVMFG um fork desse projeto.

Ele existe para coordenar centralmente o comportamento experimental do MFG, lembrar escolhas específicas do jogo e manter visíveis as atualizações e backups do tempo de execução. Ele não adiciona DLSS Frame Generation a todos os jogos nem converte uma implementação arbitrária de FSR.

O pacote atual é **0.2.3**. Ele adiciona uma biblioteca de jogos persistente, informações de atividade e capacidade, diagnóstico local e comportamento de seleção/progresso corrigido. [Transferências](../docs/downloads.md#nvmfg-unlock40) identifica os arquivos e hashes exatos.

<a id="features"></a>
## Recursos

- Controle central de ativação/desativação e inicialização opcional da bandeja Windows.
- Seleção por jogo entre Dynamic MFG, a configuração do jogo e multiplicadores fixos suportados.
- Escolhas memorizadas separadas para estados ativados/desativados observados do V-Sync.
- Dynamic usa o modo NVIDIA; ele é suspenso quando V-Sync está desligado, com uma escolha separada no jogo/fixa.
- Orientação do menu do jogo e exclusões persistentes; jogos sem DLSS FG permanecem no controle.
- Descoberta de jogos, seleção de pasta pai, pesquisa, agrupamento e remoção sem excluir arquivos de jogo.
- Streamline Download/importação SDK, cache local verificado, seleção explícita, backup e restauração por jogo.
- Verificação de provedor nativo, diagnóstico por sessão, diário de perfil global e recuperação com reconhecimento de conflito.
- 34 idiomas de interface e quatro temas.

Desligar o FG no jogo o mantém desligado. As escolhas fixas de 2x a 6x dependem do jogo/menu/tempo de execução; eles não são uma promessa de que todas as combinações funcionam. O controlador observa V-Sync e não configura V-Sync ou VRR para o usuário.

<a id="compatibility"></a>
## Compatibilidade

| Requisito | Detalhes |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| GPU | GeForce RTX 40 alvo; nenhuma reivindicação de compatibilidade universal GPU |
| Jogo | Integração NVIDIA DLSS Frame Generation existente e tempo de execução suportado; sem certificação de compatibilidade anti-cheat |
| Provedor | O candidato está fixado no provedor SHA-256 documentado em [proveniência](../docs/provenance.md); hashes desconhecidos são recusados |
| Tempo de execução | Pacote .NET 8/WPF 8.0.30 para aplicativo/agente; .NET Framework 4.8 para auxiliares de perfil |
| Permissões | Acesso de administrador para operações de controlador/perfil |
| Rede | Obrigatório para downloads oficiais selecionados do SDK; SDKs compatível importado pode ser armazenado em cache localmente |
| Binários externos | Driver NVIDIA, provedor/modelos NGX e tempos de execução de jogos Streamline não estão incluídos |

Um rótulo de versão por si só é insuficiente: driver, hash do provedor, integração do jogo e módulos realmente carregados são importantes. Processos protegidos ou incompatíveis podem recusar a anexação. O aplicativo não foi projetado para escapar das proteções anti-cheat.

<a id="installation"></a>
## Instalação

1. Leia o [status de candidato e nota de licenciamento](../docs/downloads.md#nvmfg-unlock40).
2. Baixe `NVMFGUnlock40-0.2.3-Setup-x64.exe` ou `NVMFGUnlock40-0.2.3-Portable-x64.zip` quando seu lançamento estiver disponível.
3. Verifique SHA-256 e guarde os avisos que o acompanham. Instale o .NET Framework 4.8 se o Windows ainda não o fornecer.
4. Execute a Instalação ou extraia o ZIP portátil **inteiro** para uma pasta local gravável.
5. Inicie o `NVMFGUnlock40.exe`; mantenha `agent`, `driver`, `engine` e `Licenses` no layout fornecido.

A pasta chamada `driver` contém auxiliares de espaço do usuário, não um driver de kernel. Não copie apenas o EXE principal nem substitua o hash do provedor para forçar a compatibilidade. Os EXEs atuais não estão assinados.

<a id="usage"></a>
## Uso

1. Comece com o controlador desabilitado. Adicione um jogo ou pasta pai e escolha as instalações reais.
2. Revise as configurações MFG de cada jogo. Responda o que seu cardápio oferece; a resposta é armazenada por jogo.
3. Escolha Dynamic ou a configuração do jogo globalmente e ajuste as opções elegíveis por jogo conforme necessário.
4. Habilite o controlador somente quando pretender usá-lo. Ele pode alterar temporariamente seis configurações globais do perfil NVIDIA, com um diário de recuperação.
5. Inicie um jogo elegível e ative seu próprio DLSS Frame Generation. Siga qualquer solicitação para a escolha V-Sync-off.
6. Use exclusões para jogos que você não deseja gerenciar. A remoção de um jogo registra uma exclusão e preserva seus arquivos/backups.
7. Use o fluxo completo de encerramento/desativação e recuperação do aplicativo quando terminar.

Fechar a janela principal pode deixar o controlador na bandeja. Uma DLL já carregada em um jogo permanece lá até o jogo terminar; desabilitar o controlador não é uma garantia de descarga. Feche os jogos afetados antes da manutenção ou atualizações.

**Streamline SDKs:** na página NVIDIA SDK, baixe uma versão oficial ou importe um SDK local compatível. A importação armazena uma cópia verificada; **Use this version** seleciona-o e **Uninstall** remove essa cópia em cache. DLLs Streamline ausentes podem ser complementadas a partir de um NVIDIA SDK oficial, com a fonte mostrada. Isso não baixa/substitui um modelo NGX. Feche o jogo, selecione a atualização pretendida e mantenha o backup original. Para reverter os arquivos do jogo, use a restauração do backup, não o botão Uninstall do cache.

<a id="library-diagnostics-and-updates"></a>
## Biblioteca, diagnósticos e atualizações

**Biblioteca persistente:** selecione várias pastas do jogo, incluindo unidades diferentes, antes de iniciar uma verificação. O progresso é visível e o cancelamento está disponível. Após a primeira verificação, um cache local restaura a biblioteca na inicialização sem percorrer todas as pastas do jogo. Atualize para encontrar alterações ou adicione outra pasta. As operações de manutenção ainda revalidam os arquivos afetados; o monitoramento de backup permanece ativo. O cache é armazenado em `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Seleção:** Ctrl+A seleciona todos e Ctrl+D limpa a guia Jogos ou Backups ativos. Nenhum jogo é selecionado automaticamente. Atualizações e atualizações de atividades não criam mais seleções fantasmas ou contagens inconsistentes.

**Atividade e compatibilidade:** as informações do MFG por jogo vêm de observações do NGX sem uma nova sobreposição. Não é uma contagem física dos quadros exibidos. O suporte Dynamic com V-Sync vem de recursos de tempo de execução; capacidade desconhecida não é inferida de um número de versão. O aplicativo não altera V-Sync nem VRR. Com o V-Sync desligado, o Dynamic permanece suspenso; as escolhas fixas ou controladas pelo jogo são separadas.

**Próximo lançamento:** a exclusão temporária ignora a correção no próximo lançamento do jogo e restaura o gerenciamento normal após sua saída. Não é possível remover uma DLL já carregada em um jogo: feche e reinicie o jogo. Wallpaper Engine é reconhecido como um aplicativo de desktop; esta correção preserva a proteção para jogos realmente ignorados.

**Preferências e suporte:** a importação/exportação de preferências requer a reassociação manual das pastas do jogo. O diagnóstico local em Sobre filtra informações privadas e relata códigos de erro NVAPI ou categorias de conflito disponíveis. Revise-o antes de compartilhar; nada é carregado automaticamente.

**Atualizações de aplicativos:** uma verificação opcional exibe notas de versão e oferece a configuração oficial. O download explícito é verificado em relação ao tamanho GitHub e aos metadados SHA-256; você mesmo inicia a instalação. A versão 0.2.3 também limpa mensagens de progresso concluídas, preservando erros e resultados significativos. Essas adições incluem as alterações desde a versão pública 0.1.1.

<a id="screenshots"></a>
## Capturas de tela

![Visualização da lista NVMFG SDK](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

A interface 0.1.1 em inglês existente é renderizada com um exemplo de inventário SDK. Não é uma lista de versões atuais ou evidência de um jogo em execução. [Proveniência da imagem](../assets/README.md).

<a id="update-and-uninstall"></a>
## Atualizar e desinstalar

Feche os jogos afetados. Desative/encerre o NVMFG e resolva qualquer recuperação de configurações pendente do NVIDIA antes de atualizar. Instale o próximo Setup com a identidade existente ou extraia o novo portátil para uma nova pasta; reter estado/backups.

Antes de desinstalar, restaure os backups do jogo desejado SDK e as configurações do NVIDIA por meio do aplicativo, feche os jogos e saia do controlador. Use Windows **Installed apps** para configuração ou remova a pasta portátil fechada após preservar os arquivos necessários. Não exclua manualmente um diário de recuperação ativo para desbloquear a Instalação.

Os backups locais de tempo de execução do jogo usam `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Configurações MFG/dados SDK usam `%LOCALAPPDATA%\RtxMfg`; a saída da sessão está em `Sessions` ao lado do aplicativo. Esses arquivos podem conter caminhos de jogos. Não os publique sem edição.

<a id="known-limitations"></a>
## Limitações conhecidas

- Um bloqueio de ativação/restauração/desinstalação 0.1.1 relatado permanece não reproduzido e sua causa é desconhecida. Esta versão não pretende corrigi-lo. Após uma falha, preserve o diário de recuperação e inspecione o diagnóstico local; não force a exclusão dos dados de recuperação.
- Patches nativos experimentais podem causar travamentos ou artefatos visuais; uma falha não resolvida do Bodycam é registrada no histórico de desenvolvimento.
- Os testes de renderização controlada não são certificação para todos os jogos, drivers ou anti-cheat.
- Os quadros gerados não criam novas amostras de entrada; nenhuma latência medida ou ganho de desempenho é prometido por este hub.
- Várias ferramentas/sobreposições de geração de quadros podem entrar em conflito. A aplicação reporta módulos observados sem comprovar todos os cenários de coexistência.
- O manifesto de compatibilidade é um auxílio à detecção, não uma lista de jogos totalmente testados.
- Os termos completos do NVIDIA SDK e a restrição de limitação técnica não resolvida permanecem documentados em [proveniência](../docs/provenance.md).

<a id="troubleshooting"></a>
## Solução de problemas

| Sintoma | Ação |
| --- | --- |
| Provedor não suportado | Mantenha os arquivos originais verificados. Relate as versões do driver/provedor e o erro; não ignore a verificação de hash. |
| Não há DLSS FG no jogo | Selecione essa resposta e deixe o jogo no controle; esta ferramenta não pode fabricar essa integração. |
| Falhas/artefatos do jogo | Saia do jogo, desative o NVMFG, use o backup de tempo de execução original do jogo, se ele tiver sido alterado, e relate detalhes reproduzíveis. |
| Lista SDK ou download indisponível | Atualize e verifique a fonte oficial; uma versão em cache/importada ainda deve passar na validação. |
| A recuperação pendente do NVIDIA bloqueia a saída/atualização | Use recuperação e preserve o diário; os conflitos não devem ser substituídos cegamente. |
| Um jogo removido não é redescoberto | Sua exclusão é persistente. Adicione-o explicitamente quando quiser gerenciá-lo novamente. |

[Orientação de suporte compartilhada](../docs/support.md) explica o que incluir em um relatório.

<a id="faq"></a>
## Perguntas frequentes

**Inclui DLLs ou modelos NVIDIA?** Nenhum driver, provedor/modelo NGX ou tempo de execução Streamline está incluído. Os downloads explícitos do SDK vêm do NVIDIA.

**O Dynamic funciona com o V-Sync desligado?** Ele está suspenso nesse estado. Escolha a configuração do jogo ou um multiplicador fixo elegível para o estado separado desse jogo.

**Este é um pacote ReShade/OptiScaler/FSR?** Não. Eles não são compilados ou enviados como parte deste pacote de produção.

**As fontes modificadas são públicas?** Não. Pacotes compilados e créditos/licenças necessários são fornecidos. Isto não remove direitos ou restrições de terceiros.

<a id="upstream-and-modifications"></a>
## Upstream e modificações

Referência de comparação e componentes nativos compartilhados: **RTX40MFG-Unlock por Michael Robles / dashdogy**, confirmação de referência `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Repositório](https://github.com/dashdogy/RTX40MFG-Unlock) · [Downloads originais](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

A comparação de origem identifica patches compartilhados, tratamento de provedor/política, correções temporais e componentes de desvio baseados em MinHook. Seus avisos MIT e BSD são mantidos. A comparação completa também inclui arquivos fora do destino de produção.

O aplicativo de desktop, o controlador e o fluxo de trabalho de gerenciamento do SDK são desenvolvidos pela 禅堂 Zendo (RevoluSound Team). O trabalho do projeto inclui carregamento central, integração de bootstrap NGX, seleção verificada de provedor, coordenação de jogo/V-Sync e diagnóstico de sessão. O guia de proveniência separa esse trabalho dos componentes compartilhados; uma comparação de arquivos por si só não estabelece quando um dos autores teve a ideia.

O auxiliar de perfil adapta o wrapper MIT NVAPI do Profile Inspector do Orbmu2k. [Procedência detalhada e escopo do componente](../docs/provenance.md).

<a id="credits-and-license"></a>
## Créditos e licença

Michael Robles; Orbmu2k; Contribuidores Tsuda Kageyu e HDE; NVIDIA Corporation; Microsoft e colaboradores; Autores e tradutores Inno Setup. Desenvolvimento de aplicativos, integrações e empacotamento: 禅堂 Zendo (RevoluSound Team).

O [permissão de compartilhamento de pacote compilado existente](../../../../NVMFG-Unlock40/LICENSE) e todos os [licenças de componentes](LICENSES/README.md) são preservados. As permissões MIT para código upstream são distintas dos termos NVIDIA SDK. Nenhuma licença geral os substitui.

Independente, não patrocinado e não endossado oficialmente por NVIDIA Corporation. Todas as marcas registradas mencionadas permanecem propriedade de seus proprietários.
