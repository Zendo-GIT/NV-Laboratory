<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Nguồn gốc, thay đổi và cấp phép

Cuộc kiểm tra này mô tả các ứng viên được chuẩn bị vào **2026-09-18**. Nguồn ứng dụng vẫn ở chế độ riêng tư; kho lưu trữ công khai chứa tên tệp và hàm băm, không chứa mã nguồn. Xem [thông báo thành phần đầy đủ](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Tham khảo: Orbmu2k/nvidiaProfileInspector cam kết `592d962cca8827efe8859461a84267755595064a`; phiên bản thực thi ứng cử viên 3.0.2.3. Cam kết tham chiếu và phiên bản lắp ráp của fork là các mã định danh khác nhau; không có phiên bản phát hành ngược dòng nào được suy ra từ phiên bản fork.

157 tệp nguồn/tài nguyên của người bạn đồng hành sạch sẽ được so sánh với cam kết đó: 2 byte giống hệt nhau, 134 tệp chỉ khác nhau ở phần cuối dòng hoặc BOM UTF-8, 11 tệp được sửa đổi, 10 tệp không có ở đường dẫn ngược dòng được so sánh. “Đã thêm” có liên quan đến đường dẫn đó và bản thân nó không phải là bằng chứng về quyền tác giả gốc.

[So sánh tập tin/băm hoàn chỉnh](../../../provenance/nvpi-source-provenance.json).

| Khu vực | Công việc kế thừa | Đóng góp Fork |
| --- | --- | --- |
| Biên tập hồ sơ | Mô hình hồ sơ, nhập/xuất, liên kết ứng dụng và dữ liệu tham chiếu | Tích hợp với Màn hình và trình khởi chạy công cụ bên ngoài |
| NVAPI | Tương tác DRS của Orbmu2k | Tương tác liên quan đến màu sắc/màn hình, hạn chế tải gốc trong sản xuất và loại bỏ mô hình |
| Dịch vụ hiển thị | API Windows/NVIDIA làm giao diện bên ngoài | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| giao diện người dùng | Tài nguyên, bảng màu và biểu tượng ngược dòng WPF | Hộp thoại màn hình, xác nhận 15 giây, trạng thái/đọc lại và bố cục thanh công cụ |
| Trình khởi chạy | Vỏ ứng dụng hiện có | Tra cứu và khởi chạy RasterPulse được cài đặt riêng được bảo vệ |
| Bao bì | MIT ngược dòng | Đồng hành độc lập sạch sẽ, trình cài đặt/gỡ cài đặt riêng biệt, thông báo được giữ lại |

Bản đồ nguồn công khai bao gồm các đường dẫn giải pháp/tài nguyên để truy xuất nguồn gốc; những tập tin đó không được phân phối dưới dạng nguồn. Các thử nghiệm phát triển, giao diện mô phỏng và mã nhị phân NVPI/RasterPulse kết hợp cũ đều bị loại trừ.

<a id="nvdriverforge"></a>
## NVDriverForge

Ứng dụng C#/.NET 8/WPF độc lập; quy trình làm việc hướng tới người dùng một phần được lấy cảm hứng từ NVCleanstall. Không có nguồn/nhị phân NVCleanstall nào được xác định trong tải trọng sản xuất. Nó không được thể hiện dưới dạng fork của ứng dụng độc quyền đó.

Công việc ban đầu của dự án bao gồm phân tích/lựa chọn thành phần, công việc cài đặt được bảo vệ, sao lưu và khôi phục giao dịch, tải xuống danh mục NVIDIA, kiểm tra cập nhật, giải thích bản địa hóa, quy trình làm việc nâng cao/NVENC tùy chọn và trình khởi động trình cài đặt.

Các thành phần được kế thừa/điều chỉnh: bốn bảng chủ đề NVPI, tham chiếu giao diện NVAPI DRS mở rộng và đồng hành MIT NVPI tùy chọn riêng. Giao diện người dùng lựa chọn cài sẵn Custom NV và tích hợp giao dịch trong danh sách cho phép thuộc về NVDriverForge; cài đặt trước không phải là đề xuất chính thức của NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 và Inno Setup vẫn là các thành phần bên ngoài chưa sửa đổi được sử dụng theo các điều khoản riêng của chúng. Dữ liệu keylase NVENC không được nhúng; một cam kết chính xác được chọn và kiểm tra khi người dùng yêu cầu tải xuống tương thích. Không có giấy phép phân phối lại nào được thiết lập cho dữ liệu ngược dòng đó.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 được phát triển độc lập bởi 禅堂 Zendo (RevoluSound Team). Người bảo trì đã sử dụng RTX40MFG-Unlock để so sánh và sàng lọc. Toàn bộ ứng dụng không được trình bày dưới dạng fork. Sự khác biệt này không loại bỏ phần ghi công cho các thành phần được chia sẻ/điều chỉnh trong lớp gốc hiện tại.

Tham chiếu so sánh: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, cam kết `4e776d068f91b4a665425542bb005dd57cc3d891`. Cây công cụ gốc riêng chứa 48 tệp được so sánh: 35 điểm khác biệt chỉ về định dạng, 4 tệp đã sửa đổi và 9 tệp không có ở đường dẫn tham chiếu. [So sánh hoàn chỉnh](../../../provenance/nvmfg-source-provenance.json).

Các tệp kế thừa đã sửa đổi: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Các đường dẫn bổ sung bao gồm `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` và giấy phép ngược dòng được giữ lại.

Các đơn vị C++ sản xuất: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection và vsync_observer; cộng với cụm entry_detour và bộ đệm/móc/tấm bạt lò xo/HDE64 MinHook. Giao diện ReShade được kế thừa, tài nguyên miếng chêm kế thừa và các mục tiêu CMake chưa sử dụng không nằm trong phần tổng hợp sản xuất này.

Các thành phần phù hợp bao gồm chính sách vá lỗi/nhà cung cấp và công việc tạm thời; thông báo bản quyền và sự cho phép của họ vẫn còn nguyên. Sự phối hợp trung tâm NGX/bootstrap/bộ điều khiển, xử lý V-Sync mỗi trò chơi, chẩn đoán phiên và ứng dụng Windows/SDK/quy trình sao lưu là dự án do 禅堂 Zendo (RevoluSound Team) thực hiện. Số lượng ở trên mô tả các tệp, bao gồm các tệp của bên thứ ba và các tệp chưa được sử dụng, không phải tỷ lệ phần trăm quyền tác giả hoặc trình tự thời gian của ý tưởng của một trong hai dự án.

Trình trợ giúp điều chỉnh NvapiDrsWrapper và NativeArrayHelper của NVPI thành một tập hợp riêng biệt, với logic hồ sơ do dự án tạo ra. Đường dẫn mô phỏng phát triển cũ bị loại trừ. Bảng màu gia đình dùng chung có nguồn gốc từ NVPI.

Tham chiếu MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; tập hợp con được biên dịch kế thừa không có thay đổi chức năng cục bộ nào trong so sánh. Tiêu đề tích hợp Streamline: 2.12; giấy phép tiêu đề mở đã được xác minh tại v2.12.0. Nguồn tiêu đề NGX: NVIDIA/DLSS cam kết `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Động cơ ứng cử viên SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Nhà cung cấp bắt buộc SHA-256 trong engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Nhóm nhà cung cấp 310.9 được báo cáo không thể thay thế được với hàm băm chính xác này. Không có nhà cung cấp DLL hoặc mô hình nào được bao gồm.

**Điểm cấp phép nổi bật:** giấy phép NVIDIA RTX SDK đầy đủ, phiên bản ngày 14 tháng 3 năm 2024, có hạn chế mục 4(d) liên quan đến việc vượt qua các giới hạn kỹ thuật. Việc kiểm tra không thiết lập sự cho phép cho việc sử dụng này. Giữ lại giấy phép động cơ MIT, miễn phí hoặc tuân theo các mod khác không giải quyết được tình trạng riêng biệt đó. Việc chuẩn bị ứng viên không phải là một thủ tục pháp lý. Thông báo tiêu đề ngắn ban đầu được bổ sung giấy phép đầy đủ; văn bản Windows-1252 của nó cũng được cung cấp dưới dạng UTF-8 có thể đọc được, với các byte gốc được giữ lại.

So sánh gốc đã được tính toán lại cho 0.2.3: 48 tệp và phân loại giống nhau. Kể từ lần kiểm tra trước, `game_selection.cpp`, `game_selection.h` và `patcher.cpp` đã thay đổi đối với các quan sát hoạt động/năng lực. Các quy trình thư viện, chẩn đoán, ưu tiên, cập nhật và lựa chọn mới thuộc về ứng dụng bảo trì. Giấy phép thành phần và hàm băm của nhà cung cấp được yêu cầu không thay đổi.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Trình quản lý hồ sơ RTSS độc lập được phát triển trong kho lưu trữ có nguồn gốc từ NVPI. Các tài nguyên/bảng giao diện người dùng MIT được kế thừa và nguồn gốc dự án vẫn được ghi có. Ứng dụng sản xuất sử dụng rõ ràng giấy phép MIT được cung cấp.

Công việc dự án: phân tích/ghi hồ sơ RTSS chính xác và mã hóa phân đoạn, sao lưu, loại bỏ ghi đè, cầu tải lại, phát hiện điều kiện tiên quyết, giao diện người dùng nhỏ gọn, vòng đời khay, điều khiển khởi động và bản địa hóa. RTSS thực hiện giới hạn thực tế.

Không có nguồn RTSS, hook DLL, SDK hoặc trình cài đặt nào được đóng gói. Cây cầu gọi quá trình xuất trong bản cài đặt RTSS do người dùng chọn hiện có. Không có gói trình điều khiển NVIDIA, bộ giới hạn thử nghiệm gốc, thời gian chạy Framepacer, MinHook, ReShade hoặc DLSS trong gói này.

<a id="assets-generated-data-and-tools"></a>
## Tài sản, dữ liệu và công cụ được tạo

[Tín dụng tài sản](../assets/README.md) xác định các bản xem trước giao diện hiện có và bộ chọn thiết lập NVPI. Các giá trị hư cấu trong đó được dán nhãn. Không có trò chơi/nội dung Nexus, hồ sơ cá nhân, ICC riêng tư, logo hoặc tệp phông chữ NVIDIA của công ty được sao chép.

Tên tương thích trò chơi được tạo được kế thừa trong NVMFG là công cụ hỗ trợ phát hiện chứ không phải bằng chứng kiểm tra. Danh mục trình cài đặt đã tạo được ghi có vào [thông báo dịch thuật](../../../../licenses/INSTALLER-TRANSLATORS.md). Bản ghi bản dựng được tạo với đường dẫn tuyệt đối vẫn ở chế độ riêng tư.

Các công cụ xây dựng riêng bao gồm các tập lệnh kiểm tra .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup và Python. Trình biên dịch, tiêu đề, trình chạy thử và nội dung gỡ lỗi của chúng không được phân phối. CRT phát hành tĩnh vẫn tuân theo các điều khoản chuỗi công cụ hiện hành của Microsoft.

<a id="scope-of-verification"></a>
## Phạm vi xác minh

Kiểm tra cục bộ đã kiểm kê tất cả các tệp trong ba gốc phát triển, đồng thời loại trừ cơ sở dữ liệu đối tượng Git và các mục tiêu thư mục được liên kết. Nguồn/tài liệu đang hoạt động đã được quét; các công trình lịch sử đã được kiểm kê và loại trừ. Các ZIP đã chọn và tải trọng hiện tại đã được quét và băm; các gói .NET đã được giải nén để kiểm tra bổ sung. Quá trình kiểm tra ban đầu đó không chạy sản phẩm, trình cài đặt, trò chơi, quy trình hoặc trình điều khiển RTSS.

Bản sửa đổi thiết lập NVPI sau này sửa lỗi lựa chọn ngôn ngữ độc lập bằng cách sử dụng các điều khiển Inno và bootstrap được chia sẻ. Các thiết bị riêng tư sáng/tối đã xác minh khả năng điều hướng bằng chuột và bàn phím cũng như tất cả 34 mã ngôn ngữ rõ ràng. Bộ chọn thiết lập thực tế đã được mở trên màn hình riêng tư không bao giờ hiển thị và bị hủy trước khi cài đặt. Bảy tệp ứng dụng và ZIP di động của nó không thay đổi. NVDriverForge 0.1.3 bao gồm đồng hành đã sửa và vẫn chuyển tiếp `/LANG`.

NVDriverForge 0.1.3 được hoàn thành vào ngày 10-09-2026. Báo cáo xác minh riêng của nó ghi lại 366 bài kiểm tra ứng dụng, 118 bài kiểm tra đồng hành, 32 bài kiểm tra thiết lập, 156 bài so sánh gốc và 34 trường hợp chuyển tiếp ngôn ngữ. Bản sửa lỗi lựa chọn thành phần được bảo vệ đã được phát lại dựa trên gói trình điều khiển gốc mà không thay đổi tải trọng hoặc cài đặt trình điều khiển. Đây là kết quả của nhóm sản phẩm đã ghi ngày tháng, không phải các bài kiểm tra được chạy lại bằng bản cập nhật tài liệu này hoặc bằng chứng về việc cài đặt trình điều khiển thực thành công.

Bản cập nhật trung tâm này không thay đổi mã ứng dụng chức năng. Các thử nghiệm xây dựng/đơn vị/giao diện người dùng ứng dụng trước đó vẫn là bằng chứng lịch sử cũ. Đây không phải là kỹ thuật đảo ngược hoàn toàn mọi mã nhị phân của bên thứ ba hoặc là sự đảm bảo chống lại mọi mẫu bí mật có thể có.

Bản cập nhật ngày 18 tháng 9 năm 2026: NVDriverForge 0.1.4 bổ sung tính năng kiểm tra mức độ sẵn sàng, sao lưu hồ sơ gốc, hướng dẫn thành phần, tùy chọn và bộ công cụ, kết quả chi tiết, báo cáo cục bộ và cập nhật ứng dụng. NVRasterPulse 0.2 bổ sung chẩn đoán cấu hình, hướng dẫn FPS, tạm dừng/tiếp tục, hoàn tác, cấu hình `.nvrp` và mục yêu thích/ẩn mà không có công cụ giới hạn mới. Hướng dẫn cá nhân mô tả cách sử dụng và giới hạn. Kiểm tra trung tâm tĩnh tách biệt với các thử nghiệm ứng dụng được ghi trong báo cáo riêng ngày 18 tháng 9; không có cài đặt trình điều khiển, nhập hồ sơ thực hoặc đo độ trễ nào được thực hiện cho trung tâm này.
