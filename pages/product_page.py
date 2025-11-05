from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_free_shipping(self):
        try:
            # Look for Free Shipping
            element = self.page.locator("text=Free Shipping").first
            if element.count() > 0:
                print("Free Shipping found on product page.")
                return True
            else:
                return False
        except Exception as e:
            print(f"Error verifying on Free Shipping: {e}")
            return False
