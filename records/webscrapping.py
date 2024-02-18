from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class Scrapper:
    date = datetime.now() - timedelta(weeks = 4)

    def __init__(self, url, d_path = None, headless = False):
        profile = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        
        if d_path: 
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.download.dir", d_path)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

        if headless: options.add_argument("-headless")
        
        options.profile = profile
        self.driver = webdriver.Firefox(options = options)
        self.wdwait = WebDriverWait(self.driver, timeout=20)
        self.driver.get(url)

    def write(self, byId = None, byName = None, byXpath = None, value = None, typeFormat = None):
        if byId:
            input = self.driver.find_element(by = By.ID, value = byId)
        elif byName:
            input = self.driver.find_element(by = By.NAME, value = byName)
        elif byXpath:
            input = self.driver.find_element(by = By.XPATH, value = byXpath)

        if typeFormat == 'datetime':
            input.send_keys(self.date.strftime(value))
        else:
            input.send_keys(value)

    def click(self, byId = None, byName = None, byXpath = None):
        
        self.wait_clickable(byId = byId, byName = byName, byXpath = byXpath)
        doClick = True
        if byId:
            button = self.driver.find_element(by = By.ID, value = byId)
        elif byName:
            button = self.driver.find_element(by = By.NAME, value = byName)
        elif byXpath:
            button = self.driver.find_element(by = By.XPATH, value = byXpath)
        else:
            doClick = False
        
        if doClick: button.click()

    def goto(self, url):
        self.driver.get(url)

    def wait_precense(self, byId = None, byName = None, byXpath = None):
        if byId:
            self.wdwait.until(EC.presence_of_element_located((By.ID, byId)))
        if byName:
            self.wdwait.until(EC.presence_of_element_located((By.NAME, byName)))
        if byXpath:
            self.wdwait.until(EC.presence_of_element_located((By.XPATH, byXpath)))

    def wait_clickable(self, byId = None, byName = None, byXpath = None):
        if byId:
            self.wdwait.until(EC.element_to_be_clickable((By.ID, byId)))
        elif byName:
            self.wdwait.until(EC.element_to_be_clickable((By.NAME, byName)))
        elif byXpath:
            self.wdwait.until(EC.element_to_be_clickable((By.XPATH, byXpath)))

    def wait_visibility(self, byId = None, byName = None, byXpath = None):
        if byId:
            self.wdwait.until(EC.visibility_of_element_located((By.ID, byId)))
        elif byName:
            self.wdwait.until(EC.visibility_of_element_located((By.NAME, byName)))
        elif byXpath:
            self.wdwait.until(EC.visibility_of_element_located((By.XPATH, byXpath)))

    def wait_invisibility(self, byId = None, byName = None, byXpath = None, byClass = None):
        if byId:
            self.wdwait.until(EC.invisibility_of_element_located((By.ID, byXpath)))
        elif byName:
            self.wdwait.until(EC.invisibility_of_element_located((By.NAME, byName)))
        elif byXpath:
            self.wdwait.until(EC.invisibility_of_element_located((By.XPATH, byXpath)))
        elif byClass:
            self.wdwait.until(EC.invisibility_of_element_located((By.CLASS_NAME, byClass)))

    def wait(self, time):
        sleep(time)

    def close(self):
        self.driver.quit()

    def event(self, action, id, name, xpath, value):
        if action == 'wait':
            self.wait(int(value))
        elif action == 'click':
            self.click(byId = id if id != "None" else None, 
                       byName = name if name != "None" else None, 
                       byXpath = xpath if xpath != "None" else None)
        elif action == 'write':
            self.write(byId = id if id != "None" else None, 
                       byName = name if name != "None" else None, 
                       byXpath = xpath if xpath != "None" else None, 
                       value = value)
            
        elif action == 'format_datetime':
            self.write(byId = id if id != "None" else None, 
                       byName = name if name != "None" else None, 
                       byXpath = xpath if xpath != "None" else None, 
                       value = value,
                       typeFormat = 'datetime')

    def eventList(self, QS, optionalDate = None):
        if optionalDate: self.date = optionalDate
        for ev in QS:
            exec(f"""self.event(action = '{ev.ad_type.at_name}', 
                                id = '{ev.ad_sc_id}', 
                                name = '{ev.ad_sc_name}', 
                                xpath = '{ev.ad_sc_xp}', 
                                value = '{ev.ad_sc_val}')""")