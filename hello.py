import sqlite3

# Connect to the database
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Fetch all users from the 'users' table
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()

# Print the users
for user in users:
    print(user)

# Close the connection
connection.close()