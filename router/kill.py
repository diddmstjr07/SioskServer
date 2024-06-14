import subprocess

class KillProcess:
    def __init__(self) -> None:
        self.command = ["lsof", "-i", ":9460"]

    def kill(self, pids):
        if len(pids) > 0:
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + "\033[1;32m" + "     Kill Process Detected... Starting" + "\033[0m")
        else:
            print("\033[1;32m" + "INFO" + "\033[0m" + ":" + "\033[1;32m" + "     Kill Process Non-Detected... Finishing" + "\033[0m")
            return False
        pid = ""
        for pid_id in pids:
            kill_command = ["kill", "-9", str(pid_id)]
            pid += str(pid_id) + ", "
            process = subprocess.Popen(kill_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
        print("\033[1;32m" + "INFO" + "\033[0m" + ":" + "\033[1;32m" + "     Killing Process Successfully Finished ---> " + "\033[0m" + "\033[1;31m" + f"[{pid[:len(pid) - 2]}]" + "\033[0m")

    def extract_pid_from_line(self, line) -> int:
        fields = str(line).split()
        if len(fields) >= 2:
            pid_str = fields[1]
            if pid_str.isdigit():
                return int(pid_str)
        return None 

    def extract_pids_from_ps_output(self, ps_output) -> list:
        lines = str(ps_output).splitlines()
        pids = [self.extract_pid_from_line(line) for line in lines if self.extract_pid_from_line(line) is not None]
        return pids

    def killing(self):
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        pids = self.extract_pids_from_ps_output(stdout)
        self.kill(pids)