<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · **Polski** · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Architektura i utrzymanie repozytorium

NV Laboratory jest publicznym **centrum dokumentacji i dystrybucji plików binarnych**. Nie zawiera źródła aplikacji. Cztery projekty zachowują oddzielne drzewa kompilacji, wersje, tożsamości i zasoby wydań. Ich prywatna historia rozwoju nie jest importowana do tego repozytorium Git.

<a id="layout"></a>
## Układ

| Lokalizacja | Cel |
| --- | --- |
| README.md / README.fr.md | Punkty wejścia w języku angielskim/francuskim |
| Cztery foldery projektu | Kompletne przewodniki i obowiązujące oryginalne powiadomienia |
| dokumenty | Pliki do pobrania, kompatybilność, pochodzenie, procedura rozwoju i wydawania |
| dokumentacja/releases.json | Sprawdzone metadane, rozmiary i skróty kandydatów/wydań |
| dokumenty/pochodzenie | Porównania plików/haszów; brak kodu aplikacji |
| licencje | Udostępniane pełne teksty stron trzecich i napisy tłumacza instalatora |
| aktywa | Istniejące sprawdzone podglądy interfejsu użytkownika i ich pochodzenie |
| .github | Wydawanie formularzy i sprawdzanie dokumentacji tylko do odczytu |
| narzędzia/validate_repository.py | Sprawdzanie granic publikacji i linków w bibliotece standardowej |

Domyślnym plikiem README GitHub pozostaje język angielski. Istniejące sąsiednie łącza `.fr.md` pozostają ważne. Dodatkowe tłumaczenia odzwierciedlają dokumentację pod `docs/languages/<code>`; selektor języka utrzymuje tę samą stronę podczas przełączania języków. Katalog `docs/languages/catalog.json` rejestruje wszystkie 34 języki i odciski palców źródeł. GitHub nie wybiera automatycznie pliku README według języka przeglądarki. Zobacz [indeks językowy i polityka tłumaczeniowa](../../README.md).

<a id="application-technologies"></a>
## Technologie aplikacji

| Program | Prywatna technologia | Dystrybucja |
| --- | --- | --- |
| NVPI fork | Współpraca z C#, WPF, .NET Framework 4.8, NVAPI/Windows | Kompletny folder przenośny i oddzielny Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; natywny bootstrap C++; Proces 7-Zip | Samodzielny przenośny plik EXE i konfiguracja |
| NVMFG Unlock40 | C#/WPF .NET 8, pomocnicy Framework 4.8, silnik C++20/MASM/MinHook | Przenośne drzewo i konfiguracja |
| NVRasterPulse | Struktura C#/WPF 4.8; Integracja profilu/przeładowania RTSS; natywny bootstrap | Przenośne drzewo i konfiguracja |

Ta publiczna kasa nie może odbudować aplikacji. Automatyczne archiwa „Source code” to migawki koncentratora. Linki do źródeł nadrzędnych nie reprezentują dokładnie prywatnego, zmodyfikowanego źródła. Publiczny CI sprawdza tylko to repozytorium.

<a id="local-checks"></a>
## Kontrole lokalne

Z katalogu głównego repozytorium:

```text
python tools/validate_repository.py
```

Python Wystarczy 3.10 lub nowszy. Kontrola odczytuje pliki, lokalne łącza Markdown, wymagane powiadomienia/łącza RTSS, metadane wersji i granice publikacji. Nie uruchamia oprogramowania, nie instaluje zależności ani nie kontaktuje się z siecią.

Przepływ pracy GitHub uruchamia tę samą kontrolę z uprawnieniami do zawartości tylko do odczytu w przypadku żądania push, pull lub ręcznego wysyłania. Checkout jest przypięty do kontrolowanego zatwierdzenia i nie utrwala poświadczeń. Nie skonfigurowano żadnego zadania wydania ani wdrożenia.

<a id="maintain-the-boundary"></a>
## Utrzymuj granicę

Zaktualizuj razem odniesienia w języku angielskim, przewodniki po języku francuskim i tłumaczenia, których to dotyczy. Zmiany merytoryczne należy oddzielać od porównań związanych wyłącznie z formatowaniem. Rejestruj rzeczywiste skróty kandydatów, referencje i licencje dotyczące wcześniejszych zatwierdzeń; nigdy nie wnioskuj o licencji na podstawie popularności projektu.

Korzystaj z nowych wersji zasobów wersji i ponownie kontroluj zmienione pliki binarne, archiwa i osadzone powiadomienia. Zachowaj prywatne kopie zapasowe poza tym repozytorium. Nie używaj publicznego przepływu pracy do importowania prywatnych źródeł aplikacji lub lokalnych folderów kompilacji.

Testy odpowiednie do zmiany funkcjonalnej aplikacji przeprowadzane w projekcie prywatnym. Nie uruchamiaj ponownie instalatorów sterowników ani nie pisz prawdziwych profili w celu aktualizacji dokumentacji. [Procedura ręcznego zwalniania](releasing.md).
