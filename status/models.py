from django.db import models

class Crew(models.Model):
    truck_identifier = models.IntegerField()
    truck_level = models.CharField(max_length=20)
    crew_member_alpha = models.CharField(max_length=64)
    crew_member_beta = models.CharField(max_length=64)
    crew_member_charlie = models.CharField(max_length=64)
    crew_member_delta = models.CharField(max_length=64)
    crew_member_echo = models.CharField(max_length=64)
    crew_member_foxtrot = models.CharField(max_length=64)
    crew_member_golf = models.CharField(max_length=64)
    crew_expiration = models.DateTimeField()