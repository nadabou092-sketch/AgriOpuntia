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
    st.subheader("المنصة الذكية لتطبيق الهيدروجيل الحيوي وحساب التسميد")
    st.markdown("*(Opuntia ficus-indica)* نظام هندسي ذكي لتقدير جرعات الهيدروجيل الحيوي المستخلص من الصبار وتحديد الاحتياجات السمادية والمائية لمختلف المحاصيل الزراعية في الجزائر لمكافحة الإجهاد المائي.")
    
    # أنواع المحاصيل الزراعية الصحيحة والمنظمة
    crop_type = st.sidebar.selectbox("اختر المحصول الزراعي:", [
        "أشجار الزيتون (المناطق السهبية والشمالية)", 
        "نخيل التمر (المنطقة الجنوبية والولايات الواحية)", 
        "الحبوب (القمح والشعير - مناطق الهضاب العليا والسهوب)", 
        "الحمضيات (البرتقال والليمون - الشلف والسهل الساحلي)", 
        "البقوليات الجافة (الفول، الحمص، الجلبانة)", 
        "الخضروات تحت السقي الموضعي (الطماطم، البطاطا)"
    ])
    
    # أنواع التربة بناءً على التحاليل المخبرية
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
    
    # خانة كمية الأسمدة وحدها
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌿 برنامج التسميد المخبري للمحصول")
    fertilizer_rate = st.sidebar.number_input("كمية الأسمدة الموصى بها تحليلياً للمتر المربع (كغ/م²):", min_value=0.01, value=0.12, step=0.01)

    # الحسابات الفلاحية والتقنية
    hydrogel_needed_kg = area * 0.12 
    water_saved_m3 = area * 0.22 
    total_crop_fertilizer_kg = area * fertilizer_rate 

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
            - **التسميد المحسوب:** يحتاج الحقل إجمالاً إلى **{total_crop_fertilizer_kg:.1f} كغ** من الأسمدة لتغطية احتياجات المساحة المدروسة.
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

    mcol1, mcol2, mcol3 = st.columns(3)
    mcol1.metric("الهيدروجيل المقترح", f"{hydrogel_needed_kg:.1f} كغ")
    mcol2.metric("إجمالي أسمدة الحقل", f"{total_crop_fertilizer_kg:.1f} كغ")
    mcol3.metric("المياه الموفّرة للحقل", f"{water_saved_m3:.1f} م³")

    st.markdown("---")
    st.subheader("📑 الملخص التقني والفلاحي للمزرعة")
    st.write(f"- **المساحة الكلية المستهدفة:** {area:,.0f} متر مربع.")
    st.write(f"- **نوع التربة المحددة من التحاليل:** {soil_type}.")
    st.write(f"- **الاحتياج الإجمالي من الهيدروجيل الحيوي:** {hydrogel_needed_kg:.1f} كيلوغرام لحماية الجذور.")
    st.write(f"- **الاحتياج الإجمالي من الأسمدة:** {total_crop_fertilizer_kg:.1f} كيلوغرام لضمان التغذية المثلى للمحصول.")
    st.success("المنصة جاهزة لتقديم التوصيات الدقيقة ميدانياً لتحسين الإنتاجية الزراعية في الجزائر واستدامة الموارد المائية!")

else:
    st.title("🌵 AgriOpuntia")
    st.subheader("Plateforme intelligente d'application de bio-hydrogel et de calcul de fertilisation")
    st.write("Système d'ingénierie pour la valorisation du figuier de Barbarie et l'optimisation agricole.")


