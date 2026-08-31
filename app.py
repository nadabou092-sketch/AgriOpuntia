import streamlit as st

# إعداد صفحة التطبيق
st.set_page_config(
    page_title="AgriOpuntia - منصة البيوهيدروجيل والتسميد الزراعي",
    page_icon="🌵",
    layout="wide"
)

# القائمة الجانبية للإعدادات واللغة
st.sidebar.title("⚙️ إعدادات حقل الزراعة والتسميد")
lang = st.sidebar.selectbox("Choose Language / اختر اللغة / Langue", ["العربية", "Français"])

if lang == "العربية":
    st.title("🌵 AgriOpuntia")
    st.subheader("المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد المخصص للأشجار المثمرة، البقوليات والنخيل")
    st.markdown("*(Opuntia ficus-indica)* نظام هندسي متكامل لتثمين الموسيلاج النباتي لصناعة الهيدروجيل، مع حساب الاحتياجات الدقيقة من الأسمدة والتسميد الموجه للمحاصيل لحل مشكلة الإجهاد المائي ورفع الإنتاجية.")
    
    # اختيار نوع المحصول
    crop_type = st.sidebar.selectbox("اختر المحصول الزراعي المستفيد:", [
        "أشجار مثمرة (حمضيات، زيتون، تفاح...)", 
        "نخيل التمر (مناطق جافة وشبه جافة)", 
        "البقوليات والمحاصيل الحقلية السنوية", 
        "خضروات تحت السقي الموضعي"
    ])
    
    soil_type = st.sidebar.selectbox("اختر نوع التربة في المزرعة:", ["تربة رملية (حاجة قصوى للهيدروجيل)", "تربة طينية هيكلية", "تربة سلتية"])
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("💰 المدخلات الاقتصادية لإنتاج الهيدروجيل")
    area = st.sidebar.number_input("المساحة الزراعية المغروسة (بالمتر المربع $m^2$):", min_value=100, value=5000, step=500)
    raw_cactus_cost = st.sidebar.number_input("تكلفة جمع وتوريد ألواح الصبار الخام للاستخلاص (دج):", min_value=1000.0, value=9000.0, step=1000.0)
    extraction_chem_cost = st.sidebar.number_input("تكلفة عملية الاستخلاص والمعالجة العضوية (دج):", min_value=1000.0, value=8000.0, step=500.0)
    application_labor_cost = st.sidebar.number_input("تكلفة تطبيق الهيدروجيل حول الجذور ميدانياً (دج):", min_value=1000.0, value=12000.0, step=1000.0)

    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 حساب برنامج التسميد الخاص بالمحصول")
    fertilizer_rate = st.sidebar.number_input("كمية الأسمدة الموصى بها للمتر المربع للمحصول (كغ/م²):", min_value=0.01, value=0.15, step=0.01)
    fertilizer_price_per_kg = st.sidebar.number_input("سعر كيلوغرام الأسمدة (دج):", min_value=10.0, value=70.0, step=5.0)

    expected_service_revenue = st.sidebar.number_input("سعر بيع خدمة حماية المحصول وتوفير المياه والتسميد للمتر المربع (دج):", min_value=10.0, value=150.0, step=10.0)

    # الحسابات الفلاحية والاقتصادية
    hydrogel_needed_kg = area * 0.12 # كمية الهيدروجيل اللازمة للمساحة
    water_saved_m3 = area * 0.20 # كمية المياه الموفّرة للمحصول
    
    total_crop_fertilizer_kg = area * fertilizer_rate
    total_crop_fertilizer_cost = total_crop_fertilizer_kg * fertilizer_price_per_kg

    total_project_cost = raw_cactus_cost + extraction_chem_cost + application_labor_cost + total_crop_fertilizer_cost
    total_expected_revenue = area * expected_service_revenue
    net_profit = total_expected_revenue - total_project_cost

    # عرض الأقسام الرئيسية التفاعلية
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🌵 مصدر الهيدروجيل (الصبار)")
        with st.expander("اضغط لعرض تفاصيل الاستخلاص"):
            st.write("""
            - **المصدر:** ألواح صبار التين الشوكي (*Opuntia ficus-indica*).
            - **المادة الفعالة:** الموسيلاج النباتي والألياف السكرية الطبيعية.
            - **الدور:** تحويل صبار مهمل إلى بوليمر حيوي هلامي آمن 100% على البيئة والجذور.
            """)
        
    with col2:
        st.info(f"🌿 برنامج التسميد ({crop_type.split()[0]})")
        with st.expander("اضغط لعرض تفاصيل التسميد المحسوب"):
            st.write(f"""
            - **المحصول المستهدف:** {crop_type}.
            - **الكمية المحسوبة:** يحتاج الحقل إلى حوالي **{total_crop_fertilizer_kg:.1f} كغ** من الأسمدة لتغطية الاحتياجات الغذائية للموسم.
            - **التكامل:** بفضل الهيدروجيل الحيوي، يتم الاحتفاظ بالعناصر المغذية بجانب الجذور وعدم غسلها بعيداً بفعل الري.
            """)
        
    with col3:
        st.info("💧 الاقتصاد في مياه الري")
        with st.expander("اضغط لعرض تفاصيل توفير المياه"):
            st.write("""
            - **نسبة التوفير:** تقليل استهلاك الري بنسبة تصل إلى 35%-45%.
            - **الجدوى البيئية:** الحفاظ على المخزون المائي الجوفي وتقليل تكاليف الضخ والطاقة للفلاح.
            """)

    st.markdown("---")
    st.header(f"📊 لوحة القيادة الفلاحية لتطبيق التقنية على: {crop_type}")

    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    mcol1.metric("الهيدروجيل المستعمل", f"{hydrogel_needed_kg:.1f} كغ")
    mcol2.metric("أسمدة المحصول المحسوبة", f"{total_crop_fertilizer_kg:.1f} كغ")
    mcol3.metric("المياه الموفّرة", f"{water_saved_m3:.1f} م³")
    mcol4.metric("صافي الفائدة الاقتصادية", f"{net_profit:,.0f} دج")

    st.markdown("---")
    st.subheader("📑 التفصيل المالي وتكلفة استثمار التقنية للمزرعة")

    tab1, tab2 = st.tabs(["💰 التكاليف التفصيلية", "📈 الأرباح والجدوى الفلاحية"])

    with tab1:
        st.write(f"- **تكلفة جمع ألواح الصبار الخام:** {raw_cactus_cost:,.0f} دج")
        st.write(f"- **تكلفة معالجة واستخلاص الهيدروجيل:** {extraction_chem_cost:,.0f} دج")
        st.write(f"- **تكلفة العمالة وتطبيق الخدمة حول الجذور:** {application_labor_cost:,.0f} دج")
        st.write(f"- **تكلفة أسمدة المحصول ({crop_type.split()[0]}):** {total_crop_fertilizer_cost:,.0f} دج ({total_crop_fertilizer_kg:.1f} كغ)")
        st.success(f"**التكلفة الإجمالية للمشروع والتسميد:** {total_project_cost:,.0f} دج")

    with tab2:
        st.write(f"- **إجمالي العوائد والمردود الاقتصادي للخدمة:** {total_expected_revenue:,.0f} دج")
        st.write(f"- **التكلفة الإجمالية للاستثمار:** {total_project_cost:,.0f} دج")
        if net_profit > 0:
            st.success(f"**صافي الأرباح (الفائدة):** {net_profit:,.0f} دج - المشروع يدمج التسميد الدقيق والري ببراعة لحماية {crop_type}!")
        else:
            st.warning(f"**ملاحظة اقتصادية:** التكاليف تتجاوز العوائد، يرجى إعادة ضبط التسعير أو المساحة.")

else:
    st.title("🌵 AgriOpuntia")
    st.subheader("Plateforme intelligente de bio-hydrogel et de calcul de fertilisation pour les cultures")
    st.write("Système d'ingénierie pour la valorisation du figuier de Barbarie et l'optimisation agricole.")


