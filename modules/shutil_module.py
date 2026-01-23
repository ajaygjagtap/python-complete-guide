import shutil

'''
shutil.copy(src, dst) :
Copies a file from one place to another.
'''
shutil.copy("Raw.txt", "dummy.txt")

"-----------------------------------------------------------------------------"

'''
shutil.copy2(src, dst) :
Copies a file with metadata from one place to another.
'''
shutil.copy("Raw.txt", "dummy1.txt")

"-----------------------------------------------------------------------------"


'''
shutil.copytree(src, dst) :
Copies an entire directory tree .
'''
shutil.copy("Source_Folder", "Backup_Folder .txt")

"-----------------------------------------------------------------------------"

'''
shutil.move(src, dst) :
Moves or renames files/folder.
'''
shutil.move("Old_name.txt", "New_name.txt")     # Renameing file.
shutil.move("Raw_Folder/Note.txt", "Note.txt")  # Moving file out of a folder.

"-----------------------------------------------------------------------------"

'''
shutil.rmtree(PATH) :
Deletes an entire directory tree.
'''
shutil.rmtree("Temp_Folder")

"-----------------------------------------------------------------------------"

'''
shutil.make_archive(folder/file name, zip, source_folder) :
Creates an archive.
'''
shutil.make_archive("Backup", "zip", "My_Folder")   # Creates Backup.zip from My_Folder.

shutil.unpack_archive("Backup.zip", "extract_here") # Extracts an Archive.

"-----------------------------------------------------------------------------"

'''
shutil.disk_usage(PATH) :
Returns total, used and free space.
'''
total, used, free = shutil.disk_usage("/")
print(total, used, free)
