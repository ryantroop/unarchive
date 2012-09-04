"""Extract a folder or specific files in a folder as needed by user"""
import os, sys, zipfile, tarfile


class file_to_open(object):
    """This is the object to contain all the file names to unzip, based on type.
    The extract function will unpack files based on archive name.
    """
    def __init__(self, filename):
        self.fp = os.path.abspath(filename)
        self.extension = os.path.basename(self.fp)
        if 'gz' or 'bz' in self.extenson:
            fnex, ex1 = os.path.splitext(self.fp)
            self.filename, ex0 = os.path.splitext(fnex)
            self.extension = ex0+ex1
        else:
            self.filename, self.extension = os.path.splitext(filename)
        
    def __repr__(self):
        return "Archive object located at {} --> with extension {}".format(self.fp, self.extension)
    
    def extract(self):
        """Use appropriate extracter to place extracted files in a folder based on the
        filename"""
        if '.zip' in self.extension:
            #use zipfile
            archive = zipfile.ZipFile(self.fp)
            working_path = r'{}'.format(self.filename)
            os.mkdir(working_path)
            archive.extractall(path=working_path)
        tar_extensions = ['.tar', '.tar.gz', '.tar.bz']
        if self.extension in tar_extensions:
            #use tar
            if self.extension == '.tar.gz':
                archive = tarfile.TarFile.open(self.fp, 'r:gz')
            elif self.extension == '.tar.bz':
                archive = tarfile.TarFile.open(self.fp, 'r:bz')
            else:
                archive = tarfile.TarFile.open(self.fp, 'r')
            
            working_path = r'{}'.format(self.filename)
            print (working_path)
            try:
                os.mkdir(working_path)
            except Exception as ex:
                print(ex)
            for item in archive:
                archive.extract(item)
        
        
    
    

if __name__ == "__main__":
    while True:
        # main loop
        type_of_extract = input("1: Individual File\n2: Folder with all supported extensions\n3: Exit\n//>> ")
        choices = ['1', '2', '3']
        if type_of_extract not in choices:
            print("That is not a valid choice, please try again.")
        else:
            if type_of_extract == '1':
                # if we want a specific file...
                fname = input("File name or location >> ")
                try:
                    to_extract = file_to_open(fname)
                    to_extract.extract()
                    if input("Press any key to exit..."):
                        pass
                    sys.exit()
                except Exception as ex:
                    print (ex)
                    if input("Press any key to exit..."):
                        pass
                    sys.exit()
            elif type_of_extract == '2':
                #otherwise unpack all files with extensions supported
                if input("Press any key to exit..."):
                    pass
                sys.exit()
            else:
                if input("Press any key to exit..."):
                    pass
                sys.exit()