from os import scandir
for entry in scandir('datatypes'):
    if entry.is_file():
    	if len(entry.name) > 3:
    		if entry.name[-3:] == '.py' and entry.name != "__init__.py":
    			string = f'from datatypes.{entry.name}'[:-3] + f' import *'
    			exec(string)
    else:
    	string = f'from datatypes.{entry.name}' + f' import *'
    	exec(string)
