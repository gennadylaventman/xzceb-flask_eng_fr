''' Provides translation from English to French and vise versa '''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    ''' Translate text from English to French '''
    try:
        translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    except ValueError:
        return None
    french_text = translation["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    ''' Translate text from French  to English '''
    try:
        translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    except ValueError:
        return None
    english_text = translation["translations"][0]["translation"]
    return english_text
