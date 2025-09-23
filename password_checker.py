import re
import random
import string
import sys

def check_password_strength(password: str) -> str:
    """
    檢查密碼強度。
    規則：
    1. 長度 >= 8
    2. 至少一個數字
    3. 至少一個大寫字母
    4. 至少一個小寫字母
    5. 至少一個特殊符號
    回傳 "弱"、"中等" 或 "強"
    """
    if not password:
        return "弱"
    rules = [
        len(password) >= 8,
        re.search(r'\d', password),
        re.search(r'[A-Z]', password),
        re.search(r'[a-z]', password),
        re.search(r'[\W_]', password)
    ]
    score = sum(bool(r) for r in rules)
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中等"
    else:
        return "強"

def generate_strong_password(length: int = 12) -> str:
    """
    產生一組強密碼，預設長度為 12。
    長度至少需為 8，否則拋出 ValueError。
    """
    if length < 8:
        raise ValueError("密碼長度應該至少為8")
    all_chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if check_password_strength(password) == "強":
            return password

if __name__ == '__main__':
    """
    命令列執行邏輯：
    - 若有參數，檢查密碼強度並印出結果。
    - 若無參數，產生一組強密碼並印出。
    """
    if len(sys.argv) > 1:
        password = sys.argv[1]
        strength = check_password_strength(password)
        print(f"密碼強度：{strength}")
    else:
        pwd = generate_strong_password()
        print(f"產生的強密碼：{pwd}")
