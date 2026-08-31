import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - منصة استخلاص الهيدروجين الحيوي من الصبار",
    page_icon="🌵",
    layout="wide"
)

# القائمة الجانبية للإعدادات واللغة
st.sidebar.title("⚙️ إعدادات حقل التين الشوكي")
lang = st.sidebar.selectbox("Choose Language / اختر اللغة / Langue", ["العربية", "Français"])

if lang == "العربية":
    st.title("🌵 AgriOpuntia")
    st.subheader("المنصة الذكية لاستعمال الهيدروجين الحيوي المستخلص من صبار التين الشوكي وتوفير مياه الري")
    st.markdown("*(Opuntia ficus-indica)* نظام هندسي مخصص لتحديد الجرعات الميدانية للبيوهيدروجين المستخلص من ألواح الصبار لحماية التربة ومحاربة الإجهاد المائي، مع حساب الجدوى الاقتصادية الشاملة.")
    
    soil_type = st.sidebar.selectbox("اختر نوع التربة الميدانية:", ["تربة رملية (سريعة النفاذية)", "تربة طينية (متوسطة الاحتفاظ)", "تربة سلتية هيكلية"])
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("💰 المدخلات الاقتصادية والإنتاجية")
    area = st.sidebar.number_input("مساحة القطعة المخصصة لغراسة الصبار (بالمتر المربع $m^2$):", min_value=100, value=5000, step=500)
    plant_price = st.sidebar.number_input("سعر شتلة/لوح التين الشوكي الواحد (دج):", min_value=10.0, value=80.0, step=5.0)
    fertilizer_cost_per_m2 = st.sidebar.number_input("تكلفة الأسمدة والمخصبات العضوية للمتر المربع (دج):", min_value=1.0, value=15.0, step=5.0)
    water_cost_per_m3 = st.sidebar.number_input("تكلفة متر مكعب من الماء للري التأسيسي (دج):", min_value=1.0, value=40.0, step=5.0)
    transport_cost = st.sidebar.number_input("تكاليف النقل واللوجستيات الإجمالية (دج):", min_value=0.0, value=12000.0, step=1000.0)
    expected_revenue_per_m2 = st.sidebar.number_input("سعر بيع محصول الصبار أو مشتقاته للمتر المربع (دج):", min_value=10.0, value=150.0, step=10.0)

    # الحسابات الفلاحية والاقتصادية الخاصة بصبار التين الشوكي
    plants_needed = int(area / 4) 
    water_needed_m3 = area * 0.12 # استهلاك منخفض ومنظم بفضل الهيدروجين الحيوي
    maturity_months = "18 إلى 24 شهراً (للإنتاج الأول والألواح)"

    total_plants_cost = plants_needed * plant_price
    total_fertilizer_cost = area * fertilizer_cost_per_m2
    total_water_cost = water_needed_m3 * water_cost_per_m3
    
    total_project_cost = total_plants_cost + total_fertilizer_cost + total_water_cost + transport_cost
    total_expected_revenue = area * expected_revenue_per_m2
    net_profit = total_expected_revenue - total_project_cost

    # عرض الأقسام الرئيسية للمشروع
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🌵 استخلاص البيوهيدروجين")
        st.write("تثمين صبار التين الشوكي واستغلال مادة الصمغ والموسيلاج (Mucilage) الطبيعي لاستخلاص هيدروجين حيوي ذي قدرة فائقة على الامتصاص.")
        
    with col2:
        st.info("💧 حبس رطوبة التربة")
        st.write("تطبيق الهيدروجين الحيوي حول الجذور لرفع قدرة التربة على الإمساك بالماء وتقليل التبخر الناتج عن درجات الحرارة العالية في المناطق الجافة.")
        
    with col3:
        st.info("🌱 مقاومة الجفاف")
        st.write("توفير بيئة مستدامة ومغذية حول الشعيرات الجذرية للتين الشوكي لضمان استمرارية النمو والتنمية الفلاحية المستدامة.")

    st.markdown("---")
    st.header("📊 لوحة القيادة الفلاحية والاقتصادية لمشروع التين الشوكي")

    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    mcol1.metric("عدد الشتلات / الألواح", f"{plants_needed} وحدة")
    mcol2.metric("الاحتياج المائي المقدر", f"{water_needed_m3:.1f} م³")
    mcol3.metric("مدة جاهزية الإنتاج", maturity_months)
    mcol4.metric("صافي الفائدة المتوقعة", f"{net_profit:,.0f} دج")

    st.markdown("---")
    st.subheader("📑 التفصيل المالي وتكلفة الاستثمار للمشروع")

    tab1, tab2 = st.tabs(["💰 التكاليف التفصيلية", "📈 الأرباح والجدوى الفلاحية"])

    with tab1:
        st.write(f"- **تكلفة شتلات/ألواح التين الشوكي:** {total_plants_cost:,.0f} دج ({plants_needed} شتلة)")
        st.write(f"- **تكلفة الأسمدة والمغذيات:** {total_fertilizer_cost:,.0f} دج")
        st.write(f"- **تكلفة مياه الري التأسيسي:** {total_water_cost:,.0f} دج ({water_needed_m3:.1f} م³)")
        st.write(f"- **تكاليف النقل واللوجستيات:** {transport_cost:,.0f} دج")
        st.success(f"**التكلفة الإجمالية للمشروع:** {total_project_cost:,.0f} دج")

    with tab2:
        st.write(f"- **إجمالي المداخيل المتوقعة عند التسويق:** {total_expected_revenue:,.0f} دج")
        st.write(f"- **التكلفة الإجمالية للاستثمار:** {total_project_cost:,.0f} دج")
        if net_profit > 0:
            st.success(f"**صافي الأرباح (الفائدة):** {net_profit:,.0f} دج - المشروع ذو جدوى اقتصادية وفلاحية عالية جداً وموجه لتحقيق الأمن الغذائي!")
        else:
            st.warning(f"**ملاحظة اقتصادية:** التكاليف تتجاوز المداخيل المتوقعة، يرجى إعادة ضبط أسعار التسويق أو مساحة الإنتاج.")

else:
    st.title("🌵 AgriOpuntia")
    st.subheader("Plateforme intelligente pour l'application de bio-hydrogel d'Opuntia et l'économie d'eau")
    st.write("Système d'ingénierie dédié à la valorisation du figuier de Barbarie (Opuntia ficus-indica).")


