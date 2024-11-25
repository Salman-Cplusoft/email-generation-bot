from openai import OpenAI
from get_prompts import prompts
from load_data import get_text
from dotenv import load_dotenv


load_dotenv()


def create_response(doc_type, user_prompt):
    
    doc_prompt = prompts[doc_type]
    # book_data = get_text()
    instructions = prompts["instructions"]
    
    sys_prompt = f"""
    SYSTEM PROMPT:
    {doc_prompt}
    
    INSTRUCTIONS:
    {instructions}
    """
    
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
    )
    
    reply = response.choices[0].message.content
    
    return reply


def create_response_streamlit(doc_prompt, user_prompt, engine, temperature):
    
    instructions = prompts["instructions"]
    
    sys_prompt = f"""
    SYSTEM PROMPT:
    {doc_prompt}
    
    INSTRUCTIONS:
    {instructions}
    """
    
    client = OpenAI()
    response = client.chat.completions.create(
        model=engine,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
    )
    
    reply = response.choices[0].message.content
    
    return reply