import datetime

def log_event(agent, action, content):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{agent}] {action}: {content}\n"

    # Save to file
    with open("activity_log.txt", "a") as log:
        log.write(line)

    # Print to terminal
    print(line)
