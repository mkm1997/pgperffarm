# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from models import UserMachine
from .serializer import TestRecordSerializer, TestRecordDetailSerializer, LinuxInfoSerializer, MetaInfoSerializer, \
    PGInfoSerializer, CreateTestRecordSerializer, CreateTestDateSetSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from .models import TestRecord, LinuxInfo, MetaInfo, PGInfo, TestBranch
import json


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TestRecordListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List test records
    """
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer
    pagination_class = StandardResultsSetPagination


class TestRecordDetailViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List test records
    """
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordDetailSerializer
    pagination_class = StandardResultsSetPagination


@api_view(['POST'])
def TestRecordCreate(request, format=None):
    """
    Receive data from client
    """

    # serializers = BizcircleSerializer(data=request.data)
    # if serializers.is_valid():
    #     serializers.save()
    #     return Response(serializers.data, status=status.HTTP_201_CREATED)
    data = request.data

    print type(data[0])
    json_data = json.dumps(data[0], encoding="UTF-8", ensure_ascii=False)
    json_data = json.loads(json_data, encoding="UTF-8")
    # obj = data[0].pgbench
    # jsLoads = json.loads(data[0])

    linux_data = json_data['linux']
    linuxInfo = LinuxInfoSerializer(data=linux_data)
    linuxInfoRet = None
    if linuxInfo.is_valid():
        linuxInfoRet = linuxInfo.save()

    meta_data = json_data['meta']
    metaInfo = MetaInfoSerializer(data=meta_data)
    metaInfoRet = None
    if metaInfo.is_valid():
        metaInfoRet = metaInfo.save()

    # pg_data = json_data['postgres']
    pg_data = {
        'pg_branch':1
    }
    pgInfo = PGInfoSerializer(data=pg_data)
    pgInfoRet = None
    if pgInfo.is_valid():
        pgInfoRet = pgInfo.save()

    test_record_data = {
        'pg_info': pgInfoRet.id,
        'linux_info': linuxInfoRet.id,
        'meta_info': metaInfoRet.id,
        'test_machine_id': 1,
        'test_desc': 'here is desc'
    }
    testRecord = CreateTestRecordSerializer(data=test_record_data)
    testRecordRet = None
    if testRecord.is_valid():
        testRecordRet = testRecord.save()

    ro = json_data['pgbench']['ro']
    # print(type(ro))
    for scale, dataset_list in ro.iteritems():
        print "ro[%s]=" % scale, dataset_list
        for client_num, dataset in dataset_list.iteritems():
            print dataset['std']
            test_dataset_data = {
                'test_record_id': testRecordRet.id,
                'clients': client_num,
                'scale': scale,
                'std': dataset['std'],
                'metric': dataset['metric'],
                'median': dataset['median']
                # todo status,percentage
            }
            testDateSet = CreateTestDateSetSerializer(data=test_dataset_data)
            testDateSetRet = None
            if testDateSet.is_valid():
                print 'dataset valid'
                testDateSetRet = testDateSet.save()
            else:
                print testDateSet


    msg = 'upload ok'
    return Response(msg, status=status.HTTP_200_OK)