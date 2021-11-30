"""
Created on Nov 26 2021
@author: Mengjiao ZHAO
"""

class File:
    def __init__(self):
        self.permission = "r--"   # r-read w-write x-execution for owner, owner default permission just have read.

    def chown(self,new_owner):
        """
        set new owner 
        """
        if new_owner: 
            self.owner = new_owner

    def ls(self,level=0): 
        """
        recursively prints the content of the directory and all the subdirectories,

        """       
        return self.lsplus(0) # call method lsplus
    


class PlainFile(File):

    def __init__(self,name):
        self.name = name
        self.owner = "default"
        File.__init__(self) # inherit parent class

    def __str__(self):
        return "PlainFile(" + self.name + ")"

    def __repr__(self):
        return self.namea
    
    def lsplus(self,count) :
        print(self.permission + "  " + self.owner.ljust(10)  + "  \t" + "\t"*count + self.name) # ljuest(10) method means string left aligned, and fills it with spaces to a new string of the specified length


class Directory(File):

    def __init__(self, name, filelist, owner = "default") :
        self.name = name
        self.filelist = filelist
        self.owner = owner
        File.__init__(self) # inherit parent class
    
    def __str__(self):
        try:
            ans = ""
            ans = ans + str(self.filelist[0])  
            for i in self.filelist[1:]:
                ans = ans + "," + str(i)
        except :
            ans = ""

        return "Directory(" + self.name + ",[" + ans + "])"

    def lsplus(self,count) :
        print(self.permission + "  " + self.owner.ljust(10)  + "  \t" + "\t"*count + self.name) # ljuest(10) method means string left aligned, and fills it with spaces to a new string of the specified length
        count += 1
        for i in self.filelist :
            i.lsplus(count) # recursively method lsplus


class FileSystem(File):

    statuslist = [] # Initialize the status list of class Directory
    status = 0 # Initialize the status as 0

    def __init__(self,dir):
        self.dir  = dir 
        self.statuslist.append(dir) # Puts the original class in to the statuslist

    def pwd(self):
        path = "/"
        for i in self.statuslist:
            path += i.name + "/"

        return path
    
    def ls(self):
        return self.dir.ls(self) 

    def cd(self,changefolder):
        """
        Implement a method cd() allow user move to a different directory.
        This method also allows the user to go back to the previous directory or directly to the root directory.

        parameter: 
        changefolder : the directory to be moved
        """

        temp = False # the result of initialization function cd is False
        
        #Go back to the upper level directory
        if changefolder == "..":
            if len(self.statuslist) == 1: # statuslist at least contain the one init class.
                print("Current location is root path")    
            else:
                del self.statuslist[-1] # remove the latest class
                self.dir = self.statuslist[-1] # set the upper level directory
                temp = True 

        # Go back to the parent directory, whatever subdirectory you're in.
        if changefolder == "~": 
            if len(self.statuslist) == 1:
                print("Current location is root path") 
            else:
                self.dir = self.statuslist[0] # Return the folder to its parent directory
                del self.statuslist[1:len(self.statuslist)] # delete other directory in the templist, update list status
                temp = True

        # changing the working directory
        for i in self.dir.filelist: # traverse the class of Directory's filelist
            if type(i) == Directory: # if the file list contain the Directory type, ignore the PlainFile type
                if i.name == changefolder: # if the directory want to move to exists in a subdirectory
                    self.dir = i # change the current working directory
                    self.statuslist.append(i) # add current working directory to the statuslist
                    temp = True 

        if temp == False:  
            print("The directory does not exist!")      
       
    def create_file(self,name): 
        """
        This method implements the creation of files. If the file exists, it is not created.

        parameter:
        name: the file to be created.
        
        """
        for i in self.dir.filelist: # traverse the file in current path.
            if type(i) == PlainFile and i.name == name: # if it is a file and the file to be created exists.
                print("file already exists") # then print result and return.
                return

        self.dir.filelist += [PlainFile(name)] # if the file do not exists,then create the file.

    def mkdir(self,name,owner="default"):
        """
        This method implements the creation of directory. If the directory exists, it is not created.

        parameter:
        name: the directory to be created.
        owner: the directory's owner and default owner is default.
        """
        for i in self.dir.filelist: # traverse the Directory in current path.
            if type(i) == Directory and i.name == name: #if it is a Directory and the directory to be created exists.
                print("Directory already exists") # then print result and return.
                return

        self.dir.filelist += [Directory(name,[])] #if the directory do not exists,then create the directory.
        self.dir.filelist[-1].owner = owner # give the directory owner.

    def rm(self,name):
        """
        This method implements the delete of directory or file. If the file exists, it will be delete.
        if the directory exists and the directory is empty, it will be delete. else will not worked , print the result at the same time.

        parameter:
        name: the name of directory or file to be delete.

        """
        for i in self.dir.filelist:
            if type(i) == PlainFile: # if the file type is a file.
                if i.name == name: # if the file name equal the file to be delete.
                    self.dir.filelist.remove(i) # then delete the file.
                    return 
            if type(i) == Directory: # if the file type is a folder.
                if i.name == name: # if the file name equal the name of folder to be delete.
                    if i.filelist == []: # if the folder is empty
                        self.dir.filelist.remove(i) # then remove the folder
                        return
                    else:
                        print("Sorry, the directory is not empty") # if the folder is not empty ,then return the reason.
                        return

        print("The file does not exists.") # if the name doesn't in the filelist, it will not work. return the reason.

    def find(self,name): 
        """
        This method implements the find directory or file. If the file exists, it will be return. 

        parameter:
        name: the name of directory or file to be find.
        """
        for i in self.dir.filelist :    # traverse the filelist.  
            if name == i.name :        # if the file or folder found
                self.status = 1             # mark that the status equal 1
                return self.pwd() + name  # call the method pwd() to show the path

            if type(i) == Directory :  # if i is the class of Directory
                self.cd(i.name)             # cd to the subdirectory
                result = self.find(name)    # recursively to search in the subdirectory 
                self.cd("..")               # backtrack
                if self.status == 1:  # if the status equal 1, if means the file or folder has been found
                    return result

        return False
                
    def chownR(self,newowner):
        """
        This method implements change the owner of all files and sub directories of a folder.

        Parameter:
        newowner: A new name to be replaced.
        """
        self.dir.owner = newowner
        for i in self.dir.filelist: 
            i.chown(newowner) # change the owner name to a new owner
            if type(i) == Directory: # if i is the type of Directory
                self.cd(i.name)  # cd to the subdirectory
                self.chownR(newowner)  # recursively to search in the subdirectory 
                self.cd("..") # backtrack
    
    def chmod(self,permission,filename):
        """
        This method implements change the permission of file or folder.
        (read:r, write:w, execution:x)

        Parameters:
        permission: A new permission to be replaced.
        filename: file or folder name that wants to be changed permission
        """
        for i in self.dir.filelist:
            if i.name == filename: 
                if i.permission == permission: # if the permission is same the permission wants to be changed.
                    print('The file permission already is {}'.format(permission)) # no needs change. return
                    return
                else: 
                    print("Change file permissions from {} to {}".format(i.permission,permission))
                    i.permission = permission # change the permission
                    return
                    
          
        print("The file does not exists in current path.") # return the file doesn't found.

    def mv(self,originfilename,targetfoldername):
        """
        This method implements move the file to another folder.
        if file or folder do not in current path, print error.

        Parameters:
        originfilename: file name that wants to be move.
        targetfoldername: target folder name
        """
        iffile = "" # Initializes the class value of the file.
        iffolder = 0 # Initializes the target folder index.
        for i in self.dir.filelist:  
            if i.name == originfilename and type(i) == PlainFile: # if the file is in filelist and type is PlainFile.
                iffile = i  # assign the file class to iffile
            if i.name == targetfoldername and type(i) == Directory: # if the folder is in filelist and type is Directory.
                iffolder = self.dir.filelist.index(i) # assign the folder index to iffolder
            
        if iffile !="" and iffolder != "": # if the both originfilename and targetfoldername exists.
            self.dir.filelist[iffolder].filelist += [iffile] # add file to target folder.
            self.dir.filelist.remove(iffile) # remove the file in current path.
        else: # else print error
            print("move error. Please check file or folder name.")
            

file = PlainFile("boot.exe")
folder = Directory("Downloads",[])
    
root = Directory("root",[PlainFile("boot.exe"),
               Directory("home",[
                   Directory("thor",
                      [PlainFile("hunde.jpg"),
                       PlainFile("quatsch.txt")]),
                   Directory("isaac",
                      [PlainFile("gatos.jpg")])])])
fs = FileSystem(root)