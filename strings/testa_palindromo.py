def eh_palindromo(string_testada):
    '''
    Recebe string e retorna se é palindromo
    antes tira todos os espaços, e coloca em lower
    :param string_testada:
    :return:
    '''
    string_testada = "".join([s.lower() for s in string_testada if s != " "])
    tamanho_string = len(string_testada)
    metade_tamanho = tamanho_string // 2 # faz divisao inteiria para ignorar impares

    for idx in range(metade_tamanho):
        rabeira = (idx+1)*-1
        if string_testada[idx] != string_testada[rabeira]:
            return False

    return True



