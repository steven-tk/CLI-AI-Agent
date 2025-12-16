import os

def get_files_info(working_directory, directory="."):
    try:    
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if not os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        directory_list = []
        for item in sorted(os.listdir(target_dir)):
            item_path = os.path.join(target_dir, item)
            item_name = item
            item_size = os.path.getsize(item_path)
            item_is_dir = os.path.isdir(item_path)
            directory_list.append(f"  - {item_name}: file_size={item_size}, is_dir={item_is_dir}")  
    
        return "\n".join(directory_list)

    
    except Exception as e:
        return f"Error: {e}"

