import hashlib
import base58
import bech32

def sha256(data):
    return hashlib.sha256(data).digest()

def ripemd160(data):
    return hashlib.new('ripemd160', data).digest()

def hash160(data):
    return ripemd160(sha256(data))

def decode_bech32(bech32_address):
    hrp, data = bech32.bech32_decode(bech32_address)
    if data is None:
        raise ValueError("Invalid Bech32 address")
    decoded = bech32.convertbits(data, 5, 8, False)
    if decoded is None:
        raise ValueError("Error converting bits")
    return bytes(decoded)

def decode_base58(base58_address):
    decoded = base58.b58decode_check(base58_address)
    # Remove prefix (1st byte), return rest (which should be Hash160)
    return decoded[1:]

def address_to_hash160(address, coin_type):
    coin_type = coin_type.upper()  # Normalize coin type to uppercase

    if coin_type in ['BTC', 'LTC']:  # Bech32 address (SegWit)
        if address.startswith(('bc1', 'ltc1')):
            return decode_bech32(address)
        else:
            return decode_base58(address)  # Non-SegWit Base58
        
    elif coin_type in ['DOGE', 'DASH', 'BCH']:  # Base58 address
        return decode_base58(address)

    elif coin_type == 'ZCASH':  # Base58 Zcash address
        if address.startswith('t1') or address.startswith('t3'):
            return decode_base58(address)
        else:
            raise ValueError("Unsupported Zcash address type")
    
    elif coin_type == 'XRP':  # Ripple (XRP) uses Base58 with a different prefix
        return decode_base58(address)
    
    else:
        raise ValueError("Unsupported coin type")

def process_bulk_input(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write("Address, Coin Type, Hash160\n")  # Header for output file

            for line in infile:
                # Skip empty lines
                if not line.strip():
                    continue
                
                try:
                    # Parse address and coin type (comma or space separated)
                    address, coin_type = [item.strip() for item in line.split(",")]
                    
                    # Convert to Hash160
                    hash160_value = address_to_hash160(address, coin_type)
                    
                    # Write result to the output file
                    outfile.write(f"{address}, {coin_type}, {hash160_value.hex()}\n")
                except Exception as e:
                    # Handle errors and log them to the output file
                    outfile.write(f"{address}, {coin_type}, Error: {e}\n")

        print(f"Processing complete! Output written to {output_file}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")

if __name__ == "__main__":
    input_file = input("Enter the input file name: ").strip()
    output_file = input("Enter the output file name: ").strip()

    process_bulk_input(input_file, output_file)
