<!-- nv-language-navigation:start -->
🌐 [English](../../../THIRD_PARTY_NOTICES.md) | [Français](../fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/THIRD_PARTY_NOTICES.md) · [বাংলা](../bn/THIRD_PARTY_NOTICES.md) · [简体中文](../zh/THIRD_PARTY_NOTICES.md) · [Čeština](../cs/THIRD_PARTY_NOTICES.md) · [Dansk](../da/THIRD_PARTY_NOTICES.md) · [Nederlands](../nl/THIRD_PARTY_NOTICES.md) · [English](../../../THIRD_PARTY_NOTICES.md) · [Filipino](../fil/THIRD_PARTY_NOTICES.md) · [Suomi](../fi/THIRD_PARTY_NOTICES.md) · [Français](../fr/THIRD_PARTY_NOTICES.md) · [Deutsch](../de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](../el/THIRD_PARTY_NOTICES.md) · [हिन्दी](../hi/THIRD_PARTY_NOTICES.md) · [Magyar](../hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](../id/THIRD_PARTY_NOTICES.md) · [Italiano](../it/THIRD_PARTY_NOTICES.md) · [日本語](../ja/THIRD_PARTY_NOTICES.md) · **한국어** · [मराठी](../mr/THIRD_PARTY_NOTICES.md) · [فارسی](../fa/THIRD_PARTY_NOTICES.md) · [Polski](../pl/THIRD_PARTY_NOTICES.md) · [Português](../pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](../pa/THIRD_PARTY_NOTICES.md) · [Română](../ro/THIRD_PARTY_NOTICES.md) · [Русский](../ru/THIRD_PARTY_NOTICES.md) · [Español](../es/THIRD_PARTY_NOTICES.md) · [Kiswahili](../sw/THIRD_PARTY_NOTICES.md) · [Svenska](../sv/THIRD_PARTY_NOTICES.md) · [தமிழ்](../ta/THIRD_PARTY_NOTICES.md) · [ไทย](../th/THIRD_PARTY_NOTICES.md) · [Türkçe](../tr/THIRD_PARTY_NOTICES.md) · [Українська](../uk/THIRD_PARTY_NOTICES.md) · [اردو](../ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](../vi/THIRD_PARTY_NOTICES.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="third-party-notices-and-credits"></a>
# 제3자 통지 및 크레딧

최초 감사: 2026-09-09; NVDriverForge 0.1.3 및 출처 업데이트: 2026-09-10. **구성 요소의 라이선스는 전체 제품군이 아닌 해당 구성 요소에 적용됩니다.** 애플리케이션 소스는 비공개로 유지됩니다. 저작권 및 허가 고지는 그대로 유지됩니다. 이 테이블은 인덱스이지 대체 테이블이 아닙니다. "외부"는 애플리케이션 자산에 배포되지 않음을 의미합니다.

| 구성요소/원본 프로젝트 | 작성자 | 공식 사이트, 저장소 또는 다운로드 | 라이선스/고지 | NV Tools에서 사용 | 수정 |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k; 저작권 2016 | [저장소](https://github.com/Orbmu2k/nvidiaProfileInspector), [다운로드](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](../../../NVIDIA-Profile-Inspector/LICENSE) | 전체 NVPI fork; NVDF 테마/확장 인터페이스 참조; NVMFG 래퍼/스타일; RP UI 리소스 | Fork 디스플레이 서비스, 트랜잭션 및 실행 프로그램; 테마/컨트롤 통합 및 래퍼 적응 |
| RTX40MFG-Unlock | Michael Robles / dashdogy; 저작권 2026 | [저장소](https://github.com/dashdogy/RTX40MFG-Unlock), [다운로드](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](../../../NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | 비교/개량 참조 및 공유/적응된 NVMFG 기본 구성요소 독립적으로 개발된 애플리케이션 | 중앙 로딩, NGX/컨트롤러 조정, 게임별/V-Sync 통합 및 진단 |
| MinHook, 고정된 8fda4f5 | Tsuda Kageyu; 저작권 2009-2017 | [저장소](https://github.com/TsudaKageyu/minhook), [고정된 소스](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2절 공지](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | NVMFG 엔진에 정적으로 컴파일됨 | 상속된 복사본에 대한 텍스트 서식을 제외하고 변경되지 않은 포함된 하위 집합 |
| Hacker Disassembler Engine(HDE64) | Vyacheslav Patkov; 저작권 2008-2009 | [MinHook의 소스 컬렉션](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [전체 MinHook/HDE 공지](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | NVMFG의 MinHook 디코더 | 기능적 변화는 확인되지 않았습니다. 프로덕션에서 HDE64를 사용하더라도 HDE32 알림은 유지됩니다. |
| Streamline 2.12 통합 헤더 | NVIDIA Corporation; 저작권 2023 | [저장소](https://github.com/NVIDIA-RTX/Streamline), [다운로드](https://github.com/NVIDIA-RTX/Streamline/releases) | [적격 헤더의 경우 MIT](../../../NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | NVMFG Streamline 통합 컴파일 | 헤더가 수정되지 않았습니다. 응용 프로그램 패키지에 런타임 DLL이 없습니다. |
| NVIDIA NGX / DLSS SDK 헤더 | NVIDIA Corporation | [고정된 저장소](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [NVIDIA RTX SDK 용어](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [헤더 공지](../../../NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | NVMFG NGX 통합 컴파일 | 헤더가 수정되지 않았습니다. NGX 모델/공급자가 번들로 제공되지 않습니다. 아래에 설명된 해결되지 않은 제한사항 |
| .NET 런타임 8.0.31(NVDF)/8.0.30(NVMFG) | .NET Foundation, Microsoft 및 기여자 | [소스](https://github.com/dotnet/runtime), [다운로드](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-NET-LICENSE.txt) 및 [완전한 제3자 통지](../../../licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | 독립형 NVDF 및 NVMFG 앱/에이전트 | 수정되지 않은 런타임 |
| WPF / Windows Desktop Runtime 8.0.31(NVDF) / 8.0.30(NVMFG) | .NET Foundation, Microsoft 및 기여자 | [소스](https://github.com/dotnet/wpf), [다운로드](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-WPF-LICENSE.txt), 위의 런타임 알림 | NVDF 및 NVMFG 사용자 인터페이스 | 수정되지 않은 프레임워크; 애플리케이션 UI가 별도로 제작/적용됨 |
| .NET 프레임워크 4.8 | Microsoft | [공식 런타임 다운로드](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | Microsoft 플랫폼/런타임 용어; 외부 | NVPI, RP 및 NVMFG 프로필 도우미 | 없음; 이 허브에서 재배포하는 설치 프로그램이나 프레임워크 DLL이 없습니다. |
| 7-Zip 26.03 x64 | Igor Pavlov; 저작권 1999-2026 | [사이트/다운로드](https://www.7-zip.org/download.html), [정확한 소스 아카이브](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | [전체 공지](../../../licenses/third-party/7-Zip.txt), [LGPL 2.1-or-later](../../../licenses/third-party/LGPL-2.1.txt), BSD 부분 및 unRAR 제한사항 | NVDF는 수정되지 않은 7z.exe/7z.dll를 포함하고 CLI를 별도의 프로세스로 실행합니다. | 수정 없음 |
| Inno Setup 7.1.0 | Jordan Russell, Martijn Laan 및 기여자 | [사이트/다운로드](https://jrsoftware.org/isinfo.php), [출처](https://github.com/jrsoftware/issrc) | [원본 Inno Setup 라이센스](../../../licenses/third-party/Inno-Setup.txt) | 설치 프로그램 엔진 및 생성된 제거 프로그램 | 엔진/컴파일러는 수정되지 않았습니다. 프로젝트 스크립트, 브랜딩 및 네이티브 포커스 처리 조정 |
| Inno Setup 번역 카탈로그 | 명명된 원본 번역가 | [공식 컬렉션](https://jrsoftware.org/files/istrans/) | Inno/카탈로그 공지 및 [완전한 헤더 크레딧](../../../licenses/INSTALLER-TRANSLATORS.md) | NVPI 설치 개정 2를 포함하여 4개의 설치 프로그램 모두에 대해 공유된 34개 언어 카탈로그 | 키, ID, 글꼴, 기술 영어 대체; 필요한 경우 프로젝트 작성 미리보기 카탈로그 |
| Microsoft 비주얼 C++ 런타임 / Windows SDK 지원 | Microsoft | [비주얼 Studio 도구](https://visualstudio.microsoft.com/downloads/), [재배포 용어 색인](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft 툴체인/런타임 용어; 이 테이블에서는 MIT가 아닙니다. | 기본 엔진/부트스트랩 바이너리의 정적 릴리스 CRT; Windows API 설치 | 런타임 소스는 변경되지 않습니다. 컴파일러, SDK 또는 디버그 런타임이 배포되지 않음 |
| RivaTuner Statistics Server (RTSS) | Unwinder | [공식 Guru3D 다운로드](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | 공급업체 약관 "프리웨어"에서 유추된 재배포 권한 없음 | RP에 필요한 외부 리미터; UpdateProfiles 내보내기 설치 | RTSS 코드/바이너리 수정 또는 번들 없음; RP는 선택한 프로필 키를 씁니다. |
| NVIDIA 드라이버 / NVAPI / NVML | NVIDIA Corporation | [드라이버 다운로드](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA 드라이버/SDK 용어; 외부 | 설치된 기본 인터페이스 및 명시적인 원본 드라이버 다운로드 | 허브 자산에 NVIDIA DLL이 없습니다. NVDF의 선택적 NVENC 작업은 사용자가 선택한 설치된 DLL을 수정합니다. |
| NVIDIA NGX 공급자/모델 및 Streamline 런타임 | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Streamline 릴리스](https://github.com/NVIDIA-RTX/Streamline/releases) | MIT 헤더와 구별되는 구성요소별 NVIDIA 용어 | NVMFG에서 사용되는 외부 게임/드라이버 구성 요소. SDK는 요청 시에만 가져옴 | NVMFG는 실험적인 메모리 내 동작 변경 사항을 적용합니다. SDK 게임 사본은 백업으로 업데이트 가능 |
| keylase/nvidia-patch | keylase 및 기여자 | [저장소](https://github.com/keylase/nvidia-patch), [Windows 데이터](https://github.com/keylase/nvidia-patch/tree/master/win) | 이번 감사를 통해 재배포 라이센스가 확립되지 않았습니다. | 외부 선택적 NVDF NVENC 카탈로그/패치 데이터(선택 항목당 하나의 고정된 커밋에서 가져옴) | 허브/애플리케이션 자산에 복사된 업스트림 소스, 패치 프로그램 또는 패치 데이터가 없습니다. |
| NVCleanstall | TechPowerUp | [공식 페이지/다운로드](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | 독점 배포; 추론된 소스/바이너리 재배포 권한이 없습니다. | NVDF에 대한 워크플로 및 옵션 영감 | 가져온 소스나 바이너리가 없습니다. fork 또는 런타임 종속성이 아님 |

<a id="obligations-and-boundaries"></a>
## 의무와 경계

**MIT 구성요소:** 사본과 함께 저작권, 허가 텍스트 및 면책조항을 유지합니다. 해당 라이선스는 수정된 소스의 게시를 요구하지 않습니다. 애플리케이션 소스가 비공개로 유지되는 경우에도 원본 저작자는 유지됩니다.

**MinHook/HDE:** 바이너리 문서의 고지 사항, 조건 및 면책 조항을 보존합니다. 전체 통합 통지가 제공됩니다.

**7-Zip:** LGPL/BSD/unRAR 알림을 보존하고 수정되지 않은 정확한 소스에 대한 액세스를 제공합니다. 소스 아카이브는 전체 LGPL와 함께 위에 링크되어 있습니다. unRAR 제한사항은 관련 압축 해제 코드에 적용됩니다. 이는 포괄적인 MIT 종속성이 아닙니다. 작성자의 [배포 FAQ](https://www.7-zip.org/faq.html)를 참조하세요.

**Inno Setup:** 필수 엔진 저작권/웹사이트 공지를 유지하고 해당되는 경우 소스 변경 사항을 표시합니다. 수정되지 않은 엔진의 크레딧은 설치 프로그램에 남아 있습니다. 개조된 카탈로그에는 원본 소스 공지가 유지됩니다. 이름은 여기에 색인되어 있습니다.

**NVIDIA 자료:** Streamline 통합 헤더용 MIT 라이센스는 모든 SDK 파일에 적용되지 않습니다. 해당 공지는 Nsight Perf SDK 자료를 명시적으로 구분합니다. 해당 재료는 이 생산 목표에 사용되지 않습니다. NGX 헤더는 NVIDIA의 독점 RTX SDK 용어를 따릅니다. [원본 바이트 복사본](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt)와 함께 전체 텍스트가 추가되었습니다. 기술적 한계에 관한 섹션 4(d)의 제한은 NVMFG의 사용에 대해 해결되지 않은 상태로 남아 있습니다. 다른 모드의 존재로 인해 긍정적인 권한이 유추되지는 않습니다.

**외부 알 수 없는/독점 구성 요소:** RTSS, NVCleanstall, NVIDIA 드라이버, 모델 및 keylase 패치 데이터는 준비된 허브 자산에 번들로 제공되지 않습니다. 링크는 실제 소유자를 식별합니다. 사용자가 실행한 다운로드에서는 구성 요소에 대한 라이선스가 다시 부여되지 않습니다.

이 도구는 Windows에서 제공하는 API 및 글꼴을 사용합니다. Windows SDK/compiler/font 파일은 이 Git 저장소에 복사되지 않습니다. 빌드 도구와 비공개 테스트는 배포 외부에 있습니다. 런타임 내부 구성 요소 알림은 게시자에게 다시 할당되지 않고 전체 Microsoft 알림 파일에 유지됩니다.

<a id="publisher-contributions"></a>
## 출판사 기여

禅堂 Zendo (RevoluSound Team)는 [출처 안내](docs/provenance.md)에 설명된 원본 애플리케이션 작업, 적응 및 문서를 유지 관리합니다. [NVPI](NVIDIA-Profile-Inspector/README.md), [NVDF](NVDriverForge/README.md), [NVMFG](NVMFG-Unlock40/README.md) 및 [RP](NVRasterPulse/README.md)는 각각 상속된 작업과 변경 사항을 구별합니다.

독립 프로젝트; NVIDIA Corporation 또는 나열된 업스트림 저자와의 제휴, 후원 또는 공식 승인을 암시하지 않습니다.
