import subprocess

r = subprocess.Popen("python rand.py", stdout=subprocess.PIPE, shell=True)

r = r.communicate()[0]

with open("out.txt", "wb+") as file:
    file.write(r)