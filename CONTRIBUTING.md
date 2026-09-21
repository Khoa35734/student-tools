# Hướng dẫn đóng góp (Contributing Guidelines)

Cảm ơn bạn đã tham gia đóng góp cho dự án `student-tools`! Để đảm bảo chất lượng mã nguồn và tính nhất quán, vui lòng tuân thủ các quy tắc dưới đây.

---

## 1. Quy trình làm việc (Git Workflow)

1. **Nhận nhiệm vụ**: Tìm Issue được giao hoặc thảo luận trước khi mở Issue mới.
2. **Không làm việc trực tiếp trên nhánh `main`**.
3. **Tạo nhánh mới từ `main`**:
   - Tính năng mới: `feature/<tên-chức-năng>` (Ví dụ: `feature/temperature-converter`)
   - Sửa lỗi: `fix/<tên-lỗi>` (Ví dụ: `fix/calculator-error`)
   - Tài liệu: `docs/<tên-tài-liệu>` (Ví dụ: `docs/converter-guide`)
   - Kiểm thử: `test/<tên-kiểm-thử>` (Ví dụ: `test/validator`)

```bash
git switch -c feature/<tên-chức-năng>
```

---

## 2. Quy chuẩn Commit Message

- Sử dụng commit message rõ ràng, thể hiện mục đích thay đổi.
- Khuyến khích định dạng Conventional Commits:
  - `feat: <nội dung>`: Thêm tính năng mới
  - `fix: <nội dung>`: Sửa lỗi
  - `test: <nội dung>`: Thêm hoặc cập nhật unit test
  - `docs: <nội dung>`: Cập nhật tài liệu
  - `refactor: <nội dung>`: Cấu trúc lại code mà không đổi chức năng
- Thực hiện các commit nhỏ, có ý nghĩa thay vì gộp toàn bộ vào một commit lớn.

---

## 3. Tạo Pull Request (PR)

Khi hoàn thành chức năng và vượt qua tất cả kiểm thử, đẩy nhánh lên repository và tạo PR với nội dung chuẩn:

### Mẫu tiêu đề:
`<loại>: <mô tả ngắn>` (Ví dụ: `feat: add temperature converter`)

### Mẫu mô tả Pull Request:
```markdown
## Related Issue
Closes #<số_issue>

## Changes
- <Liệt kê các thay đổi 1>
- <Liệt kê các thay đổi 2>

## Testing
- Tất cả unit tests hiện tại đều passed.
- Đã bổ sung các test cases mới: <mô tả test mới>
```

---

## 4. Quy trình Code Review (Dành cho Reviewer)

Mỗi Pull Request cần ít nhất một thành viên khác review dựa trên checklist sau:

- [ ] Code dễ đọc, tuân thủ phong cách lập trình Python
- [ ] Tên biến và hàm rõ ràng, mang tính biểu đạt
- [ ] Không có code thừa, code debug dư thừa
- [ ] Có bổ sung Unit Test tương ứng
- [ ] Tất cả test cases đều chạy pass
- [ ] Tài liệu hướng dẫn (`docs/`, `README.md`) đã được cập nhật tương ứng
- [ ] Không làm thay đổi các file không liên quan
- [ ] Commit message rõ ràng, đúng quy chuẩn
- [ ] Mô tả Pull Request đầy đủ thông tin

> **Lưu ý cho Reviewer**: Tránh chỉ bình luận ngắn gọn "OK". Hãy nhận xét cụ thể và đưa ra gợi ý cải thiện nếu có (Change Request).
