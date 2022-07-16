import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://WWW.shutterstock.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#8b0000", "#FF0000"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이예진")
write("description", "진영중학교 3학년입니다.")
write("button", "사진사이트")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "반과 학번": "8반 23번",
  "잘하는 과목": "과학,미술,역사",
  "좋아하는 책": "서부전선 이상없다,무기여 잘있거라",
  "좋아하는 동물": "푸들 모스,상어,고양이"
}
information(informations)
