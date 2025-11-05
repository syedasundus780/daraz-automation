# Daraz Playwright Automation Project

This project is part of **Assignment No. 7 – Selenium/Playwright Automation**.  
It automates search and filtering functionality on [Daraz.pk](https://www.daraz.pk) using Playwright and Pytest.



## Features
- Opens Daraz homepage
- Searches for a product (e.g. "electronics")
- Applies brand and price filters
- Counts total products found
- Opens the first product
- Verifies free shipping availability



## Installation & Run

1. Clone this repository:
   ```bash
   git clone https://github.com/sundusnadeem/daraz-automation.git
   cd daraz-automation
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. Run tests:

   ```bash
   pytest -s -v tests/test_daraz_search.py
   ```

---

## Author

**Name:** Sundus Nadeem
**Institute:** 10Pearls
**Assignment:** No. 7 – Playwright Automation
