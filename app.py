import streamlit as st
import pandas as pd

# --- إعدادات الصفحة وعنوان المتصفح ---
st.set_page_config(
    page_title="AgriOpuntia 🇩🇿", 
    page_icon="🌵",
    layout="wide"
)

# --- إدارة الحالة الأولية للغة والمحادثة ---
if 'lang_choice' not in st.session_state:
    st.session_state.lang_choice = "العربية"

if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- القائمة الجانبية لإدارة اللغة والإعدادات ---
st.sidebar.title("⚙️ الإعدادات / Settings")

lang = st.sidebar.selectbox(
    "Choose Language / اختر اللغة / Langue", 
    ["العربية", "Français", "English"],
    index=["العربية", "Français", "English"].index(st.session_state.lang_choice),
    key="language_selector"
)

if lang != st.session_state.lang_choice:
    st.session_state.lang_choice = lang
    st.rerun()

# --- قواميس الترجمة المحدثة ---
t = {
    "العربية": {
        "title": "AgriOpuntia 🇩🇿",
        "subtitle": "المنصة الذكية لتطبيق الهيدروجيل الحيوي وإدارة المزارع",
        "crops": {
            "olive": "أشجار الزيتون", 
            "palm": "نخيل التمر", 
            "cereals": "الحبوب (القمح والشعير)", 
            "citrus": "الحمضيات (البرتقال والليمون)", 
            "legumes": "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
            "vegetables": "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
        },
        "soils": {
            "sandy": "تربة رملية - Sandy",
            "loamy": "تربة لومية أو طينية سلتية - Loamy",
            "clay": "تربة طينية ثقيلة - Clay",
            "sandy_clay": "تربة رملية طينية - Sandy Clay",
            "silty_clay": "تربة غرينية طينية - Silty Clay"
        },
        "weathers": {
            "sunny": "☀️ مشمس وحار (موجة حرارة جافة)",
            "rainy": "🌧️ ممطر (تساقطات معتبرة)",
            "cloudy": "⛅ غائم جزئياً (رطوبة معتدلة)",
            "stormy": "⚡ عاصفي (رياح قوية وتقلبات)"
        },
        "weather_tips": {
            "sunny": "⚠️ تنبيه حراري: يُنصح بتفعيل الهيدروجيل بكامل طاقته للحفاظ على رطوبة الجذور، وتجنب السقي في أوقات الذروة.",
            "rainy": "💡 إرشاد: تم توفير كميات معتبرة من مياه الري بفضل الأمطار، يوصى بمراقبة الصرف لتجنب تشبع التربة بالماء.",
            "cloudy": "🌱 ملاحظة: الطقس ملائم للعمليات الزراعية الخفيفة والتسميد الورقي لامتصاص مثالي.",
            "stormy": "🚨 تحذير عاصفي: تأمين شبكات السقي الموضعي وحماية الأشجار الفتية من التيارات الهوائية القوية."
        },
        "crop_label": "اختر المحصول الزراعي:",
        "soil_label": "نوع التربة (حسب التحليل المخبري):",
        "weather_label": "حالة الطقس الحالية في الحقل:",
        "area_label": "مساحة الحقل المستهدف (بالمتر المربع م²):",
        "fert_label": "كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):",
        "sidebar_options_header": "أدوات العرض والتحليل",
        "show_ai": "إظهار لوحة التحليل الذكي",
        "card1_title": "🌵 دور الهيدروجيل الحيوي",
        "card1_text": "<b>• المصدر:</b> مستخلص طبيعي من ألواح صبار التين الشوكي.<br><b>• الوظيفة:</b> شبكة هلامية مجهرية حول الجذور لتحْبِس المياه والأسمدة.",
        "card2_title": "🌿 تخصيص المحصول والتربة",
        "card3_title": "💧 كفاءة الري والتوفير",
        "card3_text": "<b>• توفير المياه:</b> تقليص عدد مرات السقي بنسبة تصل إلى 40%.<br><b>• مقاومة الجفاف:</b> حماية فائقة من الإجهاد المائي.",
        "dashboard_title": "لوحة القيادة الفلاحية للمحصول",
        "m1": "الهيدروجيل المقترح",
        "m2": "إجمالي أسمدة الحقل",
        "m3": "المياه الموفّرة للحقل",
        "ai_header": "مساعد الذكاء الاصطناعي الفلاحي (Agri-Chat)",
        "chat_placeholder": "اسأل المساعد عن التسميد، الري، مكافحة الجفاف، أو أي استشارة فلاحية...",
        "weather_header": "التوجيهات والإرشادات الفورية حسب حالة الطقس",
        "table_header": "الجدول الزمني المقترح لسقي ومتابعة المحصول",
        "table_cols": ["مرحلة نمو المحصول", "تأثير الهيدروجيل الحيوي", "تواتر الري الموصى به"],
        "table_rows": [
            ["مرحلة الغرس / البداية", "حماية الجذور الفتية وتثبيت الرطوبة الأولية", "عادي مع تقليل الفترات بـ 20%"],
            ["مرحلة النمو الخضري", "إمداد متواصل ومستقر بالمياه والأسمدة", "تخفيض الفترات بـ 40%"],
            ["مرحلة الإزهار والعقد", "الحماية من صدمات العطش والإجهاد الحراري", "تخفيض الفترات بـ 35%"],
            ["مرحلة النضج والجني", "تقليل تدريجي للرطوبة لتحسين جودة المحصول", "ري خفيف عند الضرورة"]
        ],
        "report_header": "الملخص التقني وتحميل التقرير",
        "download_btn": "📥 تحميل التقرير التقني للمزرعة",
        "dir": "rtl",
        "align": "right"
    },
    "Français": {
        "title": "AgriOpuntia 🇩🇿",
        "subtitle": "Plateforme intelligente pour le bio-hydrogel et la gestion agricole",
        "crops": {
            "olive": "Olivier", 
            "palm": "Palmier dattier", 
            "cereals": "Céréales", 
            "citrus": "Agrumes", 
            "legumes": "Légumineuses", 
            "vegetables": "Légumes"
        },
        "soils": {
            "sandy": "Sol sableux", 
            "loamy": "Sol limoneux", 
            "clay": "Sol argileux lourd", 
            "sandy_clay": "Sol sablo-argileux",
            "silty_clay": "Sol limono-argileux"
        },
        "weathers": {
            "sunny": "☀️ Ensoleillé et chaud",
            "rainy": "🌧️ Pluvieux",
            "cloudy": "⛅ Partiellement nuageux",
            "stormy": "⚡ Orageux / Vents forts"
        },
        "weather_tips": {
            "sunny": "⚠️ Alerte chaleur : Activez l'hydrogel pour retenir l'humidité des racines, évitez l'arrosage aux heures de pointe.",
            "rainy": "💡 Conseil : Économie d'eau maximale grâce aux pluies. Surveillez le drainage du sol.",
            "cloudy": "🌱 Note : Temps idéal pour les travaux légers et la fertilisation foliaire.",
            "stormy": "🚨 Avertissement : Sécurisez les systèmes d'irrigation et protégez les cultures sensibles."
        },
        "crop_label": "Sélectionner la culture :",
        "soil_label": "Type de sol :",
        "weather_label": "Condition météo au champ :",
        "area_label": "Superficie (m²) :",
        "fert_label": "Taux d'engrais (kg/m²) :",
        "sidebar_options_header": "Options d'affichage",
        "show_ai": "Afficher le module IA",
        "card1_title": "🌵 Rôle du Bio-Hydrogel",
        "card1_text": "<b>• Source:</b> Extrait naturel de figuier de barbarie.<br><b>• Fonction:</b> Rétention d'eau et d'nutriments autour des racines.",
        "card2_title": "🌿 Culture & Sol",
        "card3_title": "💧 Efficacité d'Irrigation",
        "card3_text": "<b>• Économie d'eau:</b> Réduction jusqu'à 40%.<br><b>• Résistance:</b> Protection contre le stress hydrique.",
        "dashboard_title": "Tableau de bord agronomique",
        "m1": "Hydrogel suggéré",
        "m2": "Engrais total",
        "m3": "Eau économisée",
        "ai_header": "Assistant IA Agricole (Agri-Chat)",
        "chat_placeholder": "Posez vos questions sur l'irrigation, la fertilisation, ou la gestion des sols...",
        "weather_header": "Recommandations Météo en Temps Réel",
        "table_header": "Calendrier d'irrigation et de suivi",
        "table_cols": ["Phase de culture", "Effet du Bio-Hydrogel", "Fréquence d'irrigation"],
        "table_rows": [
            ["Plantation / Début", "Protection des jeunes racines et humidité", "Normal avec réduction de 20%"],
            ["Croissance végétative", "Alimentation continue en eau et nutriments", "Réduction de 40%"],
            ["Floraison et nouaison", "Protection contre le stress thermique", "Réduction de 35%"],
            ["Maturation et récolte", "Réduction progressive de l'humidité", "Arrosage léger si besoin"]
        ],
        "report_header": "Résumé technique et téléchargement",
        "download_btn": "📥 Télécharger le rapport technique",
        "dir": "ltr",
        "align": "left"
    },
    "English": {
        "title": "AgriOpuntia 🇩🇿",
        "subtitle": "Smart Platform for Bio-Hydrogel & Farm Management",
        "crops": {
            "olive": "Olive Trees", 
            "palm": "Date Palm Trees", 
            "cereals": "Cereals", 
            "citrus": "Citrus", 
            "legumes": "Dry Legumes", 
            "vegetables": "Vegetables"
        },
        "soils": {
            "sandy": "Sandy Soil", 
            "loamy": "Loamy Soil", 
            "clay": "Clay Soil", 
            "sandy_clay": "Sandy Clay Loam",
            "silty_clay": "Silty Clay Loam"
        },
        "weathers": {
            "sunny": "☀️ Sunny & Hot",
            "rainy": "🌧️ Rainy",
            "cloudy": "⛅ Partly Cloudy",
            "stormy": "⚡ Stormy / High Winds"
        },
        "weather_tips": {
            "sunny": "⚠️ Heat Alert: Maximize bio-hydrogel efficiency to preserve root moisture, avoid peak-hour watering.",
            "rainy": "💡 Tip: Significant irrigation water saved via rainfall. Monitor soil drainage.",
            "cloudy": "🌱 Note: Favorable weather for light farming tasks and foliar feeding.",
            "stormy": "🚨 Storm Warning: Secure irrigation systems and protect young crops from strong winds."
        },
        "crop_label": "Select Crop Type:",
        "soil_label": "Soil Type:",
        "weather_label": "Field Weather Condition:",
        "area_label": "Target Area (m²):",
        "fert_label": "Recommended fertilizer (kg/m²):",
        "sidebar_options_header": "Display Options",
        "show_ai": "Show AI Module",
        "card1_title": "🌵 Bio-Hydrogel Role",
        "card1_text": "<b>• Source:</b> Natural extract from Opuntia pads.<br><b>• Function:</b> Retains water and nutrients around roots.",
        "card2_title": "🌿 Crop & Soil",
        "card3_title": "💧 Irrigation Efficiency",
        "card3_text": "<b>• Water Saving:</b> Reduce irrigation frequency by 40%.<br><b>• Drought Defense:</b> High protection against stress.",
        "dashboard_title": "Agricultural Dashboard",
        "m1": "Suggested Hydrogel",
        "m2": "Total Fertilizer",
        "m3": "Saved Water",
        "ai_header": "Agricultural AI Assistant (Agri-Chat)",
        "chat_placeholder": "Ask the assistant about irrigation, fertilization, or soil management...",
        "weather_header": "Real-Time Weather Recommendations",
        "table_header": "Proposed Irrigation & Monitoring Schedule",
        "table_cols": ["Crop Growth Stage", "Bio-Hydrogel Effect", "Recommended Irrigation"],
        "table_rows": [
            ["Planting Stage", "Protecting young roots & initial moisture", "Normal with 20% reduced frequency"],
            ["Vegetative Growth", "Continuous stable supply of water & nutrients", "Reduce frequency by 40%"],
            ["Flowering Stage", "Protection from drought & heat stress", "Reduce frequency by 35%"],
            ["Maturation Stage", "Gradual moisture reduction for quality", "Light watering when necessary"]
        ],
        "report_header": "Technical Summary & Download",
        "download_btn": "📥 Download Technical Report",
        "dir": "ltr",
        "align": "left"
    }
}

lang_data = t[lang]

# --- تنسيق CSS المريح للأعين (Eye-Friendly Palette & Modern UI) ---
st.markdown(f"""
<style>
    .stApp {{
        background-color: #f7f9f6;
    }}
    .main-header {{
        background: linear-gradient(135deg, #1b4d3e 0%, #2e6f40 100%);
        padding: 24px;
        border-radius: 16px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(27, 77, 62, 0.12);
        border-bottom: 4px solid #d4a373;
    }}
    .main-header h1 {{
        color: #ffffff !important;
        font-size: 2.2rem;
        margin-bottom: 5px;
        font-weight: 700;
    }}
    .main-header p {{
        color: #e2ede4 !important;
        font-size: 0.95rem;
        margin: 0;
    }}
    .feature-card {{
        background-color: #ffffff;
        border: 1px solid #d8e2dc;
        border-radius: 12px;
        padding: 18px;
        height: 220px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        direction: {lang_data['dir']};
        text-align: {lang_data['align']};
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }}
    .feature-card h4 {{
        color: #1b4d3e;
        font-size: 1.05rem;
        margin-bottom: 10px;
        font-weight: 700;
        border-bottom: 2px solid #f0f4f1;
        padding-bottom: 6px;
    }}
    .feature-card p {{
        color: #2f3e46;
        font-size: 0.88rem;
        line-height: 1.6;
        margin: 0;
    }}
    .weather-box {{
        background-color: #eef5f1;
        border-inline-start: 6px solid #2e6f40;
        padding: 18px;
        border-radius: 10px;
        margin-top: 15px;
        margin-bottom: 15px;
        direction: {lang_data['dir']};
        text-align: {lang_data['align']};
        color: #1b4d3e;
        font-weight: 600;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        font-size: 1.05rem;
    }}
    .custom-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
        background-color: #ffffff;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.04);
        direction: {lang_data['dir']};
        text-align: {lang_data['align']};
    }}
    .custom-table th {{
        background-color: #1b4d3e;
        color: white;
        padding: 12px 15px;
        font-size: 1rem;
    }}
    .custom-table td {{
        padding: 12px 15px;
        border-bottom: 1px solid #e9ecef;
        color: #2f3e46;
        font-size: 0.95rem;
    }}
    .custom-table tr:hover {{
        background-color: #f2f7f4;
    }}
</style>
""", unsafe_allow_html=True)

# --- الهيدر الرئيسي ---
st.markdown(f"""
<div class="main-header">
    <h1>{lang_data['title']}</h1>
    <p>{lang_data['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# --- مدخلات القائمة الجانبية (بمفاتيح آمنة ومستقرة) ---
crop_key = st.sidebar.selectbox(
    lang_data['crop_label'], 
    options=list(lang_data['crops'].keys()), 
    format_func=lambda x: lang_data['crops'][x],
    key="selected_crop_key"
)
crop_type = lang_data['crops'][crop_key]

soil_key = st.sidebar.selectbox(
    lang_data['soil_label'], 
    options=list(lang_data['soils'].keys()), 
    format_func=lambda x: lang_data['soils'][x],
    key="selected_soil_key"
)
soil_type = lang_data['soils'][soil_key]

weather_key = st.sidebar.selectbox(
    lang_data['weather_label'], 
    options=list(lang_data['weathers'].keys()), 
    format_func=lambda x: lang_data['weathers'][x],
    key="selected_weather_key"
)
current_weather_tip = lang_data['weather_tips'][weather_key]

st.sidebar.markdown("---")
area = st.sidebar.number_input(
    lang_data['area_label'], 
    min_value=100.0, 
    value=20000.0, 
    step=500.0, 
    key="input_area"
)

st.sidebar.markdown("---")
fertilizer_rate = st.sidebar.number_input(
    lang_data['fert_label'], 
    min_value=0.01, 
    value=0.10, 
    step=0.01, 
    key="input_fert"
)

# --- خيارات العرض والتحليل في القائمة الجانبية ---
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{lang_data['sidebar_options_header']}**")
show_ai_module = st.sidebar.checkbox(lang_data['show_ai'], value=True, key="chk_ai_module")

# --- الحسابات العلمية والدقيقة ---
hydrogel_needed_kg = area * 0.12 
water_saved_m3 = area * 0.22 
total_crop_fertilizer_kg = area * fertilizer_rate 

# --- البطاقات الثلاث المتساوية ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="feature-card">
        <h4>{lang_data['card1_title']}</h4>
        <p>{lang_data['card1_text']}</p>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    if lang == "العربية":
        card2_text = f"<b>• المحصول:</b> {crop_type}<br><b>• التربة:</b> {soil_type}<br><b>• الأسمدة:</b> <b>{total_crop_fertilizer_kg:,.1f} كغ</b>"
    elif lang == "Français":
        card2_text = f"<b>• Culture:</b> {crop_type}<br><b>• Sol:</b> {soil_type}<br><b>• Engrais total:</b> <b>{total_crop_fertilizer_kg:,.1f} kg</b>"
    else:
        card2_text = f"<b>• Crop:</b> {crop_type}<br><b>• Soil:</b> {soil_type}<br><b>• Total Fertilizer:</b> <b>{total_crop_fertilizer_kg:,.1f} kg</b>"
        
    st.markdown(f"""
    <div class="feature-card">
        <h4>{lang_data['card2_title']}</h4>
        <p>{card2_text}</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown(f"""
    <div class="feature-card">
        <h4>{lang_data['card3_title']}</h4>
        <p>{lang_data['card3_text']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- لوحة القيادة (Metrics) ---
st.markdown("---")
st.markdown(f'<h2 style="direction: {lang_data["dir"]}; text-align: {lang_data["align"]}; color: #1b4d3e;">📊 {lang_data["dashboard_title"]}: {crop_type}</h2>', unsafe_allow_html=True)

mcol1, mcol2, mcol3 = st.columns(3)
mcol1.metric(lang_data['m1'], f"{hydrogel_needed_kg:,.1f} kg" if lang != "العربية" else f"{hydrogel_needed_kg:,.1f} كغ")
mcol2.metric(lang_data['m2'], f"{total_crop_fertilizer_kg:,.1f} kg" if lang != "العربية" else f"{total_crop_fertilizer_kg:,.1f} كغ")
mcol3.metric(lang_data['m3'], f"{water_saved_m3:,.1f} m³")

# --- التوجيهات الفورية حسب الطقس ---
st.markdown("---")
st.subheader(f"🌤️ {lang_data['weather_header']}")
st.markdown(f"""
<div class="weather-box">
    {current_weather_tip}
</div>
""", unsafe_allow_html=True)

# --- مساعد الذكاء الاصطناعي الفلاحي التفاعلي (Agri-Chat) ---
if show_ai_module:
    st.markdown("---")
    st.subheader(f"🤖 {lang_data['ai_header']}")
    
    # عرض سجل المحادثات
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # إدخال محادثة جديدة من المستخدم
    if user_prompt := st.chat_input(lang_data['chat_placeholder']):
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # استجابة الذكاء الاصطناعي المتخصصة قطاعياً
        with st.chat_message("assistant"):
            if any(word in user_prompt.lower() for word in ["هيدروجيل", "hydrogel", "صبار", "opuntia", "ماء", "سقي", "رطوبة"]):
                ai_reply = f"بخصوص استفسارك حول النشاط الفلاحي لـ **{crop_type}**، استخدام الهيدروجيل الحيوي المستخلص من صبار التين الشوكي في تربة مثل **{soil_type}** يساعد في خفض الاحتياجات المائية بحوالي 35-45%، مع الحفاظ على كفاءة امتصاص الأسمدة المحسوبة بـ **{total_crop_fertilizer_kg:,.1f} كغ**."
            elif any(word in user_prompt.lower() for word in ["سماد", "fertilizer", "تسميد", "أسمدة"]):
                ai_reply = f"كمية الأسمدة الموصى بها لمساحة **{area:,.0f} م²** الخاصة بـ **{crop_type}** تقدر بـ **{total_crop_fertilizer_kg:,.1f} كغ**. يُنصح دائماً بتوزيعها على دفعات لزيادة الكفاءة."
            else:
                ai_reply = f"أهلاً بكِ. بصفتي مساعدك الذكي في منصة **AgriOpuntia**، أنا هنا لمساعدتك في كل ما يتعلق بإدارة زراعة **{crop_type}**، تحسين مقاومة الجفاف، وتسيير الحقول بكفاءة عالية. تفطلي بطرح سؤالك الزراعي المحدد!"
            
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# --- جدول المتابعة ---
st.markdown("---")
st.markdown(f'<h3 style="direction: {lang_data["dir"]}; text-align: {lang_data["align"]}; color: #1b4d3e;">📅 {lang_data["table_header"]}</h3>', unsafe_allow_html=True)

rows_html = ""
for row in lang_data['table_rows']:
    rows_html += f"<tr><td><b>{row[0]}</b></td><td>{row[1]}</td><td>{row[2]}</td></tr>"

st.markdown(f"""
<table class="custom-table">
    <tr>
        <th>{lang_data['table_cols'][0]}</th>
        <th>{lang_data['table_cols'][1]}</th>
        <th>{lang_data['table_cols'][2]}</th>
    </tr>
    {rows_html}
</table>
""", unsafe_allow_html=True)

# --- التقرير والتحميل ---
st.markdown("---")
st.subheader(f"📑 {lang_data['report_header']}")
report_content = (
    f"AgriOpuntia Technical Report\n"
    f"Crop: {crop_type}\n"
    f"Soil: {soil_type}\n"
    f"Area: {area} m²\n"
    f"Hydrogel: {hydrogel_needed}"






























































