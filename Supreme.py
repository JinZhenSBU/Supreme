# Jin Zhen


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import strftime
import time
from random import randint
from tkinter import *
from tkinter import ttk
import webbrowser, requests, bs4

#######################################################################
#         create gui
######################################################################
root = Tk()
root.wm_title("Supreme SS 17 WINDOW1")
root.geometry("700x550")
root.resizable(width=False, height=False)
# relating to item
keyword = Label(root, text='Keyword')
keyword2 = Label(root, text='Keyword')

color = Label(root, text='Color')
color2 = Label(root, text='Color')

itemType = Label(root, text='Item Type')
itemType2 = Label(root, text='Item Type')

itemTypeDrop = ['jackets', 't-shirts', 'tops/sweaters', 'sweatshirts', 'pants', 'hats', 'bags', 'accessories', 'shoes',
                'shirts', 'shorts', 'skate']
var4 = StringVar()
itemTypeVar2 = StringVar()
itemTypeDropList = OptionMenu(root, var4, *itemTypeDrop)
itemTypeDropList2 = OptionMenu(root, itemTypeVar2, *itemTypeDrop)
sizes = Label(root, text='Size')
sizes2 = Label(root, text='Size')

var5 = StringVar()
sizesVar2 = StringVar()

sizesDrop = ['Shoe Sizes', '----------------------------', '8', '8.5', '9', '9.5', '10', '10.5', '11', '11.5', '12',
             '----------------------------',
             'Pants Sizes', '----------------------------', '30', '32', '34', '36', '----------------------------',
             'Jackets/Coats/Shirts Sizes',
             '----------------------------', 'Small', 'Medium', 'Large', 'XLarge', '----------------------------',
             'Hat Sizes', '----------------------------',
             '7 1/8', '7 1/4', '7 3/8', '7 1/2', '7 5/8', '7 3/4', 'S/M', 'M/L', 'L/XL', '----------------------------',
             'Accessories/Bags', '----------------------------', 'ONE SIZE']
sizesDropList = OptionMenu(root, var5, *sizesDrop)
sizesDropList2 = OptionMenu(root, sizesVar2, *sizesDrop)

# below is billing info
name = Label(root, text='Full name')
email = Label(root, text='Email')
tel = Label(root, text='Phone #')
address = Label(root, text='Address')
addy2 = Label(root, text='Address 2')
zip = Label(root, text='Zip Code')
city = Label(root, text='City')
state = Label(root, text='State(ex: NY)')
var3 = StringVar()
cc = Label(root, text='Credit card #')
ccExpDate = Label(root, text='Exp. date')
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
var1 = StringVar()
monthsDropList = OptionMenu(root, var1, *months)
var2 = StringVar()
years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
yearsDropList = OptionMenu(root, var2, *years)
cvv = Label(root, text='CVV')
warning = Label(root, text='Bot will start at 10:59. ')
browserLocation = Label(root, text='Path to chromedriver.exe: ')
browserLocation2 = Label(root, text='Default location is: ')
browserLocation3 = Label(root, text='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browserLocation4 = Label(root, text='Leave blank if no changes')
warning = Label(root, text="Only fill above if you want two items, else leave blank")
checkboxVar = IntVar()

keywordEntry = Entry(root)
colorEntry = Entry(root)
nameEntry = Entry(root)
emailEntry = Entry(root)
telEntry = Entry(root)
addressEntry = Entry(root)
addy2Entry = Entry(root)
zipEntry = Entry(root)
cityEntry = Entry(root)
stateEntry = Entry(root)
ccEntry = Entry(root)
cvvEntry = Entry(root)
browserLocationEntry = Entry(root)
keywordEntry2 = Entry(root)
colorEntry2 = Entry(root)

keyword.grid(row=0)
color.grid(row=1)
itemType.grid(row=2)
sizes.grid(row=3)
name.grid(row=4)
email.grid(row=5)
tel.grid(row=6)
address.grid(row=7)
addy2.grid(row=8)
zip.grid(row=9)
city.grid(row=10)
state.grid(row=11)
cc.grid(row=12)
ccExpDate.grid(row=13)
cvv.grid(row=15)
warning.grid(row=15, column=1)
browserLocation.grid(row=16)
browserLocation4.grid(row=17)
browserLocation2.place(relx=0.5, rely=0.87, anchor=CENTER)
browserLocation3.place(relx=0.5, rely=0.91, anchor=CENTER)

keywordEntry.grid(row=0, column=1)
colorEntry.grid(row=1, column=1)
itemTypeDropList.grid(row=2, column=1)
sizesDropList.grid(row=3, column=1)
nameEntry.grid(row=4, column=1)
emailEntry.grid(row=5, column=1)
telEntry.grid(row=6, column=1)
addressEntry.grid(row=7, column=1)
addy2Entry.grid(row=8, column=1)
zipEntry.grid(row=9, column=1)
cityEntry.grid(row=10, column=1)
stateEntry.grid(row=11, column=1)
ccEntry.grid(row=12, column=1)
monthsDropList.grid(row=13, column=1)
yearsDropList.grid(row=13, column=2)
cvvEntry.grid(row=15, column=1)
browserLocationEntry.grid(row=17, column=1)
keyword2.grid(row=0, column=3)
keywordEntry2.grid(row=0, column=4)
color2.grid(row=1, column=3)
colorEntry2.grid(row=1, column=4)
itemType2.grid(row=2, column=3)
itemTypeDropList2.grid(row=2, column=4)
sizes2.grid(row=3, column=3)
sizesDropList2.grid(row=3, column=4)
warning.grid(row=4, column=4)


#################################################################################


###


############################################## JACKETS SECTION ################

#################################################################################



def openTypeOfItem(var):
    print(str(keywordEntry.get()).title())
    if (var.get() == 'jackets'):
        browser.get('http://www.supremenewyork.com/shop/all/jackets')
    if (var.get() == 't-shirts'):
        browser.get('http://www.supremenewyork.com/shop/all/t-shirts')
    if (var.get() == 'tops/sweaters'):
        browser.get('http://www.supremenewyork.com/shop/all/tops_sweaters')
    if (var.get() == 'sweatshirts'):
        browser.get('http://www.supremenewyork.com/shop/all/sweatshirts')
    if (var.get() == 'pants'):
        browser.get('http://www.supremenewyork.com/shop/all/pants')
    if (var.get() == 'hats'):
        browser.get('http://www.supremenewyork.com/shop/all/hats')
    if (var.get() == 'bags'):
        browser.get('http://www.supremenewyork.com/shop/all/bags')
    if (var.get() == 'accessories'):
        browser.get('http://www.supremenewyork.com/shop/all/accessories')
    if (var.get() == 'shoes'):
        browser.get('http://www.supremenewyork.com/shop/all/shoes')
    if var.get() == 'skate':
        browser.get('http://www.supremenewyork.com/shop/all/skate')
    if var.get() == 'shorts':
        browser.get('http://www.supremenewyork.com/shop/all/shorts')
    if var.get() == 'shirts':
        browser.get('http://www.supremenewyork.com/shop/all/shirts')


def findItem(keywordEntry, colorEntry):

    size = browser.find_elements_by_tag_name('article')

    while True:
        try:
            for i in range(1, len(size)):
                link = browser.find_element_by_xpath('//*[@id="container"]/article[' + str(i) + ']/div/h1/a')
                if (str(keywordEntry).title() in link.text):
                    x = i
                    break

            while True:
                temp = '//*[@id="container"]/article[' + str(x) + ']/div/p/a'
                linkColor = browser.find_element_by_xpath(temp)
                if (linkColor.text == str(colorEntry).title()):
                    linkColor.click()
                    break
                else:
                    x += 1

            # Break loop when item is found
            break
        except:
            browser.refresh()
            continue

            # Adds size to cart


def addSizeToCart(var):
    browser.get(browser.current_url)
    if (var != 'ONE SIZE'):
        sizeSelect = Select(browser.find_element_by_id('s'))
        sizeSelect.select_by_visible_text(var)
    browser.find_element_by_name('commit').click()


def checkout():
    browser.get('https://www.supremenewyork.com/checkout')
    prefill = browser.find_element_by_id('order_billing_name')

    # fills out cc number and tel first
    addyLine = browser.find_element_by_id('bo')
    addyLine.send_keys(ccEntry.get())  # takes cc number and puts it in name
    addyLine.send_keys(Keys.CONTROL, 'a')
    addyLine.send_keys(Keys.CONTROL, 'c')  # copy
    ccNumber = browser.find_element_by_id('cnb')
    ccNumber.send_keys(Keys.CONTROL, 'v')  # paste

    addyLine2 = browser.find_element_by_id('oba3')
    addyLine2.send_keys(telEntry.get())
    addyLine2.send_keys(Keys.CONTROL, 'a')
    addyLine2.send_keys(Keys.CONTROL, 'c')
    telNum = browser.find_element_by_id('order_tel')
    telNum.send_keys(Keys.CONTROL, 'v')

    prefill.send_keys(nameEntry.get(), Keys.TAB, emailEntry.get(), Keys.TAB, Keys.TAB, addressEntry.get(), Keys.TAB,
                      addy2Entry.get(), Keys.TAB, zipEntry.get(), Keys.TAB, cityEntry.get())

    # below fills in state
    state2 = Select(browser.find_element_by_id('order_billing_state'))
    state2.select_by_visible_text(stateEntry.get())

    # below fills in credit card info

    ccMonth = Select(browser.find_element_by_id('credit_card_month'))
    ccMonth.select_by_visible_text(var1.get())
    ccYear = Select(browser.find_element_by_id('credit_card_year'))
    ccYear.select_by_visible_text(var2.get())
    browser.find_element_by_id('vval').send_keys(cvvEntry.get(), Keys.TAB, Keys.SPACE)
    browser.find_element_by_id('vval').send_keys(Keys.ENTER)


def loginChrome():
    browser.get('https://accounts.google.com/ServiceLogin?hl=en&sacu=1')
    emailBox = browser.find_element_by_id('identifierId')
    emailBox.send_keys('PUT IN EMAIL HERE', Keys.ENTER)

    time.sleep(3)

    time.sleep(1)
    time.sleep(3)


def execute():
    global browser

    if len(browserLocationEntry.get()) == 0:
        browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    else:
        browser = webdriver.Chrome(browserLocationEntry.get())
    loginChrome()
    openTypeOfItem(var4)
    while True:
        # 105945 is 10:59:45 . Drop is at 11
        # 105945
        # 105950
        if (int(strftime("%H%M%S")) > 105957):
            while True:
                try:
                    browser = browser.get(browser.current_url)
                    findItem(keywordEntry.get(), colorEntry.get())
                    break;
                except:
                    print('failed')
                    time.sleep((randint(7, 10)) / 10)
                    browser.refresh()
                    browser = browser.get(browser.current_url)
            break;
        else:
            {
                time.sleep(4)
            }
    addSizeToCart(var5.get())
    time.sleep(0.3)
    if len(keywordEntry2.get()) != 0:
        openTypeOfItem(itemTypeVar2)
        findItem(keywordEntry2.get(), colorEntry2.get())
        addSizeToCart(sizesVar2.get())
        time.sleep(0.1)
    else:
        time.sleep(0.2)
    checkout()


###############################################################
###
###         BELOW IS A TESTING FUNCTION TO SEE IF IT WORKS
###
###
###############################################################


def test():
    global browser

    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    loginChrome()
    browser.get('http://www.supremenewyork.com/shop/all/accessories')

    findItem('Tagless', 'White')
    addSizeToCart('Medium')
    time.sleep(1)
    browser.get('https://www.supremenewyork.com/checkout')
    prefill = browser.find_element_by_id('order_billing_name')

    # fills out cc number and tel first
    addyLine = browser.find_element_by_id('bo')
    addyLine.send_keys('1234567890123456')  # takes cc number and puts it in name
    addyLine.send_keys(Keys.CONTROL, 'a')
    addyLine.send_keys(Keys.CONTROL, 'c')  # copy
    ccNumber = browser.find_element_by_id('cnb')
    ccNumber.send_keys(Keys.CONTROL, 'v')  # paste

    addyLine2 = browser.find_element_by_id('oba3')
    addyLine2.send_keys('9179179177')
    addyLine2.send_keys(Keys.CONTROL, 'a')
    addyLine2.send_keys(Keys.CONTROL, 'c')
    telNum = browser.find_element_by_id('order_tel')
    telNum.send_keys(Keys.CONTROL, 'v')

    prefill.send_keys('Jonh Fm', Keys.TAB, 'text13@gmail.com', Keys.TAB, Keys.TAB, 'Test addy 1', Keys.TAB,'test addy 2', Keys.TAB, '11221', Keys.TAB,'Brooklyn')

    # below fills in state
    state2 = Select(browser.find_element_by_id('order_billing_state'))
    state2.select_by_visible_text('NY')

    # below fills in credit card info

    ccMonth = Select(browser.find_element_by_id('credit_card_month'))
    ccMonth.select_by_visible_text('03')
    ccYear = Select(browser.find_element_by_id('credit_card_year'))
    ccYear.select_by_visible_text('2021')
    browser.find_element_by_id('vval').send_keys('526', Keys.TAB, Keys.SPACE)
    browser.find_element_by_id('vval').send_keys(Keys.ENTER)

    ################################################################
    ################################################################

Start = Button(root, text='Start', command=execute)
Start.grid(row=19, column=1)

Test = Button(root, text= 'Test', command = test)
Test.grid(row=19, column=4)

root.mainloop()



