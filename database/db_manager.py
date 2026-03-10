# database/db_manager.py
from database.json_handler import DataHandler
from config.paths import USERS_FILE

class DBManager:
    # المسار المعتمد للملف

    @staticmethod
    def save_user(user_info):
        """يحفظ مستخدم جديد بعد التأكد من عدم التكرار"""
        users = DataHandler.load_json(USERS_FILE) 
        if users is None:
            users = []

        # فحص التكرار (الأمان المزدوج)
        for u in users:
            if u.get("username") == user_info["username"]:
                return False
            if u.get("email") == user_info["email"]:
                return False
        
        users.append(user_info)
        return DataHandler.save_json(USERS_FILE, users)
    
    @staticmethod
    def user_exists(email):
        """يفحص هل الإيميل موجود مسبقاً"""
        users = DataHandler.load_json(USERS_FILE)
        if not users: return False
        return any(u.get("email") == email for u in users)

    @staticmethod
    def user_exists_by_username(username):
        """يفحص هل اسم المستخدم (Username) موجود مسبقا"""
        users = DataHandler.load_json(USERS_FILE)
        if not users: return False
        return any(u.get("username") == username for u in users)

    @staticmethod
    def get_user_by_email(email):
        """يبحث عن مستخدم بالإيميل ويرجع بياناته كاملة"""
        users = DataHandler.load_json(USERS_FILE)
        if not users: return None
        for u in users:
            if u.get("email") == email:
                return u
        return None

    @staticmethod
    def update_password(email, new_hashed_password):
        """تحديث كلمة المرور لمستخدم معين"""
        users = DataHandler.load_json(USERS_FILE)
        if not users: return False

        found = False
        for user in users:
            if user.get('email') == email:
                user['password'] = new_hashed_password
                found = True
                break
        
        if found:
            return DataHandler.save_json(USERS_FILE, users)
        return False