<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Một fork độc lập của [NVIDIA Profile Inspector bởi Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), có thêm các điều khiển hiển thị.** Tên dự án cũ: **NVPI Custom**.

[Trạng thái tải xuống và phát hành](../docs/downloads.md#nvidia-profile-inspector) · [Cài đặt](#installation) · [Thượng nguồn và những thay đổi](#upstream-and-changes) · [Giấy phép](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Tổng quan

Ứng dụng chỉnh sửa cấu hình trình điều khiển NVIDIA, bao gồm cài đặt cho mỗi ứng dụng. fork này cũng bổ sung trình chỉnh sửa **Màn hình** cho màn hình Windows đang hoạt động: độ phân giải, tốc độ làm mới, cài đặt màu đầu ra, HDR và các liên kết cấu hình ICC/WCS được cài đặt.

Nó tồn tại để đưa các điều khiển hiển thị liên quan vào trình chỉnh sửa hồ sơ và làm cho kết quả xem trước, xác nhận và khôi phục rõ ràng hơn. Nó không thiết lập khả năng phần cứng mới.

Ứng cử viên đầu tiên là **3.0.2.3**, sử dụng bản dựng đồng hành độc lập đã được làm sạch từ ngày 9 tháng 9 năm 2026. Tệp thực thi hiện có của nó vẫn là `nvidiaProfileInspector.exe`; trình cài đặt và một số nhãn bên trong vẫn ghi `NVPI Custom NV`. Tiêu đề công khai ở trên xác định fork mà không thay đổi danh tính cài đặt hoặc giả vờ đó là bản phát hành chính thức của Orbmu2k.

<a id="features"></a>
## Tính năng

- Duyệt hồ sơ ngược dòng hiện có, liên kết ứng dụng, chỉnh sửa cài đặt và nhập/xuất hồ sơ.
- Hộp thoại **Màn hình** dành cho màn hình, chế độ, Hz, RGB/YCbCr, độ sâu màu, phạm vi và phép đo màu.
- Điều khiển Windows HDR và cài đặt lựa chọn liên kết ICC/WCS.
- Bản xem trước hiển thị 15 giây với **Keep** / **Revert** và khôi phục thời gian chờ.
- Đọc lại các thay đổi của chế độ/HDR và báo cáo lỗi khôi phục.
- Báo cáo riêng biệt về HDR, SDR với ACM/WCG và độ sâu màu tín hiệu.
- Trình khởi chạy NVRasterPulse dành cho bản sao được cài đặt riêng đủ điều kiện.

<a id="compatibility"></a>
## Khả năng tương thích

| Yêu cầu | Chi tiết |
| --- | --- |
| Hệ thống | Windows 10/11 x64 với trình điều khiển NVIDIA tương thích |
| Thời gian chạy | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), được cung cấp bởi Windows hoặc được lắp đặt riêng |
| Quyền | Người chỉnh sửa yêu cầu quyền truy cập của quản trị viên khi mở |
| Hiển thị | Các chế độ thực tế và sự kết hợp màu sắc phụ thuộc vào GPU, trình điều khiển, màn hình, cáp và API Windows |
| Công cụ tùy chọn | NVRasterPulse để quản lý giới hạn RTSS; cả RTSS đều không cần thiết cho Trình chỉnh sửa màn hình |
| Ngôn ngữ | Thiết lập: bộ chọn 34 ngôn ngữ. Trình soạn thảo vẫn giữ lại sự hỗ trợ ngôn ngữ hiện có. |

Không có ma trận hỗ trợ hoặc tối thiểu trình điều khiển chung được xác minh cho mọi GPU. Các lựa chọn bpc có sẵn của hộp thoại là các yêu cầu chứ không phải các kết hợp được chứng nhận. Các điều khiển HDR hiện đại và dự phòng Windows cũ hơn có các khả năng khác nhau.

<a id="installation"></a>
## Cài đặt

1. Mở [trang tải xuống](../docs/downloads.md#nvidia-profile-inspector) và kiểm tra trạng thái xuất bản.
2. Tải xuống Thiết lập hoặc tài sản di động và so sánh SHA-256 của nó với Bản kê khai phát hành.
3. Để Thiết lập, hãy chạy `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, chọn ngôn ngữ và làm theo trình cài đặt. Nó tạo lối tắt và trình gỡ cài đặt riêng.
4. Đối với thiết bị di động, hãy giải nén ZIP hoàn chỉnh vào một thư mục có thể ghi mới. Giữ `Reference.xml`, cấu hình EXE và tất cả các thông báo bên cạnh tệp thực thi.
5. Khởi chạy `nvidiaProfileInspector.exe`.

Chỉ cài đặt trình chỉnh sửa không áp dụng cấu hình hoặc cài đặt trình điều khiển GPU. Ứng dụng đồng hành cài đặt riêng, không tiếp quản các liên kết `.nip` và không cho phép khởi động khi đăng nhập. Các tệp nhị phân hiện có không được ký.

<a id="usage"></a>
## Cách sử dụng

**Bản sửa đổi trình cài đặt 2** thêm bộ chọn 34 ngôn ngữ gốc giống như các công cụ khác, với điều hướng bằng chuột/bàn phím, giao diện sáng/tối và tính năng hủy. Lựa chọn áp dụng cho việc thiết lập; nó không dịch trình soạn thảo NVPI. Đối số `/LANG=fr` rõ ràng hoặc chế độ im lặng bỏ qua lựa chọn đối với người gọi đã cung cấp ngôn ngữ.

**Cấu hình trình điều khiển:** chọn cấu hình, xuất bản sao lưu, sau đó chỉ chỉnh sửa các cài đặt mong muốn và áp dụng chúng. Các hiệp hội ứng dụng xác định trò chơi nào nhận được hồ sơ. Giá trị được lưu trữ không phải là bằng chứng cho thấy mọi trình điều khiển hoặc trò chơi đều sử dụng nó.

**Điều khiển hiển thị:** mở **Màn hình**, chọn hiển thị và giá trị được yêu cầu, sau đó bắt đầu xem trước. Kiểm tra hình ảnh trước khi chọn **Giữ** trong vòng 15 giây. Sử dụng **Hoàn nguyên**, đóng xác nhận hoặc để nó hết hạn để yêu cầu khôi phục. Đọc bất kỳ thông báo lỗi nào: chỉ lệnh gọi API thành công không phải là bằng chứng về việc khôi phục.

Lựa chọn ICC thay đổi liên kết hồ sơ đã cài đặt; nó không tạo, hiệu chỉnh hoặc phân phối lại tệp ICC. HDR, ACM/WCG, RGB/YCbCr và bpc mô tả các khía cạnh khác nhau của quy trình. Không có bộ chuyển mạch ACM độc lập mới nào được cung cấp.

**NVRasterPulse:** nút thanh công cụ chấp nhận cài đặt toàn hệ thống được đăng ký riêng bên dưới Tệp chương trình với quyền sở hữu và quyền được bảo vệ. Bản sao di động hoặc đường dẫn người dùng có thể ghi/liên kết có thể bị trình khởi chạy nâng cao này từ chối. Trong trường hợp đó, hãy mở NVRasterPulse bằng phím tắt riêng. [Cài đặt riêng RTSS](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) để sử dụng NVRasterPulse.

<a id="screenshots"></a>
## Ảnh chụp màn hình

![Bộ chọn ngôn ngữ sửa đổi 2 thiết lập NVPI](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Bộ chọn thiết lập thực tế bằng tiếng Pháp, được ghi lại trong quá trình kiểm tra riêng biệt và sau đó bị hủy. Điều này hiển thị trình cài đặt; trình soạn thảo vẫn giữ nguyên giao diện và hộp thoại Màn hình.

<a id="update-and-uninstall"></a>
## Cập nhật và gỡ cài đặt

Đóng trình chỉnh sửa trước khi cập nhật. Giữ các hồ sơ đã xuất và tải xuống Bản phát hành fork mới; cài đặt trên cùng một danh tính đồng hành hoặc giải nén các tệp di động vào một thư mục mới. Không trộn lẫn `Reference.xml` cũ với tệp thực thi mới. Việc ngăn chặn kiểm tra cập nhật ngược dòng đi kèm thuộc về fork này.

Để có bản sao đã cài đặt, hãy sử dụng Windows **Installed apps** và trình gỡ cài đặt của nó. Đối với thiết bị di động, hãy đóng nó và xóa thư mục đã giải nén khi quá trình xuất của bạn an toàn. Việc xóa trình chỉnh sửa sẽ **không** hoàn tác các chỉnh sửa hồ sơ trình điều khiển, hiển thị tùy chọn, NVRasterPulse hoặc RTSS. Khôi phục cài đặt mong muốn trước khi xóa.

<a id="known-limitations"></a>
## Những hạn chế đã biết

- Xác nhận 15 giây không phải là cơ quan giám sát đối với mọi sự cố của tài xế, mất điện hoặc buộc phải tắt máy.
- Một số kết hợp màu sắc/độ sâu/làm mới trả về `NVAPI_NOT_SUPPORTED`.
- Phần mềm đọc lại không đo độ sâu bit của bảng điều khiển, độ chính xác của màu sắc hoặc độ trễ.
- Cài đặt màn hình ảnh hưởng đến màn hình Windows hiện tại; hộp thoại này không tạo cài đặt trước hiển thị cho mỗi trò chơi.
- Không đảm bảo về hiệu suất, chống gian lận hoặc khả năng tương thích phổ quát HDR.

<a id="troubleshooting"></a>
## Khắc phục sự cố

| triệu chứng | hành động |
| --- | --- |
| Lỗi thời gian chạy khi khởi chạy | Kiểm tra các bản cập nhật Windows và .NET Framework 4.8; sử dụng gói hoàn chỉnh. |
| Chế độ hiển thị được yêu cầu bị từ chối | Hoàn nguyên và kiểm tra chế độ do Windows/NVIDIA cung cấp cho màn hình đó. Đọc lỗi chính xác và tránh những thay đổi mù quáng lặp đi lặp lại. |
| HDR hoặc màu trở về trạng thái cũ | Kiểm tra xem một thao tác khác có thất bại và kích hoạt khôi phục hay không; phân biệt HDR với ACM. |
| Nút NVRasterPulse từ chối đường dẫn | Khởi chạy phím tắt riêng của nó; nút này yêu cầu cài đặt toàn hệ thống được bảo vệ. |
| Một thay đổi vẫn còn sau khi gỡ cài đặt | Khôi phục cấu hình NVIDIA đã xuất hoặc cài đặt hiển thị Windows dự định; gỡ cài đặt không phải là khôi phục cài đặt. |

Xem [hướng dẫn hỗ trợ chia sẻ](../docs/support.md) trước khi gửi nhật ký.

<a id="faq"></a>
## Câu hỏi thường gặp

**Đây là phần mềm NVIDIA chính thức hay bản dựng chính thức của Orbmu2k?** Không. Đây là một fork độc lập; tác giả ngược dòng và giấy phép MIT vẫn được ghi nhận.

**NVDriverForge có yêu cầu trình chỉnh sửa này không?** Không. Cài đặt sẵn Custom NV tùy chọn của NVDriverForge sử dụng tích hợp riêng. Cài đặt trình soạn thảo là một lựa chọn riêng biệt.

**RTSS có bắt buộc đối với fork này không?** Không. RTSS là bắt buộc đối với bộ giới hạn FPS của NVRasterPulse, không dành cho chỉnh sửa hồ sơ hoặc màn hình.

**Nguồn ở đâu?** Nguồn ứng dụng đã sửa đổi được duy trì riêng tư. Thông báo MIT và kho lưu trữ ngược dòng được cung cấp; MIT không yêu cầu xuất bản nguồn đã sửa đổi.

<a id="upstream-and-changes"></a>
## Thượng nguồn và những thay đổi

Thượng nguồn: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), cam kết tham chiếu `592d962cca8827efe8859461a84267755595064a`. [Bản tải xuống gốc](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Kế thừa: trình chỉnh sửa hồ sơ, tương tác NVAPI, dữ liệu tham chiếu, tài nguyên và chủ đề giao diện người dùng. 禅堂 Zendo (RevoluSound Team) đã thêm hoặc điều chỉnh các dịch vụ hiển thị được điều chỉnh, giao dịch HDR/ICC, xác nhận/đọc lại 15 giây, bố cục thanh công cụ và hành vi khởi chạy RasterPulse. Ứng dụng đồng hành đã được làm sạch sẽ loại trừ các điểm nhập thử nghiệm/mô phỏng phát triển, sử dụng trình khởi chạy bên ngoài được bảo vệ và cung cấp trình cài đặt riêng. Gói phát triển NVPI/RasterPulse kết hợp cũ không phải là ứng cử viên trong trung tâm này.

[Xuất xứ tập tin chi tiết](../docs/provenance.md) · [Thông báo fork gốc](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Tín dụng và giấy phép

Bản quyền (c) 2016 Orbmu2k. [Giấy phép MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) được cung cấp vẫn được giữ lại. Điều chỉnh và đóng gói: 禅堂 Zendo (RevoluSound Team). Trình cài đặt sử dụng Inno Setup; Windows và .NET Framework vẫn ở bên ngoài. [Thông báo áp dụng đầy đủ](LICENSES/README.md).

Độc lập, không được tài trợ bởi và không được xác nhận chính thức bởi NVIDIA Corporation. Thương hiệu vẫn thuộc về chủ sở hữu tương ứng của họ.
