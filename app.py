import os

restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizza suprema', 'categoria' : 'Pizza', 'ativo' : True}, 
                {'nome':'Cantina', 'categoria': 'italiana', 'ativo': False}];

def exibir_nome_do_programa():
    print('''
      𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠
      ''');

def exibir_opcoes():
    print('1. Cadastrar restaurante');
    print('2. Listar restaurante');
    print('3. Alternar estado do restaurante');
    print('4. Sair\n');

def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ');
    main();

def opcao_invalida():
    print('Opção inválida!\n');
    voltar_ao_menu_principal();

def exibir_subtitulo(texto):
    '''essa função limpa o console e exibe o caractere *'''
    os.system('cls');
    linha = '*' * (len(texto));
    print(linha);
    print(texto);
    print(linha);
    print();

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
   
    Inputs:
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ');
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ');

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria' : categoria, 'ativo' : False}

    restaurantes.append(dados_do_restaurante);

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n');
    voltar_ao_menu_principal();

def listar_restaurantes():
    '''essa função armazena os restaurantes e lista eles'''
    exibir_subtitulo('Listando restaurantes ')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'];
        categoria = restaurante['categoria'];
        ativo = 'ativo' if restaurante['ativo'] else 'inativo';
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}');

    voltar_ao_menu_principal();

def alternar_estado_restaurante():
    '''essa função alterna o status do restaurante'''
    exibir_subtitulo('Alternando estado do restaurante');
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar estado: ');
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True;
            restaurante['ativo'] = not restaurante['ativo'];
            mensagem = f'O restaurante {nome_restaurante} agora está ativo com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem);
    
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado');


    voltar_ao_menu_principal();


def escolher_opcao():
    '''essa função captura a escolha do usuário no input'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '));
        # opcao_escolhida = int(opcao_escolhida);
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante();
        elif opcao_escolhida == 2:
            listar_restaurantes();
        elif opcao_escolhida == 3:
            alternar_estado_restaurante();
        elif opcao_escolhida == 4:
            finalizar_app();
        else:
            opcao_invalida();
    except:
        opcao_invalida();

def main():
    '''função main'''
    os.system('cls');
    exibir_nome_do_programa();
    exibir_opcoes();
    escolher_opcao();


if __name__ == '__main__':
    main()