import sys
import os
from pathlib import Path
sys.path.insert(0, 'src')

def main(targets):
    
    # Target `report`
    if 'report' in targets:
        # Get path of this file
        wd = str(Path(__file__).parent.absolute())
        # Notebook path contains necessary files
        build_path = wd + '/notebooks'
        notebook_path = wd + '/notebooks/report.ipynb'
        # Output to `bin` folder
        output_path = wd + '/bin/report.pdf'
        
        # Arguments for nbconvert
        args1 = [
            'nbconvert',
            notebook_path,
            '--to pdf',
            '--output ' + output_path,
            '--no-input', # Hide source from report
            '--execute', # Execute all cells
            '--Execute.Preprocessor.timeout=999999' # Prevent execution timeout
        ]
        
        command = 'cd ' + build_path + ' && jupyter ' + ' '.join(args1) + ' && cd ' + wd
        os.system(command) # Run build script
        

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)