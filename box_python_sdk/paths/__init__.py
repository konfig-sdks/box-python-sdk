# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from box_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTHORIZE = "/authorize"
    OAUTH2_TOKEN = "/oauth2/token"
    OAUTH2_TOKENREFRESH = "/oauth2/token#refresh"
    OAUTH2_REVOKE = "/oauth2/revoke"
    FILES_FILE_ID = "/files/{file_id}"
    FILES_FILE_ID_CONTENT = "/files/{file_id}/content"
    FILES_CONTENT = "/files/content"
    FILES_UPLOAD_SESSIONS = "/files/upload_sessions"
    FILES_FILE_ID_UPLOAD_SESSIONS = "/files/{file_id}/upload_sessions"
    FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID = "/files/upload_sessions/{upload_session_id}"
    FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID_PARTS = "/files/upload_sessions/{upload_session_id}/parts"
    FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID_COMMIT = "/files/upload_sessions/{upload_session_id}/commit"
    FILES_FILE_ID_COPY = "/files/{file_id}/copy"
    FILES_FILE_ID_THUMBNAIL_EXTENSION = "/files/{file_id}/thumbnail.{extension}"
    FILES_FILE_ID_COLLABORATIONS = "/files/{file_id}/collaborations"
    FILES_FILE_ID_COMMENTS = "/files/{file_id}/comments"
    FILES_FILE_ID_TASKS = "/files/{file_id}/tasks"
    FILES_FILE_ID_TRASH = "/files/{file_id}/trash"
    FILES_FILE_ID_VERSIONS = "/files/{file_id}/versions"
    FILES_FILE_ID_VERSIONS_FILE_VERSION_ID = "/files/{file_id}/versions/{file_version_id}"
    FILES_FILE_ID_VERSIONS_CURRENT = "/files/{file_id}/versions/current"
    FILES_FILE_ID_METADATA = "/files/{file_id}/metadata"
    FILES_FILE_ID_METADATA_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO = "/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
    FILES_FILE_ID_METADATA_SCOPE_TEMPLATE_KEY = "/files/{file_id}/metadata/{scope}/{template_key}"
    FILES_FILE_ID_METADATA_GLOBAL_BOX_SKILLS_CARDS = "/files/{file_id}/metadata/global/boxSkillsCards"
    FILES_FILE_ID_WATERMARK = "/files/{file_id}/watermark"
    FILE_REQUESTS_FILE_REQUEST_ID = "/file_requests/{file_request_id}"
    FILE_REQUESTS_FILE_REQUEST_ID_COPY = "/file_requests/{file_request_id}/copy"
    FOLDERS_FOLDER_ID = "/folders/{folder_id}"
    FOLDERS_FOLDER_ID_ITEMS = "/folders/{folder_id}/items"
    FOLDERS = "/folders"
    FOLDERS_FOLDER_ID_COPY = "/folders/{folder_id}/copy"
    FOLDERS_FOLDER_ID_COLLABORATIONS = "/folders/{folder_id}/collaborations"
    FOLDERS_FOLDER_ID_TRASH = "/folders/{folder_id}/trash"
    FOLDERS_FOLDER_ID_METADATA = "/folders/{folder_id}/metadata"
    FOLDERS_FOLDER_ID_METADATA_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO = "/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo"
    FOLDERS_FOLDER_ID_METADATA_SCOPE_TEMPLATE_KEY = "/folders/{folder_id}/metadata/{scope}/{template_key}"
    FOLDERS_TRASH_ITEMS = "/folders/trash/items"
    FOLDERS_FOLDER_ID_WATERMARK = "/folders/{folder_id}/watermark"
    FOLDER_LOCKS = "/folder_locks"
    FOLDER_LOCKS_FOLDER_LOCK_ID = "/folder_locks/{folder_lock_id}"
    METADATA_TEMPLATES = "/metadata_templates"
    METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMA = "/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema"
    METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMAADD = "/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#add"
    METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMAUPDATE = "/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#update"
    METADATA_TEMPLATES_SCOPE_TEMPLATE_KEY_SCHEMA = "/metadata_templates/{scope}/{template_key}/schema"
    METADATA_TEMPLATES_TEMPLATE_ID = "/metadata_templates/{template_id}"
    METADATA_TEMPLATES_GLOBAL = "/metadata_templates/global"
    METADATA_TEMPLATES_ENTERPRISE = "/metadata_templates/enterprise"
    METADATA_TEMPLATES_SCHEMA = "/metadata_templates/schema"
    METADATA_TEMPLATES_SCHEMACLASSIFICATIONS = "/metadata_templates/schema#classifications"
    METADATA_CASCADE_POLICIES = "/metadata_cascade_policies"
    METADATA_CASCADE_POLICIES_METADATA_CASCADE_POLICY_ID = "/metadata_cascade_policies/{metadata_cascade_policy_id}"
    METADATA_CASCADE_POLICIES_METADATA_CASCADE_POLICY_ID_APPLY = "/metadata_cascade_policies/{metadata_cascade_policy_id}/apply"
    METADATA_QUERIES_EXECUTE_READ = "/metadata_queries/execute_read"
    COMMENTS_COMMENT_ID = "/comments/{comment_id}"
    COMMENTS = "/comments"
    COLLABORATIONS_COLLABORATION_ID = "/collaborations/{collaboration_id}"
    COLLABORATIONS = "/collaborations"
    SEARCH = "/search"
    TASKS = "/tasks"
    TASKS_TASK_ID = "/tasks/{task_id}"
    TASKS_TASK_ID_ASSIGNMENTS = "/tasks/{task_id}/assignments"
    TASK_ASSIGNMENTS = "/task_assignments"
    TASK_ASSIGNMENTS_TASK_ASSIGNMENT_ID = "/task_assignments/{task_assignment_id}"
    SHARED_ITEMS = "/shared_items"
    FILES_FILE_IDGET_SHARED_LINK = "/files/{file_id}#get_shared_link"
    FILES_FILE_IDADD_SHARED_LINK = "/files/{file_id}#add_shared_link"
    FILES_FILE_IDUPDATE_SHARED_LINK = "/files/{file_id}#update_shared_link"
    FILES_FILE_IDREMOVE_SHARED_LINK = "/files/{file_id}#remove_shared_link"
    SHARED_ITEMSFOLDERS = "/shared_items#folders"
    FOLDERS_FOLDER_IDGET_SHARED_LINK = "/folders/{folder_id}#get_shared_link"
    FOLDERS_FOLDER_IDADD_SHARED_LINK = "/folders/{folder_id}#add_shared_link"
    FOLDERS_FOLDER_IDUPDATE_SHARED_LINK = "/folders/{folder_id}#update_shared_link"
    FOLDERS_FOLDER_IDREMOVE_SHARED_LINK = "/folders/{folder_id}#remove_shared_link"
    WEB_LINKS = "/web_links"
    WEB_LINKS_WEB_LINK_ID = "/web_links/{web_link_id}"
    WEB_LINKS_WEB_LINK_ID_TRASH = "/web_links/{web_link_id}/trash"
    SHARED_ITEMSWEB_LINKS = "/shared_items#web_links"
    WEB_LINKS_WEB_LINK_IDGET_SHARED_LINK = "/web_links/{web_link_id}#get_shared_link"
    WEB_LINKS_WEB_LINK_IDADD_SHARED_LINK = "/web_links/{web_link_id}#add_shared_link"
    WEB_LINKS_WEB_LINK_IDUPDATE_SHARED_LINK = "/web_links/{web_link_id}#update_shared_link"
    WEB_LINKS_WEB_LINK_IDREMOVE_SHARED_LINK = "/web_links/{web_link_id}#remove_shared_link"
    USERS = "/users"
    USERS_ME = "/users/me"
    USERS_TERMINATE_SESSIONS = "/users/terminate_sessions"
    USERS_USER_ID = "/users/{user_id}"
    USERS_USER_ID_AVATAR = "/users/{user_id}/avatar"
    USERS_USER_ID_FOLDERS_0 = "/users/{user_id}/folders/0"
    USERS_USER_ID_EMAIL_ALIASES = "/users/{user_id}/email_aliases"
    USERS_USER_ID_EMAIL_ALIASES_EMAIL_ALIAS_ID = "/users/{user_id}/email_aliases/{email_alias_id}"
    USERS_USER_ID_MEMBERSHIPS = "/users/{user_id}/memberships"
    INVITES = "/invites"
    INVITES_INVITE_ID = "/invites/{invite_id}"
    GROUPS = "/groups"
    GROUPS_TERMINATE_SESSIONS = "/groups/terminate_sessions"
    GROUPS_GROUP_ID = "/groups/{group_id}"
    GROUPS_GROUP_ID_MEMBERSHIPS = "/groups/{group_id}/memberships"
    GROUPS_GROUP_ID_COLLABORATIONS = "/groups/{group_id}/collaborations"
    GROUP_MEMBERSHIPS = "/group_memberships"
    GROUP_MEMBERSHIPS_GROUP_MEMBERSHIP_ID = "/group_memberships/{group_membership_id}"
    WEBHOOKS = "/webhooks"
    WEBHOOKS_WEBHOOK_ID = "/webhooks/{webhook_id}"
    SKILL_INVOCATIONS_SKILL_ID = "/skill_invocations/{skill_id}"
    EVENTS = "/events"
    COLLECTIONS = "/collections"
    COLLECTIONS_COLLECTION_ID_ITEMS = "/collections/{collection_id}/items"
    RECENT_ITEMS = "/recent_items"
    RETENTION_POLICIES = "/retention_policies"
    RETENTION_POLICIES_RETENTION_POLICY_ID = "/retention_policies/{retention_policy_id}"
    RETENTION_POLICIES_RETENTION_POLICY_ID_ASSIGNMENTS = "/retention_policies/{retention_policy_id}/assignments"
    RETENTION_POLICY_ASSIGNMENTS = "/retention_policy_assignments"
    RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID = "/retention_policy_assignments/{retention_policy_assignment_id}"
    RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID_FILES_UNDER_RETENTION = "/retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention"
    RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID_FILE_VERSIONS_UNDER_RETENTION = "/retention_policy_assignments/{retention_policy_assignment_id}/file_versions_under_retention"
    LEGAL_HOLD_POLICIES = "/legal_hold_policies"
    LEGAL_HOLD_POLICIES_LEGAL_HOLD_POLICY_ID = "/legal_hold_policies/{legal_hold_policy_id}"
    LEGAL_HOLD_POLICY_ASSIGNMENTS = "/legal_hold_policy_assignments"
    LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID = "/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}"
    LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID_FILES_ON_HOLD = "/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold"
    FILE_VERSION_RETENTIONS = "/file_version_retentions"
    LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID_FILE_VERSIONS_ON_HOLD = "/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/file_versions_on_hold"
    FILE_VERSION_RETENTIONS_FILE_VERSION_RETENTION_ID = "/file_version_retentions/{file_version_retention_id}"
    FILE_VERSION_LEGAL_HOLDS_FILE_VERSION_LEGAL_HOLD_ID = "/file_version_legal_holds/{file_version_legal_hold_id}"
    FILE_VERSION_LEGAL_HOLDS = "/file_version_legal_holds"
    SHIELD_INFORMATION_BARRIERS_SHIELD_INFORMATION_BARRIER_ID = "/shield_information_barriers/{shield_information_barrier_id}"
    SHIELD_INFORMATION_BARRIERS_CHANGE_STATUS = "/shield_information_barriers/change_status"
    SHIELD_INFORMATION_BARRIERS = "/shield_information_barriers"
    SHIELD_INFORMATION_BARRIER_REPORTS = "/shield_information_barrier_reports"
    SHIELD_INFORMATION_BARRIER_REPORTS_SHIELD_INFORMATION_BARRIER_REPORT_ID = "/shield_information_barrier_reports/{shield_information_barrier_report_id}"
    SHIELD_INFORMATION_BARRIER_SEGMENTS_SHIELD_INFORMATION_BARRIER_SEGMENT_ID = "/shield_information_barrier_segments/{shield_information_barrier_segment_id}"
    SHIELD_INFORMATION_BARRIER_SEGMENTS = "/shield_information_barrier_segments"
    SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS_SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER_ID = "/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}"
    SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS = "/shield_information_barrier_segment_members"
    SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS_SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTION_ID = "/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}"
    SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS = "/shield_information_barrier_segment_restrictions"
    DEVICE_PINNERS_DEVICE_PINNER_ID = "/device_pinners/{device_pinner_id}"
    ENTERPRISES_ENTERPRISE_ID_DEVICE_PINNERS = "/enterprises/{enterprise_id}/device_pinners"
    TERMS_OF_SERVICES = "/terms_of_services"
    TERMS_OF_SERVICES_TERMS_OF_SERVICE_ID = "/terms_of_services/{terms_of_service_id}"
    TERMS_OF_SERVICE_USER_STATUSES = "/terms_of_service_user_statuses"
    TERMS_OF_SERVICE_USER_STATUSES_TERMS_OF_SERVICE_USER_STATUS_ID = "/terms_of_service_user_statuses/{terms_of_service_user_status_id}"
    COLLABORATION_WHITELIST_ENTRIES = "/collaboration_whitelist_entries"
    COLLABORATION_WHITELIST_ENTRIES_COLLABORATION_WHITELIST_ENTRY_ID = "/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}"
    COLLABORATION_WHITELIST_EXEMPT_TARGETS = "/collaboration_whitelist_exempt_targets"
    COLLABORATION_WHITELIST_EXEMPT_TARGETS_COLLABORATION_WHITELIST_EXEMPT_TARGET_ID = "/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}"
    STORAGE_POLICIES = "/storage_policies"
    STORAGE_POLICIES_STORAGE_POLICY_ID = "/storage_policies/{storage_policy_id}"
    STORAGE_POLICY_ASSIGNMENTS = "/storage_policy_assignments"
    STORAGE_POLICY_ASSIGNMENTS_STORAGE_POLICY_ASSIGNMENT_ID = "/storage_policy_assignments/{storage_policy_assignment_id}"
    ZIP_DOWNLOADS = "/zip_downloads"
    ZIP_DOWNLOADS_ZIP_DOWNLOAD_ID_CONTENT = "/zip_downloads/{zip_download_id}/content"
    ZIP_DOWNLOADS_ZIP_DOWNLOAD_ID_STATUS = "/zip_downloads/{zip_download_id}/status"
    SIGN_REQUESTS_SIGN_REQUEST_ID_CANCEL = "/sign_requests/{sign_request_id}/cancel"
    SIGN_REQUESTS_SIGN_REQUEST_ID_RESEND = "/sign_requests/{sign_request_id}/resend"
    SIGN_REQUESTS_SIGN_REQUEST_ID = "/sign_requests/{sign_request_id}"
    SIGN_REQUESTS = "/sign_requests"
    WORKFLOWS = "/workflows"
    WORKFLOWS_WORKFLOW_ID_START = "/workflows/{workflow_id}/start"
    SIGN_TEMPLATES = "/sign_templates"
    SIGN_TEMPLATES_TEMPLATE_ID = "/sign_templates/{template_id}"
    INTEGRATION_MAPPINGS_SLACK = "/integration_mappings/slack"
    INTEGRATION_MAPPINGS_SLACK_INTEGRATION_MAPPING_ID = "/integration_mappings/slack/{integration_mapping_id}"
