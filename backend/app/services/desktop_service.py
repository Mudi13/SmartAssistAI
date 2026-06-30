import subprocess
import pyautogui

class DesktopService:
    
    applications = {
    "notepad": "notepad",
    "calculator": "calc",
    "edge": "msedge",
    "vscode": "code",
    "mspaint": "mspaint",
    "explorer": "explorer",
}

    @staticmethod
    def open_application(app_name: str):
        try:

            if app_name not in DesktopService.applications:
                return False

            command = DesktopService.applications[app_name]
            
            subprocess.Popen(command)
            
            return True
    
        except Exception as e:
            print(f"❌ App Not Found: {e}")
            return False            
        
    
    @staticmethod
    def move_mouse(x: int, y: int, duration: float = 1.0):
        try:
            pyautogui.moveTo(x, y, duration=duration)
            return True
            
        except Exception as e:
            print(f"❌ Error moving mouse: {e}")
            return False
        
    
    @staticmethod
    def type_text(text: str):
        try:
            pyautogui.write(text)
            return True
        
        except Exception as e:
            print(f"❌ Error typing text: {e}")
            return False
        
    
    @staticmethod
    def press_key(key: str):
        try:
            pyautogui.press(key)
            return True
        
        except Exception as e:
            print(f"❌ Error pressing key: {e}")
            return False
        
    @staticmethod
    def take_screenshot(filename : str = "screenshot.png"):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            return filename

        except Exception as e:
            print(f"❌ Error taking screenshot: {e}")
            return None