import subprocess

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
        