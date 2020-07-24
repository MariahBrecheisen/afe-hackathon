# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK.
import random
import logging

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
        speech_text = "Welcome to Class Manager! What would you like to do?"
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
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


class StartRollCallIntentHandler(AbstractRequestHandler):
    """Handler for Start Roll Call Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("StartRollCallIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        names = ["Annie V", "Mariah B", "Hannah N", "Acelyn C"]

        speech_text = 'Starting roll call<break time="1s"/> '

        speech_text += names[0] + " ?"

        #for i in names:
        #    speech_text += " " + i

        def handle_maths(intent, session):
        card_title = intent['name']
    session_attributes = {}
    
    # #Get hold of the value passed in the slot
    # MySlot = str(intent['slots']['MathsQuestion']['value'])
    
    # if MySlot == "2 plus 2":
    #   speech_output = "The answer is four.  Why not ask me something a bit tougher?"
    #   should_end_session = False
    # elif MySlot == "10 plus 10":     
    #   speech_output = "The answer is twenty.  But that's still really easy you know!" \
    #                   "Come on!  Ask me somethimg harder!!"
    #   should_end_session = False
    # elif MySlot == "the square root of 4":     
    #   speech_output = "The answer is two.  But seriously, listen buster.  I've got a brain the " \
    #                   "size of a planet and you're asking me this easy stuff.  Try " \
    #                   "Siri or Cortana.  That's about their level."
    #   should_end_session = False
    # elif MySlot == "the square root of 64":     
    #   speech_output = "The answer is eight.  It's also minus eight but that will probably " \
    #                   "blow your feeble human mind.  I didn't spend 3 years at AI school to "\
    #                   "deal with this trivial rubbish.  I've a friend at number 32 who " \
    #                   "gets asked about stuff like prime numbers and quadratic equations.  One last " \
    #                   "chance or I'm giving up."
    #   should_end_session = False
    # elif MySlot == "100 divided by 0":
    #   speech_output = "Now we're talking!!  One hundred divided by zero.  Let's see, " \
    #                   "OK.  Er.  Um.  Er.  Just a minute.  Can't be that hard.  Buzz, buzz, " \
    #                   "whir, whir, buzz, whir, buzz.  Oooh my brain hurts!  I know I can do this, " \
    #                   "just give me a few minutes and I'll get back to you.  Ouch, ouch, ouch, ouch!"
    #   should_end_session = True
    # else:
    #   speech_output = "Didn't understand what was passed:" + MySlot
    #   should_end_session = False    
        
    
    # reprompt_text = None
    
    # return build_response(session_attributes, build_speechlet_response(
    #     card_title, speech_output, reprompt_text, should_end_session))
        
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
        print(slots)
        #response = slots["Roll_Call_Response].resolutions.resolutionsPerAuthority[].values[].value.name

        speech_text = "hi"
        
        """
        if '{}'.format(response) == "present":
            speech_text = "Hi"
        else:
            speech_text = "Oooo someone's not here"
        """
        
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
sb.add_request_handler(StartRollCallIntentHandler())
sb.add_request_handler(CaptureRollCallResponseIntentHandler())
sb.add_request_handler(StateFactOfTheDayIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(ErrorHandler())

handler = sb.lambda_handler()