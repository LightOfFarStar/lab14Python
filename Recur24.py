def evaluate_expression(word: str) -> bool:
    def parse(index):
        char = word[index]
        if char == 'T':
            return True, index + 1
        if char == 'F':
            return False, index + 1
        if word.startswith('Not', index):
            inner_value, next_index = parse(index + 4)
            return (not inner_value), next_index + 1
        if word.startswith('And', index):
            return parse_parameters(index + 4, all)
        if word.startswith('Or', index):
            return parse_parameters(index + 3, any)

    def parse_parameters(index, func):
        values = []
        idx = index

        while True:
            val, next_idx = parse(idx)
            values.append(val)
            if word[next_idx] == ',':
                idx = next_idx + 1
            elif word[next_idx] == ')':
                return func(values), next_idx + 1
    result, _ = parse(0)
    return result

# Примеры использования:
if __name__ == "__main__":
    test_strings = [
        "T",
        "F",
        "Not(T)",
        "And(T,F)",
        "Or(T,F)",
        "And(Or(T,F),Not(F))",
        "Or(And(T,T),And(F,F))",
        "Not(And(T,Or(F,T)))"
    ]

    for expr in test_strings:
        print(f"{expr} -> {evaluate_expression(expr)}")

'''Recur24. Вывести значение логического выражения, заданного в виде строки S.
Выражени определяется следующим образом («T» — True, «F» — False):
<выражение> ::= T | F | And(<параметры>) |
Or(<параметры>) | Not(<выражение>)
<параметры> ::= <выражение> | <выражение> , <параметры>'''