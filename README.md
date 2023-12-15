**Program full name** : Student's Attendance Checking Program in OnlineClass Live Room <br><br>

 During the era when remote learning was just introduced due to COVID-19, EBS's online class platform couldn't sort students' names based on student ID, making it difficult to verify attendance. I created a program using BeautifulSoup for web crawling to sort names and compare them with the existing student ID list. Additionally, the program includes a function to detect students who haven't turned on their cameras.<br><br>

**Program function** : As automatic student attendance checking code in remote live class, this prints student's name who doesn't attend in remote classroom and who doesn't turn on their camera. <br>
**Operating environment**: Available in EBS online class live room (April 2022) <br>
**Development environmnet** : jupyter notebook, Python 3.7.2 <br>
**Note**: You must copy the html body of the online class live room and assign it to the 'html' variable. And the original list of all members must be assigned to the 'namelist' list variable.<br>
**Others**: I tried to use the requests module, but it still failed ; regarded as authority problem.

프로그램 명 : 온라인클래스 자동 출석 확인 코드
코드 기능 : 원격라이브수업 자동출석확인코드로, 현재 라이브 방에 참석한 사람과 카메라를 키지 않은 사람을 동시에 출력해줌.<br>
구동 환경 : EBS 온라인 클래스 라이브 방에서 사용 가능(2022년 4월 기준)<br>
개발 환경 : jupyter notebook, Python 3.7.2 <br>
참고 사항 : 온라인 클래스 라이브 방의 html body를 복사해서, 'html' 변수에 할당해야됨. 그리고 'namelist' 리스트 변수엔 출석부 리스트(모든 멤버들 목록)를 할당해야 됨.<br>
     기타 : requests 모듈을 사용하려 했으나 실패 ; 접근 권한 문제로 여겨짐.
