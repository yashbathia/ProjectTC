import os
import pprint
import sys

from enchant.checker import SpellChecker

project_dir = sys.argv
chkr = SpellChecker("en_US")
err_dict = {}

for root, directories, filenames in os.walk('/Users/yashbathia/magnum'):
    for filename in filenames:
        # To display all files in all subdirs
        print os.path.join(root,filename)
        if '.py' in filename:
            with open(os.path.join(root,filename), 'r') as f:
                data = f.read().split('\n')
                comments = [x for x in data if '#' in x]
                #print("comment is", comments)
                #print("data is", data)
                for comment in comments:
                    chkr.set_text(comment)
                    for err in chkr:
                        #print(("ERROR:{0}").format(os.path.join(root,filename)), err.word)
                        err_dict[("{0}").format(os.path.join(root,filename))] = err.word

print("Error information:")
pprint.pprint(err_dict)









