# 📩 Message Board with Flask + MySQL

A simple web app to collect and display user messages using a Flask backend and MySQL database.

## Tech Stack

- Python (Flask)
- MySQL
- HTML/CSS

## Setup

1. Clone the repo
2. Create MySQL DB:
```sql
CREATE DATABASE message_db;
USE message_db;
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    message TEXT
);
