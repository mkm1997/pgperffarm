
# -*- coding: utf-8 -*-
import django_filters
from django.db.models import Q

from models import UserMachine
from test_records.models import TestRecord


class MachineRecordListFilter(django_filters.rest_framework.FilterSet):
    """
    TestRecordListFilter
    """
    branch__id = django_filters.NumberFilter()
    test_machine__machine_sn = django_filters.CharFilter()

    class Meta:
        model = TestRecord
        fields = ['branch__id', 'test_machine__machine_sn']


class UserMachineListFilter(django_filters.rest_framework.FilterSet):
    """
    UserMachineListFilter
    """

    # machine_owner__username = django_filters.CharFilter()

    class Meta:
        model = UserMachine
        fields = ['machine_owner__username', ]