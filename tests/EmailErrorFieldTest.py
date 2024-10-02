import allure
import pytest
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage


class TestEmailErrorField:
    users = [("IncorectEmail1", "123", "Please enter a valid email address (Ex: johndoe@domain.com)."),
             ("Gudsds", "111", "Please enter a valid email address (Ex: johndoe@domain.com)."),
             ("%TDSF#@EDD", "1#444", "Please enter a valid email address (Ex: johndoe@domain.com)."),
             ("hffg@.c", "rrrxca", "Please enter a valid email address (Ex: johndoe@domain.com).")]

    @allure.title("Filling incorrect emails")
    @pytest.mark.parametrize("user, password, expected_error", users)
    def test_01_loginFailed(self, user, password, expected_error):
        lp = LoginPage(self.driver)
        lp.login(user, password)
        assert lp.getEmailErrorMsg() == expected_error



