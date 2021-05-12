import re

from typing import Any, Text, Dict, List ## Datatypes

from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('ram')
        battery = tracker.get_slot('battery')
        
        dispatcher.utter_message(text='The features you entered: ' + str(camera) + ", " + str(ram) + ", " + str(battery))
        dispatcher.utter_message(text='Here are your search results')
        
        return []



class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text='Here the latest news for your category')
        return []



class ProductSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        return "product_search_form"

    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["ram","battery","camera","budget"]



    def validate_ram(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        ram_int = int(re.findall(r'[0-9]+',value)[0])
        if ram_int < 50:
            return {"ram":ram_int}
        else:
            dispatcher.utter_message(response="utter_wrong_ram")
            return {"ram":None}



    def validate_battery(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        battery_int = int(re.findall(r'[0-9]+',value)[0])
        if battery_int <= 5000:
            return {"battery":battery_int}
        else:
            dispatcher.utter_message(response="utter_wrong_battery")
            return {"battery":None}



    def validate_camera(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        camera_int = int(re.findall(r'[0-9]+',value)[0])
        if camera_int < 150:
            return {"camera":camera_int}
        else:
            dispatcher.utter_message(response="utter_wrong_camera")
            return {"camera":None}



    def validate_budget(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        budget_int = int(re.findall(r'[0-9]+',value)[0])
        if budget_int < 4000:
            return {"budget":budget_int}
        else:
            dispatcher.utter_message(response="utter_wrong_budget")
            return {"budget":None}



    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('ram')
        battery = tracker.get_slot('battery')
        budget = tracker.get_slot('budget')

        message = f"You have chosen : camera : {camera} - ram : {ram} - battery : {battery}- budget : {budget}"

        dispatcher.utter_message(text=message)

        dispatcher.utter_message(text="Please find your searched items here.........")

        return []

    

class SoftwareSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        return "sofware_search_form"

    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["client_type","techno"]



    def validate_client_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate client_type value."""

        if client_type in ['particular', 'enterprise']:
            return {"client_type":client_type}
        else:
            dispatcher.utter_message(response="utter_wrong_client_type")
            return {"client_type" : None}



    def validate_techno(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate techno value."""

        if techno in ['java', 'node.js']:
            return {"techno" : techno}
        else:
            dispatcher.utter_message(response="utter_wrong_techno")
            return {"techno" : None}

    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        client_type = tracker.get_slot('client_type')
        techno = tracker.get_slot('techno')

        message = f"You have chosen : client_type : {client_type} - techno : {techno}."

        dispatcher.utter_message(text=message)

        dispatcher.utter_message(text="Please find your searched items here.........")

        return []

    