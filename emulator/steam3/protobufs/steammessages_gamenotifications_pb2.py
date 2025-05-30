# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_gamenotifications.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'steammessages_gamenotifications.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steam3.protobufs import steammessages_base_pb2 as steammessages__base__pb2
from steam3.protobufs import steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%steammessages_gamenotifications.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\xe0\x02\n\x1b\x43GameNotifications_Variable\x12\xa6\x01\n\x03key\x18\x01 \x01(\tB\x98\x01\x82\xb5\x18\x93\x01The name of the variable in the localized text -- anywhere that %variablename% is found within the text it will be substituded with the given value\x12\x97\x01\n\x05value\x18\x02 \x01(\tB\x87\x01\x82\xb5\x18\x82\x01The value of the variable to substitute in the localized text in place of the given variable.  Can itself be a localization token.\"\x85\x03\n CGameNotifications_LocalizedText\x12H\n\x05token\x18\x01 \x01(\tB9\x82\xb5\x18\x35\x41 localization token that maps to the desired string.\x12\x8d\x01\n\tvariables\x18\x02 \x03(\x0b\x32\x1c.CGameNotifications_VariableB\\\x82\xb5\x18XA list of variables values to substitute in any variables found in the localized string.\x12\x86\x01\n\rrendered_text\x18\x03 \x01(\tBo\x82\xb5\x18kText rendered in the requested language, complete with variable substitutions, if a language was specified.\"\x95\x04\n\x1d\x43GameNotifications_UserStatus\x12\x31\n\x07steamid\x18\x01 \x01(\x06\x42 \x82\xb5\x18\x1cThe specific user\'s steamid.\x12\xa4\x01\n\x05state\x18\x02 \x01(\tB\x94\x01\x82\xb5\x18\x8f\x01The user\'s state.  ready -- the user is ready to play.  waiting -- The game is waiting on an action from the user. completed, the game is over.\x12\x84\x01\n\x05title\x18\x03 \x01(\x0b\x32!.CGameNotifications_LocalizedTextBR\x82\xb5\x18NTitle of the session to display to this user in their list of active sessions.\x12\x92\x01\n\x07message\x18\x04 \x01(\x0b\x32!.CGameNotifications_LocalizedTextB^\x82\xb5\x18ZSubtitle of the session to display to this user user within their list of active sessions.\"\x96\x05\n(CGameNotifications_CreateSession_Request\x12\x37\n\x05\x61ppid\x18\x01 \x01(\rB(\x82\xb5\x18$The appid to create the session for.\x12\x7f\n\x07\x63ontext\x18\x02 \x01(\x04\x42n\x82\xb5\x18jGame-specified context value the game can used to associate the session with some object on their backend.\x12\x83\x01\n\x05title\x18\x03 \x01(\x0b\x32!.CGameNotifications_LocalizedTextBQ\x82\xb5\x18MThe title of the session to be displayed within each user\'s list of sessions.\x12\x61\n\x05users\x18\x04 \x03(\x0b\x32\x1e.CGameNotifications_UserStatusB2\x82\xb5\x18.The initial state of all users in the session.\x12\xc6\x01\n\x07steamid\x18\x05 \x01(\x06\x42\xb4\x01\x82\xb5\x18\xaf\x01(Optional) steamid to make the request_id on behalf of -- if specified, the user must be in the session and all users being added to the session must be friends with the user.\"i\n)CGameNotifications_CreateSession_Response\x12<\n\tsessionid\x18\x01 \x01(\x04\x42)\x82\xb5\x18%The sessionid of the created session.\"\x92\x02\n(CGameNotifications_DeleteSession_Request\x12/\n\tsessionid\x18\x01 \x01(\x04\x42\x1c\x82\xb5\x18\x18The sessionid to delete.\x12\x36\n\x05\x61ppid\x18\x02 \x01(\rB\'\x82\xb5\x18#The appid of the session to delete.\x12}\n\x07steamid\x18\x03 \x01(\x06\x42l\x82\xb5\x18h(Optional) steamid to make the request_id on behalf of -- if specified, the user must be in the session.\"+\n)CGameNotifications_DeleteSession_Response\"\xc0\x05\n(CGameNotifications_UpdateSession_Request\x12/\n\tsessionid\x18\x01 \x01(\x04\x42\x1c\x82\xb5\x18\x18The sessionid to update.\x12\x36\n\x05\x61ppid\x18\x02 \x01(\rB\'\x82\xb5\x18#The appid of the session to update.\x12\x90\x01\n\x05title\x18\x03 \x01(\x0b\x32!.CGameNotifications_LocalizedTextB^\x82\xb5\x18Z(Optional) The new title of the session.  If not specified, the title will not be changed.\x12\xce\x01\n\x05users\x18\x04 \x03(\x0b\x32\x1e.CGameNotifications_UserStatusB\x9e\x01\x82\xb5\x18\x99\x01(Optional) A list of users whose state will be updated to reflect the given state. If the users are not already in the session, they will be added to it.\x12\xc6\x01\n\x07steamid\x18\x06 \x01(\x06\x42\xb4\x01\x82\xb5\x18\xaf\x01(Optional) steamid to make the request_id on behalf of -- if specified, the user must be in the session and all users being added to the session must be friends with the user.\"+\n)CGameNotifications_UpdateSession_Response\"\xa5\x04\n,CGameNotifications_EnumerateSessions_Request\x12\x81\x01\n\x05\x61ppid\x18\x01 \x01(\rBr\x82\xb5\x18nThe sessionid to request_id details for. Optional. If not specified, all the user\'s sessions will be returned.\x12\x8e\x01\n\x19include_all_user_messages\x18\x03 \x01(\x08\x42k\x82\xb5\x18g(Optional) Boolean determining whether the message for all users should be included. Defaults to false.\x12\x9b\x01\n\x19include_auth_user_message\x18\x04 \x01(\x08\x42x\x82\xb5\x18t(Optional) Boolean determining whether the message for the authenticated user should be included. Defaults to false.\x12\x42\n\x08language\x18\x05 \x01(\tB0\x82\xb5\x18,(Optional) Language to localize the text in.\"\xc3\x04\n\x1a\x43GameNotifications_Session\x12\x36\n\tsessionid\x18\x01 \x01(\x04\x42#\x82\xb5\x18\x1fThe sessionid for this session.\x12-\n\x05\x61ppid\x18\x02 \x01(\x04\x42\x1e\x82\xb5\x18\x1aThe appid for the session.\x12\x7f\n\x07\x63ontext\x18\x03 \x01(\x04\x42n\x82\xb5\x18jGame-specified context value the game can used to associate the session with some object on their backend.\x12X\n\x05title\x18\x04 \x01(\x0b\x32!.CGameNotifications_LocalizedTextB&\x82\xb5\x18\"The current title for the session.\x12;\n\x0ctime_created\x18\x05 \x01(\rB%\x82\xb5\x18!The time the session was created.\x12@\n\x0ctime_updated\x18\x06 \x01(\rB*\x82\xb5\x18&The last time the session was updated.\x12\x64\n\x0buser_status\x18\x07 \x03(\x0b\x32\x1e.CGameNotifications_UserStatusB/\x82\xb5\x18+The status of all the users in the session.\"\x82\x01\n-CGameNotifications_EnumerateSessions_Response\x12Q\n\x08sessions\x18\x01 \x03(\x0b\x32\x1b.CGameNotifications_SessionB\"\x82\xb5\x18\x1e\x41 list of the user\'s sessions.\"\xd6\x03\n,CGameNotifications_GetSessionDetails_Request\x12P\n\x08sessions\x18\x01 \x03(\x0b\x32>.CGameNotifications_GetSessionDetails_Request.RequestedSession\x12.\n\x05\x61ppid\x18\x02 \x01(\rB\x1f\x82\xb5\x18\x1bThe appid for the sessions.\x12\x37\n\x08language\x18\x03 \x01(\tB%\x82\xb5\x18!Language to localize the text in.\x1a\xea\x01\n\x10RequestedSession\x12\x38\n\tsessionid\x18\x01 \x01(\x04\x42%\x82\xb5\x18!The sessionid to get details for.\x12\x9b\x01\n\x19include_auth_user_message\x18\x03 \x01(\x08\x42x\x82\xb5\x18t(Optional) Boolean determining whether the message for the authenticated user should be included. Defaults to false.\"\x7f\n-CGameNotifications_GetSessionDetails_Response\x12N\n\x08sessions\x18\x01 \x03(\x0b\x32\x1b.CGameNotifications_SessionB\x1f\x82\xb5\x18\x1bThe details of the session.\"\xa8\x01\n\x18GameNotificationSettings\x12\x37\n\x05\x61ppid\x18\x01 \x01(\rB(\x82\xb5\x18$The appid to create the session for.\x12S\n\x13\x61llow_notifications\x18\x02 \x01(\x08\x42\x36\x82\xb5\x18\x32Whether the user allows notification for this app.\"v\n5CGameNotifications_UpdateNotificationSettings_Request\x12=\n\x1agame_notification_settings\x18\x01 \x03(\x0b\x32\x19.GameNotificationSettings\"8\n6CGameNotifications_UpdateNotificationSettings_Response\"\xc6\x01\n8CGameNotifications_OnNotificationsRequested_Notification\x12N\n\x07steamid\x18\x01 \x01(\x06\x42=\x82\xb5\x18\x39steamid of the user who notifications were requested for.\x12:\n\x05\x61ppid\x18\x02 \x01(\rB+\x82\xb5\x18\'The appid that requested notifications.\"\xbe\x03\n3CGameNotifications_OnUserStatusChanged_Notification\x12>\n\x07steamid\x18\x01 \x01(\x06\x42-\x82\xb5\x18)steamid of the user whose status changed.\x12X\n\tsessionid\x18\x02 \x01(\x04\x42\x45\x82\xb5\x18\x41The sessionid of the session where the user\'s status was changed.\x12L\n\x05\x61ppid\x18\x03 \x01(\rB=\x82\xb5\x18\x39The appid of the session where the user\'s status changed.\x12V\n\x06status\x18\x04 \x01(\x0b\x32\x1e.CGameNotifications_UserStatusB&\x82\xb5\x18\"(Optional) New status of the user.\x12G\n\x07removed\x18\x05 \x01(\x08\x42\x36\x82\xb5\x18\x32(Optional) User has been removed from the session.2\xa6\x08\n\x11GameNotifications\x12\x8d\x01\n\x11UserCreateSession\x12).CGameNotifications_CreateSession_Request\x1a*.CGameNotifications_CreateSession_Response\"!\x82\xb5\x18\x1d\x43reates an async game session\x12\x8d\x01\n\x11UserDeleteSession\x12).CGameNotifications_DeleteSession_Request\x1a*.CGameNotifications_DeleteSession_Response\"!\x82\xb5\x18\x1d\x44\x65letes an async game session\x12\x8d\x01\n\x11UserUpdateSession\x12).CGameNotifications_UpdateSession_Request\x1a*.CGameNotifications_UpdateSession_Response\"!\x82\xb5\x18\x1dUpdates an async game session\x12\x94\x01\n\x11\x45numerateSessions\x12-.CGameNotifications_EnumerateSessions_Request\x1a..CGameNotifications_EnumerateSessions_Response\" \x82\xb5\x18\x1c\x45numerates a user\'s sessions\x12\x9e\x01\n\x11GetSessionDetails\x12-.CGameNotifications_GetSessionDetails_Request\x1a..CGameNotifications_GetSessionDetails_Response\"*\x82\xb5\x18&Get the details for a specific session\x12\xd6\x01\n\x1aUpdateNotificationSettings\x12\x36.CGameNotifications_UpdateNotificationSettings_Request\x1a\x37.CGameNotifications_UpdateNotificationSettings_Response\"G\x82\xb5\x18\x43Updates whether a user allows game notifications for a specific app\x1aP\x82\xb5\x18LA service for functions related to the asyncronous game notification server.2\xdf\x02\n\x17GameNotificationsClient\x12\x95\x01\n\x18OnNotificationsRequested\x12\x39.CGameNotifications_OnNotificationsRequested_Notification\x1a\x0b.NoResponse\"1\x82\xb5\x18-Requests that the user opt into notifications\x12\x8d\x01\n\x13OnUserStatusChanged\x12\x34.CGameNotifications_OnUserStatusChanged_Notification\x1a\x0b.NoResponse\"3\x82\xb5\x18/Notification that the user\'s status has changed\x1a\x1c\x82\xb5\x18\x14\x43lient notifications\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_gamenotifications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CGAMENOTIFICATIONS_VARIABLE'].fields_by_name['key']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_VARIABLE'].fields_by_name['key']._serialized_options = b'\202\265\030\223\001The name of the variable in the localized text -- anywhere that %variablename% is found within the text it will be substituded with the given value'
  _globals['_CGAMENOTIFICATIONS_VARIABLE'].fields_by_name['value']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_VARIABLE'].fields_by_name['value']._serialized_options = b'\202\265\030\202\001The value of the variable to substitute in the localized text in place of the given variable.  Can itself be a localization token.'
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT'].fields_by_name['token']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT'].fields_by_name['token']._serialized_options = b'\202\265\0305A localization token that maps to the desired string.'
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT'].fields_by_name['variables']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT'].fields_by_name['variables']._serialized_options = b'\202\265\030XA list of variables values to substitute in any variables found in the localized string.'
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT'].fields_by_name['rendered_text']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT'].fields_by_name['rendered_text']._serialized_options = b'\202\265\030kText rendered in the requested language, complete with variable substitutions, if a language was specified.'
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['steamid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['steamid']._serialized_options = b'\202\265\030\034The specific user\'s steamid.'
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['state']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['state']._serialized_options = b'\202\265\030\217\001The user\'s state.  ready -- the user is ready to play.  waiting -- The game is waiting on an action from the user. completed, the game is over.'
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['title']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['title']._serialized_options = b'\202\265\030NTitle of the session to display to this user in their list of active sessions.'
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['message']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_USERSTATUS'].fields_by_name['message']._serialized_options = b'\202\265\030ZSubtitle of the session to display to this user user within their list of active sessions.'
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030$The appid to create the session for.'
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['context']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['context']._serialized_options = b'\202\265\030jGame-specified context value the game can used to associate the session with some object on their backend.'
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['title']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['title']._serialized_options = b'\202\265\030MThe title of the session to be displayed within each user\'s list of sessions.'
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['users']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['users']._serialized_options = b'\202\265\030.The initial state of all users in the session.'
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['steamid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST'].fields_by_name['steamid']._serialized_options = b'\202\265\030\257\001(Optional) steamid to make the request_id on behalf of -- if specified, the user must be in the session and all users being added to the session must be friends with the user.'
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_RESPONSE'].fields_by_name['sessionid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_RESPONSE'].fields_by_name['sessionid']._serialized_options = b'\202\265\030%The sessionid of the created session.'
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST'].fields_by_name['sessionid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST'].fields_by_name['sessionid']._serialized_options = b'\202\265\030\030The sessionid to delete.'
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030#The appid of the session to delete.'
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST'].fields_by_name['steamid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST'].fields_by_name['steamid']._serialized_options = b'\202\265\030h(Optional) steamid to make the request_id on behalf of -- if specified, the user must be in the session.'
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['sessionid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['sessionid']._serialized_options = b'\202\265\030\030The sessionid to update.'
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030#The appid of the session to update.'
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['title']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['title']._serialized_options = b'\202\265\030Z(Optional) The new title of the session.  If not specified, the title will not be changed.'
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['users']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['users']._serialized_options = b'\202\265\030\231\001(Optional) A list of users whose state will be updated to reflect the given state. If the users are not already in the session, they will be added to it.'
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['steamid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST'].fields_by_name['steamid']._serialized_options = b'\202\265\030\257\001(Optional) steamid to make the request_id on behalf of -- if specified, the user must be in the session and all users being added to the session must be friends with the user.'
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030nThe sessionid to request_id details for. Optional. If not specified, all the user\'s sessions will be returned.'
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['include_all_user_messages']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['include_all_user_messages']._serialized_options = b'\202\265\030g(Optional) Boolean determining whether the message for all users should be included. Defaults to false.'
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['include_auth_user_message']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['include_auth_user_message']._serialized_options = b'\202\265\030t(Optional) Boolean determining whether the message for the authenticated user should be included. Defaults to false.'
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['language']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST'].fields_by_name['language']._serialized_options = b'\202\265\030,(Optional) Language to localize the text in.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['sessionid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['sessionid']._serialized_options = b'\202\265\030\037The sessionid for this session.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['appid']._serialized_options = b'\202\265\030\032The appid for the session.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['context']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['context']._serialized_options = b'\202\265\030jGame-specified context value the game can used to associate the session with some object on their backend.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['title']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['title']._serialized_options = b'\202\265\030\"The current title for the session.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['time_created']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['time_created']._serialized_options = b'\202\265\030!The time the session was created.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['time_updated']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['time_updated']._serialized_options = b'\202\265\030&The last time the session was updated.'
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['user_status']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_SESSION'].fields_by_name['user_status']._serialized_options = b'\202\265\030+The status of all the users in the session.'
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_RESPONSE'].fields_by_name['sessions']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_RESPONSE'].fields_by_name['sessions']._serialized_options = b'\202\265\030\036A list of the user\'s sessions.'
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST_REQUESTEDSESSION'].fields_by_name['sessionid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST_REQUESTEDSESSION'].fields_by_name['sessionid']._serialized_options = b'\202\265\030!The sessionid to get details for.'
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST_REQUESTEDSESSION'].fields_by_name['include_auth_user_message']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST_REQUESTEDSESSION'].fields_by_name['include_auth_user_message']._serialized_options = b'\202\265\030t(Optional) Boolean determining whether the message for the authenticated user should be included. Defaults to false.'
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030\033The appid for the sessions.'
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST'].fields_by_name['language']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST'].fields_by_name['language']._serialized_options = b'\202\265\030!Language to localize the text in.'
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_RESPONSE'].fields_by_name['sessions']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_RESPONSE'].fields_by_name['sessions']._serialized_options = b'\202\265\030\033The details of the session.'
  _globals['_GAMENOTIFICATIONSETTINGS'].fields_by_name['appid']._loaded_options = None
  _globals['_GAMENOTIFICATIONSETTINGS'].fields_by_name['appid']._serialized_options = b'\202\265\030$The appid to create the session for.'
  _globals['_GAMENOTIFICATIONSETTINGS'].fields_by_name['allow_notifications']._loaded_options = None
  _globals['_GAMENOTIFICATIONSETTINGS'].fields_by_name['allow_notifications']._serialized_options = b'\202\265\0302Whether the user allows notification for this app.'
  _globals['_CGAMENOTIFICATIONS_ONNOTIFICATIONSREQUESTED_NOTIFICATION'].fields_by_name['steamid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONNOTIFICATIONSREQUESTED_NOTIFICATION'].fields_by_name['steamid']._serialized_options = b'\202\265\0309steamid of the user who notifications were requested for.'
  _globals['_CGAMENOTIFICATIONS_ONNOTIFICATIONSREQUESTED_NOTIFICATION'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONNOTIFICATIONSREQUESTED_NOTIFICATION'].fields_by_name['appid']._serialized_options = b'\202\265\030\'The appid that requested notifications.'
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['steamid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['steamid']._serialized_options = b'\202\265\030)steamid of the user whose status changed.'
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['sessionid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['sessionid']._serialized_options = b'\202\265\030AThe sessionid of the session where the user\'s status was changed.'
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['appid']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['appid']._serialized_options = b'\202\265\0309The appid of the session where the user\'s status changed.'
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['status']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['status']._serialized_options = b'\202\265\030\"(Optional) New status of the user.'
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['removed']._loaded_options = None
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION'].fields_by_name['removed']._serialized_options = b'\202\265\0302(Optional) User has been removed from the session.'
  _globals['_GAMENOTIFICATIONS']._loaded_options = None
  _globals['_GAMENOTIFICATIONS']._serialized_options = b'\202\265\030LA service for functions related to the asyncronous game notification server.'
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UserCreateSession']._loaded_options = None
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UserCreateSession']._serialized_options = b'\202\265\030\035Creates an async game session'
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UserDeleteSession']._loaded_options = None
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UserDeleteSession']._serialized_options = b'\202\265\030\035Deletes an async game session'
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UserUpdateSession']._loaded_options = None
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UserUpdateSession']._serialized_options = b'\202\265\030\035Updates an async game session'
  _globals['_GAMENOTIFICATIONS'].methods_by_name['EnumerateSessions']._loaded_options = None
  _globals['_GAMENOTIFICATIONS'].methods_by_name['EnumerateSessions']._serialized_options = b'\202\265\030\034Enumerates a user\'s sessions'
  _globals['_GAMENOTIFICATIONS'].methods_by_name['GetSessionDetails']._loaded_options = None
  _globals['_GAMENOTIFICATIONS'].methods_by_name['GetSessionDetails']._serialized_options = b'\202\265\030&Get the details for a specific session'
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UpdateNotificationSettings']._loaded_options = None
  _globals['_GAMENOTIFICATIONS'].methods_by_name['UpdateNotificationSettings']._serialized_options = b'\202\265\030CUpdates whether a user allows game notifications for a specific app'
  _globals['_GAMENOTIFICATIONSCLIENT']._loaded_options = None
  _globals['_GAMENOTIFICATIONSCLIENT']._serialized_options = b'\202\265\030\024Client notifications\300\265\030\002'
  _globals['_GAMENOTIFICATIONSCLIENT'].methods_by_name['OnNotificationsRequested']._loaded_options = None
  _globals['_GAMENOTIFICATIONSCLIENT'].methods_by_name['OnNotificationsRequested']._serialized_options = b'\202\265\030-Requests that the user opt into notifications'
  _globals['_GAMENOTIFICATIONSCLIENT'].methods_by_name['OnUserStatusChanged']._loaded_options = None
  _globals['_GAMENOTIFICATIONSCLIENT'].methods_by_name['OnUserStatusChanged']._serialized_options = b'\202\265\030/Notification that the user\'s status has changed'
  _globals['_CGAMENOTIFICATIONS_VARIABLE']._serialized_start=102
  _globals['_CGAMENOTIFICATIONS_VARIABLE']._serialized_end=454
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT']._serialized_start=457
  _globals['_CGAMENOTIFICATIONS_LOCALIZEDTEXT']._serialized_end=846
  _globals['_CGAMENOTIFICATIONS_USERSTATUS']._serialized_start=849
  _globals['_CGAMENOTIFICATIONS_USERSTATUS']._serialized_end=1382
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST']._serialized_start=1385
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_REQUEST']._serialized_end=2047
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_RESPONSE']._serialized_start=2049
  _globals['_CGAMENOTIFICATIONS_CREATESESSION_RESPONSE']._serialized_end=2154
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST']._serialized_start=2157
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_REQUEST']._serialized_end=2431
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_RESPONSE']._serialized_start=2433
  _globals['_CGAMENOTIFICATIONS_DELETESESSION_RESPONSE']._serialized_end=2476
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST']._serialized_start=2479
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_REQUEST']._serialized_end=3183
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_RESPONSE']._serialized_start=3185
  _globals['_CGAMENOTIFICATIONS_UPDATESESSION_RESPONSE']._serialized_end=3228
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST']._serialized_start=3231
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_REQUEST']._serialized_end=3780
  _globals['_CGAMENOTIFICATIONS_SESSION']._serialized_start=3783
  _globals['_CGAMENOTIFICATIONS_SESSION']._serialized_end=4362
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_RESPONSE']._serialized_start=4365
  _globals['_CGAMENOTIFICATIONS_ENUMERATESESSIONS_RESPONSE']._serialized_end=4495
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST']._serialized_start=4498
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST']._serialized_end=4968
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST_REQUESTEDSESSION']._serialized_start=4734
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_REQUEST_REQUESTEDSESSION']._serialized_end=4968
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_RESPONSE']._serialized_start=4970
  _globals['_CGAMENOTIFICATIONS_GETSESSIONDETAILS_RESPONSE']._serialized_end=5097
  _globals['_GAMENOTIFICATIONSETTINGS']._serialized_start=5100
  _globals['_GAMENOTIFICATIONSETTINGS']._serialized_end=5268
  _globals['_CGAMENOTIFICATIONS_UPDATENOTIFICATIONSETTINGS_REQUEST']._serialized_start=5270
  _globals['_CGAMENOTIFICATIONS_UPDATENOTIFICATIONSETTINGS_REQUEST']._serialized_end=5388
  _globals['_CGAMENOTIFICATIONS_UPDATENOTIFICATIONSETTINGS_RESPONSE']._serialized_start=5390
  _globals['_CGAMENOTIFICATIONS_UPDATENOTIFICATIONSETTINGS_RESPONSE']._serialized_end=5446
  _globals['_CGAMENOTIFICATIONS_ONNOTIFICATIONSREQUESTED_NOTIFICATION']._serialized_start=5449
  _globals['_CGAMENOTIFICATIONS_ONNOTIFICATIONSREQUESTED_NOTIFICATION']._serialized_end=5647
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION']._serialized_start=5650
  _globals['_CGAMENOTIFICATIONS_ONUSERSTATUSCHANGED_NOTIFICATION']._serialized_end=6096
  _globals['_GAMENOTIFICATIONS']._serialized_start=6099
  _globals['_GAMENOTIFICATIONS']._serialized_end=7161
  _globals['_GAMENOTIFICATIONSCLIENT']._serialized_start=7164
  _globals['_GAMENOTIFICATIONSCLIENT']._serialized_end=7515
_builder.BuildServices(DESCRIPTOR, 'steammessages_gamenotifications_pb2', _globals)
# @@protoc_insertion_point(module_scope)
