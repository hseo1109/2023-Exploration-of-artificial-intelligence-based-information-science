import numpy as np
mid=[10,20,30]
final=[90,70,80]
mid_scores=np.array(mid)
final_scores=np.array(final)
print(type(mid),type(mid_scores))

total=list()
avg=[]
for i in range(len(mid)):
    total.append(mid[i]+final[i])
    avg.append(total[i]/2)
print(f"Total : {total}")
print(f"Average : {avg}")