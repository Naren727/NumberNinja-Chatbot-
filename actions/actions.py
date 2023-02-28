# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Define your menu options
menu_options = {
    'Addition': 'action_add',
    'Subtraction': 'action_subtract',
    'Multiplication': 'action_multiply',
    'Division': 'action_divide'
}

# Menu Action
class ActionMenu(Action):
    def name(self) -> Text:
        return 'action_menu'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Display the menu options to the user
        response = 'What would you like to do?\n'
        for option in menu_options:
            response += f'{option}\n'
        dispatcher.utter_message(text=response)
        return []
# Subtract
class ActionSubtract(Action):
    def name(self) -> Text:
        return "action_subtract"
    
    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if number1 is None:
            dispatcher.utter_message(text="Please provide the first number.")
            return []

        if number2 is None:
            dispatcher.utter_message(text="Please provide the second number.")
            return []

        result = float(number2) - float(number1)
        dispatcher.utter_message(text=f"The difference is {result:.2f}")
        return []

from rasa_sdk.events import SlotSet
# Add
class ActionAdd(Action):
    def name(self) -> Text:
        return "action_add"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if number1 is None:
            dispatcher.utter_message(text="Please provide the first number.")
            return []

        if number2 is None:
            dispatcher.utter_message(text="Please provide the second number.")
            return []

        result = float(number2) + float(number1)
        dispatcher.utter_message(text=f"The sum is {result:.2f}")
        return []
 # Multiply   
class ActionMultiplyNumbers(Action):

    def name(self) -> Text:
        return "action_multiply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number1 = tracker.get_slot("number1")
        number2 = tracker.get_slot("number2")

        if number1 is None or number2 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch that. Can you please provide two numbers again?")
        else:
            result = float(number1) * float(number2)
            dispatcher.utter_message(f"The result of {number1} times {number2} is {result}")
        return []
# Divide
class ActionDivide(Action):

    def name(self) -> Text:
        return "action_divide"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        num1 = tracker.get_slot("number1")
        num2 = tracker.get_slot("number2")
        if num2 == 0:
            dispatcher.utter_message(text="I'm sorry, I cannot divide by zero.")
        else:
            result = float(num1) / float(num2)
            dispatcher.utter_message(text=f"The result of dividing {num1} by {num2} is {result}.")
        return []


class ActionSetNumber1(Action):
    def name(self) -> Text:
        return "action_set_number1"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Get the user input from the latest message in the tracker
        dispatcher.utter_message("Please enter a number 1 :")
        user_input = tracker.latest_message.get("text")

        # Parse the user input to extract the number
        number1 = None
        try:
            number1 = float(user_input)
        except ValueError:
            # Handle the case where the user input is not a number
            dispatcher.utter_message("Sorry, I didn't understand that. Please enter a number.")
            return []

        # Set the number1 slot with the parsed value
        return [SlotSet("number1", number1)]
    

class ActionSetNumber2(Action):
    def name(self) -> Text:
        return "action_set_number2"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Get the user input from the latest message in the tracker
        dispatcher.utter_message("Please enter a number 2 :")
        user_input = tracker.latest_message.get("text")

        # Parse the user input to extract the number
        number1 = None
        try:
            number2 = float(user_input)
        except ValueError:
            # Handle the case where the user input is not a number
            dispatcher.utter_message("Sorry, I didn't understand that. Please enter a number.")
            return []

        # Set the number1 slot with the parsed value
        return [SlotSet("number2", number2)]
