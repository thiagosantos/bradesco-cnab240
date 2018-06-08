import collections

def merge(original, novo):
    """Merge entre dois dicionários

    O primeiro parametro dicionário será sobrescrito pelo valor do segundo parametro dicionário
    forçando a conversão do conteúdo de cada indice do segundo dicionário para string.

    :param original: dicionario original (possivelmente modulo.default())
    :param novo: dicionario alterado (possivelmente uma alteração do odict vindo modulo.default())
    :type original: odict
    :type novo: odict
    :returns: odict original alterado com os valores do novo
    :rtype: odict

    .. todo:: adicionar recursividade
    """
    _keys = original.keys()
    for _key in _keys:
        if(_key in novo):
            original[_key] = str(novo[_key])
    
    return original