import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_webpage_content(url):
    # Setup WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Replace the URL below with the webpage you're interested in
    driver.get(url)
    

    # Wait a bit for the page to load
    time.sleep(2)

    # Get the title of the webpage
    title = driver.title

    content = ""  # Initialize all_text as an empty string


    # first method
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    content = '\n'.join([paragraph.text for paragraph in paragraphs if paragraph.text.strip() != ""])

    # second method
    if not content:
        paragraphs = driver.find_elements(By.TAG_NAME, "article")
        content = '\n'.join([paragraph.text for paragraph in paragraphs if paragraph.text.strip() != ""])

    # third method: naver blog
    if not content:
        m_url = "https://m." + url.replace("https://","") 
        driver.get(m_url)
        time.sleep(2)
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        content = '\n'.join([paragraph.text for paragraph in paragraphs if paragraph.text.strip() != ""])

    # Close the WebDriver
    driver.quit()

    return title, content
