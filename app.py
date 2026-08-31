import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد",
    page_icon="🌵",
    layout="wide"
)

# تنسيق CSS مخصص للواجهة مع هوية بصرية متناسقة (أخضر طبيعي، أبيض، ولمسات ترابية دافئة)
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1b4d3e 0%, #2e6f40 50%, #558b2f 100%);
        padding: 35px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(27, 77, 62, 0.15);
        border-bottom: 4px solid #d4a373;
    }
    .main-header h1 {
        color: white !important;
        font-size: 2.7rem;
        margin-bottom: 10px;
        font-weight: 700;
    }
    .main-header p {
        color: #f4f1ea !important;
        font-size: 1.25rem;
    }
    .stMetric {
        background-color: #f7f4ee;
        padding: 18px;
        border-radius: 12px;
        border-right: 5px solid #2e6f40;
        border-top: 1px solid #e3dec3;
        box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    }
    .stSidebar {
        background-color: #faf9f5;
    }
</style>
""", unsafe_allow_html=True)

# واجهة الهيدر البصرية
st.markdown("""
<div class="main-header">
    <h1>🌵 AgriOpuntia</h1>
    <p>المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد</p>
</div>
""", unsafe_allow_html=True)

# القائمة الجانبية للإعدادات واللغة
st.sidebar.title("⚙️ إعدادات الحقل والمزرعة / Farm Settings")
lang = st.sidebar.selectbox("Choose Language / اختر اللغة / Langue", ["العربية", "Français", "English"])

if lang == "العربية":
    crop_type = st.sidebar.selectbox("اختر المحصول الزراعي:", [
        "أشجار الزيتون", 
        "نخيل التمر", 
        "الحبوب (القمح والشعير)", 
        "الحمضيات (البرتقال والليمون)", 
        "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
        "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
    ])
    
    soil_type = st.sidebar.selectbox("نوع التربة (حسب نتائج تحليل التربة المخبري):", [
        "تربة رملية (Sandy)",
        "تربة لومية أو طينية سلتية (Loamy / Silt Loam)",
        "تربة طينية ثقيلة (Clay)",
        "تربة رملية طينية (Sandy Clay Loam)",
        "تربة غرينية طينية (Silty Clay Loam)"
    ])
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 مدخلات مساحة الحقل والاحتياجات")
    area = st.sidebar.number_input("مساحة الحقل المستهدف (بالمتر المربع م²):", min_value=100, value=5000, step=500)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 برنامج التسميد المخبري للمحصول")
    fertilizer_rate = st.sidebar.number_input("كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):", min_value=0.01, value=0.12, step=0.01)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🌵 دور الهيدروجيل الحيوي")
        with st.expander("اضغط لعرض تفاصيل التقنية"):
            st.markdown("""
            <div dir="rtl" style="text-align: right; line-height: 1.8;">
            <b>• المصدر الطبيعي:</b><br>
            مستخلص من ألواح صبار التين الشوكي<br>
            <span dir="ltr" style="display: inline-block; color: #2e6f40; font-weight: bold;">(Opuntia ficus-indica)</span><br><br>
            <b>• الوظيفة الحقلية:</b><br>
            تشكيل شبكة هلامية مجهرية حول جذور النبات لتحْبِس مياه الري والأسمدة وتمنع ترشيحها عميقاً
            </div>
            """, unsafe_allow_html=True)
        
    with col2:
        st.info(f"🌿 تخصيص المحصول ({crop_type.split()[0]})")
        with st.expander("اضغط لعرض تفاصيل الاحتياجات"):
            st.markdown(f"""
            <div dir="rtl" style="text-align: right; line-height: 1.8;">
            <b>• المحصول المدروس:</b><br>
            {crop_type}<br><br>
            <b>• طبيعة التربة:</b><br>
            {soil_type}<br><br>
            <b>• التسميد المحسوب:</b><br>
            يحتاج الحقل إجمالاً إلى <b>{total_crop_fertilizer_kg:.1f} كغ</b> من الأسمدة لتغطية احتياجات المساحة المدروسة
            </div>
            """, unsafe_allow_html=True)
        
    with col3:
        st.info("💧 كفاءة الري والتوفير")
        with st.expander("اضغط لعرض أثر توفير المياه"):
            st.markdown("""
            <div dir="rtl" style="text-align: right; line-height: 1.8;">
            <b>• نسبة توفير المياه:</b><br>
            تقليص عدد مرات السقي بنسبة تصل إلى 40%<br><br>
            <b>• مقاومة الجفاف:</b><br>
            حماية المحاصيل من صدمات الإجهاد المائي في الأوقات الحارة
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <h2 style="direction: rtl; text-align: right; color: #1b4d3e;">📊 لوحة القيادة الفلاحية لتطبيق التقنية على: {crop_type}</h2>
    """, unsafe_allow_html=True)

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("الهيدروجيل المقترح", f"{hydrogel_needed_kg:.1f} كغ")
    mcol2.metric("إجمالي أسمدة الحقل", f"{total_crop_fertilizer_kg:.1f} كغ")
    mcol3.metric("المياه الموفّرة للحقل", f"{water_saved_m3:.1f} م³")

    st.markdown("---")
    st.subheader("📑 الملخص التقني والفلاحي للمزرعة")
    st.markdown(f"""
    <div dir="rtl" style="text-align: right; line-height: 1.8;">
    - <b>المساحة الكلية المستهدفة:</b> {area:,.0f} متر مربع<br>
    - <b>نوع التربة المحددة من التحاليل:</b> {soil_type}<br>
    - <b>الاحتياج الإجمالي من الهيدروجيل الحيوي:</b> {hydrogel_needed_kg:.1f} كيلوغرام لحماية الجذور<br>
    - <b>الاحتياج الإجمالي من الأسمدة:</b> {total_crop_fertilizer_kg:.1f} كيلوغرام لضمان التغذية المثلى للمحصول
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f7f4ee; padding: 18px; border-radius: 10px; border-right: 5px solid #d4a373; direction: rtl; text-align: right; color: #2c4c3b; margin-top: 15px;">
        <b>💡 إرشادات وتوصيات تطبيقية ميدانية:</b>
        <ul style="margin-top: 10px; padding-right: 20px; line-height: 1.8;">
            <li><b>عمق تطبيق الهيدروجيل:</b> يُنصح بوضع الهيدروجيل على عمق 20 إلى 30 سم تحت سطح التربة (مباشرة في منطقة انتشار الجذور الفعالة)</li>
            <li><b>نصائح التسميد:</b> يُفضل تقسيم كمية الأسمدة المحسوبة على دفعات طوال الموسم الزراعي لتعزيز كفاءة الامتصاص وتقليل الضياع</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif lang == "Français":
    crop_type = st.sidebar.selectbox("Sélectionner la culture :", [
        "Olivier", 
        "Palmier dattier", 
        "Céréales (Blé et Orge)", 
        "Agrumes (Oranges et Citrons)", 
        "Légumineuses sèches (Fèves, Pois chiches)", 
        "Légumes sous irrigation localisée (Tomates, Pommes de terre)"
    ])
    
    soil_type = st.sidebar.selectbox("Type de sol (selon l'analyse de laboratoire) :", [
        "Sol sableux (Sandy)",
        "Sol limoneux (Loamy / Silt Loam)",
        "Sol argileux lourd (Clay)",
        "Sol sablo-argileux (Sandy Clay Loam)",
        "Sol limo-argileux (Silty Clay Loam)"
    ])
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Paramètres de superficie et besoins")
    area = st.sidebar.number_input("Superficie du champ ciblé (en m²) :", min_value=100, value=5000, step=500)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 Programme de fertilisation")
    fertilizer_rate = st.sidebar.number_input("Taux d'engrais recommandé par m² (kg/m²) :", min_value=0.01, value=0.12, step=0.01)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🌵 Rôle du bio-hydrogel")
        with st.expander("Afficher les détails"):
            st.write("""
            - Source : Extrait naturel de cladodes de figuier de Barbarie (Opuntia ficus-indica)
            - Fonction : Crée un réseau gélatineux autour des racines pour retenir l'eau et les nutriments
            """)
        
    with col2:
        st.info(f"🌿 Culture ({crop_type.split()[0]})")
        with st.expander("Afficher les détails"):
            st.write(f"""
            - Culture : {crop_type}
            - Sol : {soil_type}
            - Fertilisant total : {total_crop_fertilizer_kg:.1f} kg requis pour la surface
            """)
        
    with col3:
        st.info("💧 Économie d'eau")
        with st.expander("Afficher l'impact"):
            st.write("""
            - Économie : Réduction de l'irrigation jusqu'à 40%
            - Résistance : Protection contre le stress hydrique
            """)

    st.markdown("---")
    st.header(f"📊 Tableau de bord pour : {crop_type}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Hydrogel suggéré", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Engrais total du champ", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Eau économisée", f"{water_saved_m3:.1f} m³")

    st.markdown("---")
    st.subheader("📑 Résumé technique")
    st.write(f"- Superficie ciblée : {area:,.0f} m²")
    st.write(f"- Type de sol : {soil_type}")
    st.write(f"- Besoin total en bio-hydrogel : {hydrogel_needed_kg:.1f} kg")
    st.write(f"- Besoin total en engrais : {total_crop_fertilizer_kg:.1f} kg")
    
    st.success("""
    💡 Conseils et recommandations pratiques :
    - Profondeur de l'hydrogel : Placer l'hydrogel à 20-30 cm sous la surface (zone racinaire active)
    - Conseils de fertilisation : Fractionner la quantité d'engrais tout au long de la saison
    """)

else:
    crop_type = st.sidebar.selectbox("Select Crop Type:", [
        "Olive Trees", 
        "Date Palm Trees", 
        "Cereals (Wheat and Barley)", 
        "Citrus (Oranges and Lemons)", 
        "Dry Legumes (Fava beans, Chickpeas)", 
        "Vegetables under Localized Irrigation (Tomatoes, Potatoes)"
    ])
    
    soil_type = st.sidebar.selectbox("Soil Type (Lab Analysis Results):", [
        "Sandy Soil",
        "Loamy / Silt Loam Soil",
        "Clay Soil",
        "Sandy Clay Loam Soil",
        "Silty Clay Loam Soil"
    ])
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Field Area & Requirements")
    area = st.sidebar.number_input("Target Field Area (in m²):", min_value=100, value=5000, step=500)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 Fertilization Program")
    fertilizer_rate = st.sidebar.number_input("Recommended Fertilizer Rate per m² (kg/m²):", min_value=0.01, value=0.12, step=0.01)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🌵 Bio-Hydrogel Role")
        with st.expander("View Details"):
            st.write("""
            - Source: Natural extract from cactus cladodes (Opuntia ficus-indica)
            - Function: Creates a microscopic gel network around roots to retain water and nutrients
            """)
        
    with col2:
        st.info(f"🌿 Crop Customization ({crop_type.split()[0]})")
        with st.expander("View Details"):
            st.write(f"""
            - Crop: {crop_type}
            - Soil: {soil_type}
            - Calculated Fertilizer: {total_crop_fertilizer_kg:.1f} kg needed for the area
            """)
        
    with col3:
        st.info("💧 Water Efficiency")
        with st.expander("View Impact"):
            st.write("""
            - Water Saving: Cuts irrigation frequency by up to 40%
            - Resilience: Protects crops from water stress shocks
            """)

    st.markdown("---")
    st.header(f"📊 Agricultural Dashboard for: {crop_type}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Suggested Hydrogel", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Total Field Fertilizer", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Saved Water", f"{water_saved_m3:.1f} m³")

    st.markdown("---")
    st.subheader("📑 Technical & Agronomic Summary")
    st.write(f"- Target Area: {area:,.0f} m²")
    st.write(f"- Soil Type: {soil_type}")
    st.write(f"- Total Bio-Hydrogel Requirement: {hydrogel_needed_kg:.1f} kg")
    st.write(f"- Total Fertilizer Requirement: {total_crop_fertilizer_kg:.1f} kg")
    
    st.success("""
    💡 Practical Field Guidelines & Recommendations:
    - Hydrogel Depth: Apply hydrogel at a depth of 20 to 30 cm within the active root zone
    - Fertilization Advice: Split the fertilizer amount into multiple doses throughout the growing season
    """)























