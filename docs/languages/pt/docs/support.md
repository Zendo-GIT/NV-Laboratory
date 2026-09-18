<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Compatibilidade e solução de problemas

Estes são os candidatos preparados, não uma matriz de certificação para todas as combinações de Windows, GPU, driver e jogo.

| Ferramenta | Windows/tempo de execução | Dependência de hardware/externa | Operações que necessitam de cuidados |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Driver/tela NVIDIA compatível | Gravações de perfil e visualizações de exibição |
| NVDriverForge 0.1.4 | Windows 10 compilação 19041+/11 x64; .NET/WPF incluído | Pacote de driver NVIDIA compatível | Instalação elevada, configurações avançadas, NVENC opcional |
| NVMFG Unlock40 0.2.3 | Windows 10/11x64; .NET/WPF incluído, auxiliares Framework 4.8 | RTX 40, jogo DLSS FG qualificado e provedor fixado | Patches nativos no jogo, diário de perfil global, atualizações de jogos SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS instalado; concorrendo aos bonés | Alterações de perfil por executável RTSS |

Nenhum pacote ARM64 está preparado. A disponibilidade de exibição/API e versões antigas do Windows podem limitar recursos individuais. Nenhuma versão mínima universal NVIDIA ou RTSS foi inventada. O hash exato do provedor NVMFG está em [proveniência](provenance.md).

<a id="before-reporting-a-bug"></a>
## Antes de relatar um bug

Identifique o executável/versão exato que você abriu. Uma cópia instalada anteriormente não é necessariamente a versão de um ZIP recém-baixado. Registre as etapas de reprodução, resultado esperado e resultado real. Para problemas de renderização/limitação, inclua versão do jogo, atualização de exibição, estado FG/V-Sync/VRR e qualquer outro limitador ou sobreposição.

Utilize o [formulário de bug](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Nunca anexe uma pasta de desenvolvimento privada inteira, arquivo de driver, modelo, DLL de jogo, despejo de registro ou coleção de log não revisada.

| Problema | Primeiras verificações |
| --- | --- |
| Versão errada do aplicativo | Confirme a identidade do EXE e libere o hash; feche a cópia antiga antes da substituição. |
| Erro de tempo de execução/inicialização | Instale o Framework 4.8 necessário ou mantenha todas as subpastas portáteis fornecidas. |
| UAC cancelado | Tente novamente apenas a operação pretendida; o cancelamento não é uma instalação bem-sucedida. |
| Incompatibilidade de hash/assinatura | Pare de usar esse candidato e obtenha os bytes oficiais esperados. |
| Cor/modo NVPI rejeitado | Reverta e use uma combinação suportada pelo monitor/driver real. |
| Falha de backup ou recuperação NVDF | Preservar trabalho protegido e RECOVERY.txt; não apague o diário nem force gravações conflitantes. |
| Configurações pendentes do NVMFG | Resolva a recuperação com jogos fechados, preservando alterações de outras ferramentas. |
| O limite RP não tem efeito | Execute RTSS, identifique o EXE do jogo real, inspecione o estado do gancho e os limites concorrentes. |
| A tampa RP persiste após a remoção | Inspecione RTSS Global; a remoção altera apenas as substituições do limitador local. |

NVDriverForge oferece um relatório JSON local previsível; NVMFG oferece um diagnóstico em Sobre. Prefira esses relatórios filtrados a um arquivo de log completo e inspecione-os antes de compartilhar. Um bloqueio de restauração relatado no NVMFG 0.1.1 ainda não tem causa estabelecida; preserve seu diário e registre qualquer código de erro disponível. NVRasterPulse O 0.2 oferece diagnóstico de configuração em seu menu de ações, sem medir o FPS.

<a id="logs-and-privacy"></a>
## Registros e privacidade

| Ferramenta | Dados locais para revisar, não fazer upload no atacado |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; trabalhos protegidos `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; backups `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` ao lado do EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` abaixo dele |
| NVPI | Suas exportações escolhidas e o erro exibido; nenhum caminho de log universal inventado |

Remova nomes de contas, diretórios iniciais, caminhos de bibliotecas de jogos, identificadores de dispositivos, tokens e janelas não relacionadas dos textos/imagens que você compartilha. Mantenha os originais em sigilo para recuperação. Os problemas públicos são visíveis para todos.

Para uma vulnerabilidade, comportamento privilegiado perigoso ou operação destrutiva não intencional, siga [SECURITY.md](../SECURITY.md) em vez de publicar detalhes publicamente.

<a id="what-has-been-verified"></a>
## O que foi verificado

Para a preparação do hub, foram executadas verificações de carga estática/ZIP/hash/metadados e verificações de documentação. Os testes de construção/unidade/UI de aplicativos privados existentes são evidências históricas e datadas. Nenhuma instalação de driver, alteração de exibição, operação ao vivo do RTSS ou benchmark de jogo foi realizada como parte desta preparação.

“Detectado”, “escrito”, “recarregado”, “capacidade disponível” e “medido no jogo” são resultados diferentes. Relate qual você observou.
