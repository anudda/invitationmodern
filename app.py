import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="돌잔치 모던 시안", page_icon="✨", layout="centered")

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 모던 스타일 및 고급스러운 입자 애니메이션
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Cinzel:wght@400;700&display=swap');
.stApp { background-color: #F9F9F7 !important; font-family: 'Gowun Batang', serif; color: #333; }
.block-container { padding: 3rem 1.5rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
footer, header, #MainMenu { display: none !important; }
iframe { border: none; margin-top: 10px !important; margin-bottom: -20px !important; display: block; }
.sparkle { position: fixed; background: radial-gradient(circle, #D4AF37 0%, transparent 70%); border-radius: 50%; opacity: 0; animation: twinkle 5s infinite; pointer-events: none; }
@keyframes twinkle { 
    0%, 100% { opacity: 0; transform: translateY(0); }
    50% { opacity: 0.3; transform: translateY(-20px); }
}
</style>
<div class="sparkle" style="width:4px; height:4px; left:10%; top:20%; animation-delay:0s;"></div>
<div class="sparkle" style="width:6px; height:6px; left:85%; top:15%; animation-delay:1s;"></div>
<div class="sparkle" style="width:3px; height:3px; left:20%; top:70%; animation-delay:2s;"></div>
<div class="sparkle" style="width:5px; height:5px; left:80%; top:80%; animation-delay:3s;"></div>
""", unsafe_allow_html=True)

# 3. 타이틀 섹션
st.markdown("""
<div style="text-align: center; position: relative; z-index: 10; margin-bottom: 30px;">
    <p style="font-family: 'Cinzel', serif; letter-spacing: 4px; color: #B08E59; font-size: 0.85rem; margin-bottom: 10px;">JIYEON'S 1ST BIRTHDAY</p>
    <h1 style="font-family: 'Gowun Batang', serif; color: #2C2C2C; font-size: 2.1rem; margin: 0; font-weight: 700; letter-spacing: -1px;">지연이의 첫 돌</h1>
    <div style="width: 30px; height: 1px; background: #D4AF37; margin: 20px auto;"></div>
    <p style="font-family: 'Gowun Batang', serif; color: #666; font-size: 0.95rem; line-height: 1.7; letter-spacing: 0.5px;">
        가장 소중한 날, <br>아빠 윤진수와 엄마 김소연의 예쁜 딸 지연이의 <br> 첫 생일 파티에 여러분을 초대합니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. 사진 데이터
photos = ["baby.jpg", "baby1.jpg", "baby2.jpg", "baby3.jpg"]
b64_photos = [get_b64(p) for p in photos]

# 5. 모던 페이드 슬라이드 앨범
thumbs = "".join([f'<img class="t" src="{p}" onclick="s(this, \'{p}\', {i})">' for i, p in enumerate(b64_photos)])
album_html = f"""
<style>
    body {{ margin: 0; background: transparent; overflow: hidden; }}
    #m {{ width: 100%; max-width: 450px; height: 380px; object-fit: cover; border-radius: 2px; display: block; margin: 0 auto; transition: opacity 0.4s ease-in-out; }}
    .row {{ display: flex; justify-content: center; gap: 12px; margin-top: 15px; }}
    .t {{ width: 55px; height: 55px; object-fit: cover; cursor: pointer; border-bottom: 2px solid transparent; opacity: 0.4; transition: 0.3s; }}
    .active {{ opacity: 1 !important; border-bottom: 2px solid #B08E59 !important; }}
    .cnt {{ font-family: 'Cinzel', serif; color: #B08E59; font-size: 10px; margin-top: 12px; text-align: center; letter-spacing: 2px; }}
</style>
<img id="m" src="{b64_photos[0]}">
<div class="row">{thumbs}</div>
<p class="cnt" id="c">01 / 04</p>
<script>
    function s(el, src, i) {{
        const m = document.getElementById('m');
        m.style.opacity = 0;
        setTimeout(() => {{
            m.src = src;
            m.style.opacity = 1;
            document.getElementById('c').innerText = "0" + (i+1) + " / 04";
        }}, 250);
        document.querySelectorAll('.t').forEach(t => t.classList.remove('active'));
        el.classList.add('active');
    }}
    document.querySelector('.t').classList.add('active');
</script>
"""
components.html(album_html, height=520)

# 6. [해결] 정보 카드 및 버튼 (빈 줄 없이 꽉 채운 코드)
st.markdown("""
<div style="margin-top: 10px; text-align: center; position: relative; z-index: 10;">
    <div style="border-top: 1px solid #E0E0E0; border-bottom: 1px solid #E0E0E0; padding: 30px 0; margin-bottom: 30px;">
        <p style="font-family: 'Cinzel', serif; color: #B08E59; font-size: 0.75rem; letter-spacing: 2px; margin: 0 0 10px;">WHEN</p>
        <p style="font-size: 1.05rem; color: #333; margin: 0 0 25px;">2026. 10. 24 (SAT) PM 01:00</p>
        <p style="font-family: 'Cinzel', serif; color: #B08E59; font-size: 0.75rem; letter-spacing: 2px; margin: 0 0 10px;">WHERE</p>
        <p style="font-size: 1.05rem; color: #333; font-weight: bold; margin: 0 0 5px;">행복 가든 스테이</p>
        <p style="font-size: 0.8rem; color: #888; margin: 0;">서울특별시 강남구 행복로 123</p>
    </div>
    <div style="display: flex; gap: 12px; justify-content: center; padding: 0 10px;">
        <a href="https://map.kakao.com" target="_blank" style="flex: 1; text-decoration: none; color: #666; font-size: 0.75rem; border: 1px solid #DDD; padding: 12px 0; border-radius: 0px; letter-spacing: 1px; background: #FFF;">KAKAO MAP</a>
        <a href="https://map.naver.com" target="_blank" style="flex: 1; text-decoration: none; color: #666; font-size: 0.75rem; border: 1px solid #DDD; padding: 12px 0; border-radius: 0px; letter-spacing: 1px; background: #FFF;">NAVER MAP</a>
    </div>
    <p style="color: #AAA; font-size: 0.8rem; margin-top: 50px; font-style: italic; letter-spacing: 1px;">With love and gratitude.</p>
</div>
""", unsafe_allow_html=True)
