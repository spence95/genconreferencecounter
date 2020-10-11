import requests
from bs4 import BeautifulSoup

from references import References
from talk_reference import TalkReference

# collect links to individual talks

talk_urls = [
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/11nelson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/13whiting?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/14craig?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/15cook?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/16rasband?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/17oaks?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/12bednar?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/22christofferson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/23lund?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/24gong?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/25waddell?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/26holland?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/27jackson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/27jackson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/28uchtdorf?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/31eubank?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/32craven?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/34franco?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/34franco?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/35eyring?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/36oaks?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/37nelson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/41ballard?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/42harkness?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/43soares?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/44godoy?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/44godoy?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/45andersen?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/46nelson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/51eyring?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/52jaggi?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/52jaggi?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/53stevenson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/54camargo?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/55renlund?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/56johnson?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/57holland?lang=eng",
    "https://www.churchofjesuschrist.org/study/general-conference/2020/10/58nelson?lang=eng"
    ]

# For each talk
talk_references = []
for talk_url in talk_urls:

    page = requests.get(talk_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get speaker name
    raw_speaker_name = soup.findAll("p", {"class":"author-name"})[0].text

    # Remove the "By " that starts the string
    speaker_name = raw_speaker_name[3:]
    speaker_name = speaker_name.replace('\xa0', ' ')

    # Get references
    note_counter = 1
    last_note = False
    while last_note == False:
        id_name = 'note{0}_p1'.format(str(note_counter))
        results = soup.find(id=id_name)
        if(results != None):
            get_a = results.find('a')
            if(get_a):
                text = get_a.text
                talk_reference = TalkReference(speaker_name, text.replace(',', ' '))
                talk_references.append(talk_reference)
            note_counter += 1
        else:
            last_note = True
    print("talk processed")
    
references = References(talk_references)
references.total()
references.output()