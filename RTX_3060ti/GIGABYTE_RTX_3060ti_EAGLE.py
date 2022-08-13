from selenium import webdriver
#Get access to keys like 'enter' and 'esc' and etc...
from selenium.webdriver.common.keys import Keys
import time
#import lib to provide wait conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
#SmartProxy Imports

#Assign the path variable to the string equal to the location of the driver you want to use - Must corespond with browser
PATH = "/Users/Nay/Desktop/drivers/chromedriver"

#This is always the first step -- Pick the driver you want to use
driver = webdriver.Chrome(PATH)

#Setting Options and Changing User Agent For Every Login
options = Options()
#Load Cookies to have login information
#options.add_argument("user-data-dir=C:\\Users\\Neutron\\AppData\\Local\\Google\\Chrome\\User Data")
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options, executable_path=PATH)

#Set window size to 1920 by 1080
driver.set_window_size(1152, 720)

#GIGABYTE RTX 3060ti Eagle Product Page
url_EVGA_RTX_XC_3060ti = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-eagle-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442485.p?skuId=6442485"
#Item Name
item = "GIGABYTE - NVIDIA GeForce RTX 3060 Ti EAGLE"

#Test URL
url_HDMI = "https://www.bestbuy.com/site/dynex-6-hdmi-cable-black/6405508.p?skuId=6405508"

#Cart
url_Cart = "https://www.bestbuy.com/cart"

#Login Info
email =  '' #Enter Your Best Buy Login Info
password =  '' #Enter Your Best Buy Password

#CVV
cvv = '' #Enter CVV For Card

#Personal Info
first_name = '' #Enter First Name
last_name = '' #Enter Last Name
address = '' #Enter Street Adress
city = '' #Enter City For Card
zip_code = '' #Enter Zip Code

#Relogin Page
url_ReLogin = "https://www.bestbuy.com/identity/signin?token=tid%3Ac17de720-a891-11eb-b215-005056aea131"

#Assign Target Page For Product
target = url_EVGA_RTX_XC_3060ti

#Go To Desired Site
driver.get(target)

#First Check if logged in - If Logged in signout, if not logged in - proceed
def login_status():
    # Locate User Logged In Banner

    account_signed_in = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='flyBtn logged_user_name']"))
    )
    print(account_signed_in)
    print('Must Sign Out Before You Proceed')

    #If Login Banner has Your Name - Your are Signed In.  Must Sign Out
    if driver.find_element(By.XPATH, "//span[@class='flyBtn logged_user_name']"):
        driver.find_element(By.XPATH, "//span[@class='flyBtn logged_user_name']").click()

        #Locate Signout Button
        signout = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign Out')]"))
        )
        print(signout)
        signout.click()
        print('Signing Out......')
        #Return to target page
        driver.get(target)

    else:
        print('xyz')

#Scan Items for a button with the text add to cart - to ensure its in stock
def get_stock():
    print('Checking Stock of ' + item + '....')
    # Checking If the Add To Cart Button Exist
    add_to_cart = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to Cart')]"))
    )

    # Add Item To Cart
    print(add_to_cart)
    print('In Stock... Button Found')
    add_to_cart.click()
    print('Adding to cart....')

    # Going to cart after item was added
    # time.sleep(10)
    # driver.get(url_Cart)
    print('Heading To Cart....')

    time.sleep(1)

    # if driver.find_element(By.XPATH, "//button[contains(text(),'Go to Cart')]"):
    #     driver.find_element(By.XPATH, "//button[contains(text(),'Go to Cart')]").click()
    #     print('Modal Window PopUp Avoided')
    #
    # else:
    #     print('No Modal Popup Window.... Continue')

#Once In Cart Click Checkout to start checkout process
def secure_checkout():
    time.sleep(1.5)
    # Locate Checkout Button On Page
    checkout = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Checkout')]"))
    )

    print(checkout)
    checkout.click()
    print('Heading to checkout.....')

#When Browser Makes You Relogin
def relogin():
    # Incase browser makes you sign back in
    time.sleep(2.5)
    print(driver.current_url)
    # Checking if web address is the Relogin address
    if driver.current_url[:35] == url_ReLogin[:35]:
        print('Relogging in .... ')

        # Locating Email field
        email_field = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
        )

        # Entering Email into Email field
        email_field.click()
        email_field.clear()
        email_field.send_keys(email)  # fills text box with whats in the parenthesis
        print('Email Entered.....')

        # Locating Passworc field
        password_field = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
        )

        # Entering Password into password field
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)  # fills text box with whats in the parenthesis
        print('Password Entered....')

        # Entering Password
        password_field.send_keys(Keys.RETURN)  # hit enter or return in that search box
        print('ReLogin Succesful')

#Continue To Payment
def continue_to_payment():
    time.sleep(1)
    # Locate Continue To Payment Information Button
    continue_to_payment = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Continue to Payment Information')]"))
    )
    print(continue_to_payment)
    continue_to_payment.click()
    print('Heading to payment page .....')

#Enter Credentials and place order --- Uncomment The click on the final step to activate checkout
def enter_credentials_and_place_order():
    time.sleep(0.5)
    # Locating Security Code Input
    security_code = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='credit-card-cvv']"))
    )
    print(security_code)
    # Enter CVV
    security_code.click()
    security_code.clear()
    security_code.send_keys(cvv)
    print('CVV entered')

    # Billing Address
    # Locate First Name
    name_input_first = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='payment.billingAddress.firstName']"))
    )
    print(name_input_first)
    name_input_first.click()
    name_input_first.clear()
    name_input_first.send_keys(first_name)
    print('First Name Entered.....')

    # Locate Last Name
    name_input_last = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='payment.billingAddress.lastName']"))
    )

    print(name_input_last)
    name_input_last.click()
    name_input_last.clear()
    name_input_last.send_keys(last_name)
    print('Last Name Entered....')

    # Locate Address
    input_address = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='payment.billingAddress.street']"))
    )
    print(input_address)
    input_address.click()
    input_address.clear()
    input_address.send_keys(address)
    print('Address entered....')

    # Hide Suggestions
    hide_suggestions = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Hide Suggestions')]"))
    )
    print(hide_suggestions)
    hide_suggestions.click()
    print('Hid Suggestions....')

    # Locate City Element
    input_city = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='payment.billingAddress.city']"))
    )
    print(input_city)
    input_city.click()
    input_city.clear()
    input_city.send_keys(city)
    print('City Entered...')

    # Select State from Options menu
    select = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//option[@value='NY']"))
    )
    print(select)
    select.click()
    print('State Selected....')

    # Locate ZipCode
    input_zip_code = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='payment.billingAddress.zipcode']"))
    )
    print(input_zip_code)

    # Enter Zip Code
    input_zip_code.click()
    input_zip_code.clear()
    input_zip_code.send_keys(zip_code)
    print('Zip Code Entered....')

    # Locate Place Order Button
    place_order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Place Your Order')]"))
    )
    print(place_order_button.text)
    # Uncomment Out This Line When Trying To Order
    place_order_button.click()
    print('Placing Order .... God Speed')


#Happy Scraping
def scrape():
    # Scan Items for a button with the text add to cart - Check If Any Of The Items Are Available
    try:
        get_stock()

        # Once In Cart Click Checkout
        try:
            secure_checkout()

            # When Browser makes you relogin
            try:
                relogin()

                # Continue To Payment
                try:
                    continue_to_payment()

                    # Payment Page - Enter Credentials and Place Order
                    try:
                        enter_credentials_and_place_order()

                    except:
                        print('Could not place order')
                        time.sleep(2)
                        driver.get(target)

                except:
                    print('Failed to continue to payment')
                    time.sleep(2)
                    driver.get(target)

            except:
                print('Relogin Failed')
                time.sleep(2)
                driver.get(target)

        except:
            print('Failed to Go to checkout')
            time.sleep(2)
            driver.get(target)

    except:
        print('Item Not In Stock... Get Stock Failed')
        time.sleep(1)
        driver.get(target)


# try:
#     #Checking If the Add To Cart Button Exist
#     add_to_cart = WebDriverWait(driver, 3).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to Cart')]"))
#     )
#
#     #Add Item To Cart
#     print('In Stock... Button Found')
#     add_to_cart.click()
#     print('Adding to cart....')
#
# except:
#     print('No Item In Stock..... Refreshing')


# Logout If You Are Currently Logged In
try:
    login_status()
except:
    print('Not Signed In... Continue')
    time.sleep(2)
    # driver.get(target)

while driver.current_url == target:
    scrape()















