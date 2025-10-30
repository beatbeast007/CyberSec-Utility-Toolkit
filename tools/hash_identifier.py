def identify_hash(hash_str):
    length = len(hash_str)
    possibilities = {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }
    algo = possibilities.get(length, "Unknown / Custom hash")
    return algo

if __name__ == "__main__":
    h = input("Enter hash to identify: ").strip()
    print(f"Possible algorithm: {identify_hash(h)}")
