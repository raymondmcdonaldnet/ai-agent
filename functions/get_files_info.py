import os

def get_files_info(working_directory, directory="."):
	try:
		dir = os.path.join(working_directory, directory)
		if not os.path.abspath(dir).startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
		elif not os.path.isdir(dir):
			return f'Error: "{directory}" is not a directory'
		else:
			s = ""
			for file in os.listdir(dir):
				s += f"- {file}: file_size={os.path.getsize(f"{dir}/{file}")} bytes, is_dir={os.path.isdir(f"{dir}/{file}")}\n"
			return s
	except Exception as e:
		return f"Error: {e}"



print(get_files_info("calculator", "pkg"))