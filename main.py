import topology

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
    ]

    area_metrics = {}

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
                        print("\n\nA Topologia da área de cultivo é apresentada abaixo.")
                        print("_______________________________________________________________")
                        print(" |-> Informe o valor de cada medida para as arestas do terreno e para as ruas de plantio,\nconforme as referências nomeadas no diagrama como forma de orientação:\n")
                        print("   |-> L1, L2 e L3 são medidas laterais do terreno cultivado")
                        print("   |-> R1 e R2 são medidas de largura das ruas de plantio")
                        print("     |-> Plantio de milho delineado com 2 ruas horizontais")
                        print("     |-> Plantio de cana-de-açúcar delineado com 4 e 6 ruas verticais\nem cada uma das áreas, respectivamente.")
                        print("       |-> Vale ressaltar que uma das ruas na área trapezoidal (Cana-de-Açúcar) é de formato triangular.")
                        print("   |-> Os caracteres de formato quadrado (▢) representam o espaçamento entre as ruas de plantio.")
                        topology.print_topology()

                        print("\nEntrada de medidas conforme a topologia exibida\n(somente números - separe casa decimais usando o '.'): ")
                        print("_______________________________________________________________\n")

                        area_constraints = [
                            ('L1', '(EXTENSÃO das ruas de plantio de MILHO)'),
                            ('R1', '(LARGURA das ruas de plantio de MILHO)'),
                            ('L2', '(EXTENSÃO das ruas de plantio de CANA-DE-AÇÚCAR\nNA ÁREA DE PLANTIO 1)'),
                            ('R2', '(LARGURA das ruas de plantio de CANA-DE-AÇÚCAR\n PARA AMBAS AS ÁREAS)'),
                            ('L3', '(EXTENSÃO das ruas de plantio de CANA-DE-AÇÚCAR\nNA ÁREA DE PLANTIO 2)')]
                        for constraint in area_constraints:
                            constraint_str = input(f"Informe o valor de {constraint[0]} {constraint[1]} em metros: ")
                            while True:
                                if not constraint_str.replace('.','',1).isdigit():
                                    print("Valor inválido. Informe um número válido.")
                                    constraint_str = input(f"Informe o valor de {constraint[0]} {constraint[1]} em metros: ")
                                    continue
                                else:
                                    break
                            area_metrics[constraint[0]] = float(constraint_str)
                        print("\nMedidas recebidas e atualizadas com sucesso!\n")

                    case 2:
                        if len(area_metrics) < 5:
                            print("Não há medidas suficientes informadas para atualização. Informe as medidas para que essa opção esteja disponível.\n")
                        chosen_option = "s"
                        while True:
                            measure = input("Entre com a medida a ser atualizada (L1, R1, L2, R2, L3)\nou digite 'S' para voltar ao menu anterior: ")
                            if measure.lower() == "s":
                                break
                            if measure not in area_metrics.keys():
                                print("Medida inválida. Informe uma das medidas já informadas.\n")
                                continue
                            new_value = float(input(f"Entre com o novo valor para {measure}: "))
                            area_metrics[measure] = new_value
                            print(area_metrics)
                            print(f"\nMedida {measure} atualizada com sucesso para {new_value} metros.\n")
                    case 3:
                        if len(area_metrics) < 5:
                            print("Não há medidas informadas para apagar. Informe as medidas para que essa opção esteja disponível.\n")
                        else:
                            area_metrics.clear()
                        print("Medidas e arquivos de transferência apagadas com sucesso.\n\n")
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