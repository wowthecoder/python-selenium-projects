from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome()
driver2 = webdriver.Chrome(options=chrome_options)

def parse_string(text):
    #Replace the following characters in the text
    special_characters = (
        ("%", "%25"),
        (" ", "%20"),
        (",", "%2C"),
        ("?", "%3F"),
        ("\n", "%0A"),
        ('\"', "%22"),
        ("<", "%3C"),
        (">", "%3E"),
        ("#", "%23"),
        ("|", "%7C"),
        ("&", "%26"),
        ("=", "%3D"),
        ("@", "%40"),
        ("#", "%23"),
        ("$", "%24"),
        ("^", "%5E"),
        ("`", "%60"),
        ("+", "%2B"),
        ("\'", "%27"),
        ("{", "%7B"),
        ("}", "%7D"),
        ("[", "%5B"),
        ("]", "%5D"),
        ("/", "%2F"),
        ("\\", "%5C"),
        (":", "%3A"),
        (";", "%3B")
    )

    for pair in special_characters:
        text = text.replace(*pair)

    return text

def selenium():
    text = "吃牛蛋喝鸡奶"
    text = parse_string(text)
    #source language auto detect, target language english
    link = f"https://translate.google.com/?sl=auto&tl=en&text={text}&op=translate"
    driver.get(link)
    driver2.get(link)

    copy_button = (By.CLASS_NAME, "VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.qiN4Vb.itOtF.IK3GNd")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(copy_button)).click()
    translated_text = pyperclip.paste()
    print("Using copy button:", translated_text)
    #driver.quit()
    
    translated_box = (By.CLASS_NAME, "zkZ4Kc.dHeVVb")
    trbox = WebDriverWait(driver2, 10).until(EC.presence_of_element_located(translated_box))
    translated_text2 = trbox.get_attribute("data-text")
    print("In headless mode by scraping:", translated_text2)

    driver2.quit()
    

main()
