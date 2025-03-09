# ai_service.py
import openai
from django.conf import settings
from huggingface_hub import InferenceClient

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def generate_response(self, query):
        """Generate response using OpenAI API"""
        try:
            # Detect if the query is about calories
            if "calorie" in query.lower() or "nutrition" in query.lower():
                system_prompt = "You are a nutrition expert. Provide accurate calorie information and nutritional facts about foods. Keep responses concise and informative."
            else:
                system_prompt = "You are a helpful assistant. Provide clear and concise responses."

            # response = openai.chat.completions.create(
            #     model="gpt-4o",
            #     messages=[
            #         {"role": "system", "content": system_prompt},
            #         {"role": "user", "content": query}
            #     ]
            # )

            client = InferenceClient(
                provider="hf-inference",
                 api_key="" #Please enter your API key in here
            )
            result = client.text_generation(
                model="meta-llama/Llama-3.2-1B",
                prompt=query
            )
            print(result)

            return result
        except Exception as e:
            return f"Error generating response: {str(e)}"