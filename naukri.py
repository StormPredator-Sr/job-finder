from driver import *

async def naukri_query(driver,keyword):
    driver.get('https://www.naukri.com/javascript-jobs?k=javascript')
    # Takes time to render the list so we wait
    wait = WebDriverWait(driver, 10)
    jobs = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'list'))).find_elements(By.TAG_NAME, 'article')
    json = []
    for job in jobs:
        title = job.find_element(By.CLASS_NAME, 'title').text
        link = job.find_element(By.CLASS_NAME, 'title').get_attribute('href')
        salary = job.find_element(By.CLASS_NAME,'salary').text
        location = job.find_element(By.CLASS_NAME,'location').text
        
        json.append({'title':title,'link':link,'salary':salary,'location':location})

    return json