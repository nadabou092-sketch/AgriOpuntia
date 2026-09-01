import streamlit as st
import pandas as pd

# --- إعدادات الصفحة وعنوان المتصفح ---
st.set_page_config(
    page_title="AgriOpuntia 🇩🇿", 
    page_icon="🌵",
    layout="wide"
)

# --- تنسيق CSS مخصص لتطابق أطوال البطاقات وتنظيم المحتوى ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1b4d3e 0%, #2e6f40 50%, #558b2f 100%);
        padding: 22px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(27, 77, 62, 0.15);
        border-bottom: 4px solid #d4a373;
    }
    .main-header h1 {
        color: white !important;
        font-size: 2.3rem;
        margin-bottom: 5px;
        font-weight: 700;
    }
    .main-header p {
        color: #f4f1ea !important;
        font-size: 0.95rem;
        margin: 0;
    }
    .feature-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 18px;
        height: 210px; /* توحيد الطول والارتفاع لكل البطاقات بدقة */
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        direction: rtl;
        text-align: right;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .feature-card-en {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 18px;
        height: 210px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        direction: ltr;
        text-align: left;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .feature-card h4, .feature-card-en h4 {
        color: #1b4d3e;
        font-size: 1.05rem;
        margin-bottom: 10px;
        font-weight: 700;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 6px;
    }
    .feature-card p, .feature-card-en p {
        color: #333333;
        font-size: 0.88rem;
        line-height: 1.6;
        margin: 0;
    }
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
        direction: rtl;
        text-align: right;
        background-color: #ffffff;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .custom-table th {
        background-color: #1b4d3e;
        color: white;
        padding: 12px 15px;
        font-size: 1rem;
    }
    .custom-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #e0e0e0;
        color: #333333;
        font-size: 0.95rem;
    }
    .custom-table tr:hover {
        background-color: #f7f4ee;
    }
</style>
""", unsafe_allow_html=True)

# --- الواجهة الرئيسية (Main Header) ---
st.markdown("""
<div class="main-header">
    <h1>AgriOpuntia 🇩🇿</h1>
    <p>المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد | Smart Platform for Bio-Hydrogel & Fertilization</p>
</div>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("⚙️ الإعدادات / Settings")

lang = st.sidebar.selectbox(
    "Choose Language / اختر اللغة / Langue", 
    ["العربية", "Français", "English"]
)

# --- محتوى التطبيق حسب اللغة ---
if lang == "العربية":
    crop_type = st.sidebar.selectbox("اختر المحصول الزراعي:", [
        "أشجار الزيتون", 
        "نخيل التمر", 
        "الحبوب (القمح والشعير)", 
        "الحمضيات (البرتقال والليمون)", 
        "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
        "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
    ])
    
    soil_type = st.sidebar.selectbox("نوع التربة (حسب التحليل المخبري):", [
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
    area = st.sidebar.number_input("مساحة الحقل المستهدف (بالمتر المربع م²):", min_value=100.0, value=20000.0, step=500.0)
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 برنامج التسميد المخبري")
    fertilizer_rate = st.sidebar.number_input("كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):", min_value=0.01, value=0.10, step=0.01)

    # --- أزرار التحكم الجانبية للتحليلات الذكية والتوصيات المناخية ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 أدوات المستشار الذكي")
    show_ai_insights = st.sidebar.checkbox("🤖 إظهار التحليل الذكي (AI Insights)", value=False)
    show_climate_recs = st.sidebar.checkbox("🌤️ إظهار التوصيات المناخية", value=False)

    # الحسابات الفلاحية
    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    # بطاقات متساوية الطول والارتفاع ومنظمة بدقة
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="feature-card">
            <h4>🌵 دور الهيدروجيل الحيوي</h4>
            <p><b>• المصدر:</b> مستخلص طبيعي من ألواح صبار التين الشوكي.<br>
            <b>• الوظيفة:</b> تشكيل شبكة هلامية مجهرية حول الجذور لتحْبِس المياه والأسمدة وتمنع ترشيحها.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="feature-card">
            <h4>🌿 تخصيص المحصول والتربة</h4>
            <p><b>• المحصول:</b> {crop_type}<br>
            <b>• التربة:</b> {soil_type}<br>
            <b>• الأسمدة الكلية:</b> <b>{total_crop_fertilizer_kg:,.1f} كغ</b> ({total_crop_fertilizer_kg/100:,.2f} قنطار).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="feature-card">
            <h4>💧 كفاءة الري والتوفير</h4>
            <p><b>• توفير المياه:</b> تقليص عدد مرات السقي بنسبة تصل إلى 40%.<br>
            <b>• مقاومة الجفاف:</b> حماية المحاصيل بكفاءة عالية من صدمات الإجهاد المائي.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
    <h2 style="direction: rtl; text-align: right; color: #1b4d3e;">📊 لوحة القيادة الفلاحية للمحصول: {crop_type}</h2>
    """, unsafe_allow_html=True)

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("الهيدروجيل المقترح", f"{hydrogel_needed_kg:,.1f} كغ")
    mcol2.metric("إجمالي أسمدة الحقل", f"{total_crop_fertilizer_kg:,.1f} كغ")
    mcol3.metric("المياه الموفّرة للحقل", f"{water_saved_m3:,.1f} م³")

    # --- عرض التحليل الذكي في الواجهة فقط إذا تم تفعيله من الجنب ---
    if show_ai_insights:
        st.markdown("---")
        st.subheader("🤖 التحليل الذكي وتوصيات الهيدروجيل (AI Insights)")
        st.info(f"""
        **📊 تقرير المستشار الذكي لمحصول ({crop_type}):**
        * 💧 **نسبة توفير المياه المتوقعة:** بفضل استجابة الهيدروجيل الحيوي المستخلص من الصبار، يُتوقع تقليل استهلاك مياه السقي بنسبة **35% إلى 45%**.
        * 🧪 **الجرعة المثالية الموصى بها:** استخدام **{hydrogel_needed_kg:,.1f} كغ** موزعة على عمق منطقة الجذر الحيوية.
        * 🌱 **الأثر الاقتصادي:** رفع كفاءة امتصاص الأسمدة المُقدرة بـ ({total_crop_fertilizer_kg:,.1f} كغ) وتقليل فقدان العناصر بالترشيح.
        """)

    # --- عرض التوصيات المناخية في الواجهة فقط إذا تم تفعيلها من الجنب ---
    if show_climate_recs:
        st.markdown("---")
        st.subheader("🌤️ التوصيات الذكية حسب المناخ والمنطقة")
        if "صحراوي" in climate_zone:
            st.warning("⚠️ **توصية للمناخ الصحراوي:** نظراً لشدة التبخر، يُنصح بزيادة عمق وضع الهيدروجيل إلى 35 سم واعتماد نظام سقي قطرات دقيق ومكثف في ذروة الصيف.")
        elif "شبه جاف" in climate_zone:
            st.info("💡 **توصية للمناخ الشبه جاف:** الهيدروجيل سيقلل بوضوح من صدمة الجفاف بين فترات المطر، مع إمكانية تقليص جدول الري بـ 35%.")
        else:
            st.success("🌱 **توصية للمناخ الساحلي/المعتدل:** الرطوبة النسبية مساعدة، والهيدروجيل سيمنع غسل العناصر الغذائية نحو الأسفل بسبب مياه الأمطار الزائدة.")

    # --- جدول السقي المنظم ---
    st.markdown("---")
    st.markdown("""
    <h3 style="direction: rtl; text-align: right; color: #1b4d3e;">📅 الجدول الزمني المقترح لسقي ومتابعة المحصول</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <table class="custom-table">
        <tr>
            <th>مرحلة نمو المحصول</th>
            <th>تأثير الهيدروجيل الحيوي</th>
            <th>تواتر الري الموصى به</th>
        </tr>
        <tr>
            <td><b>مرحلة الغرس / البداية</b></td>
            <td>حماية الجذور الفتية وتثبيت الرطوبة الأولية</td>
            <td>عادي مع تقليل الفترات بـ 20%</td>
        </tr>
        <tr>
            <td><b>مرحلة النمو الخضري</b></td>
            <td>إمداد متواصل ومستقر بالمياه والأسمدة</td>
            <td>تخفيض الفترات بـ 40%</td>
        </tr>
        <tr>
            <td><b>مرحلة الإزهار والعقد</b></td>
            <td>الحماية من صدمات العطش والإجهاد الحراري</td>
            <td>تخفيض الفترات بـ 35%</td>
        </tr>
        <tr>
            <td><b>مرحلة النضج والجني</b></td>
            <td>تقليل تدريجي للرطوبة لتحسين جودة المحصول</td>
            <td>ري خفيف عند الضرورة</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # --- الملخص وزر التحميل ---
    st.markdown("---")
    st.subheader("📑 الملخص التقني وتحميل التقرير")
    st.markdown(f"""
    <div dir="rtl" style="text-align: right; line-height: 1.8;">
    - <b>المساحة الكلية المستهدفة:</b> {area:,.0f} متر مربع<br>
    - <b>المنطقة المناخية:</b> {climate_zone}<br>
    - <b>نوع التربة المحددة من التحاليل:</b> {soil_type}<br>
    - <b>الاحتياج الإجمالي من الهيدروجيل الحيوي:</b> {hydrogel_needed_kg:,.1f} كيلوغرام<br>
    - <b>الاحتياج الإجمالي من الأسمدة:</b> {total_crop_fertilizer_kg:,.1f} كيلوغرام ({total_crop_fertilizer_kg/100:,.2f} قنطار)
    </div>
    """, unsafe_allow_html=True)
    
    report_content = f"""AgriOpuntia Technical Field Report
------------------------------------
Country: Algeria 🇩🇿
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
    crop_type = st.sidebar.selectbox("Sélectionner la culture :", ["Olivier", "Palmier dattier", "Céréales", "Agrumes", "Légumineuses", "Légumes"])
    soil_type = st.sidebar.selectbox("Type de sol :", ["Sol sableux", "Sol limoneux", "Sol argileux lourd", "Sol sablo-argileux"])
    climate_zone = st.sidebar.selectbox("Zone climatique :", ["Climat semi-aride", "Climat saharien", "Climat côtier"])
    area = st.sidebar.number_input("Superficie (m²) :", min_value=100.0, value=20000.0, step=500.0)
    fertilizer_rate = st.sidebar.number_input("Taux d'engrais (kg/m²) :", min_value=0.01, value=0.10, step=0.01)

    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 Assistant IA")
    show_ai_insights = st.sidebar.checkbox("🤖 Afficher Insights IA", value=False)
    show_climate_recs = st.sidebar.checkbox("🌤️ Afficher Recommandations Climatiques", value=False)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    st.header(f"📊 Tableau de bord agronomique : {crop_type}")
    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Hydrogel suggéré", f"{hydrogel_needed_kg:,.1f} kg")
    mcol2.metric("Engrais total", f"{total_crop_fertilizer_kg:,.1f} kg")
    mcol3.metric("Eau économisée", f"{water_saved_m3:,.1f} m³")

    if show_ai_insights:
        st.markdown("---")
        st.subheader("🤖 Recommandations Intelligentes (AI Insights)")
        st.info(f"**Rapport IA ({crop_type}):** Économie d'eau estimée à **35%-45%**. Quantité recommandée de bio-hydrogel: **{hydrogel_needed_kg:,.1f} kg**.")

    if show_climate_recs:
        st.markdown("---")
        st.subheader("🌤️ Recommandations Climatiques")
        st.success("Recommandation adaptée à votre zone climatique et aux conditions de sol.")

    report_content = f"AgriOpuntia Report\nCrop: {crop_type}\nArea: {area} m²\nHydrogel: {hydrogel_needed_kg:.1f} kg"
    st.download_button("📥 Download Technical Report", report_content, file_name="report.txt", mime="text/plain")

else:
    crop_type = st.sidebar.selectbox("Select Crop Type:", ["Olive Trees", "Date Palm Trees", "Cereals", "Citrus", "Dry Legumes", "Vegetables"])
    soil_type = st.sidebar.selectbox("Soil Type:", ["Sandy Soil", "Loamy Soil", "Clay Soil", "Sandy Clay Loam"])
    climate_zone = st.sidebar.selectbox("Climate Zone:", ["Semi-arid climate", "Desert climate", "Coastal climate"])
    area = st.sidebar.number_input("Target Area (m²):", min_value=100.0, value=20000.0, step=500.0)
    fertilizer_rate = st.sidebar.number_input("Recommended fertilizer (kg/m²):", min_value=0.01, value=0.10, step=0.01)

    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 AI Assistant")
    show_ai_insights = st.sidebar.checkbox("🤖 Show AI Insights", value=False)
    show_climate_recs = st.sidebar.checkbox("🌤️ Show Climate Recommendations", value=False)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    st.header(f"📊 Agricultural Dashboard: {crop_type}")
    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Suggested Hydrogel", f"{hydrogel_needed_kg:,.1f} kg")
    mcol2.metric("Total Fertilizer", f"{total_crop_fertilizer_kg:,.1f} kg")
    mcol3.metric("Saved Water", f"{water_saved_m3:,.1f} m³")

    if show_ai_insights:
        st.markdown("---")
        st.subheader("🤖 AI Smart Recommendations")
        st.info(f"**AI Report ({crop_type}):** Water saving estimated between **35%-45%**. Recommended bio-hydrogel dose: **{hydrogel_needed_kg:,.1f} kg**.")

    if show_climate_recs:
        st.markdown("---")
        st.subheader("🌤️ Climate Recommendations")
        st.success("Tailored recommendations for your selected climate zone and soil conditions.")

    report_content = f"AgriOpuntia Report\nCrop: {crop_type}\nArea: {area} m²\nHydrogel: {hydrogel_needed_kg:.1f} kg"
    st.download_button("📥 Download Technical Report", report_content, file_name="report.txt", mime="text/plain")











































