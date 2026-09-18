<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · **Português** · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tradução assistida por máquina do inglês. Nomes técnicos, comandos, URLs e textos legais originais são preservados. A revisão de falantes nativos é bem-vinda; consulte a referência em inglês se o texto não estiver claro.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publicações e lançamentos

O repositório público é **Zendo-GIT/NV-Laboratory**. As alterações na documentação são revisadas, confirmadas e enviadas pelo mantenedor com **GitHub Desktop**. Um commit local não carrega arquivos. Pacotes binários são ativos separados da versão GitHub; eles nunca pertencem à lista de alterações do Git.

<a id="documentation-updates"></a>
## Atualizações de documentação

1. Abra a pasta **NV-Laboratory** em GitHub Desktop.
2. Revise a documentação, avisos, imagens, metadados JSON e o validador de documentação.
3. Execute `python tools/validate_repository.py` dessa pasta.
4. Confirme as alterações revisadas e use **Push origin**. Verifique o resultado das ações.
5. Mantenha a identidade pública do autor **禅堂 Zendo (RevoluSound Team)** e o endereço GitHub `noreply` da conta.

Nunca selecione o espaço de trabalho de desenvolvimento pai, o diretório de auditoria privado ou o diretório de anexo binário. [Comprometa a privacidade do e-mail](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Lançamentos de aplicativos independentes

| Ferramenta | Etiqueta | Política de versão |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Versão existente do aplicativo em quatro partes; a revisão de configuração 2 tem seu próprio nome de arquivo |
| NVDriverForge | nvdriverforge-v0.1.4 | Esquema 0.x existente; atualizações versionadas preservam pacotes anteriores |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Versão do aplicativo 0.2.3; alterações cumulativas desde o público 0.1.1 |
| NVRasterPulse | nvrasterpulse-v0.2 | Versão existente em duas partes |

O mantenedor pode publicar diretamente ou autorizar um assistente a publicar os ativos auditados. A publicação é explícita; nenhum fluxo de trabalho cria um Release em cada commit.

1. Revise o relatório de pré-publicação atual, as fontes dos binários, as licenças e os valores SHA-256.
2. Crie um rascunho para a tag da ferramenta, visando o commit do hub revisado. Inclua as notas de lançamento específicas da versão preparadas.
3. Anexe apenas os ativos portáteis/de configuração dessa versão, `Licenses-and-Credits.zip` e `SHA256SUMS.txt`.
4. Verifique compatibilidade, instalação, dependências, alterações e limites conhecidos. Mantenha RTSS em destaque para NVRasterPulse.
5. Publique, verifique os URLs, tamanhos e hashes dos ativos públicos e registre a data real de publicação em `docs/releases.json`.
6. Atualize as páginas de download e traduções e, em seguida, confirme/envie suas alterações no GitHub Desktop.

Os links de tags por projeto evitam enviar usuários para outra ferramenta por meio de um link `releases/latest` compartilhado. Os arquivos automáticos **Source code** do GitHub contêm este hub de documentação. As fontes de aplicativos permanecem privadas. Os avisos de componentes originais permanecem intactos e uma versão não resolve a reserva NVIDIA SDK documentada do NVMFG.


A atualização de 18 de setembro prepara três novas tags; a versão Profile Inspector existente permanece inalterada. Os nomes dos ativos, tags e `SHA256SUMS.txt` devem permanecer exatos para as verificações de atualização do aplicativo. Publique lançamentos normais sem o sinalizador de pré-lançamento para expô-los a verificações de lançamento estável; NVMFG permanece experimental.

<a id="integrity-and-storage"></a>
## Integridade e armazenamento

Nunca substitua silenciosamente os bytes binários publicados. Use uma nova versão explícita ou revisão do instalador com novos hashes. Os sidecars legais complementam os avisos incorporados. NVDriverForge 0.1.4 portátil tem 142.017.891 bytes, acima do limite comum de arquivo Git de 100 MiB do GitHub. Liberar anexos evita colocar binários ou Git LFS neste hub. [Orientação para arquivos grandes GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

O relatório de vulnerabilidade privada deve ser habilitado nas configurações de segurança do repositório. Verifique sua disponibilidade antes de direcionar relatórios sensíveis para lá; [SECURITY.md](../SECURITY.md) fornece um substituto que não expõe detalhes da vulnerabilidade.

[Baixar catálogo](downloads.md) · [Documentação de lançamento do GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
