from datetime import datetime

today = datetime.today().day
condition = 'estupendo'


if today == 'Saturday':
    print('Party!')
if today == 'Sunday':
    if condition == 'Headache':
        print('Recover. Then rest')
    else:
        print('Rest')
else:
    print('Work, work, work.')


