import os
import sys
# Other required imports

def BackupDB():
    # Backup procedure
    # Use error handling mechanism using Try...Except block
    # Check the file already exists.  If exists, delete the file
    # Create new backup file
    # Validate the process
    # return FullPath_of_Backup_File (Eg: c:\Users\user1\Documents\DBBackup.SQL)
    pass

def ZipFile(SourceFile):
    # Zip Procudure
    # Check the zip file is already exists in the path, if exists, remove it
    # Check the SourceFile exists, if exists, do the zip process
    # Return Full_Path_of_ZipFile
    pass

def Upload(SourceFile):
    # FTP Upload procedure
    # Check the zip file exists
    # if exists, upload to ftp
    # Check ftp folder for duplicate
    # return True/False status based on Success or failure
    pass

# Main script
BACKUP_FILE=BackupDB()
ZIP_FILE=ZipFile(BACKUP_FILE)
UPLOAD_STATUS=Upload(ZIP_FILE)

if UPLOAD_STATUS==True:
    print ('Upload completed')
else:
    print ('Upload failed')
