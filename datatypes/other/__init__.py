from os import scandir
for entry in scandir('datatypes/other'):
    if entry.is_file():
    	if len(entry.name) > 3:
    		if entry.name[-3:] == '.py' and entry.name != "__init__.py":
    			string = f'from datatypes.other.{entry.name}'[:-3] + f' import *'
    			exec(string)
    else:
    	string = f'from datatypes.other.{entry.name}' + f' import *'
    	exec(string)
