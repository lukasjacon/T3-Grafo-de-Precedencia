from multiprocessing import Process, Semaphore
from time import sleep


def down(semaforo):
    semaforo.acquire()


def up(semaforo):
    semaforo.release()
    

def a(t, n, semaforo_b_c):
    print(f"A iniciando contagem (n={n}; t={t})", end="\n", flush=True)
    for i in range(1, n + 1):
        sleep(t)
        print(f'A: {i}')
    print(f"A Finalizando contagem", end="\n", flush=True)
    # Depois da contagem libera o B e C
    up(semaforo_b_c)
    up(semaforo_b_c)


def b(t, n, semaforo_b_c, semaforo_d):
    print(f"  B aguardando . . .")
    down(semaforo_b_c)
    print(f"  B iniciando contagem (n={n}; t={t})", end="\n", flush=True)
    for i in range(1, n + 1):
        sleep(t)
        print(f'  B: {i}')
    print(f"  B Finalizando contagem", end="\n", flush=True)
    # Depois da contagem libera o D
    up(semaforo_d)


def c(t, n, semaforo_b_c, semaforo_d):
    print(f"    C aguardando . . .")
    down(semaforo_b_c)
    print(f"    C iniciando contagem (n={n}; t={t})", end="\n", flush=True)
    for i in range(1, n + 1):
        sleep(t)
        print(f'    C: {i}')
    print(f"    C Finalizando contagem", end="\n", flush=True)
    # Depois da contagem libera o D
    up(semaforo_d)


def d(t, n, semaforo_d):
    print(f"      D aguardando . . .")
    down(semaforo_d)
    down(semaforo_d)
    print(f"      D iniciando contagem (n={n}; t={t})", end="\n", flush=True)
    for i in range(1, n + 1):
        sleep(t)
        print(f'      D: {i}')
    print(f"      D Finalizando contagem", end="\n", flush=True)


def main():
    print("* GRAFO DE PRECECÊNCIA")
    # Os valores de n(x) e t(x) devem ser fornecidos pelo usuário (no início do programa ou na linha de comando).
    # - Use processos e não threads.
    # - Os processos A, B, C e D devem ser iniciados no mesmo instante (no início do programa), 
    # embora a contagem de cada um só comece no instante apropriado.
    # - Use um número mínimo de semáforos para sincronizar os processos.

    # Semaforos para controle
    semaforo_b_c = Semaphore(0)
    semaforo_d = Semaphore(0)

# Solicitar inputs do usuário
    n_a = int(input("Digite o valor de n para A: "))
    t_a = float(input("Digite o valor de t para A: "))
    n_b = int(input("Digite o valor de n para B: "))
    t_b = float(input("Digite o valor de t para B: "))
    n_c = int(input("Digite o valor de n para C: "))
    t_c = float(input("Digite o valor de t para C: "))
    n_d = int(input("Digite o valor de n para D: "))
    t_d = float(input("Digite o valor de t para D: "))

    print("\n* GRAFO DE PRECECÊNCIA")

    # Iniciar processos com os valores fornecidos pelo usuário
    process_a = Process(target=a, args=(t_a, n_a, semaforo_b_c))
    process_b = Process(target=b, args=(t_b, n_b, semaforo_b_c, semaforo_d))
    process_c = Process(target=c, args=(t_c, n_c, semaforo_b_c, semaforo_d))
    process_d = Process(target=d, args=(t_d, n_d, semaforo_d))

    process_a.start()
    process_b.start()
    process_c.start()
    process_d.start()

    process_a.join()
    process_b.join()
    process_c.join()
    process_d.join()


if __name__ == "__main__":
    main()
