📘 Design Explanation – Attendance Management System

The Attendance Management System was designed using software design patterns to improve structure, maintainability, scalability, and flexibility. Instead of writing all logic in one place, the system separates responsibilities into different components. This makes the project easier to manage and extend in the future.

The following design patterns were implemented:

🔹 1. Singleton Pattern – Database Connection

The Singleton Pattern ensures that only one instance of the database connection exists in the system. The DatabaseConnection class controls the creation of the database object so that all parts of the system use the same connection.

Why it is used:

Prevents multiple database connections from being created

Saves system resources

Ensures consistent access to the database

Benefit:
Improves performance and reliability of database operations.

🔹 2. Repository Pattern – Data Access Layer

The Repository Pattern is used in the AttendanceRepository class. This pattern separates data access logic from the rest of the application. Instead of controllers or services directly interacting with the database, all database operations go through the repository.

Responsibilities of AttendanceRepository:

Add attendance records

Retrieve attendance records

Why it is used:

Keeps database logic in one place

Makes the system easier to test and maintain

Reduces code duplication

Benefit:
Improves code organization and supports future database changes without affecting business logic.

🔹 3. Factory Pattern – User Creation

The Factory Pattern is implemented through the UserFactory class. This class handles the creation of different user types such as Student, Teacher, and Admin.

Instead of directly creating objects using constructors, the system calls:

UserFactory.create_user(role)


Why it is used:

Centralizes object creation

Makes it easy to add new user roles

Reduces dependency on specific classes

Benefit:
Improves flexibility and scalability of the user management system.
