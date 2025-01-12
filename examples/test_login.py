from seleniumbase import BaseCase


class SwagLabsLoginTests(BaseCase):
    def login_to_swag_labs(self):
        self.open("https://www.saucedemo.com")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce")
        self.click('input[type="submit"]')

    def test_swag_labs_login(self):
        self.login_to_swag_labs()
        self.assert_element("#inventory_container")
        self.assert_element('.inventory_item:contains("Sauce Labs Backpack")')
