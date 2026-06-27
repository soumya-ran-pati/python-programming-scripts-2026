c_drive = {
     "File name": [],
     "Content": []
 }

while True:

 command = input("C\\: ")
  
 if command == "cl":
     break

 elif command == "list":
     for file in range(len(c_drive["File name"])):
         print(f"{file+1}. {c_drive["File name"][file]}")
     
 elif command == "create file":
      c_drive["File name"].append(input("File name: "))
      c_drive["Content"].append(input("Content: "))
      print("File is saved to the drive.")
      
 elif command == "read file":
      search_file = input("Search file: ")
      for search in range(len(c_drive["File name"])):
          if search_file == c_drive["File name"][search]:
              print(f"Content: {c_drive["Content"][search]}")
              
 elif command == "delete file":
      search_file = input("Search file: ")
      for search in range(len(c_drive["File name"])):
          if search_file == c_drive["File name"][search]:
              print(f"{c_drive["File name"][search]} is deleted from the drive.")
              c_drive["File name"].remove(c_drive["File name"][search])
              c_drive["Content"].remove(c_drive["Content"][search])
              break
              
 elif command == "help":
     print("1. list - list the all file names in the drive.")
     print("2. create file - it used to create file")
     print("3. read file - it used to read the file content.")
     print("4. delete file - it used to delete the file.")
     print("5. cl - it used to stop the shell, all the data will free.")
     
 elif command == "":
     pass
                
 else:
     print("Wrong command!")
