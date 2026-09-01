import streamlit as st
import pandas as pd

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد",
    page_icon="🌵",
    layout="wide"
)

# تنسيق CSS مخصص للواجهة والجدول لتجنب أي تداخل
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
    st.markdown("""
    <h3 style="direction: rtl; text-align: right; color: #1b4d3e;">📅 الجدول الزمني المقترح لسقي ومتابعة المحصول</h3>
    """, unsafe_allow_html=True)
    
    # جدول HTML منظم ومنعزل تماماً ضد التداخل
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
        "Olivier", "Palmier dattier", "Céréales (Blé et Orge)", "Agrumes", "Légumineuses sèches", "Légumes"
    ])
    soil_type = st.sidebar.selectbox("Type de sol :", [
        "Sol sableux (Sandy)", "Sol limoneux", "Sol argileux lourd", "Sol sablo-argileux", "Sol limo-argileux"
    ])
    climate_zone = st.sidebar.selectbox("Zone climatique :", [
        "Climat semi-aride / aride", "Climat saharien très aride", "Climat côtier / tempéré"
    ])
    area = st.sidebar.number_input("Superficie (m²) :", min_value=100, value=5000, step=500)
    fertilizer_rate = st.sidebar.number_input("Taux d'engrais (kg/m²) :", min_value=0.01, value=0.12, step=0.01)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    st.header(f"📊 Tableau de bord agronomique : {crop_type}")
    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Hydrogel suggéré", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Engrais total", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Eau économisée", f"{water_saved_m3:.1f} m³")

    st.subheader("📅 Calendrier d'irrigation suggéré")
    timeline_data = pd.DataFrame({
        "Stade de la culture": ["Plantation", "Croissance", "Floraison", "Maturation"],
        "Effet du Bio-Hydrogel": ["Protection des racines", "Approvisionnement continu", "Bouclier thermique", "Diminution progressive"],
        "Fréquence d'irrigation": ["Réduction de 20%", "Réduction de 40%", "Réduction de 35%", "Légère"]
    })
    st.table(timeline_data)

    report_content = f"AgriOpuntia Report\nCrop: {crop_type}\nArea: {area} m²\nHydrogel: {hydrogel_needed_kg:.1f} kg"
    st.download_button("📥 Download Report", report_content, file_name="report.txt", mime="text/plain")

else:
    crop_type = st.sidebar.selectbox("Select Crop Type:", [
        "Olive Trees", "Date Palm Trees", "Cereals", "Citrus", "Dry Legumes", "Vegetables"
    ])
    soil_type = st.sidebar.selectbox("Soil Type:", [
        "Sandy Soil", "Loamy Soil", "Clay Soil", "Sandy Clay Loam", "Silty Clay Loam"
    ])
    climate_zone = st.sidebar.selectbox("Climate Zone:", [
        "Semi-arid", "Desert", "Coastal"
    ])
    area = st.sidebar.number_input("Area (m²):", min_value=100, value=5000, step=500)
    fertilizer_rate = st.sidebar.number_input("Fertilizer Rate (kg/m²):", min_value=0.01, value=0.12, step=0.01)

    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

    st.header(f"📊 Agricultural Dashboard: {crop_type}")
    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("Suggested Hydrogel", f"{hydrogel_needed_kg:.1f} kg")
    mcol2.metric("Total Fertilizer", f"{total_crop_fertilizer_kg:.1f} kg")
    mcol3.metric("Saved Water", f"{water_saved_m3:.1f} m³")

    st.subheader("📅 Suggested Irrigation Timeline")
    timeline_data = pd.DataFrame({
        "Growth Stage": ["Planting", "Growth", "Flowering", "Maturation"],
        "Bio-Hydrogel Effect": ["Root protection", "Steady supply", "Thermal shield", "Gradual reduction"],
        "Irrigation Frequency": ["20% less", "40% less", "35% less", "Light"]
    })
    st.table(timeline_data)

    report_content = f"AgriOpuntia Report\nCrop: {crop_type}\nArea: {area} m²\nHydrogel: {hydrogel_needed_kg:.1f} kg"
    st.download_button("📥 Download Report", report_content, file_name="report.txt", mime="text/plain")













































