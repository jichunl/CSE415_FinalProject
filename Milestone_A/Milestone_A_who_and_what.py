#!/usr/bin/python3
'''Milestone_A_who_and_what.py
This runnable file will provide a representation of
answers to key questions about your project in CSE 415.

'''

# DO NOT EDIT THE BOILERPLATE PART OF THIS FILE HERE:

CATEGORIES=['Baroque Chess Agent','Feature-Based Reinforcement Learning for the Rubik Cube Puzzle',\
  'Hidden Markov Models: Algorithms and Applications']

class Partner():
  def __init__(self, lastname, firstname, uwnetid):
    self.uwnetid=uwnetid
    self.lastname=lastname
    self.firstname=firstname

  def __lt__(self, other):
    return (self.lastname+","+self.firstname).__lt__(other.lastname+","+other.firstname)

  def __str__(self):
    return self.lastname+", "+self.firstname+" ("+self.uwnetid+")"

class Who_and_what():
  def __init__(self, team, option, title, approach, workload_distribution, references):
    self.team=team
    self.option=option
    self.title=title
    self.approach = approach
    self.workload_distribution = workload_distribution
    self.references = references

  def report(self):
    rpt = 80*"#"+"\n"
    rpt += '''The Who and What for This Submission

Project in CSE 415, University of Washington, Winter, 2019
Milestone A

Team: 
'''
    team_sorted = sorted(self.team)
    # Note that the partner whose name comes first alphabetically
    # must do the turn-in.
    # The other partner(s) should NOT turn anything in.
    rpt += "    "+ str(team_sorted[0])+" (the partner who must turn in all files in Catalyst)\n"
    for p in team_sorted[1:]:
      rpt += "    "+str(p) + " (partner who should NOT turn anything in)\n\n"

    rpt += "Option: "+str(self.option)+"\n\n"
    rpt += "Title: "+self.title + "\n\n"
    rpt += "Approach: "+self.approach + "\n\n"
    rpt += "Workload Distribution: "+self.workload_distribution+"\n\n"
    rpt += "References: \n"
    for i in range(len(self.references)):
      rpt += "  Ref. "+str(i+1)+": "+self.references[i] + "\n"

    rpt += "\n\nThe information here indicates that the following file will need\n"+\
     "to be submitted (in addition to code and possible data files):\n"
    rpt += "    "+\
     {'1':"Baroque_Chess_Agent_Report",'2':"Rubik_Cube_Solver_Report",\
      '3':"Hidden_Markov_Models_Report"}\
        [self.option]+".pdf\n"

    rpt += "\n"+80*"#"+"\n"
    return rpt

# END OF BOILERPLATE.

# Change the following to represent your own information:

peter = Partner("Li", "Jichun", "jichunli")
jason = Partner("Li", "Xuedeliang", "xl74")
team = [peter, jason]

OPTION = '3'
# Legal options are 1, 2, and 3.

title = "Hidden Markov Model Applications"

approach = '''We plan to search for data sets which are related to location tracking and 
to generate our own data set of gambling cheating. The first case will be an 
application of Forward Algorithm and the second be the Viterbi Algorithm. 
Based on the data sets, the algorithms could be implemented for demonstration. '''

workload_distribution = '''For the project of Hidden Markov Model Application, 
    there are total two algorithms needed to be implemented. One is the Forward
    Algorithm, which takes a sequence of observations and uses that information
    to repeatedly estimate the a-posteriori probability distribution over the 
    set of possible states. The other is Viterbi algorithm, which take a 
    sequence of observations and use it to determine the most likely state 
    sequence. Each one of us will focusing on implementation of one algorithm.
    The two applications of Hidden Markov Model we would like to explore are 
    gambling and location tracking. Both of us would involve in application of
    HMM.
    '''

reference1 = '''Predicting the Viterbi Score Distribution for a Hidden Markov 
    Model and Application to Speech Recognition;
    URL: https://ieeexplore-ieee-org.offcampus.lib.washington.edu/document/4041064'''

reference2 = '''"Automatic Determination of Piano Fingering Based on Hidden Markov Models;
    http://hil.t.u-tokyo.ac.jp/research/introduction/PianoFingering/english.html'''

our_submission = Who_and_what([peter, jason], OPTION, title, approach, workload_distribution, [reference1, reference2])

# You can run this file from the command line by typing:
# python3 who_and_what.py

# Running this file by itself should produce a report that seems correct to you.
if __name__ == '__main__':
  print(our_submission.report())
