import requests
from bs4 import BeautifulSoup

class Conversation:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"
    
def get_subjects():
    subjects = []

    req = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.findAll('div', {"class": "thrv_wrapper thrv_text_element"})
    for div in divs:
        links = div.findAll('a')

        for link in links:
            subject = link.text
            subjects.append(subject)

    return subjects

subjects = get_subjects()
print('총', len(subjects), '개의 주제를 찾았습니다.')
print(subjects)

conversation = []
i = 1

for sub in subjecst:
    print('(', i, '/', len(subjects), ')', sub)

    req = requests.get('https://basicenglishspeaking.com/' + sub)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    qnas = soup.findAll('div', {"class": "sc_player_container1"})

    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling
        else:
            a = qna.next_sibling
            c = Conversation(q, a)
            conversations.append(c)

    i = i+1

print('총 ', len(conversations), '개의 대화를 찾았습니다.')

for c in conversation:
    print(str(c))

    
                       
