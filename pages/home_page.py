class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.daraz.pk/"

    def goto_homepage(self):
        self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
        print("Homepage opened successfully.")

    def search_product(self, keyword):
        try:
            # Wait for search bar to be visible
            self.page.wait_for_selector("input[placeholder='Search in Daraz']", timeout=20000)
            self.page.fill("input[placeholder='Search in Daraz']", keyword)
            self.page.keyboard.press("Enter")

            # Wait for search results
            self.page.wait_for_selector("div[data-qa-locator='product-item']", timeout=40000)
            print("Search results loaded successfully.")
        except Exception as e:
            print(f"Error searching product: {e}")
