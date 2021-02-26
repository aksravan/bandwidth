from django.shortcuts import render, redirect
from .models import Device, Activity, Result


def home(request):
    if request.method == 'POST':
        if 'btngetspeed' in request.POST:
            return redirect('result')
        if 'btnreset' in request.POST:
            return redirect('reset')

    try:
        devices = Device.objects.all()
        result = Result.objects.all()
    except:
        devices = []
        result = []

    context = {
        'devices': devices,
        'result': result
    }
    return render(request, 'bandwidthcal/home.html', context)


def device(request, device):
    try:
        dev = Device.objects.get(device_name=device)
        activity = Activity.objects.filter(device=dev)
    except:
        activity = []

    context = {
        'currdevice': device,
        'activity': activity
    }
    return render(request, 'bandwidthcal/device.html', context)


def add(request, devicename):
    if request.method == 'POST':

        speed = 0
        devicename = request.POST.get('devicename')
        devicecount = int(request.POST.get("devicecount"))
        try:
            dev = Device.objects.get(device_name=devicename)
            activity = Activity.objects.filter(device=dev)
        except:
            pass

        dct = {}
        for act in activity:
            dct[act.name] = act.speed

        if "Normal Video" in request.POST:
            speed += dct["Normal Video"]
        if "4K Video" in request.POST:
            speed += dct["4K Video"]
        if "HD Video" in request.POST:
            speed += dct["HD Video"]
        if "8K Video" in request.POST:
            speed += dct["8K Video"]
        if "Social Media" in request.POST:
            speed += dct["Social Media"]
        if "Amazon Video" in request.POST:
            speed += dct["Amazon Video"]
        if "Netflix" in request.POST:
            speed += dct["Netflix"]
        if "Other Video Apps" in request.POST:
            speed += dct["Other Video Apps"]
        if "Video Conferencing" in request.POST:
            speed += dct["Video Conferencing"]
        if "HD Video Conferencing" in request.POST:
            speed += dct["HD Video Conferencing"]
        if "Frequent Large File Download" in request.POST:
            speed += dct["Frequent Large File Download"]
        if "Google Assistant" == devicename:
            speed += 3
        if "PS5" == devicename or "PS4, XBOX" == devicename:
            speed += 5

        Result.objects.create(devicename=str(devicename),
                              speed=int(speed*devicecount))
        return redirect('/')


def result(request, r):
    res = Result.objects.all()
    speed = 0
    for re in res:
        speed += re.speed

    context = {
        'res': res,
        'speed': speed
    }
    return render(request, 'bandwidthcal/result.html', context)


def reset(request):
    #Result.objects.all().delete()
    return redirect('/')

