from engine.ai_memory import add_record

def train(signature, strategies, success):
    # success = True/False
    add_record(signature, strategies, success)
