from driver import *

async def indeed_query(driver,keyword):
    driver.get(f'https://in.indeed.com/jobs?q={keyword}')
    jobs = driver.find_element(By.CLASS_NAME, "jobsearch-ResultsList").find_elements(By.TAG_NAME,"li")
    json = []
    for job in jobs:
        # check if its a valid obtained job and then scrape information from it
        job_text = job.text.split('\n') 
        if len(job_text) > 1:
            title = job.find_element(By.CLASS_NAME, 'jobTitle').text

            # Sometimes salary div exists, but sometimes it doesnt, so we have to use exception
            try:
                salary = job.find_element(By.CLASS_NAME,'salary-snippet-container').text
            except NoSuchElementException:
                salary = 0
                
            link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')

            json.append({'title':title,'salary':salary,'link':link})
    
    return json
