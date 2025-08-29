import secrets
import string
import argparse

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор паролей")
    parser.add_argument("--length", type=int, default=12, help="Длина пароля")
    args = parser.parse_args()
    print("Ваш пароль:", generate_password(args.length))
