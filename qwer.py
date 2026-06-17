from neurapy.apps import App
from neura_gui_data_parser.converters import parse_dict_data

from typing import Dict
import qwerDependencies
from qwerPayload import qwerPayload


#Here you can add your imports, Please make sure you add them in requirements.txt and provide a compatible version with your robot

class qwer(App):
    def __init__(self, robot):
        self.robot = robot
        raise NotImplementedError(f"Constructor of qwer not implemented")
        
    def init(self, payload: Dict) -> None:
        self.payload = payload
        self.local_payload: qwerPayload = parse_dict_data(self.payload, qwerPayload)

    def run(self) -> None:
        # Please implement the logic for executing the node here
        raise NotImplementedError(f"run of qwer not implemented")

    def finish(self):
        raise NotImplementedError(f"Finish of qwer not implemented")
