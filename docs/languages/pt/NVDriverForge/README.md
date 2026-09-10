<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Prepare uma instalação do driver NVIDIA com opções claras de componentes e configurações opcionais.**

[Baixe 0.1.3 e status](../docs/downloads.md#nvdriverforge) · [Instalação](#installation) · [Créditos](#credits-and-upstream) · [Licença](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Visão geral e propósito

NVDriverForge orienta você através de um pacote de driver NVIDIA original: escolha o driver, inspecione seus componentes, revise os ajustes opcionais e confirme a instalação. Ele existe para tornar essas escolhas compreensíveis e manter unidas a instalação, as operações privilegiadas e as informações de recuperação.

É um aplicativo desenvolvido de forma independente, inspirado em parte no fluxo de trabalho do NVCleanstall. Ele não inclui NVCleanstall nem reivindica paridade completa de recursos.

<a id="features"></a>
## Recursos

- Pesquisa e downloads de NVIDIA Game Ready / Studio; descoberta de hotfix opcional com fallback manual.
- Análise do pacote original, hashes, assinaturas NVIDIA, manifestos e entradas INF compatíveis.
- Seleção de componentes com dependências e preservação de componentes desconhecidos.
- A versão 0.1.3 mantém os componentes NVIDIA opcionais selecionados ignoráveis e exclui apenas componentes não verificados verificados da descoberta. Os tempos de execução opcionais já atuais ou inaplicáveis ​​não são mais forçados como componentes críticos.
- Resumos claros de falhas de instalação e acesso a registros detalhados em todos os 34 idiomas.
- Confirmação explícita de instalação, teste protegido e exportação de pacotes de armazenamento de driver existentes.
- Configurações avançadas opcionais, com verificações de simulação, diários e recuperação com reconhecimento de conflitos.
- Predefinição opcional **Custom NV** com opções nomeadas e explicações, incluindo uma seleção de resistência SILK separada e verificações de compatibilidade.
- Downloads opcionais de patch NVENC de versão exata; commit de origem e bytes de destino são verificados.
- Uma instalação separada e opcional do Profile Inspector fork na tela Ferramentas.
- Verificações opcionais de atualização do usuário instalado, 34 idiomas de interface e quatro temas.

As opções avançadas disponíveis dizem respeito a MPO, o indicador DLSS, Ansel, suspensão de áudio NVIDIA, MSI, política/prioridade de interrupção, HDCP, inicialização de contêiner de exibição e um serviço de telemetria legado elegível. Cada um tem os seus próprios pré-requisitos e efeitos; essas não são melhorias universais de desempenho.

<a id="compatibility"></a>
## Compatibilidade

| Requisito | Detalhes |
| --- | --- |
| Sistema | Windows 10 versão 19041 ou mais recente / Windows 11, x64 |
| GPU/driver | Pacote NVIDIA compatível e hardware detectado; a pesquisa automática de catálogo cobre principalmente modelos GeForce conhecidos |
| Tempo de execução | .NET 8 / WPF 8.0.31 incluído no pacote independente preparado |
| Privilégios | Configuração normal da UI/por usuário; instalação de driver e alterações no sistema solicitam acesso de administrador |
| Rede | Obrigatório para pesquisas/downloads on-line de NVIDIA e solicitações upstream explícitas de NVENC; um driver original local pode ser selecionado |
| Ferramentas incluídas | 7-Zip 26.03 não modificado, avisos de tempo de execução, complemento opcional MIT Profile Inspector |
| Companheiro opcional | .NET Framework 4.8 para o Profile Inspector fork separado |

Nenhuma versão mínima arbitrária do driver cobre todos os recursos. A pesquisa Multi-GPU deve corresponder a cada GPU detectado. Modelos não suportados/profissionais podem exigir a seleção manual do driver. O instalador do NVIDIA continua sendo a autoridade final de hardware/sistema operacional.

<a id="installation"></a>
## Instalação

1. Visite [downloads](../docs/downloads.md#nvdriverforge) e confirme se o lançamento foi publicado.
2. Escolha `NVDriverForge-Setup.exe` para instalação ou `NVDriverForge.exe` para uso portátil.
3. Compare o SHA-256 com o `SHA256SUMS.txt` da versão.
4. Execute a Instalação para uma instalação por usuário e um desinstalador padrão ou coloque o EXE portátil em uma pasta gravável e abra-o.

O portátil inclui seu tempo de execução e seu instalador opcional. A instalação do NVDriverForge não instala um driver GPU. Seus EXEs não estão assinados no momento.

<a id="usage"></a>
## Uso

1. **Driver:** baixe do NVIDIA ou selecione um EXE instalador original do NVIDIA. Deixe a análise terminar.
2. **Componentes:** revise as descrições e as dependências necessárias. Componentes desconhecidos são retidos.
3. **Ajustes:** deixe as opções indesejadas inalteradas. Leia os efeitos e compensações antes de selecionar qualquer coisa.
4. **Revisão:** verifique o driver exato, os componentes e as operações opcionais e, em seguida, confirme a instalação.
5. Aceite UAC apenas para a operação escolhida. Guarde as instruções de recuperação do trabalho protegido.
6. Se o novo driver precisar ser reiniciado, siga o estado relatado. As operações adiadas exigem retomada explícita após a reinicialização.

Custom NV inicia inalterado. Escolha valores nomeados individuais ou revise a predefinição fornecida e suas exclusões. Seus dois campos informativos internos não são escritos de forma independente. As configurações são aplicadas somente no fluxo de trabalho de novo driver verificado, nunca abrindo uma visualização. A instalação do editor NVPI separado não é necessária.

O trabalho NVENC opcional baixa dados compatíveis de um commit keylase fixado. Altera duas DLLs de driver e invalida suas assinaturas; pode ser recusado por Windows, codificadores, DRM ou anti-cheat. Nenhum desses dados ou DLL NVIDIA está incorporado em NVDriverForge. [Limites de proveniência e licenciamento](../docs/provenance.md).

As preferências controlam o idioma, o tema e verificações opcionais de atualização do usuário instalado. O portátil não cria a tarefa de verificação de antecedentes instalada. As ferramentas e a recuperação são separadas das quatro etapas de instalação.

<a id="screenshots"></a>
## Capturas de tela

![Visualização da página do driver NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Renderização da UI francesa 0.1.2 existente com dados de exemplo; retido como uma visualização da interface. O driver 699.99 exibido é um acessório de teste, não uma versão real para download. [Proveniência da imagem](../assets/README.md).

<a id="update-and-uninstall"></a>
## Atualizar e desinstalar

Feche o NVDriverForge, obtenha o próximo pacote oficial e verifique seu hash. Use a mesma identidade de configuração para uma atualização instalada; substitua um EXE portátil fechado por um novo. Mantenha configurações e trabalhos protegidos.

Uninstall de Windows **Installed apps**. Ele remove o aplicativo e sua tarefa de atualização, não o driver NVIDIA. Configurações, registros e backups permanecem. Se desejar, restaure as alterações avançadas/NVENC por meio do fluxo de recuperação documentado **antes** de remover o aplicativo. Restaurar recusa alterações conflitantes de outra ferramenta.

Os dados locais estão sob `%LOCALAPPDATA%\NVDriverForge`; trabalhos protegidos e exportações de driver estão sob `%PROGRAMDATA%\NVDriverForge\Jobs`. O uso portátil também cria dados locais. Uma exportação de armazenamento de driver não é uma imagem do sistema ou um backup completo do perfil.

<a id="known-limitations"></a>
## Limitações conhecidas

- Sem adições de hardware/edição INF, assinaturas NVIDIA regeneradas, renúncia compatível com anti-cheat ou aceitação automática de aviso não assinado.
- Sem remoção completa de telemetria/publicidade, exportação de pacotes finos ou reversão completa automática para o driver anterior.
- A instalação do driver, a recuperação de inicialização e as gravações de perfis opcionais não foram validadas de forma abrangente em máquinas reais pela auditoria do hub.
- A leitura do registro não é prova de efeitos reais do HDCP, de desempenho ou de latência.
- As verificações de assinatura usam confiança Windows disponível localmente; a revogação online não é executada.
- Estão presentes 34 idiomas, mas os testes completos de falantes nativos/acessibilidade permanecem incompletos.

<a id="troubleshooting"></a>
## Solução de problemas

| Sintoma | Ação |
| --- | --- |
| Catálogo on-line indisponível | Selecione um pacote original de [Baixar drivers NVIDIA](https://www.nvidia.com/en-us/drivers/). Não substitua um modelo GPU vizinho. |
| Pesquisa de hotfix indisponível | Use [Fórum de drivers Game Ready do NVIDIA](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) e verifique o pacote real. |
| A instalação do NVIDIA falha | Leia o resumo da falha e abra os logs detalhados. Componentes opcionais já atuais ou inaplicáveis ​​permanecem ignoráveis ​​no 0.1.3. Instalações com falha não acionam ajustes opcionais ou um fluxo de sucesso/reinicialização. |
| Falha de assinatura/hash/backup | Pare essa instalação e retenha o erro; obtenha o pacote original novamente se estiver corrompido. |
| Opção indisponível | Leia o motivo do hardware, componente ou driver de destino; mantenha-o inalterado. |
| Reiniciar ou trabalho ainda pendente | Use as instruções de recuperação do trabalho e currículo explícito; não apague seu diário. |
| Restaurar conflito | Outro estado difere da transação registrada. Preserve-o e peça ajuda em vez de forçar uma restauração. |

Para relatórios, inclua a versão da ferramenta selecionada, Windows, GPU, driver e etapas reproduzíveis; redigir caminhos e detalhes pessoais dos registros. [Suporte](../docs/support.md).

<a id="faq"></a>
## Perguntas frequentes

**A Instalação instala um driver gráfico?** Não. Isso requer análise separada, revisão, confirmação e processo de instalação elevado do aplicativo.

**Preciso de NVCleanstall ou NVPI?** Não. NVCleanstall é apenas inspiração. O companheiro Profile Inspector é um editor opcional independente.

**Isso torna cada driver NVIDIA menor ou mais rápido?** Não. Os componentes e pré-requisitos selecionados determinam o que pode mudar; nenhum ganho medido é prometido.

**Onde estão as fontes?** A fonte específica do aplicativo e os testes privados são mantidos separadamente. Este hub fornece documentação, binários e links de fontes de terceiros necessários para atribuição/licenciamento.

<a id="credits-and-upstream"></a>
## Créditos e upstream

Aplicação original, fluxo de trabalho, transações, localização, bootstrap e adaptações: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspiração de fluxo de trabalho; nenhuma fonte ou binário importado.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): temas MIT, referência de interface NVAPI estendida e fork empacotado separadamente.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): ferramentas de extração não modificadas.
- [Microsoft.NET](https://github.com/dotnet/runtime) e [WPF](https://github.com/dotnet/wpf): tempo de execução empacotado.
- [Inno Setup](https://jrsoftware.org/isinfo.php): mecanismo instalador original e traduções creditadas.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): fonte de dados externa opcional NVENC; licença de redistribuição não estabelecida.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): downloads de drivers externos e bibliotecas NVAPI/NVML instaladas.

[Tabela completa de componentes](../THIRD_PARTY_NOTICES.md) · [Mudanças e proveniência](../docs/provenance.md)

<a id="license"></a>
## Licença

[Permissão de distribuição binária existente](../../../../NVDriverForge/LICENSE) permite o uso e compartilhamento de executáveis oficiais não modificados com seus avisos. Os direitos de origem específicos do aplicativo são reservados. Ela não restringe os direitos concedidos pelas licenças separadas de terceiros. [Avisos completos](LICENSES/README.md).

Independente de NVIDIA Corporation, TechPowerUp e keylase; não patrocinado ou endossado oficialmente por eles. Os nomes dos produtos permanecem marcas registradas de seus proprietários.
