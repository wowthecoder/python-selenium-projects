from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

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

def main():
    text = """
    Dos hogares, ambos iguales en dignidad,
En la bella Verona, donde ponemos nuestro escenario,
De la antigua ruptura de rencor a un nuevo motín,
Donde la sangre civil hace las manos civiles sucias.
De los lomos fatales de estos dos enemigos
Un par de amantes estrellados se quitan la vida;
Cuyos derrocamientos lamentables desventurados
Haz con su muerte, entierra la contienda de sus padres.
El terrible pasaje de su amor marcado por la muerte,
Y la continuación de la ira de sus padres,
Que, salvo el fin de sus hijos, nada podría eliminar,
Es ahora el tráfico de dos horas de nuestro escenario;
El que si asistes con oídos pacientes,
Lo que aquí faltará, nuestro trabajo se esforzará por enmendar."""
    text = parse_string(text)
    #source language auto detect, target language english
    link = f"https://translate.google.com/?sl=auto&tl=en&text={text}&op=translate"
    driver.get(link)
    
    translated_box = (By.CLASS_NAME, "zkZ4Kc.dHeVVb")
    trbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located(translated_box))
    translated_text = trbox.get_attribute("data-text")
    print(translated_text)
    driver.quit()

main()
