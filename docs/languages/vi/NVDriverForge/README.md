<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Chuẩn bị cài đặt trình điều khiển NVIDIA với các lựa chọn thành phần rõ ràng và cài đặt tùy chọn.**

[Tải xuống 0.1.3 & trạng thái](../docs/downloads.md#nvdriverforge) · [Cài đặt](#installation) · [Tín dụng](#credits-and-upstream) · [Giấy phép](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Tổng quan và mục đích

NVDriverForge hướng dẫn bạn qua gói trình điều khiển NVIDIA gốc: chọn trình điều khiển, kiểm tra các thành phần của nó, xem lại các chỉnh sửa tùy chọn, sau đó xác nhận cài đặt. Nó tồn tại để làm cho những lựa chọn đó trở nên dễ hiểu và giữ thông tin cài đặt, hoạt động đặc quyền và khôi phục cùng nhau.

Nó là một ứng dụng được phát triển độc lập lấy cảm hứng một phần từ quy trình làm việc của NVCleanstall. Nó không bao gồm NVCleanstall hoặc yêu cầu tính năng tương đương hoàn chỉnh.

<a id="features"></a>
## Tính năng

- Tra cứu và tải xuống NVIDIA Game Ready / Studio; khám phá hotfix tùy chọn với dự phòng thủ công.
- Phân tích gói gốc, hàm băm, chữ ký NVIDIA, bảng kê khai và các mục nhập INF tương thích.
- Lựa chọn thành phần với sự phụ thuộc và bảo tồn các thành phần chưa biết.
- Phiên bản 0.1.3 giữ cho các thành phần NVIDIA tùy chọn đã chọn có thể bỏ qua và chỉ loại trừ các thành phần chưa được kiểm tra đã được xác minh khỏi quá trình khám phá. Thời gian chạy tùy chọn hiện tại hoặc không thể áp dụng không còn bị coi là thành phần quan trọng nữa.
- Xóa các bản tóm tắt lỗi cài đặt và truy cập vào nhật ký chi tiết bằng tất cả 34 ngôn ngữ.
- Xác nhận cài đặt rõ ràng, dàn dựng được bảo vệ và xuất các gói lưu trữ trình điều khiển hiện có.
- Cài đặt nâng cao tùy chọn, với kiểm tra trước chuyến bay, nhật ký và khôi phục nhận biết xung đột.
- Tùy chọn cài sẵn **Custom NV** với các lựa chọn và giải thích được đặt tên, bao gồm lựa chọn cường độ SILK riêng biệt và kiểm tra khả năng tương thích.
- Tùy chọn tải xuống bản vá NVENC phiên bản chính xác; cam kết nguồn và byte đích được kiểm tra.
- Cài đặt tùy chọn, riêng biệt của Profile Inspector fork từ màn hình Công cụ.
- Kiểm tra cập nhật người dùng đã cài đặt tùy chọn, 34 ngôn ngữ giao diện và bốn chủ đề.

Các tùy chọn nâng cao có sẵn liên quan đến MPO, chỉ báo DLSS, Ansel, chế độ ngủ âm thanh NVIDIA, MSI, chính sách/ưu tiên ngắt, HDCP, khởi động vùng chứa màn hình và dịch vụ đo từ xa kế thừa đủ điều kiện. Mỗi cái đều có những điều kiện tiên quyết và tác dụng riêng; đây không phải là những cải tiến hiệu suất phổ quát.

<a id="compatibility"></a>
## Khả năng tương thích

| Yêu cầu | Chi tiết |
| --- | --- |
| Hệ thống | Windows 10 bản dựng 19041 hoặc mới hơn / Windows 11, x64 |
| GPU/trình điều khiển | Gói NVIDIA tương thích và phần cứng được phát hiện; tra cứu danh mục tự động chủ yếu bao gồm các mẫu GeForce đã biết |
| Thời gian chạy | .NET 8/WPF 8.0.31 có trong gói khép kín đã được chuẩn bị sẵn |
| Đặc quyền | Thiết lập giao diện người dùng/mỗi người dùng thông thường; cài đặt trình điều khiển và thay đổi hệ thống yêu cầu quyền truy cập của quản trị viên |
| Mạng | Cần thiết cho việc tra cứu/tải xuống NVIDIA trực tuyến và các yêu cầu ngược dòng rõ ràng của NVENC; một trình điều khiển gốc cục bộ có thể được chọn |
| Công cụ đi kèm | 7-Zip 26.03 chưa sửa đổi, thông báo thời gian chạy, đồng hành MIT Profile Inspector tùy chọn |
| Bạn đồng hành tùy chọn | .NET Framework 4.8 cho Profile Inspector fork riêng |

Không có phiên bản trình điều khiển tối thiểu tùy ý nào bao gồm tất cả các tính năng. Tra cứu nhiều GPU phải khớp với mọi GPU được phát hiện. Các mẫu máy chuyên nghiệp/không được hỗ trợ có thể yêu cầu lựa chọn trình điều khiển thủ công. Trình cài đặt của NVIDIA vẫn là cơ quan có thẩm quyền về phần cứng/HĐH cuối cùng.

<a id="installation"></a>
## Cài đặt

1. Truy cập [lượt tải xuống](../docs/downloads.md#nvdriverforge) và xác nhận Bản phát hành đã được xuất bản.
2. Chọn `NVDriverForge-Setup.exe` để cài đặt hoặc `NVDriverForge.exe` để sử dụng di động.
3. So sánh SHA-256 với `SHA256SUMS.txt` của Bản phát hành.
4. Chạy Thiết lập để cài đặt cho mỗi người dùng và trình gỡ cài đặt tiêu chuẩn hoặc đặt EXE di động vào một thư mục có thể ghi và mở nó.

Bản di động bao gồm thời gian chạy và trình cài đặt tùy chọn của nó. Cài đặt NVDriverForge không cài đặt trình điều khiển GPU. EXE của nó hiện chưa được ký.

<a id="usage"></a>
## Cách sử dụng

1. **Trình điều khiển:** tải xuống từ NVIDIA hoặc chọn EXE trình cài đặt NVIDIA gốc. Hãy để phân tích kết thúc.
2. **Thành phần:** xem xét mô tả và các phần phụ thuộc bắt buộc. Các thành phần không xác định được giữ lại.
3. **Chỉnh sửa:** giữ nguyên các tùy chọn không mong muốn. Đọc các hiệu ứng và sự đánh đổi trước khi chọn bất cứ thứ gì.
4. **Đánh giá:** kiểm tra chính xác trình điều khiển, các thành phần và các thao tác tùy chọn, sau đó xác nhận cài đặt.
5. Chỉ chấp nhận UAC cho thao tác bạn đã chọn. Giữ hướng dẫn khôi phục công việc được bảo vệ.
6. Nếu trình điều khiển mới cần khởi động lại, hãy làm theo trạng thái được báo cáo. Hoạt động bị trì hoãn yêu cầu tiếp tục rõ ràng sau lần khởi động lại đó.

Custom NV bắt đầu không thay đổi. Chọn các giá trị được đặt tên riêng lẻ hoặc xem lại giá trị đặt trước được cung cấp và các loại trừ của nó. Hai trường thông tin nội bộ của nó không được viết độc lập. Cài đặt chỉ được áp dụng trong quy trình làm việc của trình điều khiển mới đã được xác minh, không bao giờ được áp dụng bằng cách mở bản xem trước. Không cần cài đặt trình soạn thảo NVPI riêng biệt.

Công việc NVENC tùy chọn tải xuống dữ liệu tương thích từ cam kết keylase được ghim. Nó thay đổi hai tệp DLL trình điều khiển và vô hiệu hóa chữ ký của chúng; nó có thể bị từ chối bởi Windows, bộ mã hóa, DRM hoặc tính năng chống gian lận. Không có dữ liệu như vậy hoặc NVIDIA DLL được nhúng trong NVDriverForge. [Giới hạn xuất xứ và cấp phép](../docs/provenance.md).

Tùy chọn kiểm soát ngôn ngữ, chủ đề và kiểm tra cập nhật người dùng đã cài đặt tùy chọn. Thiết bị di động không tạo tác vụ kiểm tra lý lịch đã cài đặt. Công cụ và quá trình khôi phục tách biệt với bốn bước cài đặt.

<a id="screenshots"></a>
## Ảnh chụp màn hình

![Xem trước trang trình điều khiển NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Kết xuất giao diện người dùng tiếng Pháp 0.1.2 hiện có với dữ liệu mẫu; được giữ lại dưới dạng bản xem trước giao diện. Trình điều khiển 699.99 được hiển thị là bản cố định thử nghiệm, không phải phiên bản thực để tải xuống. [Nguồn gốc hình ảnh](../assets/README.md).

<a id="update-and-uninstall"></a>
## Cập nhật và gỡ cài đặt

Đóng NVDriverForge, lấy gói chính thức tiếp theo và xác minh hàm băm của nó. Sử dụng cùng một danh tính Thiết lập cho bản cập nhật đã cài đặt; thay thế một EXE di động đã đóng bằng một cái mới. Giữ các cài đặt và công việc được bảo vệ.

Uninstall từ Windows **Installed apps**. Nó xóa ứng dụng và tác vụ cập nhật của nó, không phải trình điều khiển NVIDIA. Cài đặt, nhật ký và bản sao lưu vẫn còn. Nếu muốn, hãy khôi phục các thay đổi nâng cao/NVENC thông qua quy trình khôi phục được ghi lại **trước khi** xóa ứng dụng. Khôi phục từ chối các thay đổi xung đột từ một công cụ khác.

Dữ liệu cục bộ dưới `%LOCALAPPDATA%\NVDriverForge`; việc làm được bảo vệ và xuất khẩu tài xế thuộc `%PROGRAMDATA%\NVDriverForge\Jobs`. Việc sử dụng di động cũng tạo ra dữ liệu cục bộ. Xuất kho trình điều khiển không phải là hình ảnh hệ thống hoặc bản sao lưu hồ sơ đầy đủ.

<a id="known-limitations"></a>
## Những hạn chế đã biết

- Không có bổ sung phần cứng/chỉnh sửa INF, chữ ký NVIDIA được tái tạo, từ chức tương thích chống gian lận hoặc chấp nhận cảnh báo không dấu tự động.
- Không loại bỏ hoàn toàn phép đo từ xa/quảng cáo, xuất gói mỏng hoặc tự động khôi phục hoàn toàn về trình điều khiển trước đó.
- Việc cài đặt trình điều khiển, khôi phục khởi động và ghi hồ sơ tùy chọn chưa được xác thực toàn diện trên các máy thực bằng quá trình kiểm tra trung tâm.
- Việc đọc lại sổ đăng ký không phải là bằng chứng về hiệu ứng HDCP, hiệu suất hoặc độ trễ thực tế.
- Kiểm tra chữ ký sử dụng tin cậy Windows có sẵn tại địa phương; việc thu hồi trực tuyến không được thực hiện.
- Có 34 ngôn ngữ nhưng việc kiểm tra đầy đủ người bản ngữ/khả năng tiếp cận vẫn chưa hoàn thiện.

<a id="troubleshooting"></a>
## Khắc phục sự cố

| triệu chứng | hành động |
| --- | --- |
| Danh mục trực tuyến không có sẵn | Chọn gói gốc từ [Tải xuống trình điều khiển NVIDIA](https://www.nvidia.com/en-us/drivers/). Không thay thế mẫu GPU lân cận. |
| Tra cứu hotfix không có sẵn | Sử dụng [Diễn đàn trình điều khiển Game Ready của NVIDIA](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) và xác minh gói thực tế. |
| Cài đặt NVIDIA không thành công | Đọc bản tóm tắt lỗi và mở nhật ký chi tiết. Các thành phần tùy chọn đã có sẵn hoặc không thể áp dụng vẫn có thể bỏ qua trong 0.1.3. Các lượt cài đặt không thành công sẽ không kích hoạt các chỉnh sửa tùy chọn hoặc quy trình thành công/khởi động lại. |
| Lỗi chữ ký/băm/sao lưu | Dừng cài đặt đó và giữ lại lỗi; lấy lại gói gốc nếu bị hỏng. |
| Tùy chọn không có sẵn | Đọc lý do phần cứng, thành phần hoặc trình điều khiển đích của nó; giữ nó không thay đổi. |
| Khởi động lại hoặc công việc vẫn đang chờ xử lý | Sử dụng hướng dẫn khôi phục công việc và sơ yếu lý lịch rõ ràng; không xóa tạp chí của nó. |
| Khôi phục xung đột | Một trạng thái khác khác với giao dịch được ghi lại. Giữ nó và yêu cầu trợ giúp thay vì buộc phải khôi phục. |

Đối với các báo cáo, hãy bao gồm phiên bản công cụ đã chọn, Windows, GPU, trình điều khiển và các bước có thể tái tạo; biên tập lại đường dẫn và thông tin cá nhân từ nhật ký. [Hỗ trợ](../docs/support.md).

<a id="faq"></a>
## Câu hỏi thường gặp

**Thiết lập có cài đặt trình điều khiển đồ họa không?** Không. Điều đó yêu cầu quá trình phân tích, đánh giá, xác nhận và cài đặt nâng cao riêng biệt của ứng dụng.

**Tôi có cần NVCleanstall hay NVPI không?** Không. NVCleanstall chỉ là nguồn cảm hứng. Người bạn đồng hành Profile Inspector là một trình soạn thảo tùy chọn độc lập.

**Nó có làm cho mọi trình điều khiển NVIDIA nhỏ hơn hoặc nhanh hơn không?** Không. Các thành phần và điều kiện tiên quyết được chọn sẽ xác định những gì có thể thay đổi; không có mức tăng đo lường nào được hứa hẹn.

**Nguồn ở đâu?** Nguồn dành riêng cho ứng dụng và các thử nghiệm riêng tư được duy trì riêng biệt. Trung tâm này cung cấp tài liệu, tệp nhị phân và các liên kết nguồn của bên thứ ba cần thiết cho việc ghi công/cấp phép.

<a id="credits-and-upstream"></a>
## Tín dụng và thượng nguồn

Ứng dụng gốc, quy trình làm việc, giao dịch, bản địa hóa, khởi động và điều chỉnh: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): nguồn cảm hứng cho quy trình làm việc; không có nguồn hoặc nhị phân được nhập.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): Chủ đề MIT, tham chiếu giao diện NVAPI mở rộng và fork được đóng gói riêng.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): công cụ trích xuất chưa sửa đổi.
- [Microsoft .NET](https://github.com/dotnet/runtime) và [WPF](https://github.com/dotnet/wpf): thời gian chạy đi kèm.
- [Inno Setup](https://jrsoftware.org/isinfo.php): công cụ cài đặt gốc và bản dịch được ghi có.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): nguồn dữ liệu NVENC tùy chọn bên ngoài; giấy phép phân phối lại không được thành lập.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): tải xuống trình điều khiển bên ngoài và cài đặt thư viện NVAPI/NVML.

[Bảng thành phần đầy đủ](../THIRD_PARTY_NOTICES.md) · [Những thay đổi và xuất xứ](../docs/provenance.md)

<a id="license"></a>
## Giấy phép

[Quyền phân phối nhị phân hiện có](../../../../NVDriverForge/LICENSE) cho phép sử dụng và chia sẻ các tệp thực thi chính thức chưa sửa đổi kèm theo thông báo của họ. Quyền nguồn dành riêng cho ứng dụng được bảo lưu. Nó không hạn chế các quyền được cấp bởi các giấy phép riêng biệt của bên thứ ba. [Thông báo đầy đủ](LICENSES/README.md).

Độc lập với NVIDIA Corporation, TechPowerUp và keylase; không được họ tài trợ hoặc xác nhận chính thức. Tên sản phẩm vẫn là thương hiệu của chủ sở hữu.
