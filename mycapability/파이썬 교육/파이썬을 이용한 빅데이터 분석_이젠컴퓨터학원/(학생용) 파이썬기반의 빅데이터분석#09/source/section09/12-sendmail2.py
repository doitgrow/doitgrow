# -*- coding:utf-8 -*-

# 헬퍼에 정의된 함수 참조
from helper import sendmail

from_addr = "직접설정하세요"                   # 보내는 사람 주소
to_addr = "직접설정하세요"                     # 받는 사람 주소
subject = '테스트 12345'                       # 메일제목
files = ["mail/hello.txt", "mail/world.txt"]   # 첨부파일

# 메일 본문 설정 -> HTML코드 형식
content = """<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>"""

# helper 모듈 안에 있는 함수 호출
# -> 첨부파일이 없는 경우 마지막 파라미터 생략 가능
sendmail(from_addr, to_addr, subject, content, files)


