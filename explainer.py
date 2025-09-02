from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def explain_code(code_snippet: str, style: str = "Brief") -> str:
    """
    Sends code to the LLM and returns an explanation.
    """

    prompt_map = {
        "Brief": (
            "You are a code explainer. "
            "Provide a concise, high-level summary of what the following code does. "
            "Do not include implementation details or step-by-step breakdowns. "
            "Keep it under 3 sentences.\n\n"
            f"Code:\n{code_snippet}"
        ),
        "Detailed": (
            "You are a code explainer. "
            "Provide a thorough, detailed explanation of the following code. "
            "Describe its purpose, logic, and how each part works. "
            "Include information about functions, variables, and any important implementation details.\n\n"
            f"Code:\n{code_snippet}"
        ),
        "Step-by-Step": (
            "You are a code explainer. "
            "Explain the following code step by step. "
            "Number each step clearly (Step 1, Step 2, etc.), and describe what happens in each part of the code. "
            "Be explicit and sequential in your breakdown.\n\n"
            f"Code:\n{code_snippet}"
        ),
    }

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI that explains code clearly."},
                {"role": "user", "content": prompt_map.get(style, prompt_map['Brief'])}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
