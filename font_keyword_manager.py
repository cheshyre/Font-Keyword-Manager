from sys import argv

commands = { 'add'           : 'add <font_name> [<keywords>]\n    Creates an association between the font name and the keywords given.\n    If a particular association already exists, it will remain unchanged.\n    If a keyword does not already exist, it will be added.',
             'find'          : 'find [<keywords>]\n    Outputs a list of all fonts that are associated with all the given keywords.\n    If no keywords are given, nothing will be output.\n    If a keyword specified does not exist, script will return a warning.',
             'list_fonts'    : 'list_fonts\n    Outputs a list of all fonts that have a place in the keyword manager.',
             'list_keywords' : 'list_keywords\n    Outputs a list of all for which there exist associations.',
             'remove'        : 'remove <font_name> [<keywords>]\n    Removes the association between the specified font and the given keywords.\n    If no keywords are specified, all assoications with the given font will\n    be removed.'
             }

if len(argv) == 1:
	print('Font Keyword Manager is a command line utility that allows simple font ')
	print('management through the use of keywords.')
	print('For more information, see <github site here>\n')
	print('usage: font_keyword_manager <command> [<args>]\n')
	print('Valid commands are:')
	print('    add           Add an assocation between a font and a set of keywords')
	print('    find          Finds all fonts that are associated with a set of keywords')
	print('    list_fonts    Lists all fonts for which there are keywords specified')
	print('    list_keywords Lists all keywords')
	print('    remove        Removes an association between a font and a set of keywords\n')
	print('See \'font_keyword_manager help <command>\' for help with a specific command')

if len(argv) == 2 and argv[1] in ['-h', 'help']:
	print('Font Keyword Manager is a command line utility that allows simple font ')
	print('management through the use of keywords.')
	print('For more information, see <github site here>\n')
	print('usage: font_keyword_manager <command> [<args>]\n')
	print('Valid commands are:')
	print('    add           Add an assocation between a font and a set of keywords')
	print('    find          Finds all fonts that are associated with a set of keywords')
	print('    list_fonts    Lists all fonts for which there are keywords specified')
	print('    list_keywords Lists all keywords')
	print('    remove        Removes an association between a font and a set of keywords\n')
	print('See \'font_keyword_manager help <command>\' for help with a specific command')

if len(argv) > 2 and argv[1] in ['-h', 'help']:
	for i in range(2, len(argv)):
		if argv[i] not in ['add','find','list_fonts','list_keywords','remove']:
			print(argv[i] + ' is not a valid command. \nSee \'font_keyword_manager help\' for a list of commands')
		else:
			print(commands[argv[i]])

