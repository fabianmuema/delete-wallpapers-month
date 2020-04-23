import os
from datetime import datetime
from datetime import date

month = datetime.now().month
for root, dirs, files in os.walk('/home/fabian/.config/variety/Fetched', topdown=True):
    for file in files:
        stat = os.stat('/home/fabian/.config/variety/Fetched/' + file)
        file_date = date.fromtimestamp(stat.st_mtime).month
        if month != file_date:
            os.remove('/home/fabian/.config/variety/Fetched/' + file)
