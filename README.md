# 🤖 BIA: Sua Consultora Financeira Inteligente

Bem-vindo ao repositório da **BIA** (Business Intelligence Assistant), um agente financeiro proativo desenvolvido para transformar a gestão de finanças pessoais através de IA Generativa.

## 🌟 O que é a BIA?

A BIA é mais do que um chatbot; é uma consultora financeira que utiliza a técnica de **RAG (Retrieval-Augmented Generation)** para analisar os dados reais do cliente (João Silva) e fornecer insights proativos sobre metas, gastos e investimentos.

### Principais Funcionalidades
- **Análise Proativa:** Identifica gargalos financeiros em seus gastos mensais.
- **Gestão de Metas:** Acompanhamento em tempo real da Reserva de Emergência e metas de longo prazo.
- **Sugestões Educativas:** Recomenda produtos financeiros adequados ao perfil de risco do usuário.
- **Interface Moderna:** Dashboard interativo construído com Streamlit.

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para iniciar a BIA em seu ambiente local:

### 1. Preparar o Ambiente
Clone o repositório e crie o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuração (Opcional)
Renomeie o arquivo `.env.example` para `.env` e adicione sua chave de API (OpenAI ou Google Gemini) para habilitar as respostas inteligentes. Caso contrário, a BIA funcionará com lógica de resposta simulada (Mock).

### 3. Iniciar a Aplicação
```bash
streamlit run src/app.py
```

---

## 📁 Estrutura do Repositório

```text
.
├── BACKLOG.md           # Planejamento completo das 4 semanas
├── requirements.txt      # Dependências do projeto
├── data/                 # Base de dados (CSV/JSON)
├── docs/                 # Documentação detalhada do agente
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── src/                  # Código-fonte da aplicação Streamlit
```

---

## 📄 Documentação do Projeto

O desenvolvimento seguiu uma trilha estruturada de 4 semanas:
1. **Semana 1:** [Documentação e Base de Conhecimento](docs/01-documentacao-agente.md)
2. **Semana 2:** [Engenharia de Prompts](docs/03-prompts.md)
3. **Semana 3:** [Arquitetura e Desenvolvimento](src/README.md)
4. **Semana 4:** [Métricas e Pitch](docs/04-metricas.md)

---

## 🎥 Pitch Final
O roteiro para a apresentação de 3 minutos está disponível em: [`docs/05-pitch.md`](docs/05-pitch.md).

---

## 🛡️ Segurança e Privacidade
Este protótipo foi construído com guardrails estritos para garantir que dados sensíveis (senhas, CPFs) nunca sejam compartilhados ou acessados inapropriadamente pela IA.
