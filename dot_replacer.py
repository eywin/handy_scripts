import os

def replace(path, R):
    old_names = os.listdir(path)
    dcount = 0
    fcount = 0
    subdirs = []
    
    for n in old_names:
        if os.path.isdir(os.path.join(path, n)):
            s = n.split('.')
            nn = ""
            if len(s) != 1:
                for i, p in enumerate(s):
                    if i < 1:
                        nn += p
                    else:
                        nn += " "+p
                    
                os.rename(os.path.join(path, n), os.path.join(path, nn))
                subdirs.append(os.path.join(path, nn))
                dcount += 1
            else:
                subdirs.append(os.path.join(path, n))
        
        elif os.path.isfile(os.path.join(path, n)):
            s = n.split('.')
            nn = ""
            if len(s) != 2:
                for i, p in enumerate(s):
                    if i < 1:
                        nn += p
                    elif i == len(s)-1:
                        nn += "."+p
                    else:
                        nn += " "+p
                    
                os.rename(os.path.join(path, n), os.path.join(path, nn))   
                fcount += 1

    if dcount != 0 or fcount != 0:
        print(f"Changed {dcount} folder name(s), {fcount} file name(s) in '{path}'")

    if R:
        for d in subdirs:
            replace(d, R)


if __name__ == "__main__":
    import argparse as argp
    parser = argp.ArgumentParser(prog ="dot replacer",
        description="searches through a folder and replaces '.' in" \
                    " file and directory names with spaces (except for filename-extensions)")
    parser.add_argument('-r', '--recursive', dest="R", action="store_true", help="runs the script recursively")
    parser.add_argument('-d', '--directory', dest="path", type=str, help="specifies working directory", default=os.getcwd())
    args = parser.parse_args()
    replace(args.path, args.R)
