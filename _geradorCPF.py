from tkinter import filedialog

try:
    X = input("Informe quantos CPFs gerar: ")
    if X.isdigit():
        i = 0
        ListaCPFs = []
        dir = filedialog.asksaveasfilename(title="Local onde você deseja salvar o arquivo:")
        while int(X) > i:
            from random import randint
            numero = str(randint(100000000, 999999999))
            File = open(dir, 'a')

            novo_cpf = numero                           # 9 números aleatórios
            reverso = 10                                # Contador reverso
            total = 0                                   # O total das multiplicações

            # Loop do CPF
            for index in range(19):
                if index > 8:                           # Primeiro índice vai de 0 a 9,
                    index -= 9                          # São os 9 primeiros digitos do CPF

                    total += int(novo_cpf[index]) * reverso # Valor total da multiplicação

                    reverso -= 1                            # Decrementa o contador reverso
                    if reverso < 2:
                        reverso = 11
                        d = 11 - (total % 11)

                        if d > 9:                           # Se o digito for > que 9 o valor é 0
                            d = 0
                        total = 0                           # Zera o total
                        novo_cpf += str(d)                  # Concatena o digito gerado no novo cpf
            ListaCPFs.append(novo_cpf)
            File.write(novo_cpf+';\n')
            print(novo_cpf)
            i += 1            
            File.close()
        print("{} CPFs gerados com sucesso!".format(X))
        print("Obrigado!")
    else:
        print("Valor digitado não é um numero inteiro.")
except TypeError:
    print("Ação inválida. Programa encerrado!")
