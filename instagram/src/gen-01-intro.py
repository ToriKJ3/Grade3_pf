# -*- coding: utf-8 -*-
"""인스타 첫 게시물 캐러셀 9장 — 포트폴리오의 네온/우주 스타일, 1080x1080"""
import io, os, random, html

OUT = os.path.dirname(os.path.abspath(__file__))   # instagram/src 에 HTML 을 만든 뒤 PNG 로 렌더한다
random.seed(11)

CODE_POOL = [
    "export function detectEncoding(bytes)", "const JUDGES=[{w:0.042,acc:1.00}]",
    "await FirebaseFirestore.instance", "ctrlId('%hlk')",
    "onSnapshot(ref,(snap)=>render(snap))", "const t=actx.currentTime",
    "setState(()=>_total+=liters)", "git commit -m \"feat: ship it\"",
    "npm run dist:mac && dist:win", "await speak(name, 'supertone')",
    "cleanChart(raw).sort((a,b)=>a.t-b.t)", "writer.hwpx(doc).toBlob()",
]

def rain(cols=15):
    out = []
    for i in range(cols):
        left = i * (1080 / cols) + random.uniform(-10, 10)
        top = random.uniform(-380, 240)
        op = random.uniform(0.10, 0.28)
        txt = "".join(random.choice(CODE_POOL).replace(" ", "") for _ in range(2))[:random.randint(26, 46)]
        hue = random.choice(["#34d399", "#5eead4", "#a78bfa"])
        out.append(f'<div class="rc" style="left:{left:.0f}px;top:{top:.0f}px;color:{hue};opacity:{op:.2f}">'
                   + "<br>".join(html.escape(c) for c in txt) + "</div>")
    return "".join(out)

BASE = """<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1080px;overflow:hidden;background:#03100c;
 font-family:'Noto Sans KR','Apple SD Gothic Neo',sans-serif;color:#e9fff7}
.stage{position:relative;width:1080px;height:1080px;overflow:hidden}
.neb{position:absolute;inset:-20%;z-index:0;filter:blur(6px);background:
  radial-gradient(40% 36% at 20% 26%, rgba(16,185,129,.34), transparent 70%),
  radial-gradient(36% 32% at 80% 20%, rgba(45,212,191,.24), transparent 70%),
  radial-gradient(44% 40% at 64% 84%, rgba(139,92,246,.26), transparent 72%)}
.rain{position:absolute;inset:0;z-index:1}
.rc{position:absolute;font:600 15px/1.18 ui-monospace,Menlo,monospace;letter-spacing:.04em;white-space:nowrap}
.stars{position:absolute;inset:0;z-index:1;background-image:
  radial-gradient(1.4px 1.4px at 60px 90px, rgba(214,255,240,.5), transparent),
  radial-gradient(1.2px 1.2px at 300px 220px, rgba(110,231,183,.4), transparent),
  radial-gradient(1.6px 1.6px at 520px 390px, rgba(230,255,248,.42), transparent),
  radial-gradient(1.2px 1.2px at 760px 140px, rgba(94,234,212,.34), transparent),
  radial-gradient(1.3px 1.3px at 180px 460px, rgba(167,139,250,.36), transparent);
 background-size:540px 520px}
.veil{position:absolute;inset:0;z-index:2;background:
  radial-gradient(52% 46% at 50% 48%, rgba(2,12,9,.80) 0%, rgba(2,12,9,.42) 52%, transparent 80%),
  linear-gradient(180deg, rgba(3,16,12,.92) 0%, transparent 22%, transparent 70%, rgba(3,16,12,.96) 100%)}
.wrap{position:relative;z-index:3;height:100%;display:flex;flex-direction:column;
 justify-content:center;padding:92px 88px 150px}
.eyebrow{font:700 23px ui-monospace,Menlo,monospace;letter-spacing:.2em;color:#6ee7b7;
 text-transform:uppercase;margin-bottom:28px}
.eyebrow b{opacity:.55}
h1{font-size:80px;font-weight:900;line-height:1.24;letter-spacing:-.035em;
 text-shadow:0 0 34px rgba(94,234,212,.42),0 0 80px rgba(16,185,129,.26)}
h2{font-size:60px;font-weight:900;line-height:1.26;letter-spacing:-.03em;
 text-shadow:0 0 30px rgba(94,234,212,.36)}
.grad{background:linear-gradient(100deg,#6ee7b7 0%,#5eead4 44%,#a78bfa 100%);
 -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.amber{color:#fbbf24;text-shadow:0 0 30px rgba(245,158,11,.5)}
p.lead{font-size:31px;line-height:1.66;color:#c9efe1;margin-top:26px}
.foot{position:absolute;left:88px;right:88px;bottom:56px;z-index:3;display:flex;
 justify-content:space-between;align-items:center;font-size:22px;color:#7fb8a4;font-weight:500}
.foot .hand{color:#a7f3d0;font-weight:700}
.pill{display:inline-flex;align-items:center;gap:12px;padding:12px 26px;border-radius:50px;
 background:rgba(16,185,129,.13);border:1px solid rgba(94,234,212,.4);
 font-size:25px;font-weight:700;color:#a7f3d0}
.dot{width:11px;height:11px;border-radius:50%;background:#34d399;box-shadow:0 0 12px #34d399}
.card{background:rgba(6,24,19,.76);border:1px solid rgba(94,234,212,.24);border-radius:22px;
 padding:28px 32px}
.card .v{font-size:34px;font-weight:700;line-height:1.36}
.card .s{font-size:23px;color:#9fd8c6;margin-top:8px;line-height:1.5}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px}
.stat{background:rgba(6,24,19,.72);border:1px solid rgba(94,234,212,.24);border-radius:22px;
 padding:30px 14px;text-align:center}
.stat .n{font-size:66px;font-weight:900;line-height:1;
 background:linear-gradient(100deg,#6ee7b7,#5eead4);-webkit-background-clip:text;
 background-clip:text;-webkit-text-fill-color:transparent}
.stat .l{font-size:22px;color:#9fd8c6;margin-top:11px;font-weight:600}
/* 프로젝트 공통 */
.pname{display:flex;align-items:baseline;gap:20px;flex-wrap:wrap}
.pname .en{font-size:74px;font-weight:900;letter-spacing:-.035em;
 background:linear-gradient(100deg,#6ee7b7,#5eead4 48%,#a78bfa);
 -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.pname .live{font:700 20px ui-monospace,Menlo,monospace;letter-spacing:.14em;color:#34d399;
 border:1px solid rgba(52,211,153,.5);border-radius:50px;padding:7px 18px;
 box-shadow:0 0 16px rgba(52,211,153,.3)}
.psub{font-size:35px;font-weight:700;color:#e9fff7;margin-top:10px}
.pwhy{font-size:28px;line-height:1.62;color:#9fd8c6;margin-top:20px}
.points{margin-top:34px;display:flex;flex-direction:column;gap:17px}
.point{display:flex;gap:18px;align-items:flex-start;font-size:29px;font-weight:600;line-height:1.46}
.point i{flex:none;width:11px;height:11px;border-radius:50%;margin-top:14px;
 background:#5eead4;box-shadow:0 0 12px rgba(94,234,212,.75)}
.tags{display:flex;flex-wrap:wrap;gap:13px;margin-top:34px}
.tag{padding:12px 24px;border-radius:50px;background:rgba(6,24,19,.74);
 border:1px solid rgba(94,234,212,.26);font-size:24px;font-weight:600;color:#cdeee0}
.tag.g{border-color:rgba(167,139,250,.34);color:#d6cafd}
/* 수상 */
.awards{display:flex;flex-direction:column;gap:20px;margin-top:40px}
.aw{display:flex;gap:24px;align-items:center;background:rgba(6,24,19,.76);
 border:1px solid rgba(94,234,212,.22);border-radius:22px;padding:26px 30px}
.aw.hi{border-color:rgba(245,158,11,.46);background:rgba(36,25,6,.6)}
.aw .ic{font-size:44px;flex:none}
.aw .t{font-size:32px;font-weight:700;line-height:1.34}
.aw .d{font-size:23px;color:#9fd8c6;margin-top:6px}
.aw.hi .t{color:#fde68a}
.ghead{font:700 22px ui-monospace,Menlo,monospace;letter-spacing:.16em;color:#a78bfa;
 margin:34px 0 14px}
</style></head><body><div class="stage">
<div class="neb"></div><div class="stars"></div><div class="rain">__RAIN__</div><div class="veil"></div>
<div class="wrap">__BODY__</div>__FOOT__</div></body></html>"""

def foot(right="SWIPE →"):
    return f'<div class="foot"><span class="hand">전경준의 슬기로운 개발생활</span><span>{right}</span></div>'

S = []

# 1 ─ 인사
S.append(("01-hello", """
<div class="eyebrow"><b>❯</b> hello</div>
<h1>안녕하세요,<br><span class="grad">전경준</span>입니다</h1>
<p class="lead">다양한 취미를 가진 <b style="color:#e9fff7">학생이자 개발자</b>입니다.<br>
불편한 걸 발견하면, 일단 만들어 봅니다.</p>
""", foot()))

# 2 ─ 진행한 프로젝트
S.append(("02-projects", """
<div class="eyebrow"><b>❯</b> projects</div>
<h2>개발 폴더에<br>쌓인 것들</h2>
<div class="stats" style="grid-template-columns:1fr 1fr">
 <div class="stat"><div class="n">23</div><div class="l">만든 프로젝트</div></div>
 <div class="stat"><div class="n">5</div><div class="l">지금도 쓰는 것</div></div>
</div>
<div class="tags" style="margin-top:34px">
 <span class="tag">Dojae</span><span class="tag">Jari</span>
 <span class="tag">Rhythm Lab V</span><span class="tag">Jooyou</span>
 <span class="tag">두루문서</span>
</div>
<p class="lead" style="font-size:27px;margin-top:30px">만들고 끝내지 않고, 쓰면서 계속 고칩니다.</p>
""", foot()))

# 3 ─ Dojae
S.append(("03-dojae", """
<div class="eyebrow"><b>❯</b> project 01</div>
<div class="pname"><span class="en">Dojae</span></div>
<div class="psub">출결 · 소통 통합 앱</div>
<div class="pwhy">출결 기록은 서버에 쌓이는데 그걸 볼 권한이<br>단 한 사람에게만 있었습니다.</div>
<div class="points">
 <div class="point"><i></i><span>사진을 올리면 기기 안에서 OCR이 시각을 읽습니다</span></div>
 <div class="point"><i></i><span>지각·근무시간 자동 계산, 이의신청과 승인 흐름</span></div>
 <div class="point"><i></i><span>공지 · 채팅 · 캘린더 · 통계까지 한 앱에</span></div>
</div>
<div class="stats">
 <div class="stat"><div class="n">33</div><div class="l">회 배포</div></div>
 <div class="stat"><div class="n">98.1</div><div class="l">% 월 출석률</div></div>
 <div class="stat"><div class="n">43k</div><div class="l">줄 (앱)</div></div>
</div>
""", foot()))

# 4 ─ Jari
S.append(("04-jari", """
<div class="eyebrow"><b>❯</b> project 02</div>
<div class="pname"><span class="en">Jari</span><span class="live">LIVE</span></div>
<div class="psub">실시간 자리배치 · 호출 시스템</div>
<div class="pwhy">누가 자리에 있는지 모른 채 찾아가서<br>헛걸음하는 일을 없애고 싶었습니다.</div>
<div class="points">
 <div class="point"><i></i><span>자리 배치와 재실 상태를 실시간으로 공유</span></div>
 <div class="point"><i></i><span>자리에 있는 사람을 화면에서 바로 호출</span></div>
 <div class="point"><i></i><span>호출되면 음성(TTS)으로 안내하고 이력을 남김</span></div>
 <div class="point"><i></i><span>직무발명 제안서 — <b class="amber">특허 출원 준비 중</b></span></div>
</div>
<div class="tags">
 <span class="tag">Firebase Realtime DB</span><span class="tag">Cloud Functions</span>
 <span class="tag">Supertone TTS</span>
</div>
""", foot()))

# 5 ─ Rhythm Lab V
S.append(("05-rhythm", """
<div class="eyebrow"><b>❯</b> project 03</div>
<div class="pname"><span class="en">Rhythm Lab V</span><span class="live">LIVE</span></div>
<div class="psub">4키 웹 리듬게임</div>
<div class="pwhy">즐겨 하던 리듬게임을 직접 만들어보고 싶었습니다.<br>플레이에서 끝내지 않고 만드는 쪽까지 열었습니다.</div>
<div class="points">
 <div class="point"><i></i><span>수록곡을 음원 파일 없이 브라우저에서 직접 합성</span></div>
 <div class="point"><i></i><span>채보 에디터 + 곡을 들으며 찍는 녹음 모드</span></div>
 <div class="point"><i></i><span>기기별 입력 지연을 재서 보정 · 맵별 순위표</span></div>
 <div class="point"><i></i><span>판정 기준 <b style="color:#5eead4">±42ms</b>, 시계는 오디오 시간 하나로 통일</span></div>
</div>
<div class="tags">
 <span class="tag">Web Audio API</span><span class="tag">Canvas</span><span class="tag">Firebase</span>
</div>
""", foot()))

# 6 ─ 두루문서
S.append(("06-duru", """
<div class="eyebrow"><b>❯</b> project 04</div>
<div class="pname"><span class="en">두루문서</span></div>
<div class="psub">HWP 문서 편집기 (Windows · macOS)</div>
<div class="pwhy">한컴오피스가 없는 컴퓨터에서도<br>HWP를 열고 고치고 저장할 수 있게.</div>
<div class="points">
 <div class="point"><i></i><span>9개 형식 열기 → PDF 포함 10개 형식으로 저장</span></div>
 <div class="point"><i></i><span>HWP 5.0 바이너리 구조를 직접 뜯어서 구현</span></div>
 <div class="point"><i></i><span>내 코드가 내 코드를 검사하면 의미가 없어서,<br>외부 파서 <b style="color:#5eead4">3개</b>로 교차 검증</span></div>
 <div class="point"><i></i><span>깨진 한글 되살리는 인코딩 자동 감지</span></div>
</div>
<div class="tags">
 <span class="tag">TypeScript</span><span class="tag">Electron</span><span class="tag">React</span>
</div>
""", foot()))

# 7 ─ 수상 · 장학
S.append(("07-awards", """
<div class="eyebrow"><b>❯</b> awards</div>
<h2>받은 것들</h2>
<div class="awards">
 <div class="aw hi"><div class="ic">🏆</div><div><div class="t">과학기술정보통신부 장관상</div>
  <div class="d">2026 AI·SW 고교챌린지 최우수상 · Flood Zero</div></div></div>
 <div class="aw"><div class="ic">🥈</div><div><div class="t">특별상 — 자율주행 경진대회</div>
  <div class="d">성균관대학교 주최</div></div></div>
 <div class="aw"><div class="ic">🎓</div><div><div class="t">KPAI 재단 장학금</div>
  <div class="d">학업 성취도와 인재 잠재력을 인정받아 선정</div></div></div>
 <div class="aw"><div class="ic">🎓</div><div><div class="t">시흥시인재양성재단 장학금</div>
  <div class="d">우수인재 전형 발탁</div></div></div>
</div>
""", foot()))

# 8 ─ 관심사
S.append(("08-interests", """
<div class="eyebrow"><b>❯</b> and more</div>
<h2>코드만 짜다<br>죽을 순 없어서</h2>
<div class="tags" style="margin-top:36px">
 <span class="tag">🎸 일렉기타</span><span class="tag">🎼 클래식기타</span>
 <span class="tag">🤘 핑거스타일</span><span class="tag">🏸 배드민턴</span>
 <span class="tag">🇩🇪 독일어</span><span class="tag">🔭 천문학</span>
 <span class="tag">🎬 영상제작</span><span class="tag">📚 독서</span>
</div>
<div class="ghead">❯ GAMES</div>
<div class="tags" style="margin-top:0">
 <span class="tag g">오버워치</span><span class="tag g">스타크래프트</span>
 <span class="tag g">발로란트</span><span class="tag g">원신</span>
 <span class="tag g">붕괴</span>
</div>
""", foot()))

# 9 ─ 계정 소개
S.append(("09-follow", """
<div class="eyebrow"><b>❯</b> what's next</div>
<h2>이 계정에는<br>이런 게 올라옵니다</h2>
<div style="display:flex;flex-direction:column;gap:19px;margin-top:38px">
 <div class="card"><div class="v">만든 결과물</div>
  <div class="s">완성한 서비스와, 그 안에 넣은 생각</div></div>
 <div class="card"><div class="v">제작 과정</div>
  <div class="s">기획부터 배포까지, 중간 과정 그대로</div></div>
 <div class="card"><div class="v">패치노트</div>
  <div class="s">쓰면서 고친 것들. 만든 뒤가 더 깁니다</div></div>
</div>
<div style="margin-top:40px"><span class="pill"><span class="dot"></span>포트폴리오는 프로필 링크에</span></div>
""", foot(right="FOLLOW →")))

for name, body, ft in S:
    doc = BASE.replace("__RAIN__", rain()).replace("__BODY__", body).replace("__FOOT__", ft)
    io.open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8").write(doc)
print("generated", len(S))
