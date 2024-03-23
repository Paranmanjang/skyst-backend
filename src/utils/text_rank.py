from krwordrank.word import KRWordRank
import re
from konlpy.tag import Okt


def split_noun_sentences(text):
    okt = Okt()
    sentences = text.replace(". ", ".")
    sentences = re.sub(r'([^\n\s\.\?!]+[^\n\.\?!]*[\.\?!])',
                       r'\1\n', sentences).strip().split("\n")

    result = []
    for sentence in sentences:
        if len(sentence) == 0:
            continue
        sentence_pos = okt.pos(sentence, stem=True)
        nouns = [word for word, pos in sentence_pos if pos ==
                 'Noun' and len(word) > 1]
        if len(nouns) < 2:
            continue
        result.append(' '.join(nouns) + '.')

    return result


text = "서울 지진 피해에 대한 데이터 분석을 위해서는 어떤 종류의 데이터를 사용해야 할지 먼저 생각해보아야 합니다. 예를 들어, 지진 발생 시간, 지진 규모, 지진 발생 지역, 피해 규모 등의 정보가 필요할 것입니다. 서울 지진 피해 분석 예시: 서울 지역에서 최근 몇 년간 발생한 지진 데이터를 수집하여 지진 발생 건수, 지진 규모, 지진 발생 지역 등의 정보를 파악할 수 있습니다. 이를 바탕으로 서울 지역에서 지진 발생이 가장 많은 지역, 지진 규모와 피해 규모 간의 상관 관계, 지진 발생 시간대 등을 분석할 수 있습니다. 또한, 특정 지역에서의 지진 발생 시 피해 규모가 어떻게 나타나는지 분석하여 지진 대비 대응 전략을 마련할 수 있습니다. 서울 지진에 대한 데이터는 국가지진정보센터에서 제공하는 '국내 지진 정보 시스템'에서 확인할 수 있습니다. 이 시스템에서는 지난 1년간의 국내 지진 정보를 확인할 수 있으며, 서울 지역에서 발생한 지진 정보도 포함되어 있습니다. 이를 바탕으로 데이터를 수집하고 분석할 수 있습니다."


def extract_keyword(text, rank_num=3):
    min_count = 1   # 단어의 최소 출현 빈도수
    max_length = 10  # 단어의 최대 길이
    wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)
    beta = 0.85
    max_iter = 20
    texts = split_noun_sentences(text)
    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)
    result = []
    for word, r in sorted(keywords.items(), key=lambda x: x[1], reverse=True):
        if rank_num == 0:
            break
        if '.' in word:
            result.append(word[:-1])
        else:
            result.append(word)
        rank_num -= 1
    print('+'.join(result))


extract_keyword(text, 3)
