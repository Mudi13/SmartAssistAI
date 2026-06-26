from app.services.browser_service import BrowserService
from app.services.music_service import MusicService
from app.services.news_service import NewsService
from app.services.ai_service import AIService


def handle_intent(data):

    intent = data["intent"]

    if intent == "youtube":
        return BrowserService.open_youtube()

    elif intent == "google":
        return BrowserService.open_google()

    elif intent == "github":
        return BrowserService.open_github()

    elif intent == "linkedin":
        return BrowserService.open_linkedin()

    elif intent == "news":
        return NewsService.fetch_news()

    elif intent == "music":
        return MusicService.play(data["song"])

    else:
        return AIService.ask(data["query"])