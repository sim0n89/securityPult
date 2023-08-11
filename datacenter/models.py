from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(f"leaved at {self.leaved_at}" if self.leaved_at else "not leaved"),
        )


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
