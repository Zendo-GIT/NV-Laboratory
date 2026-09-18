<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · **Polski** · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Eksperymentalny NVIDIA Multi Frame Generation dla GeForce RTX 40, z centralnym kontrolerem i możliwością wyboru dla poszczególnych gier.**

[Pobierz 0.2.3 i status](../docs/downloads.md#nvmfg-unlock40) · [Instalacja](#installation) · [Pod prąd](#upstream-and-modifications) · [Licencje](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Przegląd i cel

NVMFG Unlock40 to niezależnie opracowana aplikacja przez 禅堂 Zendo (RevoluSound Team). Łączy w sobie kontroler Windows, warstwę natywną, pomocnika profilu i zarządzanie grą/Streamline SDK. Dotyczy gier, które już integrują NVIDIA DLSS Frame Generation i kompatybilne środowiska wykonawcze NVIDIA.

W celu porównania i udoskonalenia pracy skonsultowano się z [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock). Bieżąca warstwa natywna zawiera udostępnione i dostosowane komponenty, opisane poniżej. To odniesienie nie oznacza, że ​​cała aplikacja NVMFG jest fork tego projektu.

Istnieje, aby centralnie koordynować eksperymentalne zachowanie MFG, zapamiętywać wybory specyficzne dla gry i zapewniać widoczność aktualizacji i kopii zapasowych w czasie wykonywania. Nie dodaje DLSS Frame Generation do każdej gry ani nie konwertuje dowolnej implementacji FSR.

Bieżący pakiet to **0.2.3**. Dodaje trwałą bibliotekę gier, informacje o aktywności i możliwościach, lokalną diagnostykę oraz poprawione zachowanie wyboru/postępu. [Pliki do pobrania](../docs/downloads.md#nvmfg-unlock40) identyfikuje dokładne pliki i skróty.

<a id="features"></a>
## Funkcje

- Centralna kontrola włączania/wyłączania i opcjonalne uruchamianie tacy Windows.
- Wybór dla każdej gry pomiędzy Dynamic MFG, ustawieniami gry i obsługiwanymi stałymi mnożnikami.
- Oddzielne zapamiętane wybory dla zaobserwowanych stanów włączenia/wyłączenia V-Sync.
- Dynamic używa trybu NVIDIA; jest zawieszany, gdy V-Sync jest wyłączony, z oddzielnym wyborem w grze/stałym.
- Wskazówki dotyczące menu gry i trwałe wykluczenia; gry bez DLSS FG zachowują kontrolę.
- Wykrywanie gier, wybór folderu nadrzędnego, wyszukiwanie, grupowanie i usuwanie bez usuwania plików gry.
- Streamline Pobieranie/importowanie SDK, zweryfikowana lokalna pamięć podręczna, jawny wybór, kopia zapasowa i przywracanie dla poszczególnych gier.
- Natywna weryfikacja dostawcy, diagnostyka poszczególnych sesji, globalny dziennik profili i odzyskiwanie uwzględniające konflikty.
- 34 języki interfejsu i cztery motywy.

Wyłączenie FG w grze powoduje jego wyłączenie. Naprawiono opcje od 2x do 6x w zależności od gry/menu/czasu działania; nie stanowią one obietnicy, że każda kombinacja będzie skuteczna. Kontroler obserwuje V-Sync i nie ustawia dla użytkownika V-Sync ani VRR.

<a id="compatibility"></a>
## Kompatybilność

| Wymaganie | Szczegóły |
| --- | --- |
| Systemu | Windows 10/11 x64 |
| GPU | GeForce RTX 40 obiektów docelowych; brak zastrzeżeń do uniwersalnej kompatybilności GPU |
| Gra | Istniejąca integracja NVIDIA DLSS Frame Generation i obsługiwane środowisko wykonawcze; brak certyfikatu zgodności z zabezpieczeniami przed oszustwami |
| Dostawca | Kandydat jest przypięty do dostawcy SHA-256 udokumentowanego w [pochodzenie](../docs/provenance.md); nieznane skróty są odrzucane |
| Czas wykonania | W pakiecie .NET 8/WPF 8.0.30 dla aplikacji/agenta; .NET Framework 4.8 dla pomocników profili |
| Uprawnienia | Dostęp administratora do operacji na kontrolerze/profilu |
| Sieć | Wymagane w przypadku wybranych oficjalnych plików do pobrania SDK; zaimportowany zgodny SDKs może być buforowany lokalnie |
| Zewnętrzne pliki binarne | Sterownik NVIDIA, dostawca/modele NGX i środowiska wykonawcze gier Streamline nie są dołączone |

Sama etykieta wersji nie wystarczy: liczy się sterownik, skrót dostawcy, integracja z grą i aktualnie załadowane moduły. Procesy chronione lub niekompatybilne mogą odmówić zajęcia. Aplikacja nie została zaprojektowana tak, aby omijać zabezpieczenia przed oszustwami.

<a id="installation"></a>
## Instalacja

1. Przeczytaj [status kandydata i notatka licencyjna](../docs/downloads.md#nvmfg-unlock40).
2. Pobierz `NVMFGUnlock40-0.2.3-Setup-x64.exe` lub `NVMFGUnlock40-0.2.3-Portable-x64.zip`, gdy będzie dostępna jego wersja.
3. Sprawdź SHA-256 i zachowaj dołączone uwagi. Zainstaluj .NET Framework 4.8, jeśli Windows jeszcze go nie udostępnia.
4. Uruchom Instalatora lub wyodrębnij **cały** przenośny plik ZIP do zapisywalnego folderu lokalnego.
5. Uruchom `NVMFGUnlock40.exe`; zachowaj `agent`, `driver`, `engine` i `Licenses` w dostarczonym układzie.

Folder o nazwie `driver` zawiera pomoce przestrzeni użytkownika, a nie sterownik jądra. Nie kopiuj tylko głównego pliku EXE ani nie zastępuj skrótu dostawcy, aby wymusić zgodność. Obecne pliki EXE są niepodpisane.

<a id="usage"></a>
## Użycie

1. Zacznij od wyłączonego kontrolera. Dodaj grę lub folder nadrzędny i wybierz rzeczywiste instalacje.
2. Przejrzyj ustawienia MFG każdej gry. Odpowiedz, co oferuje jego menu; odpowiedź jest przechowywana dla każdej gry.
3. Wybierz Dynamic lub ustawienie w grze globalnie, a następnie w razie potrzeby dostosuj odpowiednie opcje dla poszczególnych gier.
4. Włącz kontroler tylko wtedy, gdy masz zamiar go używać. Może tymczasowo zmienić sześć globalnych ustawień profilu NVIDIA za pomocą dziennika odzyskiwania.
5. Uruchom kwalifikującą się grę i włącz własny DLSS Frame Generation. Postępuj zgodnie z każdym żądaniem dotyczącym wyłączenia V-Sync.
6. Użyj wykluczeń dla gier, którymi nie chcesz zarządzać. Usunięcie gry oznacza wykluczenie i zachowanie jej plików/kopii zapasowych.
7. Po zakończeniu użyj pełnego procesu zamykania/wyłączania i odzyskiwania aplikacji.

Zamknięcie głównego okna może spowodować pozostawienie kontrolera w zasobniku. Biblioteka DLL już załadowana do gry pozostaje tam do momentu zakończenia gry; wyłączenie kontrolera nie gwarantuje rozładowania. Zamknij gry, których to dotyczy, przed konserwacją lub aktualizacjami.

**Streamline SDKs:** na stronie NVIDIA SDK pobierz oficjalną wersję lub zaimportuj kompatybilny lokalny SDK. Import przechowuje zweryfikowaną kopię; **Use this version** wybiera go, a **Uninstall** usuwa tę kopię z pamięci podręcznej. Brakujące biblioteki DLL Streamline można uzupełnić za pomocą oficjalnego pliku NVIDIA SDK, podając wskazane źródło. Nie powoduje to pobrania/zastąpienia modelu NGX. Zamknij grę, wybierz zamierzoną aktualizację gry i zachowaj jej oryginalną kopię zapasową. Aby przywrócić pliki gry, użyj przywracania kopii zapasowej, a nie przycisku Uninstall pamięci podręcznej.

<a id="library-diagnostics-and-updates"></a>
## Biblioteka, diagnostyka i aktualizacje

**Stała biblioteka:** wybierz kilka folderów z grami, w tym różne dyski, przed rozpoczęciem jednego skanowania. Postęp jest widoczny i istnieje możliwość anulowania. Po pierwszym skanowaniu lokalna pamięć podręczna przywraca bibliotekę po uruchomieniu, bez konieczności przeglądania każdego folderu gry. Odśwież, aby znaleźć zmiany lub dodaj kolejny folder. Operacje konserwacyjne nadal powodują ponowną weryfikację plików, których dotyczy problem; monitorowanie kopii zapasowych pozostaje aktywne. Pamięć podręczna jest przechowywana pod adresem `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Wybór:** Ctrl+A zaznacza wszystko, a Ctrl+D czyści aktywną kartę Gry lub Kopie zapasowe. Żadna gra nie jest wybierana automatycznie. Aktualizacje i odświeżenia aktywności nie powodują już selekcji duchów ani niespójnych zliczeń.

**Aktywność i kompatybilność:** Informacje MFG dotyczące poszczególnych gier pochodzą z obserwacji NGX bez nowej nakładki. Nie jest to fizyczna liczba wyświetlonych klatek. Obsługa Dynamic-with-V-Sync wynika z możliwości środowiska wykonawczego; nieznane możliwości nie są określane na podstawie numeru wersji. Aplikacja nie zmienia ani V-Sync, ani VRR. Gdy V-Sync jest wyłączony, Dynamic pozostaje zawieszony; wybory stałe lub kontrolowane przez grę są oddzielne.

**Następne uruchomienie:** tymczasowe wykluczenie pomija aktualizację przy następnym uruchomieniu gry i przywraca normalne zarządzanie po jej zamknięciu. Nie może usunąć biblioteki DLL już załadowanej do gry: zamknij i uruchom ponownie tę grę. Wallpaper Engine jest rozpoznawany jako aplikacja komputerowa; ta poprawka zachowuje ochronę faktycznie ignorowanych gier.

**Preferencje i obsługa:** Import/eksport preferencji wymaga ręcznego ponownego powiązania folderów z grami. Lokalna diagnostyka w sekcji Informacje filtruje prywatne informacje i raportuje dostępne kody błędów NVAPI lub kategorie konfliktów. Przejrzyj go przed udostępnieniem; nic nie jest przesyłane automatycznie.

**Aktualizacje aplikacji:** opcjonalna kontrola wyświetla informacje o wersji i oferuje oficjalną konfigurację. Jawne pobieranie jest sprawdzane pod kątem rozmiaru GitHub i metadanych SHA-256; sam inicjujesz instalację. Wersja 0.2.3 czyści także komunikaty o zakończonym postępie, zachowując jednocześnie znaczące błędy i wyniki. Dodatki te obejmują zmiany wprowadzone od wersji publicznej 0.1.1.

<a id="screenshots"></a>
## Zrzuty ekranu

![Podgląd listy NVMFG SDK](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Istniejący render interfejsu 0.1.1 w języku angielskim z przykładową inwentaryzacją SDK. Nie jest to lista aktualnych wersji ani dowód działającej gry. [Pochodzenie obrazu](../assets/README.md).

<a id="update-and-uninstall"></a>
## Zaktualizuj i odinstaluj

Zamknij gry, których to dotyczy. Przed aktualizacją wyłącz/zamknij NVMFG i rozwiąż wszelkie oczekujące odzyskiwanie ustawień NVIDIA. Zainstaluj następną instalację z istniejącą tożsamością lub wypakuj nową wersję przenośną do nowego folderu; zachowaj stan/kopie zapasowe.

Przed odinstalowaniem przywróć kopie zapasowe wybranych gier SDK i ustawienia NVIDIA za pośrednictwem aplikacji, a następnie zamknij gry i wyjdź z kontrolera. Użyj Windows **Installed apps** do instalacji lub usuń zamknięty folder przenośny po zachowaniu potrzebnych plików. Nie usuwaj ręcznie aktywnego dziennika odzyskiwania w celu odblokowania Instalatora.

Lokalne kopie zapasowe w czasie wykonywania gier korzystają z `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Ustawienia MFG/wykorzystanie danych SDK `%LOCALAPPDATA%\RtxMfg`; Dane wyjściowe sesji znajdują się pod `Sessions` obok aplikacji. Pliki te mogą zawierać ścieżki gry. Nie publikuj ich bez korekty.

<a id="known-limitations"></a>
## Znane ograniczenia

- Zgłoszona blokada aktywacji/przywrócenia/dezinstalacji 0.1.1 pozostaje nieodtworzona, a jej przyczyna jest nieznana. To wydanie nie ma na celu naprawienia tego problemu. W przypadku awarii zachowaj dziennik odzyskiwania i sprawdź lokalną diagnostykę; nie wymuszaj usunięcia danych odzyskiwania.
- Eksperymentalne łatki natywne mogą powodować awarie lub artefakty wizualne; nierozwiązana awaria Bodycam jest rejestrowana w historii rozwoju.
- Kontrolowane testy renderera nie stanowią certyfikacji dla każdej gry, sterownika lub zabezpieczenia przed oszustwami.
- Wygenerowane ramki nie tworzą nowych próbek wejściowych; ten koncentrator nie gwarantuje żadnych zmierzonych opóźnień ani wzrostu wydajności.
- Wiele narzędzi/nakładek do generowania klatek może powodować konflikty. Aplikacja raportuje zaobserwowane moduły bez potwierdzania każdego scenariusza współistnienia.
- Manifest zgodności jest pomocą w wykrywaniu, a nie listą w pełni przetestowanych gier.
- Pełne warunki NVIDIA SDK i nierozwiązane ograniczenia techniczne pozostają udokumentowane w [pochodzenie](../docs/provenance.md).

<a id="troubleshooting"></a>
## Rozwiązywanie problemów

| Objaw | Akcja |
| --- | --- |
| Dostawca nie jest obsługiwany | Zachowaj oryginalne zweryfikowane pliki. Zgłoś wersję sterownika/dostawcy i błąd; nie omijaj kontroli skrótu. |
| Brak DLSS FG w grze | Wybierz tę odpowiedź i pozostaw grę pod kontrolą; to narzędzie nie jest w stanie zapewnić takiej integracji. |
| Gra zawiesza się/artefakty | Wyjdź z gry, wyłącz NVMFG, użyj oryginalnej kopii zapasowej gry, jeśli została zmieniona, i zgłoś powtarzalne szczegóły. |
| Lista SDK lub pobieranie są niedostępne | Odśwież i sprawdź oficjalne źródło; wersja z pamięci podręcznej/zaimportowana musi jeszcze przejść weryfikację. |
| Oczekujące odtworzenie NVIDIA blokuje wyjście/aktualizację | Skorzystaj z odzyskiwania i zachowaj dziennik; konfliktów nie można nadpisywać na ślepo. |
| Usunięta gra nie zostanie ponownie odkryta | Jego wykluczenie jest trwałe. Dodaj go jawnie, jeśli chcesz, aby był ponownie zarządzany. |

[Wspólne wskazówki dotyczące wsparcia](../docs/support.md) wyjaśnia, co należy uwzględnić w raporcie.

<a id="faq"></a>
## Często zadawane pytania

**Czy zawiera biblioteki DLL lub modele NVIDIA?** Nie uwzględniono sterownika, dostawcy/modelu NGX ani środowiska wykonawczego Streamline. Jawne pliki do pobrania SDK pochodzą z NVIDIA.

**Czy Dynamic działa przy wyłączonym V-Sync?** W tym stanie jest zawieszony. Wybierz ustawienie w grze lub odpowiedni stały mnożnik dla osobnego stanu tej gry.

**Czy jest to pakiet ReShade/OptiScaler/FSR?** Nie. Nie są one kompilowane ani dostarczane w ramach tego pakietu produkcyjnego.

**Czy zmodyfikowane źródła są publiczne?** Nie. Udostępniane są skompilowane pakiety i wymagane kredyty/licencje. Nie usuwa to praw ani ograniczeń osób trzecich.

<a id="upstream-and-modifications"></a>
## Upstream i modyfikacje

Odniesienie porównawcze i współdzielone komponenty natywne: **RTX40MFG-Unlock autorstwa Michael Robles / dashdogy**, zatwierdzenie odniesienia `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Repozytorium](https://github.com/dashdogy/RTX40MFG-Unlock) · [Oryginalne pliki do pobrania](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Porównanie źródeł identyfikuje wspólne łatanie, obsługę dostawców/zasad, poprawki tymczasowe i komponenty objazdów oparte na MinHook. Ich powiadomienia MIT i BSD pozostają zachowane. Pełne porównanie obejmuje także pliki spoza celu produkcyjnego.

Aplikacja komputerowa, kontroler i przepływ pracy związany z zarządzaniem SDK zostały opracowane przez 禅堂 Zendo (RevoluSound Team). Prace projektowe obejmują centralne ładowanie, integrację bootstrap NGX, zweryfikowany wybór dostawcy, koordynację gier/V-Sync i diagnostykę sesji. Przewodnik po pochodzeniu oddziela te prace od wspólnych komponentów; samo porównanie plików nie pozwala ustalić, kiedy którykolwiek z autorów wpadł na ten pomysł.

Pomocnik profilu dostosowuje opakowanie MIT NVAPI z Profile Inspector Orbmu2k. [Szczegółowe pochodzenie i zakres komponentów](../docs/provenance.md).

<a id="credits-and-license"></a>
## Kredyty i licencja

Michael Robles; Orbmu2k; Współpracownicy Tsuda Kageyu i HDE; NVIDIA Corporation; Microsoft i współpracownicy; Autorzy i tłumacze Inno Setup. Tworzenie aplikacji, integracje i pakowanie: 禅堂 Zendo (RevoluSound Team).

[istniejące pozwolenie na udostępnianie skompilowanego pakietu](../../../../NVMFG-Unlock40/LICENSE) i wszystkie [licencje na komponenty](LICENSES/README.md) zostają zachowane. Uprawnienia MIT dla kodu źródłowego różnią się od warunków NVIDIA SDK. Żadna licencja ogólna ich nie zastąpi.

Niezależny, niesponsorowany i oficjalnie zatwierdzony przez NVIDIA Corporation. Wszystkie wymienione znaki towarowe pozostają własnością ich właścicieli.
