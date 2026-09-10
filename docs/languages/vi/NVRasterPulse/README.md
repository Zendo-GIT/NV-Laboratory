<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Giới hạn FPS cho mỗi ứng dụng đến RivaTuner Statistics Server.**

> **Cài đặt RTSS trước.** NVRasterPulse yêu cầu [RivaTuner Statistics Server (RTSS), tải xuống từ Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS phải đang chạy để thực thi các giới hạn. Không có trình cài đặt RTSS, hook DLL hoặc SDK được đóng gói.

[Tải xuống 0.1 & trạng thái](../docs/downloads.md#nvrasterpulse) · [Cài đặt](#installation) · [Cách giới hạn hoạt động](#usage) · [Giấy phép](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Tổng quan và mục đích

NVRasterPulse là giao diện Windows nhỏ gọn để quản lý giới hạn khung RTSS theo tên thực thi. RTSS thực hiện việc giới hạn. NVRasterPulse quản lý các giá trị hồ sơ tương ứng, các yêu cầu sao lưu và tải lại, với quyền truy cập vào khay và các lựa chọn liên tục.

Nó tồn tại để giúp việc chỉnh sửa giới hạn chính xác cho mỗi trò chơi trở nên dễ dàng hơn mà không cần thay thế toàn bộ cấu hình RTSS hoặc làm ảnh hưởng đến cài đặt lớp phủ của nó. Ứng cử viên **0.1** hiện tại là bản dựng ngày 9 tháng 9 năm 2026 với yêu cầu kiểm tra cài đặt RTSS.

<a id="features"></a>
## Tính năng

- Chọn một ứng dụng đang chạy hoặc thêm tệp thực thi của nó theo cách thủ công.
- Lưu giới hạn FPS từ 1 đến 1000, với tối đa ba chữ số thập phân.
- Mã hóa hợp lý chính xác các giá trị đã nhập: 59.94 trở thành 2997/50.
- Cấu hình Front Edge Sync (`SyncLimiter=1`) với chế độ chờ hoạt động (`PassiveWait=0`).
- Cập nhật hồ sơ cho mỗi lần thực thi, sao lưu tự động và ghi nguyên tử.
- Loại bỏ ghi đè giới hạn trong khi vẫn giữ lại nội dung hồ sơ khác.
- Phát hiện cài đặt RTSS, chọn đường dẫn thủ công và khởi chạy/tải lại rõ ràng.
- Hoạt động trên khay đơn, khởi động cài đặt tùy chọn, 34 ngôn ngữ và bốn chủ đề.
- Tách biệt các hành động thoát bình thường và **Thoát + RTSS**.

<a id="compatibility"></a>
## Khả năng tương thích

| Yêu cầu | Chi tiết |
| --- | --- |
| Hệ thống | Windows 10/11 x64 |
| Thời gian chạy | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), cài đặt riêng nếu cần |
| Phần mềm cần thiết | RTSS với `RTSS.exe`, thư mục `Profiles` phù hợp và hỗ trợ tải lại/hồ sơ tương thích |
| GPU | Khả năng tương thích RTSS xác định bộ giới hạn; trình quản lý hồ sơ này không yêu cầu thế hệ RTX cụ thể |
| Quyền | Ứng dụng hiện tại yêu cầu quyền truy cập của quản trị viên; thư mục hồ sơ RTSS đã chọn phải có thể truy cập được |
| Trò chơi | Phụ thuộc vào khả năng hỗ trợ hooking của RTSS và các hạn chế của từng trò chơi; không đảm bảo chống gian lận |

Không có phiên bản tối thiểu RTSS cụ thể nào được chứng nhận cho mọi chức năng trong cuộc kiểm tra trung tâm này. Sử dụng bản phân phối chính thức hiện tại và báo cáo phiên bản chính xác nếu khóa hồ sơ/tải lại không hoạt động. RTSS đã cài đặt nhưng đã dừng vượt qua quá trình kiểm tra cài đặt; sau đó nó phải được bắt đầu để giới hạn thực tế.

<a id="installation"></a>
## Cài đặt

1. **[Tải xuống và cài đặt RTSS từ Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Mở [Tải xuống NVRasterPulse](../docs/downloads.md#nvrasterpulse) và kiểm tra tính khả dụng của bản phát hành.
3. Tải xuống `NVRasterPulse-0.1-win-x64-Setup.exe` hoặc `NVRasterPulse-0.1-win-x64-portable.zip`, cùng với các thông báo/tổng kiểm tra.
4. So sánh SHA-256. Chạy Thiết lập hoặc trích xuất toàn bộ ZIP di động vào thư mục cục bộ có thể ghi.
5. Mở `NVRasterPulse.exe`. Nếu thiếu RTSS, hãy sử dụng **Tải xuống RTSS**, cài đặt nó, sau đó **Kiểm tra lại** hoặc chọn `RTSS.exe` theo cách thủ công.
6. Khởi động RTSS bằng phím tắt thông thường hoặc nút RTSS của NVRasterPulse nếu nó bị dừng.

Việc tắt lời nhắc tùy chọn sẽ không bỏ qua việc kiểm tra điều kiện tiên quyết. Quá trình khởi động khay Windows im lặng sẽ đợi cho đến khi cửa sổ chính mở trước khi hiển thị kiểm tra này. Thiết lập chỉ cài đặt NVRasterPulse. EXE của nó không được ký.

<a id="usage"></a>
## Cách sử dụng

1. Chọn ứng dụng đang chạy dự định hoặc duyệt đến trò chơi EXE của nó.
2. Nhập giới hạn từ 1 đến 1000 FPS, bao gồm giá trị phân số nếu cần.
3. Lưu và kiểm tra kết quả được báo cáo. NVRasterPulse cập nhật hồ sơ RTSS của tệp thực thi đó và yêu cầu tải lại.
4. Xác nhận RTSS đang chạy và xác minh hành vi trong trò chơi dự định.

Cấu hình được khóa bằng **tên thực thi**, chẳng hạn như `Game.exe.cfg`. Hai thư mục khác nhau chứa `Game.exe` có chung hồ sơ RTSS; lưu trữ đường dẫn đầy đủ không loại bỏ xung đột này.

Quá trình lưu sử dụng Front Edge Sync và chờ hoạt động. Chờ tích cực có thể làm tăng mức sử dụng CPU. Các trường `LimitTime` thay thế được vô hiệu hóa. Các nhận xét, cài đặt lớp phủ hiện có và `EnableHooking=0` vẫn được giữ nguyên. Cấu hình toàn cầu RTSS không bị thay đổi.

Sử dụng hành động rác để xóa phần ghi đè giới hạn của NVRasterPulse. Nó không xóa toàn bộ hồ sơ RTSS. Giới hạn kế thừa từ RTSS Global hoặc công cụ khác vẫn có thể được áp dụng sau đó.

**Đóng và thoát:** cửa sổ chính có thể ẩn vào khay. Bình thường **Thoát** khiến RTSS chạy và giữ nguyên các giới hạn đã lưu. **Thoát + RTSS** yêu cầu đóng bình thường quy trình RTSS phù hợp trong phiên hiện tại, đợi tối đa 8 giây và không buộc tắt quy trình đó. Giới hạn lưu trữ vẫn còn trong cả hai trường hợp.

Ngôn ngữ và chủ đề được chọn trong ứng dụng. Khởi động khi đăng nhập Windows là tùy chọn và dành cho bản sao đã cài đặt. Nút thông tin giải thích các hành động phổ biến.

<a id="screenshots"></a>
## Ảnh chụp màn hình

![Xem trước cửa sổ chính NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Kết xuất giao diện người dùng 0.1 hiện tại của Pháp với các tên thực thi mẫu và giá trị 176 FPS. RTSS được hiển thị là đã dừng; đây là hình minh họa giao diện, không phải là thước đo giới hạn hoạt động hoặc độ trễ. [Nguồn gốc hình ảnh](../assets/README.md).

<a id="update-and-uninstall"></a>
## Cập nhật và gỡ cài đặt

Thoát NVRasterPulse, tải xuống và xác minh phiên bản mới, sau đó chạy Cài đặt hoặc giải nén bản di động vào một thư mục mới. Giữ nguyên cài đặt và bản sao lưu RTSS. Các bản cập nhật RTSS là riêng biệt và đến từ Guru3D.

Để xóa bản sao đã cài đặt, hãy sử dụng Windows **Installed apps**. Đối với thiết bị di động, hãy thoát rồi xóa thư mục đã giải nén khi bản sao lưu của bạn an toàn. Các giới hạn RTSS đã lưu không bị xóa bằng cách gỡ cài đặt NVRasterPulse: trước tiên hãy xóa các phần ghi đè giới hạn dự định. RTSS có trình gỡ cài đặt riêng.

Trạng thái cục bộ: `%LOCALAPPDATA%\NVRasterPulse`. Tự động sao lưu RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Vị trí `%LOCALAPPDATA%\RTSSProfileBridge` cũ hơn có thể được đọc để di chuyển. Những tệp này có thể chứa các đường dẫn thực thi cá nhân và không được đăng công khai.

<a id="known-limitations"></a>
## Những hạn chế đã biết

- RTSS thực hiện giới hạn. Giá trị đã lưu hoặc yêu cầu tải lại thành công không phải là kết quả đo được thời gian kết xuất khung hình.
- Các tệp thực thi cùng tên chia sẻ một hồ sơ.
- Một giới hạn toàn cầu/mỗi trò chơi khác có thể ảnh hưởng đến kết quả; việc tắt tính năng ghi đè cục bộ sẽ không xóa giới hạn kế thừa.
- Móc RTSS bị vô hiệu hóa có chủ ý vẫn bị vô hiệu hóa.
- Chờ đợi tích cực có sự cân bằng CPU/nguồn điện.
- Không có trò chơi phổ quát, xác thực chống gian lận hoặc độ trễ từ đầu đến cuối.
- Công cụ giới hạn độc lập thử nghiệm trước đó không được biên soạn hoặc vận chuyển.
- Sao lưu tự động không ngụ ý giao diện sao lưu-khôi phục toàn bộ chỉ bằng một cú nhấp chuột.

<a id="troubleshooting"></a>
## Khắc phục sự cố

| triệu chứng | hành động |
| --- | --- |
| Điều kiện tiên quyết RTSS vẫn mở | Chọn `RTSS.exe` thực tế và thư mục Hồ sơ phù hợp, sau đó Kiểm tra lại. |
| Đã lưu giới hạn nhưng không có hiệu lực | Bắt đầu RTSS; xác minh chính xác EXE/hồ sơ trò chơi, quyền truy cập và các giới hạn khác. |
| Lưu không thành công | Kiểm tra quyền của thư mục và lưu giữ lỗi/sao lưu được hiển thị. |
| Giới hạn còn lại sau khi loại bỏ | Kiểm tra RTSS Global và các công cụ khác; hành động rác chỉ xóa phần ghi đè giới hạn cục bộ. |
| Hai trò chơi nhận được cùng một giới hạn | Kiểm tra xem tên tệp thực thi của chúng có giống nhau không. |
| Thoát + RTSS để RTSS mở | Tự mình đóng RTSS; lệnh này cố tình tránh việc buộc phải chấm dứt. |

Nếu khôi phục bản sao lưu RTSS theo cách thủ công, trước tiên hãy đóng RTSS và giữ nguyên cấu hình hiện tại trước khi thay thế bằng bản sao lưu dự định. Điều này có thể ghi đè các chỉnh sửa hồ sơ không liên quan; kiểm tra tập tin và ngày. [Hỗ trợ được chia sẻ](../docs/support.md).

<a id="faq"></a>
## Câu hỏi thường gặp

**Tôi có cần MSI Afterburner không?** NVRasterPulse yêu cầu RTSS; nó không phụ thuộc vào ứng dụng Afterburner. Thực hiện theo các tùy chọn cài đặt của nhà phân phối RTSS.

**Tôi có thể sử dụng tính năng này mà không chạy RTSS không?** Bạn có thể quản lý hồ sơ sau khi phát hiện cài đặt, nhưng RTSS phải chạy để hạn chế.

**Việc thoát hoặc gỡ cài đặt có loại bỏ giới hạn không?** Không. Xóa ghi đè giới hạn mong muốn một cách rõ ràng trước khi xóa NVRasterPulse.

**Đây có phải là fork của RTSS không?** Không. Đây là một trình quản lý hồ sơ độc lập; không có nguồn hoặc tệp thực thi RTSS nào được tích hợp.

<a id="upstream-modifications-and-credits"></a>
## Thượng nguồn, sửa đổi và tín dụng

Kho phát triển bắt nguồn từ [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Tài nguyên bảng màu/giao diện người dùng MIT của nó được ghi có. Các dịch vụ quản lý hồ sơ, mã hóa phân đoạn, sao lưu, cầu tải lại RTSS, hành vi khay, hướng dẫn điều kiện tiên quyết, ngôn ngữ và biểu tượng dành riêng cho ứng dụng đã được 禅堂 Zendo (RevoluSound Team) phát triển/điều chỉnh.

RTSS được phát triển bởi **Unwinder** và được phân phối riêng thông qua Guru3D. NVRasterPulse gọi `UpdateProfiles` từ hook DLL đã cài đặt đã chọn; không có RTSS SDK hoặc nhị phân hook nào được phân phối lại. Trình cài đặt sử dụng Inno Setup 7.1.0 chưa sửa đổi với các tập lệnh/bản dịch được điều chỉnh và một bản khởi động dự án.

[Xuất xứ đầy đủ](../docs/provenance.md) · [Bảng của bên thứ ba](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Giấy phép

Gói phân phối rõ ràng NVRasterPulse theo [Giấy phép MIT](../../../../NVRasterPulse/LICENSE) được cung cấp, giữ lại Bản quyền (c) 2016 Orbmu2k. Nguồn ứng dụng được duy trì riêng tư; MIT không yêu cầu xuất bản nguồn đã sửa đổi. RTSS và Windows/.NET vẫn tuân theo các điều khoản riêng của họ. [Thông báo đầy đủ](LICENSES/README.md).

Độc lập với NVIDIA Corporation, MSI và RTSS; không được họ tài trợ hoặc xác nhận chính thức. Tên sản phẩm vẫn là thương hiệu của chủ sở hữu.
