import os

os.system("rm -rf ./result/exp2")
os.system("mkdir ./result/exp2")

for conf_idx in range(0, 3):

  os.system("python ./main.py ./confs/exp2/conf" + str(conf_idx) + ".txt ./statistics.txt")

  result_path = "./result/exp2/result" + str(conf_idx)
  os.system("mkdir " + result_path)
  os.system("mv ./statistics.txt " + result_path)
  os.system("mv ./rTool/output.txt " + result_path)
  os.system("mv ./rTool/input.txt " + result_path)


