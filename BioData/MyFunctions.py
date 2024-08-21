from datetime import datetime

systolic_list = []
diastolic_list = []
month0 = []

def MemberMoM(member_bp,the_month):

    # MOM BLOOD PRESSURE
    for bp in member_bp:

        reading_date = datetime.strptime(bp.readingDate, "%a %b %d %Y").date()
        # print(reading_date)

        #check date are within a month
        if reading_date.month == the_month:
            systolic_list.append(bp.systolic)
            diastolic_list.append(bp.diastolic)
        
    avg_systolic = sum(systolic_list) / len(systolic_list)
    avg_diastolic = sum(diastolic_list) / len(diastolic_list) 

    return avg_systolic, avg_diastolic, the_month