You have been tasked with writing an application to remove records (lines) in a flat file where the number in the first column is strictly less than 7500 and is a prime number. The file is in a comma separated value (CSV) format that has two fields (columns):

· A number, which is a long unsigned integer and may be non-unique; and

· A string that may contain up to and including 1024 characters.

An example set of inputs and outputs is given in the table below. Note that 7867 is a prime.

Input 

1,foo
6,bar
8,baz
211,lorem
7,ipsum
32,!?#
7867, 

Output

1,foo 
6,bar 
8,baz 
32,!?# 
7867,

The application shall read the file from stdin and write its output to stdout. Examples of how this application could be used are shown in the table below.

OS Example Usage

Windows type file.csv | python filter.py

Unix cat file.csv | python filter.py

This application will be relied upon by other team members and people outside your team. The file may contain many records (tens of billions) and thus scalability with respect to run time and memory usage is important.