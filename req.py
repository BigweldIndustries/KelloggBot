import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import random
import time
import os
import functools
from faker import Faker
from concurrent.futures import ThreadPoolExecutor
from webdriver_manager.chrome import ChromeDriverManager
os.environ['WDM_LOG_LEVEL'] = '0'
import speech_recognition as sr
from pydub import AudioSegment
filename = '1.mp3'
r = sr.Recognizer()
executor = ThreadPoolExecutor(max_workers=500)
processes = []
fake = Faker()
print = functools.partial(print, flush=True)
options = Options()
count = 0

urls = ['https://jobs.kellogg.com/job/Lancaster-Permanent-Production-Associate-Lancaster-PA-17601/817684800/#',
        'https://jobs.kellogg.com/job/Omaha-Permanent-Production-Associate-Omaha-NE-68103/817685900/z',
        'https://jobs.kellogg.com/job/Battle-Creek-Permanent-Production-Associate-Battle-Creek-MI-49014/817685300/',
        'https://jobs.kellogg.com/job/Memphis-Permanent-Production-Associate-Memphis-TN-38114/817685700/'
        ]


data2 = {
    'resume': '//*[@id="49:_file"]',
    'addy': '//*[@id="69:_txtFld"]',
    'city': '//*[@id="73:_txtFld"]',
    'zip': '//*[@id="81:_txtFld"]',
    'job': '//*[@id="101:_txtFld"]',
    'salary': '//*[@id="172:_txtFld"]',
    'country': '//*[@id="195:_select"]'
}
data = {
    'email': '//*[@id="fbclc_userName"]',
    'email-retype': '//*[@id="fbclc_emailConf"]',
    'pass': '//*[@id="fbclc_pwd"]',
    'pass-retype': '//*[@id="fbclc_pwdConf"]',
    'first_name': '//*[@id="fbclc_fName"]',
    'last_name': '//*[@id="fbclc_lName"]',
    'pn': '//*[@id="fbclc_phoneNumber"]',

}


cities = {'Lancaster':  'Pennsylvania',
          'Omaha':  'Nebraska',
          'Battle Creek':   'Michigan',
          'Memphis':    'Tennessee',
          }

zip_codes = {
    'Lancaster':    ['17573', '17601', '17602', '17605', '17606', '17699'],
    'Omaha':    ['68104', '68105', '68106', '68124', '68127', '68134'],
    'Battle Creek': ['49014', '49015', '49016', '49017', '49018', '49037'],
    'Memphis':  ['38116', '38118', '38122', '38127', '38134', '38103'],
}

def audioToText(mp3Path):
    dst = "2.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(mp3Path)
    sound.export(dst, format="wav")

    with sr.AudioFile(dst) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            return(text)     
        except Exception as e:
            print(e)
            print('Sorry.. run again...')

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)

def random_email(name=None):
    if name == None:
        name = fake.name()
    
    emailData = [['0', 'gmail.com', '17.74'],
    ['2', 'yahoo.com', '17.34'],
    ['3', 'hotmail.com', '15.53'],
    ['4', 'aol.com', '3.2'],
    ['5', 'hotmail.co.uk', '1.27'],
    ['6', 'hotmail.fr', '1.24'],
    ['7', 'msn.com', '1.09'],
    ['8', 'yahoo.fr', '0.98'],
    ['9', 'wanadoo.fr', '0.9'],
    ['10', 'orange.fr', '0.83'],
    ['11', 'comcast.net', '0.76'],
    ['12', 'yahoo.co.uk', '0.73'],
    ['13', 'yahoo.com.br', '0.69'],
    ['14', 'yahoo.co.in', '0.6'],
    ['15', 'live.com', '0.56'],
    ['16', 'rediffmail.com', '0.51'],
    ['17', 'free.fr', '0.51'],
    ['18', 'gmx.de', '0.44'],
    ['19', 'web.de', '0.43'],
    ['20', 'yandex.ru', '0.42'],
    ['21', 'ymail.com', '0.41'],
    ['22', 'libero.it', '0.38'],
    ['23', 'outlook.com', '0.38'],
    ['24', 'uol.com.br', '0.34'],
    ['25', 'bol.com.br', '0.33'],
    ['26', 'mail.ru', '0.32'],
    ['27', 'cox.net', '0.25'],
    ['28', 'hotmail.it', '0.25'],
    ['29', 'sbcglobal.net', '0.24'],
    ['30', 'sfr.fr', '0.23'],
    ['31', 'live.fr', '0.23'],
    ['32', 'verizon.net', '0.22'],
    ['33', 'live.co.uk', '0.21'],
    ['34', 'googlemail.com', '0.2'],
    ['35', 'yahoo.es', '0.2'],
    ['36', 'ig.com.br', '0.19'],
    ['37', 'live.nl', '0.19'],
    ['38', 'bigpond.com', '0.18'],
    ['39', 'terra.com.br', '0.17'],
    ['40', 'yahoo.it', '0.17'],
    ['41', 'neuf.fr', '0.17'],
    ['42', 'yahoo.de', '0.16'],
    ['43', 'alice.it', '0.16'],
    ['44', 'rocketmail.com', '0.15'],
    ['45', 'att.net', '0.15'],
    ['46', 'laposte.net', '0.15'],
    ['47', 'facebook.com', '0.15'],
    ['48', 'bellsouth.net', '0.15'],
    ['49', 'yahoo.in', '0.14'],
    ['50', 'hotmail.es', '0.13'],
    ['51', 'charter.net', '0.12'],
    ['52', 'yahoo.ca', '0.12'],
    ['53', 'yahoo.com.au', '0.12'],
    ['54', 'rambler.ru', '0.12'],
    ['55', 'hotmail.de', '0.11'],
    ['56', 'tiscali.it', '0.1'],
    ['57', 'shaw.ca', '0.1'],
    ['58', 'yahoo.co.jp', '0.1'],
    ['59', 'sky.com', '0.1'],
    ['60', 'earthlink.net', '0.09'],
    ['61', 'optonline.net', '0.09'],
    ['62', 'freenet.de', '0.09'],
    ['63', 't-online.de', '0.09'],
    ['64', 'aliceadsl.fr', '0.08'],
    ['65', 'virgilio.it', '0.08'],
    ['66', 'home.nl', '0.07'],
    ['67', 'qq.com', '0.07'],
    ['68', 'telenet.be', '0.07'],
    ['69', 'me.com', '0.07'],
    ['70', 'yahoo.com.ar', '0.07'],
    ['71', 'tiscali.co.uk', '0.07'],
    ['72', 'yahoo.com.mx', '0.07'],
    ['73', 'voila.fr', '0.06'],
    ['74', 'gmx.net', '0.06'],
    ['75', 'mail.com', '0.06'],
    ['76', 'planet.nl', '0.06'],
    ['77', 'tin.it', '0.06'],
    ['78', 'live.it', '0.06'],
    ['79', 'ntlworld.com', '0.06'],
    ['80', 'arcor.de', '0.06'],
    ['81', 'yahoo.co.id', '0.06'],
    ['82', 'frontiernet.net', '0.06'],
    ['83', 'hetnet.nl', '0.05'],
    ['84', 'live.com.au', '0.05'],
    ['85', 'yahoo.com.sg', '0.05'],
    ['86', 'zonnet.nl', '0.05'],
    ['87', 'club-internet.fr', '0.05'],
    ['88', 'juno.com', '0.05'],
    ['89', 'optusnet.com.au', '0.05'],
    ['90', 'blueyonder.co.uk', '0.05'],
    ['91', 'bluewin.ch', '0.05'],
    ['92', 'skynet.be', '0.05'],
    ['93', 'sympatico.ca', '0.05'],
    ['94', 'windstream.net', '0.05'],
    ['95', 'mac.com', '0.05'],
    ['96', 'centurytel.net', '0.05'],
    ['97', 'chello.nl', '0.04'],
    ['98', 'live.ca', '0.04'],
    ['99', 'aim.com', '0.04'],
    ['100', 'bigpond.net.au', '0.04']]

    mailGens = [lambda fn, ln, *names: fn + ln,
                lambda fn, ln, *names: fn + "." + ln,
                lambda fn, ln, *names: fn + "_" + ln,
                lambda fn, ln, *names: fn[0] + "." + ln,
                lambda fn, ln, *names: fn[0] + "_" + ln,
                lambda fn, ln, *names: fn + ln + str(int(1/random.random()**3)),
                lambda fn, ln, *names: fn + "." + ln + str(int(1/random.random()**3)),
                lambda fn, ln, *names: fn + "_" + ln + str(int(1/random.random()**3)),
                lambda fn, ln, *names: fn[0] + "." + ln + str(int(1/random.random()**3)),
                lambda fn, ln, *names: fn[0] + "_" + ln + str(int(1/random.random()**3)),]

    mailGenWeights = [1, 0.9, 0.95, 0.8, 0.7, 0.75, 0.7, 0.7, 0.6, 0.5]

    emailChoices = [float(line[2]) for line in emailData]

    return random.choices(mailGens, mailGenWeights)[0](*name.split(" ")).lower() + "@" + random.choices(emailData, emailChoices)[0][1]



def start_driver(rand_num):
    global options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #driver.set_window_size(1440, 900)
    driver.get(urls[rand_num])
    # driver.manage().timeouts().pageLoadTimeout(5, SECONDS)
    # time.sleep(10)
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element(By.XPATH,  
        '//*[@id="content"]/div/div[2]/div/div[1]/div[1]/div/div/button').click()
    driver.find_element(By.XPATH,  
        '//*[@id="applyOption-top-manual"]').click()
    driver.find_element(By.XPATH,  
        '//*[@id="page_content"]/div[2]/div/div/div[2]/div/div/div[2]/a').click()
    return driver

def generate_account(rand_num):
    # start driver
    try:
        driver = start_driver(rand_num)
    except Exception as e:
        print(f"Failed to start driver: {str(e)}")
        driver.close()

    # make fake account info and fill
    global count
    try:
        name = fake.name()
        first_name = name.split(" ")[0]
        last_name  = name.split(" ")[1]
        email = random_email(name)
        password = fake.password()
        for key in data.keys():
            match key:
                case 'email' | 'email-retype':
                    info = email
                case 'pass' | 'pass-retype':
                    info = password
                case 'first_name':
                    info = first_name
                case 'last_name':
                    info = last_name
                case 'pn':
                    info = fake.phone_number()

            driver.find_element(By.XPATH, data.get(key)).send_keys(info)
            
        time.sleep(random.randint(0, 2))
        select = Select(driver.find_element(By.ID, 'fbclc_ituCode'))
        select.select_by_value('US')
        select = Select(driver.find_element(By.ID, 'fbclc_country'))
        select.select_by_value('US')

        driver.find_element(By.XPATH, '//*[@id="dataPrivacyId"]').click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, '//*[@id="dlgButton_20:"]').click()
        time.sleep(2)

        googleClass = driver.find_elements(By.CLASS_NAME,  'recapBorderAccessible')[0]
        time.sleep(2)
        outeriframe = googleClass.find_element(By.TAG_NAME, 'iframe')
        time.sleep(1)
        outeriframe.click()
        time.sleep(2)
        allIframesLen = driver.find_elements(By.TAG_NAME, 'iframe')
        time.sleep(1)
        audioBtnFound = False
        audioBtnIndex = -1
        for index in range(len(allIframesLen)):
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME, 'iframe')[index]
            driver.switch_to.frame(iframe)
            driver.implicitly_wait(2)
            try:
                audioBtn = driver.find_element(By.ID, 'recaptcha-audio-button') or driver.find_element(By.ID, 'recaptcha-anchor')
                audioBtn.click()
                audioBtnFound = True
                audioBtnIndex = index
                break
            except Exception as e:
                pass
        if audioBtnFound:
            try:
                while True:
                    href = driver.find_element(By.ID, 'audio-source').get_attribute('src')
                    response = requests.get(href, stream=True)
                    saveFile(response,filename)
                    response = audioToText(filename)
                    print(response)
                    driver.switch_to.default_content()
                    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[audioBtnIndex]
                    driver.switch_to.frame(iframe)
                    inputbtn = driver.find_element(By.ID, 'audio-response')
                    inputbtn.send_keys(response)
                    inputbtn.send_keys(Keys.ENTER)
                    time.sleep(2)
                    errorMsg = driver.find_elements(By.CLASS_NAME,  'rc-audiochallenge-error-message')[0]
                    if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                        print("reCaptcha defeated!")
                        break
            except Exception as e:
                print(e)
                print('Oops, something happened. Check above this message for errors or check the chrome window to see if captcha locked you out...')
        else:
            print('Button not found. This should not happen.')


        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '//*[@id="fbclc_createAccountButton"]').click()

        time.sleep(1.5)

        print(f"Successfully made account for fake email {email}")
        fill_out_application_and_submit(driver, rand_num)
    except Exception as e:
        print(f"Failed to create account: {str(e)}")
        driver.close()

def fill_out_application_and_submit(driver, rand_num):
    global count
    try:
        driver.implicitly_wait(10)
        city = list(cities.keys())[rand_num]
        
        # fill out form parts of app
        driver.find_element(By.XPATH,  '//*[@id="109:topBar"]').click()
        driver.find_element(By.XPATH,  '//*[@id="260:topBar"]').click()

        zip_num = random.randint(0, 4)

        for key in data2.keys():

            match key:
                case 'resume':
                    driver.find_element(By.XPATH,  '//*[@id="48:_attach"]/div[6]').click()
                    info = os.getcwd()+"/src/resume.png"
                case 'addy':
                    info = fake.street_address()
                case 'city':
                    info = city
                case 'zip':
                    zipp = zip_codes[city]
                    info = zipp[zip_num]
                case 'job':
                    info = fake.job()
                case 'salary':
                    info = random.randint(15, 35)

            driver.find_element(By.XPATH,  data2.get(key)).send_keys(info)

        print(f"Successfully filled out app forms for {city}")

        # fill out dropdowns
        select = Select(driver.find_element(By.ID,  '154:_select'))
        select.select_by_visible_text('Yes')
        select = Select(driver.find_element(By.ID,  '195:_select'))
        select.select_by_visible_text('United States')

        select = Select(driver.find_element(By.ID,  '211:_select'))
        select.select_by_visible_text('Yes')
        select = Select(driver.find_element(By.ID,  '215:_select'))
        select.select_by_visible_text('No')
        select = Select(driver.find_element(By.ID,  '219:_select'))
        select.select_by_visible_text('No')
        select = Select(driver.find_element(By.ID,  '223:_select'))
        select.select_by_visible_text('No')
        select = Select(driver.find_element(By.ID,  '227:_select'))
        select.select_by_visible_text('No')
        select = Select(driver.find_element(By.ID,  '231:_select'))
        select.select_by_visible_text('Yes')
        select = Select(driver.find_element(By.ID,  '223:_select'))
        select.select_by_visible_text('No')

        time.sleep(1)

        select = Select(driver.find_element(By.ID,  '235:_select'))
        gender = random.choice(['Male', 'Female', 'Other'])
        select.select_by_visible_text(gender)

        driver.find_element(By.XPATH,  '//label[text()="350 LBS"]').click()
        driver.find_element(By.XPATH,  '//label[text()="800 LBS"]').click()
        els = driver.find_elements_by_xpath('//label[text()="Yes"]')
        for el in els:
            el.click()

        time.sleep(5)
        driver.find_element(By.XPATH,  '//*[@id="261:_submitBtn"]').click()
        print(f"Successfully submitted application")
        count += 1
        print(f"Jobs requested: {str(count)}")
        driver.close()
    except Exception as e:
        print(f"Failed to fill out app and submit: {str(e)}")
        driver.close()

def main():
    global processes
    global executor

    speed = int(input("How many seconds between new windows?: "))
    while True:
        rand_num = random.randint(0, 3)
        processes.append(executor.submit(generate_account, rand_num))
        print("One operation started")
        time.sleep(speed)

if __name__ == '__main__':
    main()
    sys.exit()


