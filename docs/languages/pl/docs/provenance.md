<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · **Polski** · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Pochodzenie, zmiany i licencjonowanie

Audyt ten opisuje kandydatów przygotowanych dnia **2026-09-09**. Źródła aplikacji pozostają prywatne; publiczne wykazy zawierają nazwy plików i skróty, a nie kod źródłowy. Zobacz [pełne uwagi dotyczące komponentów](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Odniesienie: Orbmu2k/nvidiaProfileInspector zatwierdzenie `592d962cca8827efe8859461a84267755595064a`; kandydująca wersja wykonywalna 3.0.2.3. Zatwierdzenie odniesienia i wersja zestawu fork to różne identyfikatory; z wersji fork nie wynika żadna wcześniejsza wersja wydania.

Porównano 157 plików źródłowych/zasobów programu Clean Companion z tym zatwierdzeniem: 2 identyczne bajty, 134 różniące się jedynie zakończeniami linii lub BOM w formacie UTF-8, 11 zmodyfikowanych, 10 nieobecnych w porównywanej ścieżce upstream. „Dodano” odnosi się do tej ścieżki i samo w sobie nie stanowi dowodu oryginalnego autorstwa.

[Pełne porównanie plików/haszów](../../../provenance/nvpi-source-provenance.json).

| Obszar | Dziedziczona praca | Wkład Fork |
| --- | --- | --- |
| Edytor profili | Model profilu, import/eksport, powiązania aplikacji i dane referencyjne | Integracja z Screenem i zewnętrznym launcherem narzędzi |
| NVAPI | Współpraca DRS Orbmu2k | Współdziałanie związane z kolorem/wyświetlaniem, ograniczenia natywnego ładowania produkcyjnego i usuwanie prób |
| Usługi wystawowe | Interfejsy API Windows/NVIDIA jako interfejsy zewnętrzne | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| Interfejs użytkownika | Upstreamowe zasoby, palety i ikony WPF | Okna dialogowe na ekranie, 15-sekundowe potwierdzenie, stan/odczyt i układ paska narzędzi |
| Program uruchamiający | Istniejąca powłoka aplikacji | Chronione, oddzielnie instalowane wyszukiwanie i uruchamianie RasterPulse |
| Opakowanie | MIT powyżej | Czysty, samodzielny dodatek, oddzielny instalator/deinstalator, zachowane uwagi |

Publiczna mapa źródłowa zawiera ścieżki rozwiązań/zasobów umożliwiające śledzenie; pliki te nie są rozpowszechniane jako źródła. Testy rozwojowe, próbne interfejsy i stary połączony plik binarny NVPI/RasterPulse są wykluczone.

<a id="nvdriverforge"></a>
## NVDriverForge

Niezależna aplikacja C#/.NET 8/WPF; przepływ pracy skierowany do użytkownika jest częściowo inspirowany NVCleanstall. W ładunku produkcyjnym nie zidentyfikowano żadnego źródła/pliku binarnego NVCleanstall. Nie jest reprezentowany jako fork tej zastrzeżonej aplikacji.

Oryginalne prace projektowe obejmują analizę/wybór komponentów, chronione zadania instalacji, kopie zapasowe i odzyskiwanie transakcji, pobieranie katalogu NVIDIA, sprawdzanie aktualizacji, zlokalizowane wyjaśnienia, opcjonalne zaawansowane przepływy pracy/NVENC i bootstrap instalatora.

Odziedziczone/zaadaptowane komponenty: cztery palety motywów NVPI, rozszerzony interfejs NVAPI DRS i oddzielnie opcjonalny dodatek MIT NVPI. Interfejs wyboru ustawienia wstępnego Custom NV i integracja transakcji z listy dozwolonych należą do NVDriverForge; ustawienie wstępne nie jest oficjalną rekomendacją NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 i Inno Setup pozostają niezmodyfikowanymi komponentami zewnętrznymi, używanymi na ich własnych warunkach. keylase Dane NVENC nie są osadzone; wybierane jest jedno dokładne zatwierdzenie i sprawdzane, gdy użytkownik żąda kompatybilnego pobrania. Dla tych danych pochodzących z wyższego szczebla nie została ustanowiona żadna licencja na redystrybucję.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 został opracowany niezależnie przez 禅堂 Zendo (RevoluSound Team). Opiekun użył RTX40MFG-Unlock do porównania i udoskonalenia. Aplikacja jako całość nie jest prezentowana jako fork. To rozróżnienie nie usuwa zasług za współdzielone/dostosowane komponenty w bieżącej warstwie natywnej.

Odniesienie porównawcze: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, zatwierdzenie `4e776d068f91b4a665425542bb005dd57cc3d891`. Prywatne drzewo silnika natywnego zawiera 48 porównywanych plików: 35 różnic związanych tylko z formatowaniem, 4 zmodyfikowane pliki i 9 nieobecnych w ścieżce referencyjnej. [Pełne porównanie](../../../provenance/nvmfg-source-provenance.json).

Zmodyfikowane odziedziczone pliki: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Dodatkowe ścieżki obejmują `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` i zachowaną licencję nadrzędną.

Jednostki produkcyjne C++: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection i vsync_observer; plus zestaw entry_detour i bufor/hak/trampolina/HDE64 MinHook. Odziedziczony interfejs ReShade, starsze zasoby podkładek i niewykorzystane cele CMake nie są częścią tej kompilacji produkcyjnej.

Pasujące komponenty obejmują zasady dotyczące łatania/dostawcy i prace tymczasowe; ich informacje o prawach autorskich i zezwoleniach pozostają nienaruszone. Centralna koordynacja NGX/bootstrap/kontrolera, obsługa V-Sync dla poszczególnych gier, diagnostyka sesji i przepływ pracy z aplikacją Windows/SDK/kopią zapasową to prace projektowe autorstwa 禅堂 Zendo (RevoluSound Team). Powyższe liczby opisują pliki, w tym pliki stron trzecich i nieużywane, a nie procent autorstwa lub chronologię pomysłu któregokolwiek projektu.

Pomocnik dostosowuje NvapiDrsWrapper i NativeArrayHelper NVPI do osobnego zestawu, z logiką profilu autorstwa autora. Stara próbna ścieżka programowania jest wykluczona. Wspólne palety rodziny pochodzą z NVPI.

Numer referencyjny MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; w odziedziczonym skompilowanym podzbiorze nie ma funkcjonalnych zmian lokalnych w porównaniu. Nagłówki integracji Streamline: 2.12; licencja na otwarty nagłówek zweryfikowana pod adresem v2.12.0. Źródło nagłówka NGX: NVIDIA/DLSS zatwierdzenie `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Silnik kandydata SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Wymagany dostawca SHA-256 w engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Zgłoszona rodzina dostawców 310.9 nie jest wymienna z tym dokładnym skrótem. Nie uwzględniono żadnej biblioteki DLL ani modelu dostawcy.

**Wyjątkowy punkt licencjonowania:** pełna licencja NVIDIA RTX SDK, wersja z 14 marca 2024 r., zawiera ograniczenie w sekcji 4(d) dotyczące omijania ograniczeń technicznych. Audyt nie stwierdza pozwolenia na takie wykorzystanie. Zachowanie licencji na silnik MIT, bycie darmowym lub obserwowanie innych modów nie rozwiązuje tego odrębnego warunku. Przygotowanie kandydata nie jest zaświadczeniem prawnym. Oryginalna, krótka informacja nagłówkowa jest uzupełniona pełną licencją; jego tekst Windows-1252 jest również dostarczany w czytelnym formacie UTF-8, z zachowaniem oryginalnych bajtów.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Niezależny menedżer profili RTSS opracowany w repozytorium pochodzącym z NVPI. Odziedziczone zasoby/palety interfejsu użytkownika MIT i pochodzenie projektu pozostają zapisane. Aplikacja produkcyjna wyraźnie korzysta z dostarczonej licencji MIT.

Prace projektowe: precyzyjne parsowanie/zapis profilu RTSS i kodowanie ułamkowe, kopie zapasowe, usuwanie nadpisań, mostek przeładowania, wykrywanie wymagań wstępnych, kompaktowy interfejs użytkownika, cykl życia zasobnika, kontrola uruchamiania i lokalizacja. RTSS wykonuje rzeczywiste ograniczenie.

W zestawie nie ma źródła RTSS, biblioteki hook DLL, SDK ani instalatora. Most wywołuje eksport w istniejącej, wybranej przez użytkownika instalacji RTSS. W tym pakiecie nie ma pakietu sterowników NVIDIA, natywnego eksperymentalnego limitera, Framepacer, środowiska wykonawczego MinHook, ReShade ani DLSS.

<a id="assets-generated-data-and-tools"></a>
## Zasoby, wygenerowane dane i narzędzia

[Kredyty majątkowe](../assets/README.md) identyfikuje istniejące podglądy interfejsu i selektor konfiguracji NVPI. Znajdujące się w nich fikcyjne wartości są oznaczone. Nie jest kopiowany żaden zasób gry/Nexusa, profil osobisty, prywatne logo ICC, firmowe logo NVIDIA ani plik czcionki.

Wygenerowane nazwy zgodności gier odziedziczone w NVMFG stanowią pomoc w wykrywaniu, a nie dowód testowy. Wygenerowane katalogi instalatorów są zapisane w [uwagi tłumacza](../../../../licenses/INSTALLER-TRANSLATORS.md). Wygenerowane rekordy kompilacji ze ścieżkami bezwzględnymi pozostają prywatne.

Narzędzia do kompilacji prywatnej obejmują skrypty audytu .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup i Python. Ich kompilatory, nagłówki, programy uruchamiające testy i zasoby debugowania nie są dystrybuowane. Wersja statyczna CRT podlega obowiązującym warunkom dotyczącym łańcucha narzędzi Microsoft.

<a id="scope-of-verification"></a>
## Zakres weryfikacji

Lokalny audyt spisał wszystkie pliki w trzech głównych obszarach programistycznych, wykluczając obiektowe bazy danych Git i połączone katalogi docelowe. Przeskanowano aktywne źródło/dokumenty; zinwentaryzowano i wyłączono obiekty historyczne. Wybrane pliki ZIP i aktualne ładunki zostały zeskanowane i zaszyfrowane; pakiety .NET zostały zdekompresowane w celu dodatkowej kontroli. Podczas początkowego audytu nie uwzględniono żadnego produktu, instalatora, gry, procesu RTSS ani sterownika.

Późniejsza wersja 2 konfiguracji NVPI naprawia samodzielny wybór języka za pomocą współdzielonych elementów sterujących Inno i bootstrap. Jasne/ciemne urządzenia prywatne zweryfikowały nawigację za pomocą myszy i klawiatury oraz wszystkie 34 wyraźne kody językowe. Rzeczywisty selektor instalacji został otwarty na nigdy nie wyświetlanym prywatnym pulpicie i anulowany przed instalacją. Siedem plików aplikacji i przenośny plik ZIP pozostają niezmienione. NVDriverForge 0.1.3 zawiera poprawioną wersję towarzyszącą i nadal przekazuje `/LANG`.

NVDriverForge 0.1.3 został ukończony 10.09.2026. Jego prywatny raport z weryfikacji rejestruje 366 testów aplikacji, 118 kontroli towarzyszących, 32 kontrole konfiguracji, 156 porównań natywnych i 34 przypadki przekierowań językowych. Poprawka dotycząca chronionego wyboru komponentów została odtworzona w oparciu o oryginalny pakiet sterowników bez zmiany jego ładunku ani instalowania sterownika. Są to przestarzałe wyniki pracy zespołu ds. produktu, a nie testy powtórzone w ramach tej aktualizacji dokumentacji lub dowód udanej rzeczywistej instalacji sterownika.

Ta aktualizacja centrum nie zmienia żadnego funkcjonalnego kodu aplikacji. Wcześniejsze testy kompilacji aplikacji/jednostek/UI pozostają przestarzałymi dowodami historycznymi. Nie jest to pełna inżynieria wsteczna każdego pliku binarnego strony trzeciej ani gwarancja na każdy możliwy tajny wzór.
