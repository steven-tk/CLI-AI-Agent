import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:    
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if not os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'


        command = ["python3"]
        command.append(target_file_path)
        if args != []:
            command.extend(args)

        completed_process = subprocess.run(command, cwd=working_dir_abs, capture_output=True, timeout=30)
    
        output = ""
        if completed_process.returncode != 0:
            output += f"\nProcess exited with code {completed_process.returncode}"
        if not completed_process.stdout and not completed_process.stderr:
            output += f"\nNo output produced"
            return output
        else:
            output += f"\nSTDOUT:\n{completed_process.stdout.decode()}\nSTDERR:\n{completed_process.stderr.decode()}"
            return output

    
    except Exception as e:
        return f"Error: executing Python file: {e}"
