import os


def replace_text_in_files(directory, old_text, new_text, encoding='utf-8'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.go'):
                file_path = os.path.join(root, file)
                # Read the file
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                # Replace the text
                content = content.replace(old_text, new_text)
                # Write the file
                with open(file_path, 'w', encoding=encoding) as f:
                    f.write(content)


directory_path = 'C:\\Users\\Hydr8r\\Coding\\Go\\goth'  # Use double backslashes for Windows paths
old_string = 'github.com/markbates/goth'
new_string = 'github.com/BryceWayne/goth'

replace_text_in_files(directory_path, old_string, new_string)
