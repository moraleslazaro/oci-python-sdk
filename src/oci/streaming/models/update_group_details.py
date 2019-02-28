# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGroupDetails(object):
    """
    Request body for operationally managing a group.
    """

    #: A constant which can be used with the type property of a UpdateGroupDetails.
    #: This constant has a value of "AT_TIME"
    TYPE_AT_TIME = "AT_TIME"

    #: A constant which can be used with the type property of a UpdateGroupDetails.
    #: This constant has a value of "LATEST"
    TYPE_LATEST = "LATEST"

    #: A constant which can be used with the type property of a UpdateGroupDetails.
    #: This constant has a value of "TRIM_HORIZON"
    TYPE_TRIM_HORIZON = "TRIM_HORIZON"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateGroupDetails.
            Allowed values for this property are: "AT_TIME", "LATEST", "TRIM_HORIZON"
        :type type: str

        :param time:
            The value to assign to the time property of this UpdateGroupDetails.
        :type time: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'time': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'time': 'time'
        }

        self._type = None
        self._time = None

    @property
    def type(self):
        """
        Gets the type of this UpdateGroupDetails.
        The type of the cursor.

        Allowed values for this property are: "AT_TIME", "LATEST", "TRIM_HORIZON"


        :return: The type of this UpdateGroupDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateGroupDetails.
        The type of the cursor.


        :param type: The type of this UpdateGroupDetails.
        :type: str
        """
        allowed_values = ["AT_TIME", "LATEST", "TRIM_HORIZON"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def time(self):
        """
        Gets the time of this UpdateGroupDetails.
        The time to consume from if type is AT_TIME.


        :return: The time of this UpdateGroupDetails.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this UpdateGroupDetails.
        The time to consume from if type is AT_TIME.


        :param time: The time of this UpdateGroupDetails.
        :type: datetime
        """
        self._time = time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other