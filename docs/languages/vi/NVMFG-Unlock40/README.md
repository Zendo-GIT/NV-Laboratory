<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**NVIDIA Multi Frame Generation thử nghiệm dành cho GeForce RTX 40, với bộ điều khiển trung tâm và các lựa chọn cho mỗi trò chơi.**

[Tải xuống 0.1.1 & trạng thái](../docs/downloads.md#nvmfg-unlock40) · [Cài đặt](#installation) · [Thượng nguồn](#upstream-and-modifications) · [Giấy phép](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Tổng quan và mục đích

NVMFG Unlock40 là một ứng dụng được phát triển độc lập bởi 禅堂 Zendo (RevoluSound Team). Nó kết hợp bộ điều khiển Windows, lớp gốc, trình trợ giúp hồ sơ và quản lý trò chơi/Streamline SDK. Nó nhắm đến các trò chơi đã tích hợp NVIDIA DLSS Frame Generation và thời gian chạy NVIDIA tương thích.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) đã được tư vấn để so sánh và chắt lọc công việc. Lớp gốc hiện tại chứa các thành phần được chia sẻ và điều chỉnh, được ghi riêng bên dưới. Tham chiếu này không làm cho toàn bộ ứng dụng NVMFG trở thành fork của dự án đó.

Nó tồn tại để điều phối tập trung hành vi MFG thử nghiệm, ghi nhớ các lựa chọn dành riêng cho trò chơi và luôn hiển thị các bản cập nhật thời gian chạy và bản sao lưu. Nó không thêm DLSS Frame Generation vào mọi trò chơi hoặc chuyển đổi cách triển khai FSR tùy ý.

Ứng viên đã chuẩn bị là **0.1.1**, bao gồm cả tính năng chỉnh sửa trực quan trong danh sách SDK được ghi nội bộ dưới dạng UI2. Phiên bản công khai vẫn là 0.1.1; giá trị băm chính xác của nó giúp phân biệt ứng cử viên này với các bản dựng cục bộ cũ hơn.

<a id="features"></a>
## Tính năng

- Điều khiển bật/tắt trung tâm và khởi động khay Windows tùy chọn.
- Lựa chọn mỗi trò chơi giữa Dynamic MFG, cài đặt của trò chơi và hệ số nhân cố định được hỗ trợ.
- Các lựa chọn được ghi nhớ riêng biệt cho các trạng thái bật/tắt V-Sync được quan sát.
- Dynamic sử dụng chế độ của NVIDIA; nó bị treo khi V-Sync tắt, với một lựa chọn cố định/trong trò chơi riêng biệt.
- Hướng dẫn về menu trò chơi và loại trừ liên tục; các trò chơi không có DLSS FG vẫn nắm quyền kiểm soát.
- Khám phá trò chơi, lựa chọn thư mục mẹ, tìm kiếm, nhóm và xóa mà không xóa các tập tin trò chơi.
- Tải xuống/nhập Streamline SDK, bộ đệm cục bộ đã được xác minh, lựa chọn rõ ràng, sao lưu và khôi phục mỗi trò chơi.
- Xác minh nhà cung cấp gốc, chẩn đoán mỗi phiên, nhật ký hồ sơ toàn cầu và khôi phục nhận biết xung đột.
- 34 ngôn ngữ giao diện và bốn chủ đề.

Tắt FG trong trò chơi sẽ tắt nó. Các lựa chọn cố định từ 2x đến 6x tùy thuộc vào trò chơi/menu/thời gian chạy; chúng không phải là lời hứa rằng mọi sự kết hợp đều có tác dụng. Bộ điều khiển quan sát V-Sync và không đặt V-Sync hoặc VRR cho người dùng.

<a id="compatibility"></a>
## Khả năng tương thích

| Yêu cầu | Chi tiết |
| --- | --- |
| Hệ thống | Windows 10/11 x64 |
| GPU | Mục tiêu GeForce RTX 40; không có yêu cầu tương thích phổ biến GPU |
| trò chơi | Tích hợp NVIDIA DLSS Frame Generation hiện có và thời gian chạy được hỗ trợ; không có chứng nhận tương thích chống gian lận |
| nhà cung cấp | Ứng viên được ghim vào nhà cung cấp SHA-256 được ghi trong [xuất xứ](../docs/provenance.md); băm không xác định bị từ chối |
| Thời gian chạy | Đi kèm .NET 8/WPF 8.0.30 cho ứng dụng/tác nhân; .NET Framework 4.8 dành cho người trợ giúp hồ sơ |
| Quyền | Quyền truy cập của quản trị viên đối với các hoạt động của bộ điều khiển/hồ sơ |
| Mạng | Cần thiết cho các bản tải xuống SDK chính thức đã chọn; SDKs tương thích đã nhập có thể được lưu vào bộ nhớ đệm cục bộ |
| Tệp nhị phân bên ngoài | Trình điều khiển NVIDIA, nhà cung cấp/mô hình NGX và thời gian chạy trò chơi Streamline không được đóng gói |

Chỉ nhãn phiên bản là không đủ: trình điều khiển, hàm băm của nhà cung cấp, tích hợp trò chơi và các mô-đun được tải thực tế đều quan trọng. Các quy trình được bảo vệ hoặc không tương thích có thể từ chối tệp đính kèm. Ứng dụng này không được thiết kế để trốn tránh các biện pháp bảo vệ chống gian lận.

<a id="installation"></a>
## Cài đặt

1. Đọc [tình trạng ứng cử viên và lưu ý cấp phép](../docs/downloads.md#nvmfg-unlock40).
2. Tải xuống `NVMFGUnlock40-0.1.1-Setup-x64.exe` hoặc `NVMFGUnlock40-0.1.1-Portable-x64.zip` khi có Bản phát hành.
3. Kiểm tra SHA-256 và lưu giữ các thông báo kèm theo. Cài đặt .NET Framework 4.8 nếu Windows chưa cung cấp.
4. Chạy Thiết lập hoặc trích xuất **toàn bộ** ZIP di động vào một thư mục cục bộ có thể ghi.
5. Khởi chạy `NVMFGUnlock40.exe`; giữ `agent`, `driver`, `engine` và `Licenses` trong bố cục được cung cấp.

Thư mục có tên `driver` chứa trình trợ giúp không gian người dùng, không phải trình điều khiển kernel. Không chỉ sao chép EXE chính hoặc thay thế hàm băm của nhà cung cấp để buộc tính tương thích. Các EXE hiện tại chưa được ký.

<a id="usage"></a>
## Cách sử dụng

1. Bắt đầu với bộ điều khiển bị vô hiệu hóa. Thêm trò chơi hoặc thư mục mẹ và chọn cài đặt thực tế.
2. Xem lại cài đặt MFG của mỗi trò chơi. Trả lời những gì menu của nó cung cấp; câu trả lời được lưu trữ cho mỗi trò chơi.
3. Chọn Dynamic hoặc cài đặt trong trò chơi trên toàn cầu, sau đó điều chỉnh các lựa chọn đủ điều kiện cho mỗi trò chơi nếu cần.
4. Chỉ kích hoạt bộ điều khiển khi bạn có ý định sử dụng nó. Nó có thể tạm thời thay đổi sáu cài đặt hồ sơ NVIDIA toàn cầu, với nhật ký khôi phục.
5. Khởi chạy một trò chơi đủ điều kiện và kích hoạt DLSS Frame Generation của riêng trò chơi đó. Thực hiện theo bất kỳ yêu cầu nào về lựa chọn tắt V-Sync.
6. Sử dụng loại trừ cho các trò chơi mà bạn không muốn quản lý. Việc xóa trò chơi sẽ ghi lại một tùy chọn loại trừ và giữ nguyên các tệp/bản sao lưu của trò chơi đó.
7. Sử dụng toàn bộ quy trình thoát/vô hiệu hóa và khôi phục của ứng dụng khi hoàn tất.

Đóng cửa sổ chính có thể để lại bộ điều khiển trong khay. Một DLL đã được tải vào trò chơi vẫn ở đó cho đến khi trò chơi thoát; vô hiệu hóa bộ điều khiển không phải là một đảm bảo dỡ tải. Đóng các trò chơi bị ảnh hưởng trước khi bảo trì hoặc cập nhật.

**Streamline SDKs:** trên trang NVIDIA SDK, tải xuống phiên bản chính thức hoặc nhập SDK cục bộ tương thích. Nhập lưu trữ một bản sao đã được xác minh; **Use this version** chọn nó và **Uninstall** xóa bản sao đã lưu trong bộ nhớ đệm đó. Các DLL Streamline bị thiếu có thể được bổ sung từ NVIDIA SDK chính thức, với nguồn được hiển thị. Điều này không tải xuống/thay thế mẫu NGX. Đóng trò chơi, chọn bản cập nhật trò chơi dự định và giữ lại bản sao lưu ban đầu. Để hoàn nguyên các tệp trò chơi, hãy sử dụng khôi phục bản sao lưu của nó chứ không phải nút Uninstall của bộ đệm.

<a id="screenshots"></a>
## Ảnh chụp màn hình

![Xem trước danh sách NVMFG SDK](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Kết xuất giao diện 0.1.1 tiếng Anh hiện có với kho lưu trữ SDK mẫu. Đây không phải là danh sách phiên bản hiện tại hoặc bằng chứng về một trò chơi đang chạy. [Nguồn gốc hình ảnh](../assets/README.md).

<a id="update-and-uninstall"></a>
## Cập nhật và gỡ cài đặt

Đóng các trò chơi bị ảnh hưởng. Tắt/thoát NVMFG và giải quyết mọi khôi phục cài đặt NVIDIA đang chờ xử lý trước khi cập nhật. Cài đặt Thiết lập tiếp theo với danh tính hiện có hoặc trích xuất bản di động mới vào một thư mục mới; giữ lại trạng thái/sao lưu.

Trước khi gỡ cài đặt, hãy khôi phục các bản sao lưu SDK và cài đặt NVIDIA mong muốn thông qua ứng dụng, sau đó đóng trò chơi và thoát khỏi bộ điều khiển. Sử dụng Windows **Installed apps** để Thiết lập hoặc xóa thư mục di động đã đóng sau khi bảo quản các tệp cần thiết. Không xóa thủ công nhật ký khôi phục đang hoạt động để bỏ chặn Thiết lập.

Bản sao lưu thời gian chạy trò chơi cục bộ sử dụng `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Cài đặt MFG/dữ liệu SDK sử dụng `%LOCALAPPDATA%\RtxMfg`; đầu ra phiên nằm dưới `Sessions` bên cạnh ứng dụng. Những tập tin này có thể chứa đường dẫn trò chơi. Đừng đăng chúng mà không được chỉnh sửa.

<a id="known-limitations"></a>
## Những hạn chế đã biết

- Các bản vá gốc thử nghiệm có thể gây ra sự cố hoặc tạo tác hình ảnh; một sự cố Bodycam chưa được giải quyết đã được ghi lại trong lịch sử phát triển.
- Các thử nghiệm kết xuất có kiểm soát không phải là chứng nhận cho mọi trò chơi, trình điều khiển hoặc tính năng chống gian lận.
- Các khung được tạo không tạo các mẫu đầu vào mới; trung tâm này không hứa hẹn độ trễ hoặc mức tăng hiệu suất đo được.
- Nhiều công cụ/lớp phủ tạo khung có thể xung đột. Ứng dụng báo cáo các mô-đun đã quan sát mà không chứng minh mọi kịch bản cùng tồn tại.
- Bản kê khai khả năng tương thích là công cụ hỗ trợ phát hiện chứ không phải danh sách các trò chơi đã được kiểm tra đầy đủ.
- Các điều khoản đầy đủ của NVIDIA SDK và hạn chế giới hạn kỹ thuật chưa được giải quyết vẫn được ghi lại trong [xuất xứ](../docs/provenance.md).

<a id="troubleshooting"></a>
## Khắc phục sự cố

| triệu chứng | hành động |
| --- | --- |
| Nhà cung cấp không được hỗ trợ | Giữ các tập tin được xác minh ban đầu. Báo cáo phiên bản trình điều khiển/nhà cung cấp và lỗi; không bỏ qua việc kiểm tra hàm băm. |
| Không có DLSS FG trong trò chơi | Chọn câu trả lời đó và để trò chơi trong tầm kiểm soát; công cụ này không thể tạo ra sự tích hợp đó. |
| Sự cố/hiện vật trong trò chơi | Thoát khỏi trò chơi, tắt NVMFG, sử dụng bản sao lưu thời gian chạy ban đầu của trò chơi nếu nó bị thay đổi và báo cáo các chi tiết có thể tái tạo. |
| Danh sách hoặc tải xuống SDK không có sẵn | Làm mới và kiểm tra nguồn chính thức; phiên bản được lưu vào bộ nhớ đệm/được nhập vẫn phải vượt qua quá trình xác thực. |
| Đang chờ khôi phục NVIDIA chặn thoát/cập nhật | Sử dụng phục hồi và bảo quản nhật ký; xung đột không được ghi đè một cách mù quáng. |
| Trò chơi đã xóa không được khám phá lại | Sự loại trừ của nó là dai dẳng. Thêm nó một cách rõ ràng khi bạn muốn nó được quản lý lại. |

[Hướng dẫn hỗ trợ được chia sẻ](../docs/support.md) giải thích những gì cần đưa vào báo cáo.

<a id="faq"></a>
## Câu hỏi thường gặp

**Nó có bao gồm các tệp hoặc mô hình NVIDIA không?** Không bao gồm trình điều khiển, nhà cung cấp/mô hình NGX hoặc thời gian chạy Streamline. Các bản tải xuống SDK rõ ràng đến từ NVIDIA.

**Dynamic có hoạt động khi tắt V-Sync không?** Nó bị treo ở trạng thái đó. Chọn cài đặt trong trò chơi hoặc hệ số nhân cố định đủ điều kiện cho trạng thái riêng của trò chơi đó.

**Đây có phải là gói ReShade/OptiScaler/FSR không?** Không. Những gói này không được biên soạn hoặc vận chuyển như một phần của gói sản xuất này.

**Các nguồn được sửa đổi có được công khai không?** Không. Các gói đã biên soạn và các khoản tín dụng/giấy phép bắt buộc đều được cung cấp. Điều này không loại bỏ quyền hoặc hạn chế của bên thứ ba.

<a id="upstream-and-modifications"></a>
## Thượng nguồn và sửa đổi

Tham chiếu so sánh và các thành phần gốc được chia sẻ: **RTX40MFG-Unlock của Michael Robles / dashdogy**, cam kết tham chiếu `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Kho lưu trữ](https://github.com/dashdogy/RTX40MFG-Unlock) · [Bản tải xuống gốc](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

So sánh nguồn xác định bản vá được chia sẻ, xử lý nhà cung cấp/chính sách, sửa lỗi tạm thời và các thành phần đi vòng dựa trên MinHook. Thông báo MIT và BSD của họ được giữ lại. Việc so sánh hoàn chỉnh cũng bao gồm các tệp nằm ngoài mục tiêu sản xuất.

Ứng dụng máy tính để bàn, bộ điều khiển và quy trình quản lý SDK được phát triển bởi 禅堂 Zendo (RevoluSound Team). Công việc của dự án bao gồm tải trung tâm, tích hợp khởi động NGX, lựa chọn nhà cung cấp đã được xác minh, phối hợp trò chơi/V-Sync và chẩn đoán phiên. Hướng dẫn xuất xứ tách biệt công việc đó khỏi các thành phần được chia sẻ; chỉ việc so sánh tập tin không xác định được thời điểm một trong hai tác giả có ý tưởng.

Trình trợ giúp hồ sơ điều chỉnh trình bao bọc MIT NVAPI từ Profile Inspector của Orbmu2k. [Xuất xứ chi tiết và phạm vi thành phần](../docs/provenance.md).

<a id="credits-and-license"></a>
## Tín dụng và giấy phép

Michael Robles; Orbmu2k; Những người đóng góp Tsuda Kageyu và HDE; NVIDIA Corporation; Microsoft và những người đóng góp; Tác giả và dịch giả Inno Setup. Phát triển ứng dụng, tích hợp và đóng gói: 禅堂 Zendo (RevoluSound Team).

[quyền chia sẻ gói biên dịch hiện có](../../../../NVMFG-Unlock40/LICENSE) và tất cả [giấy phép thành phần](LICENSES/README.md) đều được giữ nguyên. Các quyền MIT đối với mã ngược dòng khác với các điều khoản NVIDIA SDK. Không có giấy phép chung nào thay thế chúng.

Độc lập, không được tài trợ bởi và không được xác nhận chính thức bởi NVIDIA Corporation. Tất cả các nhãn hiệu được tham chiếu vẫn là tài sản của chủ sở hữu.
