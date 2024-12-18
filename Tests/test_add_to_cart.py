import pytest
from Pages.login_page import LoginPage
from Pages.Homepage  import HomePage
from Pages.category_page import CategoryPage
from Pages.product_listing_page import ProductListingPage
from Pages.Product_detail_page  import ProductDetailPage
from utils.config import URL, MOBILE_NUMBER, OTP, COLOR
from utils.logger import logger  # Import the logger

def test_add_to_cart(setup):
    page = setup
    login_page = LoginPage(page)
    home_page = HomePage(page)
    category_page = CategoryPage(page)
    product_listing_page = ProductListingPage(page)
    product_detail_page = ProductDetailPage(page)

    logger.info("Starting test: test_add_to_cart")

    # Step 1: Login
    login_page.navigate_to(URL)
    login_page.click_profile_icon()
    login_page.enter_mobile_number(MOBILE_NUMBER)
    login_page.click_login()
    login_page.enter_otp(OTP)
    login_page.submit_otp()
    logger.info("Login successful")

    # Step 2: Navigate to homepage and select category
    logger.debug("Navigating to category")
    home_page.click_route_category()
    category_page.click_final_category()

    # Step 3: Select product from listing
    logger.debug("Selecting product from listing")
    with page.expect_popup() as popup_info:
        product_listing_page.click_product_name()
    product_detail_page = ProductDetailPage(popup_info.value)

    # Step 4: Select product details and add to cart
    logger.debug("Selecting product details")
    product_detail_page.select_color(COLOR)
    # product_detail_page.select_size(SIZE)
    product_detail_page.click_add_to_cart()
    logger.info("Product added to cart")

    # Add assertions to verify the product is added to the cart
    product_detail_page.wait_for_cart_confirmation()
    assert product_detail_page.is_product_added_to_cart(), "Product not added to cart: Confirmation message not visible."
    logger.info("Test completed: test_add_to_cart")
