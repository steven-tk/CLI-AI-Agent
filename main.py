import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from schemas import schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file
from call_function import call_function


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

def main():
    print("CLI AI Agent running...")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("API Key not found")

    client = genai.Client(api_key=api_key)
    

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]






    query_message = messages

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
            ],
        )


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query_message,
        config={
            'tools': [available_functions],
            'system_instruction': system_prompt,
            },
        )
    
    
    if not response.usage_metadata:
        raise RuntimeError("failed API call")
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if args.verbose:
            print(f"User prompt:\n{args.user_prompt}")
            print(f"\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}\n")


    if not response.function_calls:
        print("Response:\n", response.text)
        return
    

    function_call_results = []

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=args.verbose)

        if function_call_result.parts[0].function_response.response is None:
            raise RuntimeError("Fatal Error: Function call did not return a valid response.")

        function_call_results.append(function_call_result.parts[0])

        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")



if __name__ == "__main__":
    main()

