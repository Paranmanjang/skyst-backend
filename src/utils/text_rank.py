from summa import keywords
from googletrans import Translator


def extract_keyword():
    text = """[앵커]

의대증원 정책에 반대하는 다수의 전공의와 의대생들이 집단행동을 이어가고 있지만, 의료 현장을 지키려는 소수의 의사와 학생들도 있습니다.

이들이 오늘(23일) '집단 행동 강요'를 멈춰달라고 호소했습니다.

박경준 기잡니다.

[리포트]

의대 증원 반대를 위한 집단 행동에 반대하는 이른바 '다른 생각을 가진 의대생과 전공의'라는 단체의 익명 SNS 계정.

긴급 성명이 게재됐습니다.

이들은 "전체주의적인 조리돌림과 폭력적 강요를 중단하라"며 "일부 학교에서 복귀 희망자나 수업 참여 학생을 대상으로 대면 사과와 소명을 요구하고 있다"고 전했습니다.

그러면서 이런 일은 "단체행동 동참을 협박하는 것과 다르지 않다"고 비판했습니다.

이어 "단체 행동에 참여하지 않으면 '반역자'로 여기고 색출만 요구한다"고 꼬집었습니다.

앞서 정부는 협박성 보복에 대해 엄정 대응을 예고한 바 있습니다.

[한덕수/국무총리/지난 8일 : "사람의 생명을 구하는 의료인이라면 해서는 안 되는 언행입니다. 정부는 이런 행태를 절대 좌시하지 않겠습니다."]

경찰 역시, 집단 행동에 동참하지 않았던 의대생과 공보의 명단이 인터넷 커뮤니티에 게시된 것과 관련해 강제 수사를 벌이고 있습니다."""

    # 한글을 영어로 번역
    translator = Translator()
    english_text = translator.translate(text, src='ko', dest='en').text

    # 번역된 텍스트에서 키워드 추출
    english_keywords = keywords.keywords(english_text, ratio=0.5, words=3)

    # 영어 키워드를 한글로 다시 번역하여 출력
    lst = []
    for keyword in english_keywords.split('\n'):
        print(keyword)
        keyword = translator.translate(keyword, src='en', dest='ko').text
        lst.append(keyword)
    result = '+'.join(lst)
    return result


print(extract_keyword())