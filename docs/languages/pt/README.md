<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · **Português** · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools por 禅堂 Zendo (RevoluSound Team).** Quatro utilitários Windows independentes para perfis de driver NVIDIA, instalação de driver, limites de quadro experimentais Multi Frame Generation e RTSS.

[Obtenha as ferramentas](docs/downloads.md) · [Instalação](docs/installation.md) · [Compatibilidade e ajuda](docs/support.md) · [Créditos e licenças](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse requer RTSS.** Instale primeiro o [RivaTuner Statistics Server do Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). O RTSS deve estar em execução para que seus limites do FPS funcionem. Ele é baixado separadamente.

<a id="projects"></a>
## Projetos

| Projeto | Objetivo | Versão | Documentação | Baixar |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Editor de perfil de driver NVIDIA com exibição adicional, cor, controles HDR e ICC/WCS. Anteriormente NVPI Custom. | 3.0.2.3 | [Guia](NVIDIA-Profile-Inspector/README.md) | [Pacotes](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Prepare e instale um driver NVIDIA original com escolhas guiadas, backups e recuperação. | 0.1.4 | [Guia](NVDriverForge/README.md) | [Pacotes](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Experimental RTX 40 MFG, biblioteca de jogos persistente, diagnóstico e manutenção Streamline SDK. | 0.2.3 | [Guia](NVMFG-Unlock40/README.md) | [Pacotes e status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Gerencie os limites do RTSS FPS por programa: diagnósticos, sugestões, pausa, desfazer e compartilhamento de perfil. | 0.2 | [Guia](NVRasterPulse/README.md) | [Pacotes](docs/downloads.md#nvrasterpulse) |

**Downloads:** o [página de download](docs/downloads.md) lista o status de cada versão, arquivos e valores do SHA-256. Os recursos experimentais e os limites de compatibilidade estão descritos nos guias do projeto.

<a id="start-here"></a>
## Comece aqui

1. Escolha uma ferramenta acima. Cada um funciona de forma independente; instalar todo o conjunto é desnecessário.
2. Leia os requisitos e escolha **Configuração** para um aplicativo instalado ou **portátil** para uma pasta separada.
3. Quando seu lançamento for publicado, baixe o ativo do aplicativo nomeado, leia os avisos que o acompanham e compare seu SHA-256.
4. Mantenha backups antes de alterar um driver, configuração de vídeo, perfil NVIDIA ou tempo de execução do jogo.

A documentação está disponível nos mesmos 34 idiomas das aplicações NV através do seletor na parte superior de cada guia. GitHub não seleciona automaticamente um README por idioma do navegador. O idioma da documentação e a configuração de idioma do próprio aplicativo são separados.

<a id="provenance-and-ownership"></a>
## Proveniência e propriedade

Este hub distribui documentação e aplicativos compilados. O código-fonte do aplicativo é mantido de forma privada. Os projetos upstream mantêm sua autoria e licenças; a distribuição de fontes privadas não substitui esses termos.

- O Profile Inspector fork retém a licença Orbmu2k do MIT e é explicitamente identificado como fork.
- NVDriverForge tem seus próprios termos de distribuição binária e inclui componentes de tempo de execução/ferramenta licenciados separadamente.
- NVMFG Unlock40 é um aplicativo desenvolvido de forma independente. RTX40MFG-Unlock foi consultado para comparação e refinamento; os componentes nativos compartilhados mantêm seus créditos MIT. Os termos MinHook e NVIDIA SDK permanecem separados.
- NVRasterPulse retém a licença MIT fornecida e credita a UI derivada de Profile Inspector. RTSS é um programa externo necessário.

Consulte [tabela de componentes completa](THIRD_PARTY_NOTICES.md), [procedência e alterações do arquivo](docs/provenance.md) e [escopo da licença](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Outros projetos – RevoluSound Team

Estes são projetos separados de mod de áudio, vinculados aqui para ajudá-lo a descobrir o trabalho da equipe.

| Jogo | Projeto | Sobre |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Mudanças no som do veículo abrangendo motores, escapamentos, entradas de ar e efeitos turbo. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | O posterior pacote de áudio do veículo FH5 da equipe. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Pacote FH5 anterior; sua página Nexus direciona os visitantes para o pacote de equipe posterior acima. |

Os títulos seguem as páginas vinculadas do Nexus Mods. Seus downloads, requisitos, créditos e permissões permanecem no Nexus Mods.

<a id="help-and-participation"></a>
## Ajuda e participação

[Relate um bug ou sugira um recurso](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Contribuindo](CONTRIBUTING.md) · [Relatórios de segurança](SECURITY.md) · [Registro de alterações](CHANGELOG.md)

Para uma questão de segurança, leia SECURITY.md antes de publicar logs ou detalhes técnicos. Os relatórios privados devem ser habilitados pelo mantenedor após a publicação do repositório.

> **Projetos comunitários independentes.** NV Laboratory, NV Tools e esses utilitários não são afiliados, patrocinados ou endossados oficialmente por NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS e outros nomes de produtos são marcas registradas de seus respectivos proprietários. Os nomes descrevem compatibilidade e proveniência, não endosso oficial.
