import subprocess

def run(self, cmd):
    command = subprocess.run(["powershell", "-Command", cmd], capture_output = True)
    return command


def windowsTools(file):
    command_status = run(commmand)
    if command_status != 0:
        print("An error has occured: %s", command_status)
    else:
        pass
