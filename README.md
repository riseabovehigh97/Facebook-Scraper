# Facebook Group Scraper Bot

A Python bot that automates login to Facebook and scrapes information from Facebook groups, including group names, posts, comments, and member information. The scraped group URLs can also be saved to an Excel file. Built with Selenium WebDriver for browser automation.

---

## **Features**

* Automates Facebook login using a provided username and password.
* Navigates to the **Groups** section of Facebook.
* Automatically clicks **“See more”** to load all group content.
* Extracts group names, posts, and associated text/comments.
* Saves group URLs to an **Excel file** (`links.xlsx`).
* Works with multiple Chrome WebDriver setups.

---

## **Requirements**

* Python 3.x
* [Selenium](https://pypi.org/project/selenium/)
* [XlsxWriter](https://pypi.org/project/XlsxWriter/) (for exporting group URLs)
* Chrome Browser
* ChromeDriver compatible with your installed Chrome version

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/riseabovehigh97/Insta-Bot.git
cd Insta-Bot/Bot
```

2. Install required packages:

```bash
pip install selenium xlsxwriter
```

3. Download ChromeDriver and place it in a directory of your choice. Update the path in the script:

```python
chromedriver = "C:\\path\\to\\chromedriver"
```

---

## **Usage**

1. Open the script (`fbBot.py`).
2. Set your Facebook credentials:

```python
email = "your_email@gmail.com"
password = "your_password"
```

3. Run the script:

```bash
python fbBot.py
```

4. The bot will:

   * Login to Facebook.
   * Navigate to your groups.
   * Scrape posts, comments, and group URLs.
   * Save all group URLs to `links.xlsx`.

---

## **Notes**

* Make sure your ChromeDriver version matches your Chrome browser version.
* Facebook may block automated logins; use this responsibly and at your own risk.
* Avoid running too frequently to prevent account restrictions.

---

## **Contributing**

* Contributions are welcome!
* Feel free to improve the bot’s scraping capabilities or add new features.

---

## **License**

This project is for educational purposes. Use responsibly.

