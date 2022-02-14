from xml.dom.minidom import parse
import os

directory = "./"
for filename in os.listdir(directory):
    if filename.endswith(".xml"): 
        print(filename)
        doc = parse(os.path.join(directory, filename))

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

            parts_list.append(part_events)

        textfilename = 'OUT - MensuralMEI2TextTokens/' + filename[:-4] + '.txt'
        with open (textfilename, 'w') as f:
            i = 1
            for part in parts_list:
                f.write('NEWPART_' + str(i) + '\n')
                for event in part:
                    f.write(event)
                    f.write('\n')
                i = i + 1
                f.write('\n')