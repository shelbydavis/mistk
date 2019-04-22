# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mistk.server.models.base_model_ import Model
from mistk.server import util


class ModelInstanceInitParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, objectives: List[str]=None, model_properties: object=None, hyperparameters: object=None):  # noqa: E501
        """ModelInstanceInitParams - a model defined in Swagger

        :param objectives: The objectives of this ModelInstanceInitParams.  # noqa: E501
        :type objectives: List[str]
        :param model_properties: The model_properties of this ModelInstanceInitParams.  # noqa: E501
        :type model_properties: object
        :param hyperparameters: The hyperparameters of this ModelInstanceInitParams.  # noqa: E501
        :type hyperparameters: object
        """
        self.swagger_types = {
            'objectives': List[str],
            'model_properties': object,
            'hyperparameters': object
        }

        self.attribute_map = {
            'objectives': 'objectives',
            'model_properties': 'modelProperties',
            'hyperparameters': 'hyperparameters'
        }

        self._objectives = objectives
        self._model_properties = model_properties
        self._hyperparameters = hyperparameters

    @classmethod
    def from_dict(cls, dikt) -> 'ModelInstanceInitParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelInstanceInitParams of this ModelInstanceInitParams.  # noqa: E501
        :rtype: ModelInstanceInitParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def objectives(self) -> List[str]:
        """Gets the objectives of this ModelInstanceInitParams.

        The objectives inform the model how it will be used while running   # noqa: E501

        :return: The objectives of this ModelInstanceInitParams.
        :rtype: List[str]
        """
        return self._objectives

    @objectives.setter
    def objectives(self, objectives: List[str]):
        """Sets the objectives of this ModelInstanceInitParams.

        The objectives inform the model how it will be used while running   # noqa: E501

        :param objectives: The objectives of this ModelInstanceInitParams.
        :type objectives: List[str]
        """
        allowed_values = ["training", "prediction", "streaming_prediction", "transfer_learning"]  # noqa: E501
        if not set(objectives).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `objectives` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(objectives) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._objectives = objectives

    @property
    def model_properties(self) -> object:
        """Gets the model_properties of this ModelInstanceInitParams.

        A dictionary of model properties.  # noqa: E501

        :return: The model_properties of this ModelInstanceInitParams.
        :rtype: object
        """
        return self._model_properties

    @model_properties.setter
    def model_properties(self, model_properties: object):
        """Sets the model_properties of this ModelInstanceInitParams.

        A dictionary of model properties.  # noqa: E501

        :param model_properties: The model_properties of this ModelInstanceInitParams.
        :type model_properties: object
        """

        self._model_properties = model_properties

    @property
    def hyperparameters(self) -> object:
        """Gets the hyperparameters of this ModelInstanceInitParams.

        A dictionary mapping hyperparameter name to value  # noqa: E501

        :return: The hyperparameters of this ModelInstanceInitParams.
        :rtype: object
        """
        return self._hyperparameters

    @hyperparameters.setter
    def hyperparameters(self, hyperparameters: object):
        """Sets the hyperparameters of this ModelInstanceInitParams.

        A dictionary mapping hyperparameter name to value  # noqa: E501

        :param hyperparameters: The hyperparameters of this ModelInstanceInitParams.
        :type hyperparameters: object
        """

        self._hyperparameters = hyperparameters
