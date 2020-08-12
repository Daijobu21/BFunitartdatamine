import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherUnitIlls(filename):

    try:
        f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/21600/content/unit/img/" + filename)
        #f = urllib.urlopen("http://v2.cdn.android.brave.a-lim.jp//unit/img/" + filename)
        fetched = f.read()
        f.close()
        
        print(filename, "found")
        f = open ("resultEX/" + filename, "wb")
        f.write(fetched)
        f.close()

        global foundFilesCount
        foundFilesCount += 1

        write_to_log("BFGL Unit Illustration", "Found " + filename + "\n")
        
    except urllib.error.URLError:    
        print("File not found : ", filename)
        

############################################################
#==========================================================#
############################################################


if __name__ == "__main__":

    alreadyExistFiles = []

    for filename in glob.glob("resultEX/" + "*.png"):    
        alreadyExistFiles.append(filename[9:])

    print("Already exist: ", len(alreadyExistFiles))

    for i in range(1, 7):
        for j in range(1, 150):
            for k in range(7, 9):
                s = "unit_ills_full_8%d%03d%d_2.png" % (i, j, k)                
                if not (s in alreadyExistFiles):
                    fileList.append(s)
                elif (s in alreadyExistFiles):
                    print(s, "already exist")

    for i, filename in enumerate(fileList):        
        threadList.append(Thread(target = gatherUnitIlls, args = (filename,)))        

    for threadIndividual in threadList:
        sleep(0.02)
        threadIndividual.start()
    
    for threadIndividual in threadList:
        threadIndividual.join()

    write_to_log("BFGL Unit Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
