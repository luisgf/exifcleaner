#!/usr/bin/env python3

"""
    EXIF Cleaner. A tool to clean EXIF metadata from files

    Luis González Fernández (c) 2015
                                     luisgf at luisgf . es   

"""

import os
import sys
from subprocess import check_call, CalledProcessError, DEVNULL

class ExifCleaner():    
    def __init__(self, folder_list=None, verbose=False):
        self.folders = folder_list
        self.verbose = verbose
        self.errors = []

    def clean_exif(self, path):
        """ Clean EXIF metadata using exiv2 """

        try:
            args = ['exiv2', 'rm', path]
            check_call(args, shell=False, stdout=DEVNULL, stderr=DEVNULL)
            
            if self.verbose:
                print('File %s cleaned' % path)
        
        except FileNotFoundError:
            print('exiv2 not found. Please install it!')
            sys.exit(-1)
        
        except CalledProcessError as e:
            if self.verbose:    
                print('Error cleaning EXIF in %s' % path)

            if path not in self.errors:
                self.errors.append(path)               

    def check_exif_presence(self, path):
        """ Check the EXIF metadata presence in a given file """
        rc = False

        try:
            args = ['exiv2', 'pr', path]
            check_call(args, shell=False, stdout=DEVNULL, stderr=DEVNULL)
            rc = True         # File has exif, rc=0 running exiv2

        except CallProgramError as e:
             if e.returncode is 253:
                 pass          # File hasn't exif
             else:
                 raise 
        finally:
            return rc


    def Start(self):
        wiped = 0     # Num of wiped files
        for folder in self.folders:
            if self.verbose:
                print('Cleaning: %s' % folder)

            for path in os.listdir(folder):
                file_path = os.path.join(folder, path)
           
                if self.check_exif_presence(file_path):
                    self.clean_exif(file_path)
                    wiped += 1
        
        print('EXIF data cleaned in %d Files. Errors %d' % (wiped,len(self.errors)))
 
    def has_errors(self):
        """ Return True if some file has errors """

        return True if len(self.errors) > 0 else False

    def show_errors(self):
        """ Show the errors after execution """

        if self.errors:
            print('Clean error in:')
            for file in self.errors:
                print('   %s' % file)   

    def set_verbose(self, value):
        self.verbose = bool(value)

    def set_folders(self, folders):
        """ Set the folder list to check """

        self.folders = folders

if __name__ == '__main__':
    params = [param for param in sys.argv]
    params.pop(0)

    exif = ExifCleaner()      

    if '-v' in params:
        exif.set_verbose(True)  
        params.pop(params.index('-v'))

    if len(params) is 0:
        print('Please, pass a liste of folders to check as parameter')
        print('Example: %s /folder1 [/folder2 /folder3' % sys.argv[0])
        sys.exit(-1)
    else:
        exif.set_folders(params)

    exif.Start()

    if exif.has_errors():
        exit.show_errors()
                
    
    
