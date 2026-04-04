# validator.py
def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

if __name__ == "__main__":
    import sys
    email = sys.argv[1]
    if is_valid_email(email):
        print("Valid")
        sys.exit(0)
    else:
        print("Invalid")
        sys.exit(1)


# test_validator.py
from validator import is_valid_email   # imports cleanly, nothing runs

def test_valid():
    assert is_valid_email("user@example.com") == True

def test_invalid():
    assert is_valid_email("notanemail") == False
