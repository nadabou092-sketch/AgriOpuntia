import streamlit as st

# --- 1. إعدادات الصفحة الأساسية ---
st.set_page_config(
    page_title="AgriOpuntia DZ",
    page_icon="🌵",
    layout="wide"
)

# --- 2. تهيئة جلسة الرسائل للمساعد الذكي ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. اختيار اللغات (ترجمات واجهة المستخدم) ---
translations = {
    "fr": {
        "title": "AgriOpuntia DZ",
        "subtitle": "Plateforme intelligente pour le bio-hydrogel et la gestion agricole",
        "ai_header": "Assistant IA Agricole (Agri-Chat)",
        "chat_placeholder": "Posez vos questions sur l'irrigation, la fertilisation, ou la gestion des sols...",
        "card1_title": "Rôle du Bio-Hydrogel",
        "card2_title": "Culture & Sol",
        "card3_title": "Efficacité d'Irrigation"
    },
    "ar": {
        "title": "AgriOpuntia DZ",
        "subtitle": "المنصة الذكية لتطبيق الهيدروجيل الحيوي وإدارة المزارع",
        "ai_header": "مساعد الذكاء الاصطناعي الفلاحي (Agri-Chat)",
        "chat_placeholder": "...اسأل المساعد عن التسميد، الري، مكافحة الجفاف، أو أي استشارة فلاحية",
        "card1_title": "دور الهيدروجيل الحيوي",
        "card2_title": "تخصيص المحصول والتربة",
        "card3_title": "كفاءة الري والتوفير"
    },
    "en": {
        "title": "AgriOpuntia DZ",
        "subtitle": "Smart Platform for Bio-Hydrogel and Agricultural Management",
        "ai_header": "Agricultural AI Assistant (Agri-Chat)",
        "chat_placeholder": "Ask about irrigation, fertilization, or soil management...",
        "card1_title": "Bio-Hydrogel Role",
        "card2_title": "Crop & Soil",
        "card3_title": "Irrigation Efficiency"
    }
}

# --- 4. شريط الإعدادات الجانبي (Sidebar) ---
st.sidebar.title("🎛️ Paramètres / الإعدادات")
selected_lang = st.sidebar.selectbox("Language / اللغة", ["Français", "العربية", "English"])

lang_code = "fr"
if selected_lang == "العربية":
    lang_code = "ar"
elif selected_lang == "English":
    lang_code = "en"

lang_data = translations[lang_code]

st.sidebar.markdown("---")
crop_type = st.sidebar.selectbox("Type de Culture / المحصول", ["Olivier", "Agrumes", "Céréales", "Tomate"])
soil_type = st.sidebar.selectbox("Type de Sol / نوع التربة", ["Sol sableux", "Sol argileux", "Sol limoneux"])
area = st.sidebar.number_input("Superficie (m²) / المساحة", min_value=100, max_value=1000000, value=15000, step=500)
total_crop_fertilizer_kg = (area / 10000) * 1333.3  # حساب تقديري للأسمدة

show_ai_module = st.sidebar.checkbox("Activer l'Assistant IA / تفعيل المساعد الذكي", value=True)

# --- 5. تنسيق CSS لتوضيح الكتبة وإصلاح الإطارات ---
st.markdown("""
    <style>
    div[data-testid="stExpander"] {
        background-color: #fafbfc;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
    }
    div[data-testid="stExpander"] summary span {
        color: #1f2937 !important;
        font-weight: 600;
    }
    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p {
        color: #374151 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 6. عنوان المنصة الرئيسي ---
st.markdown(f"""
    <div style="background-color: #1e6b3eb8; padding: 25px; border-radius: 10px; text-align: center; color: white;">
        <h1 style="margin:0; font-size: 36px;">{lang_data['title']}</h1>
        <p style="margin: 10px 0 0 0; font-size: 18px;">{lang_data['subtitle']}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 7. البطاقات الإحصائية التفاعلية المتناسقة ---
col1, col2, col3 = st.columns(3)

with col1:
    with st.expander(f"🌵 {lang_data['card1_title']}", expanded=False):
        st.markdown(f"""
        - **Source:** Extrait naturel de figuier de barbarie.
        - **Fonction:** Rétention d'eau et de nutriments.
        """)

with col2:
    with st.expander(f"🌿 {lang_data['card2_title']}", expanded=False):
        st.markdown(f"""
        - **Culture:** {crop_type}
        - **Sol:** {soil_type}
        - **Engrais total:** {total_crop_fertilizer_kg:,.1f} kg
        """)

with col3:
    with st.expander(f"💧 {lang_data['card3_title']}", expanded=False):
        st.markdown(f"""
        - **Économie d'eau:** Réduction jusqu'à 40%.
        - **Résistance:** Protection contre le stress hydrique.
        """)

st.markdown("<br>", unsafe_allow_html=True)

# --- 8. مساعد الذكاء الاصطناعي الفلاحي (Agri-Chat) ---
if show_ai_module:
    st.markdown("---")
    st.subheader(f"🤖 {lang_data['ai_header']}")
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input(lang_data['chat_placeholder'], key="agri_chat_input_unique"):
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.chat_message("assistant"):
            # التحقق الذكي من لغة السؤال لتحديد لغة الرد
            is_french = any(word in user_prompt.lower() for word in ["combien", "quel", "quelle", "est", "et", "pour", "dans", "sol", "quantité"])
            is_english = any(word in user_prompt.lower() for word in ["how", "what", "is", "for", "in", "soil", "quantity", "amount"])

            if is_french:
                if any(word in user_prompt.lower() for word in ["hydrogel", "gel", "eau", "irrigation"]):
                    ai_reply = f"Concernant votre question sur la culture de **{crop_type}**, l'utilisation du bio-hydrogel extrait de figuier de barbarie dans un sol de type **{soil_type}** permet de réduire les besoins en eau de 35% à 45%, tout en maintenant l'efficacité d'absorption des engrais calculée à **{total_crop_fertilizer_kg:,.1f} kg**."
                elif any(word in user_prompt.lower() for word in ["engrais", "fertilisant", "fertilisation"]):
                    ai_reply = f"La quantité d'engrais recommandée pour la superficie de **{area:,.0f} m²** de **{crop_type}** est de **{total_crop_fertilizer_kg:,.1f} kg**. Il est recommandé de l'appliquer en plusieurs fractionnements."
                else:
                    ai_reply = f"Bienvenue ! En tant qu'assistant intelligent d'**AgriOpuntia**, je suis là pour vous aider à gérer la culture de **{crop_type}**, optimiser l'irrigation et faire face au stress hydrique. Posez votre question agronomique !"
            
            elif is_english:
                if any(word in user_prompt.lower() for word in ["hydrogel", "gel", "water", "irrigation"]):
                    ai_reply = f"Regarding your inquiry about **{crop_type}**, applying the Opuntia-derived bio-hydrogel in **{soil_type}** helps reduce water requirements by 35-45%, while efficiently maintaining the calculated fertilizer uptake of **{total_crop_fertilizer_kg:,.1f} kg**."
                elif any(word in user_prompt.lower() for word in ["fertilizer", "fertigation", "nutrient"]):
                    ai_reply = f"The recommended fertilizer amount for **{area:,.0f} m²** of **{crop_type}** is **{total_crop_fertilizer_kg:,.1f} kg**. It is best applied in stages for optimal uptake."
                else:
                    ai_reply = f"Welcome! As your **AgriOpuntia** smart assistant, I am here to help you manage **{crop_type}**, optimize water usage, and boost farm efficiency. Feel free to ask your specific farming question!"
            
            else:
                if any(word in user_prompt.lower() for word in ["هيدروجيل", "hydrogel", "صبار", "ماء", "سقي", "رطوبة"]):
                    ai_reply = f"بخصوص استفسارك حول النشاط الفلاحي لـ **{crop_type}**، استخدام الهيدروجيل الحيوي المستخلص من صبار التين الشوكي في تربة مثل **{soil_type}** يساعد في خفض الاحتياجات المائية بحوالي 35-45%، مع الحفاظ على كفاءة امتصاص الأسمدة المحسوبة بـ **{total_crop_fertilizer_kg:,.1f} كغ**."
                elif any(word in user_prompt.lower() for word in ["سماد", "fertilizer", "تسميد", "أسمدة"]):
                    ai_reply = f"كمية الأسمدة الموصى بها لمساحة **{area:,.0f} م²** الخاصة بـ **{crop_type}** تقدر بـ **{total_crop_fertilizer_kg:,.1f} كغ**. يُنصح دائماً بتوزيعها على دفعات لزيادة الكفاءة."
                else:
                    ai_reply = f"أهلاً بكِ. بصفتي مساعدك الذكي في منصة **AgriOpuntia**، أنا هنا لمساعدتك في كل ما يتعلق بإدارة زراعة **{crop_type}**، تحسين مقاومة الجفاف، وتسيير الحقول بكفاءة عالية. تفضلي بطرح سؤالك الزراعي المحدد!"
            
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
)



































































