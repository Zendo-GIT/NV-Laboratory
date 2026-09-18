<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · **Polski** · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Instrukcja instalacji

Zacznij od [Pliki do pobrania](downloads.md), który rejestruje status publikacji i dokładne nazwy zasobów. Są to osobne narzędzia: instaluj tylko te, których potrzebujesz.

> **W przypadku NVRasterPulse zainstaluj [RTSS od Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) przed otwarciem menedżera profili.**
> Aby zastosować limity, należy uruchomić RTSS; nie jest on uwzględniony w NV Tools.

| Narzędzie | Zainstalowana edycja | Wersja przenośna | Główny warunek wstępny |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Wyodrębnij kompletny plik NVPI ZIP | Sterownik NVIDIA i .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, zawiera środowisko wykonawcze | Zgodny oryginalny pakiet sterowników NVIDIA do operacji instalacyjnych |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Wyodrębnij cały plik ZIP NVMFG, zachowaj podfoldery | RTX 40, istniejący DLSS FG, dokładny dostawca i pomocnicy .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Wyodrębnij kompletny plik RP ZIP | RTSS i .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Pobierz, sprawdź, zainstaluj

1. W wybranej opublikowanej wersji pobierz nazwany zasób aplikacji, uwagi ZIP i SHA256SUMS.txt.
2. Użyj [Przykład SHA-256](downloads.md#sha-256) z rzeczywistą nazwą pobranego pliku.
3. W przypadku instalacji postępuj zgodnie ze zwykłym instalatorem. W przypadku przenośnego pliku ZIP wypakuj wszystko do nowego lokalnego folderu z możliwością zapisu; nie uruchamiaj się z wnętrza ZIP-a.
4. Otwórz własny plik EXE aplikacji. Zachowaj dołączone pliki licencji/konfiguracji/danych.
5. Przed włączeniem ustawień lub operacji systemowych przeczytaj instrukcję obsługi tego narzędzia.

Bieżące pliki binarne są niepodpisane. Pasujący skrót potwierdza oczekiwane bajty; nie jest to certyfikat bezpieczeństwa ani zgodności. Nie wyłączaj zabezpieczeń Windows tylko po to, aby ukryć ostrzeżenie.

Instalacja NVDF lub jego opcjonalnego towarzysza NVPI przebiega niezależnie od instalacji sterownika GPU. Towarzysz NVPI zachowuje istniejącą wewnętrzną nazwę instalacji. Jego podwyższony przycisk RasterPulse wymaga chronionej instalacji w całym systemie; inne kopie RP można otworzyć za pomocą własnych skrótów.

NVMFG jest eksperymentalny i ma [udokumentowana rezerwa licencyjna NVIDIA SDK](provenance.md). Nie uwzględniono sterownika NVIDIA, dostawcy/modelu NGX ani środowiska wykonawczego gry Streamline. Wybrane pliki do pobrania SDK i aktualizacje gier są odrębnymi operacjami.

<a id="language-and-updates"></a>
## Język i aktualizacje

Do dokumentacji użyj 34-językowego selektora plików README. NVDF, NVMFG i RP mają własne ustawienia interfejsu użytkownika w 34 językach; NVPI zachowuje istniejącą obsługę języków. Niektóre parametry techniczne instalatora pochodzą z języka angielskiego.

Podczas aktualizacji zachowaj tożsamość instalacji narzędzia. Najpierw zamknij go i zachowaj kopie zapasowe. W przypadku NVMFG zamknij gry, których to dotyczy i rozwiąż oczekujące odzyskanie profilu. W przypadku aktualizacji przenośnych użyj świeżego folderu zamiast łączyć wersje.

<a id="removing-a-tool"></a>
## Usuwanie narzędzia

Odinstalowanie aplikacji nie powoduje automatycznego cofnięcia jej ustawień.

- **NVPI:** w razie potrzeby przywróć zamierzone profile/ustawienia wyświetlania przed usunięciem.
- **NVDF:** najpierw skorzystaj z odzyskiwania, jeśli chcesz przywrócić zmiany zaawansowane/NVENC. Uninstall pozostawia sterownik graficzny, ustawienia i kopie zapasowe.
- **NVMFG:** zamknij gry, wyłącz/wyjdź z kontrolera, rozwiąż proces odzyskiwania NVIDIA i przywróć kopie zapasowe wybranych gier SDK przed usunięciem.
- **RP:** najpierw usuń zamierzone zastąpienia ogranicznika. Uninstall nie kasuje zapisanych wielkich liter RTSS ani nie usuwa RTSS.

Zobacz każdy [przewodnik po projekcie](../README.md#projects), aby poznać dokładne lokalizacje danych i ograniczenia, lub [wsparcie](support.md), jeśli etap odzyskiwania nie powiedzie się.
