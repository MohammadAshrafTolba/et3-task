# et3-task
Simple web application for employees to submit requests for leave and and for managers to approve/decline the requests.

## Website snippets
![Arch Diagram of website](/documentation/login.png)
![Arch Diagram of website](/documentation/incoming_requests.png)
![Arch Diagram of website](/documentation/past_requests.png)
![Arch Diagram of website](/documentation/home.png)

## Tech used
- Frontend: HTML / CSS / Bootstrap4 / JS
- Backend: Flask / SQLAlchemy as ORM / sqlite3
- Different packages used are mentioned in the requirements.txt file
  
## How to run
<ol>
<li>Populate db: ``python -m app.populate_db``</li>
<li>Run server: ``python app_runner.py``</li>
</ol>
**<em>You can run the server without the first step but it is better to populate db with new requests to approve/decline them</em>**

## Current users (for testing pyrposes)
| Employee ID | Employee Name | Employee Email | Password | Manager ID |
| --- | --- | --- | --- | --- |
1 | Ahmed | employee1@example.com | pass123 | 3 |
2 | Aly | employee2@example.com | 123pass | 1 |
3 | Mohamed | employee3@example.com | pass123 | none |
4 | Ashraf | employee4@example.com | 123pass | 1 |
5 | Ibrahim | employee5@example.com | 123pass | 3 |

## Assumptions
- No normal registration scenario, only admins register accounts
- Each employee have only one direct manager, managers would manage multiple employees ofcourse
- Managers can make leave request from their managers
- When an employees submit a leave request they must specify the reason behind that
- A manager would approve/decline incoming leave requests
  
## Features
- passwords' hash are being stored in the db instead of actual passwords
- User Sessions and db are secure by generating safe APP_KEY (in the config)
- Some routes won't work if accessed without logging in

## What is working
- Logging in
- Submiting a leave request
- As an employee I can see previous requests I made and see what was their status (unanswered, approved, declined)
- As a Manager I can view incomming requests and approve/decline them

## Features would be nice to have if I had more time
- I wanted to additional admin functionality like viewing statistics, add/delete users, assigning employees to managers (I have made some of utility functions in the handlers' modules to support those features but didn't have enough time)

## Architecture Diagram
### Layered Architecture
![Arch Diagram of website](/documentation/arch_diagram.png)

## Notes
- The whole code base is well commented, and the above arch diagram pretty much describes the project flow
- Didn't have time for further documentation

