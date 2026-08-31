import os

# عرض صورة حقل التين الشوكي بمرونة تامة مع صيغ الملفات
image_path = "2237.jpg" if os.path.exists("2237.jpg") else "2237.JPG"
if os.path.exists(image_path):
    st.image(image_path, caption="حقل التين الشوكي (Opuntia ficus-indica) - المصدر الحيوي للهيدروجيل", use_container_width=True)
else:
    # محاولة البحث عن أي صورة بلاحقة أخرى
    found = False
    for filename in os.listdir("."):
        if filename.lower().startswith("2237"):
            st.image(filename, caption="حقل التين الشوكي (Opuntia ficus-indica) - المصدر الحيوي للهيدروجيل", use_container_width=True)
            found = True
            break
    if not found:
        st.warning("⚠️ يجدر التأكد من أن اسم الصورة في مستودع GitHub يبدأ بـ 2237.")



















