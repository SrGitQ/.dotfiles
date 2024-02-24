import subprocess

def open_applications():
    
    applications = [
        ["google-chrome",  '--profile-directory=Profile 1'],
        ["google-chrome",  '--profile-directory=Default'],
        ["code"],
        ["alacritty"]
    ]

    for app in applications:
        try:
            subprocess.Popen(app)
        except Exception as e:
            print(f"This can't be opened {app}: {e}")

if __name__ == "__main__":
    open_applications()
