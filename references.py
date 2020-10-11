import os
from talk_reference import TalkReference

class References:
    
    def __init__(self, talk_references):
        self.talk_references = talk_references
        self.totals = []

    def total(self):
        references = {talk_reference.reference for talk_reference in self.talk_references}
        print(references)

        for reference in references:
            total = {}
            total['reference'] = reference
            total['speaker_names'] = []
            total['count'] = 0
            for talk_reference in self.talk_references:
                if(talk_reference.reference == reference):
                    total['count'] += 1
                if talk_reference.reference == reference:
                    total['speaker_names'].append(talk_reference.speaker_name)
            self.totals.append(total)
    
    def output(self):
        filename = 'GenConReferenceCount.csv'

        # remove file if exists
        # try:
        #     os.remove(filename)
        # except OSError:
        #     pass

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        with open(os.path.join(__location__, filename), "w") as csv_file:
            csv_file.write('Reference, Count, Speakers')
            csv_file.write('\n')
            for total in self.totals:
                csv_file.write(total['reference'] + ',' + str(total['count']) + ',' + str(total['speaker_names']))
                csv_file.write('\n')



