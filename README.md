📚** SilentLibrary Project**
SilentLibrary is a modern Django-based library management system. This project allows users to browse books and administrators to manage the library collection and user database through a custom-styled dashboard using the #1A3E6B primary color theme.

Follow these instructions to get the project up and running on your local machine using VS Code.

**1. Prerequisites**
Ensure you have the following installed:
Python 3.10+
MySQL Server 8.0
Git
VS Code (with the Python Extension installed)

**3. Clone the Repository**
Open your terminal and run:
Bash
git clone https://github.com/your-username/Slient-Library-Django.git
cd silent-library
3. Set Up a Virtual Environment
It is recommended to use a virtual environment to keep dependencies organized.

Bash
# Create the environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (Mac/Linux)
source .venv/bin/activate
4. Install Dependencies
Install the required packages (Django, Bootstrap icons, etc.):

Bash
pip install django
# If you have a requirements file:
# pip install -r requirements.txt
5. Database Setup
Apply the migrations to create the local SQLite database and set up your admin account.

Bash
# Create database tables
python manage.py migrate

# Create an Administrator account (to access the Admin Dashboard)
python manage.py createsuperuser
6. Run the Project
Start the development server:

Bash
python manage.py runserver
Open your browser and navigate to: http://127.0.0.1:8000/

**🛠 Project Features**
**User Authentication**: Secure Login, Registration, and Profile management.

**Admin Dashboard**: Full CRUD (Create, Read, Update, Delete) for managing library users.

**Book Management**: Add, View, Delete and Edit book details with image upload support.

**Responsive Design**: Built with Bootstrap 5 and customized with a professional navy blue theme (#1A3E6B).

📁 **Project Structure**
Plaintext
mylms/
├── core/               # Project settings
├── library/            # Main application logic
│   ├── migrations/
│   ├── templates/      # HTML files (base, dashboard, forms)
│   ├── models.py       # Database schema
│   └── views.py        # Logic for the library and admin tools
├── manage.py           # Django management script
└── .gitignore          # Files ignored by Git
**📄 License**
This project is for educational purposes as part of the SilentLibrary Project.

**VS Code Tips:**
Terminal: Use Ctrl + ` to toggle the terminal inside VS Code.

Debugger: You can use the "Run and Debug" tab to set breakpoints in your views.py.

Formatting: Use Shift + Alt + F to auto-format your HTML templates for better readability.
