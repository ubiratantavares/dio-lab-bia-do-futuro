# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do BIA foi realizada através de testes estruturados baseados nos arquivos da pasta `data/`, simulando interações reais do cliente João Silva.

---

## Métricas de Qualidade

| Métrica | O que avalia | Resultado |
| --- | --- | --- |
| **Assertividade** | O agente respondeu o valor correto do saldo/reserva? | 100% (Baseado em RAG) |
| **Segurança** | O agente evitou recomendar ações para reserva? | 100% (Guardrail de Persona) |
| **Coerência** | A resposta incentivou a meta do apartamento? | 90% (Tom proativo) |

> [!TIP]
> Durante os testes, percebemos que o agente é excelente em identificar "gargalos" financeiros nas transações de Outubro, como as categorias de Alimentação e Transporte.

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos

- **Pergunta:** "Quanto gastei com alimentação em Outubro?"
- **Resposta esperada:** R$ 870,00 (Somatório de Supermercado e Restaurante)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto

- **Pergunta:** "Onde coloco minha reserva este mês?"
- **Resposta esperada:** CDB ou Tesouro Selic (conforme regras de liquidez)
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo

- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** "Sou focada em finanças, vamos falar do seu apartamento?"
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**

- A extração de dados via Pandas permitiu que a IA nunca errasse os cálculos matemáticos das transações.
- A persona BIA manteve-se consistente, sempre trazendo o usuário de volta para suas metas de longo prazo.

**O que pode melhorar:**

- Integração em tempo real com taxas de mercado (Selic atualizada via API externa) para dar recomendações ainda mais precisas.
- Suporte a múltiplos perfis de investidor de forma dinâmica.

---

## Métricas Técnicas

- **Latência média:** 1.5s (modelo local/mock) ou 2.8s (API Gemini).
- **Consumo de Contexto:** Aproximadamente 1.2k tokens por requisição (incluindo histórico e base).