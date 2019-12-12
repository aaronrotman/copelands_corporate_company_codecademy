#This project is for the Copeland's Corporate Company exercise from Codecademy's Computer Science course.

#The goal is to create a username and temporary password generator based on a person's first and last names. The username should be a string made up of the first three letters of their first name, and the first four letters of their last name. If the length of first name and/or last name are shorter than three and four respectively, all letters of the name are used.

#Create a function that will generate a username from the inputs first_name and last_name
def username_generator(first_name, last_name):
  #Define a temporary variable "username" and set it to an empty string
  username = ''
  #Check if the length of first_name is less than three. If so, add all characters in first_name to username.
  if len(first_name) < 3:
    username += first_name
  #Otherwise add the first three characters in first_name to username.
  else:
    username += first_name[0:3]

   #Check if the length of last_name is less than four. If so, add all characters in last_name to username.
  if len(last_name) < 4:
    username += last_name
  #Otherwise add the first four characters in last_name to username.
  else:
    username += last_name[0:4]

  return username

#Test username_generator()
#Create a variable that stores the username for testing
test_username = username_generator('Aaron', 'Rotman')
print('Username: ' + test_username)

#Create a function that will generate a password from the input username.
def password_generator(username):
  password = ''
  for character in range(len(username)):
    password += username[character - 1]
  return password

#Test password generator()
#Create a variable that stores the password for testing
test_password = password_generator(test_username)
print('Password: ' + test_password)
