<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · **한국어** · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# 저장소 아키텍처 및 유지 관리

NV Laboratory는 공개 **문서 및 바이너리 배포 허브**입니다. 애플리케이션 소스가 포함되어 있지 않습니다. 4개의 프로젝트는 별도의 빌드 트리, 버전, ID 및 릴리스 자산을 유지합니다. 개인 개발 기록은 이 Git 저장소로 가져오지 않습니다.

<a id="layout"></a>
## 레이아웃

| 위치 | 목적 |
| --- | --- |
| README.md / README.fr.md | 영어/프랑스어 진입점 |
| 4개의 프로젝트 폴더 | 완전한 가이드 및 해당 원본 고지 사항 |
| 문서 | 다운로드, 호환성, 출처, 개발 및 출시 절차 |
| docs/releases.json | 감사된 후보/릴리스 메타데이터, 크기 및 해시 |
| 문서/출처 | 파일/해시 비교; 애플리케이션 코드 없음 |
| 라이센스 | 전체 타사 텍스트 및 설치 번역사 크레딧 공유 |
| 자산 | 기존 검토된 UI 미리보기 및 출처 |
| .github | 문제 양식 및 읽기 전용 문서 유효성 검사 |
| 도구/validate_repository.py | 표준 라이브러리 출판 경계 및 링크 확인 |

영어는 기본 GitHub README로 유지됩니다. 기존 인접 `.fr.md` 링크는 유효한 상태로 유지됩니다. 추가 번역은 `docs/languages/<code>` 문서를 반영합니다. 언어 선택기는 언어를 전환할 때 동일한 페이지를 유지합니다. 카탈로그 `docs/languages/catalog.json`는 34개 언어와 소스 지문을 모두 기록합니다. GitHub는 브라우저 언어별로 README를 자동으로 선택하지 않습니다. [언어 색인 및 번역 정책](../../README.md)를 참조하세요.

<a id="application-technologies"></a>
## 응용기술

| 프로그램 | 민간기술 | 유통 |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET 프레임워크 4.8, NVAPI/Windows 상호 운용성 | 완전한 휴대용 폴더 및 별도의 Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; 네이티브 C++ 부트스트랩; 7-Zip 프로세스 | 독립형 휴대용 EXE 및 설정 |
| NVMFG Unlock40 | C#/WPF .NET 8, 프레임워크 4.8 도우미, C++20/MASM/MinHook 엔진 | 휴대용 트리 및 설정 |
| NVRasterPulse | C#/WPF 프레임워크 4.8; RTSS 프로필/다시 로드 통합; 네이티브 부트스트랩 | 휴대용 트리 및 설정 |

이 공개 체크아웃은 애플리케이션을 다시 빌드할 수 없습니다. 자동 “Source code” 아카이브는 허브 스냅샷입니다. 업스트림 소스 링크는 정확한 개인 수정 소스를 나타내지 않습니다. 공개 CI는 이 저장소만 검증합니다.

<a id="local-checks"></a>
## 현지 점검

저장소 루트에서:

```text
python tools/validate_repository.py
```

Python 3.10 이상이면 충분합니다. 검사에서는 파일, 로컬 Markdown 링크, 필수 공지/RTSS 링크, 릴리스 메타데이터 및 게시 경계를 읽습니다. 소프트웨어를 실행하거나 종속성을 설치하거나 네트워크에 연결하지 않습니다.

GitHub 워크플로는 푸시, 풀 요청 또는 수동 디스패치 시 읽기 전용 콘텐츠 권한을 사용하여 이와 동일한 검사를 실행합니다. 체크아웃은 감사된 커밋에 고정되며 자격 증명을 유지하지 않습니다. 릴리스 또는 배포 작업이 구성되지 않았습니다.

<a id="maintain-the-boundary"></a>
## 경계를 유지하라

영어 참조, 프랑스어 가이드 및 영향을 받는 번역을 함께 업데이트합니다. 형식만 비교한 비교와는 별도로 실질적인 변경 사항을 유지하세요. 실제 후보 해시, 업스트림 커밋 참조 및 라이선스를 기록합니다. 프로젝트의 인기로 인해 라이센스를 추론하지 마십시오.

최신 버전의 릴리스 자산을 사용하고 변경된 바이너리, 아카이브 및 내장된 알림을 다시 감사하세요. 이 저장소 외부에 개인 백업을 보존하십시오. 비공개 애플리케이션 소스 또는 로컬 빌드 폴더를 가져오는 데 공개 워크플로를 사용하지 마세요.

기능적 애플리케이션 변경에 적합한 테스트는 비공개 프로젝트에서 실행됩니다. 드라이버 설치 프로그램을 다시 실행하거나 문서 업데이트를 위해 실제 프로필을 작성하지 마십시오. [수동 해제 절차](releasing.md).
