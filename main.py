# Função principal do programa
def main():
    chosen_option = 0
    option_description = [
        (1, "Entrar com as medidas para cada aresta do terreno e para\nas ruas de plantio, conforme topologia a ser apresentada\n"),
        (2, "Atualizar medida já informada\n"),
        (3, "Apagar dados já informados\n"),
        (4, "Calcular o consumo de insumos para as culturas\n"),
        (5, "Gerar dados de análise estatística\n"),
        (6, "Exibir previsão meteorológica para o município\n"),
        (7, "Sair do programa")
    ];

    print("   ______                     _______        _     \t")
    print("  |  ____|                   |__   __|      | |    \t")
    print("  | |__ __ _ _ __ _ __ ___      | | ___  ___| |__  \t")
    print("  |  __/ _` | '__| '_ ` _ \\     | |/ _ \\/ __| '_ \\ \t")
    print("  | | | (_| | |  | | | | | |    | |  __/ (__| | | |\t")
    print("  |_|  \\__,_|_|  |_| |_| |_|    |_|\\___|\\___|_| |_|\t")
    print("_____________________________________________________\t\n")

    print("FarmTech Solutions - Sistema de Agricultura Digital\n")
    print("O sistema é responsável por fazer a gestão das duas culturas de\ncana-de-açúcar e milho nas fazendas e calcular o consumo de insumos\nnecessários para o plantio, cultivo e colheita.\n")

    while chosen_option != len(option_description):

        # Impressão do menu no console
        print("\n**************Menu do Sistema**************\n")
        for (option, description) in option_description:
            if option in [2,3,4,5] and len(area_metrics) < 5:
                continue
            print(f"[{option}] - {description}")

        print("*******************************************\n")
        # Leitura e validação da opção escolhida
        chosen_option = input("Digite a opção desejada [número do item]: ")

        if not chosen_option.isdigit():
            print("Opção inválida. Selecione uma das opções disponíveis entre 1 e 7.\n\n")
            chosen_option = 0
        else:
            chosen_option = int(chosen_option)
            if chosen_option < 1 or chosen_option > 7:
                print("Opção inválida. Selecione uma das opções disponíveis entre 1 e 7.\n\n")
                chosen_option = 0
            else:
                match chosen_option:
                    case 1:
                        print("Captura das medidas")
                    case 2:
                       print("Atualizar medidas")
                    case 3:
                        print("Apagar medidas")
                    case 4:
                        print("Calcular consumo de insumos")
                    case 5:
                        print("Gerar estatística em R")
                    case 6:
                        print("Exibir previsão meteorológica para o município\n")
                    case 7:
                        print("Saindo do programa...\n")
                        break
                    case _:
                        print("Opção inválida. Selecione uma das opções disponíveis entre 1 e 5.\n\n")

# Execução do função principal do programa
main()