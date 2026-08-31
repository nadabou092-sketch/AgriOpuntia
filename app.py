import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد",
    page_icon="🌵",
    layout="wide"
)

# القائمة الجانبية للإعدادات واللغة (ثلاث لغات: العربية، الفرنسية، الإنجليزية)
st.sidebar.title("⚙️ إعدادات الحقل والمزرعة / Farm Settings")
lang = st.sidebar.selectbox("Choose Language / اختر اللغة / Langue", ["العربية", "Français", "English"])

if lang == "العربية":
    st.title("🌵 AgriOpuntia")
    st.subheader("المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد")
    
    crop_type = st.sidebar.selectbox("اختر المحصول الزراعي:", [
        "أشجار الزيتون (المناطق السهبية والشمالية)", 
        "نخيل التمر (المنطقة الجنوبية والولايات الواحية)", 
        "الحبوب (القمح والشعير - مناطق الهضاب العليا والسهوب)", 
        "الحمضيات (البرتقال والليمون - الشلف والسهل الساحلي)", 
        "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
        "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
    ])
    
    soil_type = st.sidebar.selectbox("نوع التربة (حسب نتائج تحليل التربة المخبري):", [
        "تربة رملية (Sandy) - نفاذية عالية جداً وحاجة قصوى للهيدروجيل",
        "تربة لومية أو طينية سلتية (Loamy / Silt Loam) - متوازنة",
        "تربة طينية ثقيلة (Clay) - احتفاظ عالي بالماء وتماسك",
        "تربة رملية طينية (Sandy Clay Loam) - متوسطة النفاذية",
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
            st.write("""
            - **المصدر:** مستخلص طبيعي من ألواح صبار التين الشوكي (*Opuntia ficus-indica*)
            - **الوظيفة الحقلية:** يشكل شبكة هلامية مجهرية حول جذور النبات لتحْبِس مياه الري والأسمدة وتمنع ترشيحها عميقاً
            """)
        
    with col2:
        st.info(f"🌿 تخصيص المحصول ({crop_type.split()[0]})")
        with st.expander("اضغط لعرض تفاصيل الاحتياجات"):
            st.write(f"""
            - **المحصول:** {crop_type}
            - **طبيعة التربة:** {soil_type}
            - **التسميد المحسوب:** يحتاج الحقل إجمالاً إلى **{total_crop_fertilizer_kg:.1f} كغ** من الأسمدة لتغطية احتياجات المساحة المدروسة
            """)
        
    with col3:
        st.info("💧 كفاءة الري والتوفير")
        with st.expander("اضغط لعرض أثر توفير المياه"):
            st.write("""
            - **نسبة توفير المياه:** تقليص عدد مرات السقي بنسبة تصل إلى 40%
            - **مقاومة الجفاف:** حماية المحاصيل من صدمات الإجهاد المائي في الأوقات الحارة
            """)

    st.markdown("---")
    st.header(f"📊 لوحة القيادة الفلاحية لتطبيق التقنية على: {crop_type.split()[0]}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("الهيدروجيل المقترح", f"{hydrogel_needed_kg:.1f} كغ")
    mcol2.metric("إجمالي أسمدة الحقل", f"{total_crop_fertilizer_kg:.1f} كغ")
    mcol3.metric("المياه الموفّرة للحقل", f"{water_saved_m3:.1f} م³")

    st.markdown("---")
    st.subheader("📑 الملخص التقني والفلاحي للمزرعة")
    st.write(f"- **المساحة الكلية المستهدفة:** {area:,.0f} متر مربع")
    st.write(f"- **نوع التربة المحددة من التحاليل:** {soil_type}")
    st.write(f"- **الاحتياج الإجمالي من الهيدروجيل الحيوي:** {hydrogel_needed_kg:.1f} كيلوغرام لحماية الجذور")
    st.write(f"- **الاحتياج الإجمالي من الأسمدة:** {total_crop_fertilizer_kg:.1f} كيلوغرام لضمان التغذية المثلى للمحصول")
    
    # إزالة النقاط من نهاية الجمل في التوصيات
    st.markdown("""
    <div style="background-color: #d1e7dd; padding: 15px; border-radius: 8px; border-right: 5px solid #0f5132; direction: rtl; text-align: right; color: #0f5132;">
        <b>💡 إرشادات وتوصيات تطبيقية ميدانية:</b>
        <ul style="margin-top: 10px; padding-right: 20px;">
            <li><b>عمق تطبيق الهيدروجيل:</b> يُنصح بوضع الهيدروجيل على عمق 20 إلى 30 سم تحت سطح التربة (مباشرة في منطقة انتشار الجذور الفعالة)</li>
            <li><b>نصائح التسميد:</b> يُفضل تقسيم كمية الأسمدة المحسوبة على دفعات طوال الموسم الزراعي لتعزيز كفاءة الامتصاص وتقليل الضياع</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif lang == "Français":
    st.title("🌵 AgriOpuntia")
    st.subheader("Plateforme intelligente d'application de bio-hydrogel et de calcul de fertilisation")
    
    crop_type = st.sidebar.selectbox("Sélectionner la culture :", [
        "Olivier (Régions steppiques et du Nord)", 
        "Palmier dattier (Régions du Sud et oasiennes)", 
        "Céréales (Blé et Orge - Hauts Plateaux et Steppes)", 
        "Agrumes (Oranges et Citrons - Chlef et Littoral)", 
        "Légumineuses sèches (Fèves, Pois chiches, Petits pois)", 
        "Légumes sous irrigation localisée (Tomates, Pommes de terre)"
    ])
    
    soil_type = st.sidebar.selectbox("Type de sol (selon l'analyse de laboratoire) :", [
        "Sol sableux (Sandy) - Forte perméabilité et besoin maximal en hydrogel",
        "Sol limoneux (Loamy / Silt Loam) - Équilibré",
        "Sol argileux lourd (Clay) - Haute rétention d'eau",
        "Sol sablo-argileux (Sandy Clay Loam) - Perméabilité moyenne",
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
            - **Source :** Extrait naturel de cladodes de figuier de Barbarie
            - **Fonction :** Crée un réseau gélatineux autour des racines pour retenir l'eau et les nutriments
            """)
        
    with col2:
        st.info(f"🌿 Culture ({crop_type.split()[0]})")
        with st.expander("Afficher les détails"):
            st.write(f"""
            - **Culture :** {crop_type}
            - **Sol :** {soil_type}
            - **Fertilisant total :** **{total_crop_fertilizer_kg:.1f} kg** requis pour la surface
            """)
        
    with col3:
        st.info("💧 Économie d'eau")
        with st.expander("Afficher l'impact"):
            st.write("""
            - **Économie :** Réduction de l'irrigation jusqu'à 40%
            - **Résistance :** Protection contre le stress hydrique
            """)

    st.markdown("---")
    st.header(f"📊 Tableau de bord pour : {crop_type.split()[0]}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Hydrogel suggéré", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Engrais total du champ", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Eau économisée", f"{water_saved_m3:.1f} m³")

    st.markdown("---")
    st.subheader("📑 Résumé technique")
    st.write(f"- **Superficie ciblée :** {area:,.0f} m²")
    st.write(f"- **Type de sol :** {soil_type}")
    st.write(f"- **Besoin total en bio-hydrogel :** {hydrogel_needed_kg:.1f} kg")
    st.write(f"- **Besoin total en engrais :** {total_crop_fertilizer_kg:.1f} kg")
    
    st.success("""
    💡 **Conseils et recommandations pratiques :**
    - **Profondeur de l'hydrogel :** Il est recommandé de placer l'hydrogel à une profondeur de 20 à 30 cm sous la surface (zone active des racines)
    - **Conseils de fertilisation :** Il est conseillé de fractionner la quantité d'engrais tout au long de la saison pour optimiser l'absorption
    """)

else:
    st.title("🌵 AgriOpuntia")
    st.subheader("Smart Platform for Bio-Hydrogel Application & Fertilization Calculation")
    
    crop_type = st.sidebar.selectbox("Select Crop Type:", [
        "Olive Trees (Steppe and Northern Regions)", 
        "Date Palm Trees (Southern and Oasis Regions)", 
        "Cereals (Wheat and Barley - High Plateaus and Steppes)", 
        "Citrus (Oranges and Lemons - Chlef and Coastal Plains)", 
        "Dry Legumes (Fava beans, Chickpeas, Peas)", 
        "Vegetables under Localized Irrigation (Tomatoes, Potatoes)"
    ])
    
    soil_type = st.sidebar.selectbox("Soil Type (Lab Analysis Results):", [
        "Sandy Soil - Very high permeability & maximum hydrogel need",
        "Loamy / Silt Loam Soil - Balanced",
        "Clay Soil - High water retention",
        "Sandy Clay Loam Soil - Medium permeability",
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
            - **Source:** Natural extract from cactus cladodes (*Opuntia ficus-indica*)
            - **Function:** Creates a microscopic gel network around roots to retain water and nutrients
            """)
        
    with col2:
        st.info(f"🌿 Crop Customization ({crop_type.split()[0]})")
        with st.expander("View Details"):
            st.write(f"""
            - **Crop:** {crop_type}
            - **Soil:** {soil_type}
            - **Calculated Fertilizer:** Total of **{total_crop_fertilizer_kg:.1f} kg** needed for the area
            """)
        
    with col3:
        st.info("💧 Water Efficiency")
        with st.expander("View Impact"):
            st.write("""
            - **Water Saving:** Cuts irrigation frequency by up to 40%
            - **Drought Resilience:** Protects crops from water stress shocks
            """)

    st.markdown("---")
    st.header(f"📊 Agricultural Dashboard for: {crop_type.split()[0]}")

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Suggested Hydrogel", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Total Field Fertilizer", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Saved Water", f"{water_saved_m3:.1f} m³")

    st.markdown("---")
    st.subheader("📑 Technical & Agronomic Summary")
    st.write(f"- **Target Area:** {area:,.0f} m²")
    st.write(f"- **Soil Type:** {soil_type}")
    st.write(f"- **Total Bio-Hydrogel Requirement:** {hydrogel_needed_kg:.1f} kg")
    st.write(f"- **Total Fertilizer Requirement:** {total_crop_fertilizer_kg:.1f} kg")
    
    st.success("""
    💡 **Practical Field Guidelines & Recommendations:**
    - **Hydrogel Depth:** Apply the hydrogel at a depth of 20 to 30 cm below the soil surface within the active root zone
    - **Fertilization Advice:** Split the calculated fertilizer amount into multiple doses throughout the growing season to enhance uptake
    """)






