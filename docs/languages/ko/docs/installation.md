<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · **한국어** · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# 설치 가이드

게시 상태와 정확한 자산 이름을 기록하는 [다운로드](downloads.md)부터 시작하세요. 이들은 별도의 도구이므로 필요한 도구만 설치하세요.

> **NVRasterPulse의 경우 프로필 관리자를 열기 전에 [Guru3D의 RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)를 설치하세요.**
> 제한을 적용하려면 RTSS를 실행해야 합니다. NV Tools에는 포함되어 있지 않습니다.

| 도구 | 설치된 버전 | 휴대용 버전 | 주요 전제 조건 |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | 전체 NVPI ZIP 추출 | NVIDIA 드라이버 및 .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, 런타임 포함 | 설치 작업에 호환되는 원본 NVIDIA 드라이버 패키지 |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | 전체 NVMFG ZIP 추출, 하위 폴더 유지 | RTX 40, 기존 DLSS FG, 정확한 공급자 및 .NET Framework 4.8 도우미 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | 전체 RP ZIP 추출 | RTSS 및 .NET 프레임워크 4.8 |

<a id="download-verify-install"></a>
## 다운로드, 확인, 설치

1. 선택한 게시된 릴리스에서 명명된 애플리케이션 자산을 다운로드하고 ZIP 및 SHA256SUMS.txt를 확인합니다.
2. 실제 다운로드한 파일 이름과 함께 [SHA-256 예시](downloads.md#sha-256)를 사용하세요.
3. 설치는 일반 설치 프로그램을 따르세요. 휴대용 ZIP의 경우 모든 내용을 쓰기 가능한 새 로컬 폴더에 추출합니다. ZIP 내부에서 실행하지 마십시오.
4. 응용 프로그램 자체 EXE를 엽니다. 함께 제공되는 라이센스/구성/데이터 파일을 보관하십시오.
5. 설정이나 시스템 작동을 활성화하기 전에 해당 도구의 사용 지침을 읽으십시오.

현재 바이너리는 서명되지 않았습니다. 일치하는 해시는 예상 바이트를 확인합니다. 이는 보안 또는 호환성 인증서가 아닙니다. 단지 경고를 억제하기 위해 Windows 보안 보호를 비활성화하지 마십시오.

NVDF 또는 옵션인 NVPI 동반 설치는 GPU 드라이버 설치와 별개입니다. NVPI 컴패니언은 기존 내부 설치 이름을 유지합니다. 높은 RasterPulse 버튼을 사용하려면 시스템 전체에 걸쳐 보호된 설치가 필요합니다. 다른 RP 복사본은 자체 바로가기를 통해 열 수 있습니다.

NVMFG는 실험적이며 [문서화된 NVIDIA SDK 라이센스 예약](provenance.md)를 가지고 있습니다. NVIDIA 드라이버, NGX 공급자/모델 또는 게임 Streamline 런타임은 포함되어 있지 않습니다. 선택된 SDK 다운로드와 게임 업데이트는 명시적으로 별도의 작업입니다.

<a id="language-and-updates"></a>
## 언어 및 업데이트

문서화를 위해서는 README의 34개 언어 선택기를 사용하세요. NVDF, NVMFG 및 RP에는 자체 34개 언어 UI 설정이 있습니다. NVPI는 기존 언어 지원을 유지합니다. 일부 설치 프로그램 기술 문자열은 영어로 대체됩니다.

업데이트할 때 도구의 설치 ID를 유지하세요. 먼저 닫고 백업을 보존하십시오. NVMFG의 경우 영향을 받는 게임을 닫고 보류 중인 프로필 복구를 해결하세요. 휴대용 업데이트의 경우 릴리스를 결합하는 대신 새로운 폴더를 사용하십시오.

<a id="removing-a-tool"></a>
## 도구 제거

응용 프로그램을 제거해도 해당 설정이 자동으로 취소되지는 않습니다.

- **NVPI:** 필요한 경우 제거하기 전에 의도한 프로필/디스플레이 설정을 복원하세요.
- **NVDF:** 고급/NVENC 변경 사항을 복원하려면 먼저 복구를 사용하세요. Uninstall는 그래픽 드라이버, 설정 및 백업을 그대로 둡니다.
- **NVMFG:** 게임을 닫고 컨트롤러를 비활성화/종료하고 NVIDIA 복구를 해결하고 제거하기 전에 원하는 게임 SDK 백업을 복원합니다.
- **RP:** 의도한 리미터 재정의를 먼저 제거하세요. Uninstall는 저장된 RTSS 캡을 지우거나 RTSS를 제거하지 않습니다.

정확한 데이터 위치 및 제한 사항은 각 [프로젝트 가이드](../README.md#projects)를 참조하고, 복구 단계가 실패한 경우 [지원하다](support.md)를 참조하세요.
