def contar_palavras(arquivo):
    # Abre o arquivo em modo de leitura
    with open(arquivo, 'r') as f:
        # Lê todo o conteúdo do arquivo e o divide em palavras
        palavras = f.read().split()

    # Inicializa um dicionário para armazenar a contagem de cada palavra
    contagem_palavras = {}

    # Itera sobre cada palavra no texto
    for palavra in palavras:
        # Remove possíveis caracteres especiais, como pontuações
        palavra_limpa = palavra.strip('.,!?"\'').lower()
        # Incrementa a contagem da palavra no dicionário
        contagem_palavras[palavra_limpa] = contagem_palavras.get(palavra_limpa, 0) + 1

    # Retorna o dicionário de contagem de palavras
    return contagem_palavras

def main():
    arquivo = input("Digite o caminho do arquivo de texto: ")

    try:
        # Chama a função para contar as palavras no arquivo
        contagem = contar_palavras(arquivo)
        
        # Imprime a contagem de palavras
        print("Contagem de palavras:")
        for palavra, quantidade in contagem.items():
            print(f"{palavra}: {quantidade}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__ == "__main__":
    main()
