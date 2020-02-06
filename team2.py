####
# Each team's file must define four tokens:
#     team_name: Cryostheno
#     strategy_name: hopefull betray
#     strategy_description: Only betray when the opponent backstabs you
#     move: A function that returns 'c' or 'b'
####

team_name = 'Drayzdin' # Only 10 chars displayed.
strategy_name = 'Simple Perception'
strategy_description = 'Collude or Betray based off of how it went with pevious rounds'
points = []
my_history2 = []
their_history2 = []

def move(my_history, their_history, my_score, their_score):
    global points
    global my_history2
    global their_history2
    their_history2 += their_history
    my_history2 += my_history
    while len(my_history2) > 2:
        if my_history2[-1] == their_history2[-1] and my_history2[-1] == 'c':
            points += [0]
        if my_history2[-1] == their_history2[-1] and my_history2[-1] == 'b':
            points += [-250]
        if my_history2[-1] != their_history2[-1] and my_history2[-1] == 'c':
            points += [-500]
        if my_history2[-1] != their_history2[-1] and my_history2[-1] == 'b':
            points += [100]
        if len(points) >= 2: 
            if points[-1] == points[-2]:
                return their_history2[-2]
            if points[-1] < points[-2]:
                return their_history2[-1]
            if points[-1] > points[-2]:
                return my_history2[-1]
            else:
                return 'b'
    else:
        return 'b'
   
   
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print('Test Passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
