이 폴더는 선택 사항입니다. 이미지가 없어도 페이지는 정상 동작합니다.
(프로젝트 카드는 이모지+그라데이션으로 표시됩니다.)

[프로필 사진]
- 파일명: profile.jpg  (또는 profile.png 로 바꾸려면 index.html의 <img src="images/profile.jpg"> 수정)
- 소개 섹션에 자동으로 들어갑니다. 없으면 🧑‍💻 아이콘이 표시됩니다.
- 권장: 세로형(약 4:5 비율), 800px 이상.

[프로젝트 스크린샷을 넣고 싶다면]
현재 디자인은 스크린샷 없이도 깔끔하게 보이도록 만들었습니다.
스크린샷을 추가하고 싶으면, index.html의 devProjects 배열 각 항목에
  shot: "images/jooyou.png"
같은 필드를 추가한 뒤 모달 렌더링 부분에 <img>를 끼워 넣으면 됩니다.
원하시면 이 작업도 도와드릴 수 있습니다.

추천 스크린샷 파일명 예시:
  jooyou.png      (차계부 앱)
  edubridge.png   (시선추적 학습 앱)
  dojae.png       (도제 출결 앱)
  jari.png        (자리배치/호출)
  formatguard.png (문서 호환성)
  traffic.png     (교통사고 위험도 대시보드)
  ghasquiz.png    (학교 퀴즈)
  dojae-info.png  (앱 소개 홈페이지)
