# student-tools

Dự án mã nguồn mở cung cấp một tập hợp các công cụ đơn giản phục vụ sinh viên trong học tập và lập trình.

## Cấu trúc dự án

```text
student-tools/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── src/
│   ├── calculator.py
│   ├── converter.py
│   └── validator.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_converter.py
│   └── test_validator.py
│
└── docs/
    └── usage.md
```

## Các tính năng chính

## Các tính năng chính

- **Calculator (`src/calculator.py`)**: Hỗ trợ các phép tính toán học cơ bản (`add`, `subtract`, `multiply`, `divide`).
- **Converter (`src/converter.py`)**: Hỗ trợ chuyển đổi giữa các đơn vị đo lường (nhiệt độ, độ dài,...).
  - Temperature converter: chuyển đổi °C <-> °F (`celsius_to_fahrenheit`, `fahrenheit_to_celsius`).
- **Validator (`src/validator.py`)**: Kiểm tra tính hợp lệ của dữ liệu sinh viên (mã sinh viên, email,...).

## Hướng dẫn cài đặt và chạy thử

1. Clone repository:
   ```bash
   git clone <repository-url>
   cd student-tools
   ```

2. Chạy bộ kiểm thử (Unit Tests):
   ```bash
   python -m unittest discover tests
   ```

## Đóng góp phát triển

Vui lòng tham khảo [CONTRIBUTING.md](CONTRIBUTING.md) để nắm rõ quy trình tạo Issue, mở Branch, viết Commit và gửi Pull Request.
