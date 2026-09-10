<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Khả năng tương thích và khắc phục sự cố

Đây là những ứng cử viên đã được chuẩn bị sẵn, không phải là ma trận chứng nhận cho tất cả các kết hợp Windows, GPU, trình điều khiển và trò chơi.

| Công cụ | Windows/thời gian chạy | Phần cứng/phụ thuộc bên ngoài | Các hoạt động cần quan tâm |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Trình điều khiển/màn hình NVIDIA tương thích | Hồ sơ viết và hiển thị xem trước |
| NVDriverForge 0.1.2 | Windows 10 bản dựng 19041+ / 11 x64; Đã bao gồm .NET/WPF | Gói trình điều khiển NVIDIA tương thích | Cài đặt nâng cao, cài đặt nâng cao, NVENC tùy chọn |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; Bao gồm .NET/WPF, trình trợ giúp Framework 4.8 | RTX 40, nhà cung cấp trò chơi DLSS FG đủ điều kiện và được ghim | Bản vá gốc trong trò chơi, nhật ký hồ sơ toàn cầu, cập nhật trò chơi SDK |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | Đã cài đặt RTSS; chạy cho mũ | RTSS thay đổi cấu hình mỗi lần thực thi |

Không có gói ARM64 nào được chuẩn bị. Tính khả dụng của Display/API và các phiên bản Windows cũ có thể hạn chế các tính năng riêng lẻ. Không có phiên bản NVIDIA hoặc RTSS tối thiểu phổ quát nào được phát minh. Giá trị băm của nhà cung cấp NVMFG chính xác nằm trong [xuất xứ](provenance.md).

<a id="before-reporting-a-bug"></a>
## Trước khi báo cáo lỗi

Xác định chính xác phiên bản/thực thi mà bạn đã mở. Bản sao đã cài đặt trước đó không nhất thiết phải là phiên bản của ZIP mới tải xuống. Ghi lại các bước tái tạo, kết quả mong đợi và kết quả thực tế. Đối với các vấn đề kết xuất/giới hạn, hãy bao gồm phiên bản trò chơi, làm mới màn hình, trạng thái FG/V-Sync/VRR và bất kỳ giới hạn hoặc lớp phủ nào khác.

Sử dụng [dạng lỗi](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Không bao giờ đính kèm toàn bộ thư mục phát triển riêng tư, kho lưu trữ trình điều khiển, mô hình, DLL trò chơi, kết xuất sổ đăng ký hoặc bộ sưu tập nhật ký chưa được xem xét.

| vấn đề | Kiểm tra đầu tiên |
| --- | --- |
| Phiên bản ứng dụng sai | Xác nhận danh tính EXE và phát hành hàm băm; đóng bản sao cũ hơn trước khi thay thế. |
| Lỗi thời gian chạy/khởi động | Cài đặt Framework 4.8 được yêu cầu hoặc giữ lại tất cả các thư mục con di động được cung cấp. |
| UAC đã bị hủy | Chỉ thử lại thao tác dự định; hủy bỏ là cài đặt không thành công. |
| Giá trị băm/chữ ký không khớp | Hãy ngừng sử dụng ứng cử viên đó và nhận được số byte chính thức dự kiến. |
| Màu/chế độ NVPI bị từ chối | Hoàn nguyên và sử dụng kết hợp được hỗ trợ bởi màn hình/trình điều khiển thực tế. |
| Lỗi sao lưu hoặc phục hồi NVDF | Duy trì công việc được bảo vệ và RECOVERY.txt; không xóa nhật ký hoặc ép buộc viết xung đột. |
| Cài đặt đang chờ xử lý NVMFG | Giải quyết việc khôi phục khi trò chơi đã đóng, bảo toàn các thay đổi từ các công cụ khác. |
| Mũ RP không có tác dụng | Chạy RTSS, xác định EXE trò chơi thực, kiểm tra trạng thái hook và giới hạn cạnh tranh. |
| Nắp RP vẫn tồn tại sau khi gỡ bỏ | Kiểm tra RTSS Toàn cầu; việc loại bỏ các thay đổi chỉ ghi đè giới hạn cục bộ. |

<a id="logs-and-privacy"></a>
## Nhật ký và quyền riêng tư

| Công cụ | Dữ liệu cục bộ để xem xét, không tải lên bán buôn |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; công việc được bảo vệ `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; sao lưu `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` bên cạnh EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` bên dưới nó |
| NVPI | Các bản xuất bạn đã chọn và lỗi hiển thị; không có đường dẫn nhật ký phổ quát nào được phát minh |

Xóa tên tài khoản, thư mục chính, đường dẫn thư viện trò chơi, số nhận dạng thiết bị, mã thông báo và cửa sổ không liên quan khỏi văn bản/hình ảnh bạn chia sẻ. Giữ bản gốc riêng tư để phục hồi. Các vấn đề công khai được hiển thị cho mọi người.

Đối với lỗ hổng bảo mật, hành vi đặc quyền nguy hiểm hoặc hoạt động phá hoại ngoài ý muốn, hãy theo dõi [SECURITY.md](../SECURITY.md) thay vì đăng công khai chi tiết.

<a id="what-has-been-verified"></a>
## Những gì đã được xác minh

Để chuẩn bị trung tâm, quét tải trọng tĩnh/ZIP/băm/siêu dữ liệu và kiểm tra tài liệu đã được chạy. Các thử nghiệm xây dựng/đơn vị/giao diện người dùng ứng dụng riêng hiện có là bằng chứng lịch sử, có niên đại. Không có cài đặt trình điều khiển, thay đổi hiển thị, thao tác RTSS trực tiếp hoặc điểm chuẩn trò chơi nào được thực hiện như một phần của quá trình chuẩn bị này.

“Đã phát hiện”, “được viết”, “được tải lại”, “khả năng khả dụng” và “được đo trong trò chơi” là những kết quả khác nhau. Báo cáo cái nào bạn quan sát được.
