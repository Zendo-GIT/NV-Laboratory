<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · **한국어** · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**GeForce RTX 40용 실험적 NVIDIA Multi Frame Generation, 중앙 컨트롤러 및 게임별 선택 가능**

[0.1.1 및 상태 다운로드](../docs/downloads.md#nvmfg-unlock40) · [설치](#installation) · [업스트림](#upstream-and-modifications) · [라이센스](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## 개요 및 목적

NVMFG Unlock40는 禅堂 Zendo (RevoluSound Team)가 독자적으로 개발한 애플리케이션입니다. Windows 컨트롤러, 기본 레이어, 프로필 도우미 및 게임/Streamline SDK 관리를 결합합니다. 이는 이미 NVIDIA DLSS Frame Generation 및 호환 가능한 NVIDIA 런타임을 통합한 게임을 대상으로 합니다.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock)를 참조하여 작업을 비교하고 개선했습니다. 현재 기본 레이어에는 아래에 개별적으로 표시되는 공유 및 조정된 구성 요소가 포함되어 있습니다. 이 참조는 전체 NVMFG 애플리케이션을 해당 프로젝트의 fork로 만들지 않습니다.

실험적인 MFG 동작을 중앙에서 조정하고, 게임별 선택 사항을 기억하고, 런타임 업데이트 및 백업을 계속 표시하기 위해 존재합니다. 모든 게임에 DLSS Frame Generation를 추가하거나 임의의 FSR 구현을 변환하지 않습니다.

준비된 후보는 **0.1.1**이며, 내부적으로 UI2로 기록된 SDK 목록 시각 보정을 포함합니다. 공개 버전은 0.1.1로 유지됩니다. 정확한 해시는 이 후보를 이전 로컬 빌드와 구별합니다.

<a id="features"></a>
## 특징

- 중앙 활성화/비활성화 제어 및 옵션 Windows 트레이 시작.
- Dynamic MFG, 게임 설정 및 지원되는 고정 배수 중에서 게임별로 선택합니다.
- 관찰된 V-Sync 켜기/끄기 상태에 대해 기억된 선택 항목을 구분합니다.
- Dynamic는 NVIDIA의 모드를 사용합니다. V-Sync가 꺼지면 일시 중지되며 별도의 게임 내/고정 선택이 있습니다.
- 게임 메뉴 안내 및 지속적인 제외 DLSS FG가 없는 게임은 제어 상태를 유지합니다.
- 게임 파일을 삭제하지 않고도 게임 검색, 상위 폴더 선택, 검색, 그룹화 및 제거가 가능합니다.
- Streamline SDK 다운로드/가져오기, 검증된 로컬 캐시, 명시적 선택, 게임별 백업 및 복원.
- 기본 공급자 확인, 세션별 진단, 글로벌 프로필 저널 및 충돌 인식 복구.
- 34개의 인터페이스 언어와 4개의 테마.

게임에서 FG를 끄면 계속 꺼집니다. 2x에서 6x까지의 고정 선택은 게임/메뉴/런타임에 따라 다릅니다. 모든 조합이 작동한다는 약속은 아닙니다. 컨트롤러는 V-Sync를 관찰하고 사용자에 대해 V-Sync 또는 VRR를 설정하지 않습니다.

<a id="compatibility"></a>
## 호환성

| 요구 사항 | 세부정보 |
| --- | --- |
| 시스템 | Windows 10/11 x64 |
| GPU | GeForce RTX 40 대상; 보편적인 GPU 호환성 주장 없음 |
| 게임 | 기존 NVIDIA DLSS Frame Generation 통합 및 지원되는 런타임. 치트 방지 호환성 인증 없음 |
| 공급자 | 후보자는 [출처](../docs/provenance.md)에 문서화된 공급자 SHA-256에 고정되어 있습니다. 알 수 없는 해시는 거부됩니다. |
| 런타임 | 앱/에이전트용 번들 .NET 8/WPF 8.0.30; 프로필 도우미용 .NET Framework 4.8 |
| 권한 | 컨트롤러/프로필 작업을 위한 관리자 액세스 |
| 네트워크 | 선택된 공식 SDK 다운로드에 필요합니다. 가져온 호환 SDKs를 로컬로 캐시할 수 있습니다. |
| 외부 바이너리 | NVIDIA 드라이버, NGX 공급자/모델 및 Streamline 게임 런타임은 번들로 제공되지 않습니다. |

버전 라벨만으로는 충분하지 않습니다. 드라이버, 공급자 해시, 게임 통합 및 실제 로드된 모듈이 중요합니다. 보호되거나 호환되지 않는 프로세스는 첨부를 거부할 수 있습니다. 이 애플리케이션은 치트 방지 보호 기능을 회피하도록 설계되지 않았습니다.

<a id="installation"></a>
## 설치

1. [후보자 상태 및 라이선스 노트](../docs/downloads.md#nvmfg-unlock40)를 읽어보세요.
2. 릴리스가 출시되면 `NVMFGUnlock40-0.1.1-Setup-x64.exe` 또는 `NVMFGUnlock40-0.1.1-Portable-x64.zip`를 다운로드합니다.
3. SHA-256를 확인하고 함께 제공되는 주의 사항을 유지하세요. Windows에서 아직 제공하지 않는 경우 .NET Framework 4.8를 설치하세요.
4. 설치 프로그램을 실행하거나 **전체** 휴대용 ZIP을 쓰기 가능한 로컬 폴더에 추출합니다.
5. `NVMFGUnlock40.exe`를 실행합니다. 제공된 레이아웃에서 `agent`, `driver`, `engine` 및 `Licenses`를 유지합니다.

`driver`라는 폴더에는 커널 드라이버가 아닌 사용자 공간 도우미가 포함되어 있습니다. 호환성을 강제하기 위해 기본 EXE만 복사하거나 공급자 해시를 교체하지 마십시오. 현재 EXE는 서명되지 않았습니다.

<a id="usage"></a>
## 사용법

1. 컨트롤러를 비활성화한 상태에서 시작합니다. 게임이나 상위 폴더를 추가하고 실제 설치를 선택하세요.
2. 각 게임의 MFG 설정을 검토하세요. 메뉴가 제공하는 내용에 답하세요. 답변은 게임별로 저장됩니다.
3. Dynamic 또는 게임 내 설정을 전체적으로 선택한 다음 필요에 따라 적격한 게임별 선택 사항을 조정합니다.
4. 컨트롤러를 사용하려는 경우에만 컨트롤러를 활성화하십시오. 복구 저널을 사용하여 6개의 전역 NVIDIA 프로필 설정을 일시적으로 변경할 수 있습니다.
5. 적합한 게임을 실행하고 자체 DLSS Frame Generation를 활성화합니다. V-Sync-off 선택에 대한 요청을 따르십시오.
6. 관리를 원하지 않는 게임에는 제외를 사용하세요. 게임을 제거하면 제외 항목이 기록되고 해당 파일/백업이 보존됩니다.
7. 완료되면 애플리케이션의 전체 종료/비활성화 및 복구 흐름을 사용하십시오.

기본 창을 닫으면 컨트롤러가 트레이에 남아 있을 수 있습니다. 게임에 이미 로드된 DLL은 게임이 종료될 때까지 그대로 유지됩니다. 컨트롤러를 비활성화한다고 해서 언로드가 보장되는 것은 아닙니다. 유지 관리 또는 업데이트 전에 영향을 받는 게임을 닫으십시오.

**Streamline SDKs:** NVIDIA SDK 페이지에서 공식 버전을 다운로드하거나 호환되는 로컬 SDK를 가져옵니다. 가져오기는 확인된 사본을 저장합니다. **Use this version**는 이를 선택하고 **Uninstall**는 캐시된 복사본을 제거합니다. 누락된 Streamline DLL은 표시된 소스와 함께 공식 NVIDIA SDK에서 보완될 수 있습니다. NGX 모델을 다운로드/교체하지 않습니다. 게임을 닫고 원하는 게임 업데이트를 선택한 다음 원래 백업을 유지하세요. 게임 파일을 되돌리려면 캐시의 Uninstall 버튼이 아닌 백업 복원을 사용하세요.

<a id="screenshots"></a>
## 스크린샷

![NVMFG SDK 목록 미리보기](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

기존 영어 0.1.1 인터페이스는 예제 SDK 인벤토리와 함께 렌더링됩니다. 현재 버전 목록이나 실행 중인 게임의 증거가 아닙니다. [이미지 출처](../assets/README.md).

<a id="update-and-uninstall"></a>
## 업데이트 및 제거

영향을 받는 게임을 닫습니다. 업데이트하기 전에 NVMFG를 비활성화/종료하고 보류 중인 NVIDIA 설정 복구를 해결하세요. 기존 ID로 다음 설치 프로그램을 설치하거나 새 폴더에 새 휴대용 장치를 추출하십시오. 상태/백업을 유지합니다.

제거하기 전에 애플리케이션을 통해 원하는 게임 SDK 백업 및 NVIDIA 설정을 복원한 다음 게임을 닫고 컨트롤러를 종료하십시오. 설치를 위해 Windows **Installed apps**를 사용하거나 필요한 파일을 보존한 후 닫힌 휴대용 폴더를 제거하십시오. 설치 차단을 해제하기 위해 활성 복구 저널을 수동으로 삭제하지 마십시오.

로컬 게임 런타임 백업은 `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`를 사용합니다. MFG 설정/SDK 데이터는 `%LOCALAPPDATA%\RtxMfg`를 사용합니다. 세션 출력은 애플리케이션 옆의 `Sessions` 아래에 있습니다. 이러한 파일에는 게임 경로가 포함될 수 있습니다. 수정되지 않은 상태로 게시하지 마세요.

<a id="known-limitations"></a>
## 알려진 제한사항

- 실험적인 기본 패치는 충돌이나 시각적 아티팩트를 일으킬 수 있습니다. 해결되지 않은 Bodycam 충돌이 개발 기록에 기록됩니다.
- 제어된 렌더러 테스트는 모든 게임, 드라이버 또는 치트 방지에 대한 인증이 아닙니다.
- 생성된 프레임은 새로운 입력 샘플을 생성하지 않습니다. 이 허브에서는 측정된 대기 시간이나 성능 향상을 약속하지 않습니다.
- 여러 프레임 생성 도구/오버레이가 충돌할 수 있습니다. 애플리케이션은 모든 공존 시나리오를 증명하지 않고 관찰된 모듈을 보고합니다.
- 호환성 매니페스트는 완전히 테스트된 게임 목록이 아니라 탐지 보조 도구입니다.
- 전체 NVIDIA SDK 용어와 해결되지 않은 기술 제한 제한 사항은 [출처](../docs/provenance.md)에 문서화되어 있습니다.

<a id="troubleshooting"></a>
## 문제 해결

| 증상 | 액션 |
| --- | --- |
| 지원되지 않는 제공업체 | 검증된 원본 파일을 보관하세요. 드라이버/공급자 버전 및 오류를 보고합니다. 해시 확인을 우회하지 마십시오. |
| 게임에 DLSS FG가 없습니다. | 해당 답변을 선택하고 게임을 제어하세요. 이 도구는 해당 통합을 생성할 수 없습니다. |
| 게임 충돌/아티팩트 | 게임을 종료하고 NVMFG를 비활성화하고 게임의 원래 런타임 백업이 변경된 경우 이를 사용하고 재현 가능한 세부 정보를 보고합니다. |
| SDK 목록 또는 다운로드 불가 | 공식 소스를 새로 고치고 확인하세요. 캐시된/가져온 버전은 여전히 ​​유효성 검사를 통과해야 합니다. |
| 보류 중인 NVIDIA 복구로 인해 종료/업데이트가 차단됩니다. | 복구를 사용하고 일지를 보존하십시오. 충돌을 맹목적으로 덮어쓰면 안 됩니다. |
| 제거된 게임은 재발견되지 않습니다. | 그 배제는 지속적입니다. 다시 관리하려면 명시적으로 추가하세요. |

[공유 지원 안내](../docs/support.md)는 보고서에 포함할 내용을 설명합니다.

<a id="faq"></a>
## FAQ

**NVIDIA DLL 또는 모델이 포함되어 있습니까?** 드라이버 없음, NGX 공급자/모델 또는 Streamline 런타임이 포함되어 있습니다. 명시적 SDK 다운로드는 NVIDIA에서 제공됩니다.

**Dynamic는 V-Sync가 꺼진 상태에서도 작동합니까?** 해당 상태에서는 일시 중지됩니다. 게임 내 설정을 선택하거나 해당 게임의 개별 상태에 적합한 고정 승수를 선택하세요.

**이 패키지는 ReShade/OptiScaler/FSR 패키지입니까?** 아니요. 이 패키지는 이 프로덕션 패키지의 일부로 컴파일되거나 제공되지 않습니다.

**수정된 소스는 공개됩니까?** 아니요. 컴파일된 패키지와 필수 크레딧/라이센스가 제공됩니다. 이는 제3자의 권리나 제한을 제거하지 않습니다.

<a id="upstream-and-modifications"></a>
## 업스트림 및 수정

비교 참조 및 공유 기본 구성 요소: **RTX40MFG-Unlock by Michael Robles / dashdogy**, 참조 커밋 `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [저장소](https://github.com/dashdogy/RTX40MFG-Unlock) · [원본 다운로드](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

소스 비교를 통해 공유 패치, 공급자/정책 처리, 임시 수정 및 MinHook 기반 우회 구성 요소를 식별합니다. 해당 MIT 및 BSD 알림은 유지됩니다. 전체 비교에는 프로덕션 대상 외부의 파일도 포함됩니다.

데스크탑 애플리케이션, 컨트롤러 및 SDK 관리 워크플로우는 禅堂 Zendo (RevoluSound Team)에 의해 개발되었습니다. 프로젝트 작업에는 중앙 로딩, NGX 부트스트랩 통합, 검증된 공급자 선택, 게임/V-Sync 조정 및 세션 진단이 포함됩니다. 출처 가이드는 해당 작업을 공유 구성 요소와 분리합니다. 파일 비교만으로는 작성자가 아이디어를 얻었을 때 확립되지 않습니다.

프로필 도우미는 Orbmu2k의 Profile Inspector에서 MIT NVAPI 래퍼를 채택합니다. [자세한 출처 및 구성 요소 범위](../docs/provenance.md).

<a id="credits-and-license"></a>
## 크레딧 및 라이선스

Michael Robles; Orbmu2k; Tsuda Kageyu 및 HDE 기여자 NVIDIA Corporation; Microsoft 및 기여자; Inno Setup 저자 및 번역자. 애플리케이션 개발, 통합 및 패키징: 禅堂 Zendo (RevoluSound Team).

[기존 컴파일된 패키지 공유 권한](../../../../NVMFG-Unlock40/LICENSE) 및 모든 [구성 요소 라이센스](LICENSES/README.md)는 보존됩니다. 업스트림 코드에 대한 MIT 권한은 NVIDIA SDK 용어와 다릅니다. 이를 대체할 수 있는 포괄적 라이센스는 없습니다.

NVIDIA Corporation와 독립적이고, 후원하지 않으며, 공식적으로 보증하지도 않습니다. 참조된 모든 상표는 해당 소유자의 자산으로 유지됩니다.
