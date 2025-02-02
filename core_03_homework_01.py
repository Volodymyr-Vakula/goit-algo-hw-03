from datetime import datetime

# Function to calculate time interval between current date and given date
def get_days_from_today(date: str) -> (int | None):
    """
    Calculates time interval between the current date and a given date

    Input:
    :param date: string
    
    Output:
    :return: integer or None
    """
    try:
        datetime_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        time_interval = today.toordinal() - datetime_date.toordinal()
        return time_interval
    except ValueError:
        return None
