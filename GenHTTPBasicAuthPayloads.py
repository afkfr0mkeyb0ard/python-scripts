import base64

def encode_base64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def read_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def generate_combinations(usernames_file, passwords_file, output_file):
    usernames = read_file(usernames_file)
    passwords = read_file(passwords_file)

    encoded_combinations = []

    for username in usernames:
        for password in passwords:
            combination = f"{username}:{password}"
            encoded_combination = encode_base64(combination)
            encoded_combinations.append(encoded_combination)

    with open(output_file, 'w') as f:
        for encoded in encoded_combinations:
            f.write(encoded + '\n')

    print(f"[+] File {output_file} successfully created.")

generate_combinations('usernames.txt', 'passwords.txt', 'payloads.txt')
