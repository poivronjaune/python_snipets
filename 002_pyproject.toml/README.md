# RealPython Notes for Packaging  
[Real Python Packaking](https://www.youtube.com/watch?v=v6tALyc4C10) video
### Folder for packaging    
py folder : __main__.py : converts a directory to be called directly in python  
py -m package : Looks in path to find modular directory called package  

### Python Paths 
1) active path (current worling directory in terminal)  
2) installed libraries  

Do not use sys.path.append("filepath"), this does not scale and has many issues for cde sharing.  

### History of packaging
distutils : deprecated  
setuptools : not standard library  
PEP : Python Enhancement Proposals (defined how to package)  
- PEP 427 (wheels)
- PEP 440 (verison numbers)
- PEP 508 (dependencies)
- PEP 517 (build backend)
- PEP 621 (project metadata)
- PEP 660 (editable installs)

### Local packaging  
[pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)  and [PEP621](https://peps.python.org/pep-0621/) : detailed information on pyproject.toml    
Contains information avout python projects -> Supposed to be intuitive  
Replaces all other previous pyton packaging tools  