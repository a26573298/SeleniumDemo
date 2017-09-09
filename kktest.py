from selenium import webdriver
from login_module import Login
import unittest, time

class KKweb_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1250,900)
        self.driver.get("https://play.kkbox.com/")

        #登入
        username = "a26573298@yahoo.com.tw"
        password = "test"
        Login().user_login(self.driver, username, password)

    # 登入： 在登入頁面輸入正確帳號、密碼，可以成功登入，左方顯示「我的音樂庫」、「線上精選」、「電台」、「一起聽」4 個頁籤。
    def test_Case1(self):
        driver = self.driver
        time.sleep(2)

        # 判斷登入錯誤訊息是否存在
        try:
            driver.find_element_by_xpath("//*[@id='login']/div/div[1]/div/div/div[2]").is_displayed()
        except:
            driver.save_screenshot("Test_Case1.png")
        else:
            self.assertTrue( False, driver.find_element_by_xpath("//*[@id='login']/div/div[1]/div/div/div[2]").text )


    ## 搜尋： 搜尋「清平調」，可找到王菲與鄧麗君合唱的「清平調」。
    def test_Case2(self):
        driver = self.driver

        # 搜尋框內輸入 清平調
        driver.find_element_by_xpath("//*[@id='search_form']/input").send_keys("清平調")

        # Click 搜尋 Button
        driver.find_element_by_id("search_btn_cnt").click()

        # 抓取 list 內容 
        # 定位 tbody
        res = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/table/tbody")
        # tbody > tr
        row = res.find_elements_by_tag_name("tr")
        for rows in row:
            # tbody > tr > td
            cols = rows.find_elements_by_tag_name("td")
            for a in cols:
                # tbody > tr > td 的內容
                ## 找到「王菲」與「鄧麗」君合唱的「清平調」。
                if "王菲" in a.text and "鄧麗君" in a.text:
                    true = a.text
                    print( true )

        # 執行斷言
        if "王菲" in true and "鄧麗君" in true:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    

    ## 電台播放的 Dislike 按鈕： 播放任一電台，點擊 Dislike 按鈕，自動切到下一首歌曲開始播放。
    def test_Case3(self):
        driver = self.driver

        # Click 電台頁籤
        driver.find_element_by_link_text("電台").click()
        time.sleep(5)

        # Click 圖片
        driver.find_element_by_xpath("//*[@id='promote-stations']/div/ul/li[2]/div/div[1]/a/img").click()

        # Click 播放按鈕
        driver.find_element_by_xpath("//*[@id='promote-stations']/div/ul/li[2]/div/div[1]/div/a").click()
        time.sleep(2)

        # 處理彈跳視窗
        if driver.switch_to_alert():
            driver.switch_to_alert().accept()
            time.sleep(2)
        else:
            time.sleep(2)

        #存下音樂名稱
        musicname = driver.find_element_by_xpath("//*[@id='player']/div[2]/h3").text

        # Click Dislike 按鈕
        driver.find_element_by_xpath("//*[@id='player']/div[6]/a[1]").click()

        # 判斷 Dislike 按鈕是否按下 
        self.assertEqual( driver.find_element_by_xpath("//*[@id='player']/div[6]/a[1]").get_attribute("class"), "ng-scope disabled", "Dislike Fail !" )
        time.sleep(3)

        # 判斷是否切換到下一首歌
        self.assertNotEqual( musicname, driver.find_element_by_xpath("//*[@id='player']/div[2]/h3").text, "Music of the same name" )
        time.sleep(2)

        # 判斷是否有自動播放
        self.assertEqual( driver.find_element_by_id("playBtn").get_attribute("style"), "display: none;", "No play !" )
        self.assertNotEqual( driver.find_element_by_id("playBar").get_attribute("style"), "width: 0%;", "No play !" )


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
