<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · **한국어** · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> 영어에서 기계 지원 번역. 기술 이름, 명령, URL 및 원본 법률 텍스트가 보존됩니다. 원어민 리뷰를 환영합니다. 표현이 명확하지 않은 경우 영어 참조 자료를 참조하세요.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# 호환성 및 문제 해결

이는 모든 Windows, GPU, 드라이버 및 게임 조합에 대한 인증 매트릭스가 아닌 준비된 후보자입니다.

| 도구 | Windows/런타임 | 하드웨어/외부 종속성 | 주의가 필요한 작업 |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET 프레임워크 4.8 | 호환 가능한 NVIDIA 드라이버/디스플레이 | 프로필 작성 및 미리보기 표시 |
| NVDriverForge 0.1.4 | Windows 10 빌드 19041+ / 11 x64; .NET/WPF 포함 | 호환 가능한 NVIDIA 드라이버 패키지 | 높은 설치, 고급 설정, 옵션 NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF 포함, 프레임워크 4.8 도우미 | RTX 40, 적격 DLSS FG 게임 및 고정된 공급자 | 기본 게임 내 패치, 글로벌 프로필 저널, SDK 게임 업데이트 |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET 프레임워크 4.8 | RTSS가 설치되었습니다. 모자를 향해 달리다 | RTSS 실행 가능 프로필당 변경 사항 |

ARM64 패키지가 준비되지 않았습니다. 디스플레이/API 가용성 및 이전 Windows 버전으로 인해 개별 기능이 제한될 수 있습니다. 범용 최소 NVIDIA 또는 RTSS 버전은 개발되지 않았습니다. 정확한 NVMFG 공급자 해시는 [출처](provenance.md)에 있습니다.

<a id="before-reporting-a-bug"></a>
## 버그를 신고하기 전에

열어본 정확한 실행 파일/버전을 확인하세요. 이전에 설치된 복사본이 반드시 새로 다운로드한 ZIP 버전일 필요는 없습니다. 재현 단계, 예상 결과 및 실제 결과를 기록합니다. 렌더링/제한 문제의 경우 게임 버전, 디스플레이 새로 고침, FG/V-Sync/VRR 상태 및 기타 제한기 또는 오버레이를 포함합니다.

[버그 양식](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml)를 사용하세요. 전체 개인 개발 폴더, 드라이버 아카이브, 모델, 게임 DLL, 레지스트리 덤프 또는 검토되지 않은 로그 수집을 첨부하지 마십시오.

| 문제 | 첫 번째 확인 |
| --- | --- |
| 잘못된 애플리케이션 버전 | EXE 신원과 릴리스 해시를 확인합니다. 교체하기 전에 이전 복사본을 닫습니다. |
| 런타임/시작 오류 | 필수 Framework 4.8를 설치하거나 제공된 모든 휴대용 하위 폴더를 유지하십시오. |
| UAC 취소됨 | 의도한 작업만 다시 시도하세요. 취소하면 설치가 성공적이지 않습니다. |
| 해시/서명 불일치 | 해당 후보 사용을 중지하고 예상되는 공식 바이트를 얻으십시오. |
| NVPI 색상/모드가 거부됨 | 실제 디스플레이/드라이버에서 지원하는 조합을 되돌려 사용하세요. |
| NVDF 백업 또는 복구 실패 | 보호된 작업 및 RECOVERY.txt를 보존합니다. 저널을 지우거나 충돌하는 쓰기를 강요하지 마십시오. |
| NVMFG 보류 설정 | 게임을 닫은 상태에서 복구를 해결하고 다른 도구의 변경 사항을 유지합니다. |
| RP 캡은 효과가 없습니다. | RTSS를 실행하고, 실제 게임 EXE를 식별하고, 후크 상태와 경쟁 제한을 검사합니다. |
| 제거 후에도 RP 캡이 지속됩니다. | RTSS 글로벌을 검사합니다. 제거 변경 사항은 로컬 리미터만 무시합니다. |

NVDriverForge는 미리 볼 수 있는 로컬 JSON 보고서를 제공합니다. NVMFG는 정보에서 진단을 제공합니다. 전체 로그 아카이브보다 필터링된 보고서를 선호하고 공유하기 전에 검사하세요. NVMFG 0.1.1에서 보고된 복원 막힘은 아직 확립된 원인이 없습니다. 저널을 보존하고 사용 가능한 오류 코드를 기록하십시오. NVRasterPulse 0.2는 FPS를 측정하지 않고 작업 메뉴에서 구성 진단을 제공합니다.

<a id="logs-and-privacy"></a>
## 로그 및 개인정보 보호

| 도구 | 검토할 로컬 데이터(대부분 업로드하지 않음) |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; 보호된 작업 `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; 백업 `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; EXE 옆의 `Sessions` |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; 그 아래 `Backups\RTSS` |
| NVPI | 선택한 내보내기 및 표시된 오류 발명된 범용 로그 경로 없음 |

공유하는 텍스트/이미지에서 계정 이름, 홈 디렉터리, 게임 라이브러리 경로, 장치 식별자, 토큰 및 관련 없는 창을 제거하세요. 복구를 위해 원본을 비공개로 보관하세요. 공개 문제는 모든 사람이 볼 수 있습니다.

취약성, 위험한 권한 있는 동작 또는 의도하지 않은 파괴적인 작업의 경우 세부 정보를 공개적으로 게시하는 대신 [SECURITY.md](../SECURITY.md)를 따르세요.

<a id="what-has-been-verified"></a>
## 검증된 내용

허브 준비를 위해 정적 페이로드/ZIP/해시/메타데이터 스캔 및 문서 확인이 실행되었습니다. 기존의 비공개 애플리케이션 빌드/유닛/UI 테스트는 과거의 날짜가 기록된 증거입니다. 이 준비 과정에서 드라이버 설치, 디스플레이 변경, 라이브 RTSS 작업 또는 게임 벤치마크가 수행되지 않았습니다.

"감지됨", "작성됨", "다시 로드됨", "사용 가능한 기능" 및 "게임에서 측정됨"은 서로 다른 결과입니다. 당신이 관찰한 것을 보고하세요.
