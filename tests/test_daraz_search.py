import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

@pytest.mark.parametrize("search_term, brand, min_price, max_price", [
    ("electronics", "Infinix", 500, 5000)
])
def test_daraz_search_filters(browser_context, search_term, brand, min_price, max_price):
    page = browser_context.new_page()

    # Home Page
    home = HomePage(page)
    home.goto_homepage()
    home.search_product(search_term)

    # Search Results Page
    search_results = SearchResultsPage(page)
    search_results.apply_brand_filter(brand)
    search_results.apply_price_filter(min_price, max_price)

    count = search_results.count_products()
    assert count > 0, f"No products found after filters! Found: {count}"

    search_results.open_first_product()

    # Product Page
    product_page = ProductPage(page)
    if not product_page.verify_free_shipping():
        print("Free Shipping is not available for this product.")
    else:
        print("Free Shipping is available for this product.")
