from .models import Patent
from .models import db
import string

def create_patent():
    abc = list(string.ascii_lowercase)
    patents = []
    rank = [*range(0, 1000, 1)]
    for x in abc:
        if x != 'ñ':
            for y in rank:
                prefix = str(x) * 4
                suffix = y
                if len(str(y)) == 2:
                    suffix = '0' + str(y)
                if len(str(y)) == 1:
                    suffix = '00' + str(y)
                pat = str(prefix) + str(suffix)
                patent = Patent(patent=pat.upper())
                patents.append(patent) 
    db.session.bulk_save_objects(patents)
    db.session.commit()