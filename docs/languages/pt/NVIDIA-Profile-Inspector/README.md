<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Um fork independente do [NVIDIA Profile Inspector por Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), com controles de exibição adicionais.** Nome do projeto anterior: **NVPI Custom**.

[Status de download e lançamento](../docs/downloads.md#nvidia-profile-inspector) · [Instalação](#installation) · [A montante e mudanças](#upstream-and-changes) · [Licença](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Visão geral

O aplicativo edita os perfis do driver NVIDIA, incluindo configurações por aplicativo. Este fork também adiciona um editor de **Tela** para a exibição ativa do Windows: resolução, taxa de atualização, configurações de cores de saída, HDR e associações de perfil ICC/WCS instaladas.

Ele existe para trazer controles de exibição relacionados ao editor de perfil e tornar os resultados de visualização, confirmação e restauração mais claros. Não estabelece novos recursos de hardware.

O primeiro candidato é **3.0.2.3**, usando a compilação complementar autônoma limpa de 9 de setembro de 2026. Seu executável existente permanece `nvidiaProfileInspector.exe`; o instalador e algumas etiquetas internas ainda dizem `NVPI Custom NV`. O título público acima identifica o fork sem alterar a identidade da instalação ou fingir que é o lançamento oficial do Orbmu2k.

<a id="features"></a>
## Recursos

- Navegação de perfil upstream existente, associações de aplicativos, edições de configuração e importação/exportação de perfil.
- Caixa de diálogo **Tela** para exibição, modo, Hz, RGB/YCbCr, profundidade de cor, faixa e colorimetria.
- Windows Controle HDR e seleção de associação ICC/WCS instalada.
- Uma visualização de exibição de 15 segundos com **Keep** / **Revert** e restauração de tempo limite.
- Leitura de alterações de modo/HDR e falhas de restauração relatadas.
- Relatórios separados de HDR, SDR com ACM/WCG e profundidade de cor do sinal.
- Um iniciador NVRasterPulse para uma cópia elegível instalada separadamente.

<a id="compatibility"></a>
## Compatibilidade

| Requisito | Detalhes |
| --- | --- |
| Sistema | Windows 10/11 x64 com um driver NVIDIA compatível |
| Tempo de execução | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), fornecido por Windows ou instalado separadamente |
| Permissões | O editor solicita acesso de administrador quando aberto |
| Exibições | Os modos reais e as combinações de cores dependem do GPU, driver, monitor, cabo e APIs do Windows |
| Ferramentas opcionais | NVRasterPulse para gerenciamento de limites RTSS; nem ele nem o RTSS são necessários para o editor de tela |
| Idiomas | Configuração: seletor de 34 idiomas. O editor mantém o suporte ao idioma existente. |

Não há um mínimo de driver universal verificado ou matriz de suporte para cada GPU. As opções de bpc disponíveis na caixa de diálogo são solicitações, não combinações certificadas. Os controles HDR modernos e o substituto Windows mais antigo têm recursos diferentes.

<a id="installation"></a>
## Instalação

1. Abra o [página de download](../docs/downloads.md#nvidia-profile-inspector) e verifique o status da publicação.
2. Baixe a configuração ou ativo portátil e compare seu SHA-256 com o manifesto de lançamento.
3. Para configuração, execute `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, selecione um idioma e siga o instalador. Ele cria seu próprio atalho e desinstalador.
4. Para portátil, extraia o ZIP completo para uma nova pasta gravável. Mantenha `Reference.xml`, a configuração do EXE e todos os avisos ao lado do executável.
5. Inicie o `nvidiaProfileInspector.exe`.

Instalar o editor sozinho não aplica um perfil nem instala um driver GPU. O complemento é instalado separadamente, não assume associações `.nip` e não permite a inicialização no login. Os binários existentes não estão assinados.

<a id="usage"></a>
## Uso

**A revisão 2 do instalador** adiciona o mesmo seletor nativo de 34 idiomas que as outras ferramentas, com navegação por mouse/teclado, aparência claro/escuro e cancelamento. A escolha se aplica à configuração; não traduz o editor NVPI. Um argumento `/LANG=fr` explícito ou modo silencioso ignora a seleção para chamadores que já fornecem um idioma.

**Perfis de motorista:** selecione um perfil, exporte um backup, edite apenas as configurações pretendidas e aplique-as. As associações de aplicativos determinam qual jogo recebe um perfil. Um valor armazenado não é prova de que todos os drivers ou jogos o utilizam.

**Controles de exibição:** abra a **Tela**, escolha a exibição e os valores solicitados e inicie a visualização. Verifique a imagem antes de escolher **Manter** em 15 segundos. Use **Reverter**, feche a confirmação ou deixe-a expirar para solicitar a restauração. Leia qualquer mensagem de falha: uma chamada de API bem-sucedida por si só não é prova de restauração.

Uma seleção ICC altera uma associação de perfil instalada; ele não gera, calibra ou redistribui um arquivo ICC. HDR, ACM/WCG, RGB/YCbCr e bpc descrevem diferentes aspectos do pipeline. Nenhum novo switch ACM independente é fornecido.

**NVRasterPulse:** o botão da barra de ferramentas aceita uma instalação registrada separadamente em todo o sistema abaixo de Arquivos de Programas com propriedade e permissões protegidas. Uma cópia portátil ou um caminho gravável/vinculado pelo usuário pode ser recusado por este iniciador elevado. Nesse caso, abra NVRasterPulse usando seu próprio atalho. [Instale o RTSS separadamente](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) para usar NVRasterPulse.

<a id="screenshots"></a>
## Capturas de tela

![Seletor de idioma da revisão 2 da configuração NVPI](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Seletor de configuração real em francês, capturado durante um teste isolado e depois cancelado. Isso mostra o instalador; o editor mantém sua interface e diálogo de tela.

<a id="update-and-uninstall"></a>
## Atualizar e desinstalar

Feche o editor antes de atualizar. Mantenha os perfis exportados e baixe o novo Release fork; instale com a mesma identidade complementar ou extraia arquivos portáteis para uma nova pasta. Não misture um `Reference.xml` antigo com um novo executável. A supressão de verificação de atualização upstream incluída pertence a este fork.

Para uma cópia instalada, use Windows **Installed apps** e seu desinstalador. Para portátil, feche-o e remova a pasta extraída quando suas exportações estiverem seguras. A remoção do editor **não** desfaz edições de perfil do motorista, preferências de exibição, NVRasterPulse ou RTSS. Restaure as configurações desejadas antes da remoção.

<a id="known-limitations"></a>
## Limitações conhecidas

- A confirmação de 15 segundos não é um alerta para cada falha de driver, perda de energia ou desligamento forçado.
- Algumas combinações de cor/profundidade/atualização retornam `NVAPI_NOT_SUPPORTED`.
- A leitura de software não mede a profundidade de bits do painel, a precisão das cores ou a latência.
- As configurações da tela afetam a exibição atual do Windows; esta caixa de diálogo não cria predefinições de exibição por jogo.
- Nenhuma garantia de desempenho, anti-cheat ou compatibilidade universal com HDR.

<a id="troubleshooting"></a>
## Solução de problemas

| Sintoma | Ação |
| --- | --- |
| Erro de tempo de execução na inicialização | Verifique as atualizações do Windows e do .NET Framework 4.8; use o pacote completo. |
| Modo de exibição solicitado rejeitado | Reverta e teste um modo oferecido por Windows/NVIDIA para esse monitor. Leia o erro exato e evite alterações cegas repetidas. |
| HDR ou a cor retorna ao estado antigo | Verifique se outra operação falhou e acionou a restauração; distinguir HDR de ACM. |
| O botão NVRasterPulse recusa um caminho | Inicie seu próprio atalho; este botão requer uma instalação protegida em todo o sistema. |
| Uma alteração permanece após a desinstalação | Restaure o perfil NVIDIA exportado ou as configurações de exibição pretendidas do Windows; desinstalar não é uma reversão de configurações. |

Consulte [orientação de suporte compartilhada](../docs/support.md) antes de enviar logs.

<a id="faq"></a>
## Perguntas frequentes

**Este é o software NVIDIA oficial ou a versão oficial do Orbmu2k?** Não. É um fork independente; o autor upstream e a licença MIT permanecem creditados.

**O NVDriverForge requer este editor?** Não. A predefinição Custom NV opcional do NVDriverForge usa sua própria integração. Instalar o editor é uma escolha separada.

**O RTSS é obrigatório para este fork?** Não. O RTSS é obrigatório para o limitador FPS do NVRasterPulse, não para edição de perfil ou tela.

**Onde está a fonte?** A fonte do aplicativo modificado é mantida de forma privada. O aviso MIT e o repositório upstream são fornecidos; MIT não requer publicação de fonte modificada.

<a id="upstream-and-changes"></a>
## A montante e mudanças

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), confirmação de referência `592d962cca8827efe8859461a84267755595064a`. [Downloads originais](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Herdado: editor de perfil, interoperabilidade NVAPI, dados de referência, recursos de UI e temas. 禅堂 Zendo (RevoluSound Team) adicionou ou adaptou serviços de exibição, transações HDR/ICC, confirmação/leitura de 15 segundos, layout da barra de ferramentas e comportamento de inicialização do RasterPulse. O complemento limpo exclui simulações de desenvolvimento/pontos de entrada de teste, usa um iniciador externo protegido e fornece um instalador separado. O antigo pacote de desenvolvimento combinado NVPI/RasterPulse não é o candidato neste hub.

[Proveniência detalhada do arquivo](../docs/provenance.md) · [Aviso fork original](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Créditos e licença

Direitos autorais (c) 2016 Orbmu2k. O [Licença MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) fornecido é mantido. Adaptações e embalagens: 禅堂 Zendo (RevoluSound Team). O instalador usa Inno Setup; Windows e .NET Framework permanecem externos. [Avisos aplicáveis completos](LICENSES/README.md).

Independente, não patrocinado e não endossado oficialmente por NVIDIA Corporation. As marcas registradas permanecem com seus respectivos proprietários.
