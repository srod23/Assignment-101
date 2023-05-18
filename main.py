
# WRITE THE USER NAME, STREET ADDY, AND PHONE # TO A COMMA SEPARATED LINE
def write(filename, username, streetAddress, phoneNumber):
  with open (filename, 'w') as fileHandle:
    fileHandle.write(f'{username}, {streetAddress}, {phoneNumber}')

# READ THE FILE
def read(filepath):
  print(f"Reading '{filepath}': ")
  with open(filepath, 'r') as fileHandle:
    data = fileHandle.read()
  print(data)

# CATCH EDGE CASES
def validateInputs(filename, username, streetAddress, phoneNumber):
  if len(filename) <= 0 or len(username) <= 0 or len(streetAddress) <= 0 or len(phoneNumber) <= 0:
    print('❌ Unable to Validate User Info, please try again ❌')
    print(' ')
    main()
  else:
    print('✅ User Info Validated ✅')
    print(' ')


def main():

  # PROMPTS USER FOR FILENAME, NAME, STREET ADDRESS, AND PHONE NUMBER
  filename = input("Please enter a name for your file. ")
  username = input("Please enter your first name. ")
  streetAddress = input("Please enter your street address. ")
  phoneNumber = input("Please enter your phone number. ")
  print(' ')

  # VALIDATE USER INPUTS
  validateInputs(filename, username, streetAddress, phoneNumber)

  # IF USER INPUTS ARE VALIDATED CALL WRITE FUNCTION
  write(filename, username, streetAddress, phoneNumber)

  # READ THE FILE THAT WAS WRITTEN
  read(filename)

main()