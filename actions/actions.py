# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSaludo(Action):
    def name(self) -> Text:
        return "action_saludo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent'].get('name')
        
        # Definir las respuestas basadas en las intenciones detectadas
        if intent == 'saludo':
            dispatcher.utter_message(template="utter_saludo")
        elif intent == 'despedida':
            dispatcher.utter_message(template="utter_despedida")
        elif intent == 'consultar_tiempo':
            dispatcher.utter_message(template="utter_consultar_tiempo")
        elif intent == 'informacion_personal':
            dispatcher.utter_message(template="utter_informacion_personal")

        return []

