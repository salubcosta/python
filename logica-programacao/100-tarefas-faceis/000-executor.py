# Arquivo criado para rodar os outros arquivos dos exercícios propostos.
# Esta é uma forma de não precisar ficar escrevendo o nome do arquivo para rodar
import os
import subprocess

# Caminho da pasta onde está o script:
pasta_arquivo = os.path.dirname(os.path.abspath(__file__))

exercicio = input("Informe o número do exercício: ").strip()

arquivos = [f for f in os.listdir(pasta_arquivo) if f.startswith(exercicio) and f.endswith(".py")]

if not arquivos:   
    print(f"Nenhum arquivo encontrado com o número {exercicio}")
elif len(arquivos) > 1:
    print(f"Mais de um arquivo encontrado para o número {exercicio}")
    for item in arquivos:
        print(f"- {item}")
    print("Por favor, seja mais específico!")
else:
    arquivo_para_executar = arquivos[0]
    print(f"Executando: {arquivo_para_executar}\n")
    subprocess.run(["python", os.path.join(pasta_arquivo, arquivo_para_executar)])