"""
This module contains functions that translate English to French and French to English
"""
import os as os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# The following URL is for the London UK location
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')
def english_to_french(englishtext):
    """This function translates english text to french text"""
    frenchtranslation = language_translator.translate(englishtext, model_id='en-fr').get_result()  
    frenchtext = frenchtranslation['translations'][0].get('translation')
    return frenchtext
def french_to_english(frenchtext):
    """This function translates french text to english text"""
    englishtranslation = language_translator.translate(frenchtext, model_id='fr-en').get_result()
    englishtext = englishtranslation['translations'][0].get('translation')
    return englishtext
