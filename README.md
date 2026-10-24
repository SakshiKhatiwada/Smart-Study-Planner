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
    "id":1,
    "title": "homework",
    "subject": "string",
    "priority": "low",
    "completed": true,
    "estimated_minutes": 1
  },
  {
    "id": 2,
    "title": "build calculator",
    "subject": "python",
    "priority": "high",
    "completed": false,
    "estimated_minutes": 90
  },
  {
    "id": 3,
    "title": "revise algebra",
    "subject": "maths",
    "priority": "medium",
    "completed": true,
    "estimated_minutes": 45
  },
  {
    "id": 4,
    "title": "read api docs",
    "subject": "fastapi",
    "priority": "high",
    "completed": false,
    "estimated_minutes": 60
  },
  {
    "id": 5,
    "title": "practice loops",
    "subject": "python",
    "priority": "low",
    "completed": false,
    "estimated_minutes": 30
  },
  {
    "id": 6,
    "title": "solve equations",
    "subject": "math",
    "priority": "high",
    "completed": true,
    "estimated_minutes": 75
  }
]
```