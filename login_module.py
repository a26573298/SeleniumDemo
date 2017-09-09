class Login():
    def user_login(self, driver, username, password):
        driver.find_element_by_id("uid").clear()
        driver.find_element_by_id("uid").send_keys(username)
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys(password)
        driver.find_element_by_id("login-btn").click()