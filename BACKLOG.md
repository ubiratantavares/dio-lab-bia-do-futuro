# Backlog de Desenvolvimento - Agente BIA (Refinado)

Este backlog detalha as etapas de construção do Assistente Financeiro Inteligente.

## 📅 Cronograma

### Semana 1: Fundação e Estratégia de Dados

**Objetivo:** Definir a inteligência do agente e preparar os dados.

- [x] **Definição do Escopo:** Escolher o problema financeiro específico (ex: reserva de emergência).
- [x] **Persona e Tom de Voz:** Definir o nome e comportamento do agente.
- [x] **Preparação da Base:** Revisar e adaptar os arquivos `data/` para o caso de uso.
- [x] **Documentação:** Completar `01-documentacao-agente.md` e `02-base-conhecimento.md`.

---

### Semana 2: Engenharia de Prompts e Lógica

**Objetivo:** Construir o "cérebro" do agente.

- [x] **System Prompt:** Desenvolver o prompt principal com regras e restrições.
- [x] **Few-Shot Prompting:** Criar exemplos de interação para guiar a LLM.
- [x] **Testes Manuais:** Validar se o agente responde corretamente.
- [x] **Documentação:** Completar `03-prompts.md`.

---

### Semana 3: Desenvolvimento do Protótipo (MVP)

**Objetivo:** Implementar a aplicação funcional.

- [x] **Setup do Ambiente:** Criar `requirements.txt` e `config.py`.
- [x] **Interface (UI):** Desenvolver a estrutura básica em Streamlit (`app.py`).
- [x] **Integração RAG:** Implementar a lógica para o agente ler os arquivos CSV/JSON.
- [x] **Conexão LLM:** Integrar com a API (OpenAI/Gemini) ou modelo local.

---

### Semana 4: Finalização e Refinamento

**Objetivo:** Validar a solução, refinar a experiência e preparar a entrega.

- [x] **Avaliação:** Realizar testes estruturados e documentar em `04-metricas.md`.
- [x] **Refinamento:** Melhorar tratamento de erros e interface visual.
- [x] **Pitch:** Criar roteiro em `05-pitch.md`.
- [x] **Entrega Final:** Revisão completa de todo o repositório.

## 🚀 Dicas de Sucesso

- **Persona (BIA):** Mantenha o tom pedagógico.
- **Segurança:** Nunca exponha dados sensíveis como senhas ou CPFs.
