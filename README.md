# **Tên đề tài:** Ứng dụng AI vào phân loại rác thông minh
## **Nội dung chính**: Người dùng tạo tài khoảng và vức rác bằng hệ thống. Sau khi nhận diện được đúng loại rác sẽ cộng điểm tương ứng. Người dùng có thể kiểm tra trực tiếp bằng giao diện winform đi kèm với hệ thống, và có thể báo cáo sai xót để model được cập nhập với data chỉnh sửa đó. Cuối cùng là hệ thống website để người dùng đăng nhập và đổi thưởng. 
**1. Models:** 
- Nhận diện người (YOLOv8)
- Phân loại rác (Teachable Machine)
- Nhận diện loại rác (YOLOv8)

**2. Winform:** Dùng để hiển thị hình ảnh và danh sách các loại rác được user vứt.

**3. Website:** Xây dựng bằng Django dùng để tạo hệ thống đổi điểm thưởng của người dùng có được khi đổi rác. Ngoài ra còn nhiều chức năng quan trọng khác như đăng ký, đăng nhập, xác minh bằng email....
