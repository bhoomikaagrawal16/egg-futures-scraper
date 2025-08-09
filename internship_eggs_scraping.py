import requests
from bs4 import BeautifulSoup

# URL to scrape
target_url = "https://tradingeconomics.com/commodities"

def get_egg_futures_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Fetch page content
    response = requests.get(target_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve data, status code:", response.status_code)
        return None

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    try:
        # Locate the row for Egg Futures
        row = soup.find("tr", {"data-symbol": "WEGGS:COM"})
        if not row:
            print("Egg futures data not found.")
            return None
        
        # Extract necessary data
        cells = row.find_all("td")
        date = cells[8].text.strip()
        current_price = float(cells[1].text.strip().replace(",", ""))
        price_increased = cells[2].text.strip()
        day_change_percentage = float(cells[3].text.strip().replace("%", "")) / 100
        weekly_change_percentage = float(cells[4].text.strip().replace("%", "")) / 100
        monthly_change_percentage = float(cells[5].text.strip().replace("%", "")) / 100
        ytd_change = cells[6].text.strip()
        yoy_change = cells[7].text.strip()
        
        # Compute derived metrics
        weekly_price = current_price / (1 + weekly_change_percentage) if weekly_change_percentage else 'N/A'
        monthly_price = current_price / (1 + monthly_change_percentage) if monthly_change_percentage else 'N/A'
        weekly_price_increase = current_price - weekly_price if weekly_price != 'N/A' else 'N/A'
        monthly_price_increase = current_price - monthly_price if monthly_price != 'N/A' else 'N/A'
        weekly_acceleration = (weekly_change_percentage * 100) / 7  # % per day
        monthly_acceleration = (monthly_change_percentage * 100) / 30  # % per day
        future_weekly_price = current_price * (1 + weekly_change_percentage) if weekly_change_percentage else 'N/A'
        future_monthly_price = current_price * (1 + monthly_change_percentage) if monthly_change_percentage else 'N/A'
        
        egg_data = {
            'Date': date,
            'Current Price': f"${current_price:,.2f}",
            'Price Increased': price_increased,
            'Day Change %': f"{day_change_percentage * 100:.2f}%",
            'Weekly Change %': f"{weekly_change_percentage * 100:.2f}%",
            'Monthly Change %': f"{monthly_change_percentage * 100:.2f}%",
            'YTD Change': ytd_change,
            'YoY Change': yoy_change,
            'Price Last Week': f"${weekly_price:,.2f}" if weekly_price != 'N/A' else 'N/A',
            'Price Last Month': f"${monthly_price:,.2f}" if monthly_price != 'N/A' else 'N/A',
            'Weekly Price Increase': f"${weekly_price_increase:,.2f}" if weekly_price_increase != 'N/A' else 'N/A',
            'Monthly Price Increase': f"${monthly_price_increase:,.2f}" if monthly_price_increase != 'N/A' else 'N/A',
            'Weekly Acceleration (% per day)': f"{weekly_acceleration:.2f}%",
            'Monthly Acceleration (% per day)': f"{monthly_acceleration:.2f}%",
            'Predicted Price Next Week': f"${future_weekly_price:,.2f}" if future_weekly_price != 'N/A' else 'N/A',
            'Predicted Price Next Month': f"${future_monthly_price:,.2f}" if future_monthly_price != 'N/A' else 'N/A'
        }
        
        return egg_data
    except Exception as e:
        print("Error extracting egg futures data:", e)
        return None

# Fetch data and print it
data = get_egg_futures_data()
if data:
    print("\nEgg Data:\n")
    for key, value in data.items():
        print(f"{key}: {value}")
