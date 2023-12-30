jobs = [
    ("j1",2,50),
    ("j2",1,15),
    ("j3",2,10),
    ("j4",1,25),
]

n = len(jobs)
job_seq = [-1] * n
slots = [False] * n
jobs.sort(key=lambda x: x[2], reverse=True)

for job in jobs:

    for i in range(min(n,job[1]-1),-1,-1):
        if not slots[i]:
            job_seq[i] = True
            slots[i] = True
            break

selected_jobs = []
total_profit = 0

for i in range(n):
    if job_seq[i] != -1:
        selected_jobs.append(jobs[i][0])
        total_profit += jobs[i][2]

print(selected_jobs)
print(total_profit)