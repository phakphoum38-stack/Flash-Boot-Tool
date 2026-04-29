from engine.ai_memory import find_best

def recommend(signature):
    strategies = find_best(signature)

    if strategies:
        return {
            "source": "memory",
            "strategies": strategies
        }

    # fallback → heuristic (ของเดิม)
    return {
        "source": "heuristic",
        "strategies": []
    }
