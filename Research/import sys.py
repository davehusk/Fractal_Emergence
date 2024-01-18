import random
import string
import sys 
import json
import urllib.parse

import requests
import jsonschema

from flask import Flask, jsonify

app = Flask(__name__)

def generate_hello_world_code(language):
    if language == "python":
        return "def print_hello_world():\n\tprint(\"Hello World!\")"
    elif language == "cpp":
        return "#include <iostream>\n\nint main() {\n\tstd::cout << \"Hello World!\\n\";\n\treturn 0;\n}"
    # Add more languages here
    else:
        return None
  
def print_hello_world():
    print("Hello World!")
    
import subprocess

def compile_and_run(code, language):
    if language == "python":
        exec(code)
        return eval(f"{compile(code, '<string>', 'exec')}")
    elif language == "cpp":
        temp_file = "temp.cpp"
        with open(temp_file, "w") as f:
            f.write(code)
        result = subprocess.run(["g++", "-o", "temp", temp_file], capture_output=True, text=True)
        if result.returncode == 0:
            result = subprocess.run(["./temp"], capture_output=True, text=True)
            return result.stdout
        else:
            return None
    # Add more languages here
    else:
        return None
  
def improve_code(code, language):
    feedback = compile_and_run(code, language)
    if feedback is None:
        # Generate a new code snippet if the current one fails
        code = generate_hello_world_code(language)
    return code

import random

def generate_random_number_code(language):
    if language == "python":
        return "import random\ndef print_random_number():\n\tprint(random.randint(0, 100))"
    # Add more languages here
    else:
        return None

def generate_for_loop_code(language):
    if language == "python":
        return "def print_numbers(n):\n\tfor i in range(n):\n\t\tprint(i)"
    # Add more languages here
    else:
        return None

def generate_simple_class_code(language):
    if language == "python":
        return "class Point:\n\tdef __init__(self, x, y):\n\t\tself.x = x\n\t\tself.y = y\n\tdef distance(self, other):\n\t\treturn ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5"
    # Add more languages here
    else:
        return None
  
def generate_if_else_code(language):
    if language == "python":
        return "def is_positive(n):\n\tif n > 0:\n\t\treturn True\n\telse:\n\t\treturn False"
    # Add more languages here
    else:
        return None
  
def generate_bubble_sort_code(language):
    if language == "python":
        return "def bubble_sort(arr):\n\tfor i in range(len(arr) - 1):\n\t\tfor j in range(len(arr) - i - 1):\n\t\t\tif arr[j] > arr[j + 1]:\n\t\t\t\tarr[j], arr[j + 1] = arr[j + 1], arr[j]"
    # Add more languages here
    else:
        return None

def generate_simple_stack_code(language):
    if language == "python":
        return "class Stack:\n\tdef __init__(self):\n\t\tself.items = []\n\tdef push(self, item):\n\t\tself.items.append(item)\n\tdef pop(self):\n\t\treturn self.items.pop()"
    # Add more languages here
    else:
        return None
  
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate_code", methods=["POST"])
def generate_code_api():
    data = request.get_json()
    language = data.get("language")
    code = generate_hello_world_code(language)
    if code is None:
        return jsonify({"error": "Unsupported language"}), 400
    return jsonify({"code": code})

@app.route("/compile_and_run", methods=["POST"])
def compile_and_run_api():
    data = request.get_json()
    code = data.get("code")
    language = data.get("language")
    feedback = compile_and_run(code, language)
    if feedback is None:
        return jsonify({"error": "Compilation or execution failed"}), 400
    return jsonify({"feedback": feedback})

@app.route("/api/v1/", methods=["GET", "POST"])
def get_api_response():
    response_data = {"status": "success", "message": "Success!"}

    response_json_schema = {
        "type": "object",
        "properties": {
            "status": {
                "type": "string"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "response_type": {
                        "type": "string"
                    },
                    "data": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "required": [
            "status",
            "message",
        ]
    }

    if request.method == 'GET':
        # Return an empty array for GET requests
        response_data["data"] = {"response_type": "success", "data": []}

    elif request.method == 'POST':
        try:
            request_data = request.get_json()
        except ValueError:
            return jsonify({"status": "error", "message": "Invalid JSON data"}), 400

        response_data["data"] = {"response_type": "success", "data": ["Created new record"]}

    validate_json(response_json_schema, response_data)

    return jsonify(response_data)



def validate_json(schema, json_data):
    try:
        jsonschema.validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise ValueError(f"JSON validation failed: {e.message}")



if __name__ == "__main__":
    app.run(debug=True)