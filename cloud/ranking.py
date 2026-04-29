import ast

def rank_fixes(rows):
    scored = []

    for r in rows:
        strategies, success, uses = r

        score = success * 2 + uses

        scored.append((score, strategies))

    scored.sort(reverse=True)

    if scored:
        return ast.literal_eval(scored[0][1])

    return []
