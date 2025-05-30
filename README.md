# alu-AirBnB_clone_v2

## Description

This project is a clone of the AirBnB web application, developed as part of the ALU curriculum. It implements the backend and (optionally) frontend features of a property rental platform, including user authentication, property listings, booking management, and more.

## Features

- User registration and authentication
- Property listing and management
- Booking system
- RESTful API
- Database storage (MySQL)
- Console for management and debugging

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/michael-alu/alu-AirBnB_clone_v2.git
   cd alu-AirBnB_clone_v2
   ```

2. **Install dependencies:**
   - Make sure you have Python 3.x and MySQL installed.
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up environment variables:**
   - Create a `.env` file or export the following variables:
     ```
     HBNB_MYSQL_USER=<your_mysql_user>
     HBNB_MYSQL_PWD=<your_mysql_password>
     HBNB_MYSQL_HOST=localhost
     HBNB_MYSQL_DB=hbnb_dev_db
     HBNB_TYPE_STORAGE=db
     ```

4. **Run the application:**
   ```bash
   python3 console.py
   ```

## Usage

- Use the console to manage objects:
  ```
  (hbnb) help
  (hbnb) create User
  (hbnb) show User <user_id>
  ```

- API endpoints are available if the web server is running.

## Project Structures

- `models/` - Data models and storage engines
- `console.py` - Command-line interface
- `api/` - RESTful API (if implemented)
- `tests/` - Unit and integration tests

## Authors

- [Samuel Kwizera](https://github.com/samkwizera)
- [Michael Nwuju](https://github.com/michael-alu)
