
from PIL import Image
from selenium import webdriver
import preprocessing
import captcha_predict
shot_path = 'shot.png'
username = '15905305'
password = '123456'

login_url = 'http://124.160.107.92:9090/Index.aspx'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(login_url)
browser.find_element_by_id('UserId').send_keys(username)
browser.find_element_by_id('Pwd').send_keys(password)

imgsrc = browser.find_element_by_id("imgIdentifyingCode").get_attribute('src')

browser.get_screenshot_as_file(shot_path)
location = browser.find_element_by_id('imgIdentifyingCode').location
size = browser.find_element_by_id('imgIdentifyingCode').size
left = location['x']
top = location['y']
right = location['x'] +size['width']
bottom = location['y'] +size['height']
img = Image.open(shot_path).crop((left,top,right,bottom))
pro_img = preprocessing.convert2gray(img)
pro_img = preprocessing.binarizing(pro_img,145)
pro_img = pro_img.resize((80,24), Image.NEAREST)
pro_img.save('sample/predict/1.jpg')
result = captcha_predict.main()
browser.find_element_by_id('txtIdentifyingCode').send_keys(result)
browser.find_element_by_id('btnLogin').click()
