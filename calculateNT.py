#Calculate NT hashs
#python3 calculateNT.py <passwords.txt>
import hashlib
import sys

def calculate_nt_hash(password):
    password_utf16 = password.encode('utf-16le')
    nt_hash = hashlib.new('md4', password_utf16).hexdigest().upper()
    return nt_hash

def process_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            passwords = f.readlines()
        
        passwords = [pwd.strip() for pwd in passwords]

        output_file = f"{input_file.split('.')[0]}_NT.txt" 
        
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for password in passwords:
                nt_hash = calculate_nt_hash(password)
                out_f.write(f"{nt_hash}\n") 

        print(f"Output file : {output_file}")
    
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"Error: {e}")

# Vérifier les paramètres de la ligne de commande
if len(sys.argv) != 2:
    print("Usage: python3 calculateNT.py <passwords.txt>")
else:
    input_file = sys.argv[1]
    process_file(input_file)
