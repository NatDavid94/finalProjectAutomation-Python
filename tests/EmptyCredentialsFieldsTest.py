import allure
import pytest
from FinalProjectAutomation.pageobjects.LoginPage import LoginPage


class TestEmptyCredentialsField:
    users = [("", "", "This is a required field.", "This is a required field.")]

    @allure.title("Filling empty credentials")
    @pytest.mark.parametrize("user, password, expected_error_email, expected_error_pass", users)
    def test_01_loginFailed(self, user, password, expected_error_email,expected_error_pass):
        lp = LoginPage(self.driver)
        lp.login(user, password)

        assert lp.getEmailErrorMsg() == expected_error_email
        assert lp.getPassErrorMsg() == expected_error_pass


