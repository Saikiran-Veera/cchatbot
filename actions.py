from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re


class detailForm(FormAction):
    """Example of a custom form action."""

    def name(self) -> Text:
        """Unique identifier of the form."""

        return "detail_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill."""

        return ["name", "phone", "email" , "location"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
        or a list of them, where a first match will be picked."""

        return {
            "name": self.from_text(),
            "phone": self.from_text(),
            "email": self.from_text(),
            "location":self.from_text()
        }
    
    def validate_phone(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text,Any]:
        """Validate cuisine value."""

        if len(value)>7:
            # validation succeeded
            return value
        else:
            dispatcher.utter_template('utter_wrong_phone', tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return None
        
    def validate_email(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text,Any]:
        """Validate cuisine value."""
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,value)):  
            return value
        else:  
            dispatcher.utter_template('utter_wrong_email', tracker)
            return None

    def validate_name(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text,Any]:
        """Validate cuisine value."""
        if value.replace(" ", "").isalpha():  
            return value
        else:  
            dispatcher.utter_template('utter_wrong_name', tracker)
            return None
    
    def validate_location(self,
                         value: Text,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text,Any]:
        """Validate cuisine value."""
        if value.replace(" ", "").isalpha():  
            return value
        else:  
            dispatcher.utter_template('utter_wrong_location', tracker)
            return None
        
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled."""
        
        nam = tracker.get_slot("name")
        phn = tracker.get_slot("phone")
        eml = tracker.get_slot("email")
        loc = tracker.get_slot("location")
        
        sender_email = "saikiran.v@zyclyx.com"
        receiver_email = "saikiran.v@zyclyx.com"
        password = "J@isriram"
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Virtech Website"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        # Create the plain-text and HTML version of your message
        text = "Hi,\nBelow are the details from website:\n"
        text = text +"Name: " +str(nam)+"\nPhone: " +str(phn)+"\nEmail: " +str(eml)+"\nLocation: " +str(loc)

        
        part1 = MIMEText(text, "plain")
        
        message.attach(part1)
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
      
        location = tracker.get_slot("location")
        dispatcher.utter_message(template="utter_slots_values", location=location)
        
        
        
        
        
        # dispatcher.utter_message(template="utter_slots_values")
        return []
