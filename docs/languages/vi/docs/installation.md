<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Hướng dẫn cài đặt

Bắt đầu với [Tải xuống](downloads.md), ghi lại trạng thái xuất bản và tên nội dung chính xác. Đây là những công cụ riêng biệt: chỉ cài đặt những công cụ bạn cần.

> **Đối với NVRasterPulse, hãy cài đặt [RTSS từ Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) trước khi mở trình quản lý hồ sơ.**
> RTSS phải chạy để áp dụng các giới hạn; nó không được bao gồm trong NV Tools.

| Công cụ | Phiên bản đã cài đặt | Phiên bản di động | Điều kiện tiên quyết chính |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Giải nén hoàn chỉnh NVPI ZIP | Trình điều khiển NVIDIA và .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, bao gồm thời gian chạy | Gói trình điều khiển NVIDIA gốc tương thích cho các thao tác cài đặt |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Trích xuất ZIP NVMFG hoàn chỉnh, giữ lại các thư mục con | RTX 40, DLSS FG hiện có, nhà cung cấp chính xác và người trợ giúp .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Giải nén hoàn chỉnh RP ZIP | RTSS và .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Tải xuống, xác minh, cài đặt

1. Trên Bản phát hành đã xuất bản đã chọn, hãy tải xuống nội dung ứng dụng có tên của nó, thông báo ZIP và SHA256SUMS.txt.
2. Sử dụng [Ví dụ SHA-256](downloads.md#sha-256), với tên tệp được tải xuống thực tế.
3. Để thiết lập, hãy làm theo trình cài đặt bình thường. Đối với ZIP di động, hãy trích xuất mọi thứ vào một thư mục có thể ghi cục bộ mới; không chạy từ bên trong ZIP.
4. Mở EXE riêng của ứng dụng. Giữ các tập tin giấy phép/cấu hình/dữ liệu đi kèm.
5. Đọc hướng dẫn sử dụng của công cụ đó trước khi bật cài đặt hoặc thao tác hệ thống.

Các tệp nhị phân hiện tại không được ký. Hàm băm phù hợp xác nhận số byte dự kiến; nó không phải là chứng chỉ bảo mật hoặc tương thích. Không tắt các biện pháp bảo vệ bảo mật Windows chỉ để ngăn chặn cảnh báo.

Việc cài đặt NVDF hoặc đồng hành NVPI tùy chọn của nó tách biệt với việc cài đặt trình điều khiển GPU. Đồng hành NVPI vẫn giữ tên cài đặt nội bộ hiện có. Nút RasterPulse nâng cao của nó yêu cầu cài đặt trên toàn hệ thống được bảo vệ; các bản sao RP khác có thể được mở thông qua các phím tắt riêng.

NVMFG là thử nghiệm và có [ghi lại dự trữ cấp phép NVIDIA SDK](provenance.md). Không bao gồm trình điều khiển NVIDIA, nhà cung cấp/model NGX hoặc thời gian chạy trò chơi Streamline. Các bản tải xuống và cập nhật trò chơi SDK đã chọn là các hoạt động riêng biệt rõ ràng.

<a id="language-and-updates"></a>
## Ngôn ngữ và cập nhật

Sử dụng bộ chọn 34 ngôn ngữ của README cho tài liệu. NVDF, NVMFG và RP có cài đặt giao diện người dùng 34 ngôn ngữ riêng; NVPI vẫn duy trì hỗ trợ ngôn ngữ hiện có. Một số chuỗi kỹ thuật của trình cài đặt lại chuyển sang tiếng Anh.

Giữ danh tính cài đặt của công cụ khi cập nhật. Đóng nó trước và bảo quản các bản sao lưu. Đối với NVMFG, hãy đóng các trò chơi bị ảnh hưởng và giải quyết việc khôi phục hồ sơ đang chờ xử lý. Đối với các bản cập nhật di động, hãy sử dụng thư mục mới thay vì kết hợp các bản phát hành.

<a id="removing-a-tool"></a>
## Loại bỏ một công cụ

Việc gỡ cài đặt ứng dụng không tự động hoàn tác cài đặt của ứng dụng đó.

- **NVPI:** khôi phục cấu hình/cài đặt hiển thị dự định trước khi xóa nếu cần.
- **NVDF:** trước tiên hãy sử dụng khôi phục nếu bạn muốn khôi phục các thay đổi nâng cao/NVENC. Uninstall để lại trình điều khiển đồ họa, cài đặt và sao lưu.
- **NVMFG:** đóng trò chơi, tắt/thoát bộ điều khiển, giải quyết quá trình khôi phục NVIDIA và khôi phục bản sao lưu SDK của trò chơi mong muốn trước khi xóa.
- **RP:** trước tiên hãy loại bỏ các phần ghi đè giới hạn dự định. Uninstall không xóa các mũ RTSS đã lưu hoặc xóa RTSS.

Xem từng [hướng dẫn dự án](../README.md#projects) để biết vị trí và giới hạn dữ liệu chính xác hoặc [hỗ trợ](support.md) nếu bước khôi phục không thành công.
