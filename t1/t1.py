from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_abs1():
    link = "http://saucedemo.com/"
    browser = webdriver.Chrome()
    browser.get(link)
    #проверяем аворизацию
    input1 = browser.find_element(By.ID, "user-name")
    input1.send_keys("standard_user")
    input2 = browser.find_element(By.ID, "password")
    input2.send_keys("secret_sauce")
    input3 = browser.find_element(By.ID, "login-button")
    input3.click()
    products = browser.find_elements(By.ID, "inventory_container")
    assert len(products)>0, "Авторизация не прошла"

    #добавляем товар в корзину
    addcart = browser.find_elements(By.CSS_SELECTOR, "#inventory_container div.inventory_item .btn_inventory")
    assert len(addcart)>0, "Товаров нет"
    addcart[0].click()

    #переходим в корзину
    gotocart = browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_link")
    gotocart.click()
    incart = browser.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
    assert len(incart)>0, "Корзина пустая"
    
    #Checkout
    checkoutbtn = browser.find_element(By.CSS_SELECTOR, ".cart_footer #checkout")
    checkoutbtn.click()
    continuebtn = browser.find_elements(By.ID, "continue")
    assert len(continuebtn)>0, "Страница Your Information не открылась"
    
    #Checkout: Your Information
    fin_input1 = browser.find_element(By.ID, "first-name")
    fin_input1.send_keys("Имя")
    fin_input2 = browser.find_element(By.ID, "last-name")
    fin_input2.send_keys("Фамилия")
    fin_input3 = browser.find_element(By.ID, "postal-code")
    fin_input3.send_keys("Индекс")
    continuebtn = browser.find_element(By.ID, "continue")
    continuebtn.click()
    finishbtn = browser.find_elements(By.CSS_SELECTOR, "#finish")
    assert len(finishbtn)>0, "Заказ не оформлен"

    #complete order
    finishbtn = browser.find_element(By.CSS_SELECTOR, "#finish")
    finishbtn.click()
    goodbye_text_elt = browser.find_element(By.TAG_NAME, "h2")
    goodbye_text = goodbye_text_elt.text
    assert "Thank you for your order!" == goodbye_text, "Что-то пошло не так"
    time.sleep(2)
    browser.quit()

if __name__ == "__main__":
    test_abs1()
    print("Everything passed")