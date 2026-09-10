<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · **Polski** · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Niezależny fork od [NVIDIA Profile Inspector autorstwa Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), z dodatkowymi elementami sterującymi wyświetlaniem.** Poprzednia nazwa projektu: **NVPI Custom**.

[Stan pobierania i wydania](../docs/downloads.md#nvidia-profile-inspector) · [Instalacja](#installation) · [Upstream i zmiany](#upstream-and-changes) · [Licencja](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Przegląd

Aplikacja edytuje profile sterowników NVIDIA, w tym ustawienia poszczególnych aplikacji. Ten fork dodaje także edytor **Ekranu** dla aktywnego wyświetlacza Windows: rozdzielczość, częstotliwość odświeżania, ustawienia kolorów wyjściowych, HDR i zainstalowane powiązania profili ICC/WCS.

Istnieje po to, aby przenieść powiązane elementy sterujące wyświetlaniem do edytora profili i sprawić, że podgląd, potwierdzenie i wyniki przywracania będą wyraźniejsze. Nie ustanawia nowych możliwości sprzętowych.

Pierwszym kandydatem jest **3.0.2.3**, korzystający z oczyszczonej, samodzielnej kompilacji towarzyszącej z 9 września 2026 r. Istniejący plik wykonywalny pozostaje `nvidiaProfileInspector.exe`; instalator i niektóre wewnętrzne etykiety nadal mówią `NVPI Custom NV`. Powyższy tytuł publiczny identyfikuje fork bez zmiany tożsamości instalacji i udawania, że ​​jest to oficjalna wersja Orbmu2k.

<a id="features"></a>
## Funkcje

- Przeglądanie istniejących profili nadrzędnych, powiązania aplikacji, edycja ustawień i import/eksport profilu.
- **Ekran** okna dialogowego wyświetlacza, trybu, Hz, RGB/YCbCr, głębi kolorów, zakresu i kolorymetrii.
- Sterowanie Windows HDR i wybór powiązania z zainstalowanym ICC/WCS.
- 15-sekundowy podgląd wyświetlacza z opcją **Zachowaj** / **Przywróć** i przywróceniem limitu czasu.
- Odczyt zmian trybu/HDR i zgłoszonych błędów przywracania.
- Oddzielne raportowanie HDR, SDR z ACM/WCG i głębią kolorów sygnału.
- Program uruchamiający NVRasterPulse dla kwalifikującej się oddzielnie instalowanej kopii.

<a id="compatibility"></a>
## Kompatybilność

| Wymaganie | Szczegóły |
| --- | --- |
| Systemu | Windows 10/11 x64 z kompatybilnym sterownikiem NVIDIA |
| Czas wykonania | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), dostarczany przez Windows lub instalowany osobno |
| Uprawnienia | Po otwarciu edytor żąda dostępu administratora |
| Wyświetla | Rzeczywiste tryby i kombinacje kolorów zależą od GPU, sterownika, wyświetlacza, kabla i interfejsów API Windows |
| Opcjonalne narzędzia | NVRasterPulse do zarządzania limitami RTSS; ani on, ani RTSS nie są potrzebne do edytora ekranów |
| Języki | Konfiguracja: selektor 34 języków. Edytor zachowuje istniejącą obsługę języków. |

Nie ma zweryfikowanego minimalnego minimalnego sterownika uniwersalnego ani matrycy wsparcia dla każdego GPU. Dostępne opcje bpc w oknie dialogowym to żądania, a nie certyfikowane kombinacje. Nowoczesne kontrolki HDR i starsza wersja rezerwowa Windows mają różne możliwości.

<a id="installation"></a>
## Instalacja

1. Otwórz [strona pobierania](../docs/downloads.md#nvidia-profile-inspector) i sprawdź status publikacji.
2. Pobierz plik instalacyjny lub zasób przenośny i porównaj jego SHA-256 z manifestem wydania.
3. W celu instalacji uruchom `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, wybierz język i postępuj zgodnie z instrukcjami instalatora. Tworzy własny skrót i dezinstalator.
4. W przypadku urządzeń przenośnych wyodrębnij cały plik ZIP do nowego folderu z możliwością zapisu. Zachowaj `Reference.xml`, konfigurację EXE i wszystkie uwagi obok pliku wykonywalnego.
5. Uruchom `nvidiaProfileInspector.exe`.

Sama instalacja edytora nie powoduje zastosowania profilu ani zainstalowania sterownika GPU. Towarzysz instaluje się osobno, nie przejmuje skojarzeń `.nip` i nie umożliwia uruchomienia przy logowaniu. Istniejące pliki binarne są niepodpisane.

<a id="usage"></a>
## Użycie

**Wersja instalacyjna 2** dodaje ten sam natywny selektor 34 języków, co inne narzędzia, z nawigacją za pomocą myszy/klawiatury, wyglądem jasnym/ciemnym i anulowaniem. Wybór dotyczy konfiguracji; nie tłumaczy edytora NVPI. Jawny argument `/LANG=fr` lub tryb cichy pomijają wybór w przypadku obiektów wywołujących, które już udostępniają język.

**Profile kierowców:** wybierz profil, wyeksportuj kopię zapasową, a następnie edytuj tylko zamierzone ustawienia i zastosuj je. Powiązania aplikacji określają, która gra otrzyma profil. Zapisana wartość nie jest dowodem na to, że każdy sterownik lub gra z niej korzysta.

**Sterowanie wyświetlaczem:** otwórz **Ekran**, wybierz wyświetlacz i żądane wartości, a następnie rozpocznij podgląd. Sprawdź zdjęcie, zanim w ciągu 15 sekund wybierzesz **Zachowaj**. Użyj **Przywróć**, zamknij potwierdzenie lub poczekaj, aż wygaśnie, aby poprosić o przywrócenie. Przeczytaj każdy komunikat o błędzie: samo pomyślne wywołanie API nie jest dowodem przywrócenia.

Wybór ICC zmienia zainstalowane powiązanie profilu; nie generuje, nie kalibruje ani nie rozpowszechnia pliku ICC. HDR, ACM/WCG, RGB/YCbCr i bpc opisują różne aspekty rurociągu. Nie jest dostępny żaden nowy niezależny przełącznik ACM.

**NVRasterPulse:** przycisk na pasku narzędzi akceptuje oddzielnie zarejestrowaną instalację w całym systemie poniżej plików programów z chronioną własnością i uprawnieniami. Przenośna kopia lub ścieżka zapisywana przez użytkownika/połączona może zostać odrzucona przez ten program uruchamiający z podwyższonym poziomem uprawnień. W takim przypadku otwórz NVRasterPulse za pomocą własnego skrótu. [Zainstaluj oddzielnie RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/), aby użyć NVRasterPulse.

<a id="screenshots"></a>
## Zrzuty ekranu

![Wybór języka konfiguracji NVPI wersja 2](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Rzeczywisty selektor konfiguracji w języku francuskim, zarejestrowany podczas izolowanego testu, a następnie anulowany. To pokazuje instalatora; edytor zachowuje swój interfejs i okno dialogowe na ekranie.

<a id="update-and-uninstall"></a>
## Zaktualizuj i odinstaluj

Zamknij edytor przed aktualizacją. Zachowaj wyeksportowane profile i pobierz nową wersję fork; zainstaluj na tej samej tożsamości towarzyszącej lub wyodrębnij pliki przenośne do nowego folderu. Nie mieszaj starego `Reference.xml` z nowym plikiem wykonywalnym. Dołączone tłumienie sprawdzania aktualizacji upstream należy do tego fork.

Aby zainstalować kopię, użyj Windows **Installed apps** i jego dezinstalatora. W przypadku wersji przenośnej zamknij go i usuń wyodrębniony folder, gdy eksport będzie bezpieczny. Usunięcie edytora **nie** cofa zmian w profilu kierowcy, preferencjach wyświetlania, NVRasterPulse lub RTSS. Przywróć żądane ustawienia przed usunięciem.

<a id="known-limitations"></a>
## Znane ograniczenia

- 15-sekundowe potwierdzenie nie jest sygnałem ostrzegawczym w przypadku każdej awarii sterownika, utraty zasilania lub wymuszonego wyłączenia.
- Niektóre kombinacje kolorów/głębokości/odświeżania zwracają wartość `NVAPI_NOT_SUPPORTED`.
- Odczyt oprogramowania nie mierzy głębi bitowej panelu, dokładności kolorów ani opóźnienia.
- Ustawienia ekranu wpływają na bieżący wyświetlacz Windows; to okno dialogowe nie tworzy ustawień wyświetlania dla poszczególnych gier.
- Brak gwarancji wydajności, ochrony przed oszustwami lub uniwersalnej kompatybilności z HDR.

<a id="troubleshooting"></a>
## Rozwiązywanie problemów

| Objaw | Akcja |
| --- | --- |
| Błąd wykonania podczas uruchamiania | Sprawdź aktualizacje Windows i .NET Framework 4.8; użyj pełnego pakietu. |
| Żądany tryb wyświetlania został odrzucony | Przywróć i przetestuj tryb oferowany przez Windows/NVIDIA dla tego wyświetlacza. Przeczytaj dokładny błąd i unikaj powtarzających się zmian na ślepo. |
| HDR lub kolor powraca do starego stanu | Sprawdź, czy inna operacja nie powiodła się i nie spowodowała przywrócenia; odróżnić HDR od ACM. |
| Przycisk NVRasterPulse odrzuca ścieżkę | Uruchom własny skrót; przycisk ten wymaga chronionej instalacji obejmującej cały system. |
| Zmiana pozostaje po odinstalowaniu | Przywróć wyeksportowany profil NVIDIA lub zamierzone ustawienia wyświetlania Windows; odinstalowanie nie jest przywróceniem ustawień. |

Przed wysłaniem dzienników zobacz [wspólne wskazówki dotyczące wsparcia](../docs/support.md).

<a id="faq"></a>
## Często zadawane pytania

**Czy jest to oficjalne oprogramowanie NVIDIA czy oficjalna wersja Orbmu2k?** Nie. Jest to niezależny fork; autor źródłowy i licencja MIT pozostają zapisane.

**Czy NVDriverForge wymaga tego edytora?** Nie. Opcjonalne ustawienie wstępne Custom NV NVDriverForge wykorzystuje własną integrację. Instalacja edytora to oddzielny wybór.

**Czy RTSS jest obowiązkowy dla tego fork?** Nie. RTSS jest obowiązkowy dla ogranicznika FPS NVRasterPulse, a nie do edycji profilu lub ekranu.

**Gdzie jest źródło?** Zmodyfikowane źródło aplikacji jest przechowywane prywatnie. Udostępniono powiadomienie MIT i repozytorium nadrzędne; MIT nie wymaga publikowania zmodyfikowanego źródła.

<a id="upstream-and-changes"></a>
## Upstream i zmiany

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), zatwierdzenie odniesienia `592d962cca8827efe8859461a84267755595064a`. [Oryginalne pliki do pobrania](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Odziedziczone: edytor profili, interoperacja NVAPI, dane referencyjne, zasoby interfejsu użytkownika i motywy. 禅堂 Zendo (RevoluSound Team) dodał lub dostosował usługi wyświetlania, transakcje HDR/ICC, 15-sekundowe potwierdzenie/odczyt, układ paska narzędzi i zachowanie podczas uruchamiania RasterPulse. Oczyszczony towarzysz wyklucza makiety programistyczne/testowe punkty wejścia, korzysta z chronionego zewnętrznego programu uruchamiającego i zapewnia oddzielny instalator. Stary połączony pakiet programistyczny NVPI/RasterPulse nie jest kandydatem w tym centrum.

[Szczegółowe pochodzenie pliku](../docs/provenance.md) · [Oryginalna uwaga dotycząca fork](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Kredyty i licencja

Prawa autorskie (c) 2016 Orbmu2k. Dostarczony [Licencja MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) zostaje zachowany. Adaptacje i opakowanie: 禅堂 Zendo (RevoluSound Team). Instalator używa Inno Setup; Windows i .NET Framework pozostają zewnętrzne. [Pełne obowiązujące powiadomienia](LICENSES/README.md).

Niezależny, niesponsorowany i oficjalnie zatwierdzony przez NVIDIA Corporation. Znaki towarowe pozostają własnością ich odpowiednich właścicieli.
