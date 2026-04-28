import streamlit as st

st.set_page_config(page_title="Reabilitação de Joelho", layout="centered")

# CABEÇALHO
st.title("🦵 Programa de Reabilitação")
st.subheader("Dr. Cássio Prado")

# LGPD
st.warning("⚠️ Este aplicativo é educativo e não substitui consulta médica.")
st.info("🔒 Não insira dados pessoais. Nenhuma informação é armazenada.")

# CONSENTIMENTO
st.markdown("### 📄 Consentimento")
consent = st.checkbox("Estou ciente e autorizo o uso deste aplicativo.")

if not consent:
    st.stop()

st.success("Consentimento aceito")

# DOR
st.markdown("---")
st.subheader("📊 Dor hoje")
dor = st.slider("Escala de dor", 0, 10, 5)
st.progress(dor/10)

# FASE
fase = st.selectbox("Fase do tratamento", ["Fase 1", "Fase 2", "Fase 3"])

# EXERCÍCIOS
st.subheader("🏋️ Exercícios")

if fase == "Fase 1":
    st.write("• Alongamento posterior 3x30s")
    st.write("• Elevação de perna (SLR) 3x12")
    st.write("• Clamshell 3x15")

elif fase == "Fase 2":
    st.write("• Agachamento 60°")
    st.write("• Step-up")
    st.write("• Nordic")

else:
    st.write("• Corrida leve")
    st.write("• Funcional")

# VÍDEOS (FUNCIONAM)
st.subheader("🎥 Demonstração")

st.video("https://www.youtube.com/watch?v=v7AYKMP6rOE")
st.video("https://www.youtube.com/watch?v=1xMaFs0L3ao")
st.video("https://www.youtube.com/watch?v=EG5_gXcfozw")

# BOTÃO
if st.button("Finalizar treino"):
    st.success("Treino concluído!")

# FINAL
st.markdown("---")
st.caption("Aplicativo educativo. Não substitui avaliação médica.")
