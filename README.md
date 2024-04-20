# Model Creator CLI Tool Documentation

## Overview

The Model Creator CLI Tool is a Python command-line interface (CLI) tool designed to facilitate the creation of new models in a database. It allows users to quickly generate the necessary files and directory structure for a new model, making the process efficient and standardized.

## Features

- Create Model: Generates a new directory containing Python class and JSON definition files for the specified model.
- Customizable: Users can define their own model attributes and types in the JSON definition file.

## Installation
1. Navigate to the project directory:

    ```
    cd model-creator-cli
    ```

2. The tool is compatible with Python 3.

## Usage

To create a new model, use the following command:

```
python manage.py create-model <model_name>
```

Replace `<model_name>` with the name of the model to be created.

### Example:

```
python manage.py create-model User
```

This will create a new directory named `models/User` with the following files inside it:

- `User.py`: Python class file representing the User model.
- `User.json`: JSON definition file containing model attributes and types.

## File Structure

The generated directory will have the following structure:

```
models/
└── User/
    ├── User.py
    └── User.json
```

## Model Definition File (JSON)

The JSON definition file (`User.json` in this example) contains the attributes and types of the model. This file can be customized to add or modify attributes as needed.

Example `User.json`:

```json
{
    "fields": [
        {
            "name": "username",
            "type": "string",
            "optional": "False",
        },
        {
            "name": "email",
            "type": "string",
            "optional": "False",
        },
        {
            "name": "age",
            "type": "integer",
            "optional": "True",
        }
    ]
}
```

## Model Class File (Python)

The Python class file (`User.py` in this example) contains the Python class definition for the model. You can extend this class and add custom methods as required.

Example `User.py`:

```python
class User(Document):
    pass
```

# Asynchronous Hooks System Documentation

This module provides a simple way to implement and execute hooks in an asynchronous Python application. Hooks are functions that are called at specific points in the application's lifecycle, allowing for modular and extensible behavior.

## Usage

### Defining Hooks

Hooks are defined as asynchronous functions within the `hooks.py` module. There are three types of hooks supported:

1. after_start: Executes after the application starts.
2. before_migrate: Executes before database migration.
3. after_migrate: Executes after database migration.

To define a function as a hook, simply decorate it with the appropriate decorator (`register_after_start`, `register_before_migrate`, or `register_after_migrate`).

### Adding Functions to Hooks

Functions can be added to hooks dynamically by using the appropriate decorator with the desired function. These functions can accept arbitrary positional and keyword arguments.

### Executing Hooks

To execute the hooks, call the corresponding hook function (`after_start_hooks`, `before_migrate_hooks`, or `after_migrate_hooks`) at the appropriate point in the application's lifecycle.

## Example

```python
from hooks import (
    after_start_hooks, before_migrate_hooks, after_migrate_hooks,
    register_after_start, register_before_migrate, register_after_migrate
)

@register_after_start
async def function1_after_start(arg1, arg2, kwarg1=None):
    print(f"Function 1 after_start executed with args: {arg1}, {arg2}, kwargs: {kwarg1}")

@register_after_start
async def function2_after_start(arg, *args, **kwargs):
    print(f"Function 2 after_start executed with arg: {arg}, args: {args}, kwargs: {kwargs}")

@register_after_start
async def function3_after_start(*args, **kwargs):
    print(f"Function 3 after_start executed with args: {args}, kwargs: {kwargs}")

async def main():
    await after_start_hooks("arg1", "arg2", kwarg1="kwarg1")
    await before_migrate_hooks("arg")
    await after_migrate_hooks()

asyncio.run(main())
'''


```
# API Documentation

This documentation provides details on how to use the API endpoints.

## Base URL

The base URL for all endpoints is `http://localhost:8013` when running locally.

## Endpoints

### Retrieve Data

#### Description

This endpoint allows retrieving data based on a model name with optional fields and filters.

#### Method

- POST

#### Path

- `/retrieve_data/`

#### Parameters

- `modelName`: (string, required) Name of the model.
- `fields`: (array of strings, optional) Specifies fields to retrieve. Use `["*"]` for all fields or specify specific fields.
- `filters`: (array of objects, optional) Specifies filter conditions. Each filter object should have the following keys:
  - `field`: (string) Name of the field to filter on.
  - `operator`: (string) Comparison operator (e.g., "==", ">=", "<=").
  - `value`: (string) Value to compare with.

#### Example

```
POST /retrieve_data/?modelName=User&fields=["firstName", "lastName"]&filters=[{"field":"createdAt","operator":">=","value":"2023-01-01"}]
```

This example retrieves the `firstName` and `lastName` fields for users created on or after January 1, 2023.

#### Response

- Status Code: 200 OK
- Body: JSON object containing the retrieved data.

Example Response Body:
```json
{
  "data": [
    {"firstName": "John", "lastName": "Doe"},
    {"firstName": "Jane", "lastName": "Smith"}
  ]
}
```

## Error Handling

- 400 Bad Request: Invalid request parameters.
- 404 Not Found: No match was found for your request.
- 500 Internal Server Error: Unexpected server error.
```
