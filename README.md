# Loan Onboarding & Data Transformation System

This is a full-stack loan onboarding platform built with Django and React. The system allows for the creation of new loan applications, retrieval of loan data, and transformation of that data into different formats (JSON and XML) as per specified requirements.

### ✨ Features

* **Create Loans:** A secure API endpoint to create new loan applications with nested customer and address data.
* **Retrieve Loan Data:** Fetch full loan details using a unique loan number (UUID).
* **JSON Transformation:** A dedicated service to transform the raw loan data into a simplified, custom JSON structure.
* **XML Generation:** Generate a structured XML document from the transformed loan data using a Jinja2 template.
* **React Frontend:** A minimal and responsive user interface built with React and Vite, styled with Bootstrap, for creating and searching for loans.
* **Unit Tested:** Includes backend unit tests for the API creation endpoint and the JSON transformation logic.

### 🛠️ Technologies Used

* **Backend:**
    * Python
    * Django & Django REST Framework (DRF)
    * Jinja2 (for XML templating)
    * JMESPath (for JSON transformation)
* **Frontend:**
    * React (with Vite)
    * Bootstrap 5 (for styling)
* **Database:**
    * SQLite3 (for development)

### 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

* Python 3.8+
* Node.js and npm
* Git

#### 1. Clone the Repository

```bash
git clone [https://github.com/rahulbhardwaj01/loan-onboarding-system.git](https://github.com/rahulbhardwaj01/loan-onboarding-system.git)
cd loan-onboarding-system
```

#### 2. Backend Setup

First, set up the Django backend server.

```bash
# 1. Create and activate a Python virtual environment
python -m venv venv
# On Windows:
# venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# 2. Install the required Python packages
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. (Optional but Recommended) Create a superuser to access the admin panel
python manage.py createsuperuser

# 5. Run the backend server
python manage.py runserver
```

Your Django backend will now be running at `http://127.0.0.1:8000`.

#### 3. Frontend Setup

In a **new terminal**, navigate to the `frontend` directory and set up the React application.

```bash
# 1. Navigate to the frontend folder
cd frontend

# 2. Install the required npm packages
npm install

# 3. Run the frontend development server
npm run dev
```

Your React application will open in your browser, likely at `http://localhost:5173`.

### 🧪 Running Tests

To run the automated backend tests, navigate to the project's root directory with your virtual environment activated and run:

```bash
python manage.py test
```

This will run tests for the API endpoints and the JSON transformation logic.

### 📋 API Endpoints

* `POST /api/loans/` - Creates a new loan application.
* `GET /api/loans/<uuid:loan_number>/` - Retrieves the raw details of a specific loan.
* `GET /api/loans/<uuid:loan_number>/json/` - Retrieves the transformed JSON for a specific loan.
* `GET /api/loans/<uuid:loan_number>/xml/` - Retrieves the generated XML for a specific loan.
