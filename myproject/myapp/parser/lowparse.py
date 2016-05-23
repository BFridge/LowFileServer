

import json
import sys
from collections import Counter
def handle_uploaded_file(f, fun):
    return fun(f)







def get_api_times_count(read_file):
    method_list=[]
    for line in read_file:
        print >> sys.stderr, line
        log_item = json.loads(line)
        method = log_item["InvokeApi"]
        #get methodname
        for item in method.keys():
            if item != 'return':
                 method_list += [item]
                 break

    result = Counter(method_list)
    return result


