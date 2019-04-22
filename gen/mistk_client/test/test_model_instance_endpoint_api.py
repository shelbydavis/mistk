# coding: utf-8

"""
    Model Integration Software ToolKit

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mistk_test_harness.client
from mistk_test_harness.client.api.model_instance_endpoint_api import ModelInstanceEndpointApi  # noqa: E501
from mistk_test_harness.client.rest import ApiException


class TestModelInstanceEndpointApi(unittest.TestCase):
    """ModelInstanceEndpointApi unit test stubs"""

    def setUp(self):
        self.api = mistk_test_harness.client.api.model_instance_endpoint_api.ModelInstanceEndpointApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_build_model(self):
        """Test case for build_model

        Build the model  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        Get the status of the model  # noqa: E501
        """
        pass

    def test_initialize_model(self):
        """Test case for initialize_model

        Initialize the model  # noqa: E501
        """
        pass

    def test_load_data(self):
        """Test case for load_data

        Loads data for the model  # noqa: E501
        """
        pass

    def test_pause(self):
        """Test case for pause

        Pause the model  # noqa: E501
        """
        pass

    def test_predict(self):
        """Test case for predict

        Perform predictions with the model  # noqa: E501
        """
        pass

    def test_reset(self):
        """Test case for reset

        Resets the model  # noqa: E501
        """
        pass

    def test_resume_predict(self):
        """Test case for resume_predict

        Resume predicitons on a paused model  # noqa: E501
        """
        pass

    def test_resume_training(self):
        """Test case for resume_training

        Resume training on a paused model  # noqa: E501
        """
        pass

    def test_save_model(self):
        """Test case for save_model

        Save the model snapshot  # noqa: E501
        """
        pass

    def test_save_predictions(self):
        """Test case for save_predictions

        Save the model's predictions  # noqa: E501
        """
        pass

    def test_stream_predict(self):
        """Test case for stream_predict

        Perform streaming predictions with the model  # noqa: E501
        """
        pass

    def test_terminate(self):
        """Test case for terminate

        Shut down the model  # noqa: E501
        """
        pass

    def test_train(self):
        """Test case for train

        Train the model  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()