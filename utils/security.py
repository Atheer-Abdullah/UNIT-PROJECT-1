# utils/security.py
import hashlib

def hash_password(password):
    """
    تحويل كلمة المرور إلى نص مشفر 
    """
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(input_password, stored_hash):
    """
    مقارنة كلمة المرور المدخلة مع ال Hash المخزن في الملف
    """
    return hash_password(input_password) == stored_hash