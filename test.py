import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
prompt_tokens = 0
response_tokens = 0
def main():
    print("CLI AI Agent running...")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("API Key not found")

    client = genai.Client(api_key=api_key)
    
    query_message = messages
    response = client.models.generate_content(model="gemini-2.5-flash", contents=query_message)

    if not response.usage_metadata:
        raise RuntimeError("failed API call")
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"User prompt:\n{args.user_prompt}")
        print(f"\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}\n")
    print("Response:\n", response.text)



if __name__ == "__main__":
    main()
