
def is_acceptable_password(password: str) -> bool:
    return len(password)>6 and any(it.isdigit() for it in password) \
           and not all(it.isdigit() for it in password)


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('984798734839743'))