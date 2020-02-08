import os

report_dir='./test_report'

lists=os.listdir(report_dir)
print(lists)

lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))

print("the latest report is "+lists[-1])

file=os.path.join(report_dir,lists[-1])
print(file)