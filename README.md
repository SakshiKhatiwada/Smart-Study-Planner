# Smart Study Planner
A web application where students organize subjects, assignments, deadlines, and study sessions.
Features
- Sign up, log in, and manage a personal profile.
- Create tasks, set deadlines, and track completion.
- Display daily and weekly study plans.
- Show progress charts and overdue tasks.
- Optionally generate study schedules using an LLM.
Firebase: Authentication, Cloud Firestore, Hosting.
What you learn: CRUD operations, database design, authentication, user-specific data access, and frontend integration.

# Final product requirements
01

User authentication
Register, log in, and log out securely.


02

Task management
Create, view, edit, and delete study tasks.


03

Academic organization
Categorize tasks by subject, deadline, and priority.


04

Progress dashboard
View pending, completed, and overdue tasks.


05

Cloud database
Store data in Firestore and retrieve it across sessions.


06

Deployment
Publish the app and document how it works.

### Workflow
A student creates a study task in React.
React sends an HTTP request to FastAPI.
FastAPI validates the request and verifies the student's Firebase identity.
FastAPI reads or writes the task in Firestore.
FastAPI returns a JSON response to React.
React updates the displayed task list.

## Example file data
```
[
  {
    "id": "c4de093b-4008-4b67-83c4-aa86a86476e1",
    "title": "homework",
    "subject": "string",
    "priority": "low",
    "completed": true,
    "estimated_minutes": 1
  },
  {
    "id": "301d4963-2038-4cbc-86de-1d2f5d4b0f33",
    "title": "build calculator",
    "subject": "python",
    "priority": "high",
    "completed": false,
    "estimated_minutes": 90
  },
  {
    "id": "2ab3960f-b4aa-448f-85a1-263b134e9432",
    "title": "revise algebra",
    "subject": "maths",
    "priority": "medium",
    "completed": true,
    "estimated_minutes": 45
  },
  {
    "id": "c16b803d-9272-41bf-890c-ea87f5201f01",
    "title": "read api docs",
    "subject": "fastapi",
    "priority": "high",
    "completed": false,
    "estimated_minutes": 60
  },
  {
    "id": "8b741b56-7472-4aae-9fa9-2800520cffe1",
    "title": "practice loops",
    "subject": "python",
    "priority": "low",
    "completed": false,
    "estimated_minutes": 30
  },
  {
    "id": "2f6508bf-4c93-485e-8cc5-de07fb51708d",
    "title": "solve equations",
    "subject": "math",
    "priority": "high",
    "completed": true,
    "estimated_minutes": 75
  }
]
```