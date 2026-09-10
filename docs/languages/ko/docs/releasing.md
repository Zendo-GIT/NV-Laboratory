<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · **한국어** · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# 출판 및 출시

공개 저장소는 **Zendo-GIT/NV-Laboratory**입니다. 문서 변경 사항은 **GitHub Desktop**를 사용하여 관리자에 의해 검토, 커밋 및 푸시됩니다. 로컬 커밋은 파일을 업로드하지 않습니다. 바이너리 패키지는 별도의 GitHub 릴리스 자산입니다. Git 변경 목록에 속하지 않습니다.

<a id="documentation-updates"></a>
## 문서 업데이트

1. GitHub Desktop에서 **NV-Laboratory** 폴더를 엽니다.
2. 문서, 공지, 이미지, JSON 메타데이터 및 문서 유효성 검사기를 검토하세요.
3. 해당 폴더에서 `python tools/validate_repository.py`를 실행합니다.
4. 검토된 변경 사항을 커밋한 다음 **Push origin**를 사용합니다. 작업 결과를 확인하세요.
5. 공개 작성자 ID **禅堂 Zendo (RevoluSound Team)**와 계정의 GitHub `noreply` 주소를 유지합니다.

상위 개발 작업 영역, 개인 감사 디렉터리 또는 바이너리 첨부 디렉터리를 선택하지 마세요. [이메일 개인 정보 보호 커밋](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## 독립 애플리케이션 릴리스

| 도구 | 태그 | 버전 정책 |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | 기존 4부분으로 구성된 애플리케이션 버전 설정 개정 2에는 자체 파일 이름이 있습니다. |
| NVDriverForge | nvdriverforge-v0.1.3 | 기존 0.x 방식; 버전이 지정된 업데이트는 이전 패키지를 보존합니다. |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | 새로운 애플리케이션 버전을 개발하지 않고도 정확한 해시로 식별된 UI2 후보 |
| NVRasterPulse | nvrasterpulse-v0.1 | 기존의 두 부분으로 구성된 버전 |

관리자는 직접 게시하거나 보조자에게 감사된 자산을 게시하도록 권한을 부여할 수 있습니다. 출판은 명시적입니다. 어떤 워크플로도 각 커밋에 대해 릴리스를 생성하지 않습니다.

1. 현재 사전 게시 보고서, 바이너리 소스, 라이센스 및 SHA-256 값을 검토하세요.
2. 검토된 허브 커밋을 대상으로 도구 태그의 초안을 만듭니다. 준비된 버전별 릴리스 노트를 포함합니다.
3. 해당 버전의 설정/이식 가능한 자산인 `Licenses-and-Credits.zip` 및 `SHA256SUMS.txt`만 연결합니다.
4. 호환성, 설치, 종속성, 변경 사항 및 알려진 제한 사항을 확인하세요. NVRasterPulse에 대해 RTSS를 눈에 띄게 유지하세요.
5. 공개 자산 URL, 크기 및 해시를 게시하고 확인하고 `docs/releases.json`에 실제 게시 날짜를 기록합니다.
6. 다운로드 페이지와 번역을 업데이트한 다음 GitHub Desktop에서 변경 사항을 커밋/푸시합니다.

프로젝트별 태그 링크는 공유 `releases/latest` 링크를 통해 사용자를 다른 도구로 보내는 것을 방지합니다. GitHub의 자동 **Source code** 아카이브에는 이 문서 허브가 포함되어 있습니다. 애플리케이션 소스는 비공개로 유지됩니다. 원래 구성 요소 공지는 그대로 유지되며 릴리스에서는 NVMFG의 문서화된 NVIDIA SDK 예약을 해결하지 않습니다.

<a id="integrity-and-storage"></a>
## 무결성 및 저장

게시된 바이너리 바이트를 자동으로 교체하지 마세요. 새 해시가 포함된 새로운 명시적 버전이나 설치 프로그램 개정판을 사용하세요. 법적 사이드카는 포함된 알림을 보완합니다. NVDriverForge 0.1.3 휴대용은 GitHub의 일반 100MiB Git 파일 제한보다 높은 141,760,351바이트입니다. 릴리스 첨부 파일은 이 허브에 바이너리나 Git LFS를 넣지 않도록 합니다. [GitHub 대용량 파일 지침](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

비공개 취약점 보고는 저장소 보안 설정에서 활성화되어야 합니다. 민감한 보고를 그곳으로 보내기 전에 가용성을 확인하십시오. [SECURITY.md](../SECURITY.md)는 취약점 세부정보를 노출하지 않는 대체 기능을 제공합니다.

[카탈로그 다운로드](downloads.md) · [GitHub 릴리스 문서](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
