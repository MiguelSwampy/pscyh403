#PsychoPy keypress exercises
#1
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)

rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

for trial in range(nTrials):
    rt_clock.reset()  # reset timing for every trial
    cd_timer.add(2) #add 2 seconds

    event.clearEvents(eventType='keyboard')  # reset keys for every trial
    count = -1 #reset counter for every while loop
    while cd_timer.getTime() > 0: #for 2 seconds

        my_text.text = "trial %i" % trial
        my_text.draw()
        win.flip()

        keys = event.getKeys(keyList=['1', '2'])  #collect keypresses after first flip

        if keys:
            count = count + 1
            if 'escape' in keys:
                win.close
            if count == 0:
                resp_time = rt_clock.getTime() #use getTime to determine the response time
                print(keys, resp_time) #print keys and response times

#Recording data exercises 
from psychopy import core, event, visual, monitors
import numpy as np

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks
resp_time = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

for block in range(nBlocks):
    sub_resp[block] = [0]*nTrials
    sub_acc[block] = [0]*nTrials
    prob[block] = [0]*nTrials
    corr_resp[block] = [0]*nTrials
    resp_time[block] = [0]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be somethi1ng other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])
print(resp_time)
win.close()

#Save csv exercises
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os

filename = 'Subject1Session1Nov212022.csv'

main_dir = os.getcwd()
data_dir = os.path.join(main_dir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
fullAddress = os.path.join(data_dir, filename)
print(fullAddress)

nBlocks = 2
nTrials = 4

responseData = dict()
responseData[0] = {'Block': 0, 'SubjectResponse': [-1,2,3,4], 'ResponseTime': [200,300,200,300]}
responseData[1] = {'Block': 0, 'SubjectResponse': [-2,3,1,4], 'ResponseTime': [220,320,220,320]}

with open(fullAddress, 'w', newline = '') as csvfile:
    fieldnames = ['Block', 'Trial', 'SubjectResponse', 'ResponseTime']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    
    writer.writeheader()
    for iBlock in range(nBlocks):
        for iTrial in range(nTrials):
            writer.writerow({'Block': iBlock, 'Trial':iTrial, 'SubjectResponse': responseData[iBlock]['SubjectResponse'][iTrial], 'ResponseTime': responseData[iBlock]['ResponseTime'][iTrial]})

#Save JSON exercises
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os

filename = 'Subject1Session1Nov212022.json'

main_dir = os.getcwd()
data_dir = os.path.join(main_dir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
fullAddress = os.path.join(data_dir, filename)
print(fullAddress)

nBlocks = 2
nTrials = 4

rt_clock = core.Clock() 
cd_timer = core.CountdownTimer() 

sub_resp = [[-1]*nTrials]*nBlocks
sub_acc = [[-1]*nTrials]*nBlocks
prob = [[-1]*nTrials]*nBlocks
corr_resp = [[-1]*nTrials]*nBlocks
resp_time = [[-1]*nTrials]*nBlocks
blocks = [[0,0,0,0,], [1,1,1,1]]
trials = [[0,1,2,3], [0,1,2,3]]

data_as_list = [prob, corr_resp, sub_resp, sub_acc, resp_time]
print(data_as_list)

with open(fullAddress, 'w') as sub_data:
    fieldnames = ['block', 'trial', 'problem','corr_resp','sub_resp','sub_acc', 'resp_time']
    data_writer = csv.DictWriter(sub_data, fieldnames=fieldnames)
    data_writer.writeheader()
    
    for block in range(nBlocks):
        data_as_dict = []
        for a,b,c,d,e,f,g in zip(blocks[block], trials[block], prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
            data_as_dict.append({'block':a, 'trial':b, 'problem':c,'corr_resp':d,'sub_resp':e,'sub_acc':f, 'resp_time':g})
        print(data_as_dict)
        for iTrial in range(nTrials):
            data_writer.writerow(data_as_dict[iTrial])
            
#Read JSON exercises
#1
import pandas as pd

df = pd.read_csv('C:/Users/M/Desktop/Assignment 8/data/Subject1Session1Nov212022.csv')
print(df.to_string())

acc_trials = df.loc[df['sub_acc'] == 1].mean() 
print(acc_trials)
#2
acc_trials = df.loc[df['sub_acc'] == 1] 
print(acc_trials)
#3
acc_trials = df.loc[df['sub_resp'] != -1] 
print(acc_trials)
