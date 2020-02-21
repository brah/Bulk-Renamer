# importing os module 
import os 

# Function to rename multiple files 
def main():
    print("Enter text to replace")
    text_one = input()
    print("Enter text to replace with")
    text_two = input()
    for filename in os.listdir():
        # find first character set, replace with second
          os.rename(filename, filename.replace(text_one, text_two))

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 