import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        "input[name='username']"))).send_keys(self.email)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        "input[name='password']"))).send_keys(self.password)
        passwordInput =WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        "button[type='submit']")))
        passwordInput.click()
        time.sleep(5)

    def signInWithFb(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        "span[class='KPnG0']"))).click()
        #work remaining

    def followToSuggested(self):
        self.browser.get('https://www.instagram.com/explore/people/suggested/')
        buttons=WebDriverWait(self.browser,30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[type='button']")))
        print(len(buttons))
        for x in range(0,len(buttons)):
            if buttons[x].is_displayed():
                buttons[x].click()         

    def followWithUsername(self, userlink):
        self.browser.get(userlink)
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")


    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers


bot = InstagramBot('youremail', 'yourpassword')
bot.signIn()
time.sleep(5)
bot.followToSuggested()
time.sleep(10)
followers=bot.getUserFollowers('otheraccountusername',10)
print(followers)
for users in followers:
    bot.followWithUsername(users)       






        # if(len(buttons)<100):
        #     actionChain = webdriver.ActionChains(self.browser)            
        #     actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        #     newbuttons=WebDriverWait(self.browser,30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button[type='button']")))
        #     buttons.append(newbuttons)
