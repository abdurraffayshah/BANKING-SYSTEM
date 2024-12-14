**BANKING SYSTEM**

This Python project is a simple banking system I built to simulate how basic banking operations might work. It allows users to do things like create accounts, log in, check their balance, transfer money, withdraw funds, and even delete their accounts. All of the user data (like usernames, passwords, and balances) is stored in a CSV file, which acts as a simple database. The idea is to provide a command-line interface where users can interact with the system as if it were a real bank.

### Why I Built This:

I created this project mainly to get hands-on experience with Python’s file handling and to improve my skills in building interactive systems. Here's a breakdown of what I focused on:

- **File Handling**: I used CSV files to store account details, which let me practice reading and writing data efficiently. It’s not as complex as using a full database, but it gets the job done for simulating how a bank might store user information. This way, when someone logs in or makes a transaction, the program updates the CSV file to reflect the new balances or actions taken.

- **User Authentication**: I wanted to create a basic, but effective, login system. Users input their credentials, and the program checks them against the stored data. To add a bit of realism, I also implemented a retry system—users get three attempts to log in, just like you might see in real-life applications. This part of the project helped me practice validating user inputs and controlling program flow with loops and conditions.

- **Transactions (Transfers and Withdrawals)**: The system lets users transfer money between accounts and withdraw funds from their own account. Before allowing any withdrawals, the program checks if there’s enough balance, ensuring users can’t go into debt. These features challenged me to work with basic arithmetic operations and error-checking, making sure that the system handles money the right way and prevents mistakes.

- **Menu-Driven Interface**: The program is menu-driven, meaning users can choose what action to perform by entering specific commands. This was a great way to make the program interactive and easy to use. Each option in the menu is linked to a function—whether it's checking the balance, transferring funds, or exiting the system. It taught me how to make user interactions feel more natural and flow smoothly in a text-based environment.

- **Account Creation and Deletion**: I wanted to give users full control over their accounts. They can create new accounts by entering a username, password, and initial balance. They can also delete their accounts, but only after confirming their credentials again, making sure the system remains secure. These operations reinforced my skills in managing data and structuring a program that responds to user input in real time.

### What I Learned:

Building this project was a great way for me to apply the foundational concepts I’ve learned. I got to practice:
- **Validating user inputs** and handling errors gracefully.
- Using **loops and conditionals** to create a dynamic, responsive user experience.
- Working with **CSV files** to simulate storing and updating data like a database.

Overall, this project has helped me understand how systems like this might be built in the real world. It’s a simple start, but it lays the groundwork for more advanced features I could add later, like tracking transactions or implementing different account types. For now, it’s a solid introduction to creating a basic banking system with Python.