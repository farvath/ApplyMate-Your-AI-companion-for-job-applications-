from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionJobApplication(Action):
    def name(self) -> Text:
        return "action_job_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data= tracker.get_slot("data")

        with open("job_applications.csv", "a") as file:
            file.write(f"{data}\n")

        response = (
            f"Application details saved to Data File. \n"
        )

        dispatcher.utter_message(text=response)
        return []
