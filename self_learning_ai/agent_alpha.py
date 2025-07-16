from ai_communicator import communicate
from logger import log_event

def alpha_talk(question):
    log_event("Alpha", "Asking", question)
    return communicate(question)
