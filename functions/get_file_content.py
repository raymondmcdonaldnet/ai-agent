import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
	try:
		dir = os.path.join(working_directory, file_path)

		if not os.path.abspath(dir).startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
		if not os.path.isfile(dir):
			return f'Error: File not found or is not a regular file: "{file_path}"'
		else:
			file_content_string = ""
			with open(dir, "r") as f:
				file_content_string = f.read(MAX_CHARS)
				file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
			return file_content_string

	except Exception as e:
		return f"Error: {e}"