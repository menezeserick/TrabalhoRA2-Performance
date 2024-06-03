from collections import deque

def inicializar_cache(tamanho_cache):
    """
    Inicializa a cache com tamanho especificado.

    Args:
        tamanho_cache: Tamanho da cache (número de linhas).

    Returns:
        Dicionário representando a cache (chave: posição, valor: estado).
    """
    cache = {}
    for i in range(tamanho_cache):
        cache[i] = -1 
    return cache

def imprimir_cache(cache):
    """
    Imprime o estado atual da cache.

    Args:
        cache: Dicionário representando a cache (chave: posição, valor: estado).
    """
    print("Tamanho da Cache:", len(cache))
    print(" -------------------")
    print("| Pos Cache | Posição Memória |")
    print(" -------------------")
    for posicao, estado in cache.items():
        print(f"| {posicao:2} | {estado:3} |")
    print(" -------------------")

def mapeamento_direto(tamanho_cache, posicoes_memoria_acessar):
    """
    Simula o mapeamento direto e imprime estatísticas de cache.

    Args:
        tamanho_cache: Tamanho da cache (número de linhas).
        posicoes_memoria_acessar: Lista com as posições de memória a serem acessadas.
    """
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)

    numero_hits = 0
    numero_misses = 0

    for posicao_memoria in posicoes_memoria_acessar:
        posicao_cache = posicao_memoria % tamanho_cache

        # verifica se o o endereço está presente na cache
        if cache[posicao_cache] == posicao_memoria:
            # hit na cache
            numero_hits += 1
            print(f"Hit na posição {posicao_cache} (memória {posicao_memoria})")
        else:
            # miss na cache
            numero_misses += 1
            print(f"Miss na posição {posicao_cache} (memória {posicao_memoria})")
            # atualiza a cache com o novo endereço
            cache[posicao_cache] = posicao_memoria

        imprimir_cache(cache)

    # imprime estatísticas finais
    print(" --------------------------------------")
    print(f"Total de posições de memória acessadas: {len(posicoes_memoria_acessar)}")
    print(f"Total de hits: {numero_hits}")
    print(f"Total de misses: {numero_misses}")
    print(f"Taxa de hit: {(numero_hits / len(posicoes_memoria_acessar)):.2f}")
    print(" --------------------------------------")

def inicializar_cache_associativa(tamanho_cache, tamanho_conjunto):
    """
    Inicializa a cache associativa por conjunto.

    Args:
        tamanho_cache: Tamanho total da cache (número de linhas).
        tamanho_conjunto: Tamanho do conjunto (número de linhas por conjunto).

    Returns:
        Dicionário representando a cache (chave: índice do conjunto, valor: lista de deque de estados).
    """
    numero_conjuntos = tamanho_cache // tamanho_conjunto
    cache = {i: deque(maxlen=tamanho_conjunto) for i in range(numero_conjuntos)}
    return cache

def imprimir_cache_associativa(cache):
    """
    Imprime o estado atual da cache associativa por conjunto.

    Args:
        cache: Dicionário representando a cache (chave: índice do conjunto, valor: lista de deque de estados).
    """
    print("Estado atual da Cache Associativa por Conjunto:")
    print(" -----------------------------------------")
    for indice_conjunto, conjunto in cache.items():
        print(f"Conjunto {indice_conjunto}: {list(conjunto)}")
    print(" -----------------------------------------")

def mapeamento_associativo_conjunto(tamanho_cache, tamanho_conjunto, posicoes_memoria_acessar):
    """
    Simula o mapeamento associativo por conjunto e imprime estatísticas de cache.

    Args:
        tamanho_cache: Tamanho da cache (número de linhas).
        tamanho_conjunto: Tamanho do conjunto (número de linhas por conjunto).
        posicoes_memoria_acessar: Lista com as posições de memória a serem acessadas.
    """
    cache = inicializar_cache_associativa(tamanho_cache, tamanho_conjunto)
    imprimir_cache_associativa(cache)

    numero_hits = 0
    numero_misses = 0

    for posicao_memoria in posicoes_memoria_acessar:
        indice_conjunto = posicao_memoria % (tamanho_cache // tamanho_conjunto)
        conjunto = cache[indice_conjunto]

        if posicao_memoria in conjunto:
            # hit na cache
            numero_hits += 1
            conjunto.remove(posicao_memoria)
            conjunto.append(posicao_memoria)
            print(f"Hit no conjunto {indice_conjunto} (memória {posicao_memoria})")
        else:
            # miss na cache
            numero_misses += 1
            if len(conjunto) >= conjunto.maxlen:
                print(f"Substituição no conjunto {indice_conjunto} (memória {posicao_memoria})")
            conjunto.append(posicao_memoria)
            print(f"Miss no conjunto {indice_conjunto} (memória {posicao_memoria})")

        imprimir_cache_associativa(cache)

    # imprime estatísticas finais
    print(" --------------------------------------")
    print(f"Total de posições de memória acessadas: {len(posicoes_memoria_acessar)}")
    print(f"Total de hits: {numero_hits}")
    print(f"Total de misses: {numero_misses}")
    print(f"Taxa de hit: {(numero_hits / len(posicoes_memoria_acessar)):.2f}")
    print(" --------------------------------------")

def comparar_mapemantos(tamanho_cache, tamanho_conjunto, posicoes_memoria_acessar):
    print("Mapeamento Direto:")
    mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)
    print("\nMapeamento Associativo por Conjunto:")
    mapeamento_associativo_conjunto(tamanho_cache, tamanho_conjunto, posicoes_memoria_acessar)

# Função principal com inputs do usuário
def main():
    tipo_operacao = input("Escolha a operação (direto/associativo/comparar): ").strip().lower()
    tamanho_cache = int(input("Informe o tamanho da cache: "))
    posicoes_memoria_acessar = list(map(int, input("Informe as posições de memória a serem acessadas (separadas por espaço): ").split()))

    if tipo_operacao == 'direto':
        mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)
    elif tipo_operacao == 'associativo':
        tamanho_conjunto = int(input("Informe o tamanho do conjunto (1, 2, 4, 8, 16): "))
        mapeamento_associativo_conjunto(tamanho_cache, tamanho_conjunto, posicoes_memoria_acessar)
    elif tipo_operacao == 'comparar':
        tamanho_conjunto = int(input("Informe o tamanho do conjunto para mapeamento associativo (1, 2, 4, 8, 16): "))
        comparar_mapemantos(tamanho_cache, tamanho_conjunto, posicoes_memoria_acessar)
    else:
        print("Tipo de operação inválido!")

# Executa a função principal
main()