from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_SpeechToText = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/d12ea51e-e5e1-4b62-9035-211eb6eab9c3"
SpeecheToText_APIKey = 'Zjvb-LoAiUYXdvBM9zhSvDXRZLuakhz09qXzzuoI6Yb4'

authenticator = IAMAuthenticator(SpeecheToTextAPIKey)
SpeechToText = SpeechToTextV1(authenticator=authenticator)
SpeechToText.set_service_url(url_SpeechToText)

# To load a audio and use the API

audioFileName = ''
with open(audioFileName, mpde='rb') as wav:
    response = SpeechToText.recognize(audio=wav, content_type='audio/mp3')

response.result # this a some dictionaries. Here we need join in a only one dictionary and filter just the trasnciption

# from pandas.io.json import json.normalize
# json_normalize(response.result['results'], 'alternatives')

