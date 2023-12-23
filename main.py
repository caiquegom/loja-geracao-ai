from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values('.env')

client = OpenAI(organization=config['ORGANIZATION_ID'])