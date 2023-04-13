# Address Book
#### Video Demo:  <URL https://www.youtube.com/watch?v=vXe6Lw3HLaA>
#### Description:

#### Overview
The aim of this project is to store contact details in an address book. The user is prompted to enter name, mobile number and email address. Error messages are raised if the details are invalid. All information is stored in a CSV file and can be recalled using command line (search) arguments. 

#### Instructions
Open terminal and type 'python3 project.py'. You will be prompted to added a Name. You must enter two strings - first and last names. 
You will then be prompted for an email address. Please ensure you type this correctly, using the @ symbol. No other variations are accepted. 
Finally, you will be prompted for a mobile number. This number must start with a '0' and be 11 digits in length. 
If any of the detail are entered incorrectly, you will be presented with an error message, and will need to re-run the program.

To search for a contact, you need to type a command-line argument. Type 'python3 project.py search {name}'. The name can be both first and last names, or it can be only the first or the last name. For example. '...search ben hillier', '...search ben', '...search hillier' are all acceptable. Names can be typed upper or lower case. If the contact exists, you will be presented with details for one or more contacts, depending how many share the same name. 

#### Libraries
re is used to check the email address
sys is used to check command line argument and exit out of the program
csv is used to write to, and read from the contact.csv

#### Functions

##### Split name
This function takes as input a string with first and second name. It splits the string to 2 variables and also capitalises the first letters. It then adds both names to the contact dictionary

##### Check email
This function uses re.search to check the email is valid.

##### Check number
This function checks whether number entered is valid. The number must be 11 digits long, and start with a zero.

##### Update csv
This function opens a file called contacts and writes the contact dictionary to a new row.

##### Search address book
This function reads the contact csv file and checks if either the first or second name exist. If so then it returns the row, consisting of name, email, number.

#### Assertions 

test_project.py tests the functionality of some of the functions in project.py. test_name checks that the name is split into first and last. If not the program should exit. 
test_email checks the email contains a string of alphanumeric digits, an '@', a domain with a .com/edu/co.uk. If not, then program exits.
test_number checks the number is 11 digits long and starts with a '0'

#### Future plans
I intend to incorporate a GUI into this program, for a more user friendly experience. I am currently expploring Tkinter to do this. 

