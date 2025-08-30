import os
import typing
import subprocess


def run_python_file(working_directory: str, file_path: str, args=[]) -> str:
	try:
		if not file_path.endswith(".py"):
			return f'Error: "{file_path}" is not a Python file.'

		dir = os.path.abspath(os.path.join(working_directory, file_path))

		if not dir.startswith(os.path.abspath(working_directory)):
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

		if not os.path.exists(dir):
			return f'Error: File "{file_path}" not found.'

		try:
			completed_process = subprocess.run([f"uv", "run", dir, *args], capture_output=True, cwd=working_directory, timeout=30, text=True)

			if completed_process == None:
				return "No output produced"
			else:
				output = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n"
				if completed_process.returncode != 0:
					output += f"Process exited with code {completed_process.returncode}"
				return output
		except Exception as e:
			return f"Error: executing Python file: {e}"
	except Exception as e:
		return f"Error: {e}"