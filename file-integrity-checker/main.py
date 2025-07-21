import hashlib
import os

def calculate_hash(filepath, method='sha256'):
    if not os.path.exists(filepath):
        print("❌ File not found.")
        return None

    hash_func = hashlib.sha256() if method == 'sha256' else hashlib.md5()

    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def main():
    filepath = input("Enter the path to the file: ").strip()
    expected_hash = input("Enter the expected hash value: ")._
