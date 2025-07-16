from search_module import search_web
from shared_memory import save_memory
from nn_brain import train_brain
from question_generator import generate_questions_from_text
from logger import log_event

def beta_listen_and_reply(question):
    log_event("Beta", "Searching", question)
    answer = search_web(question)
    log_event("Beta", "Answer", answer)
    save_memory(question, answer)
    train_brain()

    follow_ups = generate_questions_from_text(answer)
    for q in follow_ups:
        log_event("Beta", "Generated Follow-Up", q)
    return answer, follow_ups
