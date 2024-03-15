# doc file va xu ly text:
# doc text -> file tu dien: word
# python run_file_python.py text.txt output.txt
# 
import sys, os
from tqdm import tqdm
import time

# check dir/file
# os.path.isdir(); os.path.isfile

# create dir
# os.makerdirs()

# os.path.dirname()
# os.path.basename()
# print(len(sys.argv)) # list argument

if len(sys.argv) < 3:
    print(f"python {sys.argv[0]} text.txt output.txt")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
result = []
output_dir = os.path.dirname(output_file)
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)
start = time.time()
with open(input_file, 'r') as f:
    for line in tqdm(f.readlines(), desc="Process line"):
        for word in line.split():
            result.append(word)
        # result += line.split()
        time.sleep(2)
print(time.time() - start)
result = set(result)
with open(output_file, 'w') as f:
    f.write("\n".join(result))
    # for word in result:
    #     # f.write(word + '\n')
    #     f.writelines(word)
    
