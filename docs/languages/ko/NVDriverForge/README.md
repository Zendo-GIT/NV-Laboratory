<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · **한국어** · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**명확한 구성 요소 선택과 옵션 설정을 사용하여 NVIDIA 드라이버 설치를 준비하세요.**

[0.1.3 및 상태 다운로드](../docs/downloads.md#nvdriverforge) · [설치](#installation) · [크레딧](#credits-and-upstream) · [라이센스](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## 개요 및 목적

NVDriverForge는 원본 NVIDIA 드라이버 패키지를 안내합니다. 즉, 드라이버를 선택하고, 해당 구성 요소를 검사하고, 선택적 조정 사항을 검토한 다음 설치를 확인합니다. 이러한 선택 사항을 이해하기 쉽게 만들고 설치, 권한 있는 작업 및 복구 정보를 함께 유지하기 위해 존재합니다.

이는 NVCleanstall의 워크플로우에서 부분적으로 영감을 받아 독립적으로 개발된 애플리케이션입니다. NVCleanstall를 포함하지 않거나 완전한 기능 패리티를 요구하지 않습니다.

<a id="features"></a>
## 특징

- NVIDIA Game Ready / Studio 조회 및 다운로드; 수동 대체를 통한 선택적 핫픽스 검색.
- 원본 패키지, 해시, NVIDIA 서명, 매니페스트 및 호환 가능한 INF 항목을 분석합니다.
- 알 수 없는 구성 요소의 종속성과 보존을 통해 구성 요소 선택.
- 버전 0.1.3는 선택한 선택적 NVIDIA 구성 요소를 건너뛸 수 있도록 유지하고 확인되지 않은 확인되지 않은 구성 요소만 검색에서 제외합니다. 이미 최신이거나 적용할 수 없는 선택적 런타임은 더 이상 중요한 구성 요소로 강제되지 않습니다.
- 설치 실패 요약을 지우고 34개 언어로 된 자세한 로그에 액세스하세요.
- 명시적 설치 확인, 보호된 스테이징 및 기존 드라이버 저장소 패키지 내보내기.
- 실행 전 확인, 저널 및 충돌 인식 복구를 포함한 선택적 고급 설정입니다.
- 별도의 SILK 강도 선택 및 호환성 확인을 포함하여 이름이 지정된 선택 사항 및 설명이 포함된 옵션 **Custom NV** 사전 설정.
- 정확한 버전의 NVENC 패치 다운로드(선택 사항) 소스 커밋과 대상 바이트가 확인됩니다.
- 도구 화면에서 Profile Inspector fork를 별도로 선택적으로 설치합니다.
- 선택적 설치된 사용자 업데이트 확인, 34개 인터페이스 언어 및 4개 테마.

사용 가능한 고급 옵션에는 MPO, DLSS 표시기, Ansel, NVIDIA 오디오 절전, MSI, 인터럽트 정책/우선순위, HDCP, 디스플레이 컨테이너 시작 및 적합한 레거시 원격 측정 서비스가 포함됩니다. 각각에는 고유한 전제 조건과 효과가 있습니다. 이는 보편적인 성능 향상이 아닙니다.

<a id="compatibility"></a>
## 호환성

| 요구 사항 | 세부정보 |
| --- | --- |
| 시스템 | Windows 10 빌드 19041 이상 / Windows 11, x64 |
| GPU/드라이버 | 호환 가능한 NVIDIA 패키지 및 감지된 하드웨어; 자동 카탈로그 조회는 주로 알려진 GeForce 모델을 다룹니다. |
| 런타임 | .NET 8 / WPF 8.0.31는 준비된 자체 포함 패키지에 포함되어 있습니다. |
| 권한 | 일반 UI/사용자별 설정; 드라이버 설치 및 시스템 변경 시 관리자 액세스 요청 |
| 네트워크 | 온라인 NVIDIA 조회/다운로드 및 명시적 업스트림 NVENC 요청에 필요합니다. 로컬 원래 드라이버를 선택할 수 있습니다 |
| 포함된 도구 | 수정되지 않은 7-Zip 26.03, 런타임 알림, 옵션 MIT Profile Inspector 동반 |
| 선택적 동반자 | 별도의 Profile Inspector fork용 .NET Framework 4.8 |

모든 기능을 포함하는 임의의 최소 드라이버 버전은 없습니다. 다중 GPU 조회는 감지된 모든 GPU와 일치해야 합니다. 지원되지 않는/전문 모델에는 수동 드라이버 선택이 필요할 수 있습니다. NVIDIA의 설치 프로그램은 최종 하드웨어/OS 권한으로 남아 있습니다.

<a id="installation"></a>
## 설치

1. [다운로드](../docs/downloads.md#nvdriverforge)를 방문하여 릴리스가 게시되었는지 확인하세요.
2. 설치하려면 `NVDriverForge-Setup.exe`를 선택하고, 휴대용으로 사용하려면 `NVDriverForge.exe`를 선택하세요.
3. SHA-256를 릴리스의 `SHA256SUMS.txt`와 비교하세요.
4. 사용자별 설치 및 표준 제거 프로그램에 대해 설치 프로그램을 실행하거나 휴대용 EXE를 쓰기 가능한 폴더에 넣고 엽니다.

휴대용에는 런타임과 선택적 설치 프로그램이 포함되어 있습니다. NVDriverForge를 설치해도 GPU 드라이버는 설치되지 않습니다. 해당 EXE는 현재 서명되지 않았습니다.

<a id="usage"></a>
## 사용법

1. **드라이버:** NVIDIA에서 다운로드하거나 원본 NVIDIA 설치 프로그램 EXE를 선택하세요. 분석을 마치겠습니다.
2. **구성요소:** 설명 및 필수 종속성을 검토합니다. 알 수 없는 구성요소는 유지됩니다.
3. **조정:** 원하지 않는 옵션은 변경하지 않고 그대로 둡니다. 무엇이든 선택하기 전에 효과와 장단점을 읽어보세요.
4. **검토:** 정확한 드라이버, 구성 요소 및 선택적 작업을 확인한 다음 설치를 확인하세요.
5. 선택한 작업에 대해서만 UAC를 수락합니다. 보호된 작업의 복구 지침을 유지하십시오.
6. 새 드라이버를 다시 시작해야 하는 경우 보고된 상태를 따르십시오. 지연된 작업에는 다시 시작한 후 명시적인 재개가 필요합니다.

Custom NV는 변경되지 않고 시작됩니다. 개별 명명된 값을 선택하거나 제공된 사전 설정 및 해당 제외 항목을 검토하세요. 두 개의 정보 내부 필드는 독립적으로 작성되지 않습니다. 설정은 확인된 새 드라이버 작업 흐름에만 적용되며 미리 보기를 열면 적용되지 않습니다. 별도의 NVPI 편집기 설치가 필요하지 않습니다.

선택적 NVENC 작업은 고정된 keylase 커밋에서 호환 가능한 데이터를 다운로드합니다. 두 개의 드라이버 DLL을 변경하고 해당 서명을 무효화합니다. Windows, 인코더, DRM 또는 치트 방지 장치에 의해 거부될 수 있습니다. NVDriverForge에는 해당 데이터나 NVIDIA DLL이 포함되어 있지 않습니다. [출처 및 라이선스 제한](../docs/provenance.md).

기본 설정은 언어, 테마 및 선택적 설치된 사용자 업데이트 확인을 제어합니다. 휴대용 장치는 설치된 백그라운드 확인 작업을 생성하지 않습니다. 도구 및 복구는 네 가지 설치 단계와 별개입니다.

<a id="screenshots"></a>
## 스크린샷

![NVDriverForge 드라이버 페이지 미리보기](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

기존 0.1.2 프랑스어 UI는 예제 데이터로 렌더링됩니다. 인터페이스 미리보기로 유지됩니다. 표시된 699.99 드라이버는 테스트 픽스처이며 다운로드할 실제 버전이 아닙니다. [이미지 출처](../assets/README.md).

<a id="update-and-uninstall"></a>
## 업데이트 및 제거

NVDriverForge를 닫고 다음 공식 패키지를 얻은 후 해시를 확인하세요. 설치된 업데이트에 동일한 설치 ID를 사용하십시오. 닫힌 휴대용 EXE를 새 것으로 교체하십시오. 설정 및 보호된 작업을 유지합니다.

Windows **Installed apps**의 Uninstall. NVIDIA 드라이버가 아닌 앱과 해당 업데이트 작업을 제거합니다. 설정, 로그, 백업은 그대로 유지됩니다. 원하는 경우 앱을 제거하기 **전에** 문서화된 복구 흐름을 통해 고급/NVENC 변경 사항을 복원하세요. 복원은 다른 도구의 변경 사항 충돌을 거부합니다.

로컬 데이터는 `%LOCALAPPDATA%\NVDriverForge` 아래에 있습니다. 보호된 작업 및 드라이버 내보내기는 `%PROGRAMDATA%\NVDriverForge\Jobs`에 있습니다. 휴대용으로 사용하면 로컬 데이터도 생성됩니다. 드라이버 저장소 내보내기는 시스템 이미지나 전체 프로필 백업이 아닙니다.

<a id="known-limitations"></a>
## 알려진 제한사항

- 하드웨어 추가/INF 편집, 재생성된 NVIDIA 서명, 치트 방지 호환 사임 또는 자동 서명되지 않은 경고 수락이 없습니다.
- 완전한 원격 측정/광고 제거, 슬림 패키지 내보내기 또는 이전 드라이버로의 자동 전체 롤백이 없습니다.
- 드라이버 설치, 부팅 복구 및 선택적 프로필 쓰기는 허브 감사를 통해 실제 컴퓨터에서 포괄적으로 검증되지 않았습니다.
- 레지스트리 다시 읽기는 실제 HDCP, 성능 또는 대기 시간 효과에 대한 증거가 아닙니다.
- 서명 확인은 로컬에서 사용 가능한 Windows 신뢰를 사용합니다. 온라인 취소는 수행되지 않습니다.
- 34개 언어가 제공되지만 완전한 원어민/접근성 테스트는 아직 완료되지 않았습니다.

<a id="troubleshooting"></a>
## 문제 해결

| 증상 | 액션 |
| --- | --- |
| 온라인 카탈로그를 사용할 수 없습니다 | [NVIDIA 드라이버 다운로드](https://www.nvidia.com/en-us/drivers/)에서 원본 패키지를 선택합니다. 인접한 GPU 모델을 대체하지 마십시오. |
| 핫픽스 조회를 사용할 수 없습니다. | [NVIDIA의 Game Ready 드라이버 포럼](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/)를 사용하여 실제 패키지를 확인하십시오. |
| NVIDIA 설치 실패 | 실패 요약을 읽고 자세한 로그를 엽니다. 이미 최신이거나 적용할 수 없는 선택적 구성 요소는 0.1.3에서 건너뛸 수 있는 상태로 유지됩니다. 실패한 설치는 선택적 조정이나 성공/다시 시작 흐름을 트리거하지 않습니다. |
| 서명/해시/백업 실패 | 해당 설치를 중지하고 오류를 유지하십시오. 손상된 경우 원래 패키지를 다시 얻으십시오. |
| 옵션을 사용할 수 없습니다 | 하드웨어, 구성 요소 또는 대상 드라이버 이유를 읽으십시오. 변함없이 유지하세요. |
| 다시 시작하거나 작업이 아직 보류 중입니다. | 작업의 복구 지침과 명시적인 이력서를 사용하십시오. 일기를 지우지 마십시오. |
| 복원 충돌 | 또 다른 상태는 기록된 트랜잭션과 다릅니다. 강제로 복원하는 대신 이를 보존하고 도움을 요청하세요. |

보고서에는 선택한 도구 버전, Windows, GPU, 드라이버 및 재현 가능한 단계가 포함됩니다. 로그에서 경로와 개인 정보를 수정합니다. [지원](../docs/support.md).

<a id="faq"></a>
## FAQ

**설치 프로그램에서 그래픽 드라이버를 설치합니까?** 아니요. 이를 위해서는 응용 프로그램의 별도 분석, 검토, 확인 및 향상된 설치 프로세스가 필요합니다.

**NVCleanstall 또는 NVPI가 필요합니까?** 아니요. NVCleanstall는 영감일 뿐입니다. Profile Inspector 동반자는 독립적인 선택적 편집기입니다.

**모든 NVIDIA 드라이버가 더 작아지거나 빨라지나요?** 아니요. 선택한 구성 요소와 전제 조건에 따라 변경 가능한 사항이 결정됩니다. 어떠한 측정된 이득도 약속되지 않습니다.

**소스는 어디에 있습니까?** 애플리케이션별 소스 및 비공개 테스트는 별도로 유지 관리됩니다. 이 허브는 귀속/라이선싱에 필요한 문서, 바이너리 및 타사 소스 링크를 제공합니다.

<a id="credits-and-upstream"></a>
## 크레딧 및 업스트림

원본 애플리케이션, 워크플로우, 트랜잭션, 현지화, 부트스트랩 및 적응: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): 워크플로우 영감; 가져온 소스나 바이너리가 없습니다.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT 테마, 확장된 NVAPI 인터페이스 참조 및 별도로 패키지된 fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): 수정되지 않은 추출 도구입니다.
- [Microsoft .NET](https://github.com/dotnet/runtime) 및 [WPF](https://github.com/dotnet/wpf): 번들 런타임.
- [Inno Setup](https://jrsoftware.org/isinfo.php): 원본 설치 프로그램 엔진 및 크레딧 번역.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): 외부 선택적 NVENC 데이터 소스; 재배포 라이센스가 설정되지 않았습니다.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): 외부 드라이버를 다운로드하고 NVAPI/NVML 라이브러리를 설치합니다.

[전체 구성 요소 테이블](../THIRD_PARTY_NOTICES.md) · [변경 및 출처](../docs/provenance.md)

<a id="license"></a>
## 라이센스

[기존 바이너리 배포 권한](../../../../NVDriverForge/LICENSE)는 해당 공지와 함께 수정되지 않은 공식 실행 파일의 사용 및 공유를 허용합니다. 애플리케이션별 소스 권한은 보유됩니다. 별도의 제3자 라이선스에 의해 부여된 권리를 제한하지 않습니다. [전체 공지](LICENSES/README.md).

NVIDIA Corporation, TechPowerUp 및 keylase와 독립적입니다. 후원하거나 공식적으로 승인하지 않았습니다. 제품 이름은 해당 소유자의 상표로 유지됩니다.
