import typing_extensions

from box_python_sdk.paths import PathValues
from box_python_sdk.apis.paths.authorize import Authorize
from box_python_sdk.apis.paths.oauth2_token import Oauth2Token
from box_python_sdk.apis.paths.oauth2_tokenrefresh import Oauth2Tokenrefresh
from box_python_sdk.apis.paths.oauth2_revoke import Oauth2Revoke
from box_python_sdk.apis.paths.files_file_id import FilesFileId
from box_python_sdk.apis.paths.files_file_id_content import FilesFileIdContent
from box_python_sdk.apis.paths.files_content import FilesContent
from box_python_sdk.apis.paths.files_upload_sessions import FilesUploadSessions
from box_python_sdk.apis.paths.files_file_id_upload_sessions import FilesFileIdUploadSessions
from box_python_sdk.apis.paths.files_upload_sessions_upload_session_id import FilesUploadSessionsUploadSessionId
from box_python_sdk.apis.paths.files_upload_sessions_upload_session_id_parts import FilesUploadSessionsUploadSessionIdParts
from box_python_sdk.apis.paths.files_upload_sessions_upload_session_id_commit import FilesUploadSessionsUploadSessionIdCommit
from box_python_sdk.apis.paths.files_file_id_copy import FilesFileIdCopy
from box_python_sdk.apis.paths.files_file_id_thumbnail_extension import FilesFileIdThumbnailExtension
from box_python_sdk.apis.paths.files_file_id_collaborations import FilesFileIdCollaborations
from box_python_sdk.apis.paths.files_file_id_comments import FilesFileIdComments
from box_python_sdk.apis.paths.files_file_id_tasks import FilesFileIdTasks
from box_python_sdk.apis.paths.files_file_id_trash import FilesFileIdTrash
from box_python_sdk.apis.paths.files_file_id_versions import FilesFileIdVersions
from box_python_sdk.apis.paths.files_file_id_versions_file_version_id import FilesFileIdVersionsFileVersionId
from box_python_sdk.apis.paths.files_file_id_versions_current import FilesFileIdVersionsCurrent
from box_python_sdk.apis.paths.files_file_id_metadata import FilesFileIdMetadata
from box_python_sdk.apis.paths.files_file_id_metadata_enterprise_security_classification_6_vm_vochw_uwo import FilesFileIdMetadataEnterpriseSecurityClassification6VMVochwUWo
from box_python_sdk.apis.paths.files_file_id_metadata_scope_template_key import FilesFileIdMetadataScopeTemplateKey
from box_python_sdk.apis.paths.files_file_id_metadata_global_box_skills_cards import FilesFileIdMetadataGlobalBoxSkillsCards
from box_python_sdk.apis.paths.files_file_id_watermark import FilesFileIdWatermark
from box_python_sdk.apis.paths.file_requests_file_request_id import FileRequestsFileRequestId
from box_python_sdk.apis.paths.file_requests_file_request_id_copy import FileRequestsFileRequestIdCopy
from box_python_sdk.apis.paths.folders_folder_id import FoldersFolderId
from box_python_sdk.apis.paths.folders_folder_id_items import FoldersFolderIdItems
from box_python_sdk.apis.paths.folders import Folders
from box_python_sdk.apis.paths.folders_folder_id_copy import FoldersFolderIdCopy
from box_python_sdk.apis.paths.folders_folder_id_collaborations import FoldersFolderIdCollaborations
from box_python_sdk.apis.paths.folders_folder_id_trash import FoldersFolderIdTrash
from box_python_sdk.apis.paths.folders_folder_id_metadata import FoldersFolderIdMetadata
from box_python_sdk.apis.paths.folders_folder_id_metadata_enterprise_security_classification_6_vm_vochw_uwo import FoldersFolderIdMetadataEnterpriseSecurityClassification6VMVochwUWo
from box_python_sdk.apis.paths.folders_folder_id_metadata_scope_template_key import FoldersFolderIdMetadataScopeTemplateKey
from box_python_sdk.apis.paths.folders_trash_items import FoldersTrashItems
from box_python_sdk.apis.paths.folders_folder_id_watermark import FoldersFolderIdWatermark
from box_python_sdk.apis.paths.folder_locks import FolderLocks
from box_python_sdk.apis.paths.folder_locks_folder_lock_id import FolderLocksFolderLockId
from box_python_sdk.apis.paths.metadata_templates import MetadataTemplates
from box_python_sdk.apis.paths.metadata_templates_enterprise_security_classification_6_vm_vochw_uwo_schema import MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchema
from box_python_sdk.apis.paths.metadata_templates_enterprise_security_classification_6_vm_vochw_uwo_schemaadd import MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchemaadd
from box_python_sdk.apis.paths.metadata_templates_enterprise_security_classification_6_vm_vochw_uwo_schemaupdate import MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchemaupdate
from box_python_sdk.apis.paths.metadata_templates_scope_template_key_schema import MetadataTemplatesScopeTemplateKeySchema
from box_python_sdk.apis.paths.metadata_templates_template_id import MetadataTemplatesTemplateId
from box_python_sdk.apis.paths.metadata_templates_global import MetadataTemplatesGlobal
from box_python_sdk.apis.paths.metadata_templates_enterprise import MetadataTemplatesEnterprise
from box_python_sdk.apis.paths.metadata_templates_schema import MetadataTemplatesSchema
from box_python_sdk.apis.paths.metadata_templates_schemaclassifications import MetadataTemplatesSchemaclassifications
from box_python_sdk.apis.paths.metadata_cascade_policies import MetadataCascadePolicies
from box_python_sdk.apis.paths.metadata_cascade_policies_metadata_cascade_policy_id import MetadataCascadePoliciesMetadataCascadePolicyId
from box_python_sdk.apis.paths.metadata_cascade_policies_metadata_cascade_policy_id_apply import MetadataCascadePoliciesMetadataCascadePolicyIdApply
from box_python_sdk.apis.paths.metadata_queries_execute_read import MetadataQueriesExecuteRead
from box_python_sdk.apis.paths.comments_comment_id import CommentsCommentId
from box_python_sdk.apis.paths.comments import Comments
from box_python_sdk.apis.paths.collaborations_collaboration_id import CollaborationsCollaborationId
from box_python_sdk.apis.paths.collaborations import Collaborations
from box_python_sdk.apis.paths.search import Search
from box_python_sdk.apis.paths.tasks import Tasks
from box_python_sdk.apis.paths.tasks_task_id import TasksTaskId
from box_python_sdk.apis.paths.tasks_task_id_assignments import TasksTaskIdAssignments
from box_python_sdk.apis.paths.task_assignments import TaskAssignments
from box_python_sdk.apis.paths.task_assignments_task_assignment_id import TaskAssignmentsTaskAssignmentId
from box_python_sdk.apis.paths.shared_items import SharedItems
from box_python_sdk.apis.paths.files_file_idget_shared_link import FilesFileIdgetSharedLink
from box_python_sdk.apis.paths.files_file_idadd_shared_link import FilesFileIdaddSharedLink
from box_python_sdk.apis.paths.files_file_idupdate_shared_link import FilesFileIdupdateSharedLink
from box_python_sdk.apis.paths.files_file_idremove_shared_link import FilesFileIdremoveSharedLink
from box_python_sdk.apis.paths.shared_itemsfolders import SharedItemsfolders
from box_python_sdk.apis.paths.folders_folder_idget_shared_link import FoldersFolderIdgetSharedLink
from box_python_sdk.apis.paths.folders_folder_idadd_shared_link import FoldersFolderIdaddSharedLink
from box_python_sdk.apis.paths.folders_folder_idupdate_shared_link import FoldersFolderIdupdateSharedLink
from box_python_sdk.apis.paths.folders_folder_idremove_shared_link import FoldersFolderIdremoveSharedLink
from box_python_sdk.apis.paths.web_links import WebLinks
from box_python_sdk.apis.paths.web_links_web_link_id import WebLinksWebLinkId
from box_python_sdk.apis.paths.web_links_web_link_id_trash import WebLinksWebLinkIdTrash
from box_python_sdk.apis.paths.shared_itemsweb_links import SharedItemswebLinks
from box_python_sdk.apis.paths.web_links_web_link_idget_shared_link import WebLinksWebLinkIdgetSharedLink
from box_python_sdk.apis.paths.web_links_web_link_idadd_shared_link import WebLinksWebLinkIdaddSharedLink
from box_python_sdk.apis.paths.web_links_web_link_idupdate_shared_link import WebLinksWebLinkIdupdateSharedLink
from box_python_sdk.apis.paths.web_links_web_link_idremove_shared_link import WebLinksWebLinkIdremoveSharedLink
from box_python_sdk.apis.paths.users import Users
from box_python_sdk.apis.paths.users_me import UsersMe
from box_python_sdk.apis.paths.users_terminate_sessions import UsersTerminateSessions
from box_python_sdk.apis.paths.users_user_id import UsersUserId
from box_python_sdk.apis.paths.users_user_id_avatar import UsersUserIdAvatar
from box_python_sdk.apis.paths.users_user_id_folders_0 import UsersUserIdFolders0
from box_python_sdk.apis.paths.users_user_id_email_aliases import UsersUserIdEmailAliases
from box_python_sdk.apis.paths.users_user_id_email_aliases_email_alias_id import UsersUserIdEmailAliasesEmailAliasId
from box_python_sdk.apis.paths.users_user_id_memberships import UsersUserIdMemberships
from box_python_sdk.apis.paths.invites import Invites
from box_python_sdk.apis.paths.invites_invite_id import InvitesInviteId
from box_python_sdk.apis.paths.groups import Groups
from box_python_sdk.apis.paths.groups_terminate_sessions import GroupsTerminateSessions
from box_python_sdk.apis.paths.groups_group_id import GroupsGroupId
from box_python_sdk.apis.paths.groups_group_id_memberships import GroupsGroupIdMemberships
from box_python_sdk.apis.paths.groups_group_id_collaborations import GroupsGroupIdCollaborations
from box_python_sdk.apis.paths.group_memberships import GroupMemberships
from box_python_sdk.apis.paths.group_memberships_group_membership_id import GroupMembershipsGroupMembershipId
from box_python_sdk.apis.paths.webhooks import Webhooks
from box_python_sdk.apis.paths.webhooks_webhook_id import WebhooksWebhookId
from box_python_sdk.apis.paths.skill_invocations_skill_id import SkillInvocationsSkillId
from box_python_sdk.apis.paths.events import Events
from box_python_sdk.apis.paths.collections import Collections
from box_python_sdk.apis.paths.collections_collection_id_items import CollectionsCollectionIdItems
from box_python_sdk.apis.paths.recent_items import RecentItems
from box_python_sdk.apis.paths.retention_policies import RetentionPolicies
from box_python_sdk.apis.paths.retention_policies_retention_policy_id import RetentionPoliciesRetentionPolicyId
from box_python_sdk.apis.paths.retention_policies_retention_policy_id_assignments import RetentionPoliciesRetentionPolicyIdAssignments
from box_python_sdk.apis.paths.retention_policy_assignments import RetentionPolicyAssignments
from box_python_sdk.apis.paths.retention_policy_assignments_retention_policy_assignment_id import RetentionPolicyAssignmentsRetentionPolicyAssignmentId
from box_python_sdk.apis.paths.retention_policy_assignments_retention_policy_assignment_id_files_under_retention import RetentionPolicyAssignmentsRetentionPolicyAssignmentIdFilesUnderRetention
from box_python_sdk.apis.paths.retention_policy_assignments_retention_policy_assignment_id_file_versions_under_retention import RetentionPolicyAssignmentsRetentionPolicyAssignmentIdFileVersionsUnderRetention
from box_python_sdk.apis.paths.legal_hold_policies import LegalHoldPolicies
from box_python_sdk.apis.paths.legal_hold_policies_legal_hold_policy_id import LegalHoldPoliciesLegalHoldPolicyId
from box_python_sdk.apis.paths.legal_hold_policy_assignments import LegalHoldPolicyAssignments
from box_python_sdk.apis.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id import LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentId
from box_python_sdk.apis.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id_files_on_hold import LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentIdFilesOnHold
from box_python_sdk.apis.paths.file_version_retentions import FileVersionRetentions
from box_python_sdk.apis.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id_file_versions_on_hold import LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentIdFileVersionsOnHold
from box_python_sdk.apis.paths.file_version_retentions_file_version_retention_id import FileVersionRetentionsFileVersionRetentionId
from box_python_sdk.apis.paths.file_version_legal_holds_file_version_legal_hold_id import FileVersionLegalHoldsFileVersionLegalHoldId
from box_python_sdk.apis.paths.file_version_legal_holds import FileVersionLegalHolds
from box_python_sdk.apis.paths.shield_information_barriers_shield_information_barrier_id import ShieldInformationBarriersShieldInformationBarrierId
from box_python_sdk.apis.paths.shield_information_barriers_change_status import ShieldInformationBarriersChangeStatus
from box_python_sdk.apis.paths.shield_information_barriers import ShieldInformationBarriers
from box_python_sdk.apis.paths.shield_information_barrier_reports import ShieldInformationBarrierReports
from box_python_sdk.apis.paths.shield_information_barrier_reports_shield_information_barrier_report_id import ShieldInformationBarrierReportsShieldInformationBarrierReportId
from box_python_sdk.apis.paths.shield_information_barrier_segments_shield_information_barrier_segment_id import ShieldInformationBarrierSegmentsShieldInformationBarrierSegmentId
from box_python_sdk.apis.paths.shield_information_barrier_segments import ShieldInformationBarrierSegments
from box_python_sdk.apis.paths.shield_information_barrier_segment_members_shield_information_barrier_segment_member_id import ShieldInformationBarrierSegmentMembersShieldInformationBarrierSegmentMemberId
from box_python_sdk.apis.paths.shield_information_barrier_segment_members import ShieldInformationBarrierSegmentMembers
from box_python_sdk.apis.paths.shield_information_barrier_segment_restrictions_shield_information_barrier_segment_restriction_id import ShieldInformationBarrierSegmentRestrictionsShieldInformationBarrierSegmentRestrictionId
from box_python_sdk.apis.paths.shield_information_barrier_segment_restrictions import ShieldInformationBarrierSegmentRestrictions
from box_python_sdk.apis.paths.device_pinners_device_pinner_id import DevicePinnersDevicePinnerId
from box_python_sdk.apis.paths.enterprises_enterprise_id_device_pinners import EnterprisesEnterpriseIdDevicePinners
from box_python_sdk.apis.paths.terms_of_services import TermsOfServices
from box_python_sdk.apis.paths.terms_of_services_terms_of_service_id import TermsOfServicesTermsOfServiceId
from box_python_sdk.apis.paths.terms_of_service_user_statuses import TermsOfServiceUserStatuses
from box_python_sdk.apis.paths.terms_of_service_user_statuses_terms_of_service_user_status_id import TermsOfServiceUserStatusesTermsOfServiceUserStatusId
from box_python_sdk.apis.paths.collaboration_whitelist_entries import CollaborationWhitelistEntries
from box_python_sdk.apis.paths.collaboration_whitelist_entries_collaboration_whitelist_entry_id import CollaborationWhitelistEntriesCollaborationWhitelistEntryId
from box_python_sdk.apis.paths.collaboration_whitelist_exempt_targets import CollaborationWhitelistExemptTargets
from box_python_sdk.apis.paths.collaboration_whitelist_exempt_targets_collaboration_whitelist_exempt_target_id import CollaborationWhitelistExemptTargetsCollaborationWhitelistExemptTargetId
from box_python_sdk.apis.paths.storage_policies import StoragePolicies
from box_python_sdk.apis.paths.storage_policies_storage_policy_id import StoragePoliciesStoragePolicyId
from box_python_sdk.apis.paths.storage_policy_assignments import StoragePolicyAssignments
from box_python_sdk.apis.paths.storage_policy_assignments_storage_policy_assignment_id import StoragePolicyAssignmentsStoragePolicyAssignmentId
from box_python_sdk.apis.paths.zip_downloads import ZipDownloads
from box_python_sdk.apis.paths.zip_downloads_zip_download_id_content import ZipDownloadsZipDownloadIdContent
from box_python_sdk.apis.paths.zip_downloads_zip_download_id_status import ZipDownloadsZipDownloadIdStatus
from box_python_sdk.apis.paths.sign_requests_sign_request_id_cancel import SignRequestsSignRequestIdCancel
from box_python_sdk.apis.paths.sign_requests_sign_request_id_resend import SignRequestsSignRequestIdResend
from box_python_sdk.apis.paths.sign_requests_sign_request_id import SignRequestsSignRequestId
from box_python_sdk.apis.paths.sign_requests import SignRequests
from box_python_sdk.apis.paths.workflows import Workflows
from box_python_sdk.apis.paths.workflows_workflow_id_start import WorkflowsWorkflowIdStart
from box_python_sdk.apis.paths.sign_templates import SignTemplates
from box_python_sdk.apis.paths.sign_templates_template_id import SignTemplatesTemplateId
from box_python_sdk.apis.paths.integration_mappings_slack import IntegrationMappingsSlack
from box_python_sdk.apis.paths.integration_mappings_slack_integration_mapping_id import IntegrationMappingsSlackIntegrationMappingId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTHORIZE: Authorize,
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.OAUTH2_TOKENREFRESH: Oauth2Tokenrefresh,
        PathValues.OAUTH2_REVOKE: Oauth2Revoke,
        PathValues.FILES_FILE_ID: FilesFileId,
        PathValues.FILES_FILE_ID_CONTENT: FilesFileIdContent,
        PathValues.FILES_CONTENT: FilesContent,
        PathValues.FILES_UPLOAD_SESSIONS: FilesUploadSessions,
        PathValues.FILES_FILE_ID_UPLOAD_SESSIONS: FilesFileIdUploadSessions,
        PathValues.FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID: FilesUploadSessionsUploadSessionId,
        PathValues.FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID_PARTS: FilesUploadSessionsUploadSessionIdParts,
        PathValues.FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID_COMMIT: FilesUploadSessionsUploadSessionIdCommit,
        PathValues.FILES_FILE_ID_COPY: FilesFileIdCopy,
        PathValues.FILES_FILE_ID_THUMBNAIL_EXTENSION: FilesFileIdThumbnailExtension,
        PathValues.FILES_FILE_ID_COLLABORATIONS: FilesFileIdCollaborations,
        PathValues.FILES_FILE_ID_COMMENTS: FilesFileIdComments,
        PathValues.FILES_FILE_ID_TASKS: FilesFileIdTasks,
        PathValues.FILES_FILE_ID_TRASH: FilesFileIdTrash,
        PathValues.FILES_FILE_ID_VERSIONS: FilesFileIdVersions,
        PathValues.FILES_FILE_ID_VERSIONS_FILE_VERSION_ID: FilesFileIdVersionsFileVersionId,
        PathValues.FILES_FILE_ID_VERSIONS_CURRENT: FilesFileIdVersionsCurrent,
        PathValues.FILES_FILE_ID_METADATA: FilesFileIdMetadata,
        PathValues.FILES_FILE_ID_METADATA_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO: FilesFileIdMetadataEnterpriseSecurityClassification6VMVochwUWo,
        PathValues.FILES_FILE_ID_METADATA_SCOPE_TEMPLATE_KEY: FilesFileIdMetadataScopeTemplateKey,
        PathValues.FILES_FILE_ID_METADATA_GLOBAL_BOX_SKILLS_CARDS: FilesFileIdMetadataGlobalBoxSkillsCards,
        PathValues.FILES_FILE_ID_WATERMARK: FilesFileIdWatermark,
        PathValues.FILE_REQUESTS_FILE_REQUEST_ID: FileRequestsFileRequestId,
        PathValues.FILE_REQUESTS_FILE_REQUEST_ID_COPY: FileRequestsFileRequestIdCopy,
        PathValues.FOLDERS_FOLDER_ID: FoldersFolderId,
        PathValues.FOLDERS_FOLDER_ID_ITEMS: FoldersFolderIdItems,
        PathValues.FOLDERS: Folders,
        PathValues.FOLDERS_FOLDER_ID_COPY: FoldersFolderIdCopy,
        PathValues.FOLDERS_FOLDER_ID_COLLABORATIONS: FoldersFolderIdCollaborations,
        PathValues.FOLDERS_FOLDER_ID_TRASH: FoldersFolderIdTrash,
        PathValues.FOLDERS_FOLDER_ID_METADATA: FoldersFolderIdMetadata,
        PathValues.FOLDERS_FOLDER_ID_METADATA_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO: FoldersFolderIdMetadataEnterpriseSecurityClassification6VMVochwUWo,
        PathValues.FOLDERS_FOLDER_ID_METADATA_SCOPE_TEMPLATE_KEY: FoldersFolderIdMetadataScopeTemplateKey,
        PathValues.FOLDERS_TRASH_ITEMS: FoldersTrashItems,
        PathValues.FOLDERS_FOLDER_ID_WATERMARK: FoldersFolderIdWatermark,
        PathValues.FOLDER_LOCKS: FolderLocks,
        PathValues.FOLDER_LOCKS_FOLDER_LOCK_ID: FolderLocksFolderLockId,
        PathValues.METADATA_TEMPLATES: MetadataTemplates,
        PathValues.METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMA: MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchema,
        PathValues.METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMAADD: MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchemaadd,
        PathValues.METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMAUPDATE: MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchemaupdate,
        PathValues.METADATA_TEMPLATES_SCOPE_TEMPLATE_KEY_SCHEMA: MetadataTemplatesScopeTemplateKeySchema,
        PathValues.METADATA_TEMPLATES_TEMPLATE_ID: MetadataTemplatesTemplateId,
        PathValues.METADATA_TEMPLATES_GLOBAL: MetadataTemplatesGlobal,
        PathValues.METADATA_TEMPLATES_ENTERPRISE: MetadataTemplatesEnterprise,
        PathValues.METADATA_TEMPLATES_SCHEMA: MetadataTemplatesSchema,
        PathValues.METADATA_TEMPLATES_SCHEMACLASSIFICATIONS: MetadataTemplatesSchemaclassifications,
        PathValues.METADATA_CASCADE_POLICIES: MetadataCascadePolicies,
        PathValues.METADATA_CASCADE_POLICIES_METADATA_CASCADE_POLICY_ID: MetadataCascadePoliciesMetadataCascadePolicyId,
        PathValues.METADATA_CASCADE_POLICIES_METADATA_CASCADE_POLICY_ID_APPLY: MetadataCascadePoliciesMetadataCascadePolicyIdApply,
        PathValues.METADATA_QUERIES_EXECUTE_READ: MetadataQueriesExecuteRead,
        PathValues.COMMENTS_COMMENT_ID: CommentsCommentId,
        PathValues.COMMENTS: Comments,
        PathValues.COLLABORATIONS_COLLABORATION_ID: CollaborationsCollaborationId,
        PathValues.COLLABORATIONS: Collaborations,
        PathValues.SEARCH: Search,
        PathValues.TASKS: Tasks,
        PathValues.TASKS_TASK_ID: TasksTaskId,
        PathValues.TASKS_TASK_ID_ASSIGNMENTS: TasksTaskIdAssignments,
        PathValues.TASK_ASSIGNMENTS: TaskAssignments,
        PathValues.TASK_ASSIGNMENTS_TASK_ASSIGNMENT_ID: TaskAssignmentsTaskAssignmentId,
        PathValues.SHARED_ITEMS: SharedItems,
        PathValues.FILES_FILE_IDGET_SHARED_LINK: FilesFileIdgetSharedLink,
        PathValues.FILES_FILE_IDADD_SHARED_LINK: FilesFileIdaddSharedLink,
        PathValues.FILES_FILE_IDUPDATE_SHARED_LINK: FilesFileIdupdateSharedLink,
        PathValues.FILES_FILE_IDREMOVE_SHARED_LINK: FilesFileIdremoveSharedLink,
        PathValues.SHARED_ITEMSFOLDERS: SharedItemsfolders,
        PathValues.FOLDERS_FOLDER_IDGET_SHARED_LINK: FoldersFolderIdgetSharedLink,
        PathValues.FOLDERS_FOLDER_IDADD_SHARED_LINK: FoldersFolderIdaddSharedLink,
        PathValues.FOLDERS_FOLDER_IDUPDATE_SHARED_LINK: FoldersFolderIdupdateSharedLink,
        PathValues.FOLDERS_FOLDER_IDREMOVE_SHARED_LINK: FoldersFolderIdremoveSharedLink,
        PathValues.WEB_LINKS: WebLinks,
        PathValues.WEB_LINKS_WEB_LINK_ID: WebLinksWebLinkId,
        PathValues.WEB_LINKS_WEB_LINK_ID_TRASH: WebLinksWebLinkIdTrash,
        PathValues.SHARED_ITEMSWEB_LINKS: SharedItemswebLinks,
        PathValues.WEB_LINKS_WEB_LINK_IDGET_SHARED_LINK: WebLinksWebLinkIdgetSharedLink,
        PathValues.WEB_LINKS_WEB_LINK_IDADD_SHARED_LINK: WebLinksWebLinkIdaddSharedLink,
        PathValues.WEB_LINKS_WEB_LINK_IDUPDATE_SHARED_LINK: WebLinksWebLinkIdupdateSharedLink,
        PathValues.WEB_LINKS_WEB_LINK_IDREMOVE_SHARED_LINK: WebLinksWebLinkIdremoveSharedLink,
        PathValues.USERS: Users,
        PathValues.USERS_ME: UsersMe,
        PathValues.USERS_TERMINATE_SESSIONS: UsersTerminateSessions,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_AVATAR: UsersUserIdAvatar,
        PathValues.USERS_USER_ID_FOLDERS_0: UsersUserIdFolders0,
        PathValues.USERS_USER_ID_EMAIL_ALIASES: UsersUserIdEmailAliases,
        PathValues.USERS_USER_ID_EMAIL_ALIASES_EMAIL_ALIAS_ID: UsersUserIdEmailAliasesEmailAliasId,
        PathValues.USERS_USER_ID_MEMBERSHIPS: UsersUserIdMemberships,
        PathValues.INVITES: Invites,
        PathValues.INVITES_INVITE_ID: InvitesInviteId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_TERMINATE_SESSIONS: GroupsTerminateSessions,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS_GROUP_ID_MEMBERSHIPS: GroupsGroupIdMemberships,
        PathValues.GROUPS_GROUP_ID_COLLABORATIONS: GroupsGroupIdCollaborations,
        PathValues.GROUP_MEMBERSHIPS: GroupMemberships,
        PathValues.GROUP_MEMBERSHIPS_GROUP_MEMBERSHIP_ID: GroupMembershipsGroupMembershipId,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
        PathValues.SKILL_INVOCATIONS_SKILL_ID: SkillInvocationsSkillId,
        PathValues.EVENTS: Events,
        PathValues.COLLECTIONS: Collections,
        PathValues.COLLECTIONS_COLLECTION_ID_ITEMS: CollectionsCollectionIdItems,
        PathValues.RECENT_ITEMS: RecentItems,
        PathValues.RETENTION_POLICIES: RetentionPolicies,
        PathValues.RETENTION_POLICIES_RETENTION_POLICY_ID: RetentionPoliciesRetentionPolicyId,
        PathValues.RETENTION_POLICIES_RETENTION_POLICY_ID_ASSIGNMENTS: RetentionPoliciesRetentionPolicyIdAssignments,
        PathValues.RETENTION_POLICY_ASSIGNMENTS: RetentionPolicyAssignments,
        PathValues.RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID: RetentionPolicyAssignmentsRetentionPolicyAssignmentId,
        PathValues.RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID_FILES_UNDER_RETENTION: RetentionPolicyAssignmentsRetentionPolicyAssignmentIdFilesUnderRetention,
        PathValues.RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID_FILE_VERSIONS_UNDER_RETENTION: RetentionPolicyAssignmentsRetentionPolicyAssignmentIdFileVersionsUnderRetention,
        PathValues.LEGAL_HOLD_POLICIES: LegalHoldPolicies,
        PathValues.LEGAL_HOLD_POLICIES_LEGAL_HOLD_POLICY_ID: LegalHoldPoliciesLegalHoldPolicyId,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS: LegalHoldPolicyAssignments,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID: LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentId,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID_FILES_ON_HOLD: LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentIdFilesOnHold,
        PathValues.FILE_VERSION_RETENTIONS: FileVersionRetentions,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID_FILE_VERSIONS_ON_HOLD: LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentIdFileVersionsOnHold,
        PathValues.FILE_VERSION_RETENTIONS_FILE_VERSION_RETENTION_ID: FileVersionRetentionsFileVersionRetentionId,
        PathValues.FILE_VERSION_LEGAL_HOLDS_FILE_VERSION_LEGAL_HOLD_ID: FileVersionLegalHoldsFileVersionLegalHoldId,
        PathValues.FILE_VERSION_LEGAL_HOLDS: FileVersionLegalHolds,
        PathValues.SHIELD_INFORMATION_BARRIERS_SHIELD_INFORMATION_BARRIER_ID: ShieldInformationBarriersShieldInformationBarrierId,
        PathValues.SHIELD_INFORMATION_BARRIERS_CHANGE_STATUS: ShieldInformationBarriersChangeStatus,
        PathValues.SHIELD_INFORMATION_BARRIERS: ShieldInformationBarriers,
        PathValues.SHIELD_INFORMATION_BARRIER_REPORTS: ShieldInformationBarrierReports,
        PathValues.SHIELD_INFORMATION_BARRIER_REPORTS_SHIELD_INFORMATION_BARRIER_REPORT_ID: ShieldInformationBarrierReportsShieldInformationBarrierReportId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENTS_SHIELD_INFORMATION_BARRIER_SEGMENT_ID: ShieldInformationBarrierSegmentsShieldInformationBarrierSegmentId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENTS: ShieldInformationBarrierSegments,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS_SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER_ID: ShieldInformationBarrierSegmentMembersShieldInformationBarrierSegmentMemberId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS: ShieldInformationBarrierSegmentMembers,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS_SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTION_ID: ShieldInformationBarrierSegmentRestrictionsShieldInformationBarrierSegmentRestrictionId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS: ShieldInformationBarrierSegmentRestrictions,
        PathValues.DEVICE_PINNERS_DEVICE_PINNER_ID: DevicePinnersDevicePinnerId,
        PathValues.ENTERPRISES_ENTERPRISE_ID_DEVICE_PINNERS: EnterprisesEnterpriseIdDevicePinners,
        PathValues.TERMS_OF_SERVICES: TermsOfServices,
        PathValues.TERMS_OF_SERVICES_TERMS_OF_SERVICE_ID: TermsOfServicesTermsOfServiceId,
        PathValues.TERMS_OF_SERVICE_USER_STATUSES: TermsOfServiceUserStatuses,
        PathValues.TERMS_OF_SERVICE_USER_STATUSES_TERMS_OF_SERVICE_USER_STATUS_ID: TermsOfServiceUserStatusesTermsOfServiceUserStatusId,
        PathValues.COLLABORATION_WHITELIST_ENTRIES: CollaborationWhitelistEntries,
        PathValues.COLLABORATION_WHITELIST_ENTRIES_COLLABORATION_WHITELIST_ENTRY_ID: CollaborationWhitelistEntriesCollaborationWhitelistEntryId,
        PathValues.COLLABORATION_WHITELIST_EXEMPT_TARGETS: CollaborationWhitelistExemptTargets,
        PathValues.COLLABORATION_WHITELIST_EXEMPT_TARGETS_COLLABORATION_WHITELIST_EXEMPT_TARGET_ID: CollaborationWhitelistExemptTargetsCollaborationWhitelistExemptTargetId,
        PathValues.STORAGE_POLICIES: StoragePolicies,
        PathValues.STORAGE_POLICIES_STORAGE_POLICY_ID: StoragePoliciesStoragePolicyId,
        PathValues.STORAGE_POLICY_ASSIGNMENTS: StoragePolicyAssignments,
        PathValues.STORAGE_POLICY_ASSIGNMENTS_STORAGE_POLICY_ASSIGNMENT_ID: StoragePolicyAssignmentsStoragePolicyAssignmentId,
        PathValues.ZIP_DOWNLOADS: ZipDownloads,
        PathValues.ZIP_DOWNLOADS_ZIP_DOWNLOAD_ID_CONTENT: ZipDownloadsZipDownloadIdContent,
        PathValues.ZIP_DOWNLOADS_ZIP_DOWNLOAD_ID_STATUS: ZipDownloadsZipDownloadIdStatus,
        PathValues.SIGN_REQUESTS_SIGN_REQUEST_ID_CANCEL: SignRequestsSignRequestIdCancel,
        PathValues.SIGN_REQUESTS_SIGN_REQUEST_ID_RESEND: SignRequestsSignRequestIdResend,
        PathValues.SIGN_REQUESTS_SIGN_REQUEST_ID: SignRequestsSignRequestId,
        PathValues.SIGN_REQUESTS: SignRequests,
        PathValues.WORKFLOWS: Workflows,
        PathValues.WORKFLOWS_WORKFLOW_ID_START: WorkflowsWorkflowIdStart,
        PathValues.SIGN_TEMPLATES: SignTemplates,
        PathValues.SIGN_TEMPLATES_TEMPLATE_ID: SignTemplatesTemplateId,
        PathValues.INTEGRATION_MAPPINGS_SLACK: IntegrationMappingsSlack,
        PathValues.INTEGRATION_MAPPINGS_SLACK_INTEGRATION_MAPPING_ID: IntegrationMappingsSlackIntegrationMappingId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTHORIZE: Authorize,
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.OAUTH2_TOKENREFRESH: Oauth2Tokenrefresh,
        PathValues.OAUTH2_REVOKE: Oauth2Revoke,
        PathValues.FILES_FILE_ID: FilesFileId,
        PathValues.FILES_FILE_ID_CONTENT: FilesFileIdContent,
        PathValues.FILES_CONTENT: FilesContent,
        PathValues.FILES_UPLOAD_SESSIONS: FilesUploadSessions,
        PathValues.FILES_FILE_ID_UPLOAD_SESSIONS: FilesFileIdUploadSessions,
        PathValues.FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID: FilesUploadSessionsUploadSessionId,
        PathValues.FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID_PARTS: FilesUploadSessionsUploadSessionIdParts,
        PathValues.FILES_UPLOAD_SESSIONS_UPLOAD_SESSION_ID_COMMIT: FilesUploadSessionsUploadSessionIdCommit,
        PathValues.FILES_FILE_ID_COPY: FilesFileIdCopy,
        PathValues.FILES_FILE_ID_THUMBNAIL_EXTENSION: FilesFileIdThumbnailExtension,
        PathValues.FILES_FILE_ID_COLLABORATIONS: FilesFileIdCollaborations,
        PathValues.FILES_FILE_ID_COMMENTS: FilesFileIdComments,
        PathValues.FILES_FILE_ID_TASKS: FilesFileIdTasks,
        PathValues.FILES_FILE_ID_TRASH: FilesFileIdTrash,
        PathValues.FILES_FILE_ID_VERSIONS: FilesFileIdVersions,
        PathValues.FILES_FILE_ID_VERSIONS_FILE_VERSION_ID: FilesFileIdVersionsFileVersionId,
        PathValues.FILES_FILE_ID_VERSIONS_CURRENT: FilesFileIdVersionsCurrent,
        PathValues.FILES_FILE_ID_METADATA: FilesFileIdMetadata,
        PathValues.FILES_FILE_ID_METADATA_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO: FilesFileIdMetadataEnterpriseSecurityClassification6VMVochwUWo,
        PathValues.FILES_FILE_ID_METADATA_SCOPE_TEMPLATE_KEY: FilesFileIdMetadataScopeTemplateKey,
        PathValues.FILES_FILE_ID_METADATA_GLOBAL_BOX_SKILLS_CARDS: FilesFileIdMetadataGlobalBoxSkillsCards,
        PathValues.FILES_FILE_ID_WATERMARK: FilesFileIdWatermark,
        PathValues.FILE_REQUESTS_FILE_REQUEST_ID: FileRequestsFileRequestId,
        PathValues.FILE_REQUESTS_FILE_REQUEST_ID_COPY: FileRequestsFileRequestIdCopy,
        PathValues.FOLDERS_FOLDER_ID: FoldersFolderId,
        PathValues.FOLDERS_FOLDER_ID_ITEMS: FoldersFolderIdItems,
        PathValues.FOLDERS: Folders,
        PathValues.FOLDERS_FOLDER_ID_COPY: FoldersFolderIdCopy,
        PathValues.FOLDERS_FOLDER_ID_COLLABORATIONS: FoldersFolderIdCollaborations,
        PathValues.FOLDERS_FOLDER_ID_TRASH: FoldersFolderIdTrash,
        PathValues.FOLDERS_FOLDER_ID_METADATA: FoldersFolderIdMetadata,
        PathValues.FOLDERS_FOLDER_ID_METADATA_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO: FoldersFolderIdMetadataEnterpriseSecurityClassification6VMVochwUWo,
        PathValues.FOLDERS_FOLDER_ID_METADATA_SCOPE_TEMPLATE_KEY: FoldersFolderIdMetadataScopeTemplateKey,
        PathValues.FOLDERS_TRASH_ITEMS: FoldersTrashItems,
        PathValues.FOLDERS_FOLDER_ID_WATERMARK: FoldersFolderIdWatermark,
        PathValues.FOLDER_LOCKS: FolderLocks,
        PathValues.FOLDER_LOCKS_FOLDER_LOCK_ID: FolderLocksFolderLockId,
        PathValues.METADATA_TEMPLATES: MetadataTemplates,
        PathValues.METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMA: MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchema,
        PathValues.METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMAADD: MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchemaadd,
        PathValues.METADATA_TEMPLATES_ENTERPRISE_SECURITY_CLASSIFICATION6VMVOCHW_UWO_SCHEMAUPDATE: MetadataTemplatesEnterpriseSecurityClassification6VMVochwUWoSchemaupdate,
        PathValues.METADATA_TEMPLATES_SCOPE_TEMPLATE_KEY_SCHEMA: MetadataTemplatesScopeTemplateKeySchema,
        PathValues.METADATA_TEMPLATES_TEMPLATE_ID: MetadataTemplatesTemplateId,
        PathValues.METADATA_TEMPLATES_GLOBAL: MetadataTemplatesGlobal,
        PathValues.METADATA_TEMPLATES_ENTERPRISE: MetadataTemplatesEnterprise,
        PathValues.METADATA_TEMPLATES_SCHEMA: MetadataTemplatesSchema,
        PathValues.METADATA_TEMPLATES_SCHEMACLASSIFICATIONS: MetadataTemplatesSchemaclassifications,
        PathValues.METADATA_CASCADE_POLICIES: MetadataCascadePolicies,
        PathValues.METADATA_CASCADE_POLICIES_METADATA_CASCADE_POLICY_ID: MetadataCascadePoliciesMetadataCascadePolicyId,
        PathValues.METADATA_CASCADE_POLICIES_METADATA_CASCADE_POLICY_ID_APPLY: MetadataCascadePoliciesMetadataCascadePolicyIdApply,
        PathValues.METADATA_QUERIES_EXECUTE_READ: MetadataQueriesExecuteRead,
        PathValues.COMMENTS_COMMENT_ID: CommentsCommentId,
        PathValues.COMMENTS: Comments,
        PathValues.COLLABORATIONS_COLLABORATION_ID: CollaborationsCollaborationId,
        PathValues.COLLABORATIONS: Collaborations,
        PathValues.SEARCH: Search,
        PathValues.TASKS: Tasks,
        PathValues.TASKS_TASK_ID: TasksTaskId,
        PathValues.TASKS_TASK_ID_ASSIGNMENTS: TasksTaskIdAssignments,
        PathValues.TASK_ASSIGNMENTS: TaskAssignments,
        PathValues.TASK_ASSIGNMENTS_TASK_ASSIGNMENT_ID: TaskAssignmentsTaskAssignmentId,
        PathValues.SHARED_ITEMS: SharedItems,
        PathValues.FILES_FILE_IDGET_SHARED_LINK: FilesFileIdgetSharedLink,
        PathValues.FILES_FILE_IDADD_SHARED_LINK: FilesFileIdaddSharedLink,
        PathValues.FILES_FILE_IDUPDATE_SHARED_LINK: FilesFileIdupdateSharedLink,
        PathValues.FILES_FILE_IDREMOVE_SHARED_LINK: FilesFileIdremoveSharedLink,
        PathValues.SHARED_ITEMSFOLDERS: SharedItemsfolders,
        PathValues.FOLDERS_FOLDER_IDGET_SHARED_LINK: FoldersFolderIdgetSharedLink,
        PathValues.FOLDERS_FOLDER_IDADD_SHARED_LINK: FoldersFolderIdaddSharedLink,
        PathValues.FOLDERS_FOLDER_IDUPDATE_SHARED_LINK: FoldersFolderIdupdateSharedLink,
        PathValues.FOLDERS_FOLDER_IDREMOVE_SHARED_LINK: FoldersFolderIdremoveSharedLink,
        PathValues.WEB_LINKS: WebLinks,
        PathValues.WEB_LINKS_WEB_LINK_ID: WebLinksWebLinkId,
        PathValues.WEB_LINKS_WEB_LINK_ID_TRASH: WebLinksWebLinkIdTrash,
        PathValues.SHARED_ITEMSWEB_LINKS: SharedItemswebLinks,
        PathValues.WEB_LINKS_WEB_LINK_IDGET_SHARED_LINK: WebLinksWebLinkIdgetSharedLink,
        PathValues.WEB_LINKS_WEB_LINK_IDADD_SHARED_LINK: WebLinksWebLinkIdaddSharedLink,
        PathValues.WEB_LINKS_WEB_LINK_IDUPDATE_SHARED_LINK: WebLinksWebLinkIdupdateSharedLink,
        PathValues.WEB_LINKS_WEB_LINK_IDREMOVE_SHARED_LINK: WebLinksWebLinkIdremoveSharedLink,
        PathValues.USERS: Users,
        PathValues.USERS_ME: UsersMe,
        PathValues.USERS_TERMINATE_SESSIONS: UsersTerminateSessions,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.USERS_USER_ID_AVATAR: UsersUserIdAvatar,
        PathValues.USERS_USER_ID_FOLDERS_0: UsersUserIdFolders0,
        PathValues.USERS_USER_ID_EMAIL_ALIASES: UsersUserIdEmailAliases,
        PathValues.USERS_USER_ID_EMAIL_ALIASES_EMAIL_ALIAS_ID: UsersUserIdEmailAliasesEmailAliasId,
        PathValues.USERS_USER_ID_MEMBERSHIPS: UsersUserIdMemberships,
        PathValues.INVITES: Invites,
        PathValues.INVITES_INVITE_ID: InvitesInviteId,
        PathValues.GROUPS: Groups,
        PathValues.GROUPS_TERMINATE_SESSIONS: GroupsTerminateSessions,
        PathValues.GROUPS_GROUP_ID: GroupsGroupId,
        PathValues.GROUPS_GROUP_ID_MEMBERSHIPS: GroupsGroupIdMemberships,
        PathValues.GROUPS_GROUP_ID_COLLABORATIONS: GroupsGroupIdCollaborations,
        PathValues.GROUP_MEMBERSHIPS: GroupMemberships,
        PathValues.GROUP_MEMBERSHIPS_GROUP_MEMBERSHIP_ID: GroupMembershipsGroupMembershipId,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
        PathValues.SKILL_INVOCATIONS_SKILL_ID: SkillInvocationsSkillId,
        PathValues.EVENTS: Events,
        PathValues.COLLECTIONS: Collections,
        PathValues.COLLECTIONS_COLLECTION_ID_ITEMS: CollectionsCollectionIdItems,
        PathValues.RECENT_ITEMS: RecentItems,
        PathValues.RETENTION_POLICIES: RetentionPolicies,
        PathValues.RETENTION_POLICIES_RETENTION_POLICY_ID: RetentionPoliciesRetentionPolicyId,
        PathValues.RETENTION_POLICIES_RETENTION_POLICY_ID_ASSIGNMENTS: RetentionPoliciesRetentionPolicyIdAssignments,
        PathValues.RETENTION_POLICY_ASSIGNMENTS: RetentionPolicyAssignments,
        PathValues.RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID: RetentionPolicyAssignmentsRetentionPolicyAssignmentId,
        PathValues.RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID_FILES_UNDER_RETENTION: RetentionPolicyAssignmentsRetentionPolicyAssignmentIdFilesUnderRetention,
        PathValues.RETENTION_POLICY_ASSIGNMENTS_RETENTION_POLICY_ASSIGNMENT_ID_FILE_VERSIONS_UNDER_RETENTION: RetentionPolicyAssignmentsRetentionPolicyAssignmentIdFileVersionsUnderRetention,
        PathValues.LEGAL_HOLD_POLICIES: LegalHoldPolicies,
        PathValues.LEGAL_HOLD_POLICIES_LEGAL_HOLD_POLICY_ID: LegalHoldPoliciesLegalHoldPolicyId,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS: LegalHoldPolicyAssignments,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID: LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentId,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID_FILES_ON_HOLD: LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentIdFilesOnHold,
        PathValues.FILE_VERSION_RETENTIONS: FileVersionRetentions,
        PathValues.LEGAL_HOLD_POLICY_ASSIGNMENTS_LEGAL_HOLD_POLICY_ASSIGNMENT_ID_FILE_VERSIONS_ON_HOLD: LegalHoldPolicyAssignmentsLegalHoldPolicyAssignmentIdFileVersionsOnHold,
        PathValues.FILE_VERSION_RETENTIONS_FILE_VERSION_RETENTION_ID: FileVersionRetentionsFileVersionRetentionId,
        PathValues.FILE_VERSION_LEGAL_HOLDS_FILE_VERSION_LEGAL_HOLD_ID: FileVersionLegalHoldsFileVersionLegalHoldId,
        PathValues.FILE_VERSION_LEGAL_HOLDS: FileVersionLegalHolds,
        PathValues.SHIELD_INFORMATION_BARRIERS_SHIELD_INFORMATION_BARRIER_ID: ShieldInformationBarriersShieldInformationBarrierId,
        PathValues.SHIELD_INFORMATION_BARRIERS_CHANGE_STATUS: ShieldInformationBarriersChangeStatus,
        PathValues.SHIELD_INFORMATION_BARRIERS: ShieldInformationBarriers,
        PathValues.SHIELD_INFORMATION_BARRIER_REPORTS: ShieldInformationBarrierReports,
        PathValues.SHIELD_INFORMATION_BARRIER_REPORTS_SHIELD_INFORMATION_BARRIER_REPORT_ID: ShieldInformationBarrierReportsShieldInformationBarrierReportId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENTS_SHIELD_INFORMATION_BARRIER_SEGMENT_ID: ShieldInformationBarrierSegmentsShieldInformationBarrierSegmentId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENTS: ShieldInformationBarrierSegments,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS_SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER_ID: ShieldInformationBarrierSegmentMembersShieldInformationBarrierSegmentMemberId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS: ShieldInformationBarrierSegmentMembers,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS_SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTION_ID: ShieldInformationBarrierSegmentRestrictionsShieldInformationBarrierSegmentRestrictionId,
        PathValues.SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS: ShieldInformationBarrierSegmentRestrictions,
        PathValues.DEVICE_PINNERS_DEVICE_PINNER_ID: DevicePinnersDevicePinnerId,
        PathValues.ENTERPRISES_ENTERPRISE_ID_DEVICE_PINNERS: EnterprisesEnterpriseIdDevicePinners,
        PathValues.TERMS_OF_SERVICES: TermsOfServices,
        PathValues.TERMS_OF_SERVICES_TERMS_OF_SERVICE_ID: TermsOfServicesTermsOfServiceId,
        PathValues.TERMS_OF_SERVICE_USER_STATUSES: TermsOfServiceUserStatuses,
        PathValues.TERMS_OF_SERVICE_USER_STATUSES_TERMS_OF_SERVICE_USER_STATUS_ID: TermsOfServiceUserStatusesTermsOfServiceUserStatusId,
        PathValues.COLLABORATION_WHITELIST_ENTRIES: CollaborationWhitelistEntries,
        PathValues.COLLABORATION_WHITELIST_ENTRIES_COLLABORATION_WHITELIST_ENTRY_ID: CollaborationWhitelistEntriesCollaborationWhitelistEntryId,
        PathValues.COLLABORATION_WHITELIST_EXEMPT_TARGETS: CollaborationWhitelistExemptTargets,
        PathValues.COLLABORATION_WHITELIST_EXEMPT_TARGETS_COLLABORATION_WHITELIST_EXEMPT_TARGET_ID: CollaborationWhitelistExemptTargetsCollaborationWhitelistExemptTargetId,
        PathValues.STORAGE_POLICIES: StoragePolicies,
        PathValues.STORAGE_POLICIES_STORAGE_POLICY_ID: StoragePoliciesStoragePolicyId,
        PathValues.STORAGE_POLICY_ASSIGNMENTS: StoragePolicyAssignments,
        PathValues.STORAGE_POLICY_ASSIGNMENTS_STORAGE_POLICY_ASSIGNMENT_ID: StoragePolicyAssignmentsStoragePolicyAssignmentId,
        PathValues.ZIP_DOWNLOADS: ZipDownloads,
        PathValues.ZIP_DOWNLOADS_ZIP_DOWNLOAD_ID_CONTENT: ZipDownloadsZipDownloadIdContent,
        PathValues.ZIP_DOWNLOADS_ZIP_DOWNLOAD_ID_STATUS: ZipDownloadsZipDownloadIdStatus,
        PathValues.SIGN_REQUESTS_SIGN_REQUEST_ID_CANCEL: SignRequestsSignRequestIdCancel,
        PathValues.SIGN_REQUESTS_SIGN_REQUEST_ID_RESEND: SignRequestsSignRequestIdResend,
        PathValues.SIGN_REQUESTS_SIGN_REQUEST_ID: SignRequestsSignRequestId,
        PathValues.SIGN_REQUESTS: SignRequests,
        PathValues.WORKFLOWS: Workflows,
        PathValues.WORKFLOWS_WORKFLOW_ID_START: WorkflowsWorkflowIdStart,
        PathValues.SIGN_TEMPLATES: SignTemplates,
        PathValues.SIGN_TEMPLATES_TEMPLATE_ID: SignTemplatesTemplateId,
        PathValues.INTEGRATION_MAPPINGS_SLACK: IntegrationMappingsSlack,
        PathValues.INTEGRATION_MAPPINGS_SLACK_INTEGRATION_MAPPING_ID: IntegrationMappingsSlackIntegrationMappingId,
    }
)
