def program_starter():
    print("Input the zip: ")
    zip = input()
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome('/Users/Jia/Downloads/chromedriver')
    driver.get("https://www.taxjar.com/sales-tax-calculator/")

    blanks = driver.find_element_by_id("zip")

    blanks.clear()
    blanks.send_keys(zip)
    blanks.submit()

    import time
    time.sleep(3)

    total_tax_raw = driver.find_element_by_id('summary').text
    import re
    total_tax = re.findall("\d+\.\d+", total_tax_raw)

    if(len(total_tax) == 0):
        print("Rates can not be found for this location, please double check the zip code you entered.")
        driver.close()
        program_starter()

    else:
        state = driver.find_element_by_id('state_name').text
        city = driver.find_element_by_id('city_name').text
        county = driver.find_element_by_id('county_name').text


        state_rate = driver.find_element_by_id('state_rate').text
        city_rate = driver.find_element_by_id('city_rate').text
        county_rate = driver.find_element_by_id('county_rate').text
        district_rate = driver.find_element_by_id('district_rate').text
        driver.close()

        print ("State: " + state)
        print ("County: " + county)
        print ("City: " + city)

        print()
        print ("State rate is: " + state_rate)
        print ("County rate is: " + county_rate)
        print ("City rate is: " + city_rate)
        print ("District rate is: " + district_rate)
        print ("Total Sales Tax Rate: " + total_tax[0] + '%')

program_starter()
