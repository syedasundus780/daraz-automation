from playwright.sync_api import Page

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def apply_brand_filter(self, brand_name):
        try:
            # Scroll down
            self.page.mouse.wheel(0, 3000)
            self.page.wait_for_timeout(2000)

            
            brand_locator = self.page.locator(f"text={brand_name}").first

            if brand_locator.count() > 0:
                
                brand_locator.scroll_into_view_if_needed()
                self.page.wait_for_timeout(1000)
                brand_locator.click(force=True)
                self.page.wait_for_timeout(5000)
                self.page.wait_for_load_state("domcontentloaded")
                print(f"Brand filter is applied: {brand_name}")
            else:
                print(f"Brand filter '{brand_name}' not found on the page.")
        except Exception as e:
            print(f"Error applying brand filter: {e}")

    def apply_price_filter(self, min_price, max_price):
        try:
            self.page.fill('input[placeholder="Min"]', str(min_price))
            self.page.fill('input[placeholder="Max"]', str(max_price))
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(5000)
            self.page.wait_for_load_state("domcontentloaded")
            print(f"Price filter is applied: {min_price}-{max_price}")
        except Exception as e:
            print(f"Error applying price filter: {e}")

    def count_products(self):
        try:
            products = self.page.locator('div[data-qa-locator="product-item"]')
            count = products.count()
            print(f"Total products are found: {count}")
            return count
        except Exception as e:
            print(f"Error counting products: {e}")
            return 0

    def open_first_product(self):
        try:
            self.page.wait_for_selector('div[data-qa-locator="product-item"]', timeout=40000)
            first_product = self.page.locator('div[data-qa-locator="product-item"]').first
            first_product.scroll_into_view_if_needed()
            first_product.click(force=True)
            self.page.wait_for_timeout(8000)
            self.page.wait_for_load_state("domcontentloaded")
            print("Opened first product successfully.")
        except Exception as e:
            print(f"Error opening product: {e}")
