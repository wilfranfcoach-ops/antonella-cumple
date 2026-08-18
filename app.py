import streamlit as st
import random

# ---------- CONFIGURACIÓN DE LA PÁGINA ----------
st.set_page_config(
    page_title="Feliz Cumple Antonella 🎉",
    page_icon="💗",
    layout="centered"
)

# ---------- PWA: manifest y service worker ----------
st.markdown("""
<link rel="manifest" href="manifest.json">
<script>
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("service-worker.js");
  }
</script>
""", unsafe_allow_html=True)

# -------boton descarga-------------
st.markdown("""
<a href="https://antonellita.streamlit.app/" download>
    <button style="
        background-color:#ff2d95;
        color:white;
        font-size:20px;
        font-weight:bold;
        border-radius:50px;
        padding:15px 30px;
        border:none;
        box-shadow:0 4px 10px rgba(0,0,0,0.2);
    ">
    📥 Descargar la app
    </button>
</a>
""", unsafe_allow_html=True)

# ---------- ESTILOS (rosado/fucsia) ----------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #ff6ec7 100%);
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #4a004a !important;
        text-align: center;
    }
    div.stButton > button {
        background-color: #ff2d95;
        color: white;
        font-size: 22px;
        font-weight: bold;
        border-radius: 50px;
        padding: 15px 40px;
        border: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    div.stButton > button:hover {
        background-color: #ff69c9;
        transform: scale(1.05);
    }
    .mensaje-cariño {
        background-color: white;
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        font-size: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        color: #d6006c;
        font-weight: 600;
    }
    </style>

""", unsafe_allow_html=True)

# ---------- MENSAJES DE CARIÑO DEL PAPÁ ----------
# Puedes editar, agregar o quitar los que quieras aquí abajo:
mensajes = [
    "Antonella, eres el regalo más grande que la vida me ha dado. 💗",
    "No importa cuántos años cumplas, para mí siempre serás mi niña. 🎀",
    "Estoy tan orgulloso de la persona en la que te estás convirtiendo. ✨",
    "Cada día contigo es mi día favorito. Te amo infinito. 💕",
    "Eres fuerte, eres valiente, eres increíble. Nunca lo olvides. 🌸",
    "Gracias por llenar mi vida de risas y colores. Te amo, hija. 🎈",
    "Donde sea que estés, mi corazón siempre va contigo. 💖",
    "Eres mi razón para ser mejor cada día. Feliz cumpleaños, mi amor. 🎂",
    "Tus sueños son importantes para mí. Siempre voy a apoyarte. 🌟",
    "Te quiero tal como eres, hoy y siempre. 💗",
    "Ver crecer a una persona tan especial como tú es mi mayor orgullo. 🦋",
    "No hay distancia ni tiempo que cambie lo mucho que te amo. 💞",
    "Eres luz en mi vida, Antonella. Feliz cumpleaños, princesa. 👑",
    "Cuenta siempre conmigo, pase lo que pase. Te amo con todo mi corazón. 💗",
    "Cada logro tuyo, por pequeño que sea, me llena de alegría. 🎉",
]

# ---------- ENCABEZADO ----------
st.markdown("<h1>🎉 ¡Feliz Cumpleaños, Antonella! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3>11 años de pura magia 💗✨</h3>", unsafe_allow_html=True)

# ---------- FOTO DE ANTONELLA ----------
# Sube tu foto al repositorio de GitHub con el nombre "antonella.jpg"
# (junto a app.py y requirements.txt), y aparecerá aquí automáticamente.
col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    st.markdown("""
        <style>
        .foto-redonda img {
            border-radius: 50%;
            border: 6px solid #ff2d95;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='foto-redonda'>", unsafe_allow_html=True)
    st.image("antonella.jpg", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.balloons()

st.write("")
st.markdown("<p style='font-size:18px;'>Toca el corazón cada día y recibe un mensaje de amor de tu papá 💌</p>", unsafe_allow_html=True)

# ---------- BOTÓN INTERACTIVO ----------
if "mensaje_actual" not in st.session_state:
    st.session_state.mensaje_actual = None

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("💖 Toca aquí 💖"):
        st.session_state.mensaje_actual = random.choice(mensajes)
        st.balloons()

if st.session_state.mensaje_actual:
    st.markdown(f"<div class='mensaje-cariño'>{st.session_state.mensaje_actual}</div>", unsafe_allow_html=True)

# ---------- JUEGO EXTRA: ADIVINA EL NÚMERO ----------
st.write("")
st.write("")
st.markdown("<h3>🎁 Bonus: Adivina mi número secreto 🎁</h3>", unsafe_allow_html=True)
st.markdown("<p>Pensé un número entre 1 y 20... ¿lo adivinas?</p>", unsafe_allow_html=True)

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 20)

intento = st.number_input("Tu número:", min_value=1, max_value=20, step=1, key="intento")

if st.button("Adivinar 🎯"):
    if intento == st.session_state.numero_secreto:
        st.success("¡SÍ! ¡Lo adivinaste! Eres una genio 🌟")
        st.snow()
        st.session_state.numero_secreto = random.randint(1, 20)
    elif intento < st.session_state.numero_secreto:
        st.info("Un poquito más alto... 🔼")
    else:
        st.info("Un poquito más bajo... 🔽")

# ---------- FOOTER ----------
st.write("")
st.write("")
st.markdown("<p style='font-size:14px; opacity:0.7;'>Hecho con 💗 por tu papá</p>", unsafe_allow_html=True)
