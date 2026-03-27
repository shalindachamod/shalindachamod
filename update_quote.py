import requests
import re

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = response.json()
    quote = f"*{json_data[0]['q']}* — **{json_data[0]['a']}**"
    return quote

def update_readme(quote):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r".*",
        f"\n> {quote}\n",
        content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    quote = get_quote()
    update_readme(quote)
