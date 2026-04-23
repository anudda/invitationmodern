import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. 페이지 설정
st.set_page_config(page_title="지연이의 첫 번째 생일", page_icon="✨", layout="centered")

# [함수] 이미지 텍스트 변환
def get_b64(path):
    try: return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()
    except: return ""

# 2. 모던 스타일 및 고급스러운 입자 애니메이션
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Cinzel:wght@400;700&display=swap');

/* 배경 및 기본 폰트 */
.stApp { background-color: #F9F9F7 !important; font-family: 'Gowun Batang', serif; color: #333; }
.block-container { padding: 3rem 1.5rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0rem !important; }
footer, header, #MainMenu { display: none !important; }

/* 앨범 틀 설정 */
iframe { border: none; margin-top: 10px !important; margin-bottom: -20px !important; display: block; }

/* 은은한 반짝임 애니메이션 */
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
<div class="sparkle" style="width:4px; height:4px; left:50%; top:40%; animation-delay:4s;"></div>
""", unsafe_allow_html=True)

# 3. 타이틀 섹션 (고급스러운 영문과 정갈한 한글 조합)
st.markdown("""
<div style="text-align: center; position: relative; z-index: 10; margin-bottom: 40px;">
    <p style="font-family: 'Cinzel', serif; letter-spacing: 4px; color: #B08E59; font-size: 0.9rem; margin-bottom: 10px;">THE 1ST BIRTHDAY</p>
    <h1 style="font-family: 'Gowun Batang', serif; color: #2C2C2C; font-size: 2.2rem; margin: 0; font-weight: 700; letter-spacing: -1px;">지연이의 첫 돌</h1>
    <div style="width: 30px; height: 1px; background: #D4AF37; margin: 20px auto;"></div>
    <p style="font-family: 'Gowun Batang', serif; color: #666; font-size: 1rem; line-height: 1.8; letter-spacing: 0.5px;">
        가장 소중한 날,<br>지연이의 첫 번째 생일 파티에 초대합니다.
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
    #m {{ width: 100%; max-width: 450px; height: 380px; object-fit: cover; border-radius: 4px; display: block; margin: 0 auto; transition: opacity 0.5s ease-in-out; }}
    .row {{ display: flex; justify-content: center; gap: 10px; margin-top: 15px; }}
    .t {{ width: 60px; height: 60px; object-fit: cover; cursor: pointer; border-bottom: 2px solid transparent; opacity: 0.5; transition: 0.3s; }}
    .active {{ opacity: 1 !important; border-bottom: 2px solid #B08E59 !important; }}
    .cnt {{ font-family: 'Cinzel', serif; color: #B08E59; font-size: 11px; margin-top: 10px; text-align: center; letter-spacing: 2px; }}
</style>
<img id="m" src="{b64_photos[0]}">
<div class="row">{thumbs}</div>
<p class="cnt" id="c">IMAGE 01 / 04</p>
<script>
    function s(el, src, i) {{
        const m = document.getElementById('m');
        m.style.opacity = 0;
        setTimeout(() => {{
            m.src = src;
            m.style.opacity = 1;
            document.getElementById('c').innerText = "IMAGE 0" + (i+1) + " / 04";
        }}, 300);
        document.querySelectorAll('.t').forEach(t => t.classList.remove('active'));
        el.classList.add('active');
    }}
    document.querySelector('.t').classList.add('active');
</script>
"""
components.html(album_html, height=520)

# 6. 모던 정보 카드 (심플한 선과 여백 활용)
st.markdown("""
<div style="margin-top: 20px; text-align: center;">
    <div style="border-top: 1px solid #E0E0E0; border-bottom: 1px solid #E0E0E0; padding: 30px 0; margin-bottom: 30px;">
        <p style="font-family: 'Cinzel', serif; color: #B08E59; font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 10px;">WHEN</p>
        <p style="font-size: 1.1rem; color: #333; margin-bottom: 25px;">2026. 10. 24 (SAT) PM 01:00</p>
        
        <p style="font-family: 'Cinzel', serif; color: #B08E59; font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 10px;">WHERE</p>
        <p style="font-size: 1.1rem; color: #333; font-weight: bold; margin-bottom: 5px;">행복 가든 스테이</p>
        <p style="font-size: 0.85rem; color: #888;">서울특별시 강남구 행복로 123</p>
    </div>
    
    <div style="display: flex; gap: 15px; justify-content: center;">
        <a href="https://map.kakao.com" target="_blank" style="text-decoration: none; color: #666; font-size: 0.8rem; border: 1px solid #CCC; padding: 10px 20px; border-radius: 2px; letter-spacing: 1px;">KAKAO MAP</a>
        <a href="https://map.naver.com" target="_blank" style="text-decoration: none; color: #666; font-size: 0.8rem; border: 1px solid #CCC; padding: 10px 20px; border-radius: 2px; letter-spacing: 1px;">NAVER MAP</a>
    </div>
    
    <p style="color: #999; font-size: 0.85rem; margin-top: 50px; font-style: italic; letter-spacing: 0.5px;">
        With love and gratitude.
    </p>
</div>
""", unsafe_allow_html=True)
