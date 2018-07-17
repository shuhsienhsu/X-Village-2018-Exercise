date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')

f = open('note.txt','w')
f.write(date+"\n")
f.write(event+"\n")
f.write(description+"\n")
f.close()

#g = open('note02.txt','w')
#g.writelines(date,event,description)
#g.close()