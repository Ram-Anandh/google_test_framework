from selenium.webdriver.common.by import By


class HomepageLocators:
    google_logo = By.XPATH, '//body//div[2]/div/img'
    search_bar = By.XPATH, '//body//form/div[1]/div[1]/div[1]'
    search_icon = By.XPATH, '//form/div[1]//div[1]/div/span'
    mic_icon = By.XPATH, '//form/div[1]/div[1]/div[1]//div[3]/div[2]'
    google_search_btn = By.XPATH, '//form//div[3]/center/input[1]'
