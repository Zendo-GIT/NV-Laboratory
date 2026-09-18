<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · **한국어** · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**禅堂 Zendo (RevoluSound Team)의 NV Tools.** NVIDIA 드라이버 프로필, 드라이버 설치, 실험적인 Multi Frame Generation 및 RTSS 프레임 제한을 위한 4개의 독립적인 Windows 유틸리티입니다.

[도구 받기](docs/downloads.md) · [설치](docs/installation.md) · [호환성 및 도움말](docs/support.md) · [크레딧 및 라이선스](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse에는 RTSS가 필요합니다.** [Guru3D의 RivaTuner Statistics Server](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)를 먼저 설치하세요. FPS 제한이 작동하려면 RTSS가 실행 중이어야 합니다. 별도로 다운로드됩니다.

<a id="projects"></a>
## 프로젝트

| 프로젝트 | 목적 | 버전 | 문서 | 다운로드 |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | 디스플레이, 색상, HDR 및 ICC/WCS 컨트롤이 추가된 NVIDIA 드라이버 프로필 편집기. 이전에는 NVPI Custom입니다. | 3.0.2.3 | [가이드](NVIDIA-Profile-Inspector/README.md) | [패키지](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | 선택 안내, 백업 및 복구를 통해 원본 NVIDIA 드라이버를 준비하고 설치하세요. | 0.1.4 | [가이드](NVDriverForge/README.md) | [패키지](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | 실험적 RTX 40 MFG, 영구 게임 라이브러리, 진단 및 Streamline SDK 유지 관리. | 0.2.3 | [가이드](NVMFG-Unlock40/README.md) | [패키지 및 상태](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | 프로그램당 RTSS FPS 제한(진단, 제안, 일시 중지, 실행 취소 및 프로필 공유)을 관리합니다. | 0.2 | [가이드](NVRasterPulse/README.md) | [패키지](docs/downloads.md#nvrasterpulse) |

**다운로드:** [다운로드 페이지](docs/downloads.md)에는 각 버전의 상태, 파일 및 SHA-256 값이 나열되어 있습니다. 실험적 기능과 호환성 제한은 프로젝트 가이드에 설명되어 있습니다.

<a id="start-here"></a>
## 여기서 시작하세요

1. 위에서 도구 하나를 선택하세요. 각각은 독립적으로 작동합니다. 전체 제품군을 설치할 필요가 없습니다.
2. 요구 사항을 읽고 설치된 앱의 경우 **설정**을 선택하고, 별도의 폴더인 경우 **이식 가능**을 선택하세요.
3. 릴리스가 게시되면 명명된 애플리케이션 자산을 다운로드하고 함께 제공되는 알림을 읽고 SHA-256를 비교하십시오.
4. 드라이버, 디스플레이 설정, NVIDIA 프로필 또는 게임 런타임을 변경하기 전에 백업을 유지하세요.

문서는 각 가이드 상단에 있는 선택기를 통해 NV 애플리케이션과 동일한 34개 언어로 제공됩니다. GitHub는 브라우저 언어별로 README를 자동으로 선택하지 않습니다. 문서 언어와 애플리케이션 자체 언어 설정은 별개입니다.

<a id="provenance-and-ownership"></a>
## 출처 및 소유권

이 허브는 문서와 컴파일된 애플리케이션을 배포합니다. 애플리케이션 소스 코드는 비공개로 유지됩니다. 업스트림 프로젝트는 저작자와 라이선스를 유지합니다. 비공개 소스 배포는 해당 용어를 대체하지 않습니다.

- Profile Inspector fork는 Orbmu2k의 MIT 라이센스를 유지하며 명시적으로 fork로 식별됩니다.
- NVDriverForge에는 자체 바이너리 배포 조건이 있으며 별도로 라이센스가 부여된 런타임/도구 구성 요소가 포함되어 있습니다.
- NVMFG Unlock40는 독자적으로 개발된 애플리케이션입니다. 비교 및 개선을 위해 RTX40MFG-Unlock를 참조했습니다. 공유 기본 구성 요소는 MIT 크레딧을 유지합니다. MinHook 및 NVIDIA SDK 용어는 별도로 유지됩니다.
- NVRasterPulse는 제공된 MIT 라이센스를 유지하고 Profile Inspector 파생 UI에 크레딧을 부여합니다. RTSS는 필수 외부 프로그램입니다.

[완전한 구성 요소 테이블](THIRD_PARTY_NOTICES.md), [파일 출처 및 변경 사항](docs/provenance.md) 및 [라이센스 범위](../../../LICENSE)를 참조하세요.

<a id="other-projects--revolusound-team"></a>
## 기타 프로젝트 – RevoluSound Team

이는 팀의 작업을 발견하는 데 도움이 되도록 여기에 링크된 별도의 오디오 모드 프로젝트입니다.

| 게임 | 프로젝트 | 소개 |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | 엔진, 배기, 흡기 및 터보 효과를 다루는 차량 사운드 변경. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | 팀의 최신 FH5 차량 오디오 팩. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | 이전 FH5 팩; Nexus 페이지는 방문자를 위의 최신 팀 팩으로 안내합니다. |

제목은 링크된 Nexus Mods 페이지를 따릅니다. 다운로드, 요구 사항, 크레딧 및 권한은 Nexus Mods에 유지됩니다.

<a id="help-and-participation"></a>
## 도움과 참여

[버그 신고 또는 기능 제안](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [기여](CONTRIBUTING.md) · [보안 보고서](SECURITY.md) · [변경 내역](CHANGELOG.md)

보안 문제의 경우 로그나 기술 세부정보를 게시하기 전에 SECURITY.md를 읽어보세요. 저장소 게시 후 관리자가 비공개 보고를 활성화해야 합니다.

> **독립 커뮤니티 프로젝트.** NV Laboratory, NV Tools 및 이러한 유틸리티는 NVIDIA Corporation와 제휴하거나 후원하거나 공식적으로 보증하지 않습니다. NVIDIA, GeForce, RTX, DLSS 및 기타 제품 이름은 해당 소유자의 상표입니다. 이름은 공식적인 보증이 아닌 호환성과 출처를 설명합니다.
