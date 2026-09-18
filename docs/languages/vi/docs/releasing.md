<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · **Tiếng Việt**

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Dịch có sự hỗ trợ của máy từ tiếng Anh. Tên kỹ thuật, lệnh, URL và văn bản pháp lý gốc được giữ nguyên. Đánh giá của người bản xứ được chào đón; tham khảo tài liệu tham khảo tiếng Anh nếu từ ngữ không rõ ràng.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Xuất bản và phát hành

Kho lưu trữ công cộng là **Zendo-GIT/NV-Laboratory**. Các thay đổi về tài liệu được người bảo trì xem xét, cam kết và thúc đẩy bằng **GitHub Desktop**. Cam kết cục bộ không tải lên tập tin. Các gói nhị phân là tài sản phát hành GitHub riêng biệt; chúng không bao giờ thuộc danh sách thay đổi Git.

<a id="documentation-updates"></a>
## Cập nhật tài liệu

1. Mở thư mục **NV-Laboratory** trong GitHub Desktop.
2. Xem lại tài liệu, thông báo, hình ảnh, siêu dữ liệu JSON và trình xác thực tài liệu.
3. Chạy `python tools/validate_repository.py` từ thư mục đó.
4. Cam kết các thay đổi đã xem xét, sau đó sử dụng **Push origin**. Kiểm tra kết quả Hành động.
5. Giữ danh tính tác giả công khai **禅堂 Zendo (RevoluSound Team)** và địa chỉ GitHub `noreply` của tài khoản.

Không bao giờ chọn không gian làm việc phát triển chính, thư mục kiểm tra riêng hoặc thư mục đính kèm nhị phân. [Cam kết bảo mật email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Phát hành ứng dụng độc lập

| Công cụ | Gắn thẻ | Chính sách phiên bản |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Phiên bản ứng dụng gồm bốn phần hiện có; thiết lập phiên bản 2 có tên tệp riêng |
| NVDriverForge | nvdriverforge-v0.1.4 | Sơ đồ 0.x hiện có; các bản cập nhật được phiên bản duy trì các gói trước đó |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Phiên bản ứng dụng 0.2.3; những thay đổi tích lũy kể từ 0.1.1 công khai |
| NVRasterPulse | nvrasterpulse-v0.2 | Phiên bản hai phần hiện có |

Người bảo trì có thể công bố trực tiếp hoặc ủy quyền cho người trợ lý công bố tài sản được kiểm toán. Xuất bản là rõ ràng; không có quy trình công việc nào tạo ra Bản phát hành trên mỗi cam kết.

1. Xem lại báo cáo xuất bản trước hiện tại, nguồn của các tệp nhị phân, giấy phép và giá trị SHA-256.
2. Tạo bản nháp cho thẻ của công cụ, nhắm mục tiêu cam kết trung tâm đã được xem xét. Bao gồm các ghi chú phát hành dành riêng cho phiên bản đã chuẩn bị sẵn.
3. Chỉ đính kèm tài sản Thiết lập/di động của phiên bản đó, `Licenses-and-Credits.zip` và `SHA256SUMS.txt`.
4. Kiểm tra tính tương thích, cài đặt, phụ thuộc, thay đổi và các giới hạn đã biết. Giữ RTSS nổi bật cho NVRasterPulse.
5. Xuất bản, xác minh URL, kích thước và hàm băm của tài sản công cộng, đồng thời ghi lại ngày xuất bản thực tế trong `docs/releases.json`.
6. Cập nhật các trang tải xuống và bản dịch, sau đó cam kết/Đẩy các thay đổi của chúng trong GitHub Desktop.

Các liên kết thẻ cho mỗi dự án tránh đưa người dùng đến một công cụ khác thông qua liên kết `releases/latest` được chia sẻ. Kho lưu trữ **Source code** tự động của GitHub chứa trung tâm tài liệu này. Nguồn ứng dụng được giữ kín. Các thông báo về thành phần gốc vẫn còn nguyên và bản phát hành không giải quyết được khoản dự trữ NVIDIA SDK được ghi lại của NVMFG.


Bản cập nhật ngày 18 tháng 9 chuẩn bị ba thẻ mới; Bản phát hành Profile Inspector hiện tại không thay đổi. Tên nội dung, thẻ và `SHA256SUMS.txt` phải chính xác để kiểm tra cập nhật ứng dụng. Xuất bản các Bản phát hành bình thường mà không có cờ phát hành trước để đưa chúng ra kiểm tra bản phát hành ổn định; NVMFG vẫn còn thử nghiệm.

<a id="integrity-and-storage"></a>
## Tính toàn vẹn và lưu trữ

Không bao giờ âm thầm thay thế byte nhị phân đã xuất bản. Sử dụng phiên bản rõ ràng mới hoặc bản sửa đổi trình cài đặt với các giá trị băm mới. Sidecars hợp pháp bổ sung các thông báo nhúng. NVDriverForge 0.1.4 di động có dung lượng 142.017.891 byte, cao hơn giới hạn 100 tệp MiB Git thông thường của GitHub. Phát hành tệp đính kèm tránh đặt các tệp nhị phân hoặc Git LFS vào trung tâm này. [Hướng dẫn tệp lớn GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Báo cáo lỗ hổng riêng tư phải được bật trong cài đặt bảo mật kho lưu trữ. Xác minh tính khả dụng của nó trước khi gửi các báo cáo nhạy cảm đến đó; [SECURITY.md](../SECURITY.md) cung cấp một phương án dự phòng không tiết lộ chi tiết về lỗ hổng bảo mật.

[Tải danh mục xuống](downloads.md) · [Tài liệu phát hành GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
