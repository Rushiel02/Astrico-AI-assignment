# Astrico AI Assessment

This project is a full-stack application that manages learners, assessors, and institutions with basic reporting capabilities.

## Project Structure

```
astrico-assessment/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── learner_routes.py
│   │   ├── assessor_routes.py
│   │   ├── institution_routes.py
│   │   └── report_routes.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.js
│   │   │   ├── InstitutionForm.js
│   │   │   ├── LearnerForm.js
│   │   │   ├── AssessorForm.js
│   │   │   ├── Navbar.js
│   │   │   └── SummaryReport.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── api.js
│   ├── package.json
│   └── tailwind.config.js
└── README.md
```

## Database Design

The system uses a relational database with the following models:

1. **Institution**:
   - Primary entity for educational institutions or hospitals
   - Contains institution details and contact information
   - Has one-to-many relationships with Learners and Assessors

2. **Learner**:
   - Represents students enrolled in programs
   - Contains personal details and optional course information
   - Linked to an Institution

3. **Assessor**:
   - Represents faculty or evaluators
   - Contains personal details and role (Internal/External)
   - Linked to an Institution

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

3. Configure MySQL:
   - Create a database named `astrico_db`
   - Update the database connection string in `config.py` if needed

4. Run the Flask application:
   ```
   cd backend
   python app.py
   ```
   The backend will run on http://localhost:5000

### Frontend Setup

1. Install Node.js dependencies:
   ```
   cd frontend
   npm install
   ```

2. Start the React development server:
   ```
   npm start
   ```
   The frontend will run on http://localhost:3000

## Using the Application

1. Start by adding institutions through the "Add Institution" page
2. Once institutions are added, you can register learners and assessors
3. The dashboard displays summary statistics

## Assumptions and Simplifications

- The application assumes that users will first register institutions before adding learners or assessors
- No authentication or user management is implemented
- The UI is kept minimal and functional
- No batch data import or export features
- The application uses simple form validation