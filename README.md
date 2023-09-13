# Notepad App

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Running Tests](#running-tests)

## Introduction

This is a Notepad App that provides CRUD (Create, Read, Update, Delete) functionalities via API endpoints. The app is backed by unit tests for each endpoint to ensure stability and reliability.

## Installation

1. Clone the repository
```
git clone https://github.com/your-repo/notepad_app.git
```
2. Navigate to the project directory
```
cd notepad_app
```
3. Install the dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
python main.py
```

## Usage

The application provides the following features:

1. **Create a Notepad**: Users can create a new notepad with text content.
2. **Read a Notepad**: Users can read the content of an existing notepad.
3. **Update a Notepad**: Users can update the content of an existing notepad.
4. **Delete a Notepad**: Users can remove an existing notepad.
5. **List All Notepads**: Users can view a list of all their notepads.

## API Endpoints

- **Create a Notepad**
  - Endpoint: `/api/v1/notepad/create`
  - Method: POST
  - Payload: `{ "title": "string", "content": "string" }`

- **Read a Notepad**
  - Endpoint: `/api/v1/notepad/read/{id}`
  - Method: GET

- **Update a Notepad**
  - Endpoint: `/api/v1/notepad/update/{id}`
  - Method: PUT
  - Payload: `{ "title": "string", "content": "string" }`

- **Delete a Notepad**
  - Endpoint: `/api/v1/notepad/delete/{id}`
  - Method: DELETE

- **List All Notepads**
  - Endpoint: `/api/v1/notepad/list`
  - Method: GET

## Running Tests

To run the unit tests, navigate to the project directory and run the following command:

```
python -m unittest discover -s notepad_app/tests -p 'test_*.py'
```

This will run all the unit tests located in the `notepad_app/tests` directory.