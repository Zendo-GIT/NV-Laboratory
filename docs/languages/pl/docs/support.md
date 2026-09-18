<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · **Polski** · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatybilność i rozwiązywanie problemów

To są przygotowani kandydaci, a nie matryca certyfikacji dla wszystkich kombinacji Windows, GPU, sterowników i gier.

| Narzędzie | Windows / czas wykonania | Zależność sprzętowa/zewnętrzna | Operacje wymagające opieki |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Zgodny sterownik/wyświetlacz NVIDIA | Profil zapisuje i wyświetla podglądy |
| NVDriverForge 0.1.4 | Windows 10 kompilacja 19041+ / 11 x64; .NET/WPF w zestawie | Zgodny pakiet sterowników NVIDIA | Podwyższona instalacja, zaawansowane ustawienia, opcjonalny NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11x64; .NET/WPF w zestawie, pomocnicy Framework 4.8 | RTX 40, kwalifikująca się gra DLSS FG i przypięty dostawca | Natywne łatanie w grze, globalny dziennik profili, aktualizacje gier SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | Zainstalowano RTSS; bieganie po czapki | Zmiany profilu RTSS dla poszczególnych plików wykonywalnych |

Żaden pakiet ARM64 nie jest przygotowany. Dostępność wyświetlacza/interfejsu API i starsze wersje Windows mogą ograniczać poszczególne funkcje. Nie wynaleziono uniwersalnej minimalnej wersji NVIDIA ani RTSS. Dokładny skrót dostawcy NVMFG znajduje się w [pochodzenie](provenance.md).

<a id="before-reporting-a-bug"></a>
## Zanim zgłosisz błąd

Zidentyfikuj dokładny plik wykonywalny/wersję, którą otworzyłeś. Poprzednio zainstalowana kopia niekoniecznie jest wersją nowo pobranego pliku ZIP. Zapisz etapy odtwarzania, oczekiwany wynik i rzeczywisty wynik. W przypadku problemów z renderowaniem/ograniczaniem podaj wersję gry, odświeżenie ekranu, stan FG/V-Sync/VRR i dowolny inny ogranicznik lub nakładkę.

Użyj [formularz błędu](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Nigdy nie dołączaj całego prywatnego folderu programistycznego, archiwum sterowników, modelu, biblioteki DLL gry, zrzutu rejestru lub niesprawdzonego zbioru dzienników.

| Problem | Pierwsze kontrole |
| --- | --- |
| Zła wersja aplikacji | Potwierdź tożsamość EXE i skrót wydania; zamknij starszą kopię przed wymianą. |
| Błąd wykonania/uruchomienia | Zainstaluj wymagane środowisko Framework 4.8 lub zachowaj wszystkie dostarczone przenośne podfoldery. |
| UAC anulowany | Ponów tylko zamierzoną operację; anulowanie nie oznacza pomyślnej instalacji. |
| Niezgodność skrótu/podpisu | Przestań używać tego kandydata i uzyskaj oczekiwane oficjalne bajty. |
| Kolor/tryb NVPI odrzucony | Przywróć i użyj kombinacji obsługiwanej przez rzeczywisty wyświetlacz/sterownik. |
| Błąd tworzenia kopii zapasowej lub odzyskiwania NVDF | Zachowaj chronione zadanie i RECOVERY.txt; nie usuwaj dziennika ani nie wymuszaj sprzecznych zapisów. |
| Oczekujące ustawienia NVMFG | Rozwiąż odzyskiwanie przy zamkniętych grach, zachowując zmiany z innych narzędzi. |
| Czapka RP nie ma żadnego efektu | Uruchom RTSS, zidentyfikuj prawdziwy plik EXE gry, sprawdź stan haka i konkurencyjne limity. |
| Nasadka RP nie znika po usunięciu | Sprawdź RTSS Global; usunięcie powoduje jedynie zastąpienie lokalnego limitera. |

NVDriverForge oferuje podgląd lokalnego raportu JSON; NVMFG oferuje diagnostykę w sekcji Informacje. Wolisz te filtrowane raporty od pełnego archiwum dzienników i sprawdzasz je przed udostępnieniem. Blokada przywracania zgłoszona w NVMFG 0.1.1 nadal nie ma ustalonej przyczyny; zachowaj swój dziennik i zapisz wszelkie dostępne kody błędów. NVRasterPulse 0.2 oferuje diagnostykę konfiguracji w swoim menu akcji, bez pomiaru FPS.

<a id="logs-and-privacy"></a>
## Logi i prywatność

| Narzędzie | Dane lokalne do sprawdzenia, a nie do przesyłania hurtowego |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; chronione zadania `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; kopie zapasowe `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` obok pliku EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` poniżej |
| NVPI | Wybrany przez Ciebie eksport i wyświetlony błąd; nie wymyślono uniwersalnej ścieżki dziennika |

Usuń nazwy kont, katalogi domowe, ścieżki bibliotek gier, identyfikatory urządzeń, tokeny i niepowiązane okna z udostępnianych tekstów/obrazów. Zachowaj oryginały w celu ich odzyskania. Sprawy publiczne są widoczne dla każdego.

W przypadku luki, niebezpiecznego zachowania uprzywilejowanego lub niezamierzonej destrukcyjnej operacji należy postępować zgodnie z [SECURITY.md](../SECURITY.md), zamiast publikować szczegóły.

<a id="what-has-been-verified"></a>
## Co zostało sprawdzone

W celu przygotowania centrum przeprowadzono statyczne skanowanie ładunku/ZIP/hash/metadanych i sprawdzenie dokumentacji. Istniejące prywatne testy kompilacji/jednostek/UI aplikacji są historycznymi i przestarzałymi dowodami. W ramach tych przygotowań nie przeprowadzono żadnej instalacji sterownika, zmiany wyświetlacza, działania RTSS na żywo ani testu porównawczego gier.

„Wykryte”, „zapisane”, „przeładowane”, „dostępne możliwości” i „zmierzone w grze” to różne wyniki. Zgłoś, który zaobserwowałeś.
