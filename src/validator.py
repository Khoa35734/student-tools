"""
Module Validator: Cung cấp các hàm kiểm tra tính hợp lệ của dữ liệu học tập.
"""
import re

def is_valid_student_id(student_id):
    """
    Kiểm tra mã số sinh viên hợp lệ.
    Mã số hợp lệ là chuỗi gồm đúng 8 chữ số.
    """
    if not isinstance(student_id, str):
        return False
    return bool(re.fullmatch(r"\d{8}", student_id))

def is_valid_email(email):
    """
    Kiểm tra địa chỉ email có đúng định dạng tiêu chuẩn hay không.
    """
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))
