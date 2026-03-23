import base64
import sys

def encode_base64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def read_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def generate_combinations(usernames_file, passwords_file, output_file):
    usernames = read_file(usernames_file)
    passwords = read_file(passwords_file)

    with open(output_file, 'w') as out:
        for username in usernames:
            for password in passwords:
                combo = f"{username}:{password}"
                encoded = encode_base64(combo)
                out.write(encoded + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <usernames_file> <passwords_file> <output_file>")
        sys.exit(1)

    usernames_file = sys.argv[1]
    passwords_file = sys.argv[2]
    output_file = sys.argv[3]

    generate_combinations(usernames_file, passwords_file, output_file)
