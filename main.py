import os
from dotenv import load_dotenv
from google import genai
from config import MAX_ITERS
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import call_function, available_functions


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()



        

def generate_content(client, messages, verbose):
    # call client.models.generate_content(...)
    # mutate messages
    # maybe return final text or None




    query_message = messages

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

    if verbose:
        print(f"User prompt:\n{args.user_prompt}")
        print(f"\nPrompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}\n")


    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)


    if not response.function_calls and response.text: 
        return response.text 


    function_call_results = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)

        if function_call_result.parts[0].function_response.response is None:
            raise RuntimeError("Fatal Error: Function call did not return a valid response.")

        function_call_results.append(function_call_result.parts[0])

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")


    if function_call_results:
        messages.append(
            types.Content(
                role="user",
                parts=function_call_results,
            )
        )



    return 

    



def main():
    print("CLI AI Agent running...")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("API Key not found")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            raise Exception("Error: too many iteration attempts")
            # print message and exit non‑success
        try:
            final_text = generate_content(client, messages, args.verbose)
            if final_text:
                print("Final response:")
                print(final_text)
                break

        except Exception as e:
            print(e)
            break



if __name__ == "__main__":
    main()
