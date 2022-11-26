from xml.dom.minidom import parse
import os
import argparse

#directory = "_cpdl-music-xmls/"
def main(directory, mass_no, reduction):
    for filename in os.listdir(directory):
        if filename.endswith(".musicxml"): 
            print(filename)
            doc = parse(os.path.join(directory, filename))

            parts = doc.getElementsByTagName('part')
            parts_list = []
            for part in parts:
                part_events = []
                measures = part.getElementsByTagName('measure')
                for measure in measures:
                    notes = measure.getElementsByTagName('note')
                    for note in notes:
                        pitch = note.getElementsByTagName('pitch')
                        rest = note.getElementsByTagName('rest')
                        if pitch != []:
                            pname = pitch[0].getElementsByTagName('step')[0]
                            octave = pitch[0].getElementsByTagName('octave')[0]
                            abspitch = pname.firstChild.nodeValue + octave.firstChild.nodeValue
                        elif rest != []:
                            abspitch = 'R'

                        dur_16th = note.getElementsByTagName('duration')[0].firstChild.nodeValue
                        # note.getElementsByTagName('type')
                        try:
                            notation = note.getElementsByTagName('notations')[0]
                            tied = notation.getElementsByTagName('tied')[0]
                            type_of_tie = tied.getAttribute('type')
                            if type_of_tie == 'start':
                                tied_to_next = True
                            elif type_of_tie == 'stop':
                                tied_to_next = False
                        except:
                            tied_to_next = False

                        # append the event as a triplet in the part_events list
                        part_events.append([abspitch, dur_16th, tied_to_next])
                parts_list.append(part_events)

            noteshapes_opt2 = {64: 'Max', 32: 'L', 16: 'B', 8: 'Sb', 4: 'M', 2: 'sm', 1: 'F', 
            96: 'Max-dot', 48: 'L-dot', 24: 'B-dot', 12:'Sb-dot', 6: 'M-dot', 3: 'sm-dot'}
            noteshapes_opt1 = {32: 'Max', 16: 'L', 8: 'B', 4: 'Sb', 2: 'M', 1: 'sm', 
            48: 'Max-dot', 24: 'L-dot', 12:'B-dot', 6: 'Sb-dot', 3: 'M-dot'}
            noteshapes_opt3 = {96: 'Max', 48: 'L', 24: 'B', 12: 'Sb', 6: 'M', 3: 'sm', 2: 'sm-TRIPLETS',
            144: 'Max-dot', 72: 'L-dot', 36: 'B-dot', 18: 'Sb-dot', 9: 'M-dot'}

            # Depending on the option
            if (reduction == '3'):
                noteshapes = noteshapes_opt3
                textfilename = mass_no + '/tokens_cpdl/fusa_3beats/'
            elif (reduction == '2'):
                noteshapes = noteshapes_opt2
                textfilename = mass_no + '/tokens_cpdl/fusa_2beats/'
            elif (reduction == '1'):
                noteshapes = noteshapes_opt1
                textfilename = mass_no + '/tokens_cpdl/fusa_1beats/'

            parts_list2 = []
            for part_events in parts_list:
                try:
                    # Start the veriables for processing one part
                    dur_16th = 0
                    part_events2 = []
                    for event in part_events:
                        if event[2] == True:
                            dur_16th = int(event[1])
                        else:
                            dur_16th = dur_16th + int(event[1])
                            nshape = noteshapes[dur_16th]
                            noteval = event[0] + '_' + nshape
                            part_events2.append(noteval)
                            # Restart dur_16 variable
                            dur_16th = 0
                    parts_list2.append(part_events2)
                except KeyError as err:
                    parts_list2 = []
                    print(err)
                    break

            textfilename = textfilename + filename[:-9] + '.txt'
            with open (textfilename, 'w') as f:
                i = 1
                for part in parts_list2:
                    f.write('NEWPART_' + str(i) + '\n')
                    for event in part:
                        f.write(event)
                        f.write('\n')
                    i = i + 1
                    f.write('\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mass_number', help="Two-digit number indicating the number of the piece in the manuscript (e.g., 06 or 11)")
    parser.add_argument('-r', choices=['1', '2', '3'], help="reduction ratio")
    args = parser.parse_args()
    directory = args.mass_number + "/_cpdl-music-xmls/"
    main(directory, args.mass_number, args.r)
