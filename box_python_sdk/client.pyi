# coding: utf-8
"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

import typing
import inspect
from datetime import date, datetime
from box_python_sdk.client_custom import ClientCustom
from box_python_sdk.configuration import Configuration
from box_python_sdk.api_client import ApiClient
from box_python_sdk.type_util import copy_signature
from box_python_sdk.apis.tags.authorization_api import AuthorizationApi
from box_python_sdk.apis.tags.classifications_api import ClassificationsApi
from box_python_sdk.apis.tags.classifications_on_files_api import ClassificationsOnFilesApi
from box_python_sdk.apis.tags.classifications_on_folders_api import ClassificationsOnFoldersApi
from box_python_sdk.apis.tags.collaborations_api import CollaborationsApi
from box_python_sdk.apis.tags.collaborations_list_api import CollaborationsListApi
from box_python_sdk.apis.tags.collections_api import CollectionsApi
from box_python_sdk.apis.tags.comments_api import CommentsApi
from box_python_sdk.apis.tags.device_pinners_api import DevicePinnersApi
from box_python_sdk.apis.tags.domain_restrictions_user_exemptions_api import DomainRestrictionsUserExemptionsApi
from box_python_sdk.apis.tags.domain_restrictions_for_collaborations_api import DomainRestrictionsForCollaborationsApi
from box_python_sdk.apis.tags.downloads_api import DownloadsApi
from box_python_sdk.apis.tags.email_aliases_api import EmailAliasesApi
from box_python_sdk.apis.tags.events_api import EventsApi
from box_python_sdk.apis.tags.file_requests_api import FileRequestsApi
from box_python_sdk.apis.tags.file_version_legal_holds_api import FileVersionLegalHoldsApi
from box_python_sdk.apis.tags.file_version_retentions_api import FileVersionRetentionsApi
from box_python_sdk.apis.tags.file_versions_api import FileVersionsApi
from box_python_sdk.apis.tags.files_api import FilesApi
from box_python_sdk.apis.tags.folder_locks_api import FolderLocksApi
from box_python_sdk.apis.tags.folders_api import FoldersApi
from box_python_sdk.apis.tags.group_memberships_api import GroupMembershipsApi
from box_python_sdk.apis.tags.groups_api import GroupsApi
from box_python_sdk.apis.tags.integration_mappings_api import IntegrationMappingsApi
from box_python_sdk.apis.tags.invites_api import InvitesApi
from box_python_sdk.apis.tags.legal_hold_policies_api import LegalHoldPoliciesApi
from box_python_sdk.apis.tags.legal_hold_policy_assignments_api import LegalHoldPolicyAssignmentsApi
from box_python_sdk.apis.tags.metadata_cascade_policies_api import MetadataCascadePoliciesApi
from box_python_sdk.apis.tags.metadata_instances_files_api import MetadataInstancesFilesApi
from box_python_sdk.apis.tags.metadata_instances_folders_api import MetadataInstancesFoldersApi
from box_python_sdk.apis.tags.metadata_templates_api import MetadataTemplatesApi
from box_python_sdk.apis.tags.recent_items_api import RecentItemsApi
from box_python_sdk.apis.tags.retention_policies_api import RetentionPoliciesApi
from box_python_sdk.apis.tags.retention_policy_assignments_api import RetentionPolicyAssignmentsApi
from box_python_sdk.apis.tags.search_api import SearchApi
from box_python_sdk.apis.tags.session_termination_api import SessionTerminationApi
from box_python_sdk.apis.tags.shared_links_files_api import SharedLinksFilesApi
from box_python_sdk.apis.tags.shared_links_folders_api import SharedLinksFoldersApi
from box_python_sdk.apis.tags.shared_links_web_links_api import SharedLinksWebLinksApi
from box_python_sdk.apis.tags.shield_information_barrier_reports_api import ShieldInformationBarrierReportsApi
from box_python_sdk.apis.tags.shield_information_barrier_segment_members_api import ShieldInformationBarrierSegmentMembersApi
from box_python_sdk.apis.tags.shield_information_barrier_segment_restrictions_api import ShieldInformationBarrierSegmentRestrictionsApi
from box_python_sdk.apis.tags.shield_information_barrier_segments_api import ShieldInformationBarrierSegmentsApi
from box_python_sdk.apis.tags.shield_information_barriers_api import ShieldInformationBarriersApi
from box_python_sdk.apis.tags.sign_requests_api import SignRequestsApi
from box_python_sdk.apis.tags.sign_templates_api import SignTemplatesApi
from box_python_sdk.apis.tags.skills_api import SkillsApi
from box_python_sdk.apis.tags.standard_and_zones_storage_policies_api import StandardAndZonesStoragePoliciesApi
from box_python_sdk.apis.tags.standard_and_zones_storage_policy_assignments_api import StandardAndZonesStoragePolicyAssignmentsApi
from box_python_sdk.apis.tags.task_assignments_api import TaskAssignmentsApi
from box_python_sdk.apis.tags.tasks_api import TasksApi
from box_python_sdk.apis.tags.terms_of_service_api import TermsOfServiceApi
from box_python_sdk.apis.tags.terms_of_service_user_statuses_api import TermsOfServiceUserStatusesApi
from box_python_sdk.apis.tags.transfer_folders_api import TransferFoldersApi
from box_python_sdk.apis.tags.trashed_files_api import TrashedFilesApi
from box_python_sdk.apis.tags.trashed_folders_api import TrashedFoldersApi
from box_python_sdk.apis.tags.trashed_items_api import TrashedItemsApi
from box_python_sdk.apis.tags.trashed_web_links_api import TrashedWebLinksApi
from box_python_sdk.apis.tags.uploads_api import UploadsApi
from box_python_sdk.apis.tags.uploads_chunked_api import UploadsChunkedApi
from box_python_sdk.apis.tags.user_avatars_api import UserAvatarsApi
from box_python_sdk.apis.tags.users_api import UsersApi
from box_python_sdk.apis.tags.watermarks_files_api import WatermarksFilesApi
from box_python_sdk.apis.tags.watermarks_folders_api import WatermarksFoldersApi
from box_python_sdk.apis.tags.web_links_api import WebLinksApi
from box_python_sdk.apis.tags.webhooks_api import WebhooksApi
from box_python_sdk.apis.tags.workflows_api import WorkflowsApi
from box_python_sdk.apis.tags.zip_downloads_api import ZipDownloadsApi



class Box(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.authorization: AuthorizationApi = AuthorizationApi(api_client)
        self.classifications: ClassificationsApi = ClassificationsApi(api_client)
        self.classifications_on_files: ClassificationsOnFilesApi = ClassificationsOnFilesApi(api_client)
        self.classifications_on_folders: ClassificationsOnFoldersApi = ClassificationsOnFoldersApi(api_client)
        self.collaborations: CollaborationsApi = CollaborationsApi(api_client)
        self.collaborations_(list): CollaborationsListApi = CollaborationsListApi(api_client)
        self.collections: CollectionsApi = CollectionsApi(api_client)
        self.comments: CommentsApi = CommentsApi(api_client)
        self.device_pinners: DevicePinnersApi = DevicePinnersApi(api_client)
        self.domain_restrictions_(user_exemptions): DomainRestrictionsUserExemptionsApi = DomainRestrictionsUserExemptionsApi(api_client)
        self.domain_restrictions_for_collaborations: DomainRestrictionsForCollaborationsApi = DomainRestrictionsForCollaborationsApi(api_client)
        self.downloads: DownloadsApi = DownloadsApi(api_client)
        self.email_aliases: EmailAliasesApi = EmailAliasesApi(api_client)
        self.events: EventsApi = EventsApi(api_client)
        self.file_requests: FileRequestsApi = FileRequestsApi(api_client)
        self.file_version_legal_holds: FileVersionLegalHoldsApi = FileVersionLegalHoldsApi(api_client)
        self.file_version_retentions: FileVersionRetentionsApi = FileVersionRetentionsApi(api_client)
        self.file_versions: FileVersionsApi = FileVersionsApi(api_client)
        self.files: FilesApi = FilesApi(api_client)
        self.folder_locks: FolderLocksApi = FolderLocksApi(api_client)
        self.folders: FoldersApi = FoldersApi(api_client)
        self.group_memberships: GroupMembershipsApi = GroupMembershipsApi(api_client)
        self.groups: GroupsApi = GroupsApi(api_client)
        self.integration_mappings: IntegrationMappingsApi = IntegrationMappingsApi(api_client)
        self.invites: InvitesApi = InvitesApi(api_client)
        self.legal_hold_policies: LegalHoldPoliciesApi = LegalHoldPoliciesApi(api_client)
        self.legal_hold_policy_assignments: LegalHoldPolicyAssignmentsApi = LegalHoldPolicyAssignmentsApi(api_client)
        self.metadata_cascade_policies: MetadataCascadePoliciesApi = MetadataCascadePoliciesApi(api_client)
        self.metadata_instances_(files): MetadataInstancesFilesApi = MetadataInstancesFilesApi(api_client)
        self.metadata_instances_(folders): MetadataInstancesFoldersApi = MetadataInstancesFoldersApi(api_client)
        self.metadata_templates: MetadataTemplatesApi = MetadataTemplatesApi(api_client)
        self.recent_items: RecentItemsApi = RecentItemsApi(api_client)
        self.retention_policies: RetentionPoliciesApi = RetentionPoliciesApi(api_client)
        self.retention_policy_assignments: RetentionPolicyAssignmentsApi = RetentionPolicyAssignmentsApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.session_termination: SessionTerminationApi = SessionTerminationApi(api_client)
        self.shared_links_(files): SharedLinksFilesApi = SharedLinksFilesApi(api_client)
        self.shared_links_(folders): SharedLinksFoldersApi = SharedLinksFoldersApi(api_client)
        self.shared_links_(web_links): SharedLinksWebLinksApi = SharedLinksWebLinksApi(api_client)
        self.shield_information_barrier_reports: ShieldInformationBarrierReportsApi = ShieldInformationBarrierReportsApi(api_client)
        self.shield_information_barrier_segment_members: ShieldInformationBarrierSegmentMembersApi = ShieldInformationBarrierSegmentMembersApi(api_client)
        self.shield_information_barrier_segment_restrictions: ShieldInformationBarrierSegmentRestrictionsApi = ShieldInformationBarrierSegmentRestrictionsApi(api_client)
        self.shield_information_barrier_segments: ShieldInformationBarrierSegmentsApi = ShieldInformationBarrierSegmentsApi(api_client)
        self.shield_information_barriers: ShieldInformationBarriersApi = ShieldInformationBarriersApi(api_client)
        self.sign_requests: SignRequestsApi = SignRequestsApi(api_client)
        self.sign_templates: SignTemplatesApi = SignTemplatesApi(api_client)
        self.skills: SkillsApi = SkillsApi(api_client)
        self.standard_and_zones_storage_policies: StandardAndZonesStoragePoliciesApi = StandardAndZonesStoragePoliciesApi(api_client)
        self.standard_and_zones_storage_policy_assignments: StandardAndZonesStoragePolicyAssignmentsApi = StandardAndZonesStoragePolicyAssignmentsApi(api_client)
        self.task_assignments: TaskAssignmentsApi = TaskAssignmentsApi(api_client)
        self.tasks: TasksApi = TasksApi(api_client)
        self.terms_of_service: TermsOfServiceApi = TermsOfServiceApi(api_client)
        self.terms_of_service_user_statuses: TermsOfServiceUserStatusesApi = TermsOfServiceUserStatusesApi(api_client)
        self.transfer_folders: TransferFoldersApi = TransferFoldersApi(api_client)
        self.trashed_files: TrashedFilesApi = TrashedFilesApi(api_client)
        self.trashed_folders: TrashedFoldersApi = TrashedFoldersApi(api_client)
        self.trashed_items: TrashedItemsApi = TrashedItemsApi(api_client)
        self.trashed_web_links: TrashedWebLinksApi = TrashedWebLinksApi(api_client)
        self.uploads: UploadsApi = UploadsApi(api_client)
        self.uploads_(chunked): UploadsChunkedApi = UploadsChunkedApi(api_client)
        self.user_avatars: UserAvatarsApi = UserAvatarsApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
        self.watermarks_(files): WatermarksFilesApi = WatermarksFilesApi(api_client)
        self.watermarks_(folders): WatermarksFoldersApi = WatermarksFoldersApi(api_client)
        self.web_links: WebLinksApi = WebLinksApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)
        self.workflows: WorkflowsApi = WorkflowsApi(api_client)
        self.zip_downloads: ZipDownloadsApi = ZipDownloadsApi(api_client)
