<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Limites FPS por aplicativo até RivaTuner Statistics Server.**

> **Instale o RTSS primeiro.** O NVRasterPulse requer o [RivaTuner Statistics Server (RTSS), baixado do Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS deve estar em execução para impor limites. Nenhum instalador RTSS, DLL de gancho ou SDK está incluído.

[Baixe 0.1 e status](../docs/downloads.md#nvrasterpulse) · [Instalação](#installation) · [Como funcionam os limites](#usage) · [Licença](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Visão geral e propósito

NVRasterPulse é uma interface Windows compacta para gerenciar limites de quadros RTSS por nome executável. RTSS realiza a limitação. NVRasterPulse gerencia os valores de perfil correspondentes, backups e solicitações de recarga, com acesso à bandeja e opções persistentes.

Ele existe para facilitar a edição dos limites exatos por jogo, sem substituir um perfil RTSS inteiro ou perturbar suas configurações de sobreposição. O candidato atual ao **0.1** é a versão de 9 de setembro de 2026 com uma verificação de instalação RTSS necessária.

<a id="features"></a>
## Recursos

- Selecione um aplicativo em execução ou adicione seu executável manualmente.
- Salve os limites do FPS de 1 a 1000, com até três casas decimais.
- Codificação racional exata dos valores inseridos: 59.94 torna-se 2997/50.
- Configuração do Front Edge Sync (`SyncLimiter=1`) com espera ativa (`PassiveWait=0`).
- Atualizações de perfil por executável, backups automáticos e gravações atômicas.
- Remoção de substituições de limitadores, mantendo outro conteúdo do perfil.
- Detecção de instalação RTSS, seleção manual de caminho e inicialização/recarga explícita.
- Operação em bandeja de instância única, inicialização instalada opcional, 34 idiomas e quatro temas.
- Separe as ações normais de encerramento e **Quit + RTSS**.

<a id="compatibility"></a>
## Compatibilidade

| Requisito | Detalhes |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| Tempo de execução | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), instalado separadamente, se necessário |
| Software necessário | RTSS com `RTSS.exe`, um diretório `Profiles` correspondente e suporte de perfil/recarregamento compatível |
| GPU | A compatibilidade do RTSS determina o limitador; este gerenciador de perfil não requer uma geração RTX específica |
| Permissões | O aplicativo atual solicita acesso de administrador; a pasta de perfil RTSS selecionada deve estar acessível |
| Jogos | Depende do suporte de conexão do RTSS e das restrições de cada jogo; sem garantia anti-cheat |

Nenhuma versão mínima específica do RTSS foi certificada para todas as funções por esta auditoria do hub. Use a distribuição oficial atual e relate a versão exata se uma chave/recarregamento de perfil não funcionar. O RTSS instalado, mas parado, passa na verificação de instalação; ele deve então ser iniciado para limitação real.

<a id="installation"></a>
## Instalação

1. **[Baixe e instale RTSS do Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Abra [Downloads de NVRasterPulse](../docs/downloads.md#nvrasterpulse) e verifique a disponibilidade do lançamento.
3. Baixe `NVRasterPulse-0.1-win-x64-Setup.exe` ou `NVRasterPulse-0.1-win-x64-portable.zip`, além dos avisos/somas de verificação.
4. Comparar SHA-256. Execute a Instalação ou extraia todo o ZIP portátil para uma pasta local gravável.
5. Abra `NVRasterPulse.exe`. Se RTSS estiver faltando, use **Baixar RTSS**, instale-o e, em seguida, **Verifique novamente** ou selecione `RTSS.exe` manualmente.
6. Inicie o RTSS usando seu atalho normal ou o botão RTSS do NVRasterPulse se ele estiver parado.

Desativar o lembrete opcional não ignora a verificação de pré-requisitos. Uma inicialização silenciosa da bandeja do Windows aguarda até que a janela principal seja aberta antes de exibir esta verificação. A configuração instala apenas o NVRasterPulse. Seus EXEs não estão assinados.

<a id="usage"></a>
## Uso

1. Selecione o aplicativo em execução pretendido ou navegue até o EXE do jogo.
2. Insira um limite entre 1 e 1000 FPS, incluindo um valor fracionário, se necessário.
3. Salve e verifique o resultado relatado. NVRasterPulse atualiza o perfil RTSS desse executável e solicita uma recarga.
4. Confirme que o RTSS está em execução e verifique o comportamento no jogo pretendido.

Os perfis são codificados por **nome executável**, como `Game.exe.cfg`. Duas pastas diferentes contendo `Game.exe` compartilham o mesmo perfil RTSS; armazenar o caminho completo não remove essa colisão.

Salvar usa Front Edge Sync e espera ativa. A espera ativa pode aumentar o uso do CPU. Os campos alternativos `LimitTime` são neutralizados. Comentários existentes, configurações de sobreposição e `EnableHooking=0` são preservados. O perfil global RTSS não é alterado.

Use a ação trash para remover as substituições do limitador do NVRasterPulse. Isso não exclui todo o perfil RTSS. Um limite herdado do RTSS Global ou de outra ferramenta ainda poderá ser aplicado posteriormente.

**Fechar e sair:** a janela principal pode ficar oculta na bandeja. Normal **Sair** deixa o RTSS em execução e os limites salvos intactos. **Quit + RTSS** solicita um fechamento normal do processo RTSS correspondente na sessão atual, aguarda até oito segundos e não o interrompe à força. Os limites armazenados permanecem em ambos os casos.

O idioma e o tema são selecionados no aplicativo. A inicialização no login do Windows é opcional e destina-se a uma cópia instalada. O botão de informações explica ações comuns.

<a id="screenshots"></a>
## Capturas de tela

![Visualização da janela principal do NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

A interface de usuário 0.1 em francês existente é renderizada com exemplos de nomes de executáveis e um valor 176 FPS. RTSS é mostrado parado; esta é uma ilustração da interface, não um limitador de execução ou medição de latência. [Proveniência da imagem](../assets/README.md).

<a id="update-and-uninstall"></a>
## Atualizar e desinstalar

Saia do NVRasterPulse, baixe e verifique a nova versão e, em seguida, execute sua configuração ou extraia o portátil para uma nova pasta. Preservar configurações e backups RTSS. As atualizações do RTSS são separadas e vêm do Guru3D.

Para remover uma cópia instalada, use Windows **Installed apps**. Para portátil, saia e remova a pasta extraída quando seus backups estiverem seguros. Os limites salvos do RTSS não são removidos pela desinstalação do NVRasterPulse: remova primeiro as substituições do limitador pretendidas. RTSS possui seu próprio desinstalador.

Estado local: `%LOCALAPPDATA%\NVRasterPulse`. Backups automáticos do RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Um local `%LOCALAPPDATA%\RTSSProfileBridge` mais antigo pode ser lido para migração. Esses arquivos podem conter caminhos executáveis ​​pessoais e não devem ser publicados publicamente.

<a id="known-limitations"></a>
## Limitações conhecidas

- RTSS executa o limite. Um valor salvo ou uma solicitação de recarga bem-sucedida não é um resultado de tempo de quadro medido.
- Executáveis com o mesmo nome compartilham um perfil.
- Outro limitador global/por jogo pode afetar o resultado; desabilitar a substituição local não remove um limite herdado.
- Um gancho RTSS deliberadamente desabilitado permanece desabilitado.
- A espera ativa tem uma compensação CPU/energia.
- Nenhum jogo universal, anti-cheat ou validação de latência de ponta a ponta.
- O mecanismo limitador independente experimental anterior não foi compilado ou enviado.
- Os backups automáticos não implicam uma interface completa de restauração de backup com um clique.

<a id="troubleshooting"></a>
## Solução de problemas

| Sintoma | Ação |
| --- | --- |
| O pré-requisito RTSS permanece aberto | Selecione o `RTSS.exe` real e a pasta de perfis correspondente e verifique novamente. |
| Limite salvo, mas sem efeito | Inicie RTSS; verifique o EXE/perfil correto do jogo, permissões de gancho e outros limitadores. |
| Falha ao salvar | Verifique as permissões da pasta e preserve o erro/backup exibido. |
| O limite permanece após a remoção | Inspecione o RTSS Global e outras ferramentas; a ação trash remove apenas substituições de limitadores locais. |
| Dois jogos recebem o mesmo limite | Verifique se os nomes dos arquivos executáveis são idênticos. |
| Sair + RTSS deixa RTSS aberto | Feche o RTSS normalmente; este comando evita deliberadamente o encerramento forçado. |

Se estiver restaurando manualmente um backup RTSS, feche primeiro o RTSS e preserve o perfil atual antes de substituí-lo pelo backup pretendido. Isso pode substituir edições de perfil não relacionadas; inspecione o arquivo e a data. [Suporte compartilhado](../docs/support.md).

<a id="faq"></a>
## Perguntas frequentes

**Eu também preciso do MSI Afterburner?** NVRasterPulse requer RTSS; não depende do aplicativo Afterburner. Siga as opções de instalação do distribuidor RTSS.

**Posso usar isso sem o RTSS em execução?** Você pode gerenciar perfis assim que uma instalação for detectada, mas o RTSS deve ser executado para limitação.

**Sair ou desinstalar remove os limites?** Não. Remova explicitamente as substituições do limitador desejadas antes de remover o NVRasterPulse.

**É um fork de RTSS?** Não. É um gerenciador de perfil independente; nenhuma fonte ou executável RTSS é incorporada.

<a id="upstream-modifications-and-credits"></a>
## Upstream, modificações e créditos

O repositório de desenvolvimento é originário de [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Suas paletas/recursos de UI MIT são creditados. Os serviços de gerenciamento de perfil, codificação de frações, backups, ponte de recarga RTSS, comportamento da bandeja, guia de pré-requisitos, idiomas e ícone específico do aplicativo foram desenvolvidos/adaptados pelo 禅堂 Zendo (RevoluSound Team).

RTSS é desenvolvido por **Unwinder** e distribuído separadamente através do Guru3D. NVRasterPulse chama `UpdateProfiles` da DLL de gancho instalada selecionada; nenhum RTSS SDK ou binário de gancho é redistribuído. O instalador usa Inno Setup 7.1.0 não modificado com scripts/traduções adaptados e um bootstrap de projeto.

[Proveniência completa](../docs/provenance.md) · [Tabela de terceiros](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licença

O pacote distribui explicitamente o NVRasterPulse sob o [Licença MIT](../../../../NVRasterPulse/LICENSE) fornecido, mantendo o Copyright (c) 2016 Orbmu2k. A fonte do aplicativo é mantida de forma privada; MIT não requer publicação da fonte modificada. RTSS e Windows/.NET permanecem sob seus próprios termos. [Avisos completos](LICENSES/README.md).

Independente de NVIDIA Corporation, MSI e RTSS; não patrocinado ou endossado oficialmente por eles. Os nomes dos produtos permanecem marcas registradas de seus proprietários.
