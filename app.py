import streamlit as st
import pandas as pd

# --- إعدادات الصفحة وعنوان المتصفح ---
st.set_page_config(
    page_title="AgriOpuntia 🇩🇿", 
    page_icon="🌵",
    layout="wide"
)

# --- القائمة الجانبية لإدارة اللغة ---
st.sidebar.title("⚙️ الإعدادات / Settings")
lang = st.sidebar.selectbox(
    "Choose Language / اختر اللغة / Langue", 
    ["العربية", "Français", "English"]
)

# --- قواميس الترجمة (لتفادي أي خلل في البيانات عند تبديل اللغة) ---
t = {
    "العربية": {
        "title": "AgriOpuntia 🇩🇿",
        "subtitle": "المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد",
        "crops": ["أشجار الزيتون", "نخيل التمر", "الحبوب (القمح والشعير)", "الحمضيات (البرتقال والليمون)", "البقوليات الجافة (الفول، الحمص، الجلبانة)", "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"],
        "soils": ["تربة رملية (Sandy)", "تربة لومية أو طينية سلتية (Loamy / Silt Loam)", "تربة طينية ثقيلة (Clay)", "تربة رملية طينية (Sandy Clay Loam)", "تربة غرينية طينية (Silty Clay Loam)"],
        "climates": ["مناخ شبه جاف / جاف (حار صيفاً ومتقلب)", "مناخ صحراوي جاف جداً (شديد الحرارة وقليل الأمطار)", "مناخ ساحلي / معتدل (رطوبة نسبية ومعتدل الحرارة)"],
        "crop_label": "اختر المحصول الزراعي:",
        "soil_label": "نوع التربة (حسب التحليل المخبري):",
        "climate_label": "المنطقة المناخية للمزرعة:",
        "area_label": "مساحة الحقل المستهدف (بالمتر المربع م²):",
        "fert_label": "كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):",
        "ai_tools": "أدوات المستشار الذكي",
        "show_ai": "إظهار التحليل الذكي (AI Insights)",
        "show_climate": "إظهار التوصيات المناخية",
        "card1_title": "🌵 دور الهيدروجيل الحيوي",
        "card1_text": "<b>• المصدر:</b> مستخلص طبيعي من ألواح صبار التين الشوكي.<br><b>• الوظيفة:</b> شبكة هلامية مجهرية حول الجذور لتحْبِس المياه والأسمدة.",
        "card2_title": "🌿 تخصيص المحصول والتربة",
        "card3_title": "💧 كفاءة الري والتوفير",
        "card3_text": "<b>• توفير المياه:</b> تقليص عدد مرات السقي بنسبة تصل إلى 40%.<br><b>• مقاومة الجفاف:</b> حماية فائقة من الإجهاد المائي.",
        "dashboard_title": "لوحة القيادة الفلاحية للمحصول",
        "m1": "الهيدروجيل المقترح",
        "m2": "إجمالي أسمدة الحقل",
        "m3": "المياه الموفّرة للحقل",
        "ai_header": "التحليل الذكي وتوصيات الهيدروجيل (AI Insights)",
        "climate_header": "التوصيات الذكية حسب المناخ والمنطقة",
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
        "subtitle": "Plateforme intelligente pour le bio-hydrogel et la fertilisation",
        "crops": ["Olivier", "Palmier dattier", "Céréales", "Agrumes", "Légumineuses", "Légumes"],
        "soils": ["Sol sableux", "Sol limoneux", "Sol argileux lourd", "Sol sablo-argileux"],
        "climates": ["Climat semi-aride", "Climat saharien", "Climat côtier"],
        "crop_label": "Sélectionner la culture :",
        "soil_label": "Type de sol :",
        "climate_label": "Zone climatique :",
        "area_label": "Superficie (m²) :",
        "fert_label": "Taux d'engrais (kg/m²) :",
        "ai_tools": "Assistant IA",
        "show_ai": "Afficher Insights IA",
        "show_climate": "Afficher Recommandations Climatiques",
        "card1_title": "🌵 Rôle du Bio-Hydrogel",
        "card1_text": "<b>• Source:</b> Extrait naturel de figuier de barbarie.<br><b>• Fonction:</b> Rétention d'eau et d'nutriments autour des racines.",
        "card2_title": "🌿 Culture & Sol",
        "card3_title": "💧 Efficacité d'Irrigation",
        "card3_text": "<b>• Économie d'eau:</b> Réduction jusqu'à 40%.<br><b>• Résistance:</b> Protection contre le stress hydrique.",
        "dashboard_title": "Tableau de bord agronomique",
        "m1": "Hydrogel suggéré",
        "m2": "Engrais total",
        "m3": "Eau économisée",
        "ai_header": "Recommandations Intelligentes (AI Insights)",
        "climate_header": "Recommandations Climatiques",
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
        "subtitle": "Smart Platform for Bio-Hydrogel & Fertilization",
        "crops": ["Olive Trees", "Date Palm Trees", "Cereals", "Citrus", "Dry Legumes", "Vegetables"],
        "soils": ["Sandy Soil", "Loamy Soil", "Clay Soil", "Sandy Clay Loam"],
        "climates": ["Semi-arid climate", "Desert climate", "Coastal climate"],
        "crop_label": "Select Crop Type:",
        "soil_label": "Soil Type:",
        "climate_label": "Climate Zone:",
        "area_label": "Target Area (m²):",
        "fert_label": "Recommended fertilizer (kg/m²):",
        "ai_tools": "AI Assistant",
        "show_ai": "Show AI Insights",
        "show_climate": "Show Climate Recommendations",
        "card1_title": "🌵 Bio-Hydrogel Role",
        "card1_text": "<b>• Source:</b> Natural extract from Opuntia pads.<br><b>• Function:</b> Retains water and nutrients around roots.",
        "card2_title": "🌿 Crop & Soil",
        "card3_title": "💧 Irrigation Efficiency",
        "card3_text": "<b>• Water Saving:</b> Reduce irrigation frequency by 40%.<br><b>• Drought Defense:</b> High protection against stress.",
        "dashboard_title": "Agricultural Dashboard",
        "m1": "Suggested Hydrogel",
        "m2": "Total Fertilizer",
        "m3": "Saved Water",
        "ai_header": "AI Smart Recommendations",
        "climate_header": "Climate Recommendations",
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

# --- تنسيق CSS عام للتطبيق وتوحيد الأطوال ---
st.markdown(f"""
<style>
    .main-header {{
        background: linear-gradient(135deg, #1b4d3e 0%, #2e6f40 50%, #558b2f 100%);
        padding: 22px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(27, 77, 62, 0.15);
        border-bottom: 4px solid #d4a373;
    }}
    .main-header h1 {{
        color: white !important;
        font-size: 2.3rem;
        margin-bottom: 5px;
        font-weight: 700;
    }}
    .main-header p {{
        color: #f4f1ea !important;
        font-size: 0.95rem;
        margin: 0;
    }}
    .feature-card {{
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 18px;
        height: 210px; /* توحيد الطول والارتفاع لكل البطاقات بدقة */
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
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
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 6px;
    }}
    .feature-card p {{
        color: #333333;
        font-size: 0.88rem;
        line-height: 1.6;
        margin: 0;
    }}
    .custom-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
        background-color: #ffffff;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
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
        border-bottom: 1px solid #e0e0e0;
        color: #333333;
        font-size: 0.95rem;
    }}
    .custom-table tr:hover {{
        background-color: #f7f4ee;
    }}
</style>
""", unsafe_allow_html=True)

# --- الواجهة الرئيسية (Main Header) ---
st.markdown(f"""
<div class="main-header">
    <h1>{lang_data['title']}</h1>
    <p>{lang_data['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# --- مدخلات القائمة الجانبية (Sidebar Inputs) ---
crop_type = st.sidebar.selectbox(lang_data['crop_label'], lang_data['crops'])
soil_type = st.sidebar.selectbox(lang_data['soil_label'], lang_data['soils'])
climate_zone = st.sidebar.selectbox(lang_data['climate_label'], lang_data['climates'])

st.sidebar.markdown("---")
st.sidebar.subheader("📊 " + lang_data['area_label'])
area = st.sidebar.number_input(lang_data['area_label'], min_value=100.0, value=20000.0, step=500.0)

st.sidebar.markdown("---")
st.sidebar.subheader("🌿 Fertilization")
fertilizer_rate = st.sidebar.number_input(lang_data['fert_label'], min_value=0.01, value=0.10, step=0.01)

st.sidebar.markdown("---")
st.sidebar.subheader(f"🤖 {lang_data['ai_tools']}")
show_ai_insights = st.sidebar.checkbox(lang_data['show_ai'], value=False)
show_climate_recs = st.sidebar.checkbox(lang_data['show_climate'], value=False)

# --- الحسابات العلمية الموحدة ---
hydrogel_needed_kg = area * 0.12 
water_saved_m3 = area * 0.22 
total_crop_fertilizer_kg = area * fertilizer_rate 

# --- البطاقات الثلاث المتساوية بدقة ---
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

# --- التحليل الذكي حسب التفعيل ---
if show_ai_insights:
    st.markdown("---")
    st.subheader(f"🤖 {lang_data['ai_header']}")
    st.info(f"""
    * 💧 **Water Savings / توفير المياه:** 35% - 45%
    * 🧪 **Recommended Dose / الجرعة المقترحة:** **{hydrogel_needed_kg:,.1f} kg**
    * 🌱 **Fertilizer Efficiency / كفاءة الأسمدة:** {total_crop_fertilizer_kg:,.1f} kg
    """)

if show_climate_recs:
    st.markdown("---")
    st.subheader(f"🌤️ {lang_data['climate_header']}")
    st.success("Custom climate adaptations applied successfully to your selected regional parameters.")

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
report_content = f"AgriOpuntia Technical Report\nCrop: {crop_type}\nArea: {area} m²\nHydrogel: {hydrogel_needed_kg:.1f} kg\nFertilizer: {total_crop_fertilizer_kg:.1f} kg"
st.download_button(
    label=lang_data['download_btn'],
    data=report_content,
    file_name="AgriOpuntia_Report.txt",
    mime="text/plain"
)












































