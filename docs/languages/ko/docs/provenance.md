<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · **한국어** · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# 출처, 변경 및 라이선스

본 감사는 **2026-09-18**에 준비된 후보자에 대해 설명합니다. 애플리케이션 소스는 비공개로 유지됩니다. 공개 인벤토리에는 소스 코드가 아닌 파일 이름과 해시가 포함됩니다. [전체 구성 요소 공지](../THIRD_PARTY_NOTICES.md)를 참조하세요.

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

참조: Orbmu2k/nvidiaProfileInspector 커밋 `592d962cca8827efe8859461a84267755595064a`; 후보 실행 가능 버전 3.0.2.3. 참조 커밋과 fork의 어셈블리 버전은 서로 다른 식별자입니다. fork 버전에서는 업스트림 릴리스 버전이 유추되지 않습니다.

클린 컴패니언의 157개 소스/리소스 파일이 해당 커밋과 비교되었습니다. 2바이트는 동일하고 134개는 줄 끝 또는 UTF-8 BOM만 다르고 11개는 수정되었으며 10개는 비교된 업스트림 경로에 없습니다. "추가됨"은 해당 경로와 관련이 있으며 그 자체로 원저작자라는 증거는 아닙니다.

[완전한 파일/해시 비교](../../../provenance/nvpi-source-provenance.json).

| 면적 | 상속받은 작품 | Fork 기여 |
| --- | --- | --- |
| 프로필 편집자 | 프로필 모델, 가져오기/내보내기, 애플리케이션 연결 및 참조 데이터 | Screen 및 외부 도구 실행 프로그램과의 통합 |
| NVAPI | Orbmu2k의 DRS 상호 운용성 | 색상/디스플레이 관련 상호 운용성, 프로덕션 기본 로딩 제한 및 모의 제거 |
| 디스플레이 서비스 | 외부 인터페이스로서의 Windows/NVIDIA API | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | 업스트림 WPF 리소스, 팔레트 및 아이콘 | 화면 대화 상자, 15초 확인, 상태/읽기 및 도구 모음 레이아웃 |
| 런처 | 기존 앱 셸 | 별도로 설치된 RasterPulse 조회 및 실행 보호 |
| 포장 | MIT 업스트림 | 깨끗한 독립 실행형 컴패니언, 별도의 설치 프로그램/제거 프로그램, 유지된 알림 |

공개 소스 맵에는 추적성을 위한 솔루션/리소스 경로가 포함되어 있습니다. 해당 파일은 소스로 배포되지 않습니다. 개발 테스트, 모의 인터페이스 및 이전 결합 NVPI/RasterPulse 바이너리는 제외됩니다.

<a id="nvdriverforge"></a>
## NVDriverForge

독립적인 C#/.NET 8/WPF 애플리케이션; 사용자 지향 워크플로는 부분적으로 NVCleanstall에서 영감을 받았습니다. 프로덕션 페이로드에서 NVCleanstall 소스/바이너리가 식별되지 않았습니다. 해당 독점 애플리케이션의 fork로 표시되지 않습니다.

원본 프로젝트 작업에는 구성 요소 분석/선택, 보호된 설치 작업, 백업 및 트랜잭션 복구, NVIDIA 카탈로그 다운로드, 업데이트 확인, 현지화된 설명, 선택적 고급/NVENC 워크플로 및 설치 프로그램 부트스트랩이 포함됩니다.

상속/적응 구성 요소: 4개의 NVPI 테마 팔레트, 확장된 NVAPI DRS 인터페이스 참조 및 별도로 선택적인 MIT NVPI 동반 항목. Custom NV 사전 설정의 선택 UI 및 허용 목록에 있는 트랜잭션 통합은 NVDriverForge에 속합니다. 사전 설정은 공식 NVIDIA 권장 사항이 아닙니다.

7-Zip 26.03, .NET/WPF 8.0.31 및 Inno Setup는 자체 용어에 따라 사용되는 수정되지 않은 외부 구성 요소로 유지됩니다. keylase NVENC 데이터가 내장되어 있지 않습니다. 사용자가 호환 가능한 다운로드를 요청할 때 정확한 커밋 하나가 선택되고 확인됩니다. 해당 업스트림 데이터에 대해 재배포 라이센스가 설정되지 않았습니다.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40는 禅堂 Zendo (RevoluSound Team)에서 독립적으로 개발되었습니다. 관리자는 비교 및 ​​개선을 위해 RTX40MFG-Unlock를 사용했습니다. 애플리케이션 전체는 fork로 표시되지 않습니다. 이러한 구별은 현재 기본 레이어의 공유/적응 구성 요소에 대한 크레딧을 제거하지 않습니다.

비교 참조: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, `4e776d068f91b4a665425542bb005dd57cc3d891`를 커밋합니다. 프라이빗 네이티브 엔진 트리에는 48개의 비교 파일이 포함되어 있습니다. 35개의 형식만 다른 파일, 4개의 수정된 파일, 9개는 참조 경로에 없습니다. [완전한 비교](../../../provenance/nvmfg-source-provenance.json).

수정된 상속 파일: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. 추가 경로에는 `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` 및 유지된 업스트림 라이센스가 포함됩니다.

프로덕션 C++ 장치: 패치 프로그램, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection 및 vsync_observer; 게다가 entry_detour 어셈블리 및 MinHook 버퍼/후크/트램펄린/HDE64. 상속된 ReShade 프런트엔드, 레거시 심 리소스 및 사용되지 않은 CMake 대상은 이 프로덕션 컴파일의 일부가 아닙니다.

일치 구성 요소에는 패치/공급자 정책 및 임시 작업이 포함됩니다. 저작권 및 허가 고지는 그대로 유지됩니다. 중앙 NGX/부트스트랩/컨트롤러 조정, 게임별 V-Sync 처리, 세션 진단 및 Windows 애플리케이션/SDK/백업 워크플로는 禅堂 Zendo (RevoluSound Team)의 프로젝트 작업입니다. 위의 개수는 저작자 비율이나 두 프로젝트 아이디어의 연대순이 아니라 제3자 파일과 미사용 파일을 포함한 파일을 나타냅니다.

도우미는 프로젝트 작성 프로필 논리를 사용하여 NVPI의 NvapiDrsWrapper 및 NativeArrayHelper를 별도의 어셈블리로 조정합니다. 이전 개발 모의 경로는 제외됩니다. 공유 패밀리 팔레트는 NVPI에서 시작됩니다.

MinHook 참조: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; 상속된 컴파일된 하위 집합에는 비교 시 기능적 로컬 변경 사항이 없습니다. Streamline 통합 헤더: 2.12; 오픈 헤더 라이센스는 v2.12.0에서 확인되었습니다. NGX 헤더 소스: NVIDIA/DLSS는 `a291cc7d2cc642a51566f3dfd5376f635cd1b284`를 커밋합니다.

후보 엔진 SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`의 필수 공급자 SHA-256. 보고된 310.9 공급자 제품군은 이 정확한 해시와 호환되지 않습니다. 공급자 DLL이나 모델은 포함되어 있지 않습니다.

**뛰어난 라이선스 포인트:** 전체 NVIDIA RTX SDK 라이선스(2024년 3월 14일 버전)에는 기술적 제한 사항 우회와 관련된 섹션 4(d) 제한 사항이 포함되어 있습니다. 감사에서는 이러한 사용에 대한 허가를 설정하지 않습니다. MIT 엔진 라이센스를 유지하거나, 무료이거나, 다른 모드를 관찰한다고 해서 해당 별도의 조건이 해결되지는 않습니다. 후보자 준비는 법적 허가가 아닙니다. 원래의 짧은 헤더 공지는 전체 라이센스로 보완됩니다. 해당 Windows-1252 텍스트도 원본 바이트가 유지된 채로 읽을 수 있는 UTF-8로 제공됩니다.

0.2.3에 대해 기본 비교가 다시 계산되었습니다(동일한 48개 파일 및 분류). 이전 감사 이후 `game_selection.cpp`, `game_selection.h` 및 `patcher.cpp`는 활동/능력 관찰을 위해 변경되었습니다. 새로운 라이브러리, 진단, 기본 설정, 업데이트 및 선택 워크플로우는 관리자 애플리케이션에 속합니다. 구성 요소 라이선스와 필수 공급자 해시는 변경되지 않습니다.

<a id="nvrasterpulse"></a>
## NVRasterPulse

NVPI 파생 저장소에서 개발된 독립적인 RTSS 프로파일 관리자입니다. 상속된 MIT UI 리소스/팔레트 및 프로젝트 원본은 그대로 유지됩니다. 프로덕션 앱은 제공된 MIT 라이선스를 명시적으로 사용합니다.

프로젝트 작업: 정확한 RTSS 프로필 구문 분석/쓰기 및 분수 인코딩, 백업, 재정의 제거, 브리지 다시 로드, 필수 조건 감지, 컴팩트 UI, 트레이 수명 주기, 시작 제어 및 현지화. RTSS는 실제 제한을 수행합니다.

RTSS 소스, 후크 DLL, SDK 또는 설치 프로그램은 번들로 제공되지 않습니다. 브릿지는 사용자가 선택한 기존 RTSS 설치에서 내보내기를 호출합니다. 이 패키지에는 NVIDIA 드라이버 패키지, 기본 실험적 리미터, Framepacer, MinHook, ReShade 또는 DLSS 런타임이 없습니다.

<a id="assets-generated-data-and-tools"></a>
## 자산, 생성된 데이터 및 도구

[자산 크레딧](../assets/README.md)는 기존 인터페이스 미리보기와 NVPI 설정 선택기를 식별합니다. 그 안에 있는 가상의 값에는 라벨이 붙어 있습니다. 게임/Nexus 자산, 개인 프로필, 개인 ICC, 기업 NVIDIA 로고 또는 글꼴 파일은 복사되지 않습니다.

NVMFG에서 상속된 생성된 게임 호환성 이름은 테스트 증거가 아닌 탐지 보조 도구입니다. 생성된 설치 프로그램 카탈로그는 [번역자 공지](../../../../licenses/INSTALLER-TRANSLATORS.md)에 기록됩니다. 절대 경로가 포함된 생성된 빌드 레코드는 비공개로 유지됩니다.

프라이빗 빌드 도구에는 .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup 및 Python 감사 스크립트가 포함됩니다. 해당 컴파일러, 헤더, 테스트 실행기 및 디버그 자산은 배포되지 않습니다. 정적 릴리스 CRT는 Microsoft의 해당 도구 체인 조건에 따라 유지됩니다.

<a id="scope-of-verification"></a>
## 검증범위

로컬 감사에서는 Git 개체 데이터베이스와 연결된 디렉터리 대상을 제외하고 세 개발 루트의 모든 파일을 조사했습니다. 활성 소스/문서가 스캔되었습니다. 역사적인 빌드는 목록화되어 제외되었습니다. 선택된 ZIP과 현재 페이로드가 스캔되고 해시되었습니다. 추가 검사를 위해 .NET 번들의 압축이 풀렸습니다. 초기 감사에서는 제품, 설치 프로그램, 게임, RTSS 프로세스 또는 드라이버를 실행하지 않았습니다.

최신 NVPI 설정 개정 2에서는 공유 Inno 컨트롤 및 부트스트랩을 사용하여 독립형 언어 선택을 수정합니다. 밝은/어두운 개인 고정물은 마우스 및 키보드 탐색과 34개의 명시적인 언어 코드를 모두 확인했습니다. 실제 설정 선택기가 표시되지 않은 개인 데스크탑에서 열렸고 설치 전에 취소되었습니다. 7개의 애플리케이션 파일과 휴대용 ZIP은 변경되지 않았습니다. NVDriverForge 0.1.3에는 수정된 동반 항목이 포함되어 있으며 계속 `/LANG`를 전달합니다.

NVDriverForge 0.1.3는 2026-09-10에 완료되었습니다. 비공개 검증 보고서에는 366개의 애플리케이션 테스트, 118개의 동반 확인, 32개의 설정 확인, 156개의 네이티브 비교 및 ​​34개의 언어 전달 사례가 기록되어 있습니다. 보호된 구성 요소 선택 수정 사항은 페이로드를 변경하거나 드라이버를 설치하지 않고 원본 드라이버 패키지에 대해 재생되었습니다. 이는 이 문서 업데이트로 다시 실행된 테스트나 성공적인 실제 드라이버 설치에 대한 증거가 아닌 오래된 제품 팀 결과입니다.

이 허브 업데이트는 기능적 애플리케이션 코드를 변경하지 않습니다. 이전 애플리케이션 빌드/유닛/UI 테스트는 오래된 역사적 증거로 남아 있습니다. 이는 모든 타사 바이너리의 완전한 역엔지니어링이 아니며 가능한 모든 비밀 패턴에 대한 보장도 아닙니다.

2026년 9월 18일 업데이트: NVDriverForge 0.1.4는 준비 상태 확인, 기본 프로필 백업, 구성 요소 지침, 기본 설정 및 키트, 세부 결과, 로컬 보고 및 애플리케이션 업데이트를 추가합니다. NVRasterPulse 0.2는 새로운 리미터 엔진 없이 구성 진단, FPS 안내, 일시 중지/계속, 실행 취소, `.nvrp` 프로필 및 즐겨찾기/숨기기를 추가합니다. 개별 가이드에서는 사용법과 한도를 설명합니다. 정적 허브 확인은 9월 18일 비공개 보고서에 기록된 애플리케이션 테스트와 별개입니다. 이 허브에 대해 드라이버 설치, 실제 프로필 가져오기 또는 대기 시간 측정이 수행되지 않았습니다.
