My-Alx capstone Project 

Here is a description of my Task Management Api Project
1.	Users can create, read, update, and delete tasks.
2.	Each task belongs to a specific user → no cross-user access.
3.	Tasks can be grouped into categories (Work, Personal).
4.	A task has title, description, due date, priority, and status.
5.	Priority can be Low, Medium, or High.
6.	Status can be Pending or Completed.
7.	Users can also mark a task incomplete to reopen it.
8.	Completed tasks are locked from further editing unless reopened.
9.	API supports filtering tasks by status, priority, or due date.
10.	API supports sorting tasks by due date or priority.
11.	Categories are user-specific and cannot be shared.
12.	Authentication is required 
13.	Permissions ensure only the task owner can access/edit.
14.	Endpoints auto-generated for tasks and categories (CRUD).



Registration Endpoint: http://127.0.0.1:8000/POST/register/
To craete a task : http://127.0.0.1:8000/POST/task
To view a task : http://127.0.0.1:8000/GET/task/1
Categories: http://127.0.0.1:8000/categories

