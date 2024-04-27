import random
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    # Listas de caracteres que podem ser usados para gerar a senha
    caracteres = []
    
    if incluir_maiusculas:
        caracteres.extend(string.ascii_uppercase)  # Adiciona letras maiúsculas
    
    if incluir_minusculas:
        caracteres.extend(string.ascii_lowercase)  # Adiciona letras minúsculas
    
    if incluir_numeros:
        caracteres.extend(string.digits)  # Adiciona números
    
    if incluir_especiais:
        caracteres.extend(string.punctuation)  # Adiciona caracteres especiais
    
    # Certifique-se de ter pelo menos um tipo de caractere disponível
    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    
    # Gera uma senha aleatória com base nos caracteres disponíveis e no tamanho desejado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Exemplo de uso
senha_gerada = gerar_senha(tamanho=16, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True)
print("Senha gerada:", senha_gerada)