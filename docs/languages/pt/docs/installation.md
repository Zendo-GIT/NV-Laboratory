<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Guia de instalação

Comece com [Transferências](downloads.md), que registra o status da publicação e os nomes exatos dos ativos. Estas são ferramentas separadas: instale apenas as que você precisa.

> **Para NVRasterPulse, instale o [RTSS do Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) antes de abrir o gerenciador de perfil.**
> RTSS deve ser executado para aplicar limites; ele não está incluído no NV Tools.

| Ferramenta | Edição instalada | Edição portátil | Pré-requisito principal |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extraia o ZIP NVPI completo | Driver NVIDIA e .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, tempo de execução incluído | Pacote de driver NVIDIA original compatível para operações de instalação |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Extraia o NVMFG ZIP completo, retenha subpastas | RTX 40, DLSS FG existente, provedor exato e auxiliares .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Extraia o ZIP RP completo | RTSS e .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Baixe, verifique, instale

1. Na versão publicada escolhida, baixe seu ativo de aplicativo nomeado, avisos ZIP e SHA256SUMS.txt.
2. Use o [Exemplo SHA-256](downloads.md#sha-256), com o nome real do arquivo baixado.
3. Para configuração, siga o instalador normal. Para ZIP portátil, extraia tudo para uma nova pasta local gravável; não execute de dentro do ZIP.
4. Abra o próprio EXE do aplicativo. Mantenha os arquivos de licença/configuração/dados que os acompanham.
5. Leia as instruções de uso dessa ferramenta antes de ativar as configurações ou operações do sistema.

Os binários atuais não estão assinados. Um hash correspondente confirma os bytes esperados; não é um certificado de segurança ou compatibilidade. Não desative as proteções de segurança do Windows apenas para suprimir um aviso.

A instalação do NVDF ou seu companheiro opcional NVPI é separada da instalação de um driver GPU. O complemento NVPI mantém seu nome de instalação interna existente. Seu botão RasterPulse elevado requer uma instalação protegida em todo o sistema; outras cópias do RP podem ser abertas através de seus próprios atalhos.

O NVMFG é experimental e possui o [reserva de licenciamento NVIDIA SDK documentada](provenance.md). Nenhum driver NVIDIA, provedor/modelo NGX ou tempo de execução do jogo Streamline está incluído. Downloads e atualizações de jogos selecionados do SDK são operações separadas explícitas.

<a id="language-and-updates"></a>
## Idioma e atualizações

Use o seletor de 34 idiomas do README para documentação. NVDF, NVMFG e RP possuem sua própria configuração de UI de 34 idiomas; NVPI mantém seu suporte a idiomas existente. Algumas strings técnicas do instalador voltam para o inglês.

Mantenha a identidade de instalação de uma ferramenta ao atualizar. Feche-o primeiro e preserve os backups. Para NVMFG, feche os jogos afetados e resolva a recuperação de perfil pendente. Para atualizações portáteis, use uma nova pasta em vez de combinar versões.

<a id="removing-a-tool"></a>
## Removendo uma ferramenta

Desinstalar um aplicativo não desfaz automaticamente suas configurações.

- **NVPI:** restaure os perfis/configurações de exibição pretendidos antes da remoção, se necessário.
- **NVDF:** use a recuperação primeiro se desejar restaurar alterações avançadas/NVENC. Uninstall deixa o driver gráfico, configurações e backups.
- **NVMFG:** feche jogos, desative/encerre o controlador, resolva a recuperação do NVIDIA e restaure os backups do jogo SDK desejado antes da remoção.
- **RP:** remova primeiro as substituições do limitador pretendidas. Uninstall não apaga limites RTSS salvos nem remove RTSS.

Consulte cada [guia do projeto](../README.md#projects) para obter localizações e limitações exatas dos dados ou [suporte](support.md) se uma etapa de recuperação falhar.
