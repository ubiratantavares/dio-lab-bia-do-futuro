import pandas as pd
import json
from config import SYSTEM_PROMPT, OPENAI_API_KEY, GOOGLE_API_KEY

class AgenteFinanceiro:
    def __init__(self, transacoes, perfil, produtos):
        if transacoes is None or perfil is None:
            raise ValueError("Transações e Perfil são obrigatórios para o Agente.")
        self.transacoes = transacoes
        self.perfil = perfil
        self.produtos = produtos
        self.system_prompt = SYSTEM_PROMPT

    def get_context(self):
        try:
            # Consolida o contexto em texto para a LLM
            resumo_gastos = self.transacoes[self.transacoes['tipo'] == 'saida'].groupby('categoria')['valor'].sum().to_dict()
            gastos_texto = "\n".join([f"- {cat}: R$ {val:,.2f}" for cat, val in resumo_gastos.items()])
            
            # Cálculo de progresso da meta principal
            meta_principal = self.perfil['metas'][0]
            saldo_atual = 11000 # Valor fixo para o MVP do João
            falta = max(0, meta_principal['valor_necessario'] - saldo_atual)
            
            contexto = f"""
            NOME: {self.perfil['nome']}
            PERFIL: {self.perfil['perfil_investidor']}
            RENDA MENSAL: R$ {self.perfil['renda_mensal']}
            
            RESUMO DE GASTOS DO MÊS:
            {gastos_texto}
            
            META ATUAL: {meta_principal['meta']}
            VALOR NECESSÁRIO: R$ {meta_principal['valor_necessario']:,.2f}
            SALDO DISPONÍVEL: R$ {saldo_atual:,.2f}
            FALTA PARA META: R$ {falta:,.2f}
            """
            return contexto
        except Exception as e:
            return f"Erro ao processar contexto: {str(e)}"

    def gerar_resposta(self, user_query):
        # Aqui integraria com OpenAI ou Gemini. 
        # Como não temos a chave ativa, retornaremos um raciocínio baseado nas regras.
        
        contexto = self.get_context()
        
        # Lógica de fallback/raciocínio local para o MVP
        if "investir" in user_query.lower() or "rendimento" in user_query.lower():
            return f"João, com base no seu perfil {self.perfil['perfil_investidor']}, recomendo focar inicialmente no Tesouro Selic para terminar sua Reserva de Emergência. Faltam apenas R$ 4.000 para a meta!"
        
        if "gastos" in user_query.lower() or "outubro" in user_query.lower():
            return "Analisando seu mês, vi que os gastos com Alimentação foram os mais altos. Se conseguirmos reduzir 10% nessa categoria, você ganha fôlego para investir mais no apartamento."

        return f"Olá! Sou a BIA. Analisei suas finanças: {contexto}. Como posso ajudar especificamente?"

def integrate_llm(prompt, context):
    """
    Função preparada para integração real com OpenAI ou Google Gemini.
    """
    if GOOGLE_API_KEY:
        import google.generativeai as genai
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"{SYSTEM_PROMPT}\n\nCONTEXTO REAL:\n{context}\n\nUSUÁRIO: {prompt}")
        return response.text
    elif OPENAI_API_KEY:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"CONTEXTO: {context}\n\nPERGUNTA: {prompt}"}
            ]
        )
        return response.choices[0].message.content
    else:
        return None
