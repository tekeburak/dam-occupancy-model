from datetime import datetime, timedelta

def get_date_list_for_gmt():
    date_list = []
    curr_date = datetime.utcnow().date()

    for i in range(1,8,1):
        date_list.append(curr_date + timedelta(days=i))

    return date_list