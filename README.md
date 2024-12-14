**BANKING SYSTEM**

This Python project is a basic simulation of a banking system that provides users with core functionalities like creating accounts, logging in, checking balances, transferring funds, withdrawing money, and deleting accounts. It uses a CSV file to store user information (username, password, and balance), which serves as a simple database to maintain account data. The program is designed with a focus on user interaction through a command-line interface.

### Why I Built This:

I developed this banking system to strengthen my understanding of several fundamental programming concepts, particularly focusing on file handling and user interaction. Here's a breakdown of the key aspects:

- **File Handling**: The program uses CSV files to store user account information, including usernames, passwords, and balances. Every time a user logs in, transfers funds, or withdraws money, the CSV file is updated accordingly. This simulates a basic database structure without the complexity of actual database management systems, allowing me to practice reading from and writing to files using Python's CSV library.

- **User Authentication**: A critical part of the system is secure user login. The program checks entered credentials against the CSV file, granting access if the information matches. The program also includes a retry system that locks the user out after three failed login attempts. This allowed me to practice implementing loops and conditions to manage user inputs in a way that mimics real-world login systems.

- **Transaction Processing**: Users can transfer money to other accounts or withdraw funds from their own account. The program ensures that sufficient funds are available before processing withdrawals and updates the CSV file to reflect the new balances. This functionality required me to work with integer calculations and error-checking, ensuring that account balances never go negative, and reflecting these changes in real-time for the user.

- **Interactive Menu**: The user interacts with the system through a menu that allows them to choose different banking options such as checking balances, making transfers, or deleting accounts. Each operation is connected to specific input commands, which made me focus on designing a clean and intuitive command-line interface for the user. This part of the project helped me organize code and streamline user interaction by using loops and conditionals effectively.

- **Account Management**: Users can create accounts with a username, password, and an initial deposit. This function demonstrates my ability to handle user input, write new data to a file, and make the system scalable by allowing multiple accounts to be added. In addition, account deletion ensures that users can remove their data securely by verifying login details before removing their information from the CSV file.

### Project Learning Outcomes:

This project allowed me to apply several core programming principles in a practical setting. By building a functioning banking system, I enhanced my understanding of:
- **User input validation** to handle various situations where the user might enter incorrect or unexpected information.
- **Loops and conditionals** for handling the different paths the user can take within the menu and account management system.
- **File I/O** and how to manage external data (in this case, a CSV file) efficiently within a Python program.

In the future, this project could be expanded to include more complex banking features like interest calculations, account types, and transaction histories. However, for now, this program serves as a strong foundation for learning how a basic system can be structured and the core principles behind how user data is managed and transactions are handled.