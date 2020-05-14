from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


url_LanguageTranslator = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/5d3a4734-3137-4ef5-8cb2-f10fea7be5d3'
LanguageTranslator_APIKey = '___________'
version_LanguageTranslator = '2018-05-01'

authenticator = IAMAuthenticator(LanguageTranslator_APIKey)
LanguageTranslator = LanguageTranslatorV3(version=version_LanguageTranslator, authenticator=authenticator)
LanguageTranslator.set_service_url(url_LanguageTranslator)

from pandas.io.json import json_normalize

json_normalize(LanguageTranslator.list_identifiable_languages().get_result(), 'languages')

texto = input('O que deseja traduzir? ')

translationResponse = LanguageTranslator.translate(\
    text=texto, model_id='pt-en')

translation = translationResponse.get_result()
Brazil_translation = translation['translations'][0]['translation']
print(f'Texto traduzido: {Brazil_translation}') 
