<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · **Polski** · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tłumaczenie maszynowe z języka angielskiego. Nazwy techniczne, polecenia, adresy URL i oryginalne teksty prawne zostają zachowane. Mile widziana recenzja w języku ojczystym; jeśli sformułowanie jest niejasne, zapoznaj się z odniesieniami w języku angielskim.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publikacje i wydania

Repozytorium publiczne to **Zendo-GIT/NV-Laboratory**. Zmiany w dokumentacji są sprawdzane, zatwierdzane i zatwierdzane przez opiekuna za pomocą **GitHub Desktop**. Lokalne zatwierdzenie nie przesyła plików. Pakiety binarne są oddzielnymi zasobami wersji GitHub; nigdy nie należą one do listy zmian Git.

<a id="documentation-updates"></a>
## Aktualizacje dokumentacji

1. Otwórz folder **NV-Laboratory** w GitHub Desktop.
2. Przejrzyj dokumentację, uwagi, obrazy, metadane JSON i moduł sprawdzania dokumentacji.
3. Uruchom `python tools/validate_repository.py` z tego folderu.
4. Zatwierdź sprawdzone zmiany, a następnie użyj **Push origin**. Sprawdź wynik działań.
5. Zachowaj publiczną tożsamość autora **禅堂 Zendo (RevoluSound Team)** i adres konta GitHub `noreply`.

Nigdy nie wybieraj nadrzędnego obszaru roboczego programowania, prywatnego katalogu audytu ani katalogu załączników binarnych. [Zadbaj o prywatność poczty e-mail](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Niezależne wydania aplikacji

| Narzędzie | Oznacz | Polityka wersji |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Istniejąca czteroczęściowa wersja aplikacji; wersja instalacyjna 2 ma własną nazwę pliku |
| NVDriverForge | nvdriverforge-v0.1.4 | Istniejący schemat 0.x; Wersjonowane aktualizacje zachowują wcześniejsze pakiety |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Wersja aplikacji 0.2.3; skumulowane zmiany od czasu publicznego 0.1.1 |
| NVRasterPulse | nvrasterpulse-v0.2 | Istniejąca wersja dwuczęściowa |

Opiekun może publikować bezpośrednio lub upoważnić asystenta do publikowania audytowanych zasobów. Publikacja jest wyraźna; żaden przepływ pracy nie tworzy wydania przy każdym zatwierdzeniu.

1. Przejrzyj bieżący raport przed publikacją, źródła plików binarnych, licencje i wartości SHA-256.
2. Utwórz wersję roboczą tagu narzędzia, kierując się zatwierdzonym zatwierdzeniem centrum. Dołącz przygotowane uwagi do wydania dotyczące konkretnej wersji.
3. Dołącz tylko zasoby instalacyjne/przenośne tej wersji, `Licenses-and-Credits.zip` i `SHA256SUMS.txt`.
4. Sprawdź kompatybilność, instalację, zależności, zmiany i znane ograniczenia. Zachowaj widoczny RTSS dla NVRasterPulse.
5. Opublikuj, zweryfikuj adresy URL, rozmiary i skróty zasobów publicznych oraz zapisz rzeczywistą datę publikacji w `docs/releases.json`.
6. Zaktualizuj strony pobierania i tłumaczenia, a następnie zatwierdź/wypchnij zmiany w GitHub Desktop.

Łącza znaczników poszczególnych projektów pozwalają uniknąć odsyłania użytkowników do innego narzędzia za pośrednictwem udostępnionego łącza `releases/latest`. Automatyczne archiwa GitHub **Source code** zawierają to centrum dokumentacji. Źródła aplikacji pozostają prywatne. Oryginalne uwagi dotyczące komponentów pozostają nienaruszone, a wydanie nie rozwiązuje udokumentowanej rezerwy NVIDIA SDK firmy NVMFG.


Aktualizacja z 18 września przygotowuje trzy nowe tagi; istniejąca wersja Profile Inspector pozostaje niezmieniona. Nazwy zasobów, znaczniki i `SHA256SUMS.txt` muszą pozostać dokładne, aby umożliwić sprawdzanie aktualizacji aplikacji. Publikuj normalne wydania bez flagi wydania wstępnego, aby wystawić je na kontrolę wydania stabilnego; NVMFG pozostaje eksperymentalny.

<a id="integrity-and-storage"></a>
## Integralność i przechowywanie

Nigdy po cichu nie zastępuj opublikowanych bajtów binarnych. Użyj nowej jawnej wersji lub wersji instalatora z nowymi skrótami. Prawne przyczepki boczne uzupełniają wbudowane powiadomienia. NVDriverForge Przenośny plik 0.1.4 ma 142 017 891 bajtów, więcej niż zwykły limit pliku Git wynoszący 100 MB dla GitHub. Zwolnij załączniki, unikaj umieszczania plików binarnych lub Git LFS w tym centrum. [Wskazówki dotyczące dużych plików GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

W ustawieniach zabezpieczeń repozytorium należy włączyć opcję zgłaszania podatności na ataki prywatne. Zanim skierujesz tam wrażliwe raporty, sprawdź jego dostępność; [SECURITY.md](../SECURITY.md) zapewnia rozwiązanie awaryjne, które nie ujawnia szczegółów luk w zabezpieczeniach.

[Pobierz katalog](downloads.md) · [Dokumentacja wydania GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
