from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager # The Webdriver
import pyautogui        # To Click
import time             # To wait and all
custom_site = input("Enter The Website to Download Video...") # Take the youtube video link as the input
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) # installs the webdriver.

cus = custom_site.find('y')    # Finds 'Y' in the Link.
suc = custom_site[0:cus]    # Slices upto but not includes y
final_website = suc + 'ss' + custom_site[cus:]   # WIth the help of string concatenation it adds ss to the
                                                    # link before the letter 'y'

web = driver.get(final_website)     # Uses the Selenium Web  driver to go to the website.
driver.implicitly_wait(5)   # Waits For 5 Secs
driver.find_element_by_xpath(r'/html/body/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a').click()
# Finds the download button by x path

# Often after clicking the download button the new tab gets open automatically.
# If a new tab gets open it closes that tab.
# You Can Run the below program in your terminal to get the live position of your mouse
# import pyautogui
# pyautogui.displayMousePosition()


def new_tab_cut():
    x = 504  # You can change the x cordinate to your mouse position.
    y = 48  # # You can change the y cordinate to your mouse position.
    pyautogui.moveTo(x, y, duration=1.2)
    pyautogui.click(x, y)

# The Following block of code is used to click on the download button in firefix browser.


def save_file():
    x1 = 504
    y1 = 471
    pyautogui.moveTo(x1, y1, duration=1)
    pyautogui.click(x1, y1)
    time.sleep(1)
    x2 = 916
    y2 = 575
    pyautogui.click(x2, y2)
    time.sleep(1)


new_tab_cut()
save_file()
time.sleep(100)
driver.quit()
print("Downloaded")

# executable_path=GeckoDriverManager().install()