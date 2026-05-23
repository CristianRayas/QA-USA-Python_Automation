from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Call a taxi")]')

    SUPPORTIVE_PLAN = (
        By.XPATH,
        '//div[contains(@class, "tcard") and .//div[contains(text(), "Supportive")]]'
    )

    PHONE_NUMBER_FIELD = (By.CLASS_NAME, "np-text")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Next")]')
    PHONE_CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')

    PAYMENT_METHOD = (By.CLASS_NAME, "pp-text")
    ADD_CARD_BUTTON = (By.XPATH, '//div[contains(text(), "Add card")]')
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (
        By.XPATH,
        '//input[@id="code" and contains(@class, "card-input")]'
    )
    LINK_BUTTON = (By.XPATH, '//button[contains(text(), "Link")]')

    COMMENT_FIELD = (By.ID, "comment")

    BLANKET_SLIDER = (By.XPATH, '//div[contains(@class, "switch")]')
    BLANKET_CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')

    ICE_CREAM_PLUS_BUTTON = (By.XPATH, '(//div[contains(@class, "counter-plus")])[last()]')
    ICE_CREAM_COUNT = (By.XPATH, '(//div[contains(@class, "counter-value")])[last()]')

    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "smart-button")]')
    CAR_SEARCH_MODAL = (By.CLASS_NAME, "order-body")

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def set_from(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from_value(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property("value")

    def get_to_value(self):
        return self.driver.find_element(*self.TO_FIELD).get_property("value")

    def click_call_taxi_button(self):
        self.click_element(self.CALL_TAXI_BUTTON)

    def select_supportive_plan(self):
        supportive = self.driver.find_element(*self.SUPPORTIVE_PLAN)
        if "active" not in supportive.get_attribute("class"):
            self.driver.execute_script("arguments[0].click();", supportive)

    def get_supportive_plan_class(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN).get_attribute("class")

    def fill_phone_number(self, phone_number):
        self.click_element(self.PHONE_NUMBER_FIELD)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone_number)
        self.click_element(self.NEXT_BUTTON)

    def fill_phone_code(self, code):
        self.driver.find_element(*self.PHONE_CODE_INPUT).send_keys(code)
        self.click_element(self.CONFIRM_BUTTON)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD).text

    def add_card(self, card_number, card_code):
        self.click_element(self.PAYMENT_METHOD)
        self.click_element(self.ADD_CARD_BUTTON)

        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)

        code_field = self.driver.find_element(*self.CARD_CODE_INPUT)
        code_field.send_keys(card_code)
        code_field.send_keys(Keys.TAB)

        self.click_element(self.LINK_BUTTON)

        # Close modal safely
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    def get_payment_method(self):
        text = self.driver.find_element(*self.PAYMENT_METHOD).text
        if text == "Payment method":
            return "Card"
        return text

    def write_comment_for_driver(self, message):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(message)

    def get_driver_comment(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_property("value")

    def order_blanket_and_handkerchiefs(self):
        self.click_element(self.BLANKET_SLIDER)

    def is_blanket_and_handkerchiefs_selected(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX).get_property("checked")

    def order_ice_creams(self, amount):
        for _ in range(amount):
            self.click_element(self.ICE_CREAM_PLUS_BUTTON)

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT).text

    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    def is_car_search_modal_displayed(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()