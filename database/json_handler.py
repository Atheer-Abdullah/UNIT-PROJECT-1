# database/json.py
import json  # هذي في البداية ضرورية للتعامل مع ملفات ال JSON
import os    # هذي ضرورية عشان نتأكد هل الملف موجود في الجهاز أو لا

class DataHandler:
    @staticmethod
    def load_json(file_path):
        """يقرأ البيانات من ملف JSON"""
        try:
            # نتأكد إذا الملف مو موجود أو فاضي نرجع قائمة فاضية
            if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
                return []
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def save_json(file_path, data):
        """يحفظ البيانات في ملف JSON"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(f" Error saving to file: {e}")
            return False