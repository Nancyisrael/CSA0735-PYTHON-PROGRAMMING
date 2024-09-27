import pefile
import hashlib

# Load the malware sample
def load_malware(file_path):
    try:
        return pefile.PE(file_path)
    except pefile.PEFormatError as e:
        print(f"Error: {e}")
        return None

# Extract API calls from the malware sample
def extract_api_calls(pe):
    api_calls = []
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        for imp in entry.imports:
            api_calls.append(imp.name.decode())
    return api_calls

# Calculate the hash of the malware sample
def calculate_hash(pe):
    return hashlib.md5(pe.write()).hexdigest()

# Main function
def main():
    file_path = input("Enter the malware sample path: ")
    pe = load_malware(file_path)
    if pe:
        api_calls = extract_api_calls(pe)
        hash_value = calculate_hash(pe)
        print("API Calls:")
        print(api_calls)
        print(f"Hash: {hash_value}")

if __name__ == "__main__":
    main()
