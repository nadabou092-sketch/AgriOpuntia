import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="AgriOpuntia | Bio-Hydrogel Optimization",
    page_icon="🌵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. القاموس للغات الثلاث
TRANSLATIONS = {
    "العربية": {
        "title": "🌵 AgriOpuntia",
        "subtitle": "المنصة الذكية لاستمثال الجرعات الحيوية وتوفير مياه الري",
        "caption": "نظام هندسي مخصص لتحديد الجرعات الميدانية للهيدروجيل الحيوي المستخلص من الصبار (Opuntia)",
        "card1_title": "🌵 استخلاص الصبار",
        "card1_desc": "استغلال مادة الموكيلينج (Mucilage) الطبيعية من ألواح الصبار ذات القدرة العالية على الامتصاص.",
        "card2_title": "💧 حبس الرطوبة",
        "card2_desc": "رفع قدرة التربة على الإمساك بالمياه وتقليل الفقد الناتج عن التبخر والنفاذية العالية.",
        "card3_title": "🌱 تحفيز الجذور",
        "card3_desc": "توفير بيئة رطبة مستدامة حول الشعيرات الجذرية لمقاومة الإجهاد المائي والجفاف.",
        "sidebar_title": "⚙️ إعدادات الحقل والمزرعة",
        "soil_label": "اختر نوع التربة الميدانية:",
        "soils": ["تربة رملية (سريعة النفاذية)", "تربة طينية (حافظة للماء)", "تربة كلسية / متوسطة"],
        "crop_label": "اختر نوع المحصول المستهدف:",
        "crops": ["أشجار مثمرة (زيتون، حمضيات، نخيل)", "محاصيل حقلية وخضروات", "نباتات زينة ومساحات خضراء"],
        "area_label": "مساحة القطعة (بالأمتار المربعة m²):",
        "summary_title": "📋 تفاصيل المدخلات الحقلية",
        "soil_info": "التربة",
        "crop_info": "المحصول",
        "area_info": "المساحة",
        "btn_label": "توليد التقرير الميداني الحسابي 🚀",
        "success_msg": "✅ تم استكمال التحليل وتحديد الجرعة المثالية بنجاح!",
        "metric1": "الجرعة الحيوية المطلوبة",
        "metric2": "نسبة خفض مياه الري",
        "metric3": "المياه الموفرة تقريبياً",
        "recommendation": "💡 **توصية AgriOpuntia الميدانية:** للحصول على أقصى كفاءة لامتصاص الرطوبة، ينصح بدمج حبيبات الهيدروجيل مع التربة على عمق **15 إلى 20 سم** بالقرب من المجموع الجذرية قبل عملية الري الأولى.",
        "download_btn": "📥 تحميل التقرير الميداني (ملف نصي)"
    },
    "Français": {
        "title": "🌵 AgriOpuntia",
        "subtitle": "Plateforme Intelligente d'Optimisation des Doses Bio et de l'Eau",
        "caption": "Système d'ingénierie pour le dosage de l'hydrogel biosourcé extrait du cactus (Opuntia)",
        "card1_title": "🌵 Extraction de Cactus",
        "card1_desc": "Valorisation du mucilage naturel des raquettes de cactus à haute capacité d'absorption.",
        "card2_title": "💧 Rétention d'Humidité",
        "card2_desc": "Augmentation de la capacité du sol à retenir l'eau et réduction de l'évaporation.",
        "card3_title": "🌱 Stimulation Racinaire",
        "card3_desc": "Création d'un micro-environnement humide autour des racines contre le stress hydrique.",
        "sidebar_title": "⚙️ Paramètres de la Parcelle",
        "soil_label": "Sélectionnez le type de sol :",
        "soils": ["Sol sableux (Infiltration rapide)", "Sol argileux (Rétention d'eau)", "Sol calcaire / Moyen"],
        "crop_label": "Sélectionnez le type de culture :",
        "crops": ["Arbres fruitiers (Olivier, Agrumes, Palmier)", "Cultures maraîchères & Légumes", "Espaces verts & Plantes ornementales"],
        "area_label": "Superficie de la parcelle (en m²) :",
        "summary_title": "📋 Détails des Données d'Entrée",
        "soil_info": "Sol",
        "crop_info": "Culture",
        "area_info": "Superficie",
        "btn_label": "Générer le Rapport de Calcul 🚀",
        "success_msg": "✅ Analyse terminée et dose optimale calculée avec succès !",
        "metric1": "Dose Bio Requise",
        "metric2": "Réduction d'Eau d'Irrigation",
        "metric3": "Eau Économisée (Est.)",
        "recommendation": "💡 **Recommandation AgriOpuntia :** Pour une efficacité maximale, intégrez les granules d'hydrogel dans le sol à une profondeur de **15 à 20 cm** près du système racinaire avant le premier arrosage.",
        "download_btn": "📥 Télécharger le rapport terrain (TXT)"
    },
    "English": {
        "title": "🌵 AgriOpuntia",
        "subtitle": "Smart Platform for Bio-Dose & Irrigation Water Optimization",
        "caption": "Engineering system for field dosing of cactus-derived bio-hydrogel (Opuntia)",
        "card1_title": "🌵 Cactus Extraction",
        "card1_desc": "Utilizing natural mucilage from cactus cladodes with high water-binding capacity.",
        "card2_title": "💧 Moisture Retention",
        "card2_desc": "Enhancing soil waterholding capacity and reducing losses from evaporation.",
        "card3_title": "🌱 Root Stimulation",
        "card3_desc": "Providing a sustainable moist micro-environment around root systems against drought stress.",
        "sidebar_title": "⚙️ Field & Farm Settings",
        "soil_label": "Select Soil Type:",
        "soils": ["Sandy Soil (Fast Infiltration)", "Clay Soil (Water Retentive)", "Calcareous / Medium Soil"],
        "crop_label": "Select Target Crop Type:",
        "crops": ["Fruit Trees (Olive, Citrus, Date Palm)", "Field Crops & Vegetables", "Ornamental Plants & Green Spaces"],
        "area_label": "Plot Area (in m²):",
        "summary_title": "📋 Field Input Summary",
        "soil_info": "Soil",
        "crop_info": "Crop",
        "area_info": "Area",
        "btn_label": "Generate Field Calculation Report 🚀",
        "success_msg": "✅ Analysis completed and optimal dose calculated successfully!",
        "metric1": "Required Bio-Dose",
        "metric2": "Water Reduction Rate",
        "metric3": "Estimated Water Saved",
        "recommendation": "💡 **AgriOpuntia Field Tip:** For maximum moisture absorption efficiency, blend the hydrogel granules into the soil at a depth of **15 to 20 cm** near the root system prior to the first irrigation.",
        "download_btn": "📥 Download Field Report (TXT)"
    }
}

# 3. اختيار اللغة
lang = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة / Langue", ["العربية", "Français", "English"])
t = TRANSLATIONS[lang]

# 4. تنسيق الواجهة بـ CSS
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .feature-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border-top: 4px solid #2d6a4f;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    .stButton>button {
        background-color: #1b4332;
        color: white;
        border-radius: 10px;
        height: 3.2em;
        width: 100%;
        font-weight: bold;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2d6a4f;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 5. العناوين والبطاقات
st.title(t["title"])
st.write(f"##### **{t['subtitle']}**")
st.caption(t["caption"])

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='feature-card'><h3>{t['card1_title']}</h3><p>{t['card1_desc']}</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='feature-card'><h3>{t['card2_title']}</h3><p>{t['card2_desc']}</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='feature-card'><h3>{t['card3_title']}</h3><p>{t['card3_desc']}</p></div>", unsafe_allow_html=True)

st.divider()

# 6. القائمة الجانبية والمدخلات
st.sidebar.header(t["sidebar_title"])
soil_type = st.sidebar.selectbox(t["soil_label"], t["soils"])
crop_type = st.sidebar.selectbox(t["crop_label"], t["crops"])
area = st.sidebar.number_input(t["area_label"], min_value=1.0, value=500.0, step=50.0)

# 7. عرض الملخص
st.subheader(t["summary_title"])
c1, c2, c3 = st.columns(3)
with c1:
    st.info(f"**{t['soil_info']}:** {soil_type.split('(')[0]}")
with c2:
    st.info(f"**{t['crop_info']}:** {crop_type.split('(')[0]}")
with c3:
    st.info(f"**{t['area_info']}:** {area:,} m²")

st.write("")

# 8. زر الحسابات والنتائج
if st.button(t["btn_label"]):
    soil_idx = t["soils"].index(soil_type)
    
    if soil_idx == 0: # رملية (12غ / م²)
        dose_g_m2 = 12.0
        water_saving_pct = 45
    elif soil_idx == 1: # طينية (6غ / م²)
        dose_g_m2 = 6.0
        water_saving_pct = 25
    else: # كلسية (8.5غ / م²)
        dose_g_m2 = 8.5
        water_saving_pct = 35

    total_kg = (dose_g_m2 * area) / 1000.0
    saved_liters = area * 8 * (water_saving_pct / 100.0)

    st.success(t["success_msg"])
    
    res1, res2, res3 = st.columns(3)
    unit_kg = "kg" if lang != "العربية" else "كغ"
    unit_l = "L" if lang != "العربية" else "لتر"

    with res1:
        st.metric(label=t["metric1"], value=f"{total_kg:.2f} {unit_kg}")
    with res2:
        st.metric(label=t["metric2"], value=f"{water_saving_pct}%")
    with res3:
        st.metric(label=t["metric3"], value=f"{int(saved_liters):,} {unit_l}")

    st.balloons()
    st.warning(t["recommendation"])

    # ملف التقرير النصي
    report_text = f"AgriOpuntia Field Report\nSoil: {soil_type}\nCrop: {crop_type}\nArea: {area} m2\nRequired Dose: {total_kg:.2f} kg\nWater Saved: {int(saved_liters):,} L"
    st.download_button(
        label=t["download_btn"],
        data=report_text,
        file_name=f"AgriOpuntia_Report_{int(area)}m2.txt",
        mime="text/plain"
    )

