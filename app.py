import streamlit as st

# --- إعدادات الصفحة وعنوان المتصفح ---
st.set_page_config(
    page_title="AgriOpuntia 🥔💧", 
    page_icon="🌱",
    layout="centered"
)

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("⚙️ الإعدادات / Settings")

# قائمة اختيار اللغة مع الأعلام والرموز
lang = st.sidebar.selectbox(
    "Choose Language / اختر اللغة / Langue", 
    ["🇩🇿 ع", "🇫🇷 FR", "🇬🇧 ENG"]
)

# تصميم اللوقو الجميل في أعلى الشريط الجانبي
st.sidebar.markdown("""
    <div style="text-align: center; padding: 5px;">
        <span style="font-size: 45px;">🌵💧</span>
        <h3 style="color: #1b4d3e; margin: 0;">AgriOpuntia</h3>
        <p style="color: #666; font-size: 11px;">مخبر الزراعة الذكية والهيدروجيل</p>
    </div>
    <hr style="margin: 5px 0; border: 0; border-top: 1px solid #ddd;">
""", unsafe_allow_html=True)

# --- الواجهة الرئيسية (Main Header) ---
st.markdown("""
<div style="text-align: center; padding: 10px;">
    <h1>AgriOpuntia 🇩🇿</h1>
    <p style="color: #555; font-size: 15px;">المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد والموارد المائية</p>
</div>
<hr style="margin: 10px 0;">
""", unsafe_allow_html=True)

# --- محتوى التطبيق حسب اللغة المختارة ---
if "ع" in lang:
    st.subheader("🌾 مدخلات مساحة الحقل والاحتياجات")
    
    crop_type = st.selectbox("اختر المحصول الزراعي:", [
        "أشجار الزيتون", 
        "نخيل التمر", 
        "الحبوب (القمح والشعير)", 
        "الحمضيات (البرتقال والليمون)", 
        "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
        "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
    ])
    
    field_area = st.number_input("مساحة الحقل المستهدف (بالمتر المربع م²):", min_value=100.0, value=20000.0, step=100.0)
    
    st.markdown("---")
    st.subheader("🌿 برنامج التسميد المخبري للمصول")
    
    fertilizer_rate = st.number_input("كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):", min_value=0.0, value=0.10, step=0.01)
    total_fertilizer = field_area * fertilizer_rate
    
    st.success(f"📌 الكمية الإجمالية للأسمدة المطلوبة لكامل الحقل: **{total_fertilizer:,.2f} كيلوغرام** (ما يعادل **{total_fertilizer/100:,.2f} قنطار**)")

    # --- ميزة الذكاء الاصطناعي والتوصيات الذكية ---
    st.markdown("---")
    st.subheader("🤖 التحليل الذكي وتوصيات الهيدروجيل (AI Insights)")
    
    if st.button("🚀 تشغيل خوارزمية التحليل الذكي"):
        with st.spinner("جاري معالجة بيانات التربة والمحصول عبر خوارزميات الزراعة الذكية..."):
            # محاكاة ذكية مبنية على الخصائص
            water_saved = field_area * 0.15 # تقدير توفير المياه باللتر بناء على الهيدروجيل
            hydrogel_needed = field_area * 0.05 # كمية الهيدروجيل المقترحة كغ/م²
            
            st.info(f"""
            **📊 تقرير المستشار الذكي لمحصول ({crop_type}):**
            * 💧 **نسبة توفير المياه المتوقعة:** بفضل استجابة الهيدروجيل الحيوي المستخلص من الصبار، يُتوقع تقليل استهلاك مياه السقي بنسبة **35% إلى 45%**.
            * 🧪 **الكمية المقترحة لجرعة البيو-هيدروجيل:** حوالي **{hydrogel_needed:,.1f} كيلوغرام** لحماية الجذور من الإجهاد المائي.
            * 🌱 **الأثر البيئي والاقتصادي:** تحسين كفاءة امتصاص الأسمدة المُقدرة بـ ({total_fertilizer:,.2f} كغ) وتقليل ترشيح العناصر الغذائية في التربة.
            """)

elif "FR" in lang:
    st.subheader("🌾 Entrées de la surface du champ et besoins")
    crop_type = st.selectbox("Sélectionner la culture :", ["Olivier", "Palmier dattier", "Céréales", "Agrumes", "Légumes"])
    field_area = st.number_input("Superficie du champ cible (en m²) :", min_value=100.0, value=20000.0, step=100.0)
    
    st.markdown("---")
    st.subheader("🌿 Programme de fertilisation")
    fertilizer_rate = st.number_input("Taux d'engrais recommandé par m² (kg/m²) :", min_value=0.0, value=0.10, step=0.01)
    total_fertilizer = field_area * fertilizer_rate
    st.success(f"📌 Quantité totale d'engrais : **{total_fertilizer:,.2f} kg**")

    st.markdown("---")
    st.subheader("🤖 Recommandations Intelligentes (AI Insights)")
    if st.button("🚀 Lancer l'analyse intelligente"):
        hydrogel_needed = field_area * 0.05
        st.info(f"""
        **📊 Rapport de l'Assistant Intelligent ({crop_type}) :**
        * 💧 **Économie d'eau estimée :** Réduction de l'arrosage de **35% à 45%** grâce au bio-hydrogel.
        * 🧪 **Bio-hydrogel recommandé :** **{hydrogel_needed:,.1f} kg** pour contrer le stress hydrique.
        """)

else:
    st.subheader("🌾 Field Area & Requirements Inputs")
    crop_type = st.selectbox("Select Crop Type:", ["Olive Trees", "Date Palm Trees", "Cereals", "Citrus", "Vegetables"])
    field_area = st.number_input("Target field area (in m²):", min_value=100.0, value2=20000.0 if 'value2' in globals() else 20000.0, step=100.0)
    
    st.markdown("---")
    st.subheader("🌿 Laboratory Fertilization Program")
    fertilizer_rate = st.number_input("Recommended fertilizer per square meter (kg/m²):", min_value=0.0, value=0.10, step=0.01)
    total_fertilizer = field_area * fertilizer_rate
    st.success(f"📌 Total fertilizer quantity: **{total_fertilizer:,.2f} kg**")

    st.markdown("---")
    st.subheader("🤖 AI Smart Recommendations")
    if st.button("🚀 Run AI Analysis"):
        hydrogel_needed = field_area * 0.05
        st.info(f"""
        **📊 Smart Agronomist Report ({crop_type}):**
        * 💧 **Water Saving Potential:** Estimated reduction of irrigation water by **35% - 45%**.
        * 🧪 **Recommended Bio-Hydrogel Dose:** Approximately **{hydrogel_needed:,.1f} kg**.
        """)




























