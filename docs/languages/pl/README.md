<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · **Polski** · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools autorstwa 禅堂 Zendo (RevoluSound Team).** Cztery niezależne narzędzia Windows do profili sterowników NVIDIA, instalacji sterowników, eksperymentalnych limitów ramek Multi Frame Generation i RTSS.

[Zdobądź narzędzia](docs/downloads.md) · [Instalacja](docs/installation.md) · [Kompatybilność i pomoc](docs/support.md) · [Kredyty i licencje](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse wymaga RTSS.** Najpierw zainstaluj [RivaTuner Statistics Server od Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). Aby limity FPS działały, musi być uruchomiony RTSS. Jest pobierany osobno.

<a id="projects"></a>
## Projekty

| Projekt | Cel | Wersja | Dokumentacja | Pobierz |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Edytor profili sterowników NVIDIA z dodanym wyświetlaczem, kolorem, kontrolkami HDR i ICC/WCS. Dawniej NVPI Custom. | 3.0.2.3 | [Przewodnik](NVIDIA-Profile-Inspector/README.md) | [Pakiety](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Przygotuj i zainstaluj oryginalny sterownik NVIDIA z możliwością wyboru, kopiami zapasowymi i odzyskiwaniem. | 0.1.4 | [Przewodnik](NVDriverForge/README.md) | [Pakiety](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Eksperymentalny RTX 40 MFG, trwała biblioteka gier, diagnostyka i konserwacja Streamline SDK. | 0.2.3 | [Przewodnik](NVMFG-Unlock40/README.md) | [Pakiety i status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Zarządzaj limitami RTSS FPS na program: diagnostyka, sugestie, wstrzymywanie, cofanie i udostępnianie profilu. | 0.2 | [Przewodnik](NVRasterPulse/README.md) | [Pakiety](docs/downloads.md#nvrasterpulse) |

**Pobrane:** [strona pobierania](docs/downloads.md) wyświetla status każdej wersji, pliki i wartości SHA-256. Funkcje eksperymentalne i ograniczenia kompatybilności są opisane w przewodnikach po projektach.

<a id="start-here"></a>
## Zacznij tutaj

1. Wybierz jedno narzędzie powyżej. Każdy działa niezależnie; instalowanie całego pakietu nie jest konieczne.
2. Przeczytaj jego wymagania i wybierz **Konfiguracja** dla zainstalowanej aplikacji lub **przenośny** dla osobnego folderu.
3. Po opublikowaniu wersji pobierz wybrany zasób aplikacji, przeczytaj dołączone uwagi i porównaj jego SHA-256.
4. Wykonuj kopie zapasowe przed zmianą sterownika, ustawień wyświetlacza, profilu NVIDIA lub czasu działania gry.

Dokumentacja jest dostępna w tych samych 34 językach, co aplikacje NV, za pomocą selektora znajdującego się w górnej części każdego przewodnika. GitHub nie wybiera automatycznie pliku README według języka przeglądarki. Język dokumentacji i ustawienia języka aplikacji są oddzielne.

<a id="provenance-and-ownership"></a>
## Pochodzenie i własność

To centrum dystrybuuje dokumentację i skompilowane aplikacje. Kod źródłowy aplikacji jest przechowywany prywatnie. Projekty typu upstream zachowują swoje autorstwo i licencje; dystrybucja ze źródeł prywatnych nie zastępuje tych warunków.

- Profile Inspector fork zachowuje licencję MIT firmy Orbmu2k i jest wyraźnie identyfikowany jako fork.
- NVDriverForge ma własne warunki dystrybucji binarnej i zawiera oddzielnie licencjonowane komponenty środowiska wykonawczego/narzędzi.
- NVMFG Unlock40 to niezależnie opracowana aplikacja. W celu porównania i udoskonalenia skonsultowano się z RTX40MFG-Unlock; współdzielone komponenty natywne zachowują swoje kredyty MIT. Warunki MinHook i NVIDIA Warunki SDK pozostają odrębne.
- NVRasterPulse zachowuje dostarczoną licencję MIT i przyznaje interfejs użytkownika wywodzący się z Profile Inspector. RTSS jest wymaganym programem zewnętrznym.

Zobacz [kompletna tabela komponentów](THIRD_PARTY_NOTICES.md), [pochodzenie plików i zmiany](docs/provenance.md) i [zakres licencji](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Inne projekty – RevoluSound Team

Są to osobne projekty modów audio, do których łącza znajdują się tutaj, aby pomóc Ci odkryć pracę zespołu.

| Gra | Projekt | O |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Zmiany dźwięku pojazdu obejmujące silniki, układy wydechowe, wloty i efekty turbo. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Późniejszy pakiet audio pojazdu FH5 zespołu. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Wcześniejszy pakiet FH5; jego strona Nexusa kieruje odwiedzających do późniejszego pakietu drużyny powyżej. |

Tytuły znajdują się na powiązanych stronach Nexus Mods. Ich pliki do pobrania, wymagania, napisy i uprawnienia pozostają w Nexus Mods.

<a id="help-and-participation"></a>
## Pomoc i uczestnictwo

[Zgłoś błąd lub zaproponuj funkcję](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Wkład](CONTRIBUTING.md) · [Raporty bezpieczeństwa](SECURITY.md) · [Dziennik zmian](CHANGELOG.md)

Ze względów bezpieczeństwa przeczytaj SECURITY.md przed opublikowaniem dzienników lub szczegółów technicznych. Po opublikowaniu repozytorium opiekun musi włączyć raportowanie prywatne.

> **Niezależne projekty społeczności.** NV Laboratory, NV Tools i te narzędzia nie są powiązane, sponsorowane ani oficjalnie wspierane przez NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS i inne nazwy produktów są znakami towarowymi ich odpowiednich właścicieli. Nazwy opisują zgodność i pochodzenie, a nie oficjalne poparcie.
