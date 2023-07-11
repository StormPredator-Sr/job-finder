from driver import *

async def google_query(driver,keyword):
    driver.get(f'https://careers.google.com/jobs/results/?distance=50&q={keyword}')
    # jobs = driver.find_element(By.ID, 'search-results').find_elements(By.TAG_NAME,"li")
    # Takes time to render the list so we wait
    wait = WebDriverWait(driver, 10)
    jobs = wait.until(EC.visibility_of_element_located((By.ID, 'search-results'))).find_elements(By.CLASS_NAME, 'gc-card__container')
    json = []
    for job in jobs:
        title = job.find_element(By.TAG_NAME, 'h2').text
        address = job.find_element(By.CSS_SELECTOR, '[itemprop="address"]').text
        link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
        json.append({'title':title,'address':address,'salary': 0,'link':link})

    return json
