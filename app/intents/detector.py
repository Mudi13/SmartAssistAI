def detect_intent(command: str):

    command = command.lower()

    if "youtube" in command:
        return {
            "intent": "youtube"
        }

    elif "google" in command:
        return {
            "intent": "google"
        }

    elif "github" in command:
        return {
            "intent": "github"
        }

    elif "linkedin" in command:
        return {
            "intent": "linkedin"
        }

    elif "news" in command:
        return {
            "intent": "news"
        }

    elif command.startswith("play"):

        song = command.replace("play", "").strip()

        return {
            "intent": "music",
            "song": song
        }

    else:
        return {
            "intent": "ai",
            "query": command
        }