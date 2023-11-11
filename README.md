# Learning Log

## About The Project**

Learning Log is a web application that allows users to create, manage, and organize their learning topics, entries, and comments. Users can create both private and public topics, with private topics visible only to the owner, and public topics accessible to all users. Users can add entries to public topics and have the ability to edit them. Additionally, users can leave comments on each entry to facilitate discussion and collaboration.

The project is built using the Django framework for backend development, and it utilizes Django's built-in authentication system. The database is managed with SQLite. For the front-end design and styling, Bootstrap is employed to create a clean and user-friendly interface.
**
## Built With**

* [Django](https://www.djangoproject.com/) - The web framework used for backend development.
* [SQLite](https://www.sqlite.org/) - The database management system.
* [Bootstrap](https://getbootstrap.com/) - The CSS framework for front-end design.

## Getting Started**

To get a local copy of this project up and running, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/liubomyr8/learning-log.git

   Navigate to the project directory:
cd learning-log

2. **Create and activate a virtual environment (recommended):**
python -m venv venv
source venv/bin/activate

3. **Install the project dependencies:**
pip install -r requirements.txt

4. **Run the development server:**
python manage.py runserver
Open your web browser and access the application at http://localhost:8000/.

## Usage**

1. **Creating a Learning Topic**
Log in to your account or register if you are a new user.
Click on "New Topic" to create a new learning topic.
Choose whether the topic should be public or private.
Give your topic a name and description.

2. **Adding an Entry**
Select an existing public topic or create a new one.
Click "Add new entry" within the topic.
Write the entry's content and save it.

3. **Editing an Entry**
Navigate to the topic containing the entry.
Find the entry you want to edit and click "edit entry."
Make your changes and save them.
4. **Adding Comments**
Open an entry where you want to leave a comment.
Scroll to the bottom of the entry.
Enter your comment in the provided field and click "Submit."

**## Contact**
If you have any questions or need further assistance, feel free to contact the project maintainer:
Your Name - liunomyr.nych@gmail.com
Project Link: https://github.com/liubomyr8/learning-log
