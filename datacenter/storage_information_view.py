from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration
from django.utils.timezone import localtime


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)
    for visit in active_visits:
        duration = format_duration(get_duration(visit))
        non_closed_visits = [
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": localtime(visit.entered_at),
                "duration": duration,
            }
        ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, "storage_information.html", context)
