<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Kiến trúc và bảo trì kho lưu trữ

NV Laboratory là một **trung tâm phân phối tài liệu và nhị phân** công khai. Nó không chứa nguồn ứng dụng. Bốn dự án giữ lại cây xây dựng, phiên bản, danh tính và nội dung phát hành riêng biệt. Lịch sử phát triển riêng tư của họ không được nhập vào kho Git này.

<a id="layout"></a>
## Bố cục

| Vị trí | Mục đích |
| --- | --- |
| README.md / README.fr.md | Điểm đầu vào tiếng Anh/tiếng Pháp |
| Bốn thư mục dự án | Hướng dẫn đầy đủ và thông báo gốc hiện hành |
| tài liệu | Quy trình tải xuống, khả năng tương thích, xuất xứ, phát triển và phát hành |
| tài liệu/releases.json | Siêu dữ liệu, kích thước và giá trị băm đã được kiểm tra của ứng viên/bản phát hành |
| tài liệu/xuất xứ | So sánh tệp/băm; không có mã ứng dụng |
| giấy phép | Đã chia sẻ đầy đủ văn bản của bên thứ ba và ghi công của người dịch trình cài đặt |
| tài sản | Các bản xem trước giao diện người dùng đã được đánh giá hiện có và nguồn gốc của chúng |
| .github | Biểu mẫu phát hành và xác thực tài liệu chỉ đọc |
| công cụ/validate_repository.py | Kiểm tra liên kết và ranh giới xuất bản của thư viện tiêu chuẩn |

Tiếng Anh vẫn là GitHub README mặc định. Các liên kết `.fr.md` liền kề hiện có vẫn hợp lệ. Các bản dịch bổ sung phản ánh tài liệu theo `docs/languages/<code>`; bộ chọn ngôn ngữ giữ nguyên một trang khi chuyển đổi ngôn ngữ. Danh mục `docs/languages/catalog.json` ghi lại tất cả 34 ngôn ngữ và dấu vân tay nguồn. GitHub không tự động chọn README theo ngôn ngữ trình duyệt. Xem [chỉ mục ngôn ngữ và chính sách dịch thuật](../../README.md).

<a id="application-technologies"></a>
## Công nghệ ứng dụng

| chương trình | Công nghệ tư nhân | Phân phối |
| --- | --- | --- |
| NVPI fork | Tương tác C#, WPF, .NET Framework 4.8, NVAPI/Windows | Hoàn thành thư mục di động và Inno Setup riêng biệt |
| NVDriverForge | C#, WPF, .NET 8; bootstrap C++ nguyên gốc; Quá trình 7-Zip | EXE di động độc lập và thiết lập |
| NVMFG Unlock40 | C#/WPF .NET 8, Trình trợ giúp Framework 4.8, công cụ C++20/MASM/MinHook | Cây di động và thiết lập |
| NVRasterPulse | Khung C#/WPF 4.8; Tích hợp hồ sơ/tải lại RTSS; khởi động tự nhiên | Cây di động và thiết lập |

Thanh toán công khai này không thể xây dựng lại các ứng dụng. Bản lưu trữ “Source code” tự động là ảnh chụp nhanh trung tâm. Liên kết nguồn ngược dòng không đại diện chính xác cho nguồn được sửa đổi riêng tư. CI công khai chỉ xác thực kho lưu trữ này.

<a id="local-checks"></a>
## Séc địa phương

Từ kho lưu trữ gốc:

```text
python tools/validate_repository.py
```

Python 3.10 hoặc mới hơn là đủ. Kiểm tra đọc các tệp, liên kết Markdown cục bộ, thông báo bắt buộc/liên kết RTSS, siêu dữ liệu phát hành và ranh giới xuất bản. Nó không thực thi phần mềm, cài đặt các phần phụ thuộc hoặc liên hệ với mạng.

Luồng công việc GitHub thực hiện kiểm tra tương tự với quyền nội dung chỉ đọc đối với yêu cầu đẩy, kéo hoặc gửi thủ công. Thanh toán được ghim vào một cam kết đã được kiểm tra và không duy trì bằng chứng xác thực. Không có công việc phát hành hoặc triển khai nào được định cấu hình.

<a id="maintain-the-boundary"></a>
## Duy trì ranh giới

Cập nhật tài liệu tham khảo tiếng Anh, hướng dẫn tiếng Pháp và các bản dịch bị ảnh hưởng cùng nhau. Giữ những thay đổi quan trọng tách biệt khỏi những so sánh chỉ có định dạng. Ghi lại các giá trị băm ứng viên thực tế, các tham chiếu và giấy phép cam kết ngược dòng; không bao giờ suy ra giấy phép từ mức độ phổ biến của dự án.

Sử dụng nội dung Bản phát hành được phiên bản mới và kiểm tra lại các tệp nhị phân, kho lưu trữ và thông báo được nhúng đã thay đổi. Bảo toàn các bản sao lưu riêng tư bên ngoài kho lưu trữ này. Không sử dụng quy trình làm việc công khai để nhập nguồn ứng dụng riêng tư hoặc thư mục bản dựng cục bộ.

Các thử nghiệm phù hợp với thay đổi ứng dụng chức năng được thực hiện trong dự án riêng. Không chạy lại trình cài đặt trình điều khiển hoặc viết hồ sơ thực để cập nhật tài liệu. [Thủ tục phát hành thủ công](releasing.md).
