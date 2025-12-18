import os
from google.genai import types
from config import WORKING_DIR
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from schemas import schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file



available_functions = types.Tool(
    function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
    ],
)



def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
        }

    arguments_dict = {"working_directory": WORKING_DIR}

    if function_call_part.args:
        arguments_dict.update(function_call_part.args)


    function_name = function_call_part.name
    function_to_call = function_map.get(function_name)
    
    if not function_to_call:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_result = function_to_call(**arguments_dict)


    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
