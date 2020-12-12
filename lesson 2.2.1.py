from selenium import webdriver
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_num = browser.find_element_by_id("num1")
    second_num = browser.find_element_by_id("num2")
    summa = str(int(first_num.text) + int(second_num.text))

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summa)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()