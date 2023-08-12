from django.utils.timezone import localtime


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    time_in = localtime() - entered_at
    return time_in


def format_duration(duration):
    seconds = duration.seconds
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    formated_duration = f"{minutes}:{seconds}"
    return formated_duration


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    seconds = duration.seconds
    duration_minutes = (seconds % 3600) // 60
    if duration_minutes > minutes:
        return True
    return False