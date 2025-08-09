# 🥚 Commodity Price Scraper & Analytics Tool

A Python-based web scraping tool that extracts **real-time Egg Futures commodity data** from [TradingEconomics](https://tradingeconomics.com/commodities), performs analysis, and calculates predictive metrics.
This project demonstrates **web scraping**, **data parsing**, and **financial metric computation** using **Requests** and **BeautifulSoup**.

---

## 🚀 Features

* **Web Scraping**: Extracts live Egg Futures data 
* **Data Parsing**: Retrieves metrics such as:

  * Current Price
  * Daily, Weekly, and Monthly % Change
  * Year-to-Date (YTD) and Year-over-Year (YoY) Change
* **Analytics & Derived Insights**:

  * Price Last Week / Month
  * Absolute Price Change (Weekly & Monthly)
  * Price Acceleration (% per day)
  * Short-term price predictions based on percentage change
* **Extensible**: Can be adapted for other commodities with minimal changes.

---

## 📂 Tech Stack

* **Language**: Python
* **Libraries**:

  * `requests` — For fetching web pages
  * `beautifulsoup4` — For HTML parsing

---

## 📊 Example Output

```
Egg Data:

Date: Aug/08
Current Price: $2.46
Price Increased: 0.22
Day Change %: -8.10%
Weekly Change %: -15.83%
Monthly Change %: -7.19%
YTD Change: -57.64%
YoY Change: -22.11%
Price Last Week: $2.92
Price Last Month: $2.65
Weekly Price Increase: $-0.46
Monthly Price Increase: $-0.19
Weekly Acceleration (% per day): -2.26%
Monthly Acceleration (% per day): -0.24%
Predicted Price Next Week: $2.07
Predicted Price Next Month: $2.28
```

## 🔧 How It Works

1. Sends an HTTP GET request to the commodities page.
2. Locates the `<tr>` element containing `data-symbol="WEGGS:COM"`.
3. Extracts the table cells (`<td>` tags) for key metrics.
4. Calculates:

   * Past prices from percentage changes
   * Absolute changes
   * Average daily acceleration
   * Predicted future prices
5. Outputs the results in a readable format.
