from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import datetime, re

def hackerrank_contest(url):
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service)

    #Declare a list of dictionaries to store the contest details
    hackerrank_contest_details = []

    try:
        # Open the CodeChef contests page
        driver.get(url)
        print(driver.title) # page title

        # wait for the table to load
        list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'contests-active'))) 
        
        # get the items from the list
        items = list.find_elements(By.CLASS_NAME, 'card-content')
        print(items[0].text.split("\n"))

        #Declare a dictionary to store the contest details
        contest_details = dict()
        contest_details['platform'] = "Hackerrank"
        contest_details['name'] = items[0].text.split("\n")[0]
        contest_details['time'] = "00:00:00"
        contest_details['date'] = datetime.date(2023, 1, 1)
        contest_details['duration'] = None
        contest_details['status'] = "Ongoing"
        hackerrank_contest_details.append(contest_details)
        
    except Exception as e:
        print(e)
    finally:
        # close the driver
        driver.quit()

    return hackerrank_contest_details


def codechef_contest(url):
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service)

    #Declare a list of dictionaries to store the contest details
    codechef_contest_details = list()

    try:
        # Open the CodeChef contests page
        driver.get("https://www.codechef.com/contests")
        print(driver.title)
        #scrape ongoing contests -- wait for the table to load
        container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, '_contest-tables__container_1c9os_225')))
        
        tables = container.find_elements(By.CLASS_NAME,'_dataTable__container_1c9os_369')
        
        for i in range(2):
            rows = tables[i].find_elements(By.TAG_NAME, 'tr')
                # loop through the rows and print the data
            for row in rows[1:]:
                columns = row.find_elements(By.TAG_NAME, 'td')
                if len(columns) >1:
                    #Declare a dictionary and insert contest data for each row
                    contest_details = dict()
                    contest_details['platform'] = "Codechef"
                    contest_details['name'] = columns[1].text
                    contest_details['time'] = columns[2].text.split("\n")[1][4:]+":00"
                    contest_details['date'] = datetime.datetime.strptime(columns[2].text.split("\n")[0], '%d %b %Y').date()
                    contest_details['duration'] = None if columns[3].text == "NA" else columns[3].text
                    contest_details['status'] = "Ongoing" if columns[3].text == "NA" else "Upcoming"
                    codechef_contest_details.append(contest_details) 
              
    except TimeoutException:
        print("Timed out waiting for page to load")

    finally:
        # close the driver
        driver.quit()
    
    return codechef_contest_details



def leetcode_contest(url):
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox') 
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service,options=options)
    leetcode_contest_details = list()
    try:
        # Open the leetcode contests page
        driver.get(url)
        print(driver.title) # page title    

        # wait for the content to load
        contests = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.CLASS_NAME, "swiper-wrapper")) 

        # get the items from the list
        # items = list.find_elements(By.CLASS_NAME, 'swiper-wrapper')
        contest = list(contests.text.split("\n"))
        
        now = datetime.datetime.now()
        i=0
        while(i<len(contest)):
            contest_details = dict()
            contest_details['platform'] = 'Leetcode'
            contest_details['name'] = contest[i+1]
            contest_details['time'] = datetime.datetime.strptime(contest[i+2], '%A %I:%M %p GMT+5:30').strftime('%H:%M')+":00"
            # contest start time as string
            time_str = contest[i]
            print(time_str)
            days = 0
            hours = 0
            if 'd' in time_str:
                days = int(re.findall(r'\d+d?', time_str)[0].replace('d', ''))
            if 'h' in time_str:
                hours = int(re.findall(r'\d+h', time_str)[0].replace('h', ''))
            minutes = int(re.findall(r'\d+m', time_str)[0].replace('m', ''))
            seconds = int(re.findall(r'\d+s', time_str)[0].replace('s', ''))

            # calculate contest start time
            if 'Ends' in time_str:
                contest_time = now - datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
            else:
                contest_time = now + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

            # extract the date of the contest start time
            contest_details['date'] = contest_time.date()
            contest_details['duration'] = "1.5 hrs"
            contest_details['status'] = "Upcoming"
            leetcode_contest_details.append(contest_details) 
            i+=3

    except (TimeoutException,Exception) as e:
        print(e)

    finally:
        # close the driver
        driver.quit()

    return leetcode_contest_details

def spoj_contest(url):
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service)

    # Open the CodeChef contests page
    
    driver.get(url)
    print(driver.title)
    
    contest_details_list = list()
    try:
        #scrape ongoing contests -- wait for the table to load
        container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'content')))

        tables = container.find_elements(By.CLASS_NAME,'col-md-6')
        for i in range(2):
            rows = tables[i].find_elements(By.TAG_NAME, 'tr')
                # loop through the rows and print the data
            for row in rows[1:]:
                columns = row.find_elements(By.TAG_NAME, 'td')
                if len(columns) > 0:

                    #Declare a dictionary to store the contest details
                    contest_details = dict()
                    contest_details['platform'] = "Spoj"
                    contest_details['name'] = columns[0].text
                    contest_details['time'] = "00:00:00"
                    contest_details['date'] = datetime.datetime.strptime(columns[1].text, '%Y-%m-%d').date()
                    start_date = datetime.datetime.strptime(columns[1].text, '%Y-%m-%d').date()
                    end_date = datetime.datetime.strptime(columns[2].text, '%Y-%m-%d').date()
                    contest_details['duration'] = str((end_date-start_date).days)+" days"
                    contest_details['status'] = "Ongoing"
                    contest_details_list.append(contest_details)
    
    except Exception as e:
        print("Timed out waiting for page to load due to",e,"error at line")

    finally:
        # close the driver
        driver.quit()
    
    return contest_details_list
    

