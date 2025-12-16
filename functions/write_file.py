import os

def write_file(working_directory, file_path, content):
    try:    
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        #print(f"WORKING:{working_dir_abs}\TARGET:{target_file_path}")

        if not os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file_path),exist_ok=True)

        with open(target_file_path, "w") as f:
            file_write_confirm = f.write(content)
        
        if file_write_confirm:
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        else:
            return f'Error: Failed writing to "{file_path}" or making the directory'

    except Exception as e:
        return f"Error: {e}"
