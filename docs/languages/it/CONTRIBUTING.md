<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · **Italiano** · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# Contribuire

NV Laboratory è gestito da 禅堂 Zendo (RevoluSound Team). Il manutentore decide cosa viene accettato e rilasciato. L'apertura di una Issue o di una Pull Request non significa che un contributo sia accettato o autorizzato per la distribuzione.

Utilizza il modulo bug o funzionalità e identifica il programma/versione. Cerca prima i problemi esistenti. Discutere cambiamenti sostanziali prima di preparare un contributo di grandi dimensioni. Per questioni di sicurezza, seguire [SECURITY.md](SECURITY.md).

Questo hub pubblico contiene documentazione, avvisi, metadati di rilascio e convalida del repository. La fonte dell'applicazione e i test vengono mantenuti privatamente. Non inviare codice decompilato, origine privata, credenziali, profili utente o payload eseguibili.

I PR della documentazione dovrebbero mantenere allineate le 34 controparti linguistiche e la navigazione, preservare i nomi di comandi/file/prodotti e descrivere il comportamento effettivo. I nuovi screenshot devono essere tuoi, identificati con la versione e privi di dettagli personali; i dati sintetici devono essere etichettati. Fornire provenienza e autorizzazione per ogni nuova risorsa di terze parti.

Utilizza UTF-8, LF, Markdown leggibile e piccole modifiche mirate. Il validatore Python utilizza solo la libreria standard. Abbina lo stile esistente, evita dipendenze non necessarie ed esegui:

```text
python tools/validate_repository.py
```

Per le modifiche ai metadati della versione, includi la versione/il tag esatto, le dimensioni dei file e SHA-256 dai file binari controllati e mantieni allineate le pagine di download. Le modifiche dell'applicazione richiedono build/test privati ​​adeguati al comportamento interessato; un controllo della documentazione non è un test applicativo. Non inventare mai risultati o guadagni di test storici.

Contribuendo con materiale originale dell'hub, accetti la licenza con ambito MIT in [LICENZA](../../../LICENSE). Conservare gli avvisi di terze parti e identificare le modifiche; non sostituire una licenza upstream. L'accettazione e la pubblicazione rimangono decisioni del manutentore.
