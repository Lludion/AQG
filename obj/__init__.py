from os import scandir
for entry in scandir('obj'):
    if entry.is_file():
    	if len(entry.name) > 3:
    		if entry.name[-3:] == '.py' and entry.name != "__init__.py":
    			string = f'from obj.{entry.name}'[:-3] + f' import *'
    			exec(string)
