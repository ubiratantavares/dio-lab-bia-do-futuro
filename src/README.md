# Código da Aplicação - BIA

Esta pasta contém o protótipo funcional do seu Agente Financeiro Inteligente.

## Estrutura Atual

```text
src/
├── app.py              # Interface Streamlit (Frontend + Chat)
├── agente.py           # Lógica do Agente (RAG e Integração LLM)
└── config.py           # Configurações de caminhos e System Prompt
```

## Como Rodar

1. Certifique-se de que o ambiente virtual está ativo:
   ```bash
   source venv/bin/activate
   ```

2. (Opcional) Configure suas chaves de API no arquivo `.env` (use `.env.example` como base).

3. Inicie a aplicação:

   ```bash
   streamlit run src/app.py
   ```

## Funcionalidades Implementadas
- **Dashboard Sidebar:** Visualização em tempo real do perfil e metas do João Silva.
- **Chat Inteligente:** Interface conversacional com a BIA.
- **RAG Lite:** O agente consegue analisar o CSV de transações e o catálogo de produtos para dar respostas baseadas em dados.
- **Gráficos:** Visualização simples de gastos por categoria.
