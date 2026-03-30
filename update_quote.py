import requests
import re

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        json_data = response.json()
        quote = f"*{json_data[0]['q']}* — **{json_data[0]['a']}**"
        return quote
    except Exception as e:
        return "*Keep pushing forward!* — **Inspiration**"

def update_readme(quote):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Marker එක ඇතුලේ තියෙන කොටස විතරක් update කරනවා
    pattern = r"()(.*?)()"
    replacement = f"\\1\n> {quote}\n\\3"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    quote = get_quote()
    update_readme(quote)
