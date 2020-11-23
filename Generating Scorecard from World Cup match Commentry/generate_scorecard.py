import re
class Batsman:
    def __init__(self, names , runs, out_type, balls, mins, nof, nos, sr):
        self.names = names
        self.runs = runs
        self.out_type = out_type
        self.balls = balls
        self.mins = mins
        self.nof = nof
        self.nos = nos
        self.sr = sr

class Bowler:
    def __init__(self, names, balls, overs, m_overs, runs, wickets, econ, noz, nof, nos, wides, nb):
        self.names = names
        self.balls = balls
        self.overs = overs
        self.m_over = m_overs
        self.runs = runs
        self.wickets = wickets
        self.econ = econ
        self.noz = noz
        self.nof = nof
        self.nos = nos
        self.wides = wides
        self.nb = nb

inpt_file_fixs_arr = ['4143', '4144', '4145', '4146', '4147', '4148', '4149', '4150', '4151', '4152', '4153', '4154',
                      '4155', '4157', '4158', '4159', '4160', '4161', '4162', '4163', '4165', '4166', '4168',
                      '4169', '4170', '4171', '4172', '4173', '4174', '4176', '4177', '4178', '4179', '4180', '4182',
                      '4183', '4184', '4186', '4187', '4190', '4191', '4192', '4152a', '4156a', '4157a']

ext_over = re.compile('^\d+\.\d+$')
extras = [0, 0, 0, 0]
total = 0
maiden = []
fallOfWickets = []

def printScoreCard(write_file, batsman, bowler, extras, total, fow):
    indices = list(range(len(batsman.names)))
    indices.sort(reverse=True)
    batsman_space_adjust_1 = max(len(name) for name in batsman.names) + 3
    batsman_space_adjust_2 = max(len(out_type) for out_type in batsman.out_type) + 3
    space = 8
    print("BATTING".ljust(batsman_space_adjust_1 + batsman_space_adjust_2, ' '), end='', file=write_file)
    print("R".ljust(space, ' ') + "B".ljust(space, ' ') + "M".ljust(space, ' ') + "4s".ljust(space, ' ')
          + "6s".ljust(space, ' ') + "SR".ljust(space, ' '), file=write_file)
    for index in indices:
        print(batsman.names[index].ljust(batsman_space_adjust_1, ' '), end='',file=write_file)
        print(batsman.out_type[index].ljust(batsman_space_adjust_2, ' '), end='',file=write_file)
        print(str(batsman.runs[index]).ljust(space, ' ') + str(batsman.balls[index]).ljust(space, ' ')
              + str(batsman.mins[index]).ljust(space, ' ') + str(batsman.nof[index]).ljust(space, ' ')
              + str(batsman.nos[index]).ljust(space, ' ') + str(batsman.sr[index]).ljust(space, ' '), end='\n',file=write_file)
    if(extras[0] == 0):
        str_b = ''
    else:
        str_b = 'b ' + str(extras[0]) + ', '
    if(extras[1] == 0):
        str_lb = ''
    else:
        str_lb = 'lb ' + str(extras[1]) + ', '
    if (extras[2] == 0):
        str_nb = ''
    else:
        str_nb = 'nb ' + str(extras[2]) + ', '
    if (extras[3] == 0):
        str_w = ''
    else:
        str_w = 'w ' + str(extras[3])
    str_extras = str(sum(extras)) + " (" + str_b + str_lb + str_nb + str_w + ')'
    print("\nExtras".ljust(batsman_space_adjust_1+batsman_space_adjust_2) + str_extras, file=write_file)
    over = str(int(sum(bowler.balls) / 6)) + '.' + str(sum(bowler.balls) % 6)
    rr = total/float(over)
    print("Total".ljust(batsman_space_adjust_1+batsman_space_adjust_2) + str(total) + '/' + str(sum(bowler.wickets))
          + ' (' + over + ' Overs, RR:' + str(float("{0:.2f}".format(rr))) + ')', file=write_file)
    print("Fall of Wickets: ", end='', file=write_file)
    for fallOfWickets in reversed(fow):
        print(fallOfWickets + ', ',end='', file=write_file)
    print('\n\n', file=write_file)
    bowler_space_adjust = max(len(name) for name in bowler.names) + 3
    print("BOWLING".ljust(bowler_space_adjust, ' '), end='', file=write_file)
    print("O".ljust(space, ' ') + "M".ljust(space, ' ') + "R".ljust(space, ' ') + "W".ljust(space, ' ')
          + "ECON".ljust(space, ' ') + "0s".ljust(space, ' ') + "4s".ljust(space, ' ') + "6s".ljust(space, ' ')
          + "WD".ljust(space, ' ') + "NB".ljust(space, ' '), file=write_file)
    indices = list(range(len(bowler.names)))
    indices.sort(reverse=True)
    for index in indices:
        print(bowler.names[index].ljust(bowler_space_adjust, ' '), end='',file=write_file)
        print(str(bowler.overs[index]).ljust(space, ' ') + str(bowler.m_over[index]).ljust(space, ' ')
              + str(bowler.runs[index]).ljust(space, ' ') + str(bowler.wickets[index]).ljust(space, ' ')
              + str(bowler.econ[index]).ljust(space, ' ') + str(bowler.noz[index]).ljust(space, ' ')
              + str(bowler.nof[index]).ljust(space, ' ') + str(bowler.nos[index]).ljust(space, ' ')
              + str(bowler.wides[index]).ljust(space, ' ') + str(bowler.nb[index]).ljust(space, ' '), end='\n', file=write_file)
    print('\n\n', file=write_file)

for inpt_file_fixs in inpt_file_fixs_arr:
    if inpt_file_fixs[-1] == 'a':
        score_card_filename = '194161002-' + inpt_file_fixs + '-scorecard-computed.txt'
        write_file = open(score_card_filename, "w")
        print("Abandoned Match",file=write_file)
    else:
        current_commentry_filename = '194161002-' + inpt_file_fixs + '-commentary.txt'
        score_card_filename = '194161002-' + inpt_file_fixs + '-scorecard-computed.txt'
        commentry = open(current_commentry_filename, "r")
        write_file = open(score_card_filename, "w")
        commentry_lines = commentry.read().splitlines()
        batsman = Batsman([], [], [], [], [], [], [], [])
        bowler = Bowler([], [], [], [], [], [], [], [], [], [], [], [])
        for line_no, line_txt in enumerate(commentry_lines,1):
            flag_run_out = 0
            if line_txt[:1] == '#' and line_txt[-1:] == '#':
                total = 0
                for ind, bm in enumerate(batsman.names):
                    temp_sr = (batsman.runs[ind] / batsman.balls[ind]) * 100
                    batsman.sr[ind] = float("{0:.2f}".format(temp_sr))
                    total += batsman.runs[ind]
                total += sum(extras)
                # Computing Number of Overs and Economy from balls bowled by bowler for Innings 2
                for ind, balls in enumerate(bowler.balls):
                    bowler.overs[ind] = str(int(balls / 6)) + '.' + str(balls % 6)
                    denominator = int(float(bowler.overs[ind])) + (
                                ((float(bowler.overs[ind]) - int(float(bowler.overs[ind]))) * 10) / 6)
                    bowler.econ[ind] = float("{0:.2f}".format(bowler.runs[ind] / denominator))
                batsman_innings_2 = batsman
                bowler_innings_2 = bowler
                extras_innings_2 = extras
                total_innings_2 = total
                fallOfWickets_innings_2 = fallOfWickets
                #Resetting All Values for second innings
                extras = [0, 0, 0, 0]
                fallOfWickets = []
                batsman = Batsman([], [], [], [], [], [], [], [])
                bowler = Bowler([], [], [], [], [], [], [], [], [], [], [], [])
            if ext_over.match(line_txt):
                ballno = commentry_lines[line_no-1]
                reaction = commentry_lines[line_no]
                player_details = commentry_lines[line_no+1]
                pos_to = ballno.find('.')
                over = int(ballno[:pos_to])
                pos_to = player_details.find(' to ')
                pos_comma = player_details.find(',')
                bowler_name = player_details[:pos_to]
                batsman_name = player_details[pos_to+4:pos_comma]
                if(batsman_name not in batsman.names):
                    batsman.names.append(batsman_name)
                    batsman.runs.append(0)
                    batsman.out_type.append(' not out ')
                    batsman.balls.append(0)
                    batsman.mins.append(0)
                    batsman.nof.append(0)
                    batsman.nos.append(0)
                    batsman.sr.append(0)
                if(bowler_name not in bowler.names):
                    bowler.names.append(bowler_name)
                    bowler.balls.append(0)
                    bowler.runs.append(0)
                    bowler.wides.append(0)
                    bowler.wickets.append(0)
                    bowler.overs.append('')
                    bowler.m_over.append(0)
                    bowler.noz.append(0)
                    bowler.nof.append(0)
                    bowler.nos.append(0)
                    bowler.econ.append(0)
                    bowler.nb.append(0)
                bowler_index = bowler.names.index(bowler_name)
                batsman_index = batsman.names.index(batsman_name)
                if int(ballno[-1]) == 1 and reaction == '0':
                    maiden.append(over)
                if len(maiden) == 6:
                    bowler.m_over[bowler_index] += 1
                if int(ballno[-1] == 1):
                    maiden = []
                if reaction.isdigit():
                    batsman.balls[batsman_index] += 1
                    bowler.balls[bowler_index] += 1
                    if reaction == '0' and int(ballno[-1]) != 1:
                        bowler.noz[bowler_index] +=1
                        maiden.append(over)
                    elif reaction == '1':
                        batsman.runs[batsman_index] += 1
                        bowler.runs[bowler_index] += 1
                    elif reaction == '2':
                        batsman.runs[batsman_index] += 2
                        bowler.runs[bowler_index] += 2
                    elif reaction == '3':
                        batsman.runs[batsman_index] += 3
                        bowler.runs[bowler_index] += 3
                    elif reaction == '4':
                        batsman.runs[batsman_index] += 4
                        batsman.nof[batsman_index] += 1
                        bowler.runs[bowler_index] += 4
                        bowler.nof[bowler_index] += 1
                    elif reaction == '5':
                        batsman.runs[batsman_index] += 5
                        bowler.runs[bowler_index] += 5
                    elif reaction == '6':
                        batsman.runs[batsman_index] += 6
                        batsman.nos[batsman_index] += 1
                        bowler.runs[bowler_index] += 6
                        bowler.nos[bowler_index] += 1
                elif reaction == 'W':
                    str_wicket = '(' + batsman.names[batsman_index] + ', ' + ballno + ' ov' + ')'
                    fallOfWickets.append(str_wicket)
                    bowler.wickets[bowler_index] += 1
                    batsman.balls[batsman_index] += 1
                    bowler.balls[bowler_index] += 1
                    index_from = 0
                    dismissal_line = commentry_lines[line_no+2]
                    if dismissal_line.find(' c & b ') != -1:
                        index_from = dismissal_line.find(' c & b ')
                    elif dismissal_line.find(' lbw ') != -1:
                        index_from = dismissal_line.find(' lbw ')
                    elif dismissal_line.find(' c ') != -1:
                        index_from = dismissal_line.find(' c ')
                    elif dismissal_line.find(' b ') != -1:
                        index_from = dismissal_line.find(' b ')
                    elif dismissal_line.find(' run out ') != -1:
                        index_from = dismissal_line.find(' run out ')
                        flag_run_out = 1
                    for index_to, character in enumerate(dismissal_line):
                        if character.isdigit():
                            batsman.out_type[batsman_index] = dismissal_line[index_from+1:index_to]
                            break
                    for index_from, character in enumerate(dismissal_line):
                        if character == '(':
                            break
                    if flag_run_out == 0:
                        index_to = dismissal_line.find('m',index_from)
                        batsman.mins[batsman_index] = dismissal_line[index_from+1:index_to]
                    else:
                        index_from = dismissal_line.find('(',index_from+1)
                        index_to = dismissal_line.find('m',index_from)
                        batsman.mins[batsman_index] = dismissal_line[index_from + 1:index_to]
                elif reaction[-1:] == 'w':
                    extras[3] += int(reaction[:1])
                    bowler.wides[bowler_index] += int(reaction[:1])
                elif reaction[-2:] == 'lb':
                    extras[1] += int(reaction[:1])
                    batsman.balls[batsman_index] += 1
                    bowler.balls[bowler_index] += 1
                elif reaction[-2:] == 'nb':
                    extras[2] += int(reaction[:1])
                    bowler.nb[bowler_index] += int(reaction[:1])
                elif reaction[-1:] == 'b':
                    extras[0] += int(reaction[:1])
                    batsman.balls[batsman_index] += 1
                    bowler.balls[bowler_index] += 1
        #Computing Total for Innings 1
        total = 0
        for ind, bm in enumerate(batsman.names):
            temp_sr = (batsman.runs[ind] / batsman.balls[ind])*100
            batsman.sr[ind] = float("{0:.2f}".format(temp_sr))
            total += batsman.runs[ind]
        total += sum(extras)
        #Computing Number of Overs and Economy from balls bowled by bowler for Innings 1
        for ind, balls in enumerate(bowler.balls):
            bowler.overs[ind] = str(int(balls/6)) + '.' + str(balls%6)
            denominator = int(float(bowler.overs[ind])) + (((float(bowler.overs[ind]) - int(float(bowler.overs[ind])))*10)/6)
            bowler.econ[ind] = float("{0:.2f}".format(bowler.runs[ind]/denominator))
        print("Innings 1",file=write_file)
        printScoreCard(write_file, batsman, bowler, extras, total, fallOfWickets)
        print("Innings 2",file=write_file)
        printScoreCard(write_file, batsman_innings_2, bowler_innings_2, extras_innings_2, total_innings_2, fallOfWickets_innings_2)
        write_file.close()