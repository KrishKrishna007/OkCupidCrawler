'''
Script that prints information for every question answered by a profile
from quickmatch that contains the text "marijuana"(probably not a whole
lot, but you get the idea).
'''

from pyokc import pyokc

u = pyokc.User()
p = u.quickmatch()
print('Questions for {0}'.format(p.name))
print('----------')
p.update_questions()
for q in p.questions:
    if 'marijuana' in q.text.lower():
        print(q.text)
        print(q.user_answer)
        if len(q.explanation):
            print(q.explanation)
        print('')