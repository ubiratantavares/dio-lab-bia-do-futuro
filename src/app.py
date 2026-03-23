import streamlit as st
import pandas as pd
import json
from config import DATA_DIR, SYSTEM_PROMPT
from agente import AgenteFinanceiro, integrate_llm

# Configuração da Página
st.set_page_config(page_title="BIA - Agente Financeiro", page_icon="🤖", layout="wide")

# Estilização Customizada
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stChatFloatingInputContainer {
        bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Central de Carregamento de Dados
@st.cache_data
def load_data():
    transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
    atendimento = pd.read_csv(DATA_DIR / "historico_atendimento.csv")
    
    with open(DATA_DIR / "perfil_investidor.json", "r") as f:
        perfil = json.load(f)
        
    with open(DATA_DIR / "produtos_financeiros.json", "r") as f:
        produtos = json.load(f)
        
    return transacoes, atendimento, perfil, produtos

transacoes, atendimento, perfil, produtos = load_data()

# Sidebar - Informações do Cliente
with st.sidebar:
    st.header("👤 Perfil do Cliente")
    st.write(f"**Nome:** {perfil['nome']}")
    st.write(f"**Perfil:** {perfil['perfil_investidor'].capitalize()}")
    st.write(f"**Renda Mensal:** R$ {perfil['renda_mensal']:,.2f}")
    
    st.divider()
    st.subheader("🎯 Metas")
    for meta in perfil['metas']:
        st.write(f"- **{meta['meta']}:** R$ {meta['valor_necessario']:,.2f} ({meta['prazo']})")

# Header Principal
st.title("🤖 BIA: Sua Consultora Inteligente")

# Resumo em Métricas (Dashboard Superior)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Salário Mensal", f"R$ {perfil['renda_mensal']:,.2f}")
with col_m2:
    st.metric("Reserva Atual", "R$ 11.000,00", "+R$ 1.000,00 📈")
with col_m3:
    meta_reserva = perfil['metas'][0]['valor_necessario']
    st.metric("Meta Reserva", f"R$ {meta_reserva:,.2f}", f"-R$ {meta_reserva - 11000:,.2f} restante")

st.divider()
st.info("Olá, João! Eu analisei seus dados de Outubro. Notei que você está a 73% de completar sua Reserva de Emergência. Quer uma dica para chegar lá mais rápido?")

# Área de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar com suas finanças hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Instancia o agente
        agente = AgenteFinanceiro(transacoes, perfil, produtos)
        
        # Tenta integração real com LLM, senão usa lógica de fallback do agente
        contexto_text = agente.get_context()
        response = integrate_llm(prompt, contexto_text)
        
        if not response:
            response = agente.gerar_resposta(prompt)
            
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Dashboards Rápidos (Dashboard de Apoio)
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gastos por Categoria")
    gastos_cat = transacoes[transacoes['tipo'] == 'saida'].groupby('categoria')['valor'].sum().reset_index()
    st.bar_chart(gastos_cat.set_index('categoria'))

with col2:
    st.subheader("Produtos Recomendados")
    st.table(pd.DataFrame(produtos)[['nome', 'rentabilidade', 'risco']])
