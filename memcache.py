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

# exemplo de uso(pode ser adicionado um input de usuário)
posicoes_memoria_acessar = [33,11,3,5]
tamanho_cache = 5

mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)