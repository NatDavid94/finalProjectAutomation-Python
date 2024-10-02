import allure
import pytest
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage


class TestNotExistEmailErrorField:
    users = [("email1@walla.co.il", "123", "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."),
             ("email2@gmail.com", "111", "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."),
             ("email3@homail.com", "1#444", "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."),
             ("email4@outlook.com", "rrrxca", "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")]

    @allure.title("Filling emails that don't exist")
    @pytest.mark.parametrize("user, password, expected_error", users)
    def test_01_loginFailed(self, user, password, expected_error):
        lp = LoginPage(self.driver)
        lp.login(user, password)
        assert lp.getNotExistEmailErrorMsg() == expected_error



