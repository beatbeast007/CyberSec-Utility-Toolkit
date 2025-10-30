def is_phishing_url(url):
    flags = 0
    if len(url) > 75:
        flags += 1
    if "@" in url or "-" in url or "//" in url[8:]:
        flags += 1
    if url.count('.') > 3:
        flags += 1
    if any(char.isdigit() for char in url.split("/")[2]):
        flags += 1
    return "⚠️ Possible Phishing URL" if flags >= 2 else "✅ Looks Legit"

if __name__ == "__main__":
    link = input("Enter URL to analyze: ")
    print(is_phishing_url(link))
