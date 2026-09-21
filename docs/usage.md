# Hướng dẫn sử dụng `student-tools`

Thư viện `student-tools` cung cấp các công cụ tiện ích cho sinh viên. Dưới đây là hướng dẫn sử dụng chi tiết từng chức năng.

---

## 1. Calculator (`src/calculator.py`)

Cung cấp các phép tính số học cơ bản: `add`, `subtract`, `multiply`, `divide`.

### Ví dụ:
```python
from src.calculator import add, subtract, multiply, divide

# Phép cộng
print(add(10, 5))       # Kết quả: 15

# Phép trừ
print(subtract(10, 5))  # Kết quả: 5

# Phép nhân
print(multiply(4, 3))   # Kết quả: 12

# Phép chia
print(divide(10, 2))    # Kết quả: 5.0
```

---

## 2. Converter (`src/converter.py`)

*(Đang phát triển theo Issue #1 và Issue #3)*

Hỗ trợ chuyển đổi giữa các đơn vị đo lường như nhiệt độ (°C <-> °F), độ dài, v.v.

---

## 3. Validator (`src/validator.py`)

Hỗ trợ kiểm tra dữ liệu đầu vào.

### Ví dụ:
```python
from src.validator import is_valid_student_id, is_valid_email

# Kiểm tra MSSV (yêu cầu 8 chữ số)
print(is_valid_student_id("20210001"))  # True
print(is_valid_student_id("123"))       # False

# Kiểm tra Email
print(is_valid_email("sv@university.edu.vn")) # True
print(is_valid_email("invalid-email"))        # False
```
