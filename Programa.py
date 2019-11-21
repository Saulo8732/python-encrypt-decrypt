import pyAesCrypt

print("""
######################################################
# Programa de encriptação e desencriptação em Python #
######################################################
""")

bufferSize = 64 * 1024

while(True):
    print("\nPor favor selecione a opção desejada:\n1 - Encriptar um arquivo\n2 - Desencriptar um arquivo\n3 - Sair\n")

    opcao = int(input())
    if(opcao == 1):
        nomeArquivo = input("\nPor favor insira o nome do arquivo a ser encriptado:\n")
        senha = input("\nPor favor defina uma senha para o arquivo a ser encriptado:\n")
        input("Pressione ENTER para iniciar a encriptação.")
        pyAesCrypt.encryptFile(nomeArquivo, nomeArquivo+".aes", senha, bufferSize)
        print("Encriptação concluida! Nome do arquivo gerado: "+ nomeArquivo+".aes");
    elif(opcao == 2):
        nomeArquivo = input("\nPor favor insira o nome do arquivo a ser desencriptado:\n")
        senha = input("\nPor favor insira a senha para o arquivo a ser desencriptado:\n")
        input("Pressione ENTER para iniciar a desencriptação.")
        nomeArquivoFuturo = "RESULTADO"+nomeArquivo[:-4]
        pyAesCrypt.decryptFile(nomeArquivo, nomeArquivoFuturo, senha, bufferSize)
        print("Desencriptação concluida! Nome do arquivo gerado: "+ nomeArquivoFuturo);

    elif (opcao == 3):
        print("Bye bye...")
        break
    else:
        print("\nOPÇÃO INVÁLIDA!\n")
    

