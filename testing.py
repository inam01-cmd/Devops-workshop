import random
import string


def generate_password():
    characters = "eE"  # 'E' capital aur small dono ho sakte hain
    numbers = "0987654321"  # Numbers ko random banane ke liye
    symbols = "!@#$&*"  # Symbols random honge

    password = random.choice(characters)  # Pehla character 'E' ya 'e' hoga
    password += "sha"  # 'sha' same rahayga
    password += ''.join(random.choices(numbers, k=3))  # 3 random numbers
    password += ''.join(random.sample(symbols, len(symbols)))  # Sare symbols random order me honge

    return password


def save_passwords(filename="passwords.txt", count=1440000):  # 1,440,000 passwords generate honge
    with open(filename, "w") as file:
        for _ in range(count):
            password = generate_password()
            file.write(password + "\n")
    print(f"{count} passwords saved in {filename}")


if __name__ == "__main__":
    save_passwords()