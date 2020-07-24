# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK.
import random
import logging
import boto3
import csv
import re
import urllib.request

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Welcome to Class Manager! You can start class, state fact of the day, or begin roll call. Which would you like to do?"
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Hello World!"
        handler_input.response_builder.speak(speech_text).set_should_end_session(True)
        return handler_input.response_builder.response


class StartClassIntentHandler(AbstractRequestHandler):
    """Handler for Start Class Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("StartClassIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Starting class"
        facts = ["The first programmer was a woman named Ada Lovelace. She's famous for working on the Analytical Engine.", 
                "HP, Microsoft, Apple, and Amazon all started in garages.",
                "The computing industry boasts one of the highest starting salaries for new college graduates.",
                "A 15-year-old once hacked NASA."]

        speech_text += '<break time="1s"/>The tech fact of the day is<break time="1s"/> ' + random.choice(facts)
        speech_text += '<break time="1s"/>Roll call<break time="1s"/>Hannah, are you here? <break time="1s"/>Ace lyn? <break time="1s"/> Mariah?<break time="1s"/> Annie?<break time="1s"/>Great! everyones here, lets get started!'


        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response

class PresentRollCallIntentHandler(AbstractRequestHandler):
    """Handler for Present Roll Call Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("PresentRollCallIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = 'Hannah, are you here? <break time="1s"/>Ace lyn? <break time="1s"/> Mariah?<break time="1s"/> Annie?<break time="1s"/>Great! everyones here, lets get started!'
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response
        
class AddToRosterIntentHandler(AbstractRequestHandler):
    """Handler for Add to Roster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AddToRosterIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = 'Okay, Miranda Lewis has been added!'
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response       

class StartRollCallIntentHandler(AbstractRequestHandler):
    
    def readS3(self):
        with urllib.request.urlopen("https://aws-codestar-us-east-1-186841075729-afe-hackathon-pipe.s3.amazonaws.com/test/PracticeFAQs.csv") as url: 
            s = url.read()
            s = s.decode('utf-8') 
            names = re.split('[\r\n]+', s)
            return names
    
    """Handler for Start Roll Call Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("StartRollCallIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        names = self.readS3()
        #names = ["Annie V", "Mariah B", "Acelyn C", "Hannah N"]

        #slots = handler_input.request_envelope.request.intent.slots
        #response = slots["response"].resolutions.resolutions_per_authority[0].values[0].value.name

        speech_text = 'Starting roll call<break time="1s"/> ' + names[0] + ' ?'

        '''
        for i in names:
            if (len(i) > 0): 
                speech_text += i + " ?"
                if response == "present":
                    speech_text = "Hi"
                else:
                    speech_text = "Oooo someone's not here"
        '''
        
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


class CaptureRollCallResponseIntentHandler(AbstractRequestHandler):
    """Handler for Capture Roll Call Response Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CaptureRollCallResponseIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        
        # Prints what user actually says
        # print(slots["response"].value)
        
        response = slots["response"].resolutions.resolutions_per_authority[0].values[0].value.name

        #speech_text = "hi "
        
        if response == "present":
            speech_text = "Hi"
        else:
            speech_text = "Oooo someone's not here"
        
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response

class StateFactOfTheDayIntentHandler(AbstractRequestHandler):
    """Handler for State Fact Of The Day Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("StateFactOfTheDayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        facts = ["The first programmer was a woman named Ada Lovelace. She's famous for working on the Analytical Engine.", 
                "HP, Microsoft, Apple, and Amazon all started in garages.",
                "The computing industry boasts one of the highest starting salaries for new college graduates.",
                "A 15-year-old once hacked NASA."]

        speech_text = 'The tech fact of the day is<break time="1s"/> ' + random.choice(facts)
        reprompt_text = "Would you like me to state the fact of the day?"
        
        handler_input.response_builder.speak(speech_text).ask(reprompt_text)
        return handler_input.response_builder.response

class AddCuriosityIntentHandler(AbstractRequestHandler):
    """Handler for Add Curiosity Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AddCuriosityIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Okay I have added it to the Class Curiosity Collection."
        handler_input.response_builder.speak(speech_text).set_should_end_session(True)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "You can say hello to me! How can I help?"
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Goodbye!"
        handler_input.response_builder.speak(speech_text)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return handler_input.response_builder.response


# The intent reflector is used for interaction model testing and debugging.
# It will simply repeat the intent the user said. You can create custom handlers
# for your intents by defining them above, then also adding them to the request
# handler chain below.
class IntentReflectorHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = handler_input.request_envelope.request.intent.name
        speech_text = ("You just triggered {}").format(intent_name)
        handler_input.response_builder.speak(speech_text).set_should_end_session(True)
        return handler_input.response_builder.response


# Generic error handling to capture any syntax or routing errors. If you receive an error
# stating the request handler chain is not found, you have not implemented a handler for
# the intent being invoked or included it in the skill builder below.
class ErrorHandler(AbstractExceptionHandler):
    """Catch-all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        speech_text = "Sorry, I couldn't understand what you said. Please try again."
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


# This handler acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(StartClassIntentHandler())
sb.add_request_handler(AddToRosterIntentHandler())
sb.add_request_handler(PresentRollCallIntentHandler())
sb.add_request_handler(StartRollCallIntentHandler())
sb.add_request_handler(CaptureRollCallResponseIntentHandler())
sb.add_request_handler(StateFactOfTheDayIntentHandler())
sb.add_request_handler(AddCuriosityIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(ErrorHandler())

handler = sb.lambda_handler()