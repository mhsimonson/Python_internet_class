import subprocess

p=subprocess.Popen('python mhs_print_time_try.py',stdout=subprocess.PIPE)
print p.wait()

print "=="
print p.stdout.read()
print "=="



## dive into cherry pie - remedial web programming plumbing goo..."
## keep a log of things I trip over comprehension




#popen.communicate() # returns a tuple (stdoutdata,stderrdata)

#stdout=PIPE



