# def authorized_s2s(function):
#     """
#     When checking a service that needs authentication, check if the
#     service has auth_jwt_token
#     """

#     def wrap(self, *args, **kwargs):
#         previous_authorization = self.authorization

#         auth = generate_server_token(
#             settings.SERVICE_CALLSIGN, some_user_id
#         )
#         self.set_authorization(auth)

#         function_result = function(self, *args, **kwargs)

#         self.set_authorization(previous_authorization)

#         return function_result
    
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap