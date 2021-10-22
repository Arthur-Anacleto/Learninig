from time import sleep

menu = ''
nome = []
data = 0
dias_vacinacao = []
hora = []
vacinados_coronavac = 0
vacinados_astrazeneca = 0
vacinados_pfizer = 0
total_vacinados = 0
saldo_pfizer = 0
saldo_coronavac = 0
saldo_astrazeneca = 0
media_total = 0
media_pfizer = 0
media_coronavac = 0
media_astrazeneca = 0
while menu != '6':
    print('- ' * 10, 'Sistema de Controle Covid', '- ' * 10)
    menu = str(input('[ 1 ] Registrar uma vacinação\n[ 2 ] Adicionar estoque de uma vacina\n[ 3 ] Obter número total '
                     'de vacinados\n[ 4 ] Obter média de vacinação diária\n[ 5 ] Obter a quantidade atual de doses de '
                     'um tipo de vacina\n[ 6 ] Fechar programa\nSelecione uma das opções acima: '))
    if menu == '1':
        tipo_vacina = str(input('Você selecionou opção 1!\nAs opções de vacina são.\n[ 1 ] Pfizer\n[ 2 ] Coronavac\n'
                                '[ 3 ] Astrazeneca\n[ 4 ] Menu anterior\n''Escolha uma das opções. '))
        while not tipo_vacina.isdigit():
            tipo_vacina = str(input('Digite apenas números\nAs opções de vacina são.\n[ 1 ] Pfizer\n[ 2 ] Coronavac\n'
                                    '[ 3 ] Astrazeneca\n[ 4 ] Menu anterior\n''Escolha uma das opções. '))
        if tipo_vacina.isdigit():
            if int(tipo_vacina) == 1 and saldo_pfizer > 0:
                vacinados_pfizer += 1
                saldo_pfizer -= 1
                nome.append(str(input('Digite o nome da pessoa que vai ser vacinada. ')))
                hora.append(str(input('Digite a hora da vacinação utilizando dois dígitos. ')))
                data = int(input('Digite o dia da vacinação com dois dígitos '))
                if data not in dias_vacinacao:
                    dias_vacinacao.append(data)
            elif int(tipo_vacina) == 2 and saldo_coronavac > 0:
                vacinados_coronavac += 1
                saldo_coronavac -= 1
                nome.append(str(input('Digite o nome da pessoa que vai ser vacinada. ')))
                hora.append(str(input('Digite a hora da vacinação utilizando dois dígitos. ')))
                data = int(input('Digite o dia da vacinação com dois dígitos '))
                if data not in dias_vacinacao:
                    dias_vacinacao.append(data)
            elif int(tipo_vacina) == 3 and saldo_astrazeneca > 0:
                vacinados_astrazeneca += 1
                saldo_astrazeneca -= 1
                nome.append(str(input('Digite o nome da pessoa que vai ser vacinada. ')))
                hora.append(str(input('Digite a hora da vacinação utilizando dois dígitos. ')))
                data = int(input('Digite o dia da vacinação com dois dígitos '))
                if data not in dias_vacinacao:
                    dias_vacinacao.append(data)
            elif int(tipo_vacina) == 4:
                menu = ''
            elif int(tipo_vacina) > 4:
                print('Opção inválida. Escolha uma opção válida!\nAguarde retorno do menu principal.')
                sleep(2)
                menu = ''
            else:
                print('Opção inválida. Verifique o saldo da vacina escolhida!\nAguarde retorno do menu principal.')
                sleep(2)
                menu = ''
    elif menu == '2':
        adiciona_vacina = str(input('Você selecionou opção 2!\nAs opções de vacina são.\n[ 1 ] Pfizer\n[ 2 ] '
                                    'Coronavac\n[ 3 ] Astrazeneca\n[ 4 ] Menu anterior\n'
                                    'Digite a opção da vacina para adicionar saldo em estoque. '))
        while not adiciona_vacina.isdigit():
            adiciona_vacina = str(input('Digite apenas números!\nAs opções de vacina são.\n[ 1 ] Pfizer\n[ 2 ] '
                                        'Coronavac\n[ 3 ] Astrazeneca\n[ 4 ] Menu anterior\nDigite a opção da vacina '
                                        'para adicionar saldo em estoque. '))
        if adiciona_vacina in '123':
            qtd_vacina = ''
            while not qtd_vacina.isdigit():
                qtd_vacina = str(input('Digite a quantidade de vacinas para adicionar ao estoque.'))
            if adiciona_vacina == '1':
                saldo_pfizer += int(qtd_vacina)
            elif adiciona_vacina == '2':
                saldo_coronavac += int(qtd_vacina)
            elif adiciona_vacina == '3':
                saldo_astrazeneca += int(qtd_vacina)
        elif adiciona_vacina == '4':
            print(f'Você selecionou a opção {adiciona_vacina}. Retornando ao menu principal.')
            menu = ''
        else:
            print('Opção inválida. Selecione uma opção válida!\nAguarde retorno do menu principal.')
            sleep(2)
            menu = ''
    elif menu == '3':
        total_vacinados = vacinados_pfizer + vacinados_coronavac + vacinados_astrazeneca
        print(f'Você selecionou opção 3!\nRelatório de vacinação!\n[ 1 ] Pfizer {vacinados_pfizer} vacinas aplicadas\n'
              f'[ 2 ] Coronavac {vacinados_coronavac} vacinas aplicadas\n[ 3 ] Astrazeneca {vacinados_astrazeneca} '
              f'vacinas aplicadas\n[ 4 ] Totalizando {total_vacinados} vacinas aplicadas')
        sleep(4)
    elif menu == '4':
        if len(dias_vacinacao) > 0:
            total_vacinados = vacinados_pfizer + vacinados_coronavac + vacinados_astrazeneca
            media_total = total_vacinados / (len(dias_vacinacao))
            media_pfizer = vacinados_pfizer / (len(dias_vacinacao))
            media_coronavac = vacinados_coronavac / len(dias_vacinacao)
            media_astrazeneca = vacinados_astrazeneca / len(dias_vacinacao)
            print(f'A média total de vacinados é de {media_total} pessoas por dia.\n'
                  f'A média de vacinados com pfizer é de {media_pfizer} pessoas por dia.\n'
                  f'A média de vacinados com coronavac é de {media_coronavac} pessoas por dia.\n'
                  f'A média de vacinados com astrazeneca é de {media_astrazeneca} pessoas por dia.\n')
        else:
            print('Não há registro de vacinação. Por favor realize ao menos um registro.')
    elif menu == '5':
        consulta_saldo = str(input('Você selecionou opção 5!\nAs opções de vacina são.\n[ 1 ] Pfizer\n[ 2 ] Coronavac\n'
                                   '[ 3 ] Astrazeneca\n[ 4 ] Total Geral\n[ 5 ] Menu anterior\n'
                                   'Digite a opção da vacina para verificar o saldo em estoque.'))
        while not consulta_saldo.isdigit():
            consulta_saldo = str(input('Digite apenas números.\nAs opções de vacina são.\n[ 1 ] Pfizer\n[ 2 ] '
                                       'Coronavac\n[ 3 ] Astrazeneca\n[ 4 ] Total Geral\n[ 5 ] Menu anterior\n'
                                       'Digite a opção da vacina para verificar o saldo em estoque.'))
        if consulta_saldo == '1':
            print(f'O saldo de vacinas Pfizer é de {saldo_pfizer} vacinas.')
        elif consulta_saldo == '2':
            print(f'O saldo de vacinas Coronavac é de {saldo_coronavac} vacinas.')
        elif consulta_saldo == '3':
            print(f'O saldo de vacinas Astrazeneca é de {saldo_astrazeneca} vacinas.')
        elif consulta_saldo == '4':
            total_vacinas = saldo_pfizer + saldo_coronavac + saldo_astrazeneca
            print(f'O saldo total de vacinas é de {total_vacinas}.')
        elif consulta_saldo == '5':
            print(f'Você selecionou a opção {consulta_saldo}. Retornando ao menu principal.')
        else:
            print('Opção inválida. Selecione uma opção válida!\nAguarde retorno do menu principal.')
            sleep(2)
            menu = ''
    elif menu == '6':
        print('Ogrigado por utilizar nosso programa!\nFinalizando!!!')
        sleep(3)
    else:
        print('Opção inválida. Selecione uma opção válida!\nDigite apenas números e aguarde retorno do menu.')
        sleep(2)
        menu = ''
