import json

class microk8s_actions:
    def __init__(self, order, restart_flag, flag, file_name):
        self.order = order
        self.restart = restart_flag
        self.flag = flag
        self.file_name = file_name
        pass


class microk8s_command:
    def __init__(self, command, kubectl, folder_location, restart_flag, start, stop):        
        self.command = command
        self.kubectl = kubectl
        self.folder_location = folder_location
        self.restart = restart_flag
        self.start = start
        self.stop = stop
        pass


class job_configuration:
    def __init__(self):
        self.microk8s = None
        self.actions = []

    @classmethod
    def from_json(self, json_str):
        json_data = json.loads(json_str)
        k8s_cmd = json_data["microk8s"]
        cmd = microk8s_command(
            k8s_cmd["command"], 
            k8s_cmd["type"], 
            k8s_cmd["folder_location"],
            k8s_cmd["restart"],
            k8s_cmd["start"],
            k8s_cmd["stop"]
        )

        act = [microk8s_actions(
            data["order"],
            data["restart"],
            data["flag"],
            data["file_name"]
        ) for data in json_data["actions"]]
        job = job_configuration()
        job.microk8s = cmd
        job.actions = act
        return job

