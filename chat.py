import openai
from prompt_toolkit import prompt

# Defina sua chave de API da OpenAI
openai.api_key = "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"

# Defina o modelo que você deseja usar (pode ser "text-davinci-002" para uma versão mais avançada)
model_engine = "text-davinci-001"

# Inicialize o modelo
def get_model():
    return openai.Model(engine=model_engine)

# Função principal que roda o ChatBot
def chat(prompt_text, model, length=50):
    response = model.generate(
        prompt=prompt_text,
        max_length=length,
        temperature=0.7,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text.strip()
    return message

# Loop principal para continuar a conversa
while True:
    # Obtém a entrada do usuário
    user_input = prompt("Você: ")
    
    # Obter a resposta do modelo GPT-2
    bot_response = chat(user_input, get_model())
    
    # Imprime a resposta do ChatBot
    print("ChatBot: " + bot_response)
