import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test6(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=appearance&doc=template']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=appearance&doc=logotype']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=product_groups']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=option_groups']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=manufacturers']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=suppliers']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=delivery_statuses']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=sold_out_statuses']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=quantity_units']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=catalog&doc=csv']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=countries&doc=countries']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=currencies&doc=currencies']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=customers&doc=customers']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=customers&doc=csv']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=customers&doc=newsletter']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=languages&doc=languages']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=languages&doc=storage_encoding']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=jobs']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=customer']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=shipping']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=payment']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=order_total']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=order_success']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=modules&doc=order_action']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=orders&doc=orders']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=orders&doc=order_statuses']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=pages&doc=pages']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=reports&doc=monthly_sales']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=reports&doc=most_sold_products']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=reports&doc=most_shopping_customers']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=store_info']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=defaults']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=general']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=listings']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=images']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=checkout']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=advanced']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=settings&doc=security']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=slides&doc=slides']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=tax&doc=tax_classes']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=tax&doc=tax_rates']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=translations&doc=search']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=translations&doc=scan']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=translations&doc=csv']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=users&doc=users']").click()
    driver.find_element_by_tag_name("h1")
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=vqmods&doc=vqmods']").click()
    driver.find_element_by_tag_name("h1")
    WebDriverWait(driver, 20).until(EC.title_is("vQmods | My Store"))