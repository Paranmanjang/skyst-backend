import openai
from config import AI_Settings

key = AI_Settings().openai_key

openai.api_key = key

def generate_summary(content: str):

    system_message = {
        "role": "system",
        "content": "이 AI는 사용자가 입력한 텍스트를 요약해주는 기능을 제공합니다. 요약은 입력된 텍스트의 내용을 간략하게 설명하는 것을 의미합니다. 이 기능을 사용하면 긴 텍스트를 읽지 않고도 내용을 파악할 수 있습니다."
    }

    messages = [system_message]
    messages.append({
        "role": "user",
        "content": content
    })

    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,  # Adjust for creativity; lower for more precise responses
            max_tokens=1000,  # Adjust for length; longer for more detailed responses
        )

        summary_response = completion.choices[0].message.content

        return summary_response

    except Exception as e:
        print(f"An error occured: {e}")
        return None
