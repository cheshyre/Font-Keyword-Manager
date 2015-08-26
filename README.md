# Font-Keyword-Manager
This is a simple font management command line utility to associate fonts with keywords, so that later you can search for fonts based on a set of keywords. It works with both Python 2 and Python 3 but, because of how the data is saved (using pickle), Python 2 cannot read any data written by Python 3.

## Usage
The goal of this utility is for you to build for yourself a dictionary of sorts to allow you to easily find fonts that have certain features. To add a connection between a font and one or several keywords, run the following command:

'''
python fkm.py add <font name> <keyword> [<keyword> ...]
'''
Example:
'''
python fkm.py add dupla "sans serif" dialogue
'''

As usual, if an item you are adding contains a space, use quotes. Adding an already existing connection will simply overwrite it.

To remove connections, fonts, or keywords from your dictionary, run the following commands (respectively):

'''
python fkm.py remove -f <font name> [<font name> ...] -k <keyword> [<keyword> ...]
python fkm.py remove -f <font name> [<font name> ...]
python fkm.py remove -k <keyword> [<keyword> ...]
'''
Example:
'''
python fkm.py remove -f dupla "kozuka mincho" -k jp serif dialogue
python fkm.py remove -f dupla "kozuka mincho"
python fkm.py remove -k jp serif dialogue
'''

Note: when removing several fonts and keywords at once, the manager will remove all connections between *any* fonts and keywords given if they exist. As a result, you may accidentally remove connections you didn't mean to if you pass in too many fonts and keywords.
