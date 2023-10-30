METHODS
------------------------------------------------------------------------------------------------
Try-Except statements can be found in this version of my 16.1 homework in the form of file read testing. The script essentially tries to read the files and process the data before proceeding to the main body of the program. If either of these steps fails, the script returns a message regarding the positional arguments and required file types.

DISCUSSION
------------------------------------------------------------------------------------------------
Compared to If-Else testing of correct inputs, Try-Except provides a convenient catch-all solution to making sure the inputs are what you expect. Particularly when dealing with individual user input, programs need to be fault tolerant due to the open-ended nature of user input and the rigid interpretive capacity of computers. Typically, it is more expedient to check for acceptable input before proceeding and try to handle it--otherwise, the program may show the user the full error message and/or crash. Alternatively, some programs engineer user interfaces to prevent "incorrect" inputs from users that will cause issues.