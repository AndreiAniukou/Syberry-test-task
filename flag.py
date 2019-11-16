def flag(n):
    jap_flag = ['#' * (3 * n + 2)]

    for i in range(n // 2):
        jap_flag.append('#'.ljust(3 * n + 1) + '#')

    for i in range(1, n // 2 + 1):
        jap_line = ('#' + ' ' * (n // 2) + '*' + 'o').ljust(3 * n + 1) + '#'

        jap_flag.append(jap_line)

    all_line = '\n'.join(jap_flag)

    jap_flag.reverse()

    all_line = (all_line + '\n' + '\n'.join(jap_flag))

    return all_line


n = int(input('Give me even number'))

if int(n) % 2 == 0:
    print(flag(n))
else:
    print('EVEN NUMBER')
