from django.db import models


class Device(models.Model):
    device_name = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.device_name


class Activity(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    speed = models.IntegerField(blank=False, null=False, default=2)

    def __str__(self) -> str:
        return self.name

class Result(models.Model):
    devicename = models.CharField(max_length=100, blank=False, null=False)
    speed = models.IntegerField(default=2, null=False, blank=False)

    def __str__(self):
        return self.devicename
