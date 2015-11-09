import psychopy
from psychopy import core, visual
import subject
import shuffler

numbers = range(1, 10)

#lyons used 18 trials for each quantity

formats = ['symbolic', 'nonsymbolic', 'text', 'audio', 'addition', 'subtraction']
operations = ['comparison', 'addition', 'subtraction']
cue = [True, False] #provide the person with a cue to indicate what operation they'll be performing

stimulus_1_time = .5
stimulus_2_time = .5
delay_times = [1.5, 2.5, 3.5, 4.5, 5.5]

ISI = [1.9, 2.7, 3.6, 4.5, 5.4, 6.3, 7.2, 8.1]
