from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_SpeechToText = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/d12ea51e-e5e1-4b62-9035-211eb6eab9c3"
SpeecheToText_APIKey = '__________'

authenticator = IAMAuthenticator(SpeecheToTextAPIKey)
SpeechToText = SpeechToTextV1(authenticator=authenticator)
SpeechToText.set_service_url(url_SpeechToText)

audioFileName = '_________'
with open(audioFileName, mpde='rb') as wav:
    response = SpeechToText.recognize(audio=wav, content_type='audio/mp3')

response.result
