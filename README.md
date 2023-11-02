# T3 - Grafo de Precedência

Descrição:
Sejam A, B, C e D threads que contam de 1 a $n_x$ de $t_x$ em $t_x$ segundos (sendo que $x ∈$ {$A, B, C, D$} ). Por exemplo, se $n_A = 5$ e $t_A = 1.0$, então o processo A contará de 1 a 5, de 1 em 1 segundo.

Implemente em Python o grafo de precedência abaixo sendo que uma aresta de um processo X a um processo Y indica que Y só pode iniciar a contagem quando X terminar a sua. No grafo abaixo, isso significa que B e C só podem começar a sua contagem depois que A terminar a sua, e D só iniciará sua contagem quando B e C ambos tiverem terminado.

Detalhamento:
 - Os valores de $n_x$ e $t_x$ devem ser fornecidos pelo usuário (no início do programa ou na linha de comando).
 - Use processos e não threads.
 - Os processos A, B, C e D devem ser iniciados no mesmo instante (no início do programa), embora a contagem de cada um só comece no instante apropriado.
- Use um número mínimo de semáforos para sincronizar os processos.
