import typing_extensions

from box_python_sdk.apis.tags import TagValues
from box_python_sdk.apis.tags.metadata_templates_api import MetadataTemplatesApi
from box_python_sdk.apis.tags.uploads_chunked_api import UploadsChunkedApi
from box_python_sdk.apis.tags.files_api import FilesApi
from box_python_sdk.apis.tags.folders_api import FoldersApi
from box_python_sdk.apis.tags.group_memberships_api import GroupMembershipsApi
from box_python_sdk.apis.tags.legal_hold_policy_assignments_api import LegalHoldPolicyAssignmentsApi
from box_python_sdk.apis.tags.retention_policy_assignments_api import RetentionPolicyAssignmentsApi
from box_python_sdk.apis.tags.users_api import UsersApi
from box_python_sdk.apis.tags.sign_requests_api import SignRequestsApi
from box_python_sdk.apis.tags.comments_api import CommentsApi
from box_python_sdk.apis.tags.file_versions_api import FileVersionsApi
from box_python_sdk.apis.tags.groups_api import GroupsApi
from box_python_sdk.apis.tags.legal_hold_policies_api import LegalHoldPoliciesApi
from box_python_sdk.apis.tags.metadata_cascade_policies_api import MetadataCascadePoliciesApi
from box_python_sdk.apis.tags.metadata_instances_files_api import MetadataInstancesFilesApi
from box_python_sdk.apis.tags.metadata_instances_folders_api import MetadataInstancesFoldersApi
from box_python_sdk.apis.tags.retention_policies_api import RetentionPoliciesApi
from box_python_sdk.apis.tags.shared_links_files_api import SharedLinksFilesApi
from box_python_sdk.apis.tags.shared_links_folders_api import SharedLinksFoldersApi
from box_python_sdk.apis.tags.shared_links_web_links_api import SharedLinksWebLinksApi
from box_python_sdk.apis.tags.shield_information_barrier_segments_api import ShieldInformationBarrierSegmentsApi
from box_python_sdk.apis.tags.skills_api import SkillsApi
from box_python_sdk.apis.tags.standard_and_zones_storage_policy_assignments_api import StandardAndZonesStoragePolicyAssignmentsApi
from box_python_sdk.apis.tags.task_assignments_api import TaskAssignmentsApi
from box_python_sdk.apis.tags.tasks_api import TasksApi
from box_python_sdk.apis.tags.webhooks_api import WebhooksApi
from box_python_sdk.apis.tags.authorization_api import AuthorizationApi
from box_python_sdk.apis.tags.classifications_api import ClassificationsApi
from box_python_sdk.apis.tags.classifications_on_files_api import ClassificationsOnFilesApi
from box_python_sdk.apis.tags.classifications_on_folders_api import ClassificationsOnFoldersApi
from box_python_sdk.apis.tags.collaborations_api import CollaborationsApi
from box_python_sdk.apis.tags.collaborations_list_api import CollaborationsListApi
from box_python_sdk.apis.tags.domain_restrictions_user_exemptions_api import DomainRestrictionsUserExemptionsApi
from box_python_sdk.apis.tags.domain_restrictions_for_collaborations_api import DomainRestrictionsForCollaborationsApi
from box_python_sdk.apis.tags.file_requests_api import FileRequestsApi
from box_python_sdk.apis.tags.integration_mappings_api import IntegrationMappingsApi
from box_python_sdk.apis.tags.shield_information_barriers_api import ShieldInformationBarriersApi
from box_python_sdk.apis.tags.shield_information_barrier_segment_members_api import ShieldInformationBarrierSegmentMembersApi
from box_python_sdk.apis.tags.shield_information_barrier_segment_restrictions_api import ShieldInformationBarrierSegmentRestrictionsApi
from box_python_sdk.apis.tags.terms_of_service_api import TermsOfServiceApi
from box_python_sdk.apis.tags.web_links_api import WebLinksApi
from box_python_sdk.apis.tags.device_pinners_api import DevicePinnersApi
from box_python_sdk.apis.tags.email_aliases_api import EmailAliasesApi
from box_python_sdk.apis.tags.folder_locks_api import FolderLocksApi
from box_python_sdk.apis.tags.shield_information_barrier_reports_api import ShieldInformationBarrierReportsApi
from box_python_sdk.apis.tags.terms_of_service_user_statuses_api import TermsOfServiceUserStatusesApi
from box_python_sdk.apis.tags.trashed_files_api import TrashedFilesApi
from box_python_sdk.apis.tags.trashed_folders_api import TrashedFoldersApi
from box_python_sdk.apis.tags.trashed_web_links_api import TrashedWebLinksApi
from box_python_sdk.apis.tags.user_avatars_api import UserAvatarsApi
from box_python_sdk.apis.tags.watermarks_files_api import WatermarksFilesApi
from box_python_sdk.apis.tags.watermarks_folders_api import WatermarksFoldersApi
from box_python_sdk.apis.tags.zip_downloads_api import ZipDownloadsApi
from box_python_sdk.apis.tags.collections_api import CollectionsApi
from box_python_sdk.apis.tags.events_api import EventsApi
from box_python_sdk.apis.tags.file_version_legal_holds_api import FileVersionLegalHoldsApi
from box_python_sdk.apis.tags.file_version_retentions_api import FileVersionRetentionsApi
from box_python_sdk.apis.tags.invites_api import InvitesApi
from box_python_sdk.apis.tags.search_api import SearchApi
from box_python_sdk.apis.tags.session_termination_api import SessionTerminationApi
from box_python_sdk.apis.tags.sign_templates_api import SignTemplatesApi
from box_python_sdk.apis.tags.standard_and_zones_storage_policies_api import StandardAndZonesStoragePoliciesApi
from box_python_sdk.apis.tags.uploads_api import UploadsApi
from box_python_sdk.apis.tags.workflows_api import WorkflowsApi
from box_python_sdk.apis.tags.downloads_api import DownloadsApi
from box_python_sdk.apis.tags.recent_items_api import RecentItemsApi
from box_python_sdk.apis.tags.transfer_folders_api import TransferFoldersApi
from box_python_sdk.apis.tags.trashed_items_api import TrashedItemsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.METADATA_TEMPLATES: MetadataTemplatesApi,
        TagValues.UPLOADS_CHUNKED: UploadsChunkedApi,
        TagValues.FILES: FilesApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.GROUP_MEMBERSHIPS: GroupMembershipsApi,
        TagValues.LEGAL_HOLD_POLICY_ASSIGNMENTS: LegalHoldPolicyAssignmentsApi,
        TagValues.RETENTION_POLICY_ASSIGNMENTS: RetentionPolicyAssignmentsApi,
        TagValues.USERS: UsersApi,
        TagValues.SIGN_REQUESTS: SignRequestsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.FILE_VERSIONS: FileVersionsApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.LEGAL_HOLD_POLICIES: LegalHoldPoliciesApi,
        TagValues.METADATA_CASCADE_POLICIES: MetadataCascadePoliciesApi,
        TagValues.METADATA_INSTANCES_FILES: MetadataInstancesFilesApi,
        TagValues.METADATA_INSTANCES_FOLDERS: MetadataInstancesFoldersApi,
        TagValues.RETENTION_POLICIES: RetentionPoliciesApi,
        TagValues.SHARED_LINKS_FILES: SharedLinksFilesApi,
        TagValues.SHARED_LINKS_FOLDERS: SharedLinksFoldersApi,
        TagValues.SHARED_LINKS_WEB_LINKS: SharedLinksWebLinksApi,
        TagValues.SHIELD_INFORMATION_BARRIER_SEGMENTS: ShieldInformationBarrierSegmentsApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.STANDARD_AND_ZONES_STORAGE_POLICY_ASSIGNMENTS: StandardAndZonesStoragePolicyAssignmentsApi,
        TagValues.TASK_ASSIGNMENTS: TaskAssignmentsApi,
        TagValues.TASKS: TasksApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.CLASSIFICATIONS: ClassificationsApi,
        TagValues.CLASSIFICATIONS_ON_FILES: ClassificationsOnFilesApi,
        TagValues.CLASSIFICATIONS_ON_FOLDERS: ClassificationsOnFoldersApi,
        TagValues.COLLABORATIONS: CollaborationsApi,
        TagValues.COLLABORATIONS_LIST: CollaborationsListApi,
        TagValues.DOMAIN_RESTRICTIONS_USER_EXEMPTIONS: DomainRestrictionsUserExemptionsApi,
        TagValues.DOMAIN_RESTRICTIONS_FOR_COLLABORATIONS: DomainRestrictionsForCollaborationsApi,
        TagValues.FILE_REQUESTS: FileRequestsApi,
        TagValues.INTEGRATION_MAPPINGS: IntegrationMappingsApi,
        TagValues.SHIELD_INFORMATION_BARRIERS: ShieldInformationBarriersApi,
        TagValues.SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS: ShieldInformationBarrierSegmentMembersApi,
        TagValues.SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS: ShieldInformationBarrierSegmentRestrictionsApi,
        TagValues.TERMS_OF_SERVICE: TermsOfServiceApi,
        TagValues.WEB_LINKS: WebLinksApi,
        TagValues.DEVICE_PINNERS: DevicePinnersApi,
        TagValues.EMAIL_ALIASES: EmailAliasesApi,
        TagValues.FOLDER_LOCKS: FolderLocksApi,
        TagValues.SHIELD_INFORMATION_BARRIER_REPORTS: ShieldInformationBarrierReportsApi,
        TagValues.TERMS_OF_SERVICE_USER_STATUSES: TermsOfServiceUserStatusesApi,
        TagValues.TRASHED_FILES: TrashedFilesApi,
        TagValues.TRASHED_FOLDERS: TrashedFoldersApi,
        TagValues.TRASHED_WEB_LINKS: TrashedWebLinksApi,
        TagValues.USER_AVATARS: UserAvatarsApi,
        TagValues.WATERMARKS_FILES: WatermarksFilesApi,
        TagValues.WATERMARKS_FOLDERS: WatermarksFoldersApi,
        TagValues.ZIP_DOWNLOADS: ZipDownloadsApi,
        TagValues.COLLECTIONS: CollectionsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FILE_VERSION_LEGAL_HOLDS: FileVersionLegalHoldsApi,
        TagValues.FILE_VERSION_RETENTIONS: FileVersionRetentionsApi,
        TagValues.INVITES: InvitesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SESSION_TERMINATION: SessionTerminationApi,
        TagValues.SIGN_TEMPLATES: SignTemplatesApi,
        TagValues.STANDARD_AND_ZONES_STORAGE_POLICIES: StandardAndZonesStoragePoliciesApi,
        TagValues.UPLOADS: UploadsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.DOWNLOADS: DownloadsApi,
        TagValues.RECENT_ITEMS: RecentItemsApi,
        TagValues.TRANSFER_FOLDERS: TransferFoldersApi,
        TagValues.TRASHED_ITEMS: TrashedItemsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.METADATA_TEMPLATES: MetadataTemplatesApi,
        TagValues.UPLOADS_CHUNKED: UploadsChunkedApi,
        TagValues.FILES: FilesApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.GROUP_MEMBERSHIPS: GroupMembershipsApi,
        TagValues.LEGAL_HOLD_POLICY_ASSIGNMENTS: LegalHoldPolicyAssignmentsApi,
        TagValues.RETENTION_POLICY_ASSIGNMENTS: RetentionPolicyAssignmentsApi,
        TagValues.USERS: UsersApi,
        TagValues.SIGN_REQUESTS: SignRequestsApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.FILE_VERSIONS: FileVersionsApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.LEGAL_HOLD_POLICIES: LegalHoldPoliciesApi,
        TagValues.METADATA_CASCADE_POLICIES: MetadataCascadePoliciesApi,
        TagValues.METADATA_INSTANCES_FILES: MetadataInstancesFilesApi,
        TagValues.METADATA_INSTANCES_FOLDERS: MetadataInstancesFoldersApi,
        TagValues.RETENTION_POLICIES: RetentionPoliciesApi,
        TagValues.SHARED_LINKS_FILES: SharedLinksFilesApi,
        TagValues.SHARED_LINKS_FOLDERS: SharedLinksFoldersApi,
        TagValues.SHARED_LINKS_WEB_LINKS: SharedLinksWebLinksApi,
        TagValues.SHIELD_INFORMATION_BARRIER_SEGMENTS: ShieldInformationBarrierSegmentsApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.STANDARD_AND_ZONES_STORAGE_POLICY_ASSIGNMENTS: StandardAndZonesStoragePolicyAssignmentsApi,
        TagValues.TASK_ASSIGNMENTS: TaskAssignmentsApi,
        TagValues.TASKS: TasksApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.CLASSIFICATIONS: ClassificationsApi,
        TagValues.CLASSIFICATIONS_ON_FILES: ClassificationsOnFilesApi,
        TagValues.CLASSIFICATIONS_ON_FOLDERS: ClassificationsOnFoldersApi,
        TagValues.COLLABORATIONS: CollaborationsApi,
        TagValues.COLLABORATIONS_LIST: CollaborationsListApi,
        TagValues.DOMAIN_RESTRICTIONS_USER_EXEMPTIONS: DomainRestrictionsUserExemptionsApi,
        TagValues.DOMAIN_RESTRICTIONS_FOR_COLLABORATIONS: DomainRestrictionsForCollaborationsApi,
        TagValues.FILE_REQUESTS: FileRequestsApi,
        TagValues.INTEGRATION_MAPPINGS: IntegrationMappingsApi,
        TagValues.SHIELD_INFORMATION_BARRIERS: ShieldInformationBarriersApi,
        TagValues.SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBERS: ShieldInformationBarrierSegmentMembersApi,
        TagValues.SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTIONS: ShieldInformationBarrierSegmentRestrictionsApi,
        TagValues.TERMS_OF_SERVICE: TermsOfServiceApi,
        TagValues.WEB_LINKS: WebLinksApi,
        TagValues.DEVICE_PINNERS: DevicePinnersApi,
        TagValues.EMAIL_ALIASES: EmailAliasesApi,
        TagValues.FOLDER_LOCKS: FolderLocksApi,
        TagValues.SHIELD_INFORMATION_BARRIER_REPORTS: ShieldInformationBarrierReportsApi,
        TagValues.TERMS_OF_SERVICE_USER_STATUSES: TermsOfServiceUserStatusesApi,
        TagValues.TRASHED_FILES: TrashedFilesApi,
        TagValues.TRASHED_FOLDERS: TrashedFoldersApi,
        TagValues.TRASHED_WEB_LINKS: TrashedWebLinksApi,
        TagValues.USER_AVATARS: UserAvatarsApi,
        TagValues.WATERMARKS_FILES: WatermarksFilesApi,
        TagValues.WATERMARKS_FOLDERS: WatermarksFoldersApi,
        TagValues.ZIP_DOWNLOADS: ZipDownloadsApi,
        TagValues.COLLECTIONS: CollectionsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FILE_VERSION_LEGAL_HOLDS: FileVersionLegalHoldsApi,
        TagValues.FILE_VERSION_RETENTIONS: FileVersionRetentionsApi,
        TagValues.INVITES: InvitesApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SESSION_TERMINATION: SessionTerminationApi,
        TagValues.SIGN_TEMPLATES: SignTemplatesApi,
        TagValues.STANDARD_AND_ZONES_STORAGE_POLICIES: StandardAndZonesStoragePoliciesApi,
        TagValues.UPLOADS: UploadsApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.DOWNLOADS: DownloadsApi,
        TagValues.RECENT_ITEMS: RecentItemsApi,
        TagValues.TRANSFER_FOLDERS: TransferFoldersApi,
        TagValues.TRASHED_ITEMS: TrashedItemsApi,
    }
)
