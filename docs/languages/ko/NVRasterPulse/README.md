<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · **한국어** · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**애플리케이션별 FPS는 RivaTuner Statistics Server를 통해 제한됩니다.**

> **RTSS를 먼저 설치하세요.** NVRasterPulse에는 [RivaTuner Statistics Server(RTSS), Guru3D에서 다운로드](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)가 필요합니다. 제한을 적용하려면 RTSS를 실행해야 합니다. RTSS 설치 프로그램, 후크 DLL 또는 SDK는 번들로 제공되지 않습니다.

[0.2 및 상태 다운로드](../docs/downloads.md#nvrasterpulse) · [설치](#installation) · [한도 작동 방식](#usage) · [라이센스](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## 개요 및 목적

NVRasterPulse는 실행 파일 이름별로 RTSS 프레임 제한을 관리하기 위한 컴팩트 Windows 인터페이스입니다. RTSS가 제한을 수행합니다. NVRasterPulse는 트레이 액세스 및 지속적인 선택을 통해 해당 프로필 값, 백업 및 다시 로드 요청을 관리합니다.

전체 RTSS 프로필을 교체하거나 오버레이 설정을 방해하지 않고도 정확한 게임별 제한을 더 쉽게 편집할 수 있도록 하기 위해 존재합니다. 버전 **0.2**에는 구성 진단, FPS 도우미, 일시 중지, 실행 취소 및 프로필 공유가 추가되었습니다.

<a id="features"></a>
## 특징

- 실행 중인 애플리케이션을 선택하거나 해당 실행 파일을 수동으로 추가하세요.
- FPS 제한을 1부터 1000까지(소수점 최대 3자리까지) 저장합니다.
- 입력된 값의 정확한 유리수 인코딩: 59.94는 2997/50이 됩니다.
- 활성 대기(`PassiveWait=0`)가 포함된 전면 Edge 동기화 구성(`SyncLimiter=1`).
- 실행 가능한 프로필별 업데이트, 자동 백업 및 원자성 쓰기.
- 다른 프로필 콘텐츠를 유지하면서 리미터 재정의를 제거합니다.
- RTSS 설치 감지, 수동 경로 선택 및 명시적 시작/다시 로드.
- 단일 인스턴스 트레이 작동, 선택적 설치 시작, 34개 언어 및 4개 테마.
- 일반 종료와 **Quit + RTSS** 작업을 분리하세요.

<a id="compatibility"></a>
## 호환성

| 요구 사항 | 세부정보 |
| --- | --- |
| 시스템 | Windows 10/11 x64 |
| 런타임 | [.NET 프레임워크 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), 필요한 경우 별도로 설치 |
| 필수 소프트웨어 | `RTSS.exe`가 포함된 RTSS, 일치하는 `Profiles` 디렉터리 및 호환되는 프로필/다시 로드 지원 |
| GPU | RTSS 호환성에 따라 리미터가 결정됩니다. 이 프로필 관리자에는 특정 RTX 세대가 필요하지 않습니다. |
| 권한 | 현재 애플리케이션은 관리자 액세스를 요청합니다. 선택한 RTSS 프로필 폴더에 액세스할 수 있어야 합니다. |
| 게임 | RTSS 후킹 지원 및 각 게임의 제한 사항에 따라 다릅니다. 치트 방지 보장 없음 |

이 허브 감사에서는 모든 기능에 대해 특정 RTSS 최소 버전이 인증되지 않았습니다. 공식 현재 배포판을 사용하고 프로필 키/다시 로드가 작동하지 않으면 정확한 버전을 보고하세요. 설치되었지만 중지된 RTSS가 설치 검사를 통과했습니다. 그런 다음 실제 제한을 위해 시작해야 합니다.

<a id="installation"></a>
## 설치

1. **[Guru3D에서 RTSS를 다운로드하여 설치합니다.](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. [NVRasterPulse 다운로드](../docs/downloads.md#nvrasterpulse)를 열고 릴리스 가용성을 확인하십시오.
3. `NVRasterPulse-0.2-win-x64-Setup.exe` 또는 `NVRasterPulse-0.2-win-x64-portable.zip`와 알림/체크섬을 다운로드합니다.
4. SHA-256를 비교해보세요. 설치 프로그램을 실행하거나 전체 휴대용 ZIP을 쓰기 가능한 로컬 폴더에 추출합니다.
5. `NVRasterPulse.exe`를 엽니다. RTSS가 누락된 경우 **RTSS 다운로드**를 사용하여 설치한 후 **다시 확인**하거나 `RTSS.exe`를 수동으로 선택하세요.
6. 일반 바로가기를 사용하여 RTSS를 시작하거나 중지된 경우 NVRasterPulse의 RTSS 버튼을 사용하여 시작합니다.

선택적 알림을 꺼도 필수 구성 요소 확인을 건너뛰지 않습니다. 자동 Windows 트레이 시작은 이 확인 표시를 표시하기 전에 기본 창이 열릴 때까지 기다립니다. 설치 프로그램은 NVRasterPulse만 설치합니다. 해당 EXE는 서명되지 않았습니다.

<a id="usage"></a>
## 사용법

1. 실행하려는 응용 프로그램을 선택하거나 해당 게임 EXE를 찾아보세요.
2. 필요한 경우 분수 값을 포함하여 1~1000 FPS 사이의 제한을 입력합니다.
3. 보고된 결과를 저장하고 확인하세요. NVRasterPulse는 해당 실행 파일의 RTSS 프로필을 업데이트하고 다시 로드를 요청합니다.
4. RTSS가 실행 중인지 확인하고 의도한 게임에서 동작을 확인합니다.

프로필은 `Game.exe.cfg`와 같은 **실행 파일 이름**으로 입력됩니다. `Game.exe`가 포함된 두 개의 서로 다른 폴더는 동일한 RTSS 프로필을 공유합니다. 전체 경로를 저장해도 이 충돌은 제거되지 않습니다.

저장에는 Front Edge Sync 및 활성 대기가 사용됩니다. 활성 대기로 인해 CPU 사용이 증가할 수 있습니다. 대체 `LimitTime` 필드가 무력화됩니다. 기존 주석, 오버레이 설정 및 `EnableHooking=0`는 유지됩니다. RTSS 글로벌 프로필은 변경되지 않습니다.

NVRasterPulse의 리미터 재정의를 제거하려면 휴지통 작업을 사용하십시오. 전체 RTSS 프로필은 삭제되지 않습니다. RTSS Global 또는 다른 도구에서 상속된 제한은 이후에도 계속 적용될 수 있습니다.

**닫기 및 종료:** 메인 창을 트레이에 숨길 수 있습니다. 일반 **종료**는 RTSS 실행 및 저장된 제한을 그대로 유지합니다. **Quit + RTSS**는 현재 세션에서 일치하는 RTSS 프로세스의 정상적인 닫기를 요청하고 최대 8초 동안 기다렸다가 강제 종료하지 않습니다. 두 경우 모두 저장된 한도가 유지됩니다.

언어와 테마는 앱에서 선택됩니다. Windows 로그인 시 시작은 선택 사항이며 설치된 복사본을 위한 것입니다. 정보 버튼은 일반적인 작업을 설명합니다.

<a id="diagnostics-and-profile-tools"></a>
## 진단 및 프로필 도구

추가 도구에 대한 작업 메뉴를 엽니다. RTSS 글로벌, 오버레이 설정 및 제외를 유지합니다.

**진단:** 로컬/유효 제한, RTSS 중지, 실행 파일 누락, 감지된 창 없음, 비활성화된 후크, 상속, 일시 중지된 제한, 경쟁 설정 및 중복 실행 파일 이름을 검사합니다. 이 읽기 전용 확인은 구성을 설명합니다. 게임이 RTSS에 걸렸다는 것을 증명하거나 FPS를 측정하지 않습니다.

**FPS 도우미:** 디스플레이를 선택하고 VRR/G-Sync, V-Sync, Reflex 및 Frame Generation를 직접 선언합니다. 반올림된 새로 고침 빈도는 Windows에서 가져옵니다. Reflex 또는 Frame Generation가 활성 상태이거나 알 수 없는 경우 자동 한도가 제공되지 않습니다. V-Sync가 켜져 있고 Reflex/FG가 꺼진 VRR의 경우 휴리스틱은 최소 3개의 FPS 또는 새로 고침 빈도의 약 2%를 뺍니다. 이는 측정된 최적값이 아닙니다. 제안을 적용하면 초안이 채워집니다. **저장**은 별도의 작업으로 유지됩니다.

**일시 중지 및 재개:** 선택한 프로그램의 캡을 일시 중지한 다음 이전 리미터 필드를 복원합니다. 다른 도구의 변경 내용이 충돌하면 모호한 이력서가 방지됩니다. 항목을 숨겨도 해당 항목의 한도는 일시 중지되지 않습니다.

**실행 취소:** 해당 프로그램에 대해 관리되는 6개의 제한기 필드에 대한 마지막 변경 사항을 복원합니다. 한 가지 수준이 있습니다. 이는 RTSS를 모두 복원하지는 않습니다. 충돌하는 외부 변경은 거부됩니다. 파일 백업은 별도로 유지됩니다.

**프로필 공유:** 선택한 프로필을 `.nvrp` 파일로 내보냅니다. 가져오기는 미리보기를 표시하고 기본적으로 기존 캡을 선택하지 않은 상태로 둡니다. 파일에는 절대 경로나 스크립트 없이 실행 파일 이름, 제한 및 상태만 포함됩니다. 선택 사항을 검토하고 신청하세요. I/O 오류로 인해 일부 프로필이 이미 적용될 수 있습니다. 결과는 이를 식별하고 각각은 실행 취소를 유지합니다. 동일한 실행 파일 이름은 여전히 ​​동일한 RTSS 프로필을 처리합니다.

**즐겨찾기 및 숨겨진 항목:** 유용한 프로그램을 먼저 고정하고, 원하지 않는 항목을 숨긴 후 전용 대화상자에서 복원하세요. 이러한 선택은 지속됩니다. 닫힌 즐겨찾기는 실행 중인 애플리케이션으로 표시되지 않습니다.

<a id="screenshots"></a>
## 스크린샷

![NVRasterPulse 기본 창 미리보기](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

기존 프랑스어 0.1 UI는 예제 실행 파일 이름과 176 FPS 값을 사용하여 렌더링됩니다. RTSS는 중지된 것으로 표시됩니다. 이는 실행 중인 리미터나 대기 시간 측정이 아닌 인터페이스 예시입니다. [이미지 출처](../assets/README.md).

<a id="update-and-uninstall"></a>
## 업데이트 및 제거

NVRasterPulse를 종료하고 새 버전을 다운로드하여 확인한 다음 설치 프로그램을 실행하거나 휴대용 버전을 새 폴더에 추출합니다. 설정 및 RTSS 백업을 보존합니다. RTSS 업데이트는 별도이며 Guru3D에서 제공됩니다.

설치된 사본을 제거하려면 Windows **Installed apps**를 사용하십시오. 휴대용의 경우 백업이 안전하면 종료한 후 추출된 폴더를 제거하십시오. 저장된 RTSS 제한은 NVRasterPulse를 제거해도 제거되지 않습니다. 먼저 의도한 제한기 재정의를 제거하십시오. RTSS에는 자체 제거 프로그램이 있습니다.

로컬 상태: `%LOCALAPPDATA%\NVRasterPulse`. 자동 RTSS 백업: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. 마이그레이션을 위해 이전 `%LOCALAPPDATA%\RTSSProfileBridge` 위치를 읽을 수 있습니다. 이러한 파일에는 개인 실행 파일 경로가 포함될 수 있으므로 공개적으로 게시해서는 안 됩니다.

<a id="known-limitations"></a>
## 알려진 제한사항

- RTSS가 캡을 수행합니다. 저장된 값이나 성공적인 다시 로드 요청은 측정된 프레임 시간 결과가 아닙니다.
- 동일한 이름의 실행 파일은 프로필을 공유합니다.
- 또 다른 전역/게임별 제한이 결과에 영향을 미칠 수 있습니다. 로컬 재정의를 비활성화해도 상속된 한도는 제거되지 않습니다.
- 의도적으로 비활성화된 RTSS 후크는 비활성화된 상태로 유지됩니다.
- 활성 대기에는 CPU/전력 균형이 있습니다.
- 범용 게임, 치트 방지 또는 엔드투엔드 대기 시간 검증이 없습니다.
- 이전의 실험적 독립 리미터 엔진은 컴파일되거나 출시되지 않았습니다.
- 자동 백업은 원클릭 전체 백업-복원 인터페이스를 의미하지 않습니다.

<a id="troubleshooting"></a>
## 문제 해결

| 증상 | 액션 |
| --- | --- |
| RTSS 전제조건은 계속 열려 있습니다. | 실제 `RTSS.exe`와 일치하는 프로필 폴더를 선택한 다음 다시 확인하세요. |
| 한도가 저장되었으나 효과가 없음 | RTSS를 시작하십시오. 올바른 게임 EXE/프로필, 후크 권한 및 기타 제한 사항을 확인하세요. |
| 저장 실패 | 폴더 권한을 확인하고 표시된 오류/백업을 보존하세요. |
| 제거 후에도 한도가 남아 있음 | RTSS 글로벌 및 기타 도구를 검사합니다. 휴지통 작업은 로컬 리미터 재정의만 제거합니다. |
| 두 게임에 동일한 제한이 적용됩니다. | 실행 파일 이름이 동일한지 확인하세요. |
| Quit + RTSS는 RTSS를 열어 둡니다. | 일반적으로 RTSS를 직접 닫습니다. 이 명령은 의도적으로 강제 종료를 방지합니다. |

RTSS 백업을 수동으로 복원하는 경우 먼저 RTSS를 닫고 현재 프로필을 보존한 후 원하는 백업으로 교체하세요. 관련되지 않은 프로필 편집 내용을 덮어쓸 수 있습니다. 파일과 날짜를 검사하십시오. [공유 지원](../docs/support.md).

<a id="faq"></a>
## FAQ

**MSI Afterburner도 필요합니까?** NVRasterPulse에는 RTSS가 필요합니다. Afterburner 응용 프로그램에 의존하지 않습니다. RTSS 배포자의 설치 옵션을 따르세요.

**RTSS를 실행하지 않고 이 기능을 사용할 수 있습니까?** 설치가 감지되면 프로필을 관리할 수 있지만 제한하려면 RTSS를 실행해야 합니다.

**종료하거나 제거하면 캡이 제거됩니까?** 아니요. NVRasterPulse를 제거하기 전에 원하는 리미터 재정의를 명시적으로 제거하십시오.

**RTSS의 fork인가요?** 아니요. 독립된 프로파일 관리자입니다. RTSS 소스 또는 실행 파일이 통합되어 있지 않습니다.

<a id="upstream-modifications-and-credits"></a>
## 업스트림, 수정 및 크레딧

개발 리포지토리는 [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector)에서 시작됩니다. MIT 팔레트/UI 리소스가 인정됩니다. 프로필 관리 서비스, 분수 인코딩, 백업, RTSS 리로드 브리지, 트레이 동작, 필수 구성 요소 가이드, 언어 및 애플리케이션별 아이콘은 禅堂 Zendo (RevoluSound Team)에서 개발/적용되었습니다.

RTSS는 **Unwinder**에서 개발되었으며 Guru3D를 통해 별도로 배포됩니다. NVRasterPulse는 선택된 설치된 후크 DLL에서 `UpdateProfiles`를 호출합니다. RTSS SDK 또는 후크 바이너리가 재배포되지 않습니다. 설치 프로그램은 수정되지 않은 스크립트/번역 및 프로젝트 부트스트랩과 함께 수정되지 않은 Inno Setup 7.1.0를 사용합니다.

[완전한 출처](../docs/provenance.md) · [타사 테이블](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## 라이센스

패키지는 제공된 [MIT 라이센스](../../../../NVRasterPulse/LICENSE)에 따라 NVRasterPulse를 명시적으로 배포하며 Copyright (c) 2016 Orbmu2k를 유지합니다. 애플리케이션 소스는 비공개로 유지됩니다. MIT에서는 수정된 소스를 게시할 필요가 없습니다. RTSS 및 Windows/.NET은 자체 조건을 따릅니다. [전체 공지](LICENSES/README.md).

NVIDIA Corporation, MSI 및 RTSS와 독립적입니다. 후원하거나 공식적으로 승인하지 않았습니다. 제품 이름은 해당 소유자의 상표로 유지됩니다.
