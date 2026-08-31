import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد",
    page_icon="🌵",
    layout="wide"
)

# القائمة الجانبية للإعدادات واللغة
st.sidebar.title("⚙️ إعدادات الحقل والمزرعة")
lang = st.sidebar.selectbox("Choose Language / اختر اللغة / Langue", ["العربية", "Français"])

if lang == "العربية":
    st.title("🌵 AgriOpuntia")
    # العنوان الرئيسي حسب طلبك
    st.subheader("المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد")
    st.markdown("*(Opuntia ficus-indica)* نظام هندسي ذكي لتقدير جرعات الهيدروجيل الحيوي المستخلص من الصبار وتحديد الاحتياجات السماد والمائية لمختلف المحاصيل الزراعية في الجزائر لمكافحة الإجهاد المائي.")
    
    # أنواع المحاصيل الزراعية الشهيرة في الجزائر
    crop_type = st.sidebar.selectbox("اختر المحصول الزراعي:", [
        "أشجار الزيتون (المناطق السهبية والشمالية)", 
        "نخيل التمر (المنطقة الجنوبية والولايات الواحية)", 
        "الحبوب (القمح والشعير - السكيت والسهوب)", 
        "الحمضيات (البرتقال والليمون - الشلف والسهل الساحلي)", 
        "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
        "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
    ])
    
    # أنواع التربة بناءً على التحاليل المخبرية (Soil Analysis Textures)
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
    
    # مدخلات التسميد الموجه للمحصول
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 برنامج التسميد المخبري للمحصول")
    fertilizer_rate = st.sidebar.number_input("كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):", min_value=0.01, value=0.12, step=0.01)
    fertilizer_price_per_kg = st.sidebar.number_input("سعر كيلوغرام الأسمدة (دج):", min_value=10.0, value=75.0, step=5.0)

    expected_yield_value_per_m2 = st.sidebar.number_input("القيمة المالية المتوقعة لإنتاج المحصول للمتر المربع (دج):", min_value=10.0, value=200.0, step=10.0)

    # الحسابات الفلاحية والتقنية
    hydrogel_needed_kg = area * 0.12 # كمية الهيدروجيل المقترحة للتطبيق
    water_saved_m3 = area * 0.22 # حجم المياه الموفّرة
    
    total_crop_fertilizer_kg = area * fertilizer_rate
    total_crop_fertilizer_cost = total_crop_fertilizer_kg * fertilizer_price_per_kg

    # التكلفة الإجمالية تعتمد على الهيدروجيل والتسميد وتطبيق الحقل
    base_tech_cost = area * 15.0 # تكلفة إنتاج وتطبيق الهيدروجيل محسوبة آلياً في الخلفية دون إزعاج الفلاح بمدخلات معقدة
    total_project_cost = base_tech_cost + total_crop_fertilizer_cost
    total_expected_revenue = area * expected_yield_value_per_m2
    net_profit = total_expected_revenue - total_project_cost

    # عرض الأقسام الرئيسية التفاعلية
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🌵 دور الهيدروجيل الحيوي")
        with st.expander("اضغط لعرض تفاصيل التقنية"):
            st.write("""
            - **المصدر:** مستخلص طبيعي من ألواح صبار التين الشوكي (*Opuntia ficus-indica*).
            - **الوظيفة الحقلية:** يشكل شبكة هلامية مجهرية حول جذور النبات لتحْبِس مياه الري والأسمدة وتمنع ترشيحها عميقاً.
            """)
        
    with col2:
        st.info(f"🌿 تخصيص المحصول ({crop_type.split()[0]})")
        with st.expander("اضغط لعرض تفاصيل الاحتياجات"):
            st.write(f"""
            - **المحصول:** {crop_type}.
            - **طبيعة التربة:** {soil_type}.
            - **التسميد المحسوب:** يحتاج الحقل إلى **{total_crop_fertilizer_kg:.1f} كغ** من العناصر الغذائية الموجهة لتحسين الإنتاجية الزراعية.
            """)
        
    with col3:
        st.info("💧 كفاءة الري والتوفير")
        with st.expander("اضغط لعرض أثر توفير المياه"):
            st.write("""
            - **نسبة توفير المياه:** تقليص عدد مرات السقي بنسبة تصل إلى 40%.
            - **مقاومة الجفاف:** حماية المحاصيل من صدمات الإجهاد المائي في الأوقات الحارة.
            """)

    st.markdown("---")
    st.header(f"📊 لوحة القيادة الفلاحية لتطبيق التقنية على: {crop_type.split()[0]}")

    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    mcol1.metric("الهيدروجيل المقترح", f"{hydrogel_needed_kg:.1f} كغ")
    mcol2.metric("أسمدة المحصول المحسوبة", f"{total_crop_fertilizer_kg:.1f} كغ")
    mcol3.metric("المياه الموفّرة للحقل", f"{water_saved_m3:.1f} م³")
    mcol4.metric("صافي الفائدة الاقتصادية", f"{net_profit:,.0f} دج")

    st.markdown("---")
    st.subheader("📑 التفصيل المالي والتحليل الاقتصادي للمزرعة")

    tab1, tab2 = st.tabs(["💰 التكاليف التفصيلية", "📈 الأرباح والجدوى الفلاحية"])

    with tab1:
        st.write(f"- **تكلفة تكنولوجيا الهيدروجيل وتطبيقه:** {base_tech_cost:,.0f} دج")
        st.write(f"- **تكلفة برنامج التسميد المخبري ({crop_type.split()[0]}):** {total_crop_fertilizer_cost:,.0f} دج ({total_crop_fertilizer_kg:.1f} كغ)")
        st.success(f"**التكلفة الإجمالية للاستثمار في الحقل:** {total_project_cost:,.0f} دج")

    with tab2:
        st.write(f"- **القيمة الإجمالية للمحصول المتوقع:** {total_expected_revenue:,.0f} دج")
        st.write(f"- **إجمالي التكاليف:** {total_project_cost:,.0f} دج")
        if net_profit > 0:
            st.success(f"**صافي الأرباح (الفائدة):** {net_profit:,.0f} دج - المشروع يحقق كفاءة اقتصادية عالية جداً لحماية {crop_type.split()[0]} في بيئة الجزائر!")
        else:
            st.warning(f"**ملاحظة اقتصادية:** التكاليف تتجاوز العوائد، يرجى ضبط القيمة المتوقعة للمحصول أو المساحة.")

else:
    st.title("🌵 AgriOpuntia")
    st.subheader("Plateforme intelligente d'application de bio-hydrogel et de calcul de fertilisation")
    st.write("Système d'ingénierie pour la valorisation du figuier de Barbarie et l'optimisation agricole.")


