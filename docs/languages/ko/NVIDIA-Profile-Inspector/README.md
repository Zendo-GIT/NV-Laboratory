<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · **한국어** · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**디스플레이 컨트롤이 추가된 [NVIDIA Profile Inspector by Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector)의 독립적인 fork.** 이전 프로젝트 이름: **NVPI Custom**.

[다운로드 및 출시 상태](../docs/downloads.md#nvidia-profile-inspector) · [설치](#installation) · [업스트림 및 변경 사항](#upstream-and-changes) · [라이센스](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## 개요

이 응용 프로그램은 응용 프로그램별 설정을 포함하여 NVIDIA 드라이버 프로필을 편집합니다. 이 fork는 또한 활성 Windows 디스플레이를 위한 **화면** 편집기(해상도, 새로 고침 빈도, 출력 색상 설정, HDR 및 설치된 ICC/WCS 프로필 연결)를 추가합니다.

관련 디스플레이 제어를 프로필 편집기로 가져오고 미리보기, 확인 및 복원 결과를 더 명확하게 만들기 위해 존재합니다. 새로운 하드웨어 기능을 확립하지 않습니다.

첫 번째 후보는 2026년 9월 9일부터 정리된 독립 실행형 컴패니언 빌드를 사용하는 **3.0.2.3**입니다. 기존 실행 파일은 `nvidiaProfileInspector.exe`로 유지됩니다. 설치 프로그램과 일부 내부 레이블에는 여전히 `NVPI Custom NV`가 표시됩니다. 위의 공개 제목은 설치 ID를 변경하거나 Orbmu2k의 공식 릴리스인 것처럼 가장하지 않고 fork를 식별합니다.

<a id="features"></a>
## 특징

- 기존 업스트림 프로필 검색, 애플리케이션 연결, 설정 편집 및 프로필 가져오기/내보내기.
- 디스플레이, 모드, Hz, RGB/YCbCr, 색 농도, 범위 및 측색법에 대한 **화면** 대화 상자입니다.
- Windows HDR 제어 및 설치된 ICC/WCS 연결 선택.
- **유지** / **되돌리기** 및 시간 초과 복원 기능을 갖춘 15초 디스플레이 미리보기입니다.
- 모드/HDR 변경 사항을 다시 읽고 복원 실패를 보고했습니다.
- HDR, ACM/WCG가 포함된 SDR 및 신호 색상 심도를 별도로 보고합니다.
- 별도로 설치된 적격 사본에 대한 NVRasterPulse 실행 프로그램입니다.

<a id="compatibility"></a>
## 호환성

| 요구 사항 | 세부정보 |
| --- | --- |
| 시스템 | Windows 10/11 x64(호환 가능한 NVIDIA 드라이버 포함) |
| 런타임 | [.NET 프레임워크 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)(Windows에서 제공되거나 별도로 설치됨) |
| 권한 | 편집자는 열릴 때 관리자 액세스를 요청합니다. |
| 디스플레이 | 실제 모드와 색상 조합은 GPU, 드라이버, 디스플레이, 케이블 및 Windows API에 따라 다릅니다. |
| 선택적 도구 | RTSS 제한 관리용 NVRasterPulse; 화면 편집기에는 RTSS도 필요하지 않습니다. |
| 언어 | 설정: 34개 언어 선택기. 편집기는 기존 언어 지원을 유지합니다. |

모든 GPU에 대해 검증된 범용 드라이버 최소값이나 지원 매트릭스가 없습니다. 대화 상자에서 사용 가능한 bpc 선택은 인증된 조합이 아닌 요청입니다. 최신 HDR 컨트롤과 이전 Windows 대체 기능은 서로 다릅니다.

<a id="installation"></a>
## 설치

1. [다운로드 페이지](../docs/downloads.md#nvidia-profile-inspector)를 열고 게시 상태를 확인하세요.
2. 설치 또는 휴대용 자산을 다운로드하고 해당 SHA-256를 릴리스 매니페스트와 비교하세요.
3. 설치를 위해 `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`를 실행하고 언어를 선택한 후 설치 프로그램을 따르세요. 자체 바로가기와 제거 프로그램을 만듭니다.
4. 이식 가능한 경우 전체 ZIP을 쓰기 가능한 새 폴더에 추출하세요. `Reference.xml`, EXE 구성 및 실행 파일 옆의 모든 알림을 유지하세요.
5. `nvidiaProfileInspector.exe`를 실행합니다.

편집기만 설치하면 프로필이 적용되거나 GPU 드라이버가 설치되지 않습니다. 컴패니언은 별도로 설치되고 `.nip` 연결을 인계받지 않으며 로그인 시 시작을 활성화하지 않습니다. 기존 바이너리는 서명되지 않았습니다.

<a id="usage"></a>
## 사용법

**설치 프로그램 개정 2**에는 마우스/키보드 탐색, 밝게/어둡게 표시 및 취소 기능이 포함된 다른 도구와 동일한 기본 34개 언어 선택기가 추가되었습니다. 선택 사항은 설정에 적용됩니다. NVPI 편집기는 번역하지 않습니다. 명시적 `/LANG=fr` 인수 또는 자동 모드는 이미 언어를 제공하는 호출자에 대한 선택을 우회합니다.

**운전자 프로필:** 프로필을 선택하고 백업을 내보낸 다음 원하는 설정만 편집하고 적용합니다. 응용 프로그램 연결에 따라 프로필을 받을 게임이 결정됩니다. 저장된 값은 모든 드라이버나 게임이 이를 사용한다는 증거가 아닙니다.

**디스플레이 제어:** **화면**을 열고 디스플레이와 요청된 값을 선택한 다음 미리보기를 시작합니다. **유지**를 선택하기 전에 15초 이내에 이미지를 확인하세요. **되돌리기**를 사용하여 확인을 닫거나 만료되도록 하여 복원을 요청하세요. 실패 메시지를 읽으십시오. 성공적인 API 호출만으로는 복원이 증명되지 않습니다.

ICC 선택은 설치된 프로필 연결을 변경합니다. ICC 파일을 생성, 보정 또는 재배포하지 않습니다. HDR, ACM/WCG, RGB/YCbCr 및 bpc는 파이프라인의 다양한 측면을 설명합니다. 새로운 독립 ACM 스위치는 제공되지 않습니다.

**NVRasterPulse:** 도구 모음 버튼은 소유권과 권한이 보호된 프로그램 파일 아래에 별도로 등록된 시스템 전체 설치를 허용합니다. 휴대용 복사본이나 사용자 쓰기 가능/링크된 경로는 이 상승된 실행 프로그램에 의해 거부될 수 있습니다. 이 경우 자체 바로가기를 사용하여 NVRasterPulse를 엽니다. [RTSS를 별도로 설치하세요.](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) - NVRasterPulse를 사용합니다.

<a id="screenshots"></a>
## 스크린샷

![NVPI 설정 개정 2 언어 선택기](../../../../assets/screenshots/nvpi-setup-r2-language.png)

격리된 테스트 중에 캡처된 후 취소된 프랑스어로 된 실제 설정 선택기입니다. 설치 프로그램이 표시됩니다. 편집기는 인터페이스와 화면 대화 상자를 유지합니다.

<a id="update-and-uninstall"></a>
## 업데이트 및 제거

업데이트하기 전에 편집기를 닫으세요. 내보낸 프로필을 유지하고 새로운 fork 릴리스를 다운로드하세요. 동일한 컴패니언 ID 위에 설치하거나 휴대용 파일을 새 폴더에 추출하세요. 이전 `Reference.xml`를 새 실행 파일과 혼합하지 마십시오. 번들 업스트림 업데이트 확인 억제는 이 fork에 속합니다.

설치된 사본의 경우 Windows **Installed apps** 및 해당 제거 프로그램을 사용하십시오. 휴대용의 경우 내보내기가 안전할 때 닫고 추출된 폴더를 제거하십시오. 편집기를 제거해도 운전자 프로필 편집, 디스플레이 기본 설정, NVRasterPulse 또는 RTSS는 취소되지 **않습니다**. 제거하기 전에 원하는 설정을 복원하십시오.

<a id="known-limitations"></a>
## 알려진 제한사항

- 15초 확인은 모든 운전자 충돌, 정전 또는 강제 종료를 감시하는 것이 아닙니다.
- 일부 색상/깊이/새로 고침 조합은 `NVAPI_NOT_SUPPORTED`를 반환합니다.
- 소프트웨어 다시 읽기는 패널 비트 깊이, 색상 정확도 또는 대기 시간을 측정하지 않습니다.
- 화면 설정은 현재 Windows 디스플레이에 영향을 미칩니다. 이 대화 상자는 게임별 표시 사전 설정을 생성하지 않습니다.
- 성능, 치트 방지 또는 범용 HDR 호환성 보장이 없습니다.

<a id="troubleshooting"></a>
## 문제 해결

| 증상 | 액션 |
| --- | --- |
| 실행 시 런타임 오류 | Windows 업데이트 및 .NET Framework 4.8를 확인하세요. 완전한 패키지를 사용하십시오. |
| 요청된 디스플레이 모드가 거부되었습니다. | 해당 디스플레이에 대해 Windows/NVIDIA에서 제공하는 모드를 되돌리고 테스트합니다. 정확한 오류를 읽고 반복적인 맹목적 변경을 피하십시오. |
| HDR 또는 색상이 이전 상태로 돌아갑니다. | 다른 작업이 실패하여 복원이 시작되었는지 확인하세요. HDR를 ACM과 구별합니다. |
| NVRasterPulse 버튼이 경로를 거부합니다. | 자체 바로가기를 실행하세요. 이 버튼을 사용하려면 시스템 전체에 걸쳐 보호된 설치가 필요합니다. |
| 제거 후에도 변경 사항이 남아 있습니다. | 내보낸 NVIDIA 프로필 또는 의도한 Windows 디스플레이 설정을 복원합니다. 제거는 설정 롤백이 아닙니다. |

로그를 보내기 전에 [공유 지원 지침](../docs/support.md)를 참조하세요.

<a id="faq"></a>
## FAQ

**이것은 공식 NVIDIA 소프트웨어입니까, 아니면 Orbmu2k의 공식 빌드입니까?** 아니요. 독립적인 fork입니다. 업스트림 작성자와 MIT 라이센스는 그대로 유지됩니다.

**NVDriverForge에 이 편집기가 필요합니까?** 아니요. NVDriverForge의 옵션인 Custom NV 사전 설정은 자체 통합을 사용합니다. 편집기 설치는 별도의 선택입니다.

**이 fork에는 RTSS가 필수인가요?** 아니요. RTSS는 프로필이나 화면 편집용이 아닌 NVRasterPulse의 FPS 리미터에 필수입니다.

**소스는 어디에 있나요?** 수정된 애플리케이션 소스는 비공개로 유지됩니다. MIT 공지 및 업스트림 저장소가 제공됩니다. MIT에는 수정된 소스 게시가 필요하지 않습니다.

<a id="upstream-and-changes"></a>
## 업스트림 및 변경 사항

업스트림: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), 참조 커밋 `592d962cca8827efe8859461a84267755595064a`. [원본 다운로드](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

상속됨: 프로필 편집기, NVAPI interop, 참조 데이터, UI 리소스 및 테마. 禅堂 Zendo (RevoluSound Team)는 디스플레이 서비스, HDR/ICC 트랜잭션, 15초 확인/다시 읽기, 도구 모음 레이아웃 및 RasterPulse 시작 동작을 추가하거나 조정했습니다. 정리된 컴패니언은 개발 모의/테스트 진입점을 제외하고 보호된 외부 실행 프로그램을 사용하며 별도의 설치 프로그램을 제공합니다. 이전 결합 NVPI/RasterPulse 개발 패키지는 이 허브의 후보가 아닙니다.

[자세한 파일 출처](../docs/provenance.md) · [원본 fork 공지](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## 크레딧 및 라이선스

저작권(c) 2016 Orbmu2k. 제공된 [MIT 라이센스](../../../../NVIDIA-Profile-Inspector/LICENSE)는 유지됩니다. 적응 및 패키징: 禅堂 Zendo (RevoluSound Team). 설치 프로그램은 Inno Setup를 사용합니다. Windows 및 .NET Framework는 외부에 유지됩니다. [전체 해당 공지](LICENSES/README.md).

NVIDIA Corporation와 독립적이고, 후원하지 않으며, 공식적으로 보증하지도 않습니다. 상표는 해당 소유자에게 그대로 유지됩니다.
