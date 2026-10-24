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