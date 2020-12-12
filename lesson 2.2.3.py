from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("Myname")
    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("Mylastname")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("bla@bla.bla")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../123.txt')
    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)
    submit_button = browser.find_element_by_css_selector("[type='submit']")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()