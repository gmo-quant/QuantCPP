#!/user/bin/python

import sys
import datetime

# each templates should contain the creation time of the file
# use a loop to create the set of files

dt = datetime.datetime.now()
dtstr = dt.strftime("%Y-%m-%d %H:%M:%S")


headerFile = sys.argv[1] 
srcFile = sys.argv[2]
testerFile = sys.argv[3]


authorName = "Guangzhuan Mo"
openComment =	"/* ===========================================================\n" 
closeComment =	" * ===========================================================*/\n"

srcComment ="""|
|  
| 	 date: {2}
| Source code: {0} 
|      Author: {1}
|
| Description:
|
| 	Input:
|
|      Output:
|
|     Process:
|	the program's steps are as follows:
|
|
| Known Bugs:
| 	None;
|	the program operates correctly
|
""".format(srcFile, authorName, dtstr) 

headerComment ="""|
|  
| 	 date: {2}
| Source code: {0} 
|      Author: {1}
|
| Description:
|
| 	Input:
|
|      Output:
|
|     Process:
|	the program's steps are as follows:
|
|
| Known Bugs:
| 	None;
|	the program operates correctly
|
""".format(headerFile, authorName, dtstr) 

testerComment ="""|
|  
| 	 date: {2}
| Source code: {0} 
|      Author: {1}
|
| Description:
|
| 	Input:
|
|      Output:
|
|     Process:
|	the program's steps are as follows:
|
|
| Known Bugs:
| 	None;
|	the program operates correctly
|
""".format(testerFile, authorName, dtstr) 




headerContent = """
#ifndef {0}
#define {0}

#endif
""".format(headerFile.upper())

srcContent = """
#include "{0}"
""".format(headerFile)

testerContent = """
{0}
""".format(testerFile)

# commentList = [srcComment, headerComment, testerComment]

headerFileTemplate =  openComment + headerComment + closeComment + headerContent

srcFileTemplate =  openComment + srcComment + closeComment + srcContent

testerFileTemplate = openComment + testerComment + closeComment + testerContent

file = open(headerFile, "w")
file.write(headerFileTemplate)
file.close()

file = open(srcFile, "w")
file.write(srcFileTemplate)
file.close()

file = open(testerFile, "w")
file.write(testerFileTemplate)
file.close()
