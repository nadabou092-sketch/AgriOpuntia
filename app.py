import streamlit as st
import pandas as pd

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد",
    page_icon="🌵",
    layout="wide"
)

# تنسيق CSS مخصص للواجهة مع دعم الاتجاهات (RTL / LTR)
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1b4d3e 0%, #2e6f40 50%, #558b2f 100%);
        padding: 30px;
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
        margin-bottom: 5px;
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
        border-top: 1px solid #e3dec3;
        box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

# واجهة الهيدر البصرية
st.markdown("""
<div class="main-header">
    <h1>AgriOpuntia</h1>
    <p>المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد | Smart Platform for Bio-Hydrogel & Fertilization</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# القائمة الجانبية للإعدادات واللغة
st.sidebar.title("⚙️ إعدادات الحقل / Farm Settings")
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
    
    climate_zone = st.sidebar.selectbox("المنطقة المناخية للمزرعة:", [
        "مناخ شبه جاف / جاف (حار صيفاً ومتقلب)",
        "مناخ صحراوي جاف جداً (شديد الحرارة وقليل الأمطار)",
        "مناخ ساحلي / معتدل (رطوبة نسبية ومعتدل الحرارة)"
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
            <b>• المصدر الطبيعي:</b> مستخلص من ألواح صبار التين الشوكي (Opuntia ficus-indica)<br><br>
            <b>• الوظيفة الحقلية:</b> تشكيل شبكة هلامية مجهرية حول جذور النبات لتحْبِس مياه الري والأسمدة وتمنع ترشيحها عميقاً.
            </div>
            """, unsafe_allow_html=True)
        
    with col2:
        st.info(f"🌿 تخصيص المحصول")
        with st.expander("اضغط لعرض تفاصيل الاحتياجات"):
            st.markdown(f"""
            <div dir="rtl" style="text-align: right; line-height: 1.8;">
            <b>• المحصول المدروس:</b> {crop_type}<br><br>
            <b>• طبيعة التربة:</b> {soil_type}<br><br>
            <b>• التسميد المحسوب:</b> يحتاج الحقل إجمالاً إلى <b>{total_crop_fertilizer_kg:.1f} كغ</b> من الأسمدة.
            </div>
            """, unsafe_allow_html=True)
        
    with col3:
        st.info("💧 كفاءة الري والتوفير")
        with st.expander("اضغط لعرض أثر توفير المياه"):
            st.markdown("""
            <div dir="rtl" style="text-align: right; line-height: 1.8;">
            <b>• نسبة توفير المياه:</b> تقليص عدد مرات السقي بنسبة تصل إلى 40%<br><br>
            <b>• مقاومة الجفاف:</b> حماية المحاصيل من صدمات الإجهاد المائي.
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
    st.subheader("🌤️ التوصيات الذكية حسب المناخ والمنطقة")
    if "صحراوي" in climate_zone:
        st.warning("⚠️ **توصية للمناخ الصحراوي:** نظراً لشدة التبخر، يُنصح بزيادة عمق وضع الهيدروجيل إلى 35 سم واعتماد نظام سقي قطرات دقيق ومكثف في ذروة الصيف.")
    elif "شبه جاف" in climate_zone:
        st.info("💡 **توصية للمناخ الشبه جاف:** الهيدروجيل سيقلل بوضوح من صدمة الجفاف بين فترات المطر، مع إمكانية تقليص جدول الري بـ 35%.")
    else:
        st.success("🌱 **توصية للمناخ الساحلي/المعتدل:** الرطوبة النسبية مساعدة، والهيدروجيل سيمنع غسل العناصر الغذائية نحو الأسفل بسبب مياه الأمطار الزائدة.")

    st.markdown("---")
    st.subheader("📅 الجدول الزمني المقترح لسقي ومتابعة المحصول")
    timeline_data = pd.DataFrame({
        "مرحلة نمو المحصول (Crop Stage)": ["مرحلة الغرس / البداية", "مرحلة النمو الخضري", "مرحلة الإزهار والعقد", "مرحلة النضج والجني"],
        "تأثير الهيدروجيل الحيوي (Bio-Hydrogel Effect)": ["حماية الجذور الفتية وتثبيت الرطوبة الأولية", "إمداد متواصل ومستقر بالمياه والأسمدة", "الحماية من صدمات العطش والإجهاد الحراري", "تقليل تدريجي للرطوبة لتحسين جودة المحصول"],
        "تواتر الري (Irrigation Interval)": ["عادي مع تقليل الفترات بـ 20%", "تخفيض الفترات بـ 40%", "تخفيض الفترات بـ 35%", "ري خفيف عند الضرورة"]
    })
    st.table(timeline_data)

    st.markdown("---")
    st.subheader("📑 الملخص التقني والفلاحي للمزرعة وتحميل التقرير")
    st.markdown(f"""
    <div dir="rtl" style="text-align: right; line-height: 1.8;">
    - <b>المساحة الكلية المستهدفة:</b> {area:,.0f} متر مربع<br>
    - <b>المنطقة المناخية:</b> {climate_zone}<br>
    - <b>نوع التربة المحددة من التحاليل:</b> {soil_type}<br>
    - <b>الاحتياج الإجمالي من الهيدروجيل الحيوي:</b> {hydrogel_needed_kg:.1f} كيلوغرام لحماية الجذور<br>
    - <b>الاحتياج الإجمالي من الأسمدة:</b> {total_crop_fertilizer_kg:.1f} كيلوغرام لضمان التغذية المثلى للمحصول
    </div>
    """, unsafe_allow_html=True)
    
    # زر تحميل التقرير كملف نصي CSV/TXT
    report_content = f"""AgriOpuntia Technical Report
------------------------------------
Crop Type: {crop_type}
Target Area: {area} m²
Climate Zone: {climate_zone}
Soil Type: {soil_type}
Bio-Hydrogel Needed: {hydrogel_needed_kg:.1f} kg
Total Fertilizer Needed: {total_crop_fertilizer_kg:.1f} kg
Estimated Water Saved: {water_saved_m3:.1f} m³
------------------------------------
Generated via AgriOpuntia Smart Platform.
"""
    st.download_button(
        label="📥 تحميل التقرير التقني للمزرعة (Download Report)",
        data=report_content,
        file_name="AgriOpuntia_Field_Report.txt",
        mime="text/plain"
    )

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
    
    climate_zone = st.sidebar.selectbox("Zone climatique de l'exploitation :", [
        "Climat semi-aride / aride (Chaud en été)",
        "Climat saharien très aride (Chaleur extrême, faible pluviosité)",
        "Climat côtier / tempéré (Humidité relative, tempéré)"
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
            - **Source naturelle :** Extrait des cladodes de figuier de Barbarie (Opuntia ficus-indica).
            - **Fonction au champ :** Crée un réseau gélatineux microscopique autour des racines pour retenir l'eau et les nutriments.
            """)
        
    with col2:
        st.info(f"🌿 Culture ({crop_type})")
        with st.expander("Afficher les détails"):
            st.write(f"""
            - **Culture étudiée :** {crop_type}
            - **Type de sol :** {soil_type}
            - **Fertilisant total requis :** {total_crop_fertilizer_kg:.1f} kg pour la surface spécifiée.
            """)
        
    with col3:
        st.info("💧 Efficacité de l'irrigation")
        with st.expander("Afficher l'impact"):
            st.write("""
            - **Économie d'eau :** Réduction de la fréquence d'arrosage jusqu'à 40%.
            - **Résistance à la sécheresse :** Protection contre le stress hydrique en périodes chaudes.
            """)

    st.markdown("---")
    st.header(f"📊 Tableau de bord agronomique pour : {crop_type}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Hydrogel suggéré", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Engrais total du champ", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Eau économisée", f"{water_saved_m3:.1f} m³")

    st.markdown("---")
    st.subheader("🌤️ Recommandations climatiques adaptées")
    if "saharien" in climate_zone:
        st.warning("⚠️ **Recommandation climat saharien :** En raison de l'évaporation intense, enterrez l'hydrogel à 35 cm de profondeur et optimisez le goutte-à-goutte.")
    elif "semi-aride" in climate_zone:
        st.info("💡 **Recommandation climat semi-aride :** Réduit considérablement le stress hydrique entre les pluies, permettant d'espacer les irrigations de 35%.")
    else:
        st.success("🌱 **Recommandation climat tempéré :** L'hydrogel prévient le lixiviation des nutriments en cas d'excès d'eau de pluie.")

    st.markdown("---")
    st.subheader("📅 Calendrier d'irrigation et de suivi suggéré")
    timeline_data = pd.DataFrame({
        "Stade de la culture": ["Plantation / Établissement", "Croissance végétative", "Floraison et nouaison", "Maturation et récolte"],
        "Effet du Bio-Hydrogel": ["Protection des jeunes racines et rétention initiale", "Approvisionnement continu en eau et nutriments", "Bouclier contre le stress thermique", "Diminution progressive pour la qualité du fruit"],
        "Fréquence d'irrigation": ["Normale (réduction de 20%)", "Réduction de 40%", "Réduction de 35%", "Irrigation légère si nécessaire"]
    })
    st.table(timeline_data)

    st.markdown("---")
    st.subheader("📑 Résumé technique et téléchargement du rapport")
    st.write(f"- **Superficie ciblée :** {area:,.0f} m²")
    st.write(f"- **Zone climatique :** {climate_zone}")
    st.write(f"- **Type de sol :** {soil_type}")
    st.write(f"- **Besoin total en bio-hydrogel :** {hydrogel_needed_kg:.1f} kg")
    st.write(f"- **Besoin total en engrais :** {total_crop_fertilizer_kg:.1f} kg")
    
    report_content = f"""AgriOpuntia Technical Report
------------------------------------
Crop Type: {crop_type}
Target Area: {area} m²
Climate Zone: {climate_zone}
Soil Type: {soil_type}
Bio-Hydrogel Needed: {hydrogel_needed_kg:.1f} kg
Total Fertilizer Needed: {total_crop_fertilizer_kg:.1f} kg
Estimated Water Saved: {water_saved_m3:.1f} m³
------------------------------------
Generated via AgriOpuntia Smart Platform.
"""
    st.download_button(
        label="📥 Download Field Technical Report",
        data=report_content,
        file_name="AgriOpuntia_Field_Report.txt",
        mime="text/plain"
    )

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
    
    climate_zone = st.sidebar.selectbox("Farm Climate Zone:", [
        "Semi-arid / Arid climate (Hot summers)",
        "Desert / Hyper-arid climate (Extreme heat, low rainfall)",
        "Coastal / Temperate climate (Moderate humidity)"
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
            - **Natural Source:** Extracted from cactus cladodes (Opuntia ficus-indica).
            - **Field Function:** Creates a microscopic gel network around roots to retain water and nutrients.
            """)
        
    with col2:
        st.info(f"🌿 Crop Customization ({crop_type})")
        with st.expander("View Details"):
            st.write(f"""
            - **Studied Crop:** {crop_type}
            - **Soil Type:** {soil_type}
            - **Total Fertilizer:** {total_crop_fertilizer_kg:.1f} kg required for the area.
            """)
        
    with col3:
        st.info("💧 Water Efficiency")
        with st.expander("View Impact"):
            st.write("""
            - **Water Saving:** Cuts irrigation frequency by up to 40%.
            - **Resilience:** Protects crops from water stress during hot periods.
            """)

    st.markdown("---")
    st.header(f"📊 Agricultural Dashboard for: {crop_type}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Suggested Hydrogel", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Total Field Fertilizer", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Saved Water", f"{water_saved_m3:.1f} m³")

    st.markdown("---")
    st.subheader("🌤️ Climate-Based Recommendations")
    if "Desert" in climate_zone:
        st.warning("⚠️ **Desert Climate Recommendation:** Due to high evaporation, bury the hydrogel 35 cm deep and use precise drip irrigation.")
    elif "Semi-arid" in climate_zone:
        st.info("💡 **Semi-Arid Climate Recommendation:** Effectively mitigates drought shocks between rainfalls, cutting irrigation frequency by 35%.")
    else:
        st.success("🌱 **Temperate Climate Recommendation:** Hydrogel prevents nutrient leaching caused by excess rainfall.")

    st.markdown("---")
    st.subheader("📅 Suggested Irrigation & Monitoring Timeline")
    timeline_data = pd.DataFrame({
        "Crop Growth Stage": ["Planting / Establishment", "Vegetative Growth", "Flowering & Fruit Set", "Maturation & Harvest"],
        "Bio-Hydrogel Effect": ["Protects young roots & retains initial moisture", "Provides steady water & nutrient supply", "Acts as a shield against heat stress", "Gradually reduces moisture for fruit quality"],
        "Irrigation Frequency": ["Normal (20% reduced intervals)", "40% reduced intervals", "35% reduced intervals", "Light irrigation as needed"]
    })
    st.table(timeline_data)

    st.markdown("---")
    st.subheader("📑 Technical & Agronomic Summary & Report Download")
    st.write(f"- **Target Area:** {area:,.0f} m²")
    st.write(f"- **Climate Zone:** {climate_zone}")
    st.write(f"- **Soil Type:** {soil_type}")
    st.write(f"- **Total Bio-Hydrogel Requirement:** {hydrogel_needed_kg:.1f} kg")
    st.write(f"- **Total Fertilizer Requirement:** {total_crop_fertilizer_kg:.1f} kg")
    
    report_content = f"""AgriOpuntia Technical Report
------------------------------------
Crop Type: {crop_type}
Target Area: {area} m²
Climate Zone: {climate_zone}
Soil Type: {soil_type}
Bio-Hydrogel Needed: {hydrogel_needed_kg:.1f} kg
Total Fertilizer Needed: {total_crop_fertilizer_kg:.1f} kg
Estimated Water Saved: {water_saved_m3:.1f} m³
------------------------------------
Generated via AgriOpuntia Smart Platform.
"""
    st.download_button(
        label="📥 Download Field Technical Report",
        data=report_content,
        file_name="AgriOpuntia_Field_Report.txt",
        mime="text/plain"
    )

























