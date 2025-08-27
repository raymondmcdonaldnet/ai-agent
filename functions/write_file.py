import os
import typing


def write_file(working_directory: str, file_path: str, content: str) -> str:
	try:
		dir = os.path.join(working_directory, file_path)

		if not os.path.abspath(dir).startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

		if not os.path.exists(dir):
			with open(dir, "x") as _:
				pass

		try:
			with open(dir, "w") as f:
				f.write(content)
		except Exception as e:
			return f"Error: {e}"

		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

	except Exception as e:
		return f"Error: {e}"