def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
