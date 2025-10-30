import logging
from openai import OpenAI
from django.conf import settings

logger = logging.getLogger(__name__)
client = OpenAI(api_key=settings.OPENAI_API_KEY)
user_contexts = {}

def get_ai_response(user_id: int, message: str) -> str:
    """
    Foydalanuvchi ID asosida AI bilan suhbat kontekstini saqlaydi.
    """
    try:
        context = user_contexts.get(user_id, [])
        context.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Siz foydali, muloyim va o‘zbek tilida javob beradigan AI yordamchisiz."}
            ] + context,
            temperature=0.7,
            max_tokens=250,
            response_format={"type": "text"}, 
        )

        ai_message = response.choices[0].message.content.strip()
        context.append({"role": "assistant", "content": ai_message})
        user_contexts[user_id] = context[-10:]

        return ai_message

    except Exception as e:
        logger.error(f" OpenAI xatosi (user_id={user_id}): {e}")
        return " AI bilan aloqa vaqtida muammo yuz berdi, iltimos keyinroq urinib ko‘ring."
