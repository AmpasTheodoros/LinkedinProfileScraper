from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Sample LinkedIn profile URL for demonstration
profile_url = "https://www.linkedin.com/in/theodoros-ampas-72a517203/"

def scrape_linkedin_profile(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        content = response.text
        soup = BeautifulSoup(content, "html.parser")

        name = soup.find("li", class_="inline t-24 t-black t-normal break-words").get_text().strip()
        headline = soup.find("h2", class_="mt1 t-18 t-black t-normal break-words").get_text().strip()

        # Add more scraping code to extract other information as needed

        return {
            "name": name,
            "headline": headline,
            # Add other data to the dictionary
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def main_page():
    # Call the scraper function
    profile_data = scrape_linkedin_profile(profile_url)

    return render_template('index.html', data=profile_data)

if __name__ == "__main__":
    app.run(debug=True)
