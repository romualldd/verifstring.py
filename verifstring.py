def verifica_letra_a(texto):
    texto = texto.lower()
    
    ocorrencia = texto.count('a')
    
    if ocorrencia > 0:
        print(f"A letra 'a' (ou 'A') ocorre {ocorrencia} vez(es) no texto.")
    else:
        print("A letra 'a' (ou 'A') não ocorre no texto.")

def main():
    texto = input("Digite um texto: ")
    
    verifica_letra_a(texto)

if __name__ == "__main__":
    main()
