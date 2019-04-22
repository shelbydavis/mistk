# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mistk.server.models.base_model_ import Model
from mistk.server.models.metric import Metric  # noqa: F401,E501
from mistk.server.models.metric_data_parameters import MetricDataParameters  # noqa: F401,E501
from mistk.server.models.object_info import ObjectInfo  # noqa: F401,E501
from mistk.server import util


class MistkMetric(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, object_info: ObjectInfo=None, package: str=None, method: str=None, default_args: object=None, data_parameters: MetricDataParameters=None):  # noqa: E501
        """MistkMetric - a model defined in Swagger

        :param object_info: The object_info of this MistkMetric.  # noqa: E501
        :type object_info: ObjectInfo
        :param package: The package of this MistkMetric.  # noqa: E501
        :type package: str
        :param method: The method of this MistkMetric.  # noqa: E501
        :type method: str
        :param default_args: The default_args of this MistkMetric.  # noqa: E501
        :type default_args: object
        :param data_parameters: The data_parameters of this MistkMetric.  # noqa: E501
        :type data_parameters: MetricDataParameters
        """
        self.swagger_types = {
            'object_info': ObjectInfo,
            'package': str,
            'method': str,
            'default_args': object,
            'data_parameters': MetricDataParameters
        }

        self.attribute_map = {
            'object_info': 'objectInfo',
            'package': 'package',
            'method': 'method',
            'default_args': 'defaultArgs',
            'data_parameters': 'dataParameters'
        }

        self._object_info = object_info
        self._package = package
        self._method = method
        self._default_args = default_args
        self._data_parameters = data_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'MistkMetric':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MistkMetric of this MistkMetric.  # noqa: E501
        :rtype: MistkMetric
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_info(self) -> ObjectInfo:
        """Gets the object_info of this MistkMetric.


        :return: The object_info of this MistkMetric.
        :rtype: ObjectInfo
        """
        return self._object_info

    @object_info.setter
    def object_info(self, object_info: ObjectInfo):
        """Sets the object_info of this MistkMetric.


        :param object_info: The object_info of this MistkMetric.
        :type object_info: ObjectInfo
        """
        if object_info is None:
            raise ValueError("Invalid value for `object_info`, must not be `None`")  # noqa: E501

        self._object_info = object_info

    @property
    def package(self) -> str:
        """Gets the package of this MistkMetric.

        The name of the package containing the implementation of this metric.   # noqa: E501

        :return: The package of this MistkMetric.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package: str):
        """Sets the package of this MistkMetric.

        The name of the package containing the implementation of this metric.   # noqa: E501

        :param package: The package of this MistkMetric.
        :type package: str
        """

        self._package = package

    @property
    def method(self) -> str:
        """Gets the method of this MistkMetric.

        The name of the method to be called when applying the metric.   # noqa: E501

        :return: The method of this MistkMetric.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method: str):
        """Sets the method of this MistkMetric.

        The name of the method to be called when applying the metric.   # noqa: E501

        :param method: The method of this MistkMetric.
        :type method: str
        """

        self._method = method

    @property
    def default_args(self) -> object:
        """Gets the default_args of this MistkMetric.

        The default arguments passed to the method when the metric is called.  These can be overwritten when the metric is associated with an assessment.   # noqa: E501

        :return: The default_args of this MistkMetric.
        :rtype: object
        """
        return self._default_args

    @default_args.setter
    def default_args(self, default_args: object):
        """Sets the default_args of this MistkMetric.

        The default arguments passed to the method when the metric is called.  These can be overwritten when the metric is associated with an assessment.   # noqa: E501

        :param default_args: The default_args of this MistkMetric.
        :type default_args: object
        """

        self._default_args = default_args

    @property
    def data_parameters(self) -> MetricDataParameters:
        """Gets the data_parameters of this MistkMetric.


        :return: The data_parameters of this MistkMetric.
        :rtype: MetricDataParameters
        """
        return self._data_parameters

    @data_parameters.setter
    def data_parameters(self, data_parameters: MetricDataParameters):
        """Sets the data_parameters of this MistkMetric.


        :param data_parameters: The data_parameters of this MistkMetric.
        :type data_parameters: MetricDataParameters
        """

        self._data_parameters = data_parameters
