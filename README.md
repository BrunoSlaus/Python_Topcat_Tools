# Python_Topcat_Tools

This folder contains the codes that are used together
with the TOPCAT program.

Topcat can take commands from the terminal. The codes
use the os.system command to write strings into the terminal.
This means that the codes in this folder can give commands
directly to Topcat. In other words these codes are Python codes
(Python functions) used to automatise Topcat.

To understand the Topcat-terminal comands (i.e. to understand
what needs to be written into the terminal) see:

http://www.star.bristol.ac.uk/~mbt/stilts/


WARNING: The "os" command is old. Use "subprocess.call" instead
         if you are re-writing the codes.

The most important code is the Topcat_Match.py code used for
matching two fields.  

The folder contains:
1) Topcat_Column_Remove.py: A program that removes a column
                            from a fits file.
2) Topcat_Match_Remove.py : A program that removes all the rows
                            obtained in a match.
3) Topcat_Match_Self.py   : A program that does the matching
                            of 1 field with that same field.
4) Topcat_Match.py        : A program that does the matching 
                            between 2 fields.
5) Topcat_Subset.py       : A program that creates a subset
                            from a given fits file.
