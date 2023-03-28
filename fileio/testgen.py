from pathlib import Path
import random

# Most spoken non-official language in each prov./terr.
capitals = {'New Brunswick': 'Arabic',
            'Newfoundland' : 'Innu',
            'Nunavut': 'Inuktitut',
            'Nova Scotia': 'Chinese',
            'Ontario': 'Chinese',
            'Prince Edward Island': 'Chinese',
            'Alberta': 'Punjabi',
            'British Columbia': 'Punjabi',
            'Quebec': 'Spanish',
            'Manitoba': 'Tagalog',
            'Saskatchewan': 'Tagalog',
            'Yukon': 'Tagalog',
            'Northwest Territories': 'Tlicho'}

quizzesFolder = Path(Path.cwd() / 'quizzes')

if not quizzesFolder.exists():
    quizzesFolder.mkdir()

# Create 20 different quizzes.
for i in range(1, 21):
    quizFile = open('quizzes/quiz' + str(i), 'w')
    quizFile.write('Most Spoken Unofficial Language Quiz\nVersion ' + str(i)+'\n')

    keyFile = open('quizzes/key' + str(i), 'w')
    keyFile.write('ANSWER KEY\nMost Spoken Unofficial Language Quiz\nVersion ' + str(i)+'\n')

    randCapitals = list(capitals.keys())
    random.shuffle(randCapitals)

    for j in range(len(randCapitals)):
        quizFile.write(str(j+1) + '. ' + randCapitals[j] + '?\n')
        keyFile.write(str(j+1) + '. ' + capitals[randCapitals[j]] + '\n')
    quizFile.close()
    keyFile.close()


