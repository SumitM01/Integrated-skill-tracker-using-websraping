from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def leetcode_profile(url):

    leetcode_profile_details = dict()
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox') 
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service,options=options)
    try:
        # Open the leetcode profile page
        print(url)
        driver.get(url)
        print(driver.title) # page title    
        wait = WebDriverWait(driver, 20)
        try:
            # wait for the rank element to appear and store it in rank_element
            rank_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[3]/span[2]")))
            rank = rank_element.text

            # wait for the questions_solved element to appear and store it in contest_rating_element

            questions_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[1]")))
            # wait for the contest_rating element to appear and store it in contest_rating_element
            questions_solved = questions_solved_element.text
        
            contest_rating_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]")))
            contest_rating = contest_rating_element.text

            # wait for the contest_attended element to appear and store it in contest_attended_element
            contest_attended_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div[2]")))
            contest_attended = contest_attended_element.text
        except Exception as e:
            print("Inner except encountered",e)
            # wait for the rank element to appear and store it in rank_element
            rank_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[3]/span[2]")))
            rank = rank_element.text

            # wait for the questions_solved element to appear and store it in contest_rating_element

            questions_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[1]")))
            # wait for the contest_rating element to appear and store it in contest_rating_element
            questions_solved = questions_solved_element.text
            contest_rating = '0'
            contest_attended = '0'
        print(1)

        
        
        # store the user profile details in the dictionary
        leetcode_profile_details['rank'] =  int(rank.replace(",",""))
        leetcode_profile_details['contest_rating'] = int(contest_rating.replace(",",""))
        leetcode_profile_details['contest_attempted'] = int(contest_attended.replace(",",""))
        leetcode_profile_details['problem_solved'] = int(questions_solved.replace(",",""))
    except Exception as e:
        print("Timed out waiting for page to load due to",e)

    finally:
        # close the driver
        driver.quit()
        
        return leetcode_profile_details


def codechef_profile(url):

    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox') 
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service,options=options)
    codechef_profile_details = dict()
    try:
            # Open the leetcode profile page
            driver.get(url)
            print(driver.title) # page title    

            wait = WebDriverWait(driver, 20)

            # wait for the rank element to appear and store it in rank_element
            rank_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[1]/a/strong")))

            # wait for the contest_rating element to appear and store it in contest_rating_element
            contest_rating_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[1]")))

            # wait for the contest_attended element to appear and store it in contest_attended_element
            contest_attended_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div/div/section[3]/div[1]/div/b")))

            # wait for the questions_solved element to appear and store it in contest_rating_element
            questions_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div/div/section[6]/div/h5[1]")))

            # store the user profile details in the dictionary
            codechef_profile_details['rank'] = int(rank_element.text.replace(",","")) if rank_element.text.replace(",","").isdigit() else 0
            print(contest_rating_element.text)
            codechef_profile_details['contest_rating'] = int(contest_rating_element.text.replace("?i",""))
            codechef_profile_details['contest_attempted'] = int(contest_attended_element.text.replace(",",""))
            codechef_profile_details['problem_solved'] = int((questions_solved_element.text.replace(",","")).split(" ")[2].strip("(").strip(")"))

    except Exception as e:
        print("Timed out waiting for page to load due to",e)

    finally:
        # close the driver
        driver.quit()
        
    print(codechef_profile_details)
    return codechef_profile_details

def spoj_profile(url):

    spoj_profile_details = dict()

    return spoj_profile_details

def hackerrank_profile(url):

    hackerrank_profile_details = dict

    return hackerrank_profile_details


