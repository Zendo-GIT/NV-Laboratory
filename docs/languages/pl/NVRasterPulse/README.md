<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · **Polski** · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Limity FPS na aplikację poprzez RivaTuner Statistics Server.**

> **Najpierw zainstaluj RTSS.** NVRasterPulse wymaga [RivaTuner Statistics Server (RTSS), pobrany z Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). Aby wymusić ograniczenia, musi być uruchomiony RTSS. W zestawie nie ma instalatora RTSS, biblioteki hook DLL ani SDK.

[Pobierz 0.1 i status](../docs/downloads.md#nvrasterpulse) · [Instalacja](#installation) · [Jak działają limity](#usage) · [Licencja](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Przegląd i cel

NVRasterPulse to kompaktowy interfejs Windows do zarządzania limitami ramek RTSS według nazw plików wykonywalnych. RTSS wykonuje ograniczenie. NVRasterPulse zarządza odpowiednimi wartościami profili, kopiami zapasowymi i żądaniami przeładowania, z dostępem do zasobnika i stałymi wyborami.

Istnieje po to, aby ułatwić edycję dokładnych limitów dla poszczególnych gier bez konieczności wymiany całego profilu RTSS lub zakłócania ustawień jego nakładki. Obecny kandydat **0.1** to kompilacja z 9 września 2026 r. z wymaganą kontrolą instalacji RTSS.

<a id="features"></a>
## Funkcje

- Wybierz uruchomioną aplikację lub dodaj jej plik wykonywalny ręcznie.
- Zapisz limity FPS od 1 do 1000, z maksymalnie trzema miejscami po przecinku.
- Dokładne racjonalne kodowanie wprowadzonych wartości: 59.94 staje się 2997/50.
- Konfiguracja Front Edge Sync (`SyncLimiter=1`) z aktywnym oczekiwaniem (`PassiveWait=0`).
- Aktualizacje profili dla poszczególnych plików wykonywalnych, automatyczne kopie zapasowe i zapisy atomowe.
- Usunięcie zastąpień ograniczników przy zachowaniu innej zawartości profilu.
- Wykrywanie instalacji RTSS, ręczny wybór ścieżki i jawne uruchomienie/przeładowanie.
- Obsługa zasobnika z pojedynczą instancją, opcjonalnie instalowane uruchamianie, 34 języki i cztery motywy.
- Oddziel normalne akcje zakończenia i **Zakończ + RTSS**.

<a id="compatibility"></a>
## Kompatybilność

| Wymaganie | Szczegóły |
| --- | --- |
| Systemu | Windows 10/11 x64 |
| Czas wykonania | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), instalowany oddzielnie w razie potrzeby |
| Wymagane oprogramowanie | RTSS z `RTSS.exe`, pasującym katalogiem `Profiles` i obsługą kompatybilnych profili/przeładowania |
| GPU | Zgodność z RTSS określa ogranicznik; ten menedżer profili nie wymaga konkretnej generacji RTX |
| Uprawnienia | Bieżąca aplikacja żąda dostępu administratora; wybrany folder profilu RTSS musi być dostępny |
| Gry | Zależy od obsługi przechwytywania RTSS i ograniczeń każdej gry; brak gwarancji zapobiegania oszustwom |

W ramach audytu centrum nie certyfikowano żadnej konkretnej minimalnej wersji RTSS dla każdej funkcji. Użyj oficjalnej aktualnej dystrybucji i zgłoś dokładną wersję, jeśli klucz profilu/przeładowanie nie działa. Zainstalowany, ale zatrzymany RTSS pomyślnie przeszedł kontrolę instalacji; należy go następnie uruchomić w celu faktycznego ograniczenia.

<a id="installation"></a>
## Instalacja

1. **[Pobierz i zainstaluj RTSS z Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Otwórz [Pobieranie NVRasterPulse](../docs/downloads.md#nvrasterpulse) i sprawdź dostępność wersji.
3. Pobierz `NVRasterPulse-0.1-win-x64-Setup.exe` lub `NVRasterPulse-0.1-win-x64-portable.zip` oraz uwagi/sumy kontrolne.
4. Porównaj SHA-256. Uruchom Instalatora lub wyodrębnij cały przenośny plik ZIP do lokalnego folderu z możliwością zapisu.
5. Otwórz `NVRasterPulse.exe`. Jeśli brakuje RTSS, użyj **Pobierz RTSS**, zainstaluj go, a następnie **Sprawdź ponownie** lub wybierz `RTSS.exe` ręcznie.
6. Uruchom RTSS za pomocą normalnego skrótu lub przycisku RTSS NVRasterPulse, jeśli jest zatrzymany.

Wyłączenie opcjonalnego przypomnienia nie powoduje pominięcia sprawdzenia wymagań wstępnych. Ciche uruchomienie zasobnika Windows czeka na otwarcie głównego okna, zanim wyświetli się to sprawdzenie. Instalator instaluje tylko NVRasterPulse. Jego pliki EXE są niepodpisane.

<a id="usage"></a>
## Użycie

1. Wybierz zamierzoną uruchomioną aplikację lub przejdź do pliku EXE jej gry.
2. Wprowadź limit od 1 do 1000 FPS, w razie potrzeby łącznie z wartością ułamkową.
3. Zapisz i sprawdź raportowany wynik. NVRasterPulse aktualizuje profil RTSS tego pliku wykonywalnego i żąda ponownego załadowania.
4. Upewnij się, że RTSS działa i sprawdź zachowanie w wybranej grze.

Profile są oznaczone **nazwą pliku wykonywalnego**, na przykład `Game.exe.cfg`. Dwa różne foldery zawierające `Game.exe` mają ten sam profil RTSS; zapisanie pełnej ścieżki nie usuwa tej kolizji.

Zapisywanie wykorzystuje synchronizację Front Edge i aktywne oczekiwanie. Aktywne oczekiwanie może zwiększyć wykorzystanie CPU. Alternatywne pola `LimitTime` są neutralizowane. Istniejące komentarze, ustawienia nakładek i `EnableHooking=0` zostaną zachowane. Profil globalny RTSS nie ulega zmianie.

Użyj akcji kosza, aby usunąć przesłonięcia limitera NVRasterPulse. Nie usuwa całego profilu RTSS. Limit odziedziczony z RTSS Global lub innego narzędzia może nadal obowiązywać później.

**Zamykanie i wychodzenie:** główne okno można ukryć w zasobniku. Normalny **Zakończ** pozostawia uruchomiony RTSS i zapisane limity nienaruszone. **Zakończ + RTSS** żąda normalnego zamknięcia pasującego procesu RTSS w bieżącej sesji, czeka do ośmiu sekund i nie powoduje jego zakończenia na siłę. Zapisane limity pozostają w obu przypadkach.

Język i motyw wybiera się w aplikacji. Uruchomienie przy logowaniu Windows jest opcjonalne i przeznaczone dla zainstalowanej kopii. Przycisk informacyjny wyjaśnia typowe działania.

<a id="screenshots"></a>
## Zrzuty ekranu

![Podgląd głównego okna NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Istniejący renderowany francuski interfejs użytkownika 0.1 z przykładowymi nazwami plików wykonywalnych i wartością 176 FPS. Wyświetlany jest komunikat, że RTSS jest zatrzymany; to jest ilustracja interfejsu, a nie działający ogranicznik lub pomiar opóźnienia. [Pochodzenie obrazu](../assets/README.md).

<a id="update-and-uninstall"></a>
## Zaktualizuj i odinstaluj

Zamknij NVRasterPulse, pobierz i zweryfikuj nową wersję, a następnie uruchom instalację lub wypakuj urządzenie przenośne do nowego folderu. Zachowaj ustawienia i kopie zapasowe RTSS. Aktualizacje RTSS są oddzielne i pochodzą od Guru3D.

Aby usunąć zainstalowaną kopię, użyj Windows **Installed apps**. W przypadku wersji przenośnej zamknij, a następnie usuń wyodrębniony folder, gdy kopie zapasowe będą bezpieczne. Zapisane limity RTSS nie są usuwane podczas odinstalowywania NVRasterPulse: najpierw usuń zamierzone zastąpienia ograniczników. RTSS ma własny dezinstalator.

Stan lokalny: `%LOCALAPPDATA%\NVRasterPulse`. Automatyczne kopie zapasowe RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Na potrzeby migracji można odczytać starszą lokalizację `%LOCALAPPDATA%\RTSSProfileBridge`. Pliki te mogą zawierać osobiste ścieżki wykonywalne i nie powinny być publikowane publicznie.

<a id="known-limitations"></a>
## Znane ograniczenia

- RTSS wykonuje ograniczenie. Zapisana wartość lub pomyślne żądanie przeładowania nie jest wynikiem pomiaru czasu trwania klatki.
- Pliki wykonywalne o tej samej nazwie mają wspólny profil.
- Na wynik może mieć wpływ inny ogranicznik globalny/na grę; wyłączenie lokalnego zastąpienia nie usuwa odziedziczonego ograniczenia.
- Celowo wyłączony hak RTSS pozostaje wyłączony.
- Aktywne oczekiwanie wiąże się z kompromisem CPU/moc.
- Brak uniwersalnej gry, zabezpieczenia przed oszustwami i kompleksowej weryfikacji opóźnień.
- Wcześniejszy eksperymentalny niezależny silnik limitera nie jest kompilowany ani dostarczany.
- Automatyczne kopie zapasowe nie oznaczają interfejsu pełnego tworzenia kopii zapasowych i przywracania jednym kliknięciem.

<a id="troubleshooting"></a>
## Rozwiązywanie problemów

| Objaw | Akcja |
| --- | --- |
| Wymaganie wstępne RTSS pozostaje otwarte | Wybierz aktualny `RTSS.exe` i pasujący folder Profile, a następnie Sprawdź ponownie. |
| Limit zapisany, ale bez efektu | Uruchom RTSS; sprawdź poprawny plik EXE/profil gry, uprawnienia haka i inne ograniczenia. |
| Zapis nie powiódł się | Sprawdź uprawnienia do folderu i zachowaj wyświetlony błąd/kopię zapasową. |
| Limit pozostaje po usunięciu | Sprawdź RTSS Global i inne narzędzia; akcja kosza usuwa tylko przesłonięcia lokalnych ograniczników. |
| Dwie gry mają ten sam limit | Sprawdź, czy nazwy ich plików wykonywalnych są identyczne. |
| Zakończ + RTSS pozostawia RTSS otwarty | Zamknij normalnie RTSS samodzielnie; to polecenie celowo pozwala uniknąć wymuszonego zakończenia. |

Jeśli ręcznie przywracasz kopię zapasową RTSS, najpierw zamknij RTSS i zachowaj bieżący profil przed zastąpieniem go zamierzoną kopią zapasową. Może to zastąpić niepowiązane zmiany w profilu; sprawdź plik i datę. [Wspólne wsparcie](../docs/support.md).

<a id="faq"></a>
## Często zadawane pytania

**Czy potrzebuję także MSI Afterburner?** NVRasterPulse wymaga RTSS; nie zależy to od aplikacji Afterburner. Postępuj zgodnie z opcjami instalacji dystrybutora RTSS.

**Czy mogę używać tego bez uruchomionego RTSS?** Możesz zarządzać profilami po wykryciu instalacji, ale RTSS musi działać w celu ograniczenia.

**Czy zamknięcie lub odinstalowanie powoduje usunięcie wielkich liter?** Nie. Przed usunięciem NVRasterPulse należy wyraźnie usunąć żądane zastąpienia ograniczników.

**Czy jest to fork czy RTSS?** Nie. Jest to niezależny menedżer profili; nie dołączono źródła ani pliku wykonywalnego RTSS.

<a id="upstream-modifications-and-credits"></a>
## Upstream, modyfikacje i napisy

Repozytorium rozwojowe pochodzi z [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Zasoby palet/interfejsu MIT są uznane. Usługi zarządzania profilami, kodowanie frakcji, kopie zapasowe, mostek przeładowania RTSS, zachowanie zasobnika, przewodnik po wymaganiach wstępnych, języki i ikona specyficzna dla aplikacji zostały opracowane/zaadaptowane przez 禅堂 Zendo (RevoluSound Team).

RTSS został opracowany przez **Unwinder** i dystrybuowany oddzielnie przez Guru3D. NVRasterPulse wywołuje `UpdateProfiles` z wybranej zainstalowanej biblioteki DLL haka; nie RTSS SDK lub plik binarny przechwytujący jest redystrybuowany. Instalator używa niezmodyfikowanego Inno Setup 7.1.0 z dostosowanymi skryptami/tłumaczeniami i bootstrapem projektu.

[Pełne pochodzenie](../docs/provenance.md) · [Tabela innej firmy](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licencja

Pakiet wyraźnie rozpowszechnia NVRasterPulse w ramach dostarczonego [Licencja MIT](../../../../NVRasterPulse/LICENSE), zachowując prawa autorskie (c) 2016 Orbmu2k. Źródło aplikacji jest utrzymywane prywatnie; MIT nie wymaga publikacji zmodyfikowanego źródła. RTSS i Windows/.NET podlegają własnym warunkom. [Pełne powiadomienia](LICENSES/README.md).

Niezależny od NVIDIA Corporation, MSI i RTSS; nie są przez nich sponsorowane ani oficjalnie wspierane. Nazwy produktów pozostają znakami towarowymi ich właścicieli.
