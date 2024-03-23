from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_title_and_content_selenium(url):
    driver = None
    try:
        # Selenium 설정: 머리 없는(headless) 브라우저로 설정
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # WebDriver 경로 설정
        service = Service(ChromeDriverManager().install())

        # WebDriver 초기화
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 주어진 URL로 이동
        driver.get(url)

        # 페이지가 완전히 로드될 때까지 기다립니다.
        time.sleep(5)  # 실제 상황에 따라 대기 시간을 조절해야 할 수 있습니다.

        # 페이지의 제목 가져오기
        title = driver.title

        # BeautifulSoup를 사용하지 않고 Selenium으로 내용 추출
        content_elements = driver.find_elements(By.TAG_NAME, 'p')
        content = ' '.join([element.text for element in content_elements])

        print("성공적으로 웹 페이지를 가져왔습니다.")

        driver.quit()  # 브라우저 닫기

        return title, content

    except Exception as e:
        print(f"오류 발생: {e}")
        driver.quit()