import os
import datetime
#os.remove("file_to_delete.txt")
#os.rename("file_is_renamed","file_is_renamed.txt")
print(os.path.exists("file_is_renamed.txt"))
print(os.path.getsize("file_is_renamed.txt"),"Bytes")
timestamp=os.path.getmtime("file_is_renamed.txt")  #get modified time  UNIX timestamp
print(datetime.datetime.fromtimestamp(timestamp))   #human readable date
print(os.path.abspath("file_is_renamed.txt"))    #absolute path of a file
