"""
=======
Copyright, 2021, LogicMonitor, Inc.
This Source Code Form is subject to the terms of the 
Mozilla Public License, v. 2.0. If a copy of the MPL 
was not distributed with this file, You can obtain 
one at https://mozilla.org/MPL/2.0/.
=======
"""

# coding: utf-8

"""
    LogicMonitor API-Ingest Rest API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. API-Ingest provides the entry point in the form of public rest APIs for ingesting metrics into LogicMonitor. For using this application users have to create LMAuth token using access id and key from santaba.  # noqa: E501

    OpenAPI spec version: 3.0.0

"""

import pprint
import re  # noqa: F401

import six

from logicmonitor_data_sdk.models.map_string_string import \
  MapStringString  # noqa: F401,E501


class RestDataPointV1(object):
  """NOTE: This class is auto generated by the swagger code generator program.

  Do not edit the class manually.
  """

  """
  Attributes:
    swagger_types (dict): The key is attribute name
                          and the value is attribute type.
    attribute_map (dict): The key is attribute name
                          and the value is json key in definition.
  """
  swagger_types = {
    'data_point_aggregation_type': 'str',
    'data_point_description': 'str',
    'data_point_name': 'str',
    'data_point_type': 'str',
    'values': 'MapStringString'
  }

  attribute_map = {
    'data_point_aggregation_type': 'dataPointAggregationType',
    'data_point_description': 'dataPointDescription',
    'data_point_name': 'dataPointName',
    'data_point_type': 'dataPointType',
    'values': 'values'
  }

  def __init__(self, data_point_aggregation_type=None,
      data_point_description=None, data_point_name=None, data_point_type=None,
      values=None):  # noqa: E501
    """RestDataPointV1 - a model defined in Swagger"""  # noqa: E501

    self._data_point_aggregation_type = None
    self._data_point_description = None
    self._data_point_name = None
    self._data_point_type = None
    self._values = None
    self.discriminator = None

    if data_point_aggregation_type is not None:
      self.data_point_aggregation_type = data_point_aggregation_type
    if data_point_description is not None:
      self.data_point_description = data_point_description
    if data_point_name is not None:
      self.data_point_name = data_point_name
    if data_point_type is not None:
      self.data_point_type = data_point_type
    if values is not None:
      self.values = values

  @property
  def data_point_aggregation_type(self):
    """Gets the data_point_aggregation_type of this RestDataPointV1.  # noqa: E501


    :return: The data_point_aggregation_type of this RestDataPointV1.  # noqa: E501
    :rtype: str
    """
    return self._data_point_aggregation_type

  @data_point_aggregation_type.setter
  def data_point_aggregation_type(self, data_point_aggregation_type):
    """Sets the data_point_aggregation_type of this RestDataPointV1.


    :param data_point_aggregation_type: The data_point_aggregation_type of this RestDataPointV1.  # noqa: E501
    :type: str
    """

    self._data_point_aggregation_type = data_point_aggregation_type

  @property
  def data_point_description(self):
    """Gets the data_point_description of this RestDataPointV1.  # noqa: E501


    :return: The data_point_description of this RestDataPointV1.  # noqa: E501
    :rtype: str
    """
    return self._data_point_description

  @data_point_description.setter
  def data_point_description(self, data_point_description):
    """Sets the data_point_description of this RestDataPointV1.


    :param data_point_description: The data_point_description of this RestDataPointV1.  # noqa: E501
    :type: str
    """

    self._data_point_description = data_point_description

  @property
  def data_point_name(self):
    """Gets the data_point_name of this RestDataPointV1.  # noqa: E501


    :return: The data_point_name of this RestDataPointV1.  # noqa: E501
    :rtype: str
    """
    return self._data_point_name

  @data_point_name.setter
  def data_point_name(self, data_point_name):
    """Sets the data_point_name of this RestDataPointV1.


    :param data_point_name: The data_point_name of this RestDataPointV1.  # noqa: E501
    :type: str
    """

    self._data_point_name = data_point_name

  @property
  def data_point_type(self):
    """Gets the data_point_type of this RestDataPointV1.  # noqa: E501


    :return: The data_point_type of this RestDataPointV1.  # noqa: E501
    :rtype: str
    """
    return self._data_point_type

  @data_point_type.setter
  def data_point_type(self, data_point_type):
    """Sets the data_point_type of this RestDataPointV1.


    :param data_point_type: The data_point_type of this RestDataPointV1.  # noqa: E501
    :type: str
    """

    self._data_point_type = data_point_type

  @property
  def values(self):
    """Gets the values of this RestDataPointV1.  # noqa: E501


    :return: The values of this RestDataPointV1.  # noqa: E501
    :rtype: MapStringString
    """
    return self._values

  @values.setter
  def values(self, values):
    """Sets the values of this RestDataPointV1.


    :param values: The values of this RestDataPointV1.  # noqa: E501
    :type: MapStringString
    """

    self._values = values

  def to_dict(self):
    """Returns the model properties as a dict"""
    result = {}

    for attr, _ in six.iteritems(self.swagger_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(map(
            lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
            value
        ))
      elif hasattr(value, "to_dict"):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(map(
            lambda item: (item[0], item[1].to_dict())
            if hasattr(item[1], "to_dict") else item,
            value.items()
        ))
      else:
        result[attr] = value
    if issubclass(RestDataPointV1, dict):
      for key, value in self.items():
        result[key] = value

    return result

  def to_str(self):
    """Returns the string representation of the model"""
    return pprint.pformat(self.to_dict())

  def __repr__(self):
    """For `print` and `pprint`"""
    return self.to_str()

  def __eq__(self, other):
    """Returns true if both objects are equal"""
    if not isinstance(other, RestDataPointV1):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """Returns true if both objects are not equal"""
    return not self == other
