from agent_beta import beta_listen_and_reply
from nn_brain import predict_answer
from logger import log_event

def communicate(question):
    try:
        answer = predict_answer(question)
        log_event("Brain", "Predicted", answer)
        return answer, []
    except:
        log_event("Alpha", "Brain didn't know", question)
        return beta_listen_and_reply(question)
