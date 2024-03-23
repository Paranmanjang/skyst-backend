from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# ChromeDriverManager 라인은 제거
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_title_and_content_selenium(url):
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # 직접 지정한 ChromeDriver 경로
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

        driver.get(url)
        time.sleep(5)

        title = driver.title
        content_elements = driver.find_elements(By.TAG_NAME, 'p')
        content = ' '.join([element.text for element in content_elements])

        print("성공적으로 웹 페이지를 가져왔습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        if driver is not None:
            driver.quit()
    return title, content