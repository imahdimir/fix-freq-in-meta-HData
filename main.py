"""

    """

import json
from pathlib import Path

import pandas as pd
from mirutil.pathes import get_all_subdirs
from mirutil.pathes import has_subdir


class Params :
    _pth = '/Users/mahdi/Library/CloudStorage/OneDrive-khatam.ac.ir/Datasets/Heidari Data/V2'
    root_dir = Path(_pth)

p = Params()

class ColName :
    path = 'path'
    mp = 'mp'

c = ColName()

conv1 = {
        "Annual"    : "A" ,
        "Monthly"   : "M" ,
        "Quarterly" : "Q" ,
        "Seasonal"  : "Q" ,
        's'         : 'S' ,
        "Daily"     : "D" ,
        }

def fix_jsons(jsp) :
    with open(jsp , 'r') as fi :
        js = json.load(fi)

    if js['freq'] in conv1.keys() :
        js['freq'] = conv1[js['freq']]
    else :
        js['freq'] = None

    with open(jsp , 'w') as fo :
        json.dump(js , fo , indent = 4)

def main() :
    pass

    ##
    # 1. get all subdirs
    subs = get_all_subdirs(p.root_dir)
    ##
    df = pd.DataFrame()
    df[c.path] = list(subs)
    ##
    msk = ~ df[c.path].apply(has_subdir)
    df = df[msk]
    ##
    df[c.mp] = df[c.path] / 'meta.json'
    ##
    _ = df[c.mp].apply(fix_jsons)

    ##

    ##

##
if __name__ == "__main__" :
    main()
    print("Done!")
