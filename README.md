# Smart Study Planner API
> Folder: backend/

A RESTful backend application built with **FastAPI** and Python. It provides endpoints for managing tasks, filtering and sorting task lists, pagination, and task summaries.

## Table of Contents

1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation and Setup](#installation-and-setup)
6. [Running the Application](#running-the-application)
7. [API Documentation](#api-documentation)
8. [API Usage Examples](#api-usage-examples)
9. [Query Parameters](#query-parameters)
10. [Data Storage](#data-storage)
11. [Troubleshooting](#troubleshooting)
12. [Development Workflow](#development-workflow)

---

## 1. Features

- Create, retrieve, update, and delete tasks.
- Filter tasks by subject, completion status, search terms, or priority, where supported by the implemented endpoints.
- Sort tasks by title or estimated completion time.
- Paginate results using `skip` and `limit`.
- Generate task summaries, including completed task counts and total estimated time, where implemented.
- Validate request data using Pydantic.
- Automatically generate interactive API documentation using FastAPI.
- Store task data in a local JSON file.

> Note: The available features depend on which endpoints have been implemented in the current version.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server for running the application |
| Pydantic | Request validation and data modelling |
| JSON | Local file-based data persistence |
| Swagger UI | Interactive API documentation |

## 3. Project Structure

The application follows a modular structure to separate the application entry point, API routes, and data models.

```text
task-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
├── data/
│   └── tasks.json
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

### Directory and file descriptions

- `app/main.py`: Creates the FastAPI application and registers routers.
- `app/schemas/task.py`: Defines Pydantic models for request validation and query parameters.
- `app/routers/tasks.py`: Contains task-related API endpoints.
- `data/tasks.json`: Stores task data if JSON file-based persistence is implemented.
- `requirements.txt`: Lists Python dependencies.
- `.gitignore`: Specifies files and directories Git should ignore.
- `README.md`: Documents the project and explains how to run it.
.

## 4. Prerequisites

Before running the application, ensure that the following software is installed:

- Python 3.12 or another version supported by your dependencies.
- `pip`, the Python package installer.
- A terminal or command-line interface.
- Git, if cloning the repository.

Check your Python and pip versions:

```bash
python3 --version
python3 -m pip --version
```

If you are cloning the project, first navigate to your preferred workspace:

```bash
git clone https://github.com/SakshiKhatiwada/Smart-Study-Planner
cd Smart-Study-Planner/backend
```

If the project already exists locally, navigate directly to its root directory.

## 5. Installation and Setup

### Step 1: Create a virtual environment

A virtual environment isolates the project's dependencies from other Python projects on your machine.

From the project root, run:

```bash
python3 -m venv .venv
```

This creates a `.venv` directory containing the environment's Python interpreter and package installation location.

### Step 2: Activate the virtual environment

On Windows:

```bash
source .venv/Scripts/activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

After activation, your terminal prompt will usually display `(.venv)`.

Verify that Python points to the virtual environment:

```bash
which python
```

The output should point to a path inside your project's `.venv` directory.

### Step 3: Install dependencies

If the repository contains a `requirements.txt` file, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

If the file does not exist yet, install the required packages directly:

```bash
python -m pip install "fastapi[standard]"
```

This installs FastAPI and its standard optional dependencies, including Uvicorn.

Once the dependencies are installed, you can save the project's current dependency versions with:

```bash
python -m pip freeze > requirements.txt
```

Only do this if you intend to generate or refresh the project's dependency list. Review the resulting file before committing it.

### Step 4: Verify the installation

Run:

```bash
python -c "import fastapi, uvicorn; print('FastAPI:', fastapi.__version__); print('Uvicorn:', uvicorn.__version__)"
```

If the command prints both versions without errors, the packages are available in the active environment.

## 6. Running the Application

### Step 1: Confirm your working directory

Your terminal should be at the project root (backend/), where the `app/` directory is located.

```bash
pwd
ls
```

You should see the `app` directory and, if present, `requirements.txt`.

### Step 2: Start the development server

If `main.py` is located at `app/main.py` and the FastAPI instance is named `app`, run:

```bash
uvicorn app.main:app --reload
```

The command consists of:

- `uvicorn`: Starts the ASGI server.
- `app.main`: Imports the Python module `app/main.py`.
- `:app`: Selects the FastAPI application instance named `app` inside that module.
- `--reload`: Restarts the development server when source files change.

If your application entry point is instead a root-level `main.py`, the command would be:

```bash
uvicorn main:app --reload
```

Use the command that matches your actual project structure.

### Step 3: Verify the server is running

Uvicorn should display a message indicating that the server is running, usually at:

```text
http://127.0.0.1:8000
```

Open the URL in your browser. If no root endpoint is defined, the browser may display a `404 Not Found` response. That does not necessarily mean the server failed to start.

### Step 4: Stop the server

To stop the development server, press:

```text
Ctrl + C
```

### Step 5: Restart the application later

When you return to the project:

```bash
cd Smart-Study-Planner/backend
source .venv/bin/activate
uvicorn app.main:app --reload
```

## 7. API Documentation

FastAPI generates API documentation from the application's routes, parameter annotations, and Pydantic schemas.

Once the server is running, open the following URLs.

### Swagger UI

**URL:** http://127.0.0.1:8000/docs

Swagger UI lets you:

- Inspect available endpoints and HTTP methods.
- View required request fields and response schemas.
- Enter path and query parameters.
- Submit requests using **Try it out**.
- Inspect status codes and response bodies.
- Test validation rules.

### ReDoc

**URL:** http://127.0.0.1:8000/redoc

ReDoc provides an alternative documentation interface organised around the API specification.

These documentation pages are generated automatically by FastAPI using the OpenAPI schema. They do not replace the backend; they provide an interface for exploring and testing it.

## 8. API Usage Examples

The exact paths and request bodies depend on the endpoints implemented in `app/routers/tasks.py`. The following examples illustrate common task-management operations.

###  Retrieve all tasks

```http
GET /tasks
```

Example URL:

```text
http://127.0.0.1:8000/tasks
```

###  Retrieve a task by ID

```http
GET /tasks/1
```

Replace `1` with the ID of the task you want to retrieve.

### Create a task

If your create endpoint accepts fields such as `title` and `estimated_minutes`, a request body might look like:

```json
{
  "title": "Study FastAPI",
  "estimated_minutes": 45,
  "completed": false
}
```

Submit the JSON using the `POST` endpoint shown in Swagger UI. The actual accepted fields must match your request schema.

###  Update a task

A partial update using `PATCH` might look like:

```http
PATCH /tasks/1
```

Example request body:

```json
{
  "title": "string",
  "subject": "string",
  "priority": "low",
  "completed": false,
  "estimated_minutes": 1
}
```

### Replace a Task

Endpoint: `PUT` 

```http
PUT /tasks/{task_id}
```

Replaces an existing task with the provided data. The request body should contain all required task fields.

Example request:

PUT /tasks/1
Content-Type: application/json

{
  "title": "Study FastAPI",
  "subject": "Backend Engineering",
  "priority": "high",
  "completed": false,
  "estimated_minutes": 60
}

The precise fields and update behaviour depend on your implementation.

### Delete a task

```http
DELETE /tasks/1
```

Replace `1` with the relevant task ID.

### Retrieve a task summary

If a summary endpoint is implemented at `/tasks/summary`, request:

```http
GET /tasks/summary
```

A possible response structure is:

```json
{
  "total_tasks": 6,
  "completed_tasks": 3,
  "pending_tasks": 3,
  "total_estimated_minutes": 780,
  "remaining_estimated_minutes": 180
}
```

The values above are illustrative, not actual application data.

**Route ordering:** If `/tasks/summary` and `/tasks/{task_id}` are both declared, register the specific `/tasks/summary` route before the dynamic `/{task_id}` route. Otherwise, the string `summary` may be interpreted as a task ID and fail integer validation.

## 9. Query Parameters

Query parameters allow clients to filter, sort, and paginate results without creating separate endpoints for every combination.

For example:

```text
GET /tasks?priority=high&skip=0&limit=5&sort_by=title&order=asc
```

The following parameters correspond to the query schema, if connected to the endpoint.

| Parameter | Purpose | Example |
|---|---|---|
| `priority` | Filter by priority | `priority=high` |
| `skip` | Number of results to skip | `skip=5` |
| `limit` | Maximum number of results | `limit=10` |
| `sort_by` | Field used for sorting | `sort_by=title` |
| `order` | Sorting direction | `order=desc` |
| `search` | Search task content | `search=python` |
| `completed_status` | Filter by completion state | `completed_status=true` |

### Pagination

Pagination divides a potentially large result list into smaller portions.

For example:

```text
GET /tasks?skip=0&limit=10
GET /tasks?skip=10&limit=10
GET /tasks?skip=20&limit=10
```

- `skip=0&limit=10` requests the first ten results.
- `skip=10&limit=10` requests the next ten.
- `skip=20&limit=10` requests the following ten.

### Sorting

To sort alphabetically by title:

```text
GET /tasks?sort_by=title&order=asc
```

To sort by estimated time in descending order:

```text
GET /tasks?sort_by=estimated_minutes&order=desc
```

Sorting should normally happen before pagination so that each page represents a portion of the consistently sorted result set.

### Query validation

The application may restrict query values using Pydantic and FastAPI validation.

For example:

- `priority` must be `low`, `medium`, or `high`.
- `skip` must be non-negative.
- `limit` must be between 1 and 20.
- `sort_by` must be `title` or `estimated_minutes`.
- `order` must be `asc` or `desc`.

Invalid values generally produce a `422 Unprocessable Entity` response.

## 10. Data Storage

If the application uses JSON file-based storage, task records may be persisted in a file such as:

```text
data/tasks.json
```

The application can read the file when retrieving tasks and update it when tasks are created, modified, or deleted.

### Important considerations

- Ensure the data directory exists before writing to the file.
- Initialise the JSON file with valid JSON, such as an empty list (`[]`), if the application expects a list.
- Use a consistent file path so the application can find the file regardless of the directory from which it is launched.
- Avoid manually editing the file while the application is actively writing to it.
- JSON file storage is suitable for learning and small local projects, but it does not provide the concurrency and transaction guarantees of a database.

If the project intentionally clears task data on startup, document that behaviour here so users do not mistake it for a persistence failure.

## 11. Troubleshooting

### Problem 1: `ModuleNotFoundError`

**Possible cause:** A dependency is missing, or the wrong Python environment is active.

**Solution:**

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If the error concerns one of your own modules, check your imports and project structure.

### Problem 2: `uvicorn: command not found`

**Possible cause:** Uvicorn is not installed in the active environment.

**Solution:**

```bash
python -m pip install "fastapi[standard]"
python -m uvicorn app.main:app --reload
```

### Problem 3: `Could not import module "app.main"`

**Possible cause:** The command is being executed from the wrong directory, the module path is incorrect, or an import inside the module is failing.

**Solution:**

1. Navigate to the project root.
2. Confirm that `app/main.py` exists.
3. Check that your imports are correct.
4. Run the command again:

```bash
python -m uvicorn app.main:app --reload
```

### Problem 4: `422 Unprocessable Entity`

**Possible cause:** A request parameter is missing, has an invalid type, or violates a validation rule.

**Solution:**

1. Open the error response in Swagger UI.
2. Inspect the `loc` field to identify the source, such as `path`, `query`, or `body`.
3. Inspect the `input` field to identify the rejected value.
4. Compare that value with the endpoint's type annotation and validation constraints.

For example, if the route expects `task_id: int`, requesting `/tasks/summary` may fail if `summary` is captured by `/tasks/{task_id}`.

### Problem 5: `404 Not Found`

**Possible cause:** The requested path or HTTP method does not match a registered endpoint.

**Solution:** Open `/docs`, locate the endpoint, and verify its exact path and HTTP method.

### Problem 6: Port 8000 is already in use

**Possible cause:** Another server process is already listening on port 8000.

**Solution:** Stop the existing process or use another port:

```bash
uvicorn app.main:app --reload --port 8001
```

The application will then be available at `http://127.0.0.1:8001`.

### Problem 7: Changes do not appear in Swagger UI

**Possible cause:** The server was not restarted, the application is running from another directory, or the browser is displaying stale documentation.

**Solution:**

- Check the terminal for import or startup errors.
- Confirm that `--reload` is enabled during development.
- Verify the URL and port.
- Refresh the documentation page.

### Problem 8: Task data disappears after restarting

**Possible cause:** The application resets the JSON file at startup, uses a different file path, or fails to persist modifications.

**Solution:** Inspect the startup logic, file paths, and read/write functions. Confirm that data is written to the intended file and that no startup code unintentionally clears it.

## 12. Development Workflow

A typical development session follows these steps:

1. Open a terminal at the project root.
2. Activate the virtual environment.
3. Start the Uvicorn development server.
4. Open Swagger UI and test the endpoints.
5. Modify the code and let the reload server restart.
6. Check the terminal for errors.
7. Test the affected functionality.
8. Inspect the changes with Git.

Useful Git commands:

```bash
git status
git diff
git add -A
git commit -m "Describe the change"
```

Before committing, review the staged changes and ensure that `.venv/`, secrets, temporary files, and unintended data files are not included.

---

## License

Add the project's chosen license here if you intend to distribute or publish it.

## Author

Add your name or GitHub profile here if you want to identify the project author.
