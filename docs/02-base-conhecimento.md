# Base de Conhecimento

## Dados Utilizados

O agente utiliza a base de dados mockada completa para garantir um contexto 360º do cliente João Silva:

| Arquivo | Formato | Utilização no Agente |
| --- | --- | --- |
| `historico_atendimento.csv` | CSV | Utilizado para saber que João já perguntou sobre CDB e Tesouro Selic no passado. |
| `perfil_investidor.json` | JSON | Base para determinar o risco aceitável e as metas vigentes (Reserva/Apartamento). |
| `produtos_financeiros.json` | JSON | Catálogo de produtos usados para sugerir onde colocar a economia mensal. |
| `transacoes.csv` | CSV | Fonte principal para análise de fluxo de caixa e identificação de excessos de gastos. |

> [!TIP]
> Os dados em `transacoes.csv` foram expandidos para cobrir um mês completo (Outubro/2025), permitindo que o agente calcule a "sobra" mensal com precisão.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim. Expandi o histórico de transações em `data/transacoes.csv` para incluir despesas recorrentes (Internet, Conta de Luz) e uma transação simbólica de investimento, a fim de testar se o agente reconhece hábitos disciplinados.

---

## Estratégia de Integração

### Como os dados são carregados?

> Descreva como seu agente acessa a base de conhecimento.

Os arquivos são carregados via `pandas` (CSV) e `json.load` (JSON) no carregamento inicial da aplicação Streamlit. Eles são convertidos em representações de texto estruturado (Markdown/YAML) para serem incluídos no contexto da janela de conversa da LLM.

### Como os dados são usados no prompt?

> Os dados vão no system prompt? São consultados dinamicamente?

O perfil do investidor e as metas são incluídos no **System Prompt**. Já as transações e o catálogo de produtos são inseridos dinamicamente conforme a necessidade da pergunta do usuário (RAG Lite).

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```text
Dados do Cliente:
CONTEXTO DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Saldo p/ Reserva de Emergência: R$ 10.000 (Meta: R$ 15.000)

RESUMO DE GASTOS (OUT/2025):
- Moradia: R$ 1.500
- Alimentação: R$ 870
- Lazer/Streaming: R$ 55.90
- Transferência p/ Investimento: R$ 1.000
```
