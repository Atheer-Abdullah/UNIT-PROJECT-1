# utils/validator.py
import re

def validate_name(name):
    """
    يسمح بالحروف (عربي/إنجليزي) والمسافات, ويجب أن يكون طوله حرفين على الأقل
    """
    name = name.strip()
    if len(name) < 2:
        return False
    # يسمح بالحروف والمسافات فقط
    return all(char.isalpha() or char.isspace() for char in name)

def validate_email(email):
    
   
    email = email.strip().lower()
    
    # 1. التعبير النمطي (Regex) لشروط قوقل:
    # ^[a-z0-9.] -> يبدأ بحرف أو رقم أو نقطة
    # {6,30}    -> الطول من 6 إلى 30 خانة
    # @gmail\.com$ -> ينتهي حصراً بجيميل
    pattern = r'^[a-z0-9.]{6,30}@gmail\.com$'
    
    if bool(re.match(pattern, email)):
        #شرط  إضافي: قوقل لا تسمح بنقطة في البداية أو النهاية قبل @
        username_part = email.split('@')[0]
        if username_part.startswith('.') or username_part.endswith('.'):
            return False
        return True
    
    return False

def validate_username(username):
    """
    اسم المستخدم: حروف صغيرة وأرقام فقط, 4 خانات على الأقل, بدون مسافات
    """
    return bool(re.match(r'^[a-z0-9]{4,}$', username))

def validate_password(password):
    """
    كلمة المرور :حرف كبير, حرف صغير, رقم, رمز , وطول لا يقل عن 6
    """
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{6,}$"
    return bool(re.match(pattern, password)) 