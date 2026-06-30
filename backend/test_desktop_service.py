from app.services.desktop_service import DesktopService
from app.ai.services.ai_service import AIService


# DesktopService.move_mouse(950, 500)

# DesktopService.type_text("Hello SmartAssist")

# DesktopService.press_key("volumeup")

# DesktopService.take_screenshot()

# DesktopService.take_screenshot("screenshot.png")

response = AIService.analyze_image("screenshot.png")

print(response)