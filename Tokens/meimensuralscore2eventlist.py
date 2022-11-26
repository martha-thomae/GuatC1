from xml.dom.minidom import parse
import os
import argparse

#directory = "MuRET_&_MPeditor/"
def main(in_directory, out_directory):
    for filename in os.listdir(in_directory):
        if 'MENSURAL_SCORE' in filename:
            print(filename)
            doc = parse(os.path.join(in_directory, filename))

            noteshapes = {'maxima': 'Max', 'longa': 'L', 'brevis': 'B', 'semibrevis': 'Sb', 'minima': 'M', 
            'semiminima': 'sm', 'fusa': 'F', 'semifusa': 'sf'}

            staves = doc.getElementsByTagName('staff')
            parts_list = []
            for staff in staves:
                part_events = []
                layer = staff.getElementsByTagName('layer')[0]
                for element in layer.childNodes:
                    if (element.nodeName == 'rest'):
                        abspitch = 'R'
                        
                        dur = element.getAttribute('dur')
                        nshape = noteshapes[dur]
                        if (element.nextSibling.nextSibling.nodeName == 'dot'):
                            nshape = nshape + '-dot'

                        noteval = abspitch + '_' + nshape
                        part_events.append(noteval)

                    elif (element.nodeName == 'note'):
                        pname = element.getAttribute('pname')
                        octave = element.getAttribute('oct')
                        abspitch = pname.upper() + octave
                        
                        dur = element.getAttribute('dur')
                        nshape = noteshapes[dur]
                        if (element.nextSibling.nextSibling):
                            if (element.nextSibling.nextSibling.nodeName == 'dot'):
                                nshape = nshape + '-dot'
                        
                        noteval = abspitch + '_' + nshape
                        part_events.append(noteval)

                    elif (element.nodeName == 'ligature'):
                        for child in element.childNodes:
                            if (child.nodeName == 'rest'):
                                abspitch = 'R'

                                dur = child.getAttribute('dur')
                                nshape = noteshapes[dur]
                                if (element.nextSibling.nextSibling.nodeName == 'dot'):
                                    nshape = nshape + '-dot'

                                noteval = abspitch + '_' + nshape
                                part_events.append(noteval)

                            elif (child.nodeName == 'note'):
                                pname = child.getAttribute('pname')
                                octave = child.getAttribute('oct')
                                abspitch = pname.upper() + octave

                                dur = child.getAttribute('dur')
                                nshape = noteshapes[dur]
                                if (element.nextSibling.nextSibling.nodeName == 'dot'):
                                    nshape = nshape + '-dot'

                                noteval = abspitch + '_' + nshape
                                part_events.append(noteval)

                    elif (element.nodeName == 'choice'):
                        for child in element.childNodes:
                            if (child.nodeName == 'corr'):
                                for grandchild in child.childNodes:
                                    if (grandchild.nodeName == 'rest'):
                                        abspitch = 'R'

                                        dur = grandchild.getAttribute('dur')
                                        nshape = noteshapes[dur]
                                        if (element.nextSibling.nextSibling.nodeName == 'dot'):
                                            nshape = nshape + '-dot'

                                        noteval = abspitch + '_' + nshape
                                        part_events.append(noteval)

                                    elif (grandchild.nodeName == 'note'):
                                        pname = grandchild.getAttribute('pname')
                                        octave = grandchild.getAttribute('oct')
                                        abspitch = pname.upper() + octave

                                        dur = grandchild.getAttribute('dur')
                                        nshape = noteshapes[dur]
                                        if (element.nextSibling.nextSibling):
                                            if (element.nextSibling.nextSibling.nodeName == 'dot'):
                                                nshape = nshape + '-dot'

                                        noteval = abspitch + '_' + nshape
                                        part_events.append(noteval)

                parts_list.append(part_events)

            textfilename = out_directory + filename[:-4] + '.txt'
            with open (textfilename, 'w') as f:
                i = 1
                for part in parts_list:
                    f.write('NEWPART_' + str(i) + '\n')
                    for event in part:
                        f.write(event)
                        f.write('\n')
                    i = i + 1
                    f.write('\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help="Directory with MP Editor's MEI files to be tokenized")
    parser.add_argument('mass_number', help="Two-digit number indicating the number of the piece in the manuscript (e.g., 06 or 11)")
    args = parser.parse_args()
    output_dir = args.mass_number + "/tokens_mpeditorial-scores/"
    main(args.input_dir, output_dir)