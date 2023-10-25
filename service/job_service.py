import subprocess
from models.request_model import RequestModel
import pandas as pd
import json

from dataclasses import dataclass

# import sys
# sys.path.append("./Models") 
# from app_config import config

from models.app_config import config
from models.job_config import job_configuration, microk8s_actions, microk8s_command


class JobStarter:
    def __init__(self):
        print("Inside the jobstarter")
        self.microk8sJob = RunMicrok8sJob()

    def run_service(self, requestModel: RequestModel):
        # with open("config.json", "r") as file:
        #    json_data = json.load(file)

        # jtopy = json.dumps(json_data)  # convert file read value to json

        # df = pd.read_json("config.json", typ='series')
        # _config = config(**json.loads(df.to_json()))

        mdf = pd.read_json("models/json_model/job_config.json", typ='series')
        job_data: job_configuration = job_configuration.from_json(mdf.to_json())

        print(f"Trigged for: {requestModel.Trigger}")
        match requestModel.Trigger:
            case "restart":
                job_data.microk8s.restart = True
                job_data.microk8s.start = False
                job_data.microk8s.stop = False
            case "start":
                job_data.microk8s.restart = False
                job_data.microk8s.start = True
                job_data.microk8s.stop = False
            case "stop":
                job_data.microk8s.restart = False
                job_data.microk8s.start = False
                job_data.microk8s.stop = True

        if job_data == None:
            raise ValueError("Fail to convert data into commands")
        
        self.microk8sJob._comfigMap_job(job_data)


class RunMicrok8sJob:
    def __init__(self):
        print("Inside the RunMicrok8sJob")

    def to_string(self, lst):
        for elem in lst:
            print(elem.order)

    def _comfigMap_job(self, job_data):
        try:
            k8s_cmd = job_data.microk8s
            job_files = job_data.actions          

            if job_files != None and len(job_files) > 0:
                if k8s_cmd.start or k8s_cmd.restart:
                    job_files = sorted(job_files, key=lambda job_files: job_files.order)
                elif k8s_cmd.stop:
                    job_files = sorted(job_files, key=lambda x: x.order, reverse=True)  
                
                for index, item in enumerate(job_files):
                    command = []
                    if k8s_cmd.restart == True:
                        print(f'Restarting: {item.file_name}')

                        if item.restart:
                            command = [k8s_cmd.command, k8s_cmd.kubectl]
                            command.extend(['delete', item.flag, f'{k8s_cmd.folder_location}/{item.file_name}'])

                            command = []
                            command = [k8s_cmd.command, k8s_cmd.kubectl]
                            command.extend(['apply', item.flag, f'{k8s_cmd.folder_location}/{item.file_name}'])
                    
                    if k8s_cmd.start == True:
                        print(f'Starting: {item.file_name}')

                        if item.restart:
                            command = [k8s_cmd.command, k8s_cmd.kubectl]
                            command.extend(['apply', item.flag, f'{k8s_cmd.folder_location}/{item.file_name}'])

                    if k8s_cmd.stop == True:
                        print(f'Stoping: {item.file_name}')

                        if item.restart:
                            command = [k8s_cmd.command, k8s_cmd.kubectl]
                            command.extend(['delete', item.flag, f'{k8s_cmd.folder_location}/{item.file_name}'])
                    
                    if command is not None and len(command) == 5:
                        # Run the command
                        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        command_output = result.stdout

                        # Check the result
                        if result.returncode == 0:
                            print("Command was successful. Output:")
                            print(f"Command Output: {command_output}")
                        else:
                            print(f"Command failed with error: {result.returncode}")
                            print(f"Error output: {result.stderr}")
            else:
                print("No action command found")
        except subprocess.CalledProcessError as e:
            print(f"Error {e}")
            command_output = ''
