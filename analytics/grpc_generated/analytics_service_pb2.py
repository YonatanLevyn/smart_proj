# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61nalytics_service.proto\x12\x11\x61nalytics_service\"A\n\x0e\x41nalyticsEvent\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"*\n\x17\x45ventProcessingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"E\n\x13\x44\x61ilyMetricsRequest\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x03\x12\x15\n\rend_timestamp\x18\x02 \x01(\x03\"G\n\x14\x44\x61ilyMetricsResponse\x12/\n\x07metrics\x18\x01 \x03(\x0b\x32\x1e.analytics_service.DailyMetric\"c\n\x0b\x44\x61ilyMetric\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0ctotal_visits\x18\x02 \x01(\x05\x12\x1c\n\x14\x61vg_session_duration\x18\x03 \x01(\x02\x12\x13\n\x0b\x62ounce_rate\x18\x04 \x01(\x02\"\'\n\x14ProcessedDataRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x87\x01\n\x15ProcessedDataResponse\x12\x37\n\x0f\x64\x61ily_pageviews\x18\x01 \x03(\x0b\x32\x1e.analytics_service.DailyMetric\x12 \n\x18\x61verage_session_duration\x18\x02 \x01(\x02\x12\x13\n\x0b\x62ounce_rate\x18\x03 \x01(\x02\x32\xbc\x02\n\x10\x41nalyticsService\x12]\n\x0cProcessEvent\x12!.analytics_service.AnalyticsEvent\x1a*.analytics_service.EventProcessingResponse\x12\x62\n\x0fGetDailyMetrics\x12&.analytics_service.DailyMetricsRequest\x1a\'.analytics_service.DailyMetricsResponse\x12\x65\n\x10GetProcessedData\x12\'.analytics_service.ProcessedDataRequest\x1a(.analytics_service.ProcessedDataResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analytics_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ANALYTICSEVENT._serialized_start=46
  _ANALYTICSEVENT._serialized_end=111
  _EVENTPROCESSINGRESPONSE._serialized_start=113
  _EVENTPROCESSINGRESPONSE._serialized_end=155
  _DAILYMETRICSREQUEST._serialized_start=157
  _DAILYMETRICSREQUEST._serialized_end=226
  _DAILYMETRICSRESPONSE._serialized_start=228
  _DAILYMETRICSRESPONSE._serialized_end=299
  _DAILYMETRIC._serialized_start=301
  _DAILYMETRIC._serialized_end=400
  _PROCESSEDDATAREQUEST._serialized_start=402
  _PROCESSEDDATAREQUEST._serialized_end=441
  _PROCESSEDDATARESPONSE._serialized_start=444
  _PROCESSEDDATARESPONSE._serialized_end=579
  _ANALYTICSSERVICE._serialized_start=582
  _ANALYTICSSERVICE._serialized_end=898
# @@protoc_insertion_point(module_scope)
