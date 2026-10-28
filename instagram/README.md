# 인스타그램 게시물 소스

계정: **전경준의 슬기로운 개발생활**

업로드용 이미지와, 그 이미지를 만든 스크립트를 함께 둡니다.
문구를 고치고 싶으면 PNG를 다시 그리지 말고 `src/` 의 스크립트를 고쳐서 다시 뽑으세요.

```
instagram/
├── slides-01-intro/     # 1번 게시물 — 자기소개 캐러셀 9장 (1080×1080)
└── src/
    └── gen-01-intro.py  # 위 9장을 만드는 스크립트
```

## 1번 게시물 — 자기소개 (9장)

| 순서 | 파일 | 내용 |
| --- | --- | --- |
| 1 | `01-hello.png` | 인사 — 다양한 취미를 가진 학생이자 개발자 |
| 2 | `02-projects.png` | 프로젝트 23개, 그중 5개는 지금도 사용 중 |
| 3 | `03-dojae.png` | Dojae — 출결·소통 통합 앱 |
| 4 | `04-jari.png` | Jari — 실시간 자리배치·호출 |
| 5 | `05-rhythm.png` | Rhythm Lab V — 4키 웹 리듬게임 |
| 6 | `06-duru.png` | 두루문서 — HWP 문서 편집기 |
| 7 | `07-awards.png` | 장관상 · 특별상 · 장학금 |
| 8 | `08-interests.png` | 관심사와 게임 |
| 9 | `09-follow.png` | 계정 소개 — 결과물 / 제작 과정 / 패치노트 |

## 다시 만들기

Python 과 Chrome 만 있으면 됩니다. 별도 설치 없음.

```bash
cd instagram/src
python3 gen-01-intro.py                     # HTML 9개 생성
for f in *.html; do
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1080 \
    --virtual-time-budget=6000 \
    --screenshot="${f%.html}.png" "file://$PWD/$f"
done
mv *.png ../slides-01-intro/ && rm -f *.html
```

- 크기는 **1080×1080** 고정입니다. 인스타 캐러셀은 첫 장의 비율로 전체가 맞춰지니 장마다 크기를 섞지 마세요.
- 한글 폰트는 Noto Sans KR 을 웹폰트로 불러옵니다. 렌더링할 때 인터넷 연결이 필요합니다.
- 디자인 토큰(네온 색, 성운 배경, 코드 레인)은 포트폴리오 `common.css` 의 히어로와 같은 값입니다. 사이트 색을 바꾸면 여기도 같이 맞춰주세요.

## 올리기 전 확인

- [ ] 프로필 **웹사이트 칸**에 포트폴리오 주소 — 캡션 안의 링크는 인스타에서 눌리지 않습니다
- [ ] 파일명 순서(01→09)대로 업로드
- [ ] 수치가 최신인지 (`02` 의 프로젝트 개수, `03` 의 배포 횟수·출석률)
