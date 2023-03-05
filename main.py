def gera_primo_str(max_int: int):

  primos = [True] * max_int
  primos[0] = primos[1] = False

  for i, estado in enumerate(primos):
    if estado and i <= max_int**(1 / 2):
      for multiplo in range(i**2, max_int, i):
        primos[multiplo] = False

  return ''.join(f"{i}" for i, estado in enumerate(primos) if estado)


def gera_primo_string(func):
  max = 10_000
  primo_str = gera_primo_str(max)

  def envolto(n: int) -> str:
    nonlocal primo_str, max

    while n > len(primo_str):
      max *= 2
      primo_str = gera_primo_str(max * 2)

    return func(primo_str, n)

  return envolto


@gera_primo_string
def solution(primo_str, n: int) -> str:
  return primo_str[n:n + 5]


print(solution(3))

'''import time

start = time.time()
for n in range(10000):
  print(solution(n))
print(f'{(time.time() - start)} seconds')'''
