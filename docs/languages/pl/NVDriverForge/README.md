<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · **Polski** · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Przygotuj instalację sterownika NVIDIA z przejrzystym wyborem komponentów i opcjonalnymi ustawieniami.**

[Pobierz 0.1.4 i status](../docs/downloads.md#nvdriverforge) · [Instalacja](#installation) · [Kredyty](#credits-and-upstream) · [Licencja](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Przegląd i cel

NVDriverForge prowadzi Cię przez oryginalny pakiet sterowników NVIDIA: wybierz sterownik, sprawdź jego komponenty, przejrzyj opcjonalne poprawki, a następnie potwierdź instalację. Istnieje, aby uczynić te wybory zrozumiałymi i zachować razem informacje dotyczące instalacji, operacji uprzywilejowanych i odzyskiwania.

Jest to niezależnie opracowana aplikacja, inspirowana częściowo przepływem pracy NVCleanstall. Nie obejmuje NVCleanstall ani nie zapewnia pełnej parzystości funkcji.

<a id="features"></a>
## Funkcje

- NVIDIA Game Ready / Studio wyszukiwanie i pobieranie; opcjonalne wykrywanie poprawek z ręcznym przywracaniem.
- Analiza oryginalnego pakietu, hashów, podpisów NVIDIA, manifestów i zgodnych wpisów INF.
- Wybór komponentów z zależnościami i zachowaniem nieznanych komponentów.
- Wersja 0.1.4 umożliwia pominięcie wybranych opcjonalnych komponentów NVIDIA i wyklucza z wykrywania tylko zweryfikowane, niesprawdzone komponenty. Już istniejące lub niemające zastosowania opcjonalne środowiska wykonawcze nie są już wymuszane jako komponenty krytyczne.
- Przejrzyste podsumowania niepowodzeń instalacji i dostęp do szczegółowych dzienników we wszystkich 34 językach.
- Sprawdzanie gotowości, wyraźne potwierdzenie, eksport magazynu sterowników i natywna kopia zapasowa profilu NVIDIA przed instalacją.
- Opcjonalne ustawienia zaawansowane z kontrolą wstępną, dziennikami i odzyskiwaniem uwzględniającym konflikty.
- Opcjonalne ustawienie wstępne **Custom NV** z nazwanymi opcjami i wyjaśnieniami, w tym oddzielny wybór siły SILK i sprawdzenie zgodności.
- Opcjonalne pobieranie dokładnej wersji poprawki NVENC; sprawdzane są bajty źródłowe i docelowe.
- Oddzielna, opcjonalna instalacja Profile Inspector fork z ekranu Narzędzia.
- Przewodnik po komponentach, preferencje wielokrotnego użytku, zestawy sterowników, raporty lokalnego wsparcia i opcjonalne aktualizacje aplikacji.
- 34 języki interfejsu i cztery motywy.

Dostępne opcje zaawansowane obejmują MPO, wskaźnik DLSS, Ansel, uśpienie audio NVIDIA, MSI, zasady/priorytet przerwań, HDCP, uruchamianie kontenera wyświetlacza i kwalifikującą się starszą usługę telemetryczną. Każdy ma swoje własne warunki wstępne i skutki; nie są to uniwersalne ulepszenia wydajności.

<a id="compatibility"></a>
## Kompatybilność

| Wymaganie | Szczegóły |
| --- | --- |
| Systemu | Windows 10 kompilacja 19041 lub nowsza / Windows 11, x64 |
| GPU/sterownik | Zgodny pakiet NVIDIA i wykryty sprzęt; automatyczne przeszukiwanie katalogu obejmuje przede wszystkim znane modele GeForce |
| Czas wykonania | .NET 8 / WPF 8.0.31 zawarty w przygotowanym samodzielnym pakiecie |
| Przywileje | Normalna konfiguracja interfejsu użytkownika/na użytkownika; instalacja sterownika i zmiany systemu wymagają dostępu administratora |
| Sieć | Wymagane do wyszukiwania/pobierania NVIDIA online i jawnych żądań NVENC przesyłanych dalej; można wybrać lokalny oryginalny sterownik |
| Dołączone narzędzia | Niezmodyfikowany 7-Zip 26.03, uwagi dotyczące czasu działania, opcjonalny dodatek MIT Profile Inspector |
| Opcjonalny towarzysz | .NET Framework 4.8 dla oddzielnego Profile Inspector fork |

Żadna dowolna minimalna wersja sterownika nie obejmuje wszystkich funkcji. Wyszukiwanie Multi-GPU musi odpowiadać każdemu wykrytemu GPU. Nieobsługiwane/profesjonalne modele mogą wymagać ręcznego wyboru sterownika. Instalator NVIDIA pozostaje ostatecznym autorytetem w zakresie sprzętu/systemu operacyjnego.

<a id="installation"></a>
## Instalacja

1. Odwiedź [pliki do pobrania](../docs/downloads.md#nvdriverforge) i potwierdź, że wydanie zostało opublikowane.
2. Wybierz `NVDriverForge-Setup.exe` do instalacji lub `NVDriverForge.exe` do użytku przenośnego.
3. Porównaj SHA-256 z wersją `SHA256SUMS.txt`.
4. Uruchom Instalatora w celu instalacji dla każdego użytkownika i standardowego dezinstalatora lub umieść przenośny plik EXE w zapisywalnym folderze i otwórz go.

Wersja przenośna zawiera środowisko wykonawcze i opcjonalny instalator. Zainstalowanie NVDriverForge nie powoduje zainstalowania sterownika GPU. Jego pliki EXE są obecnie niepodpisane.

<a id="usage"></a>
## Użycie

1. **Sterownik:** pobierz z NVIDIA lub wybierz oryginalny plik EXE instalatora NVIDIA. Niech analiza się zakończy.
2. **Komponenty:** opisy przeglądów i wymagane zależności. Nieznane komponenty zostają zachowane.
3. **Ulepszenia:** pozostaw niechciane opcje bez zmian. Przeczytaj efekty i kompromisy, zanim cokolwiek wybierzesz.
4. **Recenzja:** sprawdź dokładny sterownik, komponenty i opcjonalne operacje, a następnie potwierdź instalację.
5. Zaakceptuj UAC tylko dla wybranej operacji. Zachowaj instrukcje odzyskiwania chronionego zadania.
6. Jeśli nowy sterownik wymaga ponownego uruchomienia, postępuj zgodnie ze zgłoszonym stanem. Odroczone operacje wymagają jawnego wznowienia po tym ponownym uruchomieniu.

Custom NV uruchamia się bez zmian. Wybierz poszczególne nazwane wartości lub przejrzyj dostarczone ustawienie wstępne i jego wykluczenia. Jego dwa wewnętrzne pola informacyjne nie są zapisywane niezależnie. Ustawienia są stosowane tylko w procesie zweryfikowania nowego sterownika, nigdy poprzez otwarcie podglądu. Instalowanie oddzielnego edytora NVPI nie jest wymagane.

Opcjonalna praca NVENC pobiera kompatybilne dane z przypiętego zatwierdzenia keylase. Zmienia dwie biblioteki DLL sterowników i unieważnia ich podpisy; może zostać odrzucony przez Windows, kodery, DRM lub funkcję zapobiegającą oszustwom. Żadne takie dane ani biblioteka DLL NVIDIA nie są osadzone w NVDriverForge. [Pochodzenie i ograniczenia licencyjne](../docs/provenance.md).

Preferencje kontrolują język, motyw i opcjonalne sprawdzanie aktualizacji zainstalowanych przez użytkowników. Urządzenie przenośne nie tworzy zainstalowanego zadania sprawdzania w tle. Narzędzia i odzyskiwanie są oddzielne od czterech etapów instalacji.

<a id="backup-and-diagnostic-tools"></a>
## Narzędzia do tworzenia kopii zapasowych i diagnostyki

**Przed instalacją:** kontrole gotowości obejmują sygnaturę pakietu, procesory graficzne, szacowany obszar roboczy/miejsce na kopie zapasowe, oczekiwanie na ponowne uruchomienie i konkurencyjne instalatory. Wywyższony pracownik powtarza je. Konkurencyjne procesy nigdy nie są zatrzymywane automatycznie. Natywna kopia zapasowa bazy danych profilu NVIDIA musi zakończyć się pomyślnie przed rozpoczęciem instalacji NVIDIA; Eksport magazynu sterowników stanowi osobną kopię zapasową.

**Możliwości wielokrotnego użytku:** przewodnik po komponentach zawiera cztery pytania dotyczące gier, dźwięku, NVIDIA App i nagrywania. Przejrzyj jego sugestie; wymagane, nieznane i zależne komponenty pozostają chronione. Eksportuj preferencje, a następnie przeglądaj je i ponownie sprawdzaj w odniesieniu do wybranego pakietu podczas importowania. Zgody, operacje ponownego uruchomienia, ścieżki programów i ładunki poprawek nie są importowane.

**Zestaw sterowników:** wyeksportuj `.nvdfkit.zip`, aby zachować oryginalny podpisany instalator NVIDIA, opcje, skróty i instrukcje razem. Noś `NVDriverForge.exe` osobno. Zaimportuj zestaw w Narzędziach, przejrzyj podgląd, a następnie wykonaj normalny proces instalacji. To nie jest wąski sterownik ani zmodyfikowany samodzielny instalator. Opcjonalny NVENC nadal wymaga pobrania i uzyskania zgody na konkretny sterownik. Warunki redystrybucji NVIDIA nadal obowiązują.

**Wyniki i wsparcie:** przeczytaj krótki wynik i rozwiń szczegóły poszczególnych etapów/opcji. Pomyślny odczyt pozwala ustalić przechowywaną wartość, a nie zmierzoną poprawę. Lokalny raport pomocy technicznej JSON wykorzystuje pola z listy dozwolonych, w tym ostatnie zapisane zadanie po ponownym uruchomieniu aplikacji. Wyświetl podgląd przed zapisaniem lub udostępnieniem. Nie zawiera surowych dzienników, treści profili ani identyfikatorów sprzętu i nigdy nie jest przesyłany automatycznie.

**Odzyskiwanie:** postępuj zgodnie z instrukcją dotyczącą zadania chronionego, aby odzyskać sterownik z kopii zapasowej. Jawne przywrócenie profilu wymaga oryginalnej wersji sterownika i tych samych procesorów graficznych; zastępuje całą bazę danych, zachowuje bieżącą kopię oraz sprawdza skróty i stan konfliktu. Nie usuwaj jego dziennika ani nie wymuszaj niezgodności. Prawdziwa instalacja sterowników, pełne odzyskiwanie i import profilu natywnego za pomocą tego nowego przepływu pracy pozostają niesprawdzone w prawdziwym systemie.

**Aktualizacje aplikacji:** przeczytaj uwagi do wydania, a następnie wybierz plik do pobrania zweryfikowany za pomocą SHA-256. Domyślnie sprawdzanie odbywa się ręcznie, z opcjonalnym sprawdzeniem przy uruchomieniu. Żaden instalator nie jest uruchamiany automatycznie. Ta funkcja jest niezależna od sprawdzania aktualizacji sterowników i opcjonalnego zadania sprawdzania sterowników zainstalowanej wersji.

<a id="screenshots"></a>
## Zrzuty ekranu

![Podgląd strony sterownika NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Istniejący render 0.1.2 w języku francuskim z przykładowymi danymi; zachowane jako podgląd interfejsu. Wyświetlany sterownik 699.99 jest urządzeniem testowym, a nie rzeczywistą wersją do pobrania. [Pochodzenie obrazu](../assets/README.md).

<a id="update-and-uninstall"></a>
## Zaktualizuj i odinstaluj

Zamknij NVDriverForge, uzyskaj następny oficjalny pakiet i zweryfikuj jego skrót. Użyj tej samej tożsamości instalatora dla zainstalowanej aktualizacji; zastąp zamknięty przenośny plik EXE nowym. Zachowaj ustawienia i chronione zadania.

Uninstall z Windows **Installed apps**. Usuwa aplikację i jej zadanie aktualizacji, a nie sterownik NVIDIA. Ustawienia, dzienniki i kopie zapasowe pozostają. W razie potrzeby przywróć zmiany zaawansowane/NVENC poprzez udokumentowaną procedurę odzyskiwania **przed** usunięciem aplikacji. Przywracanie odrzuca sprzeczne zmiany z innego narzędzia.

Dane lokalne znajdują się pod `%LOCALAPPDATA%\NVDriverForge`; chronione zadania i eksport sterowników znajdują się pod `%PROGRAMDATA%\NVDriverForge\Jobs`. Użycie przenośne tworzy również dane lokalne. Eksport do magazynu sterowników i kopia zapasowa profilu natywnego to odrębne kwestie. Nie jest to również obraz systemu.

<a id="known-limitations"></a>
## Znane ograniczenia

- Żadnych dodatków sprzętowych/edycji INF, regenerowanych podpisów NVIDIA, rezygnacji zgodnej z ochroną przed oszustwami lub automatycznego akceptowania ostrzeżeń bez podpisu.
- Brak całkowitego usuwania danych telemetrycznych/reklam, eksportu niewielkich pakietów lub automatycznego pełnego przywracania poprzedniego sterownika.
- Instalacja sterowników, odzyskiwanie rozruchu i opcjonalne zapisy profili nie zostały kompleksowo sprawdzone na rzeczywistych komputerach w ramach audytu centrum.
- Odczyt rejestru nie jest dowodem rzeczywistego wpływu HDCP, wydajności lub opóźnień.
- Sprawdzanie podpisu wykorzystuje lokalnie dostępne zaufanie Windows; anulowanie online nie jest wykonywane.
- Dostępne są 34 języki, ale pełne testy dotyczące native speakerów/dostępności pozostają niekompletne.

<a id="troubleshooting"></a>
## Rozwiązywanie problemów

| Objaw | Akcja |
| --- | --- |
| Katalog online niedostępny | Wybierz oryginalny pakiet z [Pobieranie sterowników NVIDIA](https://www.nvidia.com/en-us/drivers/). Nie zastępuj sąsiedniego modelu GPU. |
| Wyszukiwanie poprawek jest niedostępne | Użyj [Forum sterowników NVIDIA Game Ready](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) i sprawdź rzeczywisty pakiet. |
| Instalacja NVIDIA nie powiodła się | Przeczytaj podsumowanie awarii i otwórz szczegółowe logi. Opcjonalne komponenty, które są już aktualne lub nie mają zastosowania, można pominąć w 0.1.4. Nieudane instalacje nie powodują wprowadzenia opcjonalnych poprawek ani pomyślnego uruchomienia/ponownego uruchomienia. |
| Błąd podpisu/haszu/kopii zapasowej | Zatrzymaj tę instalację i zachowaj błąd; uzyskaj ponownie oryginalne opakowanie, jeśli jest uszkodzone. |
| Opcja niedostępna | Przeczytaj przyczynę dotyczącą sprzętu, komponentu lub sterownika docelowego; zachowaj to bez zmian. |
| Uruchom ponownie lub zadanie nadal oczekuje na realizację | Skorzystaj z instrukcji przywracania pracy i wyraźnego CV; nie usuwaj jego dziennika. |
| Przywróć konflikt | Inny stan różni się od zarejestrowanej transakcji. Zachowaj go i poproś o pomoc, zamiast wymuszać przywracanie. |

W przypadku raportów uwzględnij wybraną wersję narzędzia, Windows, GPU, sterownik i powtarzalne kroki; redaguj ścieżki i dane osobowe z logów. [Wsparcie](../docs/support.md).

<a id="faq"></a>
## Często zadawane pytania

**Czy Instalator instaluje sterownik karty graficznej?** Nie. Wymaga to osobnej analizy, przeglądu, potwierdzenia i zaawansowanego procesu instalacji aplikacji.

**Czy potrzebuję NVCleanstall lub NVPI?** Nie. NVCleanstall to tylko inspiracja. Towarzysz Profile Inspector jest niezależnym, opcjonalnym edytorem.

**Czy dzięki temu każdy sterownik NVIDIA jest mniejszy lub szybszy?** Nie. Wybrane komponenty i wymagania wstępne określają, co można zmienić; nie obiecuje się żadnego wymiernego zysku.

**Gdzie są źródła?** Specyficzne dla aplikacji testy źródłowe i prywatne są prowadzone oddzielnie. To centrum udostępnia dokumentację, pliki binarne i linki do źródeł stron trzecich wymagane do uznania/licencjonowania.

<a id="credits-and-upstream"></a>
## Kredyty i upstream

Oryginalna aplikacja, przepływ pracy, transakcje, lokalizacja, bootstrap i adaptacje: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspiracja w zakresie przepływu pracy; nie importowano żadnych źródeł ani plików binarnych.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): motywy MIT, rozszerzony interfejs NVAPI i oddzielnie pakowany fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): niezmodyfikowane narzędzia do ekstrakcji.
- [Microsoft .NET](https://github.com/dotnet/runtime) i [WPF](https://github.com/dotnet/wpf): pakiet środowiska wykonawczego.
- [Inno Setup](https://jrsoftware.org/isinfo.php): oryginalny silnik instalatora i przypisane tłumaczenia.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): zewnętrzne opcjonalne źródło danych NVENC; nie ustanowiono licencji na redystrybucję.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): pobranie zewnętrznego sterownika i zainstalowanie bibliotek NVAPI/NVML.

[Pełna tabela komponentów](../THIRD_PARTY_NOTICES.md) · [Zmiany i pochodzenie](../docs/provenance.md)

<a id="license"></a>
## Licencja

[Istniejące pozwolenie na dystrybucję binarną](../../../../NVDriverForge/LICENSE) pozwala na używanie i udostępnianie niezmodyfikowanych oficjalnych plików wykonywalnych wraz z ich powiadomieniami. Prawa źródłowe specyficzne dla aplikacji są zastrzeżone. Nie ogranicza to praw przyznanych na mocy odrębnych licencji podmiotów trzecich. [Pełne powiadomienia](LICENSES/README.md).

Niezależny od NVIDIA Corporation, TechPowerUp i keylase; nie są przez nich sponsorowane ani oficjalnie wspierane. Nazwy produktów pozostają znakami towarowymi ich właścicieli.
