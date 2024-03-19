<div align="left">

[![Visit Box](./header.png)](https://box.com)

# Box<a id="box"></a>

[Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Getting Started](#getting-started)
  * [Async](#async)
  * [Raw HTTP Response](#raw-http-response)
  * [Reference](#reference)
    + [`box.authorization.authorize`](#boxauthorizationauthorize)
    + [`box.authorization.refresh_access_token`](#boxauthorizationrefresh_access_token)
    + [`box.authorization.request_access_token`](#boxauthorizationrequest_access_token)
    + [`box.authorization.revoke_access_token`](#boxauthorizationrevoke_access_token)
    + [`box.classifications.add_new_classifications`](#boxclassificationsadd_new_classifications)
    + [`box.classifications.initialize_template`](#boxclassificationsinitialize_template)
    + [`box.classifications.list_all_classifications`](#boxclassificationslist_all_classifications)
    + [`box.classifications.update_labels_descriptions`](#boxclassificationsupdate_labels_descriptions)
    + [`box.classifications_on_files.add_classification`](#boxclassifications_on_filesadd_classification)
    + [`box.classifications_on_files.get_classification_metadata_instance`](#boxclassifications_on_filesget_classification_metadata_instance)
    + [`box.classifications_on_files.remove_classification`](#boxclassifications_on_filesremove_classification)
    + [`box.classifications_on_files.update_classification_metadata_instance`](#boxclassifications_on_filesupdate_classification_metadata_instance)
    + [`box.classifications_on_folders.add_classification_to_folder`](#boxclassifications_on_foldersadd_classification_to_folder)
    + [`box.classifications_on_folders.get_classification_metadata`](#boxclassifications_on_foldersget_classification_metadata)
    + [`box.classifications_on_folders.remove_from_folder`](#boxclassifications_on_foldersremove_from_folder)
    + [`box.classifications_on_folders.update_classification`](#boxclassifications_on_foldersupdate_classification)
    + [`box.collaborations.collaborations`](#boxcollaborationscollaborations)
    + [`box.collaborations.get_single_collaboration`](#boxcollaborationsget_single_collaboration)
    + [`box.collaborations.remove_single_collaboration`](#boxcollaborationsremove_single_collaboration)
    + [`box.collaborations.update_collaboration`](#boxcollaborationsupdate_collaboration)
    + [`box.collaborations_(list).collaborations`](#boxcollaborations_listcollaborations)
    + [`box.collaborations_(list).file_access_list`](#boxcollaborations_listfile_access_list)
    + [`box.collaborations_(list).folder_access`](#boxcollaborations_listfolder_access)
    + [`box.collaborations_(list).group_access_details`](#boxcollaborations_listgroup_access_details)
    + [`box.collections.collections`](#boxcollectionscollections)
    + [`box.collections.list_items`](#boxcollectionslist_items)
    + [`box.comments.comments`](#boxcommentscomments)
    + [`box.comments.get_by_id`](#boxcommentsget_by_id)
    + [`box.comments.list_file_comments`](#boxcommentslist_file_comments)
    + [`box.comments.remove_by_id`](#boxcommentsremove_by_id)
    + [`box.comments.update_message`](#boxcommentsupdate_message)
    + [`box.device_pinners.get_pinner_info`](#boxdevice_pinnersget_pinner_info)
    + [`box.device_pinners.list_pinner_info`](#boxdevice_pinnerslist_pinner_info)
    + [`box.device_pinners.remove_device_pin`](#boxdevice_pinnersremove_device_pin)
    + [`box.domain_restrictions_(user_exemptions).create_user_exemption_from_collaboration_domain_restrictions`](#boxdomain_restrictions_user_exemptionscreate_user_exemption_from_collaboration_domain_restrictions)
    + [`box.domain_restrictions_(user_exemptions).get_user_exemption`](#boxdomain_restrictions_user_exemptionsget_user_exemption)
    + [`box.domain_restrictions_(user_exemptions).list_exempt_users`](#boxdomain_restrictions_user_exemptionslist_exempt_users)
    + [`box.domain_restrictions_(user_exemptions).remove_exemption`](#boxdomain_restrictions_user_exemptionsremove_exemption)
    + [`box.domain_restrictions_for_collaborations.add_allowed_domain_entry`](#boxdomain_restrictions_for_collaborationsadd_allowed_domain_entry)
    + [`box.domain_restrictions_for_collaborations.allowed_collaboration_domain`](#boxdomain_restrictions_for_collaborationsallowed_collaboration_domain)
    + [`box.domain_restrictions_for_collaborations.list_allowed_collaboration_domains`](#boxdomain_restrictions_for_collaborationslist_allowed_collaboration_domains)
    + [`box.domain_restrictions_for_collaborations.remove_allowed_domain_entry`](#boxdomain_restrictions_for_collaborationsremove_allowed_domain_entry)
    + [`box.downloads.file_content_get`](#boxdownloadsfile_content_get)
    + [`box.email_aliases.create_new_alias`](#boxemail_aliasescreate_new_alias)
    + [`box.email_aliases.list_user_email_aliases`](#boxemail_aliaseslist_user_email_aliases)
    + [`box.email_aliases.remove_alias`](#boxemail_aliasesremove_alias)
    + [`box.events.events`](#boxeventsevents)
    + [`box.events.events_0`](#boxeventsevents_0)
    + [`box.file_requests.copy_request_to_folder`](#boxfile_requestscopy_request_to_folder)
    + [`box.file_requests.delete_permanently`](#boxfile_requestsdelete_permanently)
    + [`box.file_requests.get_information`](#boxfile_requestsget_information)
    + [`box.file_requests.update_request`](#boxfile_requestsupdate_request)
    + [`box.file_version_legal_holds.get_file_version_legal_hold_info`](#boxfile_version_legal_holdsget_file_version_legal_hold_info)
    + [`box.file_version_legal_holds.list_file_version_legal_holds`](#boxfile_version_legal_holdslist_file_version_legal_holds)
    + [`box.file_version_retentions.get_file_version_retention_info`](#boxfile_version_retentionsget_file_version_retention_info)
    + [`box.file_version_retentions.list_retentions`](#boxfile_version_retentionslist_retentions)
    + [`box.file_versions.get_specific_version`](#boxfile_versionsget_specific_version)
    + [`box.file_versions.list_all_versions`](#boxfile_versionslist_all_versions)
    + [`box.file_versions.move_to_trash`](#boxfile_versionsmove_to_trash)
    + [`box.file_versions.promote_file_version`](#boxfile_versionspromote_file_version)
    + [`box.file_versions.restore_version`](#boxfile_versionsrestore_version)
    + [`box.files.create_copy`](#boxfilescreate_copy)
    + [`box.files.delete_file`](#boxfilesdelete_file)
    + [`box.files.get_details`](#boxfilesget_details)
    + [`box.files.get_thumbnail`](#boxfilesget_thumbnail)
    + [`box.files.preflight_check_before_upload`](#boxfilespreflight_check_before_upload)
    + [`box.files.update_file`](#boxfilesupdate_file)
    + [`box.folder_locks.create`](#boxfolder_lockscreate)
    + [`box.folder_locks.delete_folder_lock`](#boxfolder_locksdelete_folder_lock)
    + [`box.folder_locks.list_details`](#boxfolder_lockslist_details)
    + [`box.folders.create_copy`](#boxfolderscreate_copy)
    + [`box.folders.delete_by_id`](#boxfoldersdelete_by_id)
    + [`box.folders.folders`](#boxfoldersfolders)
    + [`box.folders.get_folder_details`](#boxfoldersget_folder_details)
    + [`box.folders.list_items_in_folder`](#boxfolderslist_items_in_folder)
    + [`box.folders.update_folder`](#boxfoldersupdate_folder)
    + [`box.group_memberships.create_membership`](#boxgroup_membershipscreate_membership)
    + [`box.group_memberships.get_all`](#boxgroup_membershipsget_all)
    + [`box.group_memberships.get_specific_membership`](#boxgroup_membershipsget_specific_membership)
    + [`box.group_memberships.list_members_of_group`](#boxgroup_membershipslist_members_of_group)
    + [`box.group_memberships.remove_user_from_group`](#boxgroup_membershipsremove_user_from_group)
    + [`box.group_memberships.update_membership`](#boxgroup_membershipsupdate_membership)
    + [`box.groups.get_info`](#boxgroupsget_info)
    + [`box.groups.groups`](#boxgroupsgroups)
    + [`box.groups.groups_0`](#boxgroupsgroups_0)
    + [`box.groups.remove`](#boxgroupsremove)
    + [`box.groups.update_group`](#boxgroupsupdate_group)
    + [`box.integration_mappings.create_slack_mapping`](#boxintegration_mappingscreate_slack_mapping)
    + [`box.integration_mappings.delete_slack_mapping`](#boxintegration_mappingsdelete_slack_mapping)
    + [`box.integration_mappings.list_slack_mappings`](#boxintegration_mappingslist_slack_mappings)
    + [`box.integration_mappings.update_slack_mapping`](#boxintegration_mappingsupdate_slack_mapping)
    + [`box.invites.get_user_invite_status`](#boxinvitesget_user_invite_status)
    + [`box.invites.invites`](#boxinvitesinvites)
    + [`box.legal_hold_policies.create_new_policy`](#boxlegal_hold_policiescreate_new_policy)
    + [`box.legal_hold_policies.get_policy`](#boxlegal_hold_policiesget_policy)
    + [`box.legal_hold_policies.list_all`](#boxlegal_hold_policieslist_all)
    + [`box.legal_hold_policies.remove_policy`](#boxlegal_hold_policiesremove_policy)
    + [`box.legal_hold_policies.update_policy`](#boxlegal_hold_policiesupdate_policy)
    + [`box.legal_hold_policy_assignments.assign_file_legal_hold`](#boxlegal_hold_policy_assignmentsassign_file_legal_hold)
    + [`box.legal_hold_policy_assignments.get_assignment`](#boxlegal_hold_policy_assignmentsget_assignment)
    + [`box.legal_hold_policy_assignments.get_list_items`](#boxlegal_hold_policy_assignmentsget_list_items)
    + [`box.legal_hold_policy_assignments.list_file_versions`](#boxlegal_hold_policy_assignmentslist_file_versions)
    + [`box.legal_hold_policy_assignments.list_previous_file_versions`](#boxlegal_hold_policy_assignmentslist_previous_file_versions)
    + [`box.legal_hold_policy_assignments.unassign_policy`](#boxlegal_hold_policy_assignmentsunassign_policy)
    + [`box.metadata_cascade_policies.apply_to_children`](#boxmetadata_cascade_policiesapply_to_children)
    + [`box.metadata_cascade_policies.create_policy`](#boxmetadata_cascade_policiescreate_policy)
    + [`box.metadata_cascade_policies.get_policy_assigned_to_folder`](#boxmetadata_cascade_policiesget_policy_assigned_to_folder)
    + [`box.metadata_cascade_policies.list`](#boxmetadata_cascade_policieslist)
    + [`box.metadata_cascade_policies.remove_policy`](#boxmetadata_cascade_policiesremove_policy)
    + [`box.metadata_instances_(files).apply_template`](#boxmetadata_instances_filesapply_template)
    + [`box.metadata_instances_(files).get_instance`](#boxmetadata_instances_filesget_instance)
    + [`box.metadata_instances_(files).list_file_metadata`](#boxmetadata_instances_fileslist_file_metadata)
    + [`box.metadata_instances_(files).remove_instance`](#boxmetadata_instances_filesremove_instance)
    + [`box.metadata_instances_(files).update_instance_on_file`](#boxmetadata_instances_filesupdate_instance_on_file)
    + [`box.metadata_instances_(folders).apply_template`](#boxmetadata_instances_foldersapply_template)
    + [`box.metadata_instances_(folders).get_folder_metadata_instance`](#boxmetadata_instances_foldersget_folder_metadata_instance)
    + [`box.metadata_instances_(folders).list_on_folder`](#boxmetadata_instances_folderslist_on_folder)
    + [`box.metadata_instances_(folders).remove_instance`](#boxmetadata_instances_foldersremove_instance)
    + [`box.metadata_instances_(folders).update_instance_on_folder`](#boxmetadata_instances_foldersupdate_instance_on_folder)
    + [`box.metadata_templates.create_new_template`](#boxmetadata_templatescreate_new_template)
    + [`box.metadata_templates.delete_schema`](#boxmetadata_templatesdelete_schema)
    + [`box.metadata_templates.find_by_instance_id`](#boxmetadata_templatesfind_by_instance_id)
    + [`box.metadata_templates.get_by_id`](#boxmetadata_templatesget_by_id)
    + [`box.metadata_templates.get_by_name_schema`](#boxmetadata_templatesget_by_name_schema)
    + [`box.metadata_templates.list_for_enterprise`](#boxmetadata_templateslist_for_enterprise)
    + [`box.metadata_templates.list_global`](#boxmetadata_templateslist_global)
    + [`box.metadata_templates.update_schema`](#boxmetadata_templatesupdate_schema)
    + [`box.recent_items.list_accessed_items`](#boxrecent_itemslist_accessed_items)
    + [`box.retention_policies.create_policy`](#boxretention_policiescreate_policy)
    + [`box.retention_policies.delete_policy`](#boxretention_policiesdelete_policy)
    + [`box.retention_policies.get_policy`](#boxretention_policiesget_policy)
    + [`box.retention_policies.list_all`](#boxretention_policieslist_all)
    + [`box.retention_policies.update_policy`](#boxretention_policiesupdate_policy)
    + [`box.retention_policy_assignments.create_retention_assignment`](#boxretention_policy_assignmentscreate_retention_assignment)
    + [`box.retention_policy_assignments.get_assignment`](#boxretention_policy_assignmentsget_assignment)
    + [`box.retention_policy_assignments.list_all_assignments`](#boxretention_policy_assignmentslist_all_assignments)
    + [`box.retention_policy_assignments.list_file_versions_under_retention`](#boxretention_policy_assignmentslist_file_versions_under_retention)
    + [`box.retention_policy_assignments.list_files_under_retention`](#boxretention_policy_assignmentslist_files_under_retention)
    + [`box.retention_policy_assignments.remove_assignment`](#boxretention_policy_assignmentsremove_assignment)
    + [`box.search.items_by_metadata`](#boxsearchitems_by_metadata)
    + [`box.search.search`](#boxsearchsearch)
    + [`box.session_termination.create_session_termination_jobs`](#boxsession_terminationcreate_session_termination_jobs)
    + [`box.session_termination.create_termination_jobs`](#boxsession_terminationcreate_termination_jobs)
    + [`box.shared_links_(files).add_shared_link_to_file`](#boxshared_links_filesadd_shared_link_to_file)
    + [`box.shared_links_(files).get_by_shared_link`](#boxshared_links_filesget_by_shared_link)
    + [`box.shared_links_(files).get_shared_link_info`](#boxshared_links_filesget_shared_link_info)
    + [`box.shared_links_(files).remove_shared_link`](#boxshared_links_filesremove_shared_link)
    + [`box.shared_links_(files).update_link_on_file`](#boxshared_links_filesupdate_link_on_file)
    + [`box.shared_links_(folders).add_link_to_folder`](#boxshared_links_foldersadd_link_to_folder)
    + [`box.shared_links_(folders).find_folder_by_shared_link`](#boxshared_links_foldersfind_folder_by_shared_link)
    + [`box.shared_links_(folders).get_shared_link_for_folder`](#boxshared_links_foldersget_shared_link_for_folder)
    + [`box.shared_links_(folders).remove_from_folder`](#boxshared_links_foldersremove_from_folder)
    + [`box.shared_links_(folders).update_folder_shared_link`](#boxshared_links_foldersupdate_folder_shared_link)
    + [`box.shared_links_(web_links).add_link_to_web_link`](#boxshared_links_web_linksadd_link_to_web_link)
    + [`box.shared_links_(web_links).find_shared_web_link`](#boxshared_links_web_linksfind_shared_web_link)
    + [`box.shared_links_(web_links).get_link_info`](#boxshared_links_web_linksget_link_info)
    + [`box.shared_links_(web_links).remove_shared_link`](#boxshared_links_web_linksremove_shared_link)
    + [`box.shared_links_(web_links).update_shared_link`](#boxshared_links_web_linksupdate_shared_link)
    + [`box.shield_information_barrier_reports.create_report`](#boxshield_information_barrier_reportscreate_report)
    + [`box.shield_information_barrier_reports.get_by_id`](#boxshield_information_barrier_reportsget_by_id)
    + [`box.shield_information_barrier_reports.list_reports`](#boxshield_information_barrier_reportslist_reports)
    + [`box.shield_information_barrier_segment_members.create_new_member`](#boxshield_information_barrier_segment_memberscreate_new_member)
    + [`box.shield_information_barrier_segment_members.get_by_id`](#boxshield_information_barrier_segment_membersget_by_id)
    + [`box.shield_information_barrier_segment_members.list_segment_members_based_on_ids`](#boxshield_information_barrier_segment_memberslist_segment_members_based_on_ids)
    + [`box.shield_information_barrier_segment_members.remove_by_id`](#boxshield_information_barrier_segment_membersremove_by_id)
    + [`box.shield_information_barrier_segment_restrictions.create_barrier_object`](#boxshield_information_barrier_segment_restrictionscreate_barrier_object)
    + [`box.shield_information_barrier_segment_restrictions.get_by_id`](#boxshield_information_barrier_segment_restrictionsget_by_id)
    + [`box.shield_information_barrier_segment_restrictions.list_based_on_segment_id`](#boxshield_information_barrier_segment_restrictionslist_based_on_segment_id)
    + [`box.shield_information_barrier_segment_restrictions.remove_by_id`](#boxshield_information_barrier_segment_restrictionsremove_by_id)
    + [`box.shield_information_barrier_segments.create_segment`](#boxshield_information_barrier_segmentscreate_segment)
    + [`box.shield_information_barrier_segments.delete_segment_by_id`](#boxshield_information_barrier_segmentsdelete_segment_by_id)
    + [`box.shield_information_barrier_segments.get_by_id`](#boxshield_information_barrier_segmentsget_by_id)
    + [`box.shield_information_barrier_segments.list_information_objects`](#boxshield_information_barrier_segmentslist_information_objects)
    + [`box.shield_information_barrier_segments.update_by_id`](#boxshield_information_barrier_segmentsupdate_by_id)
    + [`box.shield_information_barriers.add_changed_status`](#boxshield_information_barriersadd_changed_status)
    + [`box.shield_information_barriers.create_barrier`](#boxshield_information_barrierscreate_barrier)
    + [`box.shield_information_barriers.get_by_id`](#boxshield_information_barriersget_by_id)
    + [`box.shield_information_barriers.list_information_objects`](#boxshield_information_barrierslist_information_objects)
    + [`box.sign_requests.cancel_request`](#boxsign_requestscancel_request)
    + [`box.sign_requests.create_request`](#boxsign_requestscreate_request)
    + [`box.sign_requests.get_by_id`](#boxsign_requestsget_by_id)
    + [`box.sign_requests.list`](#boxsign_requestslist)
    + [`box.sign_requests.resend_sign_request_emails`](#boxsign_requestsresend_sign_request_emails)
    + [`box.sign_templates.get_details`](#boxsign_templatesget_details)
    + [`box.sign_templates.list_templates`](#boxsign_templateslist_templates)
    + [`box.skills.apply_box_skill_cards`](#boxskillsapply_box_skill_cards)
    + [`box.skills.list_box_skill_cards`](#boxskillslist_box_skill_cards)
    + [`box.skills.remove_box_skill_cards`](#boxskillsremove_box_skill_cards)
    + [`box.skills.update_all_box_skill_cards`](#boxskillsupdate_all_box_skill_cards)
    + [`box.skills.update_box_skill_cards_on_file`](#boxskillsupdate_box_skill_cards_on_file)
    + [`box.standard_and_zones_storage_policies.get_specific`](#boxstandard_and_zones_storage_policiesget_specific)
    + [`box.standard_and_zones_storage_policies.list_policies`](#boxstandard_and_zones_storage_policieslist_policies)
    + [`box.standard_and_zones_storage_policy_assignments.create_assignment`](#boxstandard_and_zones_storage_policy_assignmentscreate_assignment)
    + [`box.standard_and_zones_storage_policy_assignments.get_specific_assignment`](#boxstandard_and_zones_storage_policy_assignmentsget_specific_assignment)
    + [`box.standard_and_zones_storage_policy_assignments.list_assignments`](#boxstandard_and_zones_storage_policy_assignmentslist_assignments)
    + [`box.standard_and_zones_storage_policy_assignments.unassign_storage_policy`](#boxstandard_and_zones_storage_policy_assignmentsunassign_storage_policy)
    + [`box.standard_and_zones_storage_policy_assignments.update_specific_assignment`](#boxstandard_and_zones_storage_policy_assignmentsupdate_specific_assignment)
    + [`box.task_assignments.assign_multiple_users`](#boxtask_assignmentsassign_multiple_users)
    + [`box.task_assignments.delete_specific_assignment`](#boxtask_assignmentsdelete_specific_assignment)
    + [`box.task_assignments.get_task_assignment_info`](#boxtask_assignmentsget_task_assignment_info)
    + [`box.task_assignments.list_for_task`](#boxtask_assignmentslist_for_task)
    + [`box.task_assignments.update_state_assigned_to_user`](#boxtask_assignmentsupdate_state_assigned_to_user)
    + [`box.tasks.get_info`](#boxtasksget_info)
    + [`box.tasks.list_on_file`](#boxtaskslist_on_file)
    + [`box.tasks.remove_file`](#boxtasksremove_file)
    + [`box.tasks.tasks`](#boxtaskstasks)
    + [`box.tasks.update_task_configuration`](#boxtasksupdate_task_configuration)
    + [`box.terms_of_service.create_for_enterprise_and_type`](#boxterms_of_servicecreate_for_enterprise_and_type)
    + [`box.terms_of_service.get_settings`](#boxterms_of_serviceget_settings)
    + [`box.terms_of_service.get_specific`](#boxterms_of_serviceget_specific)
    + [`box.terms_of_service.update_specific_term`](#boxterms_of_serviceupdate_specific_term)
    + [`box.terms_of_service_user_statuses.create_user_status`](#boxterms_of_service_user_statusescreate_user_status)
    + [`box.terms_of_service_user_statuses.list_user_statuses`](#boxterms_of_service_user_statuseslist_user_statuses)
    + [`box.terms_of_service_user_statuses.update_user_status`](#boxterms_of_service_user_statusesupdate_user_status)
    + [`box.transfer_folders.to_destination`](#boxtransfer_foldersto_destination)
    + [`box.trashed_files.get_file`](#boxtrashed_filesget_file)
    + [`box.trashed_files.permanently_remove_file`](#boxtrashed_filespermanently_remove_file)
    + [`box.trashed_files.restore_file`](#boxtrashed_filesrestore_file)
    + [`box.trashed_folders.getd_folder`](#boxtrashed_foldersgetd_folder)
    + [`box.trashed_folders.permanently_remove_folder`](#boxtrashed_folderspermanently_remove_folder)
    + [`box.trashed_folders.restore_folder`](#boxtrashed_foldersrestore_folder)
- [Folder locking](#folder-locking)
    + [`box.trashed_items.list_retrieved_items`](#boxtrashed_itemslist_retrieved_items)
    + [`box.trashed_web_links.get_trashed_link`](#boxtrashed_web_linksget_trashed_link)
    + [`box.trashed_web_links.permanently_remove`](#boxtrashed_web_linkspermanently_remove)
    + [`box.trashed_web_links.restore_web_link`](#boxtrashed_web_linksrestore_web_link)
    + [`box.uploads.file_content_update`](#boxuploadsfile_content_update)
- [Request body order](#request-body-order)
    + [`box.uploads.small_file`](#boxuploadssmall_file)
- [Request body order](#request-body-order-1)
    + [`box.uploads_(chunked).commit_session`](#boxuploads_chunkedcommit_session)
    + [`box.uploads_(chunked).create_session_for_upload`](#boxuploads_chunkedcreate_session_for_upload)
    + [`box.uploads_(chunked).create_session_for_upload_0`](#boxuploads_chunkedcreate_session_for_upload_0)
    + [`box.uploads_(chunked).file_part_update`](#boxuploads_chunkedfile_part_update)
    + [`box.uploads_(chunked).info`](#boxuploads_chunkedinfo)
    + [`box.uploads_(chunked).list_parts`](#boxuploads_chunkedlist_parts)
    + [`box.uploads_(chunked).remove_upload_session`](#boxuploads_chunkedremove_upload_session)
    + [`box.user_avatars.add_or_update_image`](#boxuser_avatarsadd_or_update_image)
    + [`box.user_avatars.get_image`](#boxuser_avatarsget_image)
    + [`box.user_avatars.remove_existing`](#boxuser_avatarsremove_existing)
    + [`box.users.delete_user`](#boxusersdelete_user)
    + [`box.users.get_current_user`](#boxusersget_current_user)
    + [`box.users.get_user_info`](#boxusersget_user_info)
    + [`box.users.update_managed_user`](#boxusersupdate_managed_user)
    + [`box.users.users`](#boxusersusers)
    + [`box.users.users_0`](#boxusersusers_0)
    + [`box.watermarks_(files).apply_watermark_to_file`](#boxwatermarks_filesapply_watermark_to_file)
    + [`box.watermarks_(files).get`](#boxwatermarks_filesget)
    + [`box.watermarks_(files).remove_watermark`](#boxwatermarks_filesremove_watermark)
    + [`box.watermarks_(folders).apply_to_folder`](#boxwatermarks_foldersapply_to_folder)
    + [`box.watermarks_(folders).get_folder_watermark`](#boxwatermarks_foldersget_folder_watermark)
    + [`box.watermarks_(folders).remove_folder_watermark`](#boxwatermarks_foldersremove_folder_watermark)
    + [`box.web_links.create_object`](#boxweb_linkscreate_object)
    + [`box.web_links.get_information`](#boxweb_linksget_information)
    + [`box.web_links.remove_link`](#boxweb_linksremove_link)
    + [`box.web_links.update_object`](#boxweb_linksupdate_object)
    + [`box.webhooks.get_specific_webhook`](#boxwebhooksget_specific_webhook)
    + [`box.webhooks.remove`](#boxwebhooksremove)
    + [`box.webhooks.update_webhook`](#boxwebhooksupdate_webhook)
    + [`box.webhooks.webhooks`](#boxwebhookswebhooks)
    + [`box.webhooks.webhooks_0`](#boxwebhookswebhooks_0)
    + [`box.workflows.start_based_on_request`](#boxworkflowsstart_based_on_request)
    + [`box.workflows.workflows`](#boxworkflowsworkflows)
    + [`box.zip_downloads.create_request`](#boxzip_downloadscreate_request)
    + [`box.zip_downloads.get_content_by_id`](#boxzip_downloadsget_content_by_id)
    + [`box.zip_downloads.get_status`](#boxzip_downloadsget_status)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Box&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from box_python_sdk import Box, ApiException

box = Box(
)

try:
    # Authorize user
    authorize_response = box.authorization.authorize(
        response_type="code",
        client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
        redirect_uri="http://example.com/auth/callback",
        state="my_state",
        scope="admin_readwrite",
    )
except ApiException as e:
    print("Exception when calling AuthorizationApi.authorize: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from box_python_sdk import Box, ApiException

box = Box(
)

async def main():
    try:
        # Authorize user
        authorize_response = await box.authorization.aauthorize(
            response_type="code",
            client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
            redirect_uri="http://example.com/auth/callback",
            state="my_state",
            scope="admin_readwrite",
        )
    except ApiException as e:
        print("Exception when calling AuthorizationApi.authorize: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from box_python_sdk import Box, ApiException

box = Box(
)

try:
    # Authorize user
    authorize_response = box.authorization.raw.authorize(
        response_type="code",
        client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
        redirect_uri="http://example.com/auth/callback",
        state="my_state",
        scope="admin_readwrite",
    )
    pprint(authorize_response.headers)
    pprint(authorize_response.status)
    pprint(authorize_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AuthorizationApi.authorize: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `box.authorization.authorize`<a id="boxauthorizationauthorize"></a>

Authorize a user by sending them through the [Box](https://box.com)
website and request their permission to act on their behalf.

This is the first step when authenticating a user using
OAuth 2.0. To request a user's authorization to use the Box APIs
on their behalf you will need to send a user to the URL with this
format.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authorize_response = box.authorization.authorize(
    response_type="code",
    client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
    redirect_uri="http://example.com/auth/callback",
    state="my_state",
    scope="admin_readwrite",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### response_type: `str`<a id="response_type-str"></a>

The type of response we'd like to receive.

##### client_id: `str`<a id="client_id-str"></a>

The Client ID of the application that is requesting to authenticate the user. To get the Client ID for your application, log in to your Box developer console and click the **Edit Application** link for the application you're working with. In the OAuth 2.0 Parameters section of the configuration page, find the item labelled `client_id`. The text of that item is your application's Client ID.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The URI to which Box redirects the browser after the user has granted or denied the application permission. This URI match one of the redirect URIs in the configuration of your application. It must be a valid HTTPS URI and it needs to be able to handle the redirection to complete the next step in the OAuth 2.0 flow. Although this parameter is optional, it must be a part of the authorization URL if you configured multiple redirect URIs for the application in the developer console. A missing parameter causes a `redirect_uri_missing` error after the user grants application access.

##### state: `str`<a id="state-str"></a>

A custom string of your choice. Box will pass the same string to the redirect URL when authentication is complete. This parameter can be used to identify a user on redirect, as well as protect against hijacked sessions and other exploits.

##### scope: `str`<a id="scope-str"></a>

A space-separated list of application scopes you'd like to authenticate the user for. This defaults to all the scopes configured for the application in its configuration page.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/authorize` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.authorization.refresh_access_token`<a id="boxauthorizationrefresh_access_token"></a>

Refresh an Access Token using its client ID, secret, and refresh token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_access_token_response = box.authorization.refresh_access_token(
    grant_type="refresh_token",
    client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
    client_secret="hOzsTeFlT6ko0dme22uGbQal04SBPYc1",
    refresh_token="c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

The type of request being made, in this case a refresh request.

##### client_id: `str`<a id="client_id-str"></a>

The client ID of the application requesting to refresh the token.

##### client_secret: `str`<a id="client_secret-str"></a>

The client secret of the application requesting to refresh the token.

##### refresh_token: `str`<a id="refresh_token-str"></a>

The refresh token to refresh.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostOAuth2TokenRefreshAccessToken`](./box_python_sdk/type/post_o_auth2_token_refresh_access_token.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessToken`](./box_python_sdk/pydantic/access_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth2/token#refresh` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.authorization.request_access_token`<a id="boxauthorizationrequest_access_token"></a>

Request an Access Token using either a client-side obtained OAuth 2.0
authorization code or a server-side JWT assertion.

An Access Token is a string that enables Box to verify that a
request belongs to an authorized session. In the normal order of
operations you will begin by requesting authentication from the
[authorize](https://raw.githubusercontent.com) endpoint and Box will send you an
authorization code.

You will then send this code to this endpoint to exchange it for
an Access Token. The returned Access Token can then be used to to make
Box API calls.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_access_token_response = box.authorization.request_access_token(
    grant_type="authorization_code",
    client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
    client_secret="hOzsTeFlT6ko0dme22uGbQal04SBPYc1",
    code="n22JPxrh18m4Y0wIZPIqYZK7VRrsMTWW",
    refresh_token="c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ",
    assertion="xxxxx.yyyyy.zzzzz",
    subject_token="c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ",
    subject_token_type="urn:ietf:params:oauth:token-type:access_token",
    actor_token="c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ",
    actor_token_type="urn:ietf:params:oauth:token-type:id_token",
    scope="item_upload item_preview base_explorer",
    resource="https://api.box.com/2.0/files/123456",
    box_subject_type="enterprise",
    box_subject_id="123456789",
    box_shared_link="https://cloud.box.com/s/123456",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

The type of request being made, either using a client-side obtained authorization code, a refresh token, a JWT assertion, client credentials grant or another access token for the purpose of downscoping a token.

##### client_id: `str`<a id="client_id-str"></a>

The Client ID of the application requesting an access token.  Used in combination with `authorization_code`, `client_credentials`, or `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.

##### client_secret: `str`<a id="client_secret-str"></a>

The client secret of the application requesting an access token.  Used in combination with `authorization_code`, `client_credentials`, or `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.

##### code: `str`<a id="code-str"></a>

The client-side authorization code passed to your application by Box in the browser redirect after the user has successfully granted your application permission to make API calls on their behalf.  Used in combination with `authorization_code` as the `grant_type`.

##### refresh_token: `str`<a id="refresh_token-str"></a>

A refresh token used to get a new access token with.  Used in combination with `refresh_token` as the `grant_type`.

##### assertion: `str`<a id="assertion-str"></a>

A JWT assertion for which to request a new access token.  Used in combination with `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.

##### subject_token: `str`<a id="subject_token-str"></a>

The token to exchange for a downscoped token. This can be a regular access token, a JWT assertion, or an app token.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.

##### subject_token_type: `str`<a id="subject_token_type-str"></a>

The type of `subject_token` passed in.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.

##### actor_token: `str`<a id="actor_token-str"></a>

The token used to create an annotator token. This is a JWT assertion.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.

##### actor_token_type: `str`<a id="actor_token_type-str"></a>

The type of `actor_token` passed in.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.

##### scope: `str`<a id="scope-str"></a>

The space-delimited list of scopes that you want apply to the new access token.  The `subject_token` will need to have all of these scopes or the call will error with **401 Unauthorized**.

##### resource: `str`<a id="resource-str"></a>

Full URL for the file that the token should be generated for.

##### box_subject_type: `str`<a id="box_subject_type-str"></a>

Used in combination with `client_credentials` as the `grant_type`.

##### box_subject_id: `str`<a id="box_subject_id-str"></a>

Used in combination with `client_credentials` as the `grant_type`. Value is determined by `box_subject_type`. If `user` use user ID and if `enterprise` use enterprise ID.

##### box_shared_link: `str`<a id="box_shared_link-str"></a>

Full URL of the shared link on the file or folder that the token should be generated for.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostOAuth2Token`](./box_python_sdk/type/post_o_auth2_token.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessToken`](./box_python_sdk/pydantic/access_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.authorization.revoke_access_token`<a id="boxauthorizationrevoke_access_token"></a>

Revoke an active Access Token, effectively logging a user out
that has been previously authenticated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.authorization.revoke_access_token(
    client_id="ly1nj6n11vionaie65emwzk575hnnmrk",
    client_secret="hOzsTeFlT6ko0dme22uGbQal04SBPYc1",
    token="n22JPxrh18m4Y0wIZPIqYZK7VRrsMTWW",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

The Client ID of the application requesting to revoke the access token.

##### client_secret: `str`<a id="client_secret-str"></a>

The client secret of the application requesting to revoke an access token.

##### token: `str`<a id="token-str"></a>

The access token to revoke.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostOAuth2Revoke`](./box_python_sdk/type/post_o_auth2_revoke.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth2/revoke` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications.add_new_classifications`<a id="boxclassificationsadd_new_classifications"></a>

Adds one or more new classifications to the list of classifications
available to the enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_classifications_response = box.classifications.add_new_classifications(
    body=[
        {
            "op": "addEnumOption",
            "field_key": "Box__Security__Classification__Key",
            "data": {
                "key": "Sensitive",
            },
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClassificationsAddNewClassificationsRequest`](./box_python_sdk/type/classifications_add_new_classifications_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClassificationTemplate`](./box_python_sdk/pydantic/classification_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#add` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications.initialize_template`<a id="boxclassificationsinitialize_template"></a>

When an enterprise does not yet have any classifications, this API call
initializes the classification template with an initial set of
classifications.

If an enterprise already has a classification, the template will already
exist and instead an API call should be made to add additional
classifications.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initialize_template_response = box.classifications.initialize_template(
    scope="enterprise",
    template_key="securityClassification-6VMVochwUWo",
    display_name="Classification",
    fields=[
        {
            "type": "enum",
            "key": "Box__Security__Classification__Key",
            "display_name": "Classification",
            "hidden": False,
            "options": [
                {
                    "key": "Sensitive",
                }
            ],
        }
    ],
    hidden=False,
    copy_instance_on_item_copy=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

The scope in which to create the classifications. This should be `enterprise` or `enterprise_{id}` where `id` is the unique ID of the enterprise.

##### template_key: `str`<a id="template_key-str"></a>

Defines the list of metadata templates.

##### display_name: `str`<a id="display_name-str"></a>

The name of the template as shown in web and mobile interfaces.

##### fields: [`ClassificationsInitializeTemplateRequestFields`](./box_python_sdk/type/classifications_initialize_template_request_fields.py)<a id="fields-classificationsinitializetemplaterequestfieldsbox_python_sdktypeclassifications_initialize_template_request_fieldspy"></a>

##### hidden: `bool`<a id="hidden-bool"></a>

Determines if the classification template is hidden or available on web and mobile devices.

##### copy_instance_on_item_copy: `bool`<a id="copy_instance_on_item_copy-bool"></a>

Determines if classifications are copied along when the file or folder is copied.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClassificationsInitializeTemplateRequest`](./box_python_sdk/type/classifications_initialize_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClassificationTemplate`](./box_python_sdk/pydantic/classification_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/schema#classifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications.list_all_classifications`<a id="boxclassificationslist_all_classifications"></a>

Retrieves the classification metadata template and lists all the
classifications available to this enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_classifications_response = box.classifications.list_all_classifications()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ClassificationTemplate`](./box_python_sdk/pydantic/classification_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications.update_labels_descriptions`<a id="boxclassificationsupdate_labels_descriptions"></a>

Updates the labels and descriptions of one or more classifications
available to the enterprise.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_labels_descriptions_response = box.classifications.update_labels_descriptions(
    body=[
        {
            "op": "editEnumOption",
            "field_key": "Box__Security__Classification__Key",
            "enum_option_key": "Sensitive",
            "data": {
                "key": "Very Sensitive",
            },
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClassificationsUpdateLabelsDescriptionsRequest`](./box_python_sdk/type/classifications_update_labels_descriptions_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ClassificationTemplate`](./box_python_sdk/pydantic/classification_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#update` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_files.add_classification`<a id="boxclassifications_on_filesadd_classification"></a>

Adds a classification to a file by specifying the label of the
classification to add.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_classification_response = box.classifications_on_files.add_classification(
    file_id="12345",
    box__security__classification__key="Sensitive",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### box__security__classification__key: `str`<a id="box__security__classification__key-str"></a>

The name of the classification to apply to this file.  To list the available classifications in an enterprise, use the classification API to retrieve the [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema) which lists all available classification keys.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClassificationsOnFilesAddClassificationRequest`](./box_python_sdk/type/classifications_on_files_add_classification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./box_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_files.get_classification_metadata_instance`<a id="boxclassifications_on_filesget_classification_metadata_instance"></a>

Retrieves the classification metadata instance that
has been applied to a file.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_classification_metadata_instance_response = box.classifications_on_files.get_classification_metadata_instance(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./box_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_files.remove_classification`<a id="boxclassifications_on_filesremove_classification"></a>

Removes any classifications from a file.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.classifications_on_files.remove_classification(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_files.update_classification_metadata_instance`<a id="boxclassifications_on_filesupdate_classification_metadata_instance"></a>

Updates a classification on a file.

The classification can only be updated if a classification has already been
applied to the file before. When editing classifications, only values are
defined for the enterprise will be accepted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_classification_metadata_instance_response = box.classifications_on_files.update_classification_metadata_instance(
    body=[
        {
            "op": "replace",
            "path": "/Box__Security__Classification__Key",
            "value": "Sensitive",
        }
    ],
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### requestBody: [`ClassificationsOnFilesUpdateClassificationMetadataInstanceRequest`](./box_python_sdk/type/classifications_on_files_update_classification_metadata_instance_request.py)<a id="requestbody-classificationsonfilesupdateclassificationmetadatainstancerequestbox_python_sdktypeclassifications_on_files_update_classification_metadata_instance_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./box_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_folders.add_classification_to_folder`<a id="boxclassifications_on_foldersadd_classification_to_folder"></a>

Adds a classification to a folder by specifying the label of the
classification to add.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_classification_to_folder_response = box.classifications_on_folders.add_classification_to_folder(
    folder_id="12345",
    box__security__classification__key="Sensitive",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### box__security__classification__key: `str`<a id="box__security__classification__key-str"></a>

The name of the classification to apply to this folder.  To list the available classifications in an enterprise, use the classification API to retrieve the [classification template](e://get_metadata_templates_enterprise_securityClassification-6VMVochwUWo_schema) which lists all available classification keys.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ClassificationsOnFoldersAddClassificationToFolderRequest`](./box_python_sdk/type/classifications_on_folders_add_classification_to_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./box_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_folders.get_classification_metadata`<a id="boxclassifications_on_foldersget_classification_metadata"></a>

Retrieves the classification metadata instance that
has been applied to a folder.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_classification_metadata_response = box.classifications_on_folders.get_classification_metadata(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./box_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_folders.remove_from_folder`<a id="boxclassifications_on_foldersremove_from_folder"></a>

Removes any classifications from a folder.

This API can also be called by including the enterprise ID in the
URL explicitly, for example
`/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.classifications_on_folders.remove_from_folder(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.classifications_on_folders.update_classification`<a id="boxclassifications_on_foldersupdate_classification"></a>

Updates a classification on a folder.

The classification can only be updated if a classification has already been
applied to the folder before. When editing classifications, only values are
defined for the enterprise will be accepted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_classification_response = box.classifications_on_folders.update_classification(
    body=[
        {
            "op": "replace",
            "path": "/Box__Security__Classification__Key",
            "value": "Sensitive",
        }
    ],
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### requestBody: [`ClassificationsOnFoldersUpdateClassificationRequest`](./box_python_sdk/type/classifications_on_folders_update_classification_request.py)<a id="requestbody-classificationsonfoldersupdateclassificationrequestbox_python_sdktypeclassifications_on_folders_update_classification_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Classification`](./box_python_sdk/pydantic/classification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations.collaborations`<a id="boxcollaborationscollaborations"></a>

Adds a collaboration for a single user or a single group to a file
or folder.

Collaborations can be created using email address, user IDs, or a
group IDs.

If a collaboration is being created with a group, access to
this endpoint is dependent on the group's ability to be invited.

If collaboration is in `pending` status, the following fields
are redacted:
- `login` and `name` are hidden if a collaboration was created
using `user_id`,
-  `name` is hidden if a collaboration was created using `login`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
collaborations_response = box.collaborations.collaborations(
    item={
        "type": "file",
        "id": "11446498",
    },
    accessible_by={
        "type": "user",
        "id": "23522323",
        "login": "john@example.com",
    },
    role="editor",
    is_access_only=True,
    can_view_path=True,
    expires_at="2019-08-29T23:59:00-07:00",
    fields=["id", "type", "name"],
    notify=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### item: [`PostCollaborationsRequestItem`](./box_python_sdk/type/post_collaborations_request_item.py)<a id="item-postcollaborationsrequestitembox_python_sdktypepost_collaborations_request_itempy"></a>


##### accessible_by: [`PostCollaborationsRequestAccessibleBy`](./box_python_sdk/type/post_collaborations_request_accessible_by.py)<a id="accessible_by-postcollaborationsrequestaccessiblebybox_python_sdktypepost_collaborations_request_accessible_bypy"></a>


##### role: `str`<a id="role-str"></a>

The level of access granted.

##### is_access_only: `bool`<a id="is_access_only-bool"></a>

If set to `true`, collaborators have access to shared items, but such items won't be visible in the All Files list. Additionally, collaborators won't see the the path to the root folder for the shared item.

##### can_view_path: `bool`<a id="can_view_path-bool"></a>

Determines if the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore can not see content the user is not collaborated on.  Be aware that this meaningfully increases the time required to load the invitee's **All Files** page. We recommend you limit the number of collaborations with `can_view_path` enabled to 1,000 per user.  Only owner or co-owners can invite collaborators with a `can_view_path` of `true`.  `can_view_path` can only be used for folder collaborations.

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

Set the expiration date for the collaboration. At this date, the collaboration will be automatically removed from the item.  This feature will only work if the **Automatically remove invited collaborators: Allow folder owners to extend the expiry date** setting has been enabled in the **Enterprise Settings** of the **Admin Console**. When the setting is not enabled, collaborations can not have an expiry date and a value for this field will be result in an error.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### notify: `bool`<a id="notify-bool"></a>

Determines if users should receive email notification for the action performed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostCollaborationsRequest`](./box_python_sdk/type/post_collaborations_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Collaboration`](./box_python_sdk/pydantic/collaboration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaborations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations.get_single_collaboration`<a id="boxcollaborationsget_single_collaboration"></a>

Retrieves a single collaboration.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_collaboration_response = box.collaborations.get_single_collaboration(
    collaboration_id="1234",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collaboration_id: `str`<a id="collaboration_id-str"></a>

The ID of the collaboration

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`Collaboration`](./box_python_sdk/pydantic/collaboration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaborations/{collaboration_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations.remove_single_collaboration`<a id="boxcollaborationsremove_single_collaboration"></a>

Deletes a single collaboration.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.collaborations.remove_single_collaboration(
    collaboration_id="1234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collaboration_id: `str`<a id="collaboration_id-str"></a>

The ID of the collaboration

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaborations/{collaboration_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations.update_collaboration`<a id="boxcollaborationsupdate_collaboration"></a>

Updates a collaboration.
Can be used to change the owner of an item, or to
accept collaboration invites.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_collaboration_response = box.collaborations.update_collaboration(
    role="editor",
    collaboration_id="1234",
    status="accepted",
    expires_at="2019-08-29T23:59:00-07:00",
    can_view_path=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role: `str`<a id="role-str"></a>

The level of access granted.

##### collaboration_id: `str`<a id="collaboration_id-str"></a>

The ID of the collaboration

##### status: `str`<a id="status-str"></a>

<!--alex ignore reject--> Set the status of a `pending` collaboration invitation, effectively accepting, or rejecting the invite.

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

Update the expiration date for the collaboration. At this date, the collaboration will be automatically removed from the item.  This feature will only work if the **Automatically remove invited collaborators: Allow folder owners to extend the expiry date** setting has been enabled in the **Enterprise Settings** of the **Admin Console**. When the setting is not enabled, collaborations can not have an expiry date and a value for this field will be result in an error.  Additionally, a collaboration can only be given an expiration if it was created after the **Automatically remove invited collaborator** setting was enabled.

##### can_view_path: `bool`<a id="can_view_path-bool"></a>

Determines if the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore can not see content the user is not collaborated on.  Be aware that this meaningfully increases the time required to load the invitee's **All Files** page. We recommend you limit the number of collaborations with `can_view_path` enabled to 1,000 per user.  Only owner or co-owners can invite collaborators with a `can_view_path` of `true`.  `can_view_path` can only be used for folder collaborations.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CollaborationsUpdateCollaborationRequest`](./box_python_sdk/type/collaborations_update_collaboration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Collaboration`](./box_python_sdk/pydantic/collaboration.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaborations/{collaboration_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations_(list).collaborations`<a id="boxcollaborations_listcollaborations"></a>

Retrieves all pending collaboration invites for this user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
collaborations_response = box.collaborations_(list).collaborations(
    status="pending",
    fields=["id", "type", "name"],
    offset=1000,
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

The status of the collaborations to retrieve

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`Collaborations`](./box_python_sdk/pydantic/collaborations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaborations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations_(list).file_access_list`<a id="boxcollaborations_listfile_access_list"></a>

Retrieves a list of pending and active collaborations for a
file. This returns all the users that have access to the file
or have been invited to the file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_access_list_response = box.collaborations_(list).file_access_list(
    file_id="12345",
    fields=["id", "type", "name"],
    limit=1000,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`Collaborations`](./box_python_sdk/pydantic/collaborations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/collaborations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations_(list).folder_access`<a id="boxcollaborations_listfolder_access"></a>

Retrieves a list of pending and active collaborations for a
folder. This returns all the users that have access to the folder
or have been invited to the folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
folder_access_response = box.collaborations_(list).folder_access(
    folder_id="12345",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`Collaborations`](./box_python_sdk/pydantic/collaborations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/collaborations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collaborations_(list).group_access_details`<a id="boxcollaborations_listgroup_access_details"></a>

Retrieves all the collaborations for a group. The user
must have admin permissions to inspect enterprise's groups.

Each collaboration object has details on which files or
folders the group has access to and with what role.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
group_access_details_response = box.collaborations_(list).group_access_details(
    group_id="57645",
    limit=1000,
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

The ID of the group.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`Collaborations`](./box_python_sdk/pydantic/collaborations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{group_id}/collaborations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collections.collections`<a id="boxcollectionscollections"></a>

Retrieves all collections for a given user.

Currently, only the `favorites` collection
is supported.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
collections_response = box.collections.collections(
    fields=["id", "type", "name"],
    offset=1000,
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`Collections`](./box_python_sdk/pydantic/collections.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.collections.list_items`<a id="boxcollectionslist_items"></a>

Retrieves the files and/or folders contained within
this collection.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_items_response = box.collections.list_items(
    collection_id="926489",
    fields=["id", "type", "name"],
    offset=1000,
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

The ID of the collection.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`Items`](./box_python_sdk/pydantic/items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collections/{collection_id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.comments.comments`<a id="boxcommentscomments"></a>

Adds a comment by the user to a specific file, or
as a reply to an other comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
comments_response = box.comments.comments(
    message="Review completed!",
    item={
        "id": "11446498",
        "type": "file",
    },
    tagged_message="@[1234:John] Review completed!",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message: `str`<a id="message-str"></a>

The text of the comment.  To mention a user, use the `tagged_message` parameter instead.

##### item: [`PostCommentsRequestItem`](./box_python_sdk/type/post_comments_request_item.py)<a id="item-postcommentsrequestitembox_python_sdktypepost_comments_request_itempy"></a>


##### tagged_message: `str`<a id="tagged_message-str"></a>

The text of the comment, including `@[user_id:name]` somewhere in the message to mention another user, which will send them an email notification, letting them know they have been mentioned.  The `user_id` is the target user's ID, where the `name` can be any custom phrase. In the Box UI this name will link to the user's profile.  If you are not mentioning another user, use `message` instead.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostCommentsRequest`](./box_python_sdk/type/post_comments_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CommentFull`](./box_python_sdk/pydantic/comment_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.comments.get_by_id`<a id="boxcommentsget_by_id"></a>

Retrieves the message and metadata for a specific comment, as well
as information on the user who created the comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.comments.get_by_id(
    comment_id="12345",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

The ID of the comment.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`CommentFull`](./box_python_sdk/pydantic/comment_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{comment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.comments.list_file_comments`<a id="boxcommentslist_file_comments"></a>

Retrieves a list of comments for a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_file_comments_response = box.comments.list_file_comments(
    file_id="12345",
    fields=["id", "type", "name"],
    limit=1000,
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`Comments`](./box_python_sdk/pydantic/comments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.comments.remove_by_id`<a id="boxcommentsremove_by_id"></a>

Permanently deletes a comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.comments.remove_by_id(
    comment_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

The ID of the comment.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{comment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.comments.update_message`<a id="boxcommentsupdate_message"></a>

Update the message of a comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_message_response = box.comments.update_message(
    comment_id="12345",
    message="Review completed!",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### comment_id: `str`<a id="comment_id-str"></a>

The ID of the comment.

##### message: `str`<a id="message-str"></a>

The text of the comment to update

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CommentsUpdateMessageRequest`](./box_python_sdk/type/comments_update_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CommentFull`](./box_python_sdk/pydantic/comment_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/comments/{comment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.device_pinners.get_pinner_info`<a id="boxdevice_pinnersget_pinner_info"></a>

Retrieves information about an individual device pin.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pinner_info_response = box.device_pinners.get_pinner_info(
    device_pinner_id="2324234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_pinner_id: `str`<a id="device_pinner_id-str"></a>

The ID of the device pin

#### 🔄 Return<a id="🔄-return"></a>

[`DevicePinner`](./box_python_sdk/pydantic/device_pinner.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/device_pinners/{device_pinner_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.device_pinners.list_pinner_info`<a id="boxdevice_pinnerslist_pinner_info"></a>

Retrieves all the device pins within an enterprise.

The user must have admin privileges, and the application
needs the "manage enterprise" scope to make this call.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_pinner_info_response = box.device_pinners.list_pinner_info(
    enterprise_id="3442311",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
    direction="ASC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enterprise_id: `str`<a id="enterprise_id-str"></a>

The ID of the enterprise

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### direction: `str`<a id="direction-str"></a>

The direction to sort results in. This can be either in alphabetical ascending (`ASC`) or descending (`DESC`) order.

#### 🔄 Return<a id="🔄-return"></a>

[`DevicePinners`](./box_python_sdk/pydantic/device_pinners.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/enterprises/{enterprise_id}/device_pinners` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.device_pinners.remove_device_pin`<a id="boxdevice_pinnersremove_device_pin"></a>

Deletes an individual device pin.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.device_pinners.remove_device_pin(
    device_pinner_id="2324234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_pinner_id: `str`<a id="device_pinner_id-str"></a>

The ID of the device pin

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/device_pinners/{device_pinner_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_(user_exemptions).create_user_exemption_from_collaboration_domain_restrictions`<a id="boxdomain_restrictions_user_exemptionscreate_user_exemption_from_collaboration_domain_restrictions"></a>

Exempts a user from the restrictions set out by the allowed list of domains
for collaborations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_exemption_from_collaboration_domain_restrictions_response = box.domain_restrictions_(user_exemptions).create_user_exemption_from_collaboration_domain_restrictions(
    user={
        "id": "23522323",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user: [`DomainRestrictionsUserExemptionsCreateUserExemptionFromCollaborationDomainRestrictionsRequestUser`](./box_python_sdk/type/domain_restrictions_user_exemptions_create_user_exemption_from_collaboration_domain_restrictions_request_user.py)<a id="user-domainrestrictionsuserexemptionscreateuserexemptionfromcollaborationdomainrestrictionsrequestuserbox_python_sdktypedomain_restrictions_user_exemptions_create_user_exemption_from_collaboration_domain_restrictions_request_userpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainRestrictionsUserExemptionsCreateUserExemptionFromCollaborationDomainRestrictionsRequest`](./box_python_sdk/type/domain_restrictions_user_exemptions_create_user_exemption_from_collaboration_domain_restrictions_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CollaborationAllowlistExemptTarget`](./box_python_sdk/pydantic/collaboration_allowlist_exempt_target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_exempt_targets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_(user_exemptions).get_user_exemption`<a id="boxdomain_restrictions_user_exemptionsget_user_exemption"></a>

Returns a users who has been exempt from the collaboration
domain restrictions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_exemption_response = box.domain_restrictions_(user_exemptions).get_user_exemption(
    collaboration_whitelist_exempt_target_id="984923",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collaboration_whitelist_exempt_target_id: `str`<a id="collaboration_whitelist_exempt_target_id-str"></a>

The ID of the exemption to the list.

#### 🔄 Return<a id="🔄-return"></a>

[`CollaborationAllowlistExemptTarget`](./box_python_sdk/pydantic/collaboration_allowlist_exempt_target.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_(user_exemptions).list_exempt_users`<a id="boxdomain_restrictions_user_exemptionslist_exempt_users"></a>

Returns a list of users who have been exempt from the collaboration
domain restrictions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_exempt_users_response = box.domain_restrictions_(user_exemptions).list_exempt_users(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`CollaborationAllowlistExemptTargets`](./box_python_sdk/pydantic/collaboration_allowlist_exempt_targets.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_exempt_targets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_(user_exemptions).remove_exemption`<a id="boxdomain_restrictions_user_exemptionsremove_exemption"></a>

Removes a user's exemption from the restrictions set out by the allowed list
of domains for collaborations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.domain_restrictions_(user_exemptions).remove_exemption(
    collaboration_whitelist_exempt_target_id="984923",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collaboration_whitelist_exempt_target_id: `str`<a id="collaboration_whitelist_exempt_target_id-str"></a>

The ID of the exemption to the list.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_for_collaborations.add_allowed_domain_entry`<a id="boxdomain_restrictions_for_collaborationsadd_allowed_domain_entry"></a>

Creates a new entry in the list of allowed domains to allow
collaboration for.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_allowed_domain_entry_response = box.domain_restrictions_for_collaborations.add_allowed_domain_entry(
    domain="example.com",
    direction="inbound",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

The domain to add to the list of allowed domains.

##### direction: `str`<a id="direction-str"></a>

The direction in which to allow collaborations.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DomainRestrictionsForCollaborationsAddAllowedDomainEntryRequest`](./box_python_sdk/type/domain_restrictions_for_collaborations_add_allowed_domain_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CollaborationAllowlistEntry`](./box_python_sdk/pydantic/collaboration_allowlist_entry.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_entries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_for_collaborations.allowed_collaboration_domain`<a id="boxdomain_restrictions_for_collaborationsallowed_collaboration_domain"></a>

Returns a domain that has been deemed safe to create collaborations
for within the current enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
allowed_collaboration_domain_response = box.domain_restrictions_for_collaborations.allowed_collaboration_domain(
    collaboration_whitelist_entry_id="213123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collaboration_whitelist_entry_id: `str`<a id="collaboration_whitelist_entry_id-str"></a>

The ID of the entry in the list.

#### 🔄 Return<a id="🔄-return"></a>

[`CollaborationAllowlistEntry`](./box_python_sdk/pydantic/collaboration_allowlist_entry.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_for_collaborations.list_allowed_collaboration_domains`<a id="boxdomain_restrictions_for_collaborationslist_allowed_collaboration_domains"></a>

Returns the list domains that have been deemed safe to create collaborations
for within the current enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_allowed_collaboration_domains_response = box.domain_restrictions_for_collaborations.list_allowed_collaboration_domains(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`CollaborationAllowlistEntries`](./box_python_sdk/pydantic/collaboration_allowlist_entries.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_entries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.domain_restrictions_for_collaborations.remove_allowed_domain_entry`<a id="boxdomain_restrictions_for_collaborationsremove_allowed_domain_entry"></a>

Removes a domain from the list of domains that have been deemed safe to create
collaborations for within the current enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.domain_restrictions_for_collaborations.remove_allowed_domain_entry(
    collaboration_whitelist_entry_id="213123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### collaboration_whitelist_entry_id: `str`<a id="collaboration_whitelist_entry_id-str"></a>

The ID of the entry in the list.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.downloads.file_content_get`<a id="boxdownloadsfile_content_get"></a>

Returns the contents of a file in binary format.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_content_get_response = box.downloads.file_content_get(
    file_id="12345",
    range="bytes=0-1024",
    boxapi="shared_link=[link]&shared_link_password=[password]",
    version="4",
    access_token="c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### range: `str`<a id="range-str"></a>

The byte range of the content to download.  The format `bytes={start_byte}-{end_byte}` can be used to specify what section of the file to download.

##### boxapi: `str`<a id="boxapi-str"></a>

The URL, and optional password, for the shared link of this item.  This header can be used to access items that have not been explicitly shared with a user.  Use the format `shared_link=[link]` or if a password is required then use `shared_link=[link]&shared_link_password=[password]`.  This header can be used on the file or folder shared, as well as on any files or folders nested within the item.

##### version: `str`<a id="version-str"></a>

The file version to download

##### access_token: `str`<a id="access_token-str"></a>

An optional access token that can be used to pre-authenticate this request, which means that a download link can be shared with a browser or a third party service without them needing to know how to handle the authentication. When using this parameter, please make sure that the access token is sufficiently scoped down to only allow read access to that file and no other files or folders.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.email_aliases.create_new_alias`<a id="boxemail_aliasescreate_new_alias"></a>

Adds a new email alias to a user account..

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_alias_response = box.email_aliases.create_new_alias(
    email="alias@example.com",
    user_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

The email address to add to the account as an alias.  Note: The domain of the email alias needs to be registered  to your enterprise. See the [domain verification guide](https://support.box.com/hc/en-us/articles/4408619650579-Domain-Verification) for steps to add a new domain.

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailAliasesCreateNewAliasRequest`](./box_python_sdk/type/email_aliases_create_new_alias_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailAlias`](./box_python_sdk/pydantic/email_alias.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/email_aliases` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.email_aliases.list_user_email_aliases`<a id="boxemail_aliaseslist_user_email_aliases"></a>

Retrieves all email aliases for a user. The collection
does not include the primary login for the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_email_aliases_response = box.email_aliases.list_user_email_aliases(
    user_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

#### 🔄 Return<a id="🔄-return"></a>

[`EmailAliases`](./box_python_sdk/pydantic/email_aliases.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/email_aliases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.email_aliases.remove_alias`<a id="boxemail_aliasesremove_alias"></a>

Removes an email alias from a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.email_aliases.remove_alias(
    user_id="12345",
    email_alias_id="23432",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### email_alias_id: `str`<a id="email_alias_id-str"></a>

The ID of the email alias.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/email_aliases/{email_alias_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.events.events`<a id="boxeventsevents"></a>

Returns up to a year of past events for a given user
or for the entire enterprise.

By default this returns events for the authenticated user. To retrieve events
for the entire enterprise, set the `stream_type` to `admin_logs_streaming`
for live monitoring of new events, or `admin_logs` for querying across
historical events. The user making the API call will
need to have admin privileges, and the application will need to have the
scope `manage enterprise properties` checked.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
events_response = box.events.events(
    stream_type="all",
    stream_position="1348790499819",
    limit=50,
    event_type=["ACCESS_GRANTED"],
    created_after="2012-12-12T10:53:43-08:00",
    created_before="2013-12-12T10:53:43-08:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### stream_type: `str`<a id="stream_type-str"></a>

Defines the type of events that are returned  * `all` returns everything for a user and is the default * `changes` returns events that may cause file tree changes   such as file updates or collaborations. * `sync` is similar to `changes` but only applies to synced folders * `admin_logs` returns all events for an entire enterprise and   requires the user making the API call to have admin permissions. This   stream type is for programmatically pulling from a 1 year history of   events across all users within the enterprise and within a   `created_after` and `created_before` time frame. The complete history   of events will be returned in chronological order based on the event   time, but latency will be much higher than `admin_logs_streaming`. * `admin_logs_streaming` returns all events for an entire enterprise and   requires the user making the API call to have admin permissions. This   stream type is for polling for recent events across all users within   the enterprise. Latency will be much lower than `admin_logs`, but   events will not be returned in chronological order and may   contain duplicates.

##### stream_position: `str`<a id="stream_position-str"></a>

The location in the event stream to start receiving events from.  * `now` will return an empty list events and the latest stream position for initialization. * `0` or `null` will return all events.

##### limit: `int`<a id="limit-int"></a>

Limits the number of events returned  Note: Sometimes, the events less than the limit requested can be returned even when there may be more events remaining. This is primarily done in the case where a number of events have already been retrieved and these retrieved events are returned rather than delaying for an unknown amount of time to see if there are any more results.

##### event_type: List[`str`]<a id="event_type-liststr"></a>

A comma-separated list of events to filter by. This can only be used when requesting the events with a `stream_type` of `admin_logs` or `adming_logs_streaming`. For any other `stream_type` this value will be ignored.

##### created_after: `datetime`<a id="created_after-datetime"></a>

The lower bound date and time to return events for. This can only be used when requesting the events with a `stream_type` of `admin_logs`. For any other `stream_type` this value will be ignored.

##### created_before: `datetime`<a id="created_before-datetime"></a>

The upper bound date and time to return events for. This can only be used when requesting the events with a `stream_type` of `admin_logs`. For any other `stream_type` this value will be ignored.

#### 🔄 Return<a id="🔄-return"></a>

[`Events`](./box_python_sdk/pydantic/events.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.events.events_0`<a id="boxeventsevents_0"></a>

Returns a list of real-time servers that can be used for long-polling updates
to the [event stream](https://raw.githubusercontent.com).

Long polling is the concept where a HTTP request is kept open until the
server sends a response, then repeating the process over and over to receive
updated responses.

Long polling the event stream can only be used for user events, not for
enterprise events.

To use long polling, first use this endpoint to retrieve a list of long poll
URLs. Next, make a long poll request to any of the provided URLs.

When an event occurs in monitored account a response with the value
`new_change` will be sent. The response contains no other details as
it only serves as a prompt to take further action such as sending a
request to the [events endpoint](https://raw.githubusercontent.com) with the last known
`stream_position`.

After the server sends this response it closes the connection. You must now
repeat the long poll process to begin listening for events again.

If no events occur for a while and the connection times out you will
receive a response with the value `reconnect`. When you receive this response
you’ll make another call to this endpoint to restart the process.

If you receive no events in `retry_timeout` seconds then you will need to
make another request to the real-time server (one of the URLs in the response
for this endpoint). This might be necessary due to network errors.

Finally, if you receive a `max_retries` error when making a request to the
real-time server, you should start over by making a call to this endpoint
first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
events_0_response = box.events.events_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RealtimeServers`](./box_python_sdk/pydantic/realtime_servers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events` `options`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_requests.copy_request_to_folder`<a id="boxfile_requestscopy_request_to_folder"></a>

Copies an existing file request that is already present on one folder,
and applies it to another folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
copy_request_to_folder_response = box.file_requests.copy_request_to_folder(
    folder={
        "type": "folder",
        "id": "42037322",
    },
    file_request_id="123",
    title="Please upload required documents",
    description="Please upload required documents",
    status="active",
    is_email_required=True,
    is_description_required=True,
    expires_at="2020-09-28T10:53:43-08:00",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder: [`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`](./box_python_sdk/type/typing_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="folder-dictstr-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_dict_str_typing_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


The folder to associate the new file request to.

##### file_request_id: `str`<a id="file_request_id-str"></a>

The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/filerequest/123` the `file_request_id` is `123`.

##### title: `str`<a id="title-str"></a>

An optional new title for the file request. This can be used to change the title of the file request.  This will default to the value on the existing file request.

##### description: `str`<a id="description-str"></a>

An optional new description for the file request. This can be used to change the description of the file request.  This will default to the value on the existing file request.

##### status: `str`<a id="status-str"></a>

An optional new status of the file request.  When the status is set to `inactive`, the file request will no longer accept new submissions, and any visitor to the file request URL will receive a `HTTP 404` status code.  This will default to the value on the existing file request.

##### is_email_required: `bool`<a id="is_email_required-bool"></a>

Whether a file request submitter is required to provide their email address.  When this setting is set to true, the Box UI will show an email field on the file request form.  This will default to the value on the existing file request.

##### is_description_required: `bool`<a id="is_description_required-bool"></a>

Whether a file request submitter is required to provide a description of the files they are submitting.  When this setting is set to true, the Box UI will show a description field on the file request form.  This will default to the value on the existing file request.

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

The date after which a file request will no longer accept new submissions.  After this date, the `status` will automatically be set to `inactive`.  This will default to the value on the existing file request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileRequestCopyRequest`](./box_python_sdk/type/file_request_copy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileRequest`](./box_python_sdk/pydantic/file_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_requests/{file_request_id}/copy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_requests.delete_permanently`<a id="boxfile_requestsdelete_permanently"></a>

Deletes a file request permanently.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.file_requests.delete_permanently(
    file_request_id="123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_request_id: `str`<a id="file_request_id-str"></a>

The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/filerequest/123` the `file_request_id` is `123`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_requests/{file_request_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_requests.get_information`<a id="boxfile_requestsget_information"></a>

Retrieves the information about a file request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = box.file_requests.get_information(
    file_request_id="123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_request_id: `str`<a id="file_request_id-str"></a>

The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/filerequest/123` the `file_request_id` is `123`.

#### 🔄 Return<a id="🔄-return"></a>

[`FileRequest`](./box_python_sdk/pydantic/file_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_requests/{file_request_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_requests.update_request`<a id="boxfile_requestsupdate_request"></a>

Updates a file request. This can be used to activate or
deactivate a file request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_request_response = box.file_requests.update_request(
    file_request_id="123",
    title="Please upload required documents",
    description="Please upload required documents",
    status="active",
    is_email_required=True,
    is_description_required=True,
    expires_at="2020-09-28T10:53:43-08:00",
    if_match="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_request_id: `str`<a id="file_request_id-str"></a>

The unique identifier that represent a file request.  The ID for any file request can be determined by visiting a file request builder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/filerequest/123` the `file_request_id` is `123`.

##### title: `str`<a id="title-str"></a>

An optional new title for the file request. This can be used to change the title of the file request.  This will default to the value on the existing file request.

##### description: `str`<a id="description-str"></a>

An optional new description for the file request. This can be used to change the description of the file request.  This will default to the value on the existing file request.

##### status: `str`<a id="status-str"></a>

An optional new status of the file request.  When the status is set to `inactive`, the file request will no longer accept new submissions, and any visitor to the file request URL will receive a `HTTP 404` status code.  This will default to the value on the existing file request.

##### is_email_required: `bool`<a id="is_email_required-bool"></a>

Whether a file request submitter is required to provide their email address.  When this setting is set to true, the Box UI will show an email field on the file request form.  This will default to the value on the existing file request.

##### is_description_required: `bool`<a id="is_description_required-bool"></a>

Whether a file request submitter is required to provide a description of the files they are submitting.  When this setting is set to true, the Box UI will show a description field on the file request form.  This will default to the value on the existing file request.

##### expires_at: `datetime`<a id="expires_at-datetime"></a>

The date after which a file request will no longer accept new submissions.  After this date, the `status` will automatically be set to `inactive`.  This will default to the value on the existing file request.

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileRequestUpdateRequest`](./box_python_sdk/type/file_request_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileRequest`](./box_python_sdk/pydantic/file_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_requests/{file_request_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_version_legal_holds.get_file_version_legal_hold_info`<a id="boxfile_version_legal_holdsget_file_version_legal_hold_info"></a>

Retrieves information about the legal hold policies
assigned to a file version.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_version_legal_hold_info_response = box.file_version_legal_holds.get_file_version_legal_hold_info(
    file_version_legal_hold_id="2348213",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_version_legal_hold_id: `str`<a id="file_version_legal_hold_id-str"></a>

The ID of the file version legal hold

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionLegalHold`](./box_python_sdk/pydantic/file_version_legal_hold.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_version_legal_holds/{file_version_legal_hold_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_version_legal_holds.list_file_version_legal_holds`<a id="boxfile_version_legal_holdslist_file_version_legal_holds"></a>

Get a list of file versions on legal hold for a legal hold
assignment.

Due to ongoing re-architecture efforts this API might not return all file
versions for this policy ID.

Instead, this API will only return file versions held in the legacy
architecture. Two new endpoints will available to request any file versions
held in the new architecture.

For file versions held in the new architecture, the `GET
/legal_hold_policy_assignments/:id/file_versions_on_hold` API can be used to
return all past file versions available for this policy assignment, and the
`GET /legal_hold_policy_assignments/:id/files_on_hold` API can be used to
return any current (latest) versions of a file under legal hold.

The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to
find a list of policy assignments for a given policy ID.

Once the re-architecture is completed this API will be deprecated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_file_version_legal_holds_response = box.file_version_legal_holds.list_file_version_legal_holds(
    policy_id="133870",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

The ID of the legal hold policy to get the file version legal holds for.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionLegalHolds`](./box_python_sdk/pydantic/file_version_legal_holds.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_version_legal_holds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_version_retentions.get_file_version_retention_info`<a id="boxfile_version_retentionsget_file_version_retention_info"></a>

Returns information about a file version retention.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_version_retention_info_response = box.file_version_retentions.get_file_version_retention_info(
    file_version_retention_id="3424234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_version_retention_id: `str`<a id="file_version_retention_id-str"></a>

The ID of the file version retention

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionRetention`](./box_python_sdk/pydantic/file_version_retention.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_version_retentions/{file_version_retention_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_version_retentions.list_retentions`<a id="boxfile_version_retentionslist_retentions"></a>

Retrieves all file version retentions for the given enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_retentions_response = box.file_version_retentions.list_retentions(
    file_id="43123123",
    file_version_id="1",
    policy_id="982312",
    disposition_action="permanently_delete",
    disposition_before="2012-12-12T10:53:43-08:00",
    disposition_after="2012-12-19T10:34:23-08:00",
    limit=1000,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

Filters results by files with this ID.

##### file_version_id: `str`<a id="file_version_id-str"></a>

Filters results by file versions with this ID.

##### policy_id: `str`<a id="policy_id-str"></a>

Filters results by the retention policy with this ID.

##### disposition_action: `str`<a id="disposition_action-str"></a>

Filters results by the retention policy with this disposition action.

##### disposition_before: `str`<a id="disposition_before-str"></a>

Filters results by files that will have their disposition come into effect before this date.

##### disposition_after: `str`<a id="disposition_after-str"></a>

Filters results by files that will have their disposition come into effect after this date.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionRetentions`](./box_python_sdk/pydantic/file_version_retentions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/file_version_retentions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_versions.get_specific_version`<a id="boxfile_versionsget_specific_version"></a>

Retrieve a specific version of a file.

Versions are only tracked for Box users with premium accounts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_version_response = box.file_versions.get_specific_version(
    file_id="12345",
    file_version_id="1234",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### file_version_id: `str`<a id="file_version_id-str"></a>

The ID of the file version

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionFull`](./box_python_sdk/pydantic/file_version_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/versions/{file_version_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_versions.list_all_versions`<a id="boxfile_versionslist_all_versions"></a>

Retrieve a list of the past versions for a file.

Versions are only tracked by Box users with premium accounts. To fetch the ID
of the current version of a file, use the `GET /file/:id` API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_versions_response = box.file_versions.list_all_versions(
    file_id="12345",
    fields=["id", "type", "name"],
    limit=1000,
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersions`](./box_python_sdk/pydantic/file_versions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_versions.move_to_trash`<a id="boxfile_versionsmove_to_trash"></a>

Move a file version to the trash.

Versions are only tracked for Box users with premium accounts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.file_versions.move_to_trash(
    file_id="12345",
    file_version_id="1234",
    if_match="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### file_version_id: `str`<a id="file_version_id-str"></a>

The ID of the file version

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/versions/{file_version_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_versions.promote_file_version`<a id="boxfile_versionspromote_file_version"></a>

Promote a specific version of a file.

If previous versions exist, this method can be used to
promote one of the older versions to the top of the version history.

This creates a new copy of the old version and puts it at the
top of the versions history. The file will have the exact same contents
as the older version, with the the same hash digest, `etag`, and
name as the original.

Other properties such as comments do not get updated to their
former values.

Don't use this endpoint to restore Box Notes,
as it works with file formats such as PDF, DOC,
PPTX or similar.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
promote_file_version_response = box.file_versions.promote_file_version(
    file_id="12345",
    id="11446498",
    type="file_version",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### id: `str`<a id="id-str"></a>

The file version ID

##### type: `str`<a id="type-str"></a>

The type to promote

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileVersionsPromoteFileVersionRequest`](./box_python_sdk/type/file_versions_promote_file_version_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionFull`](./box_python_sdk/pydantic/file_version_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/versions/current` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.file_versions.restore_version`<a id="boxfile_versionsrestore_version"></a>

Restores a specific version of a file after it was deleted.
Don't use this endpoint to restore Box Notes,
as it works with file formats such as PDF, DOC,
PPTX or similar.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
restore_version_response = box.file_versions.restore_version(
    file_id="12345",
    file_version_id="1234",
    trashed_at="null",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### file_version_id: `str`<a id="file_version_id-str"></a>

The ID of the file version

##### trashed_at: `str`<a id="trashed_at-str"></a>

Set this to `null` to clear the date and restore the file.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileVersionsRestoreVersionRequest`](./box_python_sdk/type/file_versions_restore_version_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionFull`](./box_python_sdk/pydantic/file_version_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/versions/{file_version_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.files.create_copy`<a id="boxfilescreate_copy"></a>

Creates a copy of a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_copy_response = box.files.create_copy(
    parent={
        "id": "0",
    },
    file_id="12345",
    version="0",
    name="FileCopy.txt",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent: [`FilesCreateCopyRequestParent`](./box_python_sdk/type/files_create_copy_request_parent.py)<a id="parent-filescreatecopyrequestparentbox_python_sdktypefiles_create_copy_request_parentpy"></a>


##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### version: `str`<a id="version-str"></a>

An optional ID of the specific file version to copy.

##### name: `str`<a id="name-str"></a>

An optional new name for the copied file.  There are some restrictions to the file name. Names containing non-printable ASCII characters, forward and backward slashes (`/`, `\\\\`), and protected names like `.` and `..` are automatically sanitized by removing the non-allowed characters.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilesCreateCopyRequest`](./box_python_sdk/type/files_create_copy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/copy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.files.delete_file`<a id="boxfilesdelete_file"></a>

Deletes a file, either permanently or by moving it to
the trash.

The the enterprise settings determine whether the item will
be permanently deleted from Box or moved to the trash.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.files.delete_file(
    file_id="12345",
    if_match="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.files.get_details`<a id="boxfilesget_details"></a>

Retrieves the details about a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = box.files.get_details(
    file_id="12345",
    fields=["id", "type", "name"],
    if_none_match="1",
    boxapi="shared_link=[link]&shared_link_password=[password]",
    x_rep_hints="[pdf]",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.  Additionally this field can be used to query any metadata applied to the file by specifying the `metadata` field as well as the scope and key of the template to retrieve, for example `?field=metadata.enterprise_12345.contractTemplate`.

##### if_none_match: `str`<a id="if_none_match-str"></a>

Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.

##### boxapi: `str`<a id="boxapi-str"></a>

The URL, and optional password, for the shared link of this item.  This header can be used to access items that have not been explicitly shared with a user.  Use the format `shared_link=[link]` or if a password is required then use `shared_link=[link]&shared_link_password=[password]`.  This header can be used on the file or folder shared, as well as on any files or folders nested within the item.

##### x_rep_hints: `Optional[str]`<a id="x_rep_hints-optionalstr"></a>

A header required to request specific `representations` of a file. Use this in combination with the `fields` query parameter to request a specific file representation.  The general format for these representations is `X-Rep-Hints: [...]` where `[...]` is one or many hints in the format `[fileType?query]`.  For example, to request a `png` representation in `32x32` as well as `64x64` pixel dimensions provide the following hints.  `x-rep-hints: [jpg?dimensions=32x32][jpg?dimensions=64x64]`  Additionally, a `text` representation is available for all document file types in Box using the `[extracted_text]` representation.  `x-rep-hints: [extracted_text]`

#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.files.get_thumbnail`<a id="boxfilesget_thumbnail"></a>

Retrieves a thumbnail, or smaller image representation, of a file.

Sizes of `32x32`,`64x64`, `128x128`, and `256x256` can be returned in
the `.png` format and sizes of `32x32`, `160x160`, and `320x320`
can be returned in the `.jpg` format.

Thumbnails can be generated for the image and video file formats listed
[found on our community site][1].

[1]: https://community.box.com/t5/Migrating-and-Previewing-Content/File-Types-and-Fonts-Supported-in-Box-Content-Preview/ta-p/327

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_thumbnail_response = box.files.get_thumbnail(
    file_id="12345",
    extension="png",
    min_height=32,
    min_width=32,
    max_height=320,
    max_width=320,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### extension: `str`<a id="extension-str"></a>

The file format for the thumbnail

##### min_height: `int`<a id="min_height-int"></a>

The minimum height of the thumbnail

##### min_width: `int`<a id="min_width-int"></a>

The minimum width of the thumbnail

##### max_height: `int`<a id="max_height-int"></a>

The maximum height of the thumbnail

##### max_width: `int`<a id="max_width-int"></a>

The maximum width of the thumbnail

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/thumbnail.{extension}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.files.preflight_check_before_upload`<a id="boxfilespreflight_check_before_upload"></a>

Performs a check to verify that a file will be accepted by Box
before you upload the entire file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preflight_check_before_upload_response = box.files.preflight_check_before_upload(
    name="File.mp4",
    size=1024,
    parent=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name for the file

##### size: `int`<a id="size-int"></a>

The size of the file in bytes

##### parent: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilesPreflightCheckBeforeUploadRequest`](./box_python_sdk/type/files_preflight_check_before_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadUrl`](./box_python_sdk/pydantic/upload_url.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/content` `options`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.files.update_file`<a id="boxfilesupdate_file"></a>

Updates a file. This can be used to rename or move a file,
create a shared link, or lock a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_file_response = box.files.update_file(
    file_id="12345",
    tags=["approved"],
    description="The latest reports. Automatically updated",
    name="NewFile.txt",
    parent=None,
    shared_link=None,
    lock={
        "access": "lock",
        "expires_at": "2012-12-12T10:53:43-08:00",
        "is_download_prevented": True,
    },
    disposition_at="2012-12-12T10:53:43-08:00",
    permissions={
        "can_download": "open",
    },
    collections=[
        {
            "id": "11446498",
            "type": "file",
        }
    ],
    fields=["id", "type", "name"],
    if_match="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### tags: [`FilesUpdateFileRequestTags`](./box_python_sdk/type/files_update_file_request_tags.py)<a id="tags-filesupdatefilerequesttagsbox_python_sdktypefiles_update_file_request_tagspy"></a>

##### description: `str`<a id="description-str"></a>

The description for a file. This can be seen in the right-hand sidebar panel when viewing a file in the Box web app. Additionally, this index is used in the search index of the file, allowing users to find the file by the content in the description.

##### name: `str`<a id="name-str"></a>

An optional different name for the file. This can be used to rename the file.

##### parent: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### shared_link: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="shared_link-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### lock: [`FilesUpdateFileRequestLock`](./box_python_sdk/type/files_update_file_request_lock.py)<a id="lock-filesupdatefilerequestlockbox_python_sdktypefiles_update_file_request_lockpy"></a>


##### disposition_at: `datetime`<a id="disposition_at-datetime"></a>

The retention expiration timestamp for the given file. This date cannot be shortened once set on a file.

##### permissions: [`FilesUpdateFileRequestPermissions`](./box_python_sdk/type/files_update_file_request_permissions.py)<a id="permissions-filesupdatefilerequestpermissionsbox_python_sdktypefiles_update_file_request_permissionspy"></a>


##### collections: [`FilesUpdateFileRequestCollections`](./box_python_sdk/type/files_update_file_request_collections.py)<a id="collections-filesupdatefilerequestcollectionsbox_python_sdktypefiles_update_file_request_collectionspy"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilesUpdateFileRequest`](./box_python_sdk/type/files_update_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folder_locks.create`<a id="boxfolder_lockscreate"></a>

Creates a folder lock on a folder, preventing it from being moved and/or
deleted.

You must be authenticated as the owner or co-owner of the folder to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = box.folder_locks.create(
    folder={
        "type": "folder",
        "id": "1234567890",
    },
    locked_operations={
        "move": True,
        "delete": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder: [`FolderLocksCreateRequestFolder`](./box_python_sdk/type/folder_locks_create_request_folder.py)<a id="folder-folderlockscreaterequestfolderbox_python_sdktypefolder_locks_create_request_folderpy"></a>


##### locked_operations: [`FolderLocksCreateRequestLockedOperations`](./box_python_sdk/type/folder_locks_create_request_locked_operations.py)<a id="locked_operations-folderlockscreaterequestlockedoperationsbox_python_sdktypefolder_locks_create_request_locked_operationspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FolderLocksCreateRequest`](./box_python_sdk/type/folder_locks_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderLock`](./box_python_sdk/pydantic/folder_lock.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folder_locks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folder_locks.delete_folder_lock`<a id="boxfolder_locksdelete_folder_lock"></a>

Deletes a folder lock on a given folder.

You must be authenticated as the owner or co-owner of the folder to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.folder_locks.delete_folder_lock(
    folder_lock_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_lock_id: `str`<a id="folder_lock_id-str"></a>

The ID of the folder lock.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folder_locks/{folder_lock_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folder_locks.list_details`<a id="boxfolder_lockslist_details"></a>

Retrieves folder lock details for a given folder.

You must be authenticated as the owner or co-owner of the folder to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_details_response = box.folder_locks.list_details(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🔄 Return<a id="🔄-return"></a>

[`FolderLocks`](./box_python_sdk/pydantic/folder_locks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folder_locks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folders.create_copy`<a id="boxfolderscreate_copy"></a>

Creates a copy of a folder within a destination folder.

The original folder will not be changed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_copy_response = box.folders.create_copy(
    parent={
        "id": "0",
    },
    folder_id="0",
    name="New Folder",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent: [`FoldersCreateCopyRequestParent`](./box_python_sdk/type/folders_create_copy_request_parent.py)<a id="parent-folderscreatecopyrequestparentbox_python_sdktypefolders_create_copy_request_parentpy"></a>


##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier of the folder to copy.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder with the ID `0` can not be copied.

##### name: `str`<a id="name-str"></a>

An optional new name for the copied folder.  There are some restrictions to the file name. Names containing non-printable ASCII characters, forward and backward slashes (`/`, `\\\\`), as well as names with trailing spaces are prohibited.  Additionally, the names `.` and `..` are not allowed either.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FoldersCreateCopyRequest`](./box_python_sdk/type/folders_create_copy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/copy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folders.delete_by_id`<a id="boxfoldersdelete_by_id"></a>

Deletes a folder, either permanently or by moving it to
the trash.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.folders.delete_by_id(
    folder_id="12345",
    if_match="1",
    recursive=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

##### recursive: `bool`<a id="recursive-bool"></a>

Delete a folder that is not empty by recursively deleting the folder and all of its content.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folders.folders`<a id="boxfoldersfolders"></a>

Creates a new empty folder within the specified parent folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
folders_response = box.folders.folders(
    name="New Folder",
    parent={
        "id": "0",
    },
    folder_upload_email=None,
    sync_state="synced",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name for the new folder.  There are some restrictions to the file name. Names containing non-printable ASCII characters, forward and backward slashes (`/`, `\\\\`), as well as names with trailing spaces are prohibited.  Additionally, the names `.` and `..` are not allowed either.

##### parent: [`PostFoldersRequestParent`](./box_python_sdk/type/post_folders_request_parent.py)<a id="parent-postfoldersrequestparentbox_python_sdktypepost_folders_request_parentpy"></a>


##### folder_upload_email: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="folder_upload_email-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### sync_state: `str`<a id="sync_state-str"></a>

Specifies whether a folder should be synced to a user's device or not. This is used by Box Sync (discontinued) and is not used by Box Drive.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostFoldersRequest`](./box_python_sdk/type/post_folders_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folders.get_folder_details`<a id="boxfoldersget_folder_details"></a>

Retrieves details for a folder, including the first 100 entries
in the folder.

Passing `sort`, `direction`, `offset`, and `limit`
parameters in query allows you to manage the
list of returned
[folder items](r://folder--full#param-item-collection).

To fetch more items within the folder, use the
[Get items in a folder](e://get-folders-id-items) endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_folder_details_response = box.folders.get_folder_details(
    folder_id="12345",
    fields=["id", "type", "name"],
    if_none_match="1",
    boxapi="shared_link=[link]&shared_link_password=[password]",
    sort="id",
    direction="ASC",
    offset=1000,
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.  Additionally this field can be used to query any metadata applied to the file by specifying the `metadata` field as well as the scope and key of the template to retrieve, for example `?field=metadata.enterprise_12345.contractTemplate`.

##### if_none_match: `str`<a id="if_none_match-str"></a>

Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.

##### boxapi: `str`<a id="boxapi-str"></a>

The URL, and optional password, for the shared link of this item.  This header can be used to access items that have not been explicitly shared with a user.  Use the format `shared_link=[link]` or if a password is required then use `shared_link=[link]&shared_link_password=[password]`.  This header can be used on the file or folder shared, as well as on any files or folders nested within the item.

##### sort: `str`<a id="sort-str"></a>

Defines the **second** attribute by which items are sorted.  The folder type affects the way the items are sorted:    * **Standard folder**:   Items are always sorted by   their `type` first, with   folders listed before files,   and files listed   before web links.    * **Root folder**:   This parameter is not supported   for marker-based pagination   on the root folder    (the folder with an `id` of `0`).    * **Shared folder with parent path   to the associated folder visible to   the collaborator**:   Items are always sorted by   their `type` first, with   folders listed before files,   and files listed   before web links.

##### direction: `str`<a id="direction-str"></a>

The direction to sort results in. This can be either in alphabetical ascending (`ASC`) or descending (`DESC`) order.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folders.list_items_in_folder`<a id="boxfolderslist_items_in_folder"></a>

Retrieves a page of items in a folder. These items can be files,
folders, and web links.

To request more information about the folder itself, like its size,
use the [Get a folder](https://raw.githubusercontent.com) endpoint instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_items_in_folder_response = box.folders.list_items_in_folder(
    folder_id="12345",
    fields=["id", "type", "name"],
    usemarker=True,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    offset=1000,
    limit=1000,
    boxapi="shared_link=[link]&shared_link_password=[password]",
    sort="id",
    direction="ASC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.  Additionally this field can be used to query any metadata applied to the file by specifying the `metadata` field as well as the scope and key of the template to retrieve, for example `?field=metadata.enterprise_12345.contractTemplate`.

##### usemarker: `bool`<a id="usemarker-bool"></a>

Specifies whether to use marker-based pagination instead of offset-based pagination. Only one pagination method can be used at a time.  By setting this value to true, the API will return a `marker` field that can be passed as a parameter to this endpoint to get the next page of the response.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### boxapi: `str`<a id="boxapi-str"></a>

The URL, and optional password, for the shared link of this item.  This header can be used to access items that have not been explicitly shared with a user.  Use the format `shared_link=[link]` or if a password is required then use `shared_link=[link]&shared_link_password=[password]`.  This header can be used on the file or folder shared, as well as on any files or folders nested within the item.

##### sort: `str`<a id="sort-str"></a>

Defines the **second** attribute by which items are sorted.  The folder type affects the way the items are sorted:    * **Standard folder**:   Items are always sorted by   their `type` first, with   folders listed before files,   and files listed   before web links.    * **Root folder**:   This parameter is not supported   for marker-based pagination   on the root folder    (the folder with an `id` of `0`).    * **Shared folder with parent path   to the associated folder visible to   the collaborator**:   Items are always sorted by   their `type` first, with   folders listed before files,   and files listed   before web links.

##### direction: `str`<a id="direction-str"></a>

The direction to sort results in. This can be either in alphabetical ascending (`ASC`) or descending (`DESC`) order.

#### 🔄 Return<a id="🔄-return"></a>

[`Items`](./box_python_sdk/pydantic/items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.folders.update_folder`<a id="boxfoldersupdate_folder"></a>

Updates a folder. This can be also be used to move the folder,
create shared links, update collaborations, and more.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_folder_response = box.folders.update_folder(
    folder_id="12345",
    tags=["approved"],
    description="Legal contracts for the new ACME deal",
    name="New Folder",
    sync_state="synced",
    can_non_owners_invite=True,
    parent={
        "id": "0",
    },
    shared_link=None,
    folder_upload_email=None,
    is_collaboration_restricted_to_enterprise=True,
    collections=[
        {
            "id": "11446498",
            "type": "file",
        }
    ],
    can_non_owners_view_collaborators=True,
    fields=["id", "type", "name"],
    if_match="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### tags: [`FoldersUpdateFolderRequestTags`](./box_python_sdk/type/folders_update_folder_request_tags.py)<a id="tags-foldersupdatefolderrequesttagsbox_python_sdktypefolders_update_folder_request_tagspy"></a>

##### description: `str`<a id="description-str"></a>

The optional description of this folder

##### name: `str`<a id="name-str"></a>

The optional new name for this folder.

##### sync_state: `str`<a id="sync_state-str"></a>

Specifies whether a folder should be synced to a user's device or not. This is used by Box Sync (discontinued) and is not used by Box Drive.

##### can_non_owners_invite: `bool`<a id="can_non_owners_invite-bool"></a>

Specifies if users who are not the owner of the folder can invite new collaborators to the folder.

##### parent: [`FoldersUpdateFolderRequestParent`](./box_python_sdk/type/folders_update_folder_request_parent.py)<a id="parent-foldersupdatefolderrequestparentbox_python_sdktypefolders_update_folder_request_parentpy"></a>


##### shared_link: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="shared_link-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### folder_upload_email: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="folder_upload_email-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### is_collaboration_restricted_to_enterprise: `bool`<a id="is_collaboration_restricted_to_enterprise-bool"></a>

Specifies if new invites to this folder are restricted to users within the enterprise. This does not affect existing collaborations.

##### collections: [`FoldersUpdateFolderRequestCollections`](./box_python_sdk/type/folders_update_folder_request_collections.py)<a id="collections-foldersupdatefolderrequestcollectionsbox_python_sdktypefolders_update_folder_request_collectionspy"></a>

##### can_non_owners_view_collaborators: `bool`<a id="can_non_owners_view_collaborators-bool"></a>

Restricts collaborators who are not the owner of this folder from viewing other collaborations on this folder.  It also restricts non-owners from inviting new collaborators.  When setting this field to `false`, it is required to also set `can_non_owners_invite_collaborators` to `false` if it has not already been set.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FoldersUpdateFolderRequest`](./box_python_sdk/type/folders_update_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.group_memberships.create_membership`<a id="boxgroup_membershipscreate_membership"></a>

Creates a group membership. Only users with
admin-level permissions will be able to use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_membership_response = box.group_memberships.create_membership(
    user={
        "id": "1434325",
    },
    group={
        "id": "4545523",
    },
    role="member",
    configurable_permissions={
        "key": True,
    },
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user: [`GroupMembershipsCreateMembershipRequestUser`](./box_python_sdk/type/group_memberships_create_membership_request_user.py)<a id="user-groupmembershipscreatemembershiprequestuserbox_python_sdktypegroup_memberships_create_membership_request_userpy"></a>


##### group: [`GroupMembershipsCreateMembershipRequestGroup`](./box_python_sdk/type/group_memberships_create_membership_request_group.py)<a id="group-groupmembershipscreatemembershiprequestgroupbox_python_sdktypegroup_memberships_create_membership_request_grouppy"></a>


##### role: `str`<a id="role-str"></a>

The role of the user in the group.

##### configurable_permissions: [`GroupMembershipsCreateMembershipRequestConfigurablePermissions`](./box_python_sdk/type/group_memberships_create_membership_request_configurable_permissions.py)<a id="configurable_permissions-groupmembershipscreatemembershiprequestconfigurablepermissionsbox_python_sdktypegroup_memberships_create_membership_request_configurable_permissionspy"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupMembershipsCreateMembershipRequest`](./box_python_sdk/type/group_memberships_create_membership_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupMembership`](./box_python_sdk/pydantic/group_membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_memberships` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.group_memberships.get_all`<a id="boxgroup_membershipsget_all"></a>

Retrieves all the groups for a user. Only members of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = box.group_memberships.get_all(
    user_id="12345",
    limit=1000,
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`GroupMemberships`](./box_python_sdk/pydantic/group_memberships.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.group_memberships.get_specific_membership`<a id="boxgroup_membershipsget_specific_membership"></a>

Retrieves a specific group membership. Only admins of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_membership_response = box.group_memberships.get_specific_membership(
    group_membership_id="434534",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_membership_id: `str`<a id="group_membership_id-str"></a>

The ID of the group membership.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`GroupMembership`](./box_python_sdk/pydantic/group_membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_memberships/{group_membership_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.group_memberships.list_members_of_group`<a id="boxgroup_membershipslist_members_of_group"></a>

Retrieves all the members for a group. Only members of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_members_of_group_response = box.group_memberships.list_members_of_group(
    group_id="57645",
    limit=1000,
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

The ID of the group.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`GroupMemberships`](./box_python_sdk/pydantic/group_memberships.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{group_id}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.group_memberships.remove_user_from_group`<a id="boxgroup_membershipsremove_user_from_group"></a>

Deletes a specific group membership. Only admins of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.group_memberships.remove_user_from_group(
    group_membership_id="434534",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_membership_id: `str`<a id="group_membership_id-str"></a>

The ID of the group membership.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_memberships/{group_membership_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.group_memberships.update_membership`<a id="boxgroup_membershipsupdate_membership"></a>

Updates a user's group membership. Only admins of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_membership_response = box.group_memberships.update_membership(
    group_membership_id="434534",
    role="member",
    configurable_permissions={
        "key": True,
    },
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_membership_id: `str`<a id="group_membership_id-str"></a>

The ID of the group membership.

##### role: `str`<a id="role-str"></a>

The role of the user in the group.

##### configurable_permissions: [`GroupMembershipsUpdateMembershipRequestConfigurablePermissions`](./box_python_sdk/type/group_memberships_update_membership_request_configurable_permissions.py)<a id="configurable_permissions-groupmembershipsupdatemembershiprequestconfigurablepermissionsbox_python_sdktypegroup_memberships_update_membership_request_configurable_permissionspy"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupMembershipsUpdateMembershipRequest`](./box_python_sdk/type/group_memberships_update_membership_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupMembership`](./box_python_sdk/pydantic/group_membership.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/group_memberships/{group_membership_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.groups.get_info`<a id="boxgroupsget_info"></a>

Retrieves information about a group. Only members of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = box.groups.get_info(
    group_id="57645",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

The ID of the group.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`GroupFull`](./box_python_sdk/pydantic/group_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{group_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.groups.groups`<a id="boxgroupsgroups"></a>

Retrieves all of the groups for a given enterprise. The user
must have admin permissions to inspect enterprise's groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
groups_response = box.groups.groups(
    filter_term="Engineering",
    fields=["id", "type", "name"],
    limit=1000,
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter_term: `str`<a id="filter_term-str"></a>

Limits the results to only groups whose `name` starts with the search term.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`Groups`](./box_python_sdk/pydantic/groups.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.groups.groups_0`<a id="boxgroupsgroups_0"></a>

Creates a new group of users in an enterprise. Only users with admin
permissions can create new groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
groups_0_response = box.groups.groups_0(
    name="Customer Support",
    description="\"Customer Support Group - as imported from Active Directory\"",
    provenance="Active Directory",
    external_sync_identifier="AD:123456",
    invitability_level="admins_only",
    member_viewability_level="admins_only",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the new group to be created. This name must be unique within the enterprise.

##### description: `str`<a id="description-str"></a>

A human readable description of the group.

##### provenance: `str`<a id="provenance-str"></a>

Keeps track of which external source this group is coming, for example `Active Directory`, or `Okta`.  Setting this will also prevent Box admins from editing the group name and its members directly via the Box web application.  This is desirable for one-way syncing of groups.

##### external_sync_identifier: `str`<a id="external_sync_identifier-str"></a>

An arbitrary identifier that can be used by external group sync tools to link this Box Group to an external group.  Example values of this field could be an **Active Directory Object ID** or a **Google Group ID**.  We recommend you use of this field in order to avoid issues when group names are updated in either Box or external systems.

##### invitability_level: `str`<a id="invitability_level-str"></a>

Specifies who can invite the group to collaborate on folders.  When set to `admins_only` the enterprise admin, co-admins, and the group's admin can invite the group.  When set to `admins_and_members` all the admins listed above and group members can invite the group.  When set to `all_managed_users` all managed users in the enterprise can invite the group.

##### member_viewability_level: `str`<a id="member_viewability_level-str"></a>

Specifies who can see the members of the group.  * `admins_only` - the enterprise admin, co-admins, group's   group admin * `admins_and_members` - all admins and group members * `all_managed_users` - all managed users in the   enterprise

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostGroupsRequest`](./box_python_sdk/type/post_groups_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupFull`](./box_python_sdk/pydantic/group_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.groups.remove`<a id="boxgroupsremove"></a>

Permanently deletes a group. Only users with
admin-level permissions will be able to use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.groups.remove(
    group_id="57645",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

The ID of the group.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{group_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.groups.update_group`<a id="boxgroupsupdate_group"></a>

Updates a specific group. Only admins of this
group or users with admin-level permissions will be able to
use this API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_group_response = box.groups.update_group(
    group_id="57645",
    description="\"Customer Support Group - as imported from Active Directory\"",
    name="Customer Support",
    provenance="Active Directory",
    external_sync_identifier="AD:123456",
    invitability_level="admins_only",
    member_viewability_level="admins_only",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_id: `str`<a id="group_id-str"></a>

The ID of the group.

##### description: `str`<a id="description-str"></a>

A human readable description of the group.

##### name: `str`<a id="name-str"></a>

The name of the new group to be created. Must be unique within the enterprise.

##### provenance: `str`<a id="provenance-str"></a>

Keeps track of which external source this group is coming, for example `Active Directory`, or `Okta`.  Setting this will also prevent Box admins from editing the group name and its members directly via the Box web application.  This is desirable for one-way syncing of groups.

##### external_sync_identifier: `str`<a id="external_sync_identifier-str"></a>

An arbitrary identifier that can be used by external group sync tools to link this Box Group to an external group.  Example values of this field could be an **Active Directory Object ID** or a **Google Group ID**.  We recommend you use of this field in order to avoid issues when group names are updated in either Box or external systems.

##### invitability_level: `str`<a id="invitability_level-str"></a>

Specifies who can invite the group to collaborate on folders.  When set to `admins_only` the enterprise admin, co-admins, and the group's admin can invite the group.  When set to `admins_and_members` all the admins listed above and group members can invite the group.  When set to `all_managed_users` all managed users in the enterprise can invite the group.

##### member_viewability_level: `str`<a id="member_viewability_level-str"></a>

Specifies who can see the members of the group.  * `admins_only` - the enterprise admin, co-admins, group's   group admin * `admins_and_members` - all admins and group members * `all_managed_users` - all managed users in the   enterprise

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GroupsUpdateGroupRequest`](./box_python_sdk/type/groups_update_group_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GroupFull`](./box_python_sdk/pydantic/group_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/{group_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.integration_mappings.create_slack_mapping`<a id="boxintegration_mappingscreate_slack_mapping"></a>

Creates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack)
by mapping a Slack channel to a Box item.

You need Admin or Co-Admin role to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_slack_mapping_response = box.integration_mappings.create_slack_mapping(
    partner_item={
        "type": "channel",
        "id": "C12378991223",
        "slack_workspace_id": "T12352314",
        "slack_org_id": "E1234567",
    },
    box_item={
        "type": "folder",
        "id": "1234567891",
    },
    options={
        "is_access_management_disabled": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_item: [`IntegrationMappingPartnerItemSlack`](./box_python_sdk/type/integration_mapping_partner_item_slack.py)<a id="partner_item-integrationmappingpartneritemslackbox_python_sdktypeintegration_mapping_partner_item_slackpy"></a>


##### box_item: [`IntegrationMappingBoxItemSlack`](./box_python_sdk/type/integration_mapping_box_item_slack.py)<a id="box_item-integrationmappingboxitemslackbox_python_sdktypeintegration_mapping_box_item_slackpy"></a>


##### options: [`IntegrationMappingSlackOptions`](./box_python_sdk/type/integration_mapping_slack_options.py)<a id="options-integrationmappingslackoptionsbox_python_sdktypeintegration_mapping_slack_optionspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntegrationMappingSlackCreateRequest`](./box_python_sdk/type/integration_mapping_slack_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationMapping`](./box_python_sdk/pydantic/integration_mapping.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/integration_mappings/slack` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.integration_mappings.delete_slack_mapping`<a id="boxintegration_mappingsdelete_slack_mapping"></a>

Deletes a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).


You need Admin or Co-Admin role to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.integration_mappings.delete_slack_mapping(
    integration_mapping_id="11235432",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### integration_mapping_id: `str`<a id="integration_mapping_id-str"></a>

An ID of an integration mapping

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/integration_mappings/slack/{integration_mapping_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.integration_mappings.list_slack_mappings`<a id="boxintegration_mappingslist_slack_mappings"></a>

Lists [Slack integration mappings](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack) in a users' enterprise.

You need Admin or Co-Admin role to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_slack_mappings_response = box.integration_mappings.list_slack_mappings(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
    partner_item_type="channel",
    partner_item_id="12345",
    box_item_id="12345",
    box_item_type="folder",
    is_manually_created=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### partner_item_type: `str`<a id="partner_item_type-str"></a>

Mapped item type, for which the mapping should be returned

##### partner_item_id: `str`<a id="partner_item_id-str"></a>

ID of the mapped item, for which the mapping should be returned

##### box_item_id: `str`<a id="box_item_id-str"></a>

Box item ID, for which the mappings should be returned

##### box_item_type: `str`<a id="box_item_type-str"></a>

Box item type, for which the mappings should be returned

##### is_manually_created: `bool`<a id="is_manually_created-bool"></a>

Whether the mapping has been manually created

#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationMappings`](./box_python_sdk/pydantic/integration_mappings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/integration_mappings/slack` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.integration_mappings.update_slack_mapping`<a id="boxintegration_mappingsupdate_slack_mapping"></a>

Updates a [Slack integration mapping](https://support.box.com/hc/en-us/articles/4415585987859-Box-as-the-Content-Layer-for-Slack).
Supports updating the Box folder ID and options.

You need Admin or Co-Admin role to
use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_slack_mapping_response = box.integration_mappings.update_slack_mapping(
    integration_mapping_id="11235432",
    box_item={
        "type": "folder",
        "id": "1234567891",
    },
    options={
        "is_access_management_disabled": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### integration_mapping_id: `str`<a id="integration_mapping_id-str"></a>

An ID of an integration mapping

##### box_item: [`IntegrationMappingBoxItemSlack`](./box_python_sdk/type/integration_mapping_box_item_slack.py)<a id="box_item-integrationmappingboxitemslackbox_python_sdktypeintegration_mapping_box_item_slackpy"></a>


##### options: [`IntegrationMappingSlackOptions`](./box_python_sdk/type/integration_mapping_slack_options.py)<a id="options-integrationmappingslackoptionsbox_python_sdktypeintegration_mapping_slack_optionspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntegrationMappingsUpdateSlackMappingRequest`](./box_python_sdk/type/integration_mappings_update_slack_mapping_request.py)
At least one of `box_item` and `options` must be provided.

#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationMapping`](./box_python_sdk/pydantic/integration_mapping.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/integration_mappings/slack/{integration_mapping_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.invites.get_user_invite_status`<a id="boxinvitesget_user_invite_status"></a>

Returns the status of a user invite.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_invite_status_response = box.invites.get_user_invite_status(
    invite_id="213723",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invite_id: `str`<a id="invite_id-str"></a>

The ID of an invite.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`Invite`](./box_python_sdk/pydantic/invite.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invites/{invite_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.invites.invites`<a id="boxinvitesinvites"></a>

Invites an existing external user to join an enterprise.

The existing user can not be part of another enterprise and
must already have a Box account. Once invited, the user will receive an
email and are prompted to accept the invitation within the
Box web application.

This method requires the "Manage An Enterprise" scope enabled for
the application, which can be enabled within the developer console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invites_response = box.invites.invites(
    enterprise={
        "id": "1232234",
    },
    actionable_by={
        "login": "john@example.com",
    },
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enterprise: [`PostInvitesRequestEnterprise`](./box_python_sdk/type/post_invites_request_enterprise.py)<a id="enterprise-postinvitesrequestenterprisebox_python_sdktypepost_invites_request_enterprisepy"></a>


##### actionable_by: [`PostInvitesRequestActionableBy`](./box_python_sdk/type/post_invites_request_actionable_by.py)<a id="actionable_by-postinvitesrequestactionablebybox_python_sdktypepost_invites_request_actionable_bypy"></a>


##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostInvitesRequest`](./box_python_sdk/type/post_invites_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Invite`](./box_python_sdk/pydantic/invite.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invites` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policies.create_new_policy`<a id="boxlegal_hold_policiescreate_new_policy"></a>

Create a new legal hold policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_policy_response = box.legal_hold_policies.create_new_policy(
    policy_name="Sales Policy",
    description="A custom policy for the sales team",
    filter_started_at="2012-12-12T10:53:43-08:00",
    filter_ended_at="2012-12-18T10:53:43-08:00",
    is_ongoing=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_name: `str`<a id="policy_name-str"></a>

The name of the policy.

##### description: `str`<a id="description-str"></a>

A description for the policy.

##### filter_started_at: `datetime`<a id="filter_started_at-datetime"></a>

The filter start date.  When this policy is applied using a `custodian` legal hold assignments, it will only apply to file versions created or uploaded inside of the date range. Other assignment types, such as folders and files, will ignore the date filter.  Required if `is_ongoing` is set to `false`.

##### filter_ended_at: `datetime`<a id="filter_ended_at-datetime"></a>

The filter end date.  When this policy is applied using a `custodian` legal hold assignments, it will only apply to file versions created or uploaded inside of the date range. Other assignment types, such as folders and files, will ignore the date filter.  Required if `is_ongoing` is set to `false`.

##### is_ongoing: `bool`<a id="is_ongoing-bool"></a>

Whether new assignments under this policy should continue applying to files even after initialization.  When this policy is applied using a legal hold assignment, it will continue applying the policy to any new file versions even after it has been applied.  For example, if a legal hold assignment is placed on a user today, and that user uploads a file tomorrow, that file will get held. This will continue until the policy is retired.  Required if no filter dates are set.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LegalHoldPoliciesCreateNewPolicyRequest`](./box_python_sdk/type/legal_hold_policies_create_new_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicy`](./box_python_sdk/pydantic/legal_hold_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policies.get_policy`<a id="boxlegal_hold_policiesget_policy"></a>

Retrieve a legal hold policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_response = box.legal_hold_policies.get_policy(
    legal_hold_policy_id="324432",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_id: `str`<a id="legal_hold_policy_id-str"></a>

The ID of the legal hold policy

#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicy`](./box_python_sdk/pydantic/legal_hold_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policies/{legal_hold_policy_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policies.list_all`<a id="boxlegal_hold_policieslist_all"></a>

Retrieves a list of legal hold policies that belong to
an enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = box.legal_hold_policies.list_all(
    policy_name="Sales Policy",
    fields=["id", "type", "name"],
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_name: `str`<a id="policy_name-str"></a>

Limits results to policies for which the names start with this search term. This is a case-insensitive prefix.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicies`](./box_python_sdk/pydantic/legal_hold_policies.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policies.remove_policy`<a id="boxlegal_hold_policiesremove_policy"></a>

Delete an existing legal hold policy.

This is an asynchronous process. The policy will not be
fully deleted yet when the response returns.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.legal_hold_policies.remove_policy(
    legal_hold_policy_id="324432",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_id: `str`<a id="legal_hold_policy_id-str"></a>

The ID of the legal hold policy

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policies/{legal_hold_policy_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policies.update_policy`<a id="boxlegal_hold_policiesupdate_policy"></a>

Update legal hold policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_policy_response = box.legal_hold_policies.update_policy(
    legal_hold_policy_id="324432",
    description="A custom policy for the sales team",
    policy_name="Sales Policy",
    release_notes="Required for GDPR",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_id: `str`<a id="legal_hold_policy_id-str"></a>

The ID of the legal hold policy

##### description: `str`<a id="description-str"></a>

A description for the policy.

##### policy_name: `str`<a id="policy_name-str"></a>

The name of the policy.

##### release_notes: `str`<a id="release_notes-str"></a>

Notes around why the policy was released.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LegalHoldPoliciesUpdatePolicyRequest`](./box_python_sdk/type/legal_hold_policies_update_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicy`](./box_python_sdk/pydantic/legal_hold_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policies/{legal_hold_policy_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policy_assignments.assign_file_legal_hold`<a id="boxlegal_hold_policy_assignmentsassign_file_legal_hold"></a>

Assign a legal hold to a file, file version, folder, or user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_file_legal_hold_response = box.legal_hold_policy_assignments.assign_file_legal_hold(
    policy_id="123244",
    assign_to={
        "type": "folder",
        "id": "6564564",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

The ID of the policy to assign.

##### assign_to: [`LegalHoldPolicyAssignmentsAssignFileLegalHoldRequestAssignTo`](./box_python_sdk/type/legal_hold_policy_assignments_assign_file_legal_hold_request_assign_to.py)<a id="assign_to-legalholdpolicyassignmentsassignfilelegalholdrequestassigntobox_python_sdktypelegal_hold_policy_assignments_assign_file_legal_hold_request_assign_topy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LegalHoldPolicyAssignmentsAssignFileLegalHoldRequest`](./box_python_sdk/type/legal_hold_policy_assignments_assign_file_legal_hold_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicyAssignment`](./box_python_sdk/pydantic/legal_hold_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policy_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policy_assignments.get_assignment`<a id="boxlegal_hold_policy_assignmentsget_assignment"></a>

Retrieve a legal hold policy assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignment_response = box.legal_hold_policy_assignments.get_assignment(
    legal_hold_policy_assignment_id="753465",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_assignment_id: `str`<a id="legal_hold_policy_assignment_id-str"></a>

The ID of the legal hold policy assignment

#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicyAssignment`](./box_python_sdk/pydantic/legal_hold_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policy_assignments.get_list_items`<a id="boxlegal_hold_policy_assignmentsget_list_items"></a>

Retrieves a list of items a legal hold policy has been assigned to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_items_response = box.legal_hold_policy_assignments.get_list_items(
    policy_id="324432",
    assign_to_type="file",
    assign_to_id="1234323",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

The ID of the legal hold policy

##### assign_to_type: `str`<a id="assign_to_type-str"></a>

Filters the results by the type of item the policy was applied to.

##### assign_to_id: `str`<a id="assign_to_id-str"></a>

Filters the results by the ID of item the policy was applied to.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`LegalHoldPolicyAssignments`](./box_python_sdk/pydantic/legal_hold_policy_assignments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policy_assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policy_assignments.list_file_versions`<a id="boxlegal_hold_policy_assignmentslist_file_versions"></a>

Get a list of current file versions for a legal hold
assignment.

In some cases you may want to get previous file versions instead. In these
cases, use the `GET  /legal_hold_policy_assignments/:id/file_versions_on_hold`
API instead to return any previous versions of a file for this legal hold
policy assignment.

Due to ongoing re-architecture efforts this API might not return all file
versions held for this policy ID. Instead, this API will only return the
latest file version held in the newly developed architecture. The `GET
/file_version_legal_holds` API can be used to fetch current and past versions
of files held within the legacy architecture.

The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to
find a list of policy assignments for a given policy ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_file_versions_response = box.legal_hold_policy_assignments.list_file_versions(
    legal_hold_policy_assignment_id="753465",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_assignment_id: `str`<a id="legal_hold_policy_assignment_id-str"></a>

The ID of the legal hold policy assignment

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionLegalHolds`](./box_python_sdk/pydantic/file_version_legal_holds.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policy_assignments.list_previous_file_versions`<a id="boxlegal_hold_policy_assignmentslist_previous_file_versions"></a>

Get a list of previous file versions for a legal hold
assignment.

In some cases you may only need the latest file versions instead. In these
cases, use the `GET  /legal_hold_policy_assignments/:id/files_on_hold` API
instead to return any current (latest) versions of a file for this legal hold
policy assignment.

Due to ongoing re-architecture efforts this API might not return all files
held for this policy ID. Instead, this API will only return past file versions
held in the newly developed architecture. The `GET /file_version_legal_holds`
API can be used to fetch current and past versions of files held within the
legacy architecture.

The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to
find a list of policy assignments for a given policy ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_previous_file_versions_response = box.legal_hold_policy_assignments.list_previous_file_versions(
    legal_hold_policy_assignment_id="753465",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_assignment_id: `str`<a id="legal_hold_policy_assignment_id-str"></a>

The ID of the legal hold policy assignment

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`FileVersionLegalHolds`](./box_python_sdk/pydantic/file_version_legal_holds.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/file_versions_on_hold` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.legal_hold_policy_assignments.unassign_policy`<a id="boxlegal_hold_policy_assignmentsunassign_policy"></a>

Remove a legal hold from an item.

This is an asynchronous process. The policy will not be
fully removed yet when the response returns.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.legal_hold_policy_assignments.unassign_policy(
    legal_hold_policy_assignment_id="753465",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_hold_policy_assignment_id: `str`<a id="legal_hold_policy_assignment_id-str"></a>

The ID of the legal hold policy assignment

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_cascade_policies.apply_to_children`<a id="boxmetadata_cascade_policiesapply_to_children"></a>

Force the metadata on a folder with a metadata cascade policy to be applied to
all of its children. This can be used after creating a new cascade policy to
enforce the metadata to be cascaded down to all existing files within that
folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.metadata_cascade_policies.apply_to_children(
    conflict_resolution="none",
    metadata_cascade_policy_id="6fd4ff89-8fc1-42cf-8b29-1890dedd26d7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conflict_resolution: `str`<a id="conflict_resolution-str"></a>

Describes the desired behavior when dealing with the conflict where a metadata template already has an instance applied to a child.  * `none` will preserve the existing value on the file * `overwrite` will force-apply the templates values over   any existing values.

##### metadata_cascade_policy_id: `str`<a id="metadata_cascade_policy_id-str"></a>

The ID of the cascade policy to force-apply.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MetadataCascadePoliciesApplyToChildrenRequest`](./box_python_sdk/type/metadata_cascade_policies_apply_to_children_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_cascade_policies/{metadata_cascade_policy_id}/apply` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_cascade_policies.create_policy`<a id="boxmetadata_cascade_policiescreate_policy"></a>

Creates a new metadata cascade policy that applies a given
metadata template to a given folder and automatically
cascades it down to any files within that folder.

In order for the policy to be applied a metadata instance must first
be applied to the folder the policy is to be applied to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_policy_response = box.metadata_cascade_policies.create_policy(
    folder_id="1234567",
    scope="enterprise",
    template_key="productInfo",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The ID of the folder to apply the policy to. This folder will need to already have an instance of the targeted metadata template applied to it.

##### scope: `str`<a id="scope-str"></a>

The scope of the targeted metadata template. This template will need to already have an instance applied to the targeted folder.

##### template_key: `str`<a id="template_key-str"></a>

The key of the targeted metadata template. This template will need to already have an instance applied to the targeted folder.  In many cases the template key is automatically derived of its display name, for example `Contract Template` would become `contractTemplate`. In some cases the creator of the template will have provided its own template key.  Please [list the templates for an enterprise][list], or get all instances on a [file][file] or [folder][folder] to inspect a template's key.  [list]: e://get-metadata-templates-enterprise [file]: e://get-files-id-metadata [folder]: e://get-folders-id-metadata

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MetadataCascadePoliciesCreatePolicyRequest`](./box_python_sdk/type/metadata_cascade_policies_create_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MetadataCascadePolicy`](./box_python_sdk/pydantic/metadata_cascade_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_cascade_policies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_cascade_policies.get_policy_assigned_to_folder`<a id="boxmetadata_cascade_policiesget_policy_assigned_to_folder"></a>

Retrieve a specific metadata cascade policy assigned to a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_assigned_to_folder_response = box.metadata_cascade_policies.get_policy_assigned_to_folder(
    metadata_cascade_policy_id="6fd4ff89-8fc1-42cf-8b29-1890dedd26d7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### metadata_cascade_policy_id: `str`<a id="metadata_cascade_policy_id-str"></a>

The ID of the metadata cascade policy.

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataCascadePolicy`](./box_python_sdk/pydantic/metadata_cascade_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_cascade_policies/{metadata_cascade_policy_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_cascade_policies.list`<a id="boxmetadata_cascade_policieslist"></a>

Retrieves a list of all the metadata cascade policies
that are applied to a given folder. This can not be used on the root
folder with ID `0`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = box.metadata_cascade_policies.list(
    folder_id="31232",
    owner_enterprise_id="31232",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    offset=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

Specifies which folder to return policies for. This can not be used on the root folder with ID `0`.

##### owner_enterprise_id: `str`<a id="owner_enterprise_id-str"></a>

The ID of the enterprise ID for which to find metadata cascade policies. If not specified, it defaults to the current enterprise.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataCascadePolicies`](./box_python_sdk/pydantic/metadata_cascade_policies.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_cascade_policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_cascade_policies.remove_policy`<a id="boxmetadata_cascade_policiesremove_policy"></a>

Deletes a metadata cascade policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.metadata_cascade_policies.remove_policy(
    metadata_cascade_policy_id="6fd4ff89-8fc1-42cf-8b29-1890dedd26d7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### metadata_cascade_policy_id: `str`<a id="metadata_cascade_policy_id-str"></a>

The ID of the metadata cascade policy.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_cascade_policies/{metadata_cascade_policy_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(files).apply_template`<a id="boxmetadata_instances_filesapply_template"></a>

Applies an instance of a metadata template to a file.

In most cases only values that are present in the metadata template
will be accepted, except for the `global.properties` template which accepts
any key-value pair.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apply_template_response = box.metadata_instances_(files).apply_template(
    file_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MetadataInstancesFilesApplyTemplateRequest`](./box_python_sdk/type/metadata_instances_files_apply_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MetadataFull`](./box_python_sdk/pydantic/metadata_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/{scope}/{template_key}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(files).get_instance`<a id="boxmetadata_instances_filesget_instance"></a>

Retrieves the instance of a metadata template that has been applied to a
file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instance_response = box.metadata_instances_(files).get_instance(
    file_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataFull`](./box_python_sdk/pydantic/metadata_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/{scope}/{template_key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(files).list_file_metadata`<a id="boxmetadata_instances_fileslist_file_metadata"></a>

Retrieves all metadata for a given file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_file_metadata_response = box.metadata_instances_(files).list_file_metadata(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🔄 Return<a id="🔄-return"></a>

[`Metadatas`](./box_python_sdk/pydantic/metadatas.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(files).remove_instance`<a id="boxmetadata_instances_filesremove_instance"></a>

Deletes a piece of file metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.metadata_instances_(files).remove_instance(
    file_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/{scope}/{template_key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(files).update_instance_on_file`<a id="boxmetadata_instances_filesupdate_instance_on_file"></a>

Updates a piece of metadata on a file.

The metadata instance can only be updated if the template has already been
applied to the file before. When editing metadata, only values that match
the metadata template schema will be accepted.

The update is applied atomically. If any errors occur during the
application of the operations, the metadata instance will not be changed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instance_on_file_response = box.metadata_instances_(files).update_instance_on_file(
    body=[
        {
            "op": "add",
            "path": "/currentState",
            "value": "reviewed",
            "_from": "/nextState",
        }
    ],
    file_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

##### requestBody: [`MetadataInstancesFilesUpdateInstanceOnFileRequest`](./box_python_sdk/type/metadata_instances_files_update_instance_on_file_request.py)<a id="requestbody-metadatainstancesfilesupdateinstanceonfilerequestbox_python_sdktypemetadata_instances_files_update_instance_on_file_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataFull`](./box_python_sdk/pydantic/metadata_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/{scope}/{template_key}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(folders).apply_template`<a id="boxmetadata_instances_foldersapply_template"></a>

Applies an instance of a metadata template to a folder.

In most cases only values that are present in the metadata template
will be accepted, except for the `global.properties` template which accepts
any key-value pair.

To display the metadata template in the Box web app the enterprise needs to be
configured to enable **Cascading Folder Level Metadata** for the user in the
admin console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apply_template_response = box.metadata_instances_(folders).apply_template(
    folder_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MetadataInstancesFoldersApplyTemplateRequest`](./box_python_sdk/type/metadata_instances_folders_apply_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MetadataFull`](./box_python_sdk/pydantic/metadata_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/{scope}/{template_key}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(folders).get_folder_metadata_instance`<a id="boxmetadata_instances_foldersget_folder_metadata_instance"></a>

Retrieves the instance of a metadata template that has been applied to a
folder. This can not be used on the root folder with ID `0`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_folder_metadata_instance_response = box.metadata_instances_(folders).get_folder_metadata_instance(
    folder_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataFull`](./box_python_sdk/pydantic/metadata_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/{scope}/{template_key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(folders).list_on_folder`<a id="boxmetadata_instances_folderslist_on_folder"></a>

Retrieves all metadata for a given folder. This can not be used on the root
folder with ID `0`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_on_folder_response = box.metadata_instances_(folders).list_on_folder(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🔄 Return<a id="🔄-return"></a>

[`Metadatas`](./box_python_sdk/pydantic/metadatas.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(folders).remove_instance`<a id="boxmetadata_instances_foldersremove_instance"></a>

Deletes a piece of folder metadata.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.metadata_instances_(folders).remove_instance(
    folder_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/{scope}/{template_key}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_instances_(folders).update_instance_on_folder`<a id="boxmetadata_instances_foldersupdate_instance_on_folder"></a>

Updates a piece of metadata on a folder.

The metadata instance can only be updated if the template has already been
applied to the folder before. When editing metadata, only values that match
the metadata template schema will be accepted.

The update is applied atomically. If any errors occur during the
application of the operations, the metadata instance will not be changed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instance_on_folder_response = box.metadata_instances_(folders).update_instance_on_folder(
    body=[
        {
            "op": "add",
            "path": "/currentState",
            "value": "reviewed",
            "_from": "/nextState",
        }
    ],
    folder_id="12345",
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

##### requestBody: [`MetadataInstancesFoldersUpdateInstanceOnFolderRequest`](./box_python_sdk/type/metadata_instances_folders_update_instance_on_folder_request.py)<a id="requestbody-metadatainstancesfoldersupdateinstanceonfolderrequestbox_python_sdktypemetadata_instances_folders_update_instance_on_folder_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataFull`](./box_python_sdk/pydantic/metadata_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/metadata/{scope}/{template_key}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.create_new_template`<a id="boxmetadata_templatescreate_new_template"></a>

Creates a new metadata template that can be applied to
files and folders.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_template_response = box.metadata_templates.create_new_template(
    scope="enterprise",
    display_name="Product Info",
    template_key="productInfo",
    hidden=True,
    fields=[
        {
            "description": "The category",
            "type": "string",
            "key": "category",
            "display_name": "Category",
            "hidden": True,
        }
    ],
    copy_instance_on_item_copy=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template to create. Applications can only create templates for use within the authenticated user's enterprise.  This value needs to be set to `enterprise`, as `global` scopes can not be created by applications.

##### display_name: `str`<a id="display_name-str"></a>

The display name of the template.

##### template_key: `str`<a id="template_key-str"></a>

A unique identifier for the template. This identifier needs to be unique across the enterprise for which the metadata template is being created.  When not provided, the API will create a unique `templateKey` based on the value of the `displayName`.

##### hidden: `bool`<a id="hidden-bool"></a>

Defines if this template is visible in the Box web app UI, or if it is purely intended for usage through the API.

##### fields: [`MetadataTemplatesCreateNewTemplateRequestFields`](./box_python_sdk/type/metadata_templates_create_new_template_request_fields.py)<a id="fields-metadatatemplatescreatenewtemplaterequestfieldsbox_python_sdktypemetadata_templates_create_new_template_request_fieldspy"></a>

##### copy_instance_on_item_copy: `bool`<a id="copy_instance_on_item_copy-bool"></a>

Whether or not to copy any metadata attached to a file or folder when it is copied. By default, metadata is not copied along with a file or folder when it is copied.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MetadataTemplatesCreateNewTemplateRequest`](./box_python_sdk/type/metadata_templates_create_new_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplate`](./box_python_sdk/pydantic/metadata_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/schema` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.delete_schema`<a id="boxmetadata_templatesdelete_schema"></a>

Delete a metadata template and its instances.
This deletion is permanent and can not be reversed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.metadata_templates.delete_schema(
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/{scope}/{template_key}/schema` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.find_by_instance_id`<a id="boxmetadata_templatesfind_by_instance_id"></a>

Finds a metadata template by searching for the ID of an instance of the
template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_by_instance_id_response = box.metadata_templates.find_by_instance_id(
    metadata_instance_id="01234500-12f1-1234-aa12-b1d234cb567e",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### metadata_instance_id: `str`<a id="metadata_instance_id-str"></a>

The ID of an instance of the metadata template to find.

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplates`](./box_python_sdk/pydantic/metadata_templates.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.get_by_id`<a id="boxmetadata_templatesget_by_id"></a>

Retrieves a metadata template by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.metadata_templates.get_by_id(
    template_id="f7a9891f",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

The ID of the template

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplate`](./box_python_sdk/pydantic/metadata_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/{template_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.get_by_name_schema`<a id="boxmetadata_templatesget_by_name_schema"></a>

Retrieves a metadata template by its `scope` and `templateKey` values.

To find the `scope` and `templateKey` for a template, list all templates for
an enterprise or globally, or list all templates applied to a file or folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_schema_response = box.metadata_templates.get_by_name_schema(
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplate`](./box_python_sdk/pydantic/metadata_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/{scope}/{template_key}/schema` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.list_for_enterprise`<a id="boxmetadata_templateslist_for_enterprise"></a>

Used to retrieve all metadata templates created to be used specifically within
the user's enterprise

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_enterprise_response = box.metadata_templates.list_for_enterprise(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplates`](./box_python_sdk/pydantic/metadata_templates.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/enterprise` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.list_global`<a id="boxmetadata_templateslist_global"></a>

Used to retrieve all generic, global metadata templates available to all
enterprises using Box.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_global_response = box.metadata_templates.list_global(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplates`](./box_python_sdk/pydantic/metadata_templates.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/global` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.metadata_templates.update_schema`<a id="boxmetadata_templatesupdate_schema"></a>

Updates a metadata template.

The metadata template can only be updated if the template
already exists.

The update is applied atomically. If any errors occur during the
application of the operations, the metadata template will not be changed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_schema_response = box.metadata_templates.update_schema(
    body=[
        {
            "op": "addEnumOption",
            "field_key": "category",
            "field_keys": ["category", "name"],
            "enum_option_key": "option1",
            "enum_option_keys": ["option1", "option2", "option3"],
            "multi_select_option_key": "option1",
            "multi_select_option_keys": ["option1", "option2", "option3"],
        }
    ],
    scope="global",
    template_key="properties",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### scope: `str`<a id="scope-str"></a>

The scope of the metadata template

##### template_key: `str`<a id="template_key-str"></a>

The name of the metadata template

##### requestBody: [`MetadataTemplatesUpdateSchemaRequest`](./box_python_sdk/type/metadata_templates_update_schema_request.py)<a id="requestbody-metadatatemplatesupdateschemarequestbox_python_sdktypemetadata_templates_update_schema_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MetadataTemplate`](./box_python_sdk/pydantic/metadata_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_templates/{scope}/{template_key}/schema` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.recent_items.list_accessed_items`<a id="boxrecent_itemslist_accessed_items"></a>

Returns information about the recent items accessed
by a user, either in the last 90 days or up to the last
1000 items accessed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accessed_items_response = box.recent_items.list_accessed_items(
    fields=["id", "type", "name"],
    limit=1000,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`RecentItems`](./box_python_sdk/pydantic/recent_items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/recent_items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policies.create_policy`<a id="boxretention_policiescreate_policy"></a>

Creates a retention policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_policy_response = box.retention_policies.create_policy(
    policy_name="Some Policy Name",
    policy_type="finite",
    disposition_action="permanently_delete",
    description="Policy to retain all reports for at least one month",
    retention_length=None,
    retention_type="modifiable",
    can_owner_extend_retention=True,
    are_owners_notified=True,
    custom_notification_recipients=[
        {}
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_name: `str`<a id="policy_name-str"></a>

The name for the retention policy

##### policy_type: `str`<a id="policy_type-str"></a>

The type of the retention policy. A retention policy type can either be `finite`, where a specific amount of time to retain the content is known upfront, or `indefinite`, where the amount of time to retain the content is still unknown.

##### disposition_action: `str`<a id="disposition_action-str"></a>

The disposition action of the retention policy. `permanently_delete` deletes the content retained by the policy permanently. `remove_retention` lifts retention policy from the content, allowing it to be deleted by users once the retention policy has expired.

##### description: `str`<a id="description-str"></a>

The additional text description of the retention policy.

##### retention_length: Union[`Optional[str]`, `Union[int, float]`]<a id="retention_length-unionoptionalstr-unionint-float"></a>


The length of the retention policy. This value specifies the duration in days that the retention policy will be active for after being assigned to content.  If the policy has a `policy_type` of `indefinite`, the `retention_length` will also be `indefinite`.

##### retention_type: `str`<a id="retention_type-str"></a>

Specifies the retention type:  * `modifiable`: You can modify the retention policy. For example, you can add or remove folders, shorten or lengthen the policy duration, or delete the assignment. Use this type if your retention policy is not related to any regulatory purposes.  * `non_modifiable`: You can modify the retention policy only in a limited way: add a folder, lengthen the duration, retire the policy, change the disposition action or notification settings. You cannot perform other actions, such as deleting the assignment or shortening the policy duration. Use this type to ensure compliance with regulatory retention policies.

##### can_owner_extend_retention: `bool`<a id="can_owner_extend_retention-bool"></a>

Whether the owner of a file will be allowed to extend the retention.

##### are_owners_notified: `bool`<a id="are_owners_notified-bool"></a>

Whether owner and co-owners of a file are notified when the policy nears expiration.

##### custom_notification_recipients: List[`UserMini`]<a id="custom_notification_recipients-listusermini"></a>

A list of users notified when the retention policy duration is about to end.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RetentionPoliciesCreatePolicyRequest`](./box_python_sdk/type/retention_policies_create_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicy`](./box_python_sdk/pydantic/retention_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policies.delete_policy`<a id="boxretention_policiesdelete_policy"></a>

Permanently deletes a retention policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.retention_policies.delete_policy(
    retention_policy_id="982312",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_id: `str`<a id="retention_policy_id-str"></a>

The ID of the retention policy.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policies/{retention_policy_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policies.get_policy`<a id="boxretention_policiesget_policy"></a>

Retrieves a retention policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_policy_response = box.retention_policies.get_policy(
    retention_policy_id="982312",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_id: `str`<a id="retention_policy_id-str"></a>

The ID of the retention policy.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicy`](./box_python_sdk/pydantic/retention_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policies/{retention_policy_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policies.list_all`<a id="boxretention_policieslist_all"></a>

Retrieves all of the retention policies for an enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = box.retention_policies.list_all(
    policy_name="Sales Policy",
    policy_type="finite",
    created_by_user_id="21312321",
    fields=["id", "type", "name"],
    limit=1000,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_name: `str`<a id="policy_name-str"></a>

Filters results by a case sensitive prefix of the name of retention policies.

##### policy_type: `str`<a id="policy_type-str"></a>

Filters results by the type of retention policy.

##### created_by_user_id: `str`<a id="created_by_user_id-str"></a>

Filters results by the ID of the user who created policy.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.

#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicies`](./box_python_sdk/pydantic/retention_policies.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policies.update_policy`<a id="boxretention_policiesupdate_policy"></a>

Updates a retention policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_policy_response = box.retention_policies.update_policy(
    retention_policy_id="982312",
    description="Policy to retain all reports for at least one month",
    policy_name="Some Policy Name",
    disposition_action="string_example",
    retention_type="non-modifiable",
    retention_length=None,
    status="retired",
    can_owner_extend_retention=False,
    are_owners_notified=False,
    custom_notification_recipients=[
        {
            "id": "11446498",
            "type": "user",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_id: `str`<a id="retention_policy_id-str"></a>

The ID of the retention policy.

##### description: `Optional[str]`<a id="description-optionalstr"></a>

The additional text description of the retention policy.

##### policy_name: `Optional[str]`<a id="policy_name-optionalstr"></a>

The name for the retention policy

##### disposition_action: Union[`str`, `Optional[str]`]<a id="disposition_action-unionstr-optionalstr"></a>


The disposition action of the retention policy. This action can be `permanently_delete`, which will cause the content retained by the policy to be permanently deleted, or `remove_retention`, which will lift the retention policy from the content, allowing it to be deleted by users, once the retention policy has expired. You can use \\\"null\\\" if you don't want to change `disposition_action`.

##### retention_type: `Optional[str]`<a id="retention_type-optionalstr"></a>

Specifies the retention type:  * `modifiable`: You can modify the retention policy. For example, you can add or remove folders, shorten or lengthen the policy duration, or delete the assignment. Use this type if your retention policy is not related to any regulatory purposes. * `non-modifiable`: You can modify the retention policy only in a limited way: add a folder, lengthen the duration, retire the policy, change the disposition action or notification settings. You cannot perform other actions, such as deleting the assignment or shortening the policy duration. Use this type to ensure compliance with regulatory retention policies.  When updating a retention policy, you can use `non-modifiable` type only. You can convert a `modifiable` policy to `non-modifiable`, but not the other way around.

##### retention_length: Union[`Optional[str]`, `Union[int, float]`]<a id="retention_length-unionoptionalstr-unionint-float"></a>


The length of the retention policy. This value specifies the duration in days that the retention policy will be active for after being assigned to content.  If the policy has a `policy_type` of `indefinite`, the `retention_length` will also be `indefinite`.

##### status: `Optional[str]`<a id="status-optionalstr"></a>

Used to retire a retention policy.  If not retiring a policy, do not include this parameter or set it to `null`.

##### can_owner_extend_retention: `Optional[bool]`<a id="can_owner_extend_retention-optionalbool"></a>

Determines if the owner of items under the policy can extend the retention when the original retention duration is about to end.

##### are_owners_notified: `Optional[bool]`<a id="are_owners_notified-optionalbool"></a>

Determines if owners and co-owners of items under the policy are notified when the retention duration is about to end.

##### custom_notification_recipients: List[`UserBase`]<a id="custom_notification_recipients-listuserbase"></a>

A list of users notified when the retention duration is about to end.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RetentionPoliciesUpdatePolicyRequest`](./box_python_sdk/type/retention_policies_update_policy_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicy`](./box_python_sdk/pydantic/retention_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policies/{retention_policy_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policy_assignments.create_retention_assignment`<a id="boxretention_policy_assignmentscreate_retention_assignment"></a>

Assigns a retention policy to an item.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_retention_assignment_response = box.retention_policy_assignments.create_retention_assignment(
    policy_id="173463",
    assign_to={
        "type": "metadata_template",
        "id": "6564564",
    },
    filter_fields=[
        {
            "field": "a0f4ee4e-1dc1-4h90-a8a9-aef55fc681d4",
            "value": "0c27b756-0p87-4fe0-a43a-59fb661ccc4e",
        }
    ],
    start_date_field="upload_date",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### policy_id: `str`<a id="policy_id-str"></a>

The ID of the retention policy to assign

##### assign_to: [`RetentionPolicyAssignmentsCreateRetentionAssignmentRequestAssignTo`](./box_python_sdk/type/retention_policy_assignments_create_retention_assignment_request_assign_to.py)<a id="assign_to-retentionpolicyassignmentscreateretentionassignmentrequestassigntobox_python_sdktyperetention_policy_assignments_create_retention_assignment_request_assign_topy"></a>


##### filter_fields: [`RetentionPolicyAssignmentsCreateRetentionAssignmentRequestFilterFields`](./box_python_sdk/type/retention_policy_assignments_create_retention_assignment_request_filter_fields.py)<a id="filter_fields-retentionpolicyassignmentscreateretentionassignmentrequestfilterfieldsbox_python_sdktyperetention_policy_assignments_create_retention_assignment_request_filter_fieldspy"></a>

##### start_date_field: `str`<a id="start_date_field-str"></a>

The date the retention policy assignment begins.  If the `assigned_to` type is `metadata_template`, this field can be a date field's metadata attribute key id.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RetentionPolicyAssignmentsCreateRetentionAssignmentRequest`](./box_python_sdk/type/retention_policy_assignments_create_retention_assignment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicyAssignment`](./box_python_sdk/pydantic/retention_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policy_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policy_assignments.get_assignment`<a id="boxretention_policy_assignmentsget_assignment"></a>

Retrieves a retention policy assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_assignment_response = box.retention_policy_assignments.get_assignment(
    retention_policy_assignment_id="1233123",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_assignment_id: `str`<a id="retention_policy_assignment_id-str"></a>

The ID of the retention policy assignment.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicyAssignment`](./box_python_sdk/pydantic/retention_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policy_assignments/{retention_policy_assignment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policy_assignments.list_all_assignments`<a id="boxretention_policy_assignmentslist_all_assignments"></a>

Returns a list of all retention policy assignments associated with a specified
retention policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_assignments_response = box.retention_policy_assignments.list_all_assignments(
    retention_policy_id="982312",
    type="metadata_template",
    fields=["id", "type", "name"],
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_id: `str`<a id="retention_policy_id-str"></a>

The ID of the retention policy.

##### type: `str`<a id="type-str"></a>

The type of the retention policy assignment to retrieve.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`RetentionPolicyAssignments`](./box_python_sdk/pydantic/retention_policy_assignments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policies/{retention_policy_id}/assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policy_assignments.list_file_versions_under_retention`<a id="boxretention_policy_assignmentslist_file_versions_under_retention"></a>

Returns a list of file versions under retention for a retention policy
assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_file_versions_under_retention_response = box.retention_policy_assignments.list_file_versions_under_retention(
    retention_policy_assignment_id="1233123",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_assignment_id: `str`<a id="retention_policy_assignment_id-str"></a>

The ID of the retention policy assignment.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`FilesUnderRetention`](./box_python_sdk/pydantic/files_under_retention.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policy_assignments/{retention_policy_assignment_id}/file_versions_under_retention` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policy_assignments.list_files_under_retention`<a id="boxretention_policy_assignmentslist_files_under_retention"></a>

Returns a list of files under retention for a retention policy assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_files_under_retention_response = box.retention_policy_assignments.list_files_under_retention(
    retention_policy_assignment_id="1233123",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_assignment_id: `str`<a id="retention_policy_assignment_id-str"></a>

The ID of the retention policy assignment.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`FilesUnderRetention`](./box_python_sdk/pydantic/files_under_retention.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.retention_policy_assignments.remove_assignment`<a id="boxretention_policy_assignmentsremove_assignment"></a>

Removes a retention policy assignment
applied to content.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.retention_policy_assignments.remove_assignment(
    retention_policy_assignment_id="1233123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### retention_policy_assignment_id: `str`<a id="retention_policy_assignment_id-str"></a>

The ID of the retention policy assignment.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/retention_policy_assignments/{retention_policy_assignment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.search.items_by_metadata`<a id="boxsearchitems_by_metadata"></a>

Create a search using SQL-like syntax to return items that match specific
metadata.

By default, this endpoint returns only the most basic info about the items for
which the query matches. To get additional fields for each item, including any
of the metadata, use the `fields` attribute in the query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
items_by_metadata_response = box.search.items_by_metadata(
    _from="enterprise_123456.someTemplate",
    ancestor_folder_id="0",
    query="value >= :amount",
    _query_params={
        "key": "100",
    },
    order_by=[
        {
            "field_key": "amount",
            "direction": "asc",
        }
    ],
    limit=50,
    marker="AAAAAmVYB1FWec8GH6yWu2nwmanfMh07IyYInaa7DZDYjgO1H4KoLW29vPlLY173OKsci6h6xGh61gG73gnaxoS+o0BbI1/h6le6cikjlupVhASwJ2Cj0tOD9wlnrUMHHw3/ISf+uuACzrOMhN6d5fYrbidPzS6MdhJOejuYlvsg4tcBYzjauP3+VU51p77HFAIuObnJT0ff",
    fields=["extension", "created_at", "item_status", "metadata.enterprise_1234.contracts", "metadata.enterprise_1234.regions.location"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

Specifies the template used in the query. Must be in the form `scope.templateKey`. Not all templates can be used in this field, most notably the built-in, Box-provided classification templates can not be used in a query.

##### ancestor_folder_id: `str`<a id="ancestor_folder_id-str"></a>

The ID of the folder that you are restricting the query to. A value of zero will return results from all folders you have access to. A non-zero value will only return results found in the folder corresponding to the ID or in any of its subfolders.

##### query: `str`<a id="query-str"></a>

The query to perform. A query is a logical expression that is very similar to a SQL `SELECT` statement. Values in the search query can be turned into parameters specified in the `query_param` arguments list to prevent having to manually insert search values into the query string.  For example, a value of `:amount` would represent the `amount` value in `query_params` object.

##### _query_params: [`MetadataQueryQueryParams`](./box_python_sdk/type/metadata_query_query_params.py)<a id="_query_params-metadataqueryqueryparamsbox_python_sdktypemetadata_query_query_paramspy"></a>

##### order_by: [`MetadataQueryOrderBy`](./box_python_sdk/type/metadata_query_order_by.py)<a id="order_by-metadataqueryorderbybox_python_sdktypemetadata_query_order_bypy"></a>

##### limit: `int`<a id="limit-int"></a>

A value between 0 and 100 that indicates the maximum number of results to return for a single request. This only specifies a maximum boundary and will not guarantee the minimum number of results returned.

##### marker: `str`<a id="marker-str"></a>

Marker to use for requesting the next page.

##### fields: [`MetadataQueryFields`](./box_python_sdk/type/metadata_query_fields.py)<a id="fields-metadataqueryfieldsbox_python_sdktypemetadata_query_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MetadataQuery`](./box_python_sdk/type/metadata_query.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MetadataQueryResults`](./box_python_sdk/pydantic/metadata_query_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/metadata_queries/execute_read` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.search.search`<a id="boxsearchsearch"></a>

Searches for files, folders, web links, and shared files across the
users content or across the entire enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_response = box.search.search(
    query="sales",
    scope="user_content",
    file_extensions=["pdf", "png", "gif"],
    created_at_range=["2014-05-15T13:35:01-07:00", "2014-05-17T13:35:01-07:00"],
    updated_at_range=["2014-05-15T13:35:01-07:00", "2014-05-17T13:35:01-07:00"],
    size_range=[1000000, 5000000],
    owner_user_ids=["123422", "23532", "3241212"],
    recent_updater_user_ids=["123422", "23532", "3241212"],
    ancestor_folder_ids=["4535234", "234123235", "2654345"],
    content_types=["name", "description"],
    type="file",
    trash_content="non_trashed_only",
    mdfilters=[{
    "scope": "enterprise",
    "template_key": "contract",
}],
    sort="modified_at",
    direction="ASC",
    limit=100,
    include_recent_shared_links=True,
    fields=["id", "type", "name"],
    offset=1000,
    deleted_user_ids=["123422", "23532", "3241212"],
    deleted_at_range=["2014-05-15T13:35:01-07:00", "2014-05-17T13:35:01-07:00"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types.  This parameter supports a variety of operators to further refine the results returns.  * `\"\"` - by wrapping a query in double quotes only exact matches are   returned by the API. Exact searches do not return search matches   based on specific character sequences. Instead, they return   matches based on phrases, that is, word sequences. For example:   A search for `\"Blue-Box\"` may return search results including   the sequence `\"blue.box\"`, `\"Blue Box\"`, and `\"Blue-Box\"`;   any item containing the words `Blue` and `Box` consecutively, in   the order specified. * `AND` - returns items that contain both the search terms. For   example, a search for `marketing AND BoxWorks` returns items   that have both `marketing` and `BoxWorks` within its text in any order.   It does not return a result that only has `BoxWorks` in its text. * `OR` - returns items that contain either of the search terms. For   example, a search for `marketing OR BoxWorks` returns a result that   has either `marketing` or `BoxWorks` within its text. Using this   operator is not necessary as we implicitly interpret multi-word   queries as `OR` unless another supported boolean term is used. * `NOT` - returns items that do not contain the search term provided.   For example, a search for `marketing AND NOT BoxWorks` returns a result   that has only `marketing` within its text. Results containing   `BoxWorks` are omitted.  We do not support lower case (that is, `and`, `or`, and `not`) or mixed case (that is, `And`, `Or`, and `Not`) operators.  This field is required unless the `mdfilters` parameter is defined.

##### scope: `str`<a id="scope-str"></a>

Limits the search results to either the files that the user has access to, or to files available to the entire enterprise.  The scope defaults to `user_content`, which limits the search results to content that is available to the currently authenticated user.  The `enterprise_content` can be requested by an admin through our support channels. Once this scope has been enabled for a user, it will allow that use to query for content across the entire enterprise and not only the content that they have access to.

##### file_extensions: List[`str`]<a id="file_extensions-liststr"></a>

Limits the search results to any files that match any of the provided file extensions. This list is a comma-separated list of file extensions without the dots.

##### created_at_range: List[`str`]<a id="created_at_range-liststr"></a>

Limits the search results to any items created within a given date range.  Date ranges are defined as comma separated RFC3339 timestamps.  If the the start date is omitted (`,2014-05-17T13:35:01-07:00`) anything created before the end date will be returned.  If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the current date will be used as the end date instead.

##### updated_at_range: List[`str`]<a id="updated_at_range-liststr"></a>

Limits the search results to any items updated within a given date range.  Date ranges are defined as comma separated RFC3339 timestamps.  If the start date is omitted (`,2014-05-17T13:35:01-07:00`) anything updated before the end date will be returned.  If the end date is omitted (`2014-05-15T13:35:01-07:00,`) the current date will be used as the end date instead.

##### size_range: List[`int`]<a id="size_range-listint"></a>

Limits the search results to any items with a size within a given file size range. This applied to files and folders.  Size ranges are defined as comma separated list of a lower and upper byte size limit (inclusive).  The upper and lower bound can be omitted to create open ranges.

##### owner_user_ids: List[`str`]<a id="owner_user_ids-liststr"></a>

Limits the search results to any items that are owned by the given list of owners, defined as a list of comma separated user IDs.  The items still need to be owned or shared with the currently authenticated user for them to show up in the search results. If the user does not have access to any files owned by any of the users an empty result set will be returned.  To search across an entire enterprise, we recommend using the `enterprise_content` scope parameter which can be requested with our support team.

##### recent_updater_user_ids: List[`str`]<a id="recent_updater_user_ids-liststr"></a>

Limits the search results to any items that have been updated by the given list of users, defined as a list of comma separated user IDs.  The items still need to be owned or shared with the currently authenticated user for them to show up in the search results. If the user does not have access to any files owned by any of the users an empty result set will be returned.  This feature only searches back to the last 10 versions of an item.

##### ancestor_folder_ids: List[`str`]<a id="ancestor_folder_ids-liststr"></a>

Limits the search results to items within the given list of folders, defined as a comma separated lists of folder IDs.  Search results will also include items within any subfolders of those ancestor folders.  The folders still need to be owned or shared with the currently authenticated user. If the folder is not accessible by this user, or it does not exist, a `HTTP 404` error code will be returned instead.  To search across an entire enterprise, we recommend using the `enterprise_content` scope parameter which can be requested with our support team.

##### content_types: List[`str`]<a id="content_types-liststr"></a>

Limits the search results to any items that match the search query for a specific part of the file, for example the file description.  Content types are defined as a comma separated lists of Box recognized content types. The allowed content types are as follows.  * `name` - The name of the item, as defined by its `name` field. * `description` - The description of the item, as defined by its   `description` field. * `file_content` - The actual content of the file. * `comments` - The content of any of the comments on a file or    folder. * `tags` - Any tags that are applied to an item, as defined by its    `tags` field.

##### type: `str`<a id="type-str"></a>

Limits the search results to any items of this type. This parameter only takes one value. By default the API returns items that match any of these types.  * `file` - Limits the search results to files * `folder` - Limits the search results to folders * `web_link` - Limits the search results to web links, also known    as bookmarks

##### trash_content: `str`<a id="trash_content-str"></a>

Determines if the search should look in the trash for items.  By default, this API only returns search results for items not currently in the trash (`non_trashed_only`).  * `trashed_only` - Only searches for items currently in the trash * `non_trashed_only` - Only searches for items currently not in   the trash * `all_items` - Searches for both trashed and non-trashed items.

##### mdfilters: List[`MetadataFilter`]<a id="mdfilters-listmetadatafilter"></a>

Limits the search results to any items for which the metadata matches the provided filter.  This parameter contains a list of 1 metadata template to filter the search results by. This list can currently only contain one entry, though this might be expanded in the future.  This parameter is required unless the `query` parameter is provided.

##### sort: `str`<a id="sort-str"></a>

Defines the order in which search results are returned. This API defaults to returning items by relevance unless this parameter is explicitly specified.  * `relevance` (default) returns the results sorted by relevance to the query search term. The relevance is based on the occurrence of the search term in the items name, description, content, and additional properties. * `modified_at` returns the results ordered in descending order by date at which the item was last modified.

##### direction: `str`<a id="direction-str"></a>

Defines the direction in which search results are ordered. This API defaults to returning items in descending (`DESC`) order unless this parameter is explicitly specified.  When results are sorted by `relevance` the ordering is locked to returning items in descending order of relevance, and this parameter is ignored.

##### limit: `int`<a id="limit-int"></a>

Defines the maximum number of items to return as part of a page of results.

##### include_recent_shared_links: `bool`<a id="include_recent_shared_links-bool"></a>

Defines whether the search results should include any items that the user recently accessed through a shared link.  When this parameter has been set to true, the format of the response of this API changes to return a list of [Search Results with Shared Links](r://search_results_with_shared_links)

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### deleted_user_ids: List[`str`]<a id="deleted_user_ids-liststr"></a>

Limits the search results to items that were deleted by the given list of users, defined as a list of comma separated user IDs.  The `trash_content` parameter needs to be set to `trashed_only`.  If searching in trash is not performed, an empty result set is returned. The items need to be owned or shared with the currently authenticated user for them to show up in the search results.  If the user does not have access to any files owned by any of the users, an empty result set is returned.  Data available from 2023-02-01 onwards.

##### deleted_at_range: List[`str`]<a id="deleted_at_range-liststr"></a>

Limits the search results to any items deleted within a given date range.  Date ranges are defined as comma separated RFC3339 timestamps.  If the the start date is omitted (`2014-05-17T13:35:01-07:00`), anything deleted before the end date will be returned.  If the end date is omitted (`2014-05-15T13:35:01-07:00`), the current date will be used as the end date instead.  The `trash_content` parameter needs to be set to `trashed_only`.  If searching in trash is not performed, then an empty result is returned.  Data available from 2023-02-01 onwards.

#### 🔄 Return<a id="🔄-return"></a>

[`GetSearchResponse`](./box_python_sdk/pydantic/get_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.session_termination.create_session_termination_jobs`<a id="boxsession_terminationcreate_session_termination_jobs"></a>

Validates the roles and permissions of the user,
and creates asynchronous jobs
to terminate the user's sessions.
Returns the status for the POST request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_termination_jobs_response = box.session_termination.create_session_termination_jobs(
    user_ids=["123456", "456789"],
    user_logins=["user@sample.com", "user2@sample.com"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_ids: [`SessionTerminationCreateSessionTerminationJobsRequestUserIds`](./box_python_sdk/type/session_termination_create_session_termination_jobs_request_user_ids.py)<a id="user_ids-sessionterminationcreatesessionterminationjobsrequestuseridsbox_python_sdktypesession_termination_create_session_termination_jobs_request_user_idspy"></a>

##### user_logins: [`SessionTerminationCreateSessionTerminationJobsRequestUserLogins`](./box_python_sdk/type/session_termination_create_session_termination_jobs_request_user_logins.py)<a id="user_logins-sessionterminationcreatesessionterminationjobsrequestuserloginsbox_python_sdktypesession_termination_create_session_termination_jobs_request_user_loginspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SessionTerminationCreateSessionTerminationJobsRequest`](./box_python_sdk/type/session_termination_create_session_termination_jobs_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SessionTerminationMessage`](./box_python_sdk/pydantic/session_termination_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/terminate_sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.session_termination.create_termination_jobs`<a id="boxsession_terminationcreate_termination_jobs"></a>

Validates the roles and permissions of the group,
and creates asynchronous jobs
to terminate the group's sessions.
Returns the status for the POST request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_termination_jobs_response = box.session_termination.create_termination_jobs(
    group_ids=["123456", "456789"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_ids: [`SessionTerminationCreateTerminationJobsRequestGroupIds`](./box_python_sdk/type/session_termination_create_termination_jobs_request_group_ids.py)<a id="group_ids-sessionterminationcreateterminationjobsrequestgroupidsbox_python_sdktypesession_termination_create_termination_jobs_request_group_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SessionTerminationCreateTerminationJobsRequest`](./box_python_sdk/type/session_termination_create_termination_jobs_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SessionTerminationMessage`](./box_python_sdk/pydantic/session_termination_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/groups/terminate_sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(files).add_shared_link_to_file`<a id="boxshared_links_filesadd_shared_link_to_file"></a>

Adds a shared link to a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_shared_link_to_file_response = box.shared_links_(files).add_shared_link_to_file(
    file_id="12345",
    fields="shared_link",
    shared_link={
        "access": "open",
        "password": "do-n8t-use-this-Password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: [`SharedLinksFilesAddSharedLinkToFileRequestSharedLink`](./box_python_sdk/type/shared_links_files_add_shared_link_to_file_request_shared_link.py)<a id="shared_link-sharedlinksfilesaddsharedlinktofilerequestsharedlinkbox_python_sdktypeshared_links_files_add_shared_link_to_file_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksFilesAddSharedLinkToFileRequest`](./box_python_sdk/type/shared_links_files_add_shared_link_to_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}#add_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(files).get_by_shared_link`<a id="boxshared_links_filesget_by_shared_link"></a>

Returns the file represented by a shared link.

A shared file can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared file when only given a shared link.

The `shared_link_permission_options` array field can be returned
by requesting it in the `fields` query parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_shared_link_response = box.shared_links_(files).get_by_shared_link(
    boxapi="shared_link=[link]&shared_link_password=[password]",
    if_none_match="1",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### boxapi: `str`<a id="boxapi-str"></a>

A header containing the shared link and optional password for the shared link.  The format for this header is as follows.  `shared_link=[link]&shared_link_password=[password]`

##### if_none_match: `str`<a id="if_none_match-str"></a>

Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shared_items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(files).get_shared_link_info`<a id="boxshared_links_filesget_shared_link_info"></a>

Gets the information for a shared link on a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_shared_link_info_response = box.shared_links_(files).get_shared_link_info(
    file_id="12345",
    fields="shared_link",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}#get_shared_link` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(files).remove_shared_link`<a id="boxshared_links_filesremove_shared_link"></a>

Removes a shared link from a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_shared_link_response = box.shared_links_(files).remove_shared_link(
    file_id="12345",
    fields="shared_link",
    shared_link={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="shared_link-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

By setting this value to `null`, the shared link is removed from the file.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksFilesRemoveSharedLinkRequest`](./box_python_sdk/type/shared_links_files_remove_shared_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}#remove_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(files).update_link_on_file`<a id="boxshared_links_filesupdate_link_on_file"></a>

Updates a shared link on a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_link_on_file_response = box.shared_links_(files).update_link_on_file(
    file_id="12345",
    fields="shared_link",
    shared_link={
        "access": "open",
        "password": "do-n8t-use-this-Password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: [`SharedLinksFilesUpdateLinkOnFileRequestSharedLink`](./box_python_sdk/type/shared_links_files_update_link_on_file_request_shared_link.py)<a id="shared_link-sharedlinksfilesupdatelinkonfilerequestsharedlinkbox_python_sdktypeshared_links_files_update_link_on_file_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksFilesUpdateLinkOnFileRequest`](./box_python_sdk/type/shared_links_files_update_link_on_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileFull`](./box_python_sdk/pydantic/file_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}#update_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(folders).add_link_to_folder`<a id="boxshared_links_foldersadd_link_to_folder"></a>

Adds a shared link to a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_link_to_folder_response = box.shared_links_(folders).add_link_to_folder(
    folder_id="12345",
    fields="shared_link",
    shared_link={
        "access": "open",
        "password": "do-n8t-use-this-Password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: [`SharedLinksFoldersAddLinkToFolderRequestSharedLink`](./box_python_sdk/type/shared_links_folders_add_link_to_folder_request_shared_link.py)<a id="shared_link-sharedlinksfoldersaddlinktofolderrequestsharedlinkbox_python_sdktypeshared_links_folders_add_link_to_folder_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksFoldersAddLinkToFolderRequest`](./box_python_sdk/type/shared_links_folders_add_link_to_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}#add_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(folders).find_folder_by_shared_link`<a id="boxshared_links_foldersfind_folder_by_shared_link"></a>

Return the folder represented by a shared link.

A shared folder can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared folder when only given a shared link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_folder_by_shared_link_response = box.shared_links_(folders).find_folder_by_shared_link(
    boxapi="shared_link=[link]&shared_link_password=[password]",
    if_none_match="1",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### boxapi: `str`<a id="boxapi-str"></a>

A header containing the shared link and optional password for the shared link.  The format for this header is as follows.  `shared_link=[link]&shared_link_password=[password]`

##### if_none_match: `str`<a id="if_none_match-str"></a>

Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shared_items#folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(folders).get_shared_link_for_folder`<a id="boxshared_links_foldersget_shared_link_for_folder"></a>

Gets the information for a shared link on a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_shared_link_for_folder_response = box.shared_links_(folders).get_shared_link_for_folder(
    folder_id="12345",
    fields="shared_link",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}#get_shared_link` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(folders).remove_from_folder`<a id="boxshared_links_foldersremove_from_folder"></a>

Removes a shared link from a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_from_folder_response = box.shared_links_(folders).remove_from_folder(
    folder_id="12345",
    fields="shared_link",
    shared_link={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="shared_link-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

By setting this value to `null`, the shared link is removed from the folder.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksFoldersRemoveFromFolderRequest`](./box_python_sdk/type/shared_links_folders_remove_from_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}#remove_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(folders).update_folder_shared_link`<a id="boxshared_links_foldersupdate_folder_shared_link"></a>

Updates a shared link on a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_folder_shared_link_response = box.shared_links_(folders).update_folder_shared_link(
    folder_id="12345",
    fields="shared_link",
    shared_link={
        "access": "open",
        "password": "do-n8t-use-this-Password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: [`SharedLinksFoldersUpdateFolderSharedLinkRequestSharedLink`](./box_python_sdk/type/shared_links_folders_update_folder_shared_link_request_shared_link.py)<a id="shared_link-sharedlinksfoldersupdatefoldersharedlinkrequestsharedlinkbox_python_sdktypeshared_links_folders_update_folder_shared_link_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksFoldersUpdateFolderSharedLinkRequest`](./box_python_sdk/type/shared_links_folders_update_folder_shared_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}#update_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(web_links).add_link_to_web_link`<a id="boxshared_links_web_linksadd_link_to_web_link"></a>

Adds a shared link to a web link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_link_to_web_link_response = box.shared_links_(web_links).add_link_to_web_link(
    web_link_id="12345",
    fields="shared_link",
    shared_link={
        "access": "open",
        "password": "do-n8t-use-this-Password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: [`SharedLinksWebLinksAddLinkToWebLinkRequestSharedLink`](./box_python_sdk/type/shared_links_web_links_add_link_to_web_link_request_shared_link.py)<a id="shared_link-sharedlinksweblinksaddlinktoweblinkrequestsharedlinkbox_python_sdktypeshared_links_web_links_add_link_to_web_link_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksWebLinksAddLinkToWebLinkRequest`](./box_python_sdk/type/shared_links_web_links_add_link_to_web_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}#add_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(web_links).find_shared_web_link`<a id="boxshared_links_web_linksfind_shared_web_link"></a>

Returns the web link represented by a shared link.

A shared web link can be represented by a shared link,
which can originate within the current enterprise or within another.

This endpoint allows an application to retrieve information about a
shared web link when only given a shared link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_shared_web_link_response = box.shared_links_(web_links).find_shared_web_link(
    boxapi="shared_link=[link]&shared_link_password=[password]",
    if_none_match="1",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### boxapi: `str`<a id="boxapi-str"></a>

A header containing the shared link and optional password for the shared link.  The format for this header is as follows.  `shared_link=[link]&shared_link_password=[password]`

##### if_none_match: `str`<a id="if_none_match-str"></a>

Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shared_items#web_links` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(web_links).get_link_info`<a id="boxshared_links_web_linksget_link_info"></a>

Gets the information for a shared link on a web link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_link_info_response = box.shared_links_(web_links).get_link_info(
    web_link_id="12345",
    fields="shared_link",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}#get_shared_link` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(web_links).remove_shared_link`<a id="boxshared_links_web_linksremove_shared_link"></a>

Removes a shared link from a web link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_shared_link_response = box.shared_links_(web_links).remove_shared_link(
    web_link_id="12345",
    fields="shared_link",
    shared_link={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="shared_link-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

By setting this value to `null`, the shared link is removed from the web link.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksWebLinksRemoveSharedLinkRequest`](./box_python_sdk/type/shared_links_web_links_remove_shared_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}#remove_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shared_links_(web_links).update_shared_link`<a id="boxshared_links_web_linksupdate_shared_link"></a>

Updates a shared link on a web link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_shared_link_response = box.shared_links_(web_links).update_shared_link(
    web_link_id="12345",
    fields="shared_link",
    shared_link={
        "access": "open",
        "password": "do-n8t-use-this-Password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### fields: `str`<a id="fields-str"></a>

Explicitly request the `shared_link` fields to be returned for this item.

##### shared_link: [`SharedLinksWebLinksUpdateSharedLinkRequestSharedLink`](./box_python_sdk/type/shared_links_web_links_update_shared_link_request_shared_link.py)<a id="shared_link-sharedlinksweblinksupdatesharedlinkrequestsharedlinkbox_python_sdktypeshared_links_web_links_update_shared_link_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SharedLinksWebLinksUpdateSharedLinkRequest`](./box_python_sdk/type/shared_links_web_links_update_shared_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}#update_shared_link` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_reports.create_report`<a id="boxshield_information_barrier_reportscreate_report"></a>

Creates a shield information barrier report for a given barrier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_report_response = box.shield_information_barrier_reports.create_report(
    shield_information_barrier={
        "id": "11446498",
        "type": "shield_information_barrier",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier: [`ShieldInformationBarrierBase`](./box_python_sdk/type/shield_information_barrier_base.py)<a id="shield_information_barrier-shieldinformationbarrierbasebox_python_sdktypeshield_information_barrier_basepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarrierReference`](./box_python_sdk/type/shield_information_barrier_reference.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierReport`](./box_python_sdk/pydantic/shield_information_barrier_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_reports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_reports.get_by_id`<a id="boxshield_information_barrier_reportsget_by_id"></a>

Retrieves a shield information barrier report by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.shield_information_barrier_reports.get_by_id(
    shield_information_barrier_report_id="3423",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_report_id: `str`<a id="shield_information_barrier_report_id-str"></a>

The ID of the shield information barrier Report.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierReport`](./box_python_sdk/pydantic/shield_information_barrier_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_reports/{shield_information_barrier_report_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_reports.list_reports`<a id="boxshield_information_barrier_reportslist_reports"></a>

Lists shield information barrier reports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_reports_response = box.shield_information_barrier_reports.list_reports(
    shield_information_barrier_id="1910967",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_id: `str`<a id="shield_information_barrier_id-str"></a>

The ID of the shield information barrier.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierReports`](./box_python_sdk/pydantic/shield_information_barrier_reports.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_reports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_members.create_new_member`<a id="boxshield_information_barrier_segment_memberscreate_new_member"></a>

Creates a new shield information barrier segment member.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_member_response = box.shield_information_barrier_segment_members.create_new_member(
    shield_information_barrier_segment={
        "id": "432554",
        "type": "shield_information_barrier_segment",
    },
    user={
        "id": "11446498",
        "type": "user",
    },
    type="shield_information_barrier_segment_member",
    shield_information_barrier={
        "id": "11446498",
        "type": "shield_information_barrier",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment: [`ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment`](./box_python_sdk/type/shield_information_barrier_segment_members_create_new_member_request_shield_information_barrier_segment.py)<a id="shield_information_barrier_segment-shieldinformationbarriersegmentmemberscreatenewmemberrequestshieldinformationbarriersegmentbox_python_sdktypeshield_information_barrier_segment_members_create_new_member_request_shield_information_barrier_segmentpy"></a>


##### user: [`UserBase`](./box_python_sdk/type/user_base.py)<a id="user-userbasebox_python_sdktypeuser_basepy"></a>


User to which restriction will be applied.

##### type: `str`<a id="type-str"></a>

-| A type of the shield barrier segment member.

##### shield_information_barrier: [`ShieldInformationBarrierBase`](./box_python_sdk/type/shield_information_barrier_base.py)<a id="shield_information_barrier-shieldinformationbarrierbasebox_python_sdktypeshield_information_barrier_basepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarrierSegmentMembersCreateNewMemberRequest`](./box_python_sdk/type/shield_information_barrier_segment_members_create_new_member_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegmentMember`](./box_python_sdk/pydantic/shield_information_barrier_segment_member.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_members` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_members.get_by_id`<a id="boxshield_information_barrier_segment_membersget_by_id"></a>

Retrieves a shield information barrier
segment member by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.shield_information_barrier_segment_members.get_by_id(
    shield_information_barrier_segment_member_id="7815",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_member_id: `str`<a id="shield_information_barrier_segment_member_id-str"></a>

The ID of the shield information barrier segment Member.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegmentMember`](./box_python_sdk/pydantic/shield_information_barrier_segment_member.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_members.list_segment_members_based_on_ids`<a id="boxshield_information_barrier_segment_memberslist_segment_members_based_on_ids"></a>

Lists shield information barrier segment members
based on provided segment IDs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_segment_members_based_on_ids_response = box.shield_information_barrier_segment_members.list_segment_members_based_on_ids(
    shield_information_barrier_segment_id="3423",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_id: `str`<a id="shield_information_barrier_segment_id-str"></a>

The ID of the shield information barrier segment.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegmentMembers`](./box_python_sdk/pydantic/shield_information_barrier_segment_members.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_members.remove_by_id`<a id="boxshield_information_barrier_segment_membersremove_by_id"></a>

Deletes a shield information barrier
segment member based on provided ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.shield_information_barrier_segment_members.remove_by_id(
    shield_information_barrier_segment_member_id="7815",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_member_id: `str`<a id="shield_information_barrier_segment_member_id-str"></a>

The ID of the shield information barrier segment Member.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_restrictions.create_barrier_object`<a id="boxshield_information_barrier_segment_restrictionscreate_barrier_object"></a>

Creates a shield information barrier
segment restriction object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_barrier_object_response = box.shield_information_barrier_segment_restrictions.create_barrier_object(
    type="shield_information_barrier_segment_restriction",
    shield_information_barrier_segment={
        "id": "1910967",
        "type": "shield_information_barrier_segment",
    },
    restricted_segment={
        "id": "1910967",
        "type": "shield_information_barrier_segment",
    },
    shield_information_barrier={
        "id": "11446498",
        "type": "shield_information_barrier",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

The type of the shield barrier segment restriction for this member.

##### shield_information_barrier_segment: [`ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment`](./box_python_sdk/type/shield_information_barrier_segment_restrictions_create_barrier_object_request_shield_information_barrier_segment.py)<a id="shield_information_barrier_segment-shieldinformationbarriersegmentrestrictionscreatebarrierobjectrequestshieldinformationbarriersegmentbox_python_sdktypeshield_information_barrier_segment_restrictions_create_barrier_object_request_shield_information_barrier_segmentpy"></a>


##### restricted_segment: [`ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment`](./box_python_sdk/type/shield_information_barrier_segment_restrictions_create_barrier_object_request_restricted_segment.py)<a id="restricted_segment-shieldinformationbarriersegmentrestrictionscreatebarrierobjectrequestrestrictedsegmentbox_python_sdktypeshield_information_barrier_segment_restrictions_create_barrier_object_request_restricted_segmentpy"></a>


##### shield_information_barrier: [`ShieldInformationBarrierBase`](./box_python_sdk/type/shield_information_barrier_base.py)<a id="shield_information_barrier-shieldinformationbarrierbasebox_python_sdktypeshield_information_barrier_basepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequest`](./box_python_sdk/type/shield_information_barrier_segment_restrictions_create_barrier_object_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegmentRestriction`](./box_python_sdk/pydantic/shield_information_barrier_segment_restriction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_restrictions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_restrictions.get_by_id`<a id="boxshield_information_barrier_segment_restrictionsget_by_id"></a>

Retrieves a shield information barrier segment
restriction based on provided ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.shield_information_barrier_segment_restrictions.get_by_id(
    shield_information_barrier_segment_restriction_id="4563",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_restriction_id: `str`<a id="shield_information_barrier_segment_restriction_id-str"></a>

The ID of the shield information barrier segment Restriction.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegmentRestriction`](./box_python_sdk/pydantic/shield_information_barrier_segment_restriction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_restrictions.list_based_on_segment_id`<a id="boxshield_information_barrier_segment_restrictionslist_based_on_segment_id"></a>

Lists shield information barrier segment restrictions
based on provided segment ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_based_on_segment_id_response = box.shield_information_barrier_segment_restrictions.list_based_on_segment_id(
    shield_information_barrier_segment_id="3423",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_id: `str`<a id="shield_information_barrier_segment_id-str"></a>

The ID of the shield information barrier segment.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegmentRestrictions`](./box_python_sdk/pydantic/shield_information_barrier_segment_restrictions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_restrictions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segment_restrictions.remove_by_id`<a id="boxshield_information_barrier_segment_restrictionsremove_by_id"></a>

Delete shield information barrier segment restriction
based on provided ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.shield_information_barrier_segment_restrictions.remove_by_id(
    shield_information_barrier_segment_restriction_id="4563",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_restriction_id: `str`<a id="shield_information_barrier_segment_restriction_id-str"></a>

The ID of the shield information barrier segment Restriction.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segments.create_segment`<a id="boxshield_information_barrier_segmentscreate_segment"></a>

Creates a shield information barrier segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_segment_response = box.shield_information_barrier_segments.create_segment(
    shield_information_barrier={
        "id": "11446498",
        "type": "shield_information_barrier",
    },
    name="Investment Banking",
    description='Corporate division that engages in\n advisory_based financial\ntransactions on behalf of individuals,\ncorporations, and governments.',
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier: [`ShieldInformationBarrierBase`](./box_python_sdk/type/shield_information_barrier_base.py)<a id="shield_information_barrier-shieldinformationbarrierbasebox_python_sdktypeshield_information_barrier_basepy"></a>


##### name: `str`<a id="name-str"></a>

Name of the shield information barrier segment

##### description: `str`<a id="description-str"></a>

Description of the shield information barrier segment

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarrierSegmentsCreateSegmentRequest`](./box_python_sdk/type/shield_information_barrier_segments_create_segment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegment`](./box_python_sdk/pydantic/shield_information_barrier_segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segments.delete_segment_by_id`<a id="boxshield_information_barrier_segmentsdelete_segment_by_id"></a>

Deletes the shield information barrier segment
based on provided ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.shield_information_barrier_segments.delete_segment_by_id(
    shield_information_barrier_segment_id="3423",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_id: `str`<a id="shield_information_barrier_segment_id-str"></a>

The ID of the shield information barrier segment.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segments/{shield_information_barrier_segment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segments.get_by_id`<a id="boxshield_information_barrier_segmentsget_by_id"></a>

Retrieves shield information barrier segment based on provided ID..

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.shield_information_barrier_segments.get_by_id(
    shield_information_barrier_segment_id="3423",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_id: `str`<a id="shield_information_barrier_segment_id-str"></a>

The ID of the shield information barrier segment.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegment`](./box_python_sdk/pydantic/shield_information_barrier_segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segments/{shield_information_barrier_segment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segments.list_information_objects`<a id="boxshield_information_barrier_segmentslist_information_objects"></a>

Retrieves a list of shield information barrier segment objects
for the specified Information Barrier ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_information_objects_response = box.shield_information_barrier_segments.list_information_objects(
    shield_information_barrier_id="1910967",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_id: `str`<a id="shield_information_barrier_id-str"></a>

The ID of the shield information barrier.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegments`](./box_python_sdk/pydantic/shield_information_barrier_segments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barrier_segments.update_by_id`<a id="boxshield_information_barrier_segmentsupdate_by_id"></a>

Updates the shield information barrier segment based on provided ID..

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = box.shield_information_barrier_segments.update_by_id(
    shield_information_barrier_segment_id="3423",
    description='Corporate division that engages in advisory_based\nfinancial transactions on behalf of individuals,\ncorporations, and governments.',
    name="Investment Banking",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_segment_id: `str`<a id="shield_information_barrier_segment_id-str"></a>

The ID of the shield information barrier segment.

##### description: `Optional[str]`<a id="description-optionalstr"></a>

The updated description for the shield information barrier segment.

##### name: `str`<a id="name-str"></a>

The updated name for the shield information barrier segment.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarrierSegmentsUpdateByIdRequest`](./box_python_sdk/type/shield_information_barrier_segments_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrierSegment`](./box_python_sdk/pydantic/shield_information_barrier_segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barrier_segments/{shield_information_barrier_segment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barriers.add_changed_status`<a id="boxshield_information_barriersadd_changed_status"></a>

Change status of shield information barrier with the specified ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_changed_status_response = box.shield_information_barriers.add_changed_status(
    id="1910967",
    status="pending",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the shield information barrier.

##### status: `str`<a id="status-str"></a>

The desired status for the shield information barrier.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarriersAddChangedStatusRequest`](./box_python_sdk/type/shield_information_barriers_add_changed_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrier`](./box_python_sdk/pydantic/shield_information_barrier.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barriers/change_status` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barriers.create_barrier`<a id="boxshield_information_barrierscreate_barrier"></a>

Creates a shield information barrier to
separate individuals/groups within the same
firm and prevents confidential information passing between them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_barrier_response = box.shield_information_barriers.create_barrier(
    enterprise={
        "id": "1910967",
        "type": "enterprise",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### enterprise: [`EnterpriseBase`](./box_python_sdk/type/enterprise_base.py)<a id="enterprise-enterprisebasebox_python_sdktypeenterprise_basepy"></a>


The `type` and `id` of enterprise this barrier is under.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShieldInformationBarriersCreateBarrierRequest`](./box_python_sdk/type/shield_information_barriers_create_barrier_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrier`](./box_python_sdk/pydantic/shield_information_barrier.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barriers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barriers.get_by_id`<a id="boxshield_information_barriersget_by_id"></a>

Get shield information barrier based on provided ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.shield_information_barriers.get_by_id(
    shield_information_barrier_id="1910967",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### shield_information_barrier_id: `str`<a id="shield_information_barrier_id-str"></a>

The ID of the shield information barrier.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarrier`](./box_python_sdk/pydantic/shield_information_barrier.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barriers/{shield_information_barrier_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.shield_information_barriers.list_information_objects`<a id="boxshield_information_barrierslist_information_objects"></a>

Retrieves a list of shield information barrier objects
for the enterprise of JWT.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_information_objects_response = box.shield_information_barriers.list_information_objects(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ShieldInformationBarriers`](./box_python_sdk/pydantic/shield_information_barriers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shield_information_barriers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_requests.cancel_request`<a id="boxsign_requestscancel_request"></a>

Cancels a sign request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_request_response = box.sign_requests.cancel_request(
    sign_request_id="33243242",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sign_request_id: `str`<a id="sign_request_id-str"></a>

The ID of the sign request

#### 🔄 Return<a id="🔄-return"></a>

[`SignRequest`](./box_python_sdk/pydantic/sign_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_requests/{sign_request_id}/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_requests.create_request`<a id="boxsign_requestscreate_request"></a>

Creates a sign request. This involves preparing a document for signing and
sending the sign request to signers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = box.sign_requests.create_request(
    signers=[
        {
            "email": "example@gmail.com",
            "role": "signer",
            "is_in_person": True,
            "order": 2,
            "embed_url_external_user_id": "1234",
            "redirect_url": "https://example.com",
            "declined_redirect_url": "https://declined-example.com",
            "login_required": True,
            "verification_phone_number": "6314578901",
            "password": "SecretPassword123",
            "signer_group_id": "cd4ff89-8fc1-42cf-8b29-1890dedd26d7",
        }
    ],
    is_document_preparation_needed=True,
    redirect_url="https://www.example.com",
    declined_redirect_url="https://declined-redirect.com",
    are_text_signatures_enabled=True,
    email_subject="Sign Request from Acme",
    email_message="Hello! Please sign the document below",
    are_reminders_enabled=True,
    name="name",
    prefill_tags=[
        {
            "document_tag_id": "1234",
            "text_value": "text",
            "checkbox_value": True,
            "date_value": "2021-04-26",
        }
    ],
    days_valid=2,
    external_id="123",
    is_phone_verification_required_to_view=True,
    template_id="123075213-af2c8822-3ef2-4952-8557-52d69c2fe9cb",
    source_files=[
        {
            "id": "12345",
            "etag": "1",
            "type": "file",
        }
    ],
    signature_color="blue",
    parent_folder=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signers: List[`SignRequestCreateSigner`]<a id="signers-listsignrequestcreatesigner"></a>

Array of signers for the sign request. 35 is the max number of signers permitted.

##### is_document_preparation_needed: `bool`<a id="is_document_preparation_needed-bool"></a>

Indicates if the sender should receive a `prepare_url` in the response to complete document preparation via UI.

##### redirect_url: `Optional[str]`<a id="redirect_url-optionalstr"></a>

When specified, signature request will be redirected to this url when a document is signed.

##### declined_redirect_url: `Optional[str]`<a id="declined_redirect_url-optionalstr"></a>

The uri that a signer will be redirected to after declining to sign a document.

##### are_text_signatures_enabled: `bool`<a id="are_text_signatures_enabled-bool"></a>

Disables the usage of signatures generated by typing (text).

##### email_subject: `Optional[str]`<a id="email_subject-optionalstr"></a>

Subject of sign request email. This is cleaned by sign request. If this field is not passed, a default subject will be used.

##### email_message: `Optional[str]`<a id="email_message-optionalstr"></a>

Message to include in sign request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used.

##### are_reminders_enabled: `bool`<a id="are_reminders_enabled-bool"></a>

Reminds signers to sign a document on day 3, 8, 13 and 18. Reminders are only sent to outstanding signers.

##### name: `str`<a id="name-str"></a>

Name of the sign request.

##### prefill_tags: List[`SignRequestPrefillTag`]<a id="prefill_tags-listsignrequestprefilltag"></a>

When a document contains sign related tags in the content, you can prefill them using this `prefill_tags` by referencing the 'id' of the tag as the `external_id` field of the prefill tag.

##### days_valid: `Optional[int]`<a id="days_valid-optionalint"></a>

Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire.

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

This can be used to reference an ID in an external system that the sign request is related to.

##### is_phone_verification_required_to_view: `Optional[bool]`<a id="is_phone_verification_required_to_view-optionalbool"></a>

Forces signers to verify a text message prior to viewing the document. You must specify the phone number of signers to have this setting apply to them.

##### template_id: `Optional[str]`<a id="template_id-optionalstr"></a>

When a signature request is created from a template this field will indicate the id of that template.

##### source_files: List[`FileBase`]<a id="source_files-listfilebase"></a>

List of files to create a signing document from. This is currently limited to ten files. Only the ID and type fields are required for each file.

##### signature_color: `Optional[str]`<a id="signature_color-optionalstr"></a>

Force a specific color for the signature (blue, black, or red)

##### parent_folder: Union[`FolderMini`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent_folder-unionfoldermini-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SignRequestCreateRequest`](./box_python_sdk/type/sign_request_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SignRequest`](./box_python_sdk/pydantic/sign_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_requests.get_by_id`<a id="boxsign_requestsget_by_id"></a>

Gets a sign request by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = box.sign_requests.get_by_id(
    sign_request_id="33243242",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sign_request_id: `str`<a id="sign_request_id-str"></a>

The ID of the sign request

#### 🔄 Return<a id="🔄-return"></a>

[`SignRequest`](./box_python_sdk/pydantic/sign_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_requests/{sign_request_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_requests.list`<a id="boxsign_requestslist"></a>

Gets sign requests created by a user. If the `sign_files` and/or
`parent_folder` are deleted, the sign request will not return in the list.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = box.sign_requests.list(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`SignRequests`](./box_python_sdk/pydantic/sign_requests.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_requests.resend_sign_request_emails`<a id="boxsign_requestsresend_sign_request_emails"></a>

Resends a sign request email to all outstanding signers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.sign_requests.resend_sign_request_emails(
    sign_request_id="33243242",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sign_request_id: `str`<a id="sign_request_id-str"></a>

The ID of the sign request

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_requests/{sign_request_id}/resend` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_templates.get_details`<a id="boxsign_templatesget_details"></a>

Fetches details of a specific Box Sign template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = box.sign_templates.get_details(
    template_id="123075213-7d117509-8f05-42e4-a5ef-5190a319d41d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

The ID of a Box Sign template.

#### 🔄 Return<a id="🔄-return"></a>

[`SignTemplate`](./box_python_sdk/pydantic/sign_template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_templates/{template_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.sign_templates.list_templates`<a id="boxsign_templateslist_templates"></a>

Gets Box Sign templates created by a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_templates_response = box.sign_templates.list_templates(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`SignTemplates`](./box_python_sdk/pydantic/sign_templates.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sign_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.skills.apply_box_skill_cards`<a id="boxskillsapply_box_skill_cards"></a>

Applies one or more Box Skills metadata cards to a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apply_box_skill_cards_response = box.skills.apply_box_skill_cards(
    cards=[
        None
    ],
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cards: [`SkillsApplyBoxSkillCardsRequestCards`](./box_python_sdk/type/skills_apply_box_skill_cards_request_cards.py)<a id="cards-skillsapplyboxskillcardsrequestcardsbox_python_sdktypeskills_apply_box_skill_cards_request_cardspy"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillsApplyBoxSkillCardsRequest`](./box_python_sdk/type/skills_apply_box_skill_cards_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SkillCardsMetadata`](./box_python_sdk/pydantic/skill_cards_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/global/boxSkillsCards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.skills.list_box_skill_cards`<a id="boxskillslist_box_skill_cards"></a>

List the Box Skills metadata cards that are attached to a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_box_skill_cards_response = box.skills.list_box_skill_cards(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🔄 Return<a id="🔄-return"></a>

[`SkillCardsMetadata`](./box_python_sdk/pydantic/skill_cards_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/global/boxSkillsCards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.skills.remove_box_skill_cards`<a id="boxskillsremove_box_skill_cards"></a>

Removes any Box Skills cards metadata from a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.skills.remove_box_skill_cards(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/global/boxSkillsCards` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.skills.update_all_box_skill_cards`<a id="boxskillsupdate_all_box_skill_cards"></a>

An alternative method that can be used to overwrite and update all Box Skill
metadata cards on a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.skills.update_all_box_skill_cards(
    status="success",
    metadata={
    },
    file={
        "type": "file",
        "id": "3243244",
    },
    skill_id="33243242",
    file_version={
        "type": "file_version",
        "id": "731381601045",
    },
    usage={
        "unit": "file",
        "value": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Defines the status of this invocation. Set this to `success` when setting Skill cards.

##### metadata: [`SkillsUpdateAllBoxSkillCardsRequestMetadata`](./box_python_sdk/type/skills_update_all_box_skill_cards_request_metadata.py)<a id="metadata-skillsupdateallboxskillcardsrequestmetadatabox_python_sdktypeskills_update_all_box_skill_cards_request_metadatapy"></a>


##### file: [`SkillsUpdateAllBoxSkillCardsRequestFile`](./box_python_sdk/type/skills_update_all_box_skill_cards_request_file.py)<a id="file-skillsupdateallboxskillcardsrequestfilebox_python_sdktypeskills_update_all_box_skill_cards_request_filepy"></a>


##### skill_id: `str`<a id="skill_id-str"></a>

The ID of the skill to apply this metadata for.

##### file_version: [`SkillsUpdateAllBoxSkillCardsRequestFileVersion`](./box_python_sdk/type/skills_update_all_box_skill_cards_request_file_version.py)<a id="file_version-skillsupdateallboxskillcardsrequestfileversionbox_python_sdktypeskills_update_all_box_skill_cards_request_file_versionpy"></a>


##### usage: [`SkillsUpdateAllBoxSkillCardsRequestUsage`](./box_python_sdk/type/skills_update_all_box_skill_cards_request_usage.py)<a id="usage-skillsupdateallboxskillcardsrequestusagebox_python_sdktypeskills_update_all_box_skill_cards_request_usagepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SkillsUpdateAllBoxSkillCardsRequest`](./box_python_sdk/type/skills_update_all_box_skill_cards_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skill_invocations/{skill_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.skills.update_box_skill_cards_on_file`<a id="boxskillsupdate_box_skill_cards_on_file"></a>

Updates one or more Box Skills metadata cards to a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_box_skill_cards_on_file_response = box.skills.update_box_skill_cards_on_file(
    body=[
        {
            "op": "replace",
            "path": "/cards/0",
        }
    ],
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### requestBody: [`SkillsUpdateBoxSkillCardsOnFileRequest`](./box_python_sdk/type/skills_update_box_skill_cards_on_file_request.py)<a id="requestbody-skillsupdateboxskillcardsonfilerequestbox_python_sdktypeskills_update_box_skill_cards_on_file_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SkillCardsMetadata`](./box_python_sdk/pydantic/skill_cards_metadata.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/metadata/global/boxSkillsCards` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policies.get_specific`<a id="boxstandard_and_zones_storage_policiesget_specific"></a>

Fetches a specific storage policy.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_response = box.standard_and_zones_storage_policies.get_specific(
    storage_policy_id="34342",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### storage_policy_id: `str`<a id="storage_policy_id-str"></a>

The ID of the storage policy.

#### 🔄 Return<a id="🔄-return"></a>

[`StoragePolicy`](./box_python_sdk/pydantic/storage_policy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policies/{storage_policy_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policies.list_policies`<a id="boxstandard_and_zones_storage_policieslist_policies"></a>

Fetches all the storage policies in the enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_policies_response = box.standard_and_zones_storage_policies.list_policies(
    fields=["id", "type", "name"],
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`StoragePolicies`](./box_python_sdk/pydantic/storage_policies.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policy_assignments.create_assignment`<a id="boxstandard_and_zones_storage_policy_assignmentscreate_assignment"></a>

Creates a storage policy assignment for an enterprise or user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_assignment_response = box.standard_and_zones_storage_policy_assignments.create_assignment(
    storage_policy={
        "type": "storage_policy",
        "id": "1434325",
    },
    assigned_to={
        "type": "user",
        "id": "9987987",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### storage_policy: [`StandardAndZonesStoragePolicyAssignmentsCreateAssignmentRequestStoragePolicy`](./box_python_sdk/type/standard_and_zones_storage_policy_assignments_create_assignment_request_storage_policy.py)<a id="storage_policy-standardandzonesstoragepolicyassignmentscreateassignmentrequeststoragepolicybox_python_sdktypestandard_and_zones_storage_policy_assignments_create_assignment_request_storage_policypy"></a>


##### assigned_to: [`StandardAndZonesStoragePolicyAssignmentsCreateAssignmentRequestAssignedTo`](./box_python_sdk/type/standard_and_zones_storage_policy_assignments_create_assignment_request_assigned_to.py)<a id="assigned_to-standardandzonesstoragepolicyassignmentscreateassignmentrequestassignedtobox_python_sdktypestandard_and_zones_storage_policy_assignments_create_assignment_request_assigned_topy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StandardAndZonesStoragePolicyAssignmentsCreateAssignmentRequest`](./box_python_sdk/type/standard_and_zones_storage_policy_assignments_create_assignment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`StoragePolicyAssignment`](./box_python_sdk/pydantic/storage_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policy_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policy_assignments.get_specific_assignment`<a id="boxstandard_and_zones_storage_policy_assignmentsget_specific_assignment"></a>

Fetches a specific storage policy assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_assignment_response = box.standard_and_zones_storage_policy_assignments.get_specific_assignment(
    storage_policy_assignment_id="932483",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### storage_policy_assignment_id: `str`<a id="storage_policy_assignment_id-str"></a>

The ID of the storage policy assignment.

#### 🔄 Return<a id="🔄-return"></a>

[`StoragePolicyAssignment`](./box_python_sdk/pydantic/storage_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policy_assignments/{storage_policy_assignment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policy_assignments.list_assignments`<a id="boxstandard_and_zones_storage_policy_assignmentslist_assignments"></a>

Fetches all the storage policy assignment for an enterprise or user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assignments_response = box.standard_and_zones_storage_policy_assignments.list_assignments(
    resolved_for_type="user",
    resolved_for_id="984322",
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resolved_for_type: `str`<a id="resolved_for_type-str"></a>

The target type to return assignments for

##### resolved_for_id: `str`<a id="resolved_for_id-str"></a>

The ID of the user or enterprise to return assignments for

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`StoragePolicyAssignments`](./box_python_sdk/pydantic/storage_policy_assignments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policy_assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policy_assignments.unassign_storage_policy`<a id="boxstandard_and_zones_storage_policy_assignmentsunassign_storage_policy"></a>

Delete a storage policy assignment.

Deleting a storage policy assignment on a user
will have the user inherit the enterprise's default
storage policy.

There is a rate limit for calling this endpoint of only
twice per user in a 24 hour time frame.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.standard_and_zones_storage_policy_assignments.unassign_storage_policy(
    storage_policy_assignment_id="932483",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### storage_policy_assignment_id: `str`<a id="storage_policy_assignment_id-str"></a>

The ID of the storage policy assignment.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policy_assignments/{storage_policy_assignment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.standard_and_zones_storage_policy_assignments.update_specific_assignment`<a id="boxstandard_and_zones_storage_policy_assignmentsupdate_specific_assignment"></a>

Updates a specific storage policy assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_specific_assignment_response = box.standard_and_zones_storage_policy_assignments.update_specific_assignment(
    storage_policy={
        "type": "storage_policy",
        "id": "1434325",
    },
    storage_policy_assignment_id="932483",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### storage_policy: [`StandardAndZonesStoragePolicyAssignmentsUpdateSpecificAssignmentRequestStoragePolicy`](./box_python_sdk/type/standard_and_zones_storage_policy_assignments_update_specific_assignment_request_storage_policy.py)<a id="storage_policy-standardandzonesstoragepolicyassignmentsupdatespecificassignmentrequeststoragepolicybox_python_sdktypestandard_and_zones_storage_policy_assignments_update_specific_assignment_request_storage_policypy"></a>


##### storage_policy_assignment_id: `str`<a id="storage_policy_assignment_id-str"></a>

The ID of the storage policy assignment.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StandardAndZonesStoragePolicyAssignmentsUpdateSpecificAssignmentRequest`](./box_python_sdk/type/standard_and_zones_storage_policy_assignments_update_specific_assignment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`StoragePolicyAssignment`](./box_python_sdk/pydantic/storage_policy_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/storage_policy_assignments/{storage_policy_assignment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.task_assignments.assign_multiple_users`<a id="boxtask_assignmentsassign_multiple_users"></a>

Assigns a task to a user.

A task can be assigned to more than one user by creating multiple
assignments.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_multiple_users_response = box.task_assignments.assign_multiple_users(
    task={
        "id": "11446498",
        "type": "task",
    },
    assign_to={
        "id": "3242343",
        "login": "john@example.com",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task: [`TaskAssignmentsAssignMultipleUsersRequestTask`](./box_python_sdk/type/task_assignments_assign_multiple_users_request_task.py)<a id="task-taskassignmentsassignmultipleusersrequesttaskbox_python_sdktypetask_assignments_assign_multiple_users_request_taskpy"></a>


##### assign_to: [`TaskAssignmentsAssignMultipleUsersRequestAssignTo`](./box_python_sdk/type/task_assignments_assign_multiple_users_request_assign_to.py)<a id="assign_to-taskassignmentsassignmultipleusersrequestassigntobox_python_sdktypetask_assignments_assign_multiple_users_request_assign_topy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskAssignmentsAssignMultipleUsersRequest`](./box_python_sdk/type/task_assignments_assign_multiple_users_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskAssignment`](./box_python_sdk/pydantic/task_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.task_assignments.delete_specific_assignment`<a id="boxtask_assignmentsdelete_specific_assignment"></a>

Deletes a specific task assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.task_assignments.delete_specific_assignment(
    task_assignment_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_assignment_id: `str`<a id="task_assignment_id-str"></a>

The ID of the task assignment.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_assignments/{task_assignment_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.task_assignments.get_task_assignment_info`<a id="boxtask_assignmentsget_task_assignment_info"></a>

Retrieves information about a task assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_assignment_info_response = box.task_assignments.get_task_assignment_info(
    task_assignment_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_assignment_id: `str`<a id="task_assignment_id-str"></a>

The ID of the task assignment.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskAssignment`](./box_python_sdk/pydantic/task_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_assignments/{task_assignment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.task_assignments.list_for_task`<a id="boxtask_assignmentslist_for_task"></a>

Lists all of the assignments for a given task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_task_response = box.task_assignments.list_for_task(
    task_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

The ID of the task.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskAssignments`](./box_python_sdk/pydantic/task_assignments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_id}/assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.task_assignments.update_state_assigned_to_user`<a id="boxtask_assignmentsupdate_state_assigned_to_user"></a>

Updates a task assignment. This endpoint can be
used to update the state of a task assigned to a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_state_assigned_to_user_response = box.task_assignments.update_state_assigned_to_user(
    task_assignment_id="12345",
    message="Looks good to me",
    resolution_state="completed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_assignment_id: `str`<a id="task_assignment_id-str"></a>

The ID of the task assignment.

##### message: `str`<a id="message-str"></a>

An optional message by the assignee that can be added to the task.

##### resolution_state: `str`<a id="resolution_state-str"></a>

The state of the task assigned to the user.  * For a task with an `action` value of `complete` this can be `incomplete` or `completed`. * For a task with an `action` of `review` this can be `incomplete`, `approved`, or `rejected`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskAssignmentsUpdateStateAssignedToUserRequest`](./box_python_sdk/type/task_assignments_update_state_assigned_to_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskAssignment`](./box_python_sdk/pydantic/task_assignment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/task_assignments/{task_assignment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.tasks.get_info`<a id="boxtasksget_info"></a>

Retrieves information about a specific task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = box.tasks.get_info(
    task_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

The ID of the task.

#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./box_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.tasks.list_on_file`<a id="boxtaskslist_on_file"></a>

Retrieves a list of all the tasks for a file. This
endpoint does not support pagination.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_on_file_response = box.tasks.list_on_file(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🔄 Return<a id="🔄-return"></a>

[`Tasks`](./box_python_sdk/pydantic/tasks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.tasks.remove_file`<a id="boxtasksremove_file"></a>

Removes a task from a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.tasks.remove_file(
    task_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

The ID of the task.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.tasks.tasks`<a id="boxtaskstasks"></a>

Creates a single task on a file. This task is not assigned to any user and
will need to be assigned separately.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tasks_response = box.tasks.tasks(
    item={
        "id": "11446498",
        "type": "file",
    },
    action="review",
    message="Please review",
    due_at="2012-12-12T10:53:43-08:00",
    completion_rule="all_assignees",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### item: [`PostTasksRequestItem`](./box_python_sdk/type/post_tasks_request_item.py)<a id="item-posttasksrequestitembox_python_sdktypepost_tasks_request_itempy"></a>


##### action: `str`<a id="action-str"></a>

The action the task assignee will be prompted to do. Must be  * `review` defines an approval task that can be approved or rejected * `complete` defines a general task which can be completed

##### message: `str`<a id="message-str"></a>

An optional message to include with the task.

##### due_at: `datetime`<a id="due_at-datetime"></a>

Defines when the task is due. Defaults to `null` if not provided.

##### completion_rule: `str`<a id="completion_rule-str"></a>

Defines which assignees need to complete this task before the task is considered completed.  * `all_assignees` (default) requires all assignees to review or approve the the task in order for it to be considered completed. * `any_assignee` accepts any one assignee to review or approve the the task in order for it to be considered completed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostTasksRequest`](./box_python_sdk/type/post_tasks_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./box_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.tasks.update_task_configuration`<a id="boxtasksupdate_task_configuration"></a>

Updates a task. This can be used to update a task's configuration, or to
update its completion state.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_task_configuration_response = box.tasks.update_task_configuration(
    task_id="12345",
    action="review",
    message="Please review",
    due_at="2012-12-12T10:53:43-08:00",
    completion_rule="all_assignees",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task_id: `str`<a id="task_id-str"></a>

The ID of the task.

##### action: `str`<a id="action-str"></a>

The action the task assignee will be prompted to do. Must be  * `review` defines an approval task that can be approved or rejected * `complete` defines a general task which can be completed

##### message: `str`<a id="message-str"></a>

The message included with the task.

##### due_at: `datetime`<a id="due_at-datetime"></a>

When the task is due at.

##### completion_rule: `str`<a id="completion_rule-str"></a>

Defines which assignees need to complete this task before the task is considered completed.  * `all_assignees` (default) requires all assignees to review or approve the the task in order for it to be considered completed. * `any_assignee` accepts any one assignee to review or approve the the task in order for it to be considered completed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TasksUpdateTaskConfigurationRequest`](./box_python_sdk/type/tasks_update_task_configuration_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Task`](./box_python_sdk/pydantic/task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tasks/{task_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service.create_for_enterprise_and_type`<a id="boxterms_of_servicecreate_for_enterprise_and_type"></a>

Creates a terms of service for a given enterprise
and type of user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_for_enterprise_and_type_response = box.terms_of_service.create_for_enterprise_and_type(
    status="enabled",
    text="By collaborating on this file you are accepting...",
    tos_type="managed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Whether this terms of service is active.

##### text: `str`<a id="text-str"></a>

The terms of service text to display to users.  The text can be set to empty if the `status` is set to `disabled`.

##### tos_type: `str`<a id="tos_type-str"></a>

The type of user to set the terms of service for.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TermsOfServiceCreateForEnterpriseAndTypeRequest`](./box_python_sdk/type/terms_of_service_create_for_enterprise_and_type_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfService`](./box_python_sdk/pydantic/terms_of_service.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_services` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service.get_settings`<a id="boxterms_of_serviceget_settings"></a>

Returns the current terms of service text and settings
for the enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = box.terms_of_service.get_settings(
    tos_type="managed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tos_type: `str`<a id="tos_type-str"></a>

Limits the results to the terms of service of the given type.

#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfServices`](./box_python_sdk/pydantic/terms_of_services.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_services` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service.get_specific`<a id="boxterms_of_serviceget_specific"></a>

Fetches a specific terms of service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_response = box.terms_of_service.get_specific(
    terms_of_service_id="324234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### terms_of_service_id: `str`<a id="terms_of_service_id-str"></a>

The ID of the terms of service.

#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfService`](./box_python_sdk/pydantic/terms_of_service.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_services/{terms_of_service_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service.update_specific_term`<a id="boxterms_of_serviceupdate_specific_term"></a>

Updates a specific terms of service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_specific_term_response = box.terms_of_service.update_specific_term(
    status="enabled",
    text="By collaborating on this file you are accepting...",
    terms_of_service_id="324234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Whether this terms of service is active.

##### text: `str`<a id="text-str"></a>

The terms of service text to display to users.  The text can be set to empty if the `status` is set to `disabled`.

##### terms_of_service_id: `str`<a id="terms_of_service_id-str"></a>

The ID of the terms of service.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TermsOfServiceUpdateSpecificTermRequest`](./box_python_sdk/type/terms_of_service_update_specific_term_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfService`](./box_python_sdk/pydantic/terms_of_service.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_services/{terms_of_service_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service_user_statuses.create_user_status`<a id="boxterms_of_service_user_statusescreate_user_status"></a>

Sets the status for a terms of service for a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_user_status_response = box.terms_of_service_user_statuses.create_user_status(
    tos={
        "type": "terms_of_service",
        "id": "1232132",
    },
    user={
        "type": "user",
        "id": "3423423",
    },
    is_accepted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tos: [`TermsOfServiceUserStatusesCreateUserStatusRequestTos`](./box_python_sdk/type/terms_of_service_user_statuses_create_user_status_request_tos.py)<a id="tos-termsofserviceuserstatusescreateuserstatusrequesttosbox_python_sdktypeterms_of_service_user_statuses_create_user_status_request_tospy"></a>


##### user: [`TermsOfServiceUserStatusesCreateUserStatusRequestUser`](./box_python_sdk/type/terms_of_service_user_statuses_create_user_status_request_user.py)<a id="user-termsofserviceuserstatusescreateuserstatusrequestuserbox_python_sdktypeterms_of_service_user_statuses_create_user_status_request_userpy"></a>


##### is_accepted: `bool`<a id="is_accepted-bool"></a>

Whether the user has accepted the terms.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TermsOfServiceUserStatusesCreateUserStatusRequest`](./box_python_sdk/type/terms_of_service_user_statuses_create_user_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfServiceUserStatus`](./box_python_sdk/pydantic/terms_of_service_user_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_service_user_statuses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service_user_statuses.list_user_statuses`<a id="boxterms_of_service_user_statuseslist_user_statuses"></a>

Retrieves an overview of users and their status for a
terms of service, including Whether they have accepted
the terms and when.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_statuses_response = box.terms_of_service_user_statuses.list_user_statuses(
    tos_id="324234",
    user_id="123334",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tos_id: `str`<a id="tos_id-str"></a>

The ID of the terms of service.

##### user_id: `str`<a id="user_id-str"></a>

Limits results to the given user ID.

#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfServiceUserStatuses`](./box_python_sdk/pydantic/terms_of_service_user_statuses.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_service_user_statuses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.terms_of_service_user_statuses.update_user_status`<a id="boxterms_of_service_user_statusesupdate_user_status"></a>

Updates the status for a terms of service for a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_status_response = box.terms_of_service_user_statuses.update_user_status(
    is_accepted=True,
    terms_of_service_user_status_id="324234",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### is_accepted: `bool`<a id="is_accepted-bool"></a>

Whether the user has accepted the terms.

##### terms_of_service_user_status_id: `str`<a id="terms_of_service_user_status_id-str"></a>

The ID of the terms of service status.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TermsOfServiceUserStatusesUpdateUserStatusRequest`](./box_python_sdk/type/terms_of_service_user_statuses_update_user_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TermsOfServiceUserStatus`](./box_python_sdk/pydantic/terms_of_service_user_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms_of_service_user_statuses/{terms_of_service_user_status_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.transfer_folders.to_destination`<a id="boxtransfer_foldersto_destination"></a>

Move all of the items (files, folders and workflows) owned by a user into
another user's account

Only the root folder (`0`) can be transferred.

Folders can only be moved across users by users with administrative
permissions.

All existing shared links and folder-level collaborations are transferred
during the operation. Please note that while collaborations at the individual
file-level are transferred during the operation, the collaborations are
deleted when the original user is deleted.

This call will be performed synchronously which might lead to a slow response
when the source user has a large number of items in all of its folders.

If the destination path has a metadata cascade policy attached to any of
the parent folders, a metadata cascade operation will be kicked off
asynchronously.

There is currently no way to check for when this operation is finished.

The destination folder's name will be in the format `{User}'s Files and
Folders`, where `{User}` is the display name of the user.

To make this API call your application will need to have the "Read and write
all files and folders stored in Box" scope enabled.

Please make sure the destination user has access to `Relay` or `Relay Lite`,
and has access to the files and folders involved in the workflows being
transferred.

Admins will receive an email when the operation is completed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
to_destination_response = box.transfer_folders.to_destination(
    owned_by={
        "id": "1232234",
    },
    user_id="12345",
    fields=["id", "type", "name"],
    notify=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owned_by: [`TransferFoldersToDestinationRequestOwnedBy`](./box_python_sdk/type/transfer_folders_to_destination_request_owned_by.py)<a id="owned_by-transferfolderstodestinationrequestownedbybox_python_sdktypetransfer_folders_to_destination_request_owned_bypy"></a>


##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### notify: `bool`<a id="notify-bool"></a>

Determines if users should receive email notification for the action performed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransferFoldersToDestinationRequest`](./box_python_sdk/type/transfer_folders_to_destination_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FolderFull`](./box_python_sdk/pydantic/folder_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/folders/0` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_files.get_file`<a id="boxtrashed_filesget_file"></a>

Retrieves a file that has been moved to the trash.

Please note that only if the file itself has been moved to the
trash can it be retrieved with this API call. If instead one of
its parent folders was moved to the trash, only that folder
can be inspected using the
[`GET /folders/:id/trash`](e://get_folders_id_trash) API.

To list all items that have been moved to the trash, please
use the [`GET /folders/trash/items`](e://get-folders-trash-items/)
API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_response = box.trashed_files.get_file(
    file_id="12345",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`TrashFile`](./box_python_sdk/pydantic/trash_file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/trash` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_files.permanently_remove_file`<a id="boxtrashed_filespermanently_remove_file"></a>

Permanently deletes a file that is in the trash.
This action cannot be undone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.trashed_files.permanently_remove_file(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/trash` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_files.restore_file`<a id="boxtrashed_filesrestore_file"></a>

Restores a file that has been moved to the trash.

An optional new parent ID can be provided to restore the file to in case the
original folder has been deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
restore_file_response = box.trashed_files.restore_file(
    file_id="12345",
    name="Restored.docx",
    parent=None,
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### name: `str`<a id="name-str"></a>

An optional new name for the file.

##### parent: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrashedFilesRestoreFileRequest`](./box_python_sdk/type/trashed_files_restore_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TrashFileRestored`](./box_python_sdk/pydantic/trash_file_restored.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_folders.getd_folder`<a id="boxtrashed_foldersgetd_folder"></a>

Retrieves a folder that has been moved to the trash.

Please note that only if the folder itself has been moved to the
trash can it be retrieved with this API call. If instead one of
its parent folders was moved to the trash, only that folder
can be inspected using the
[`GET /folders/:id/trash`](e://get_folders_id_trash) API.

To list all items that have been moved to the trash, please
use the [`GET /folders/trash/items`](e://get-folders-trash-items/)
API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
getd_folder_response = box.trashed_folders.getd_folder(
    folder_id="12345",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`TrashFolder`](./box_python_sdk/pydantic/trash_folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/trash` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_folders.permanently_remove_folder`<a id="boxtrashed_folderspermanently_remove_folder"></a>

Permanently deletes a folder that is in the trash.
This action cannot be undone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.trashed_folders.permanently_remove_folder(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/trash` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_folders.restore_folder`<a id="boxtrashed_foldersrestore_folder"></a>

Restores a folder that has been moved to the trash.

An optional new parent ID can be provided to restore the folder to in case the
original folder has been deleted.

# Folder locking<a id="folder-locking"></a>

During this operation, part of the file tree will be locked, mainly
the source folder and all of its descendants, as well as the destination
folder.

For the duration of the operation, no other move, copy, delete, or restore
operation can performed on any of the locked folders.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
restore_folder_response = box.trashed_folders.restore_folder(
    folder_id="12345",
    name="Restored Photos",
    parent=None,
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### name: `str`<a id="name-str"></a>

An optional new name for the folder.

##### parent: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrashedFoldersRestoreFolderRequest`](./box_python_sdk/type/trashed_folders_restore_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TrashFolderRestored`](./box_python_sdk/pydantic/trash_folder_restored.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_items.list_retrieved_items`<a id="boxtrashed_itemslist_retrieved_items"></a>

Retrieves the files and folders that have been moved
to the trash.

Any attribute in the full files or folders objects can be passed
in with the `fields` parameter to retrieve those specific
attributes that are not returned by default.

This endpoint defaults to use offset-based pagination, yet also supports
marker-based pagination using the `marker` parameter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_retrieved_items_response = box.trashed_items.list_retrieved_items(
    fields=["id", "type", "name"],
    limit=1000,
    offset=1000,
    usemarker=True,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    direction="ASC",
    sort="name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### usemarker: `bool`<a id="usemarker-bool"></a>

Specifies whether to use marker-based pagination instead of offset-based pagination. Only one pagination method can be used at a time.  By setting this value to true, the API will return a `marker` field that can be passed as a parameter to this endpoint to get the next page of the response.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### direction: `str`<a id="direction-str"></a>

The direction to sort results in. This can be either in alphabetical ascending (`ASC`) or descending (`DESC`) order.

##### sort: `str`<a id="sort-str"></a>

Defines the **second** attribute by which items are sorted.  Items are always sorted by their `type` first, with folders listed before files, and files listed before web links.  This parameter is not supported when using marker-based pagination.

#### 🔄 Return<a id="🔄-return"></a>

[`Items`](./box_python_sdk/pydantic/items.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/trash/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_web_links.get_trashed_link`<a id="boxtrashed_web_linksget_trashed_link"></a>

Retrieves a web link that has been moved to the trash.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_trashed_link_response = box.trashed_web_links.get_trashed_link(
    web_link_id="12345",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`TrashWebLink`](./box_python_sdk/pydantic/trash_web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}/trash` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_web_links.permanently_remove`<a id="boxtrashed_web_linkspermanently_remove"></a>

Permanently deletes a web link that is in the trash.
This action cannot be undone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.trashed_web_links.permanently_remove(
    web_link_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}/trash` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.trashed_web_links.restore_web_link`<a id="boxtrashed_web_linksrestore_web_link"></a>

Restores a web link that has been moved to the trash.

An optional new parent ID can be provided to restore the  web link to in case
the original folder has been deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
restore_web_link_response = box.trashed_web_links.restore_web_link(
    web_link_id="12345",
    name="Restored.docx",
    parent=None,
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### name: `str`<a id="name-str"></a>

An optional new name for the web link.

##### parent: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrashedWebLinksRestoreWebLinkRequest`](./box_python_sdk/type/trashed_web_links_restore_web_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TrashWebLinkRestored`](./box_python_sdk/pydantic/trash_web_link_restored.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads.file_content_update`<a id="boxuploadsfile_content_update"></a>

Update a file's content. For file sizes over 50MB we recommend
using the Chunk Upload APIs.

# Request body order<a id="request-body-order"></a>

The `attributes` part of the body must come **before** the
`file` part. Requests that do not follow this format when
uploading the file will receive a HTTP `400` error with a
`metadata_after_file_contents` error code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_content_update_response = box.uploads.file_content_update(
    file_id="12345",
    attributes={
        "name": "Photo 2.0.png",
        "content_modified_at": "2012-12-12T10:53:43-08:00",
    },
    file=open('/path/to/file', 'rb'),
    if_match="1",
    fields=["id", "type", "name"],
    content_md5="134b65991ed521fcfe4724b7d814ab8ded5185dc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### attributes: [`UploadsFileContentUpdateRequestAttributes`](./box_python_sdk/type/uploads_file_content_update_request_attributes.py)<a id="attributes-uploadsfilecontentupdaterequestattributesbox_python_sdktypeuploads_file_content_update_request_attributespy"></a>


##### file: `IO`<a id="file-io"></a>

The content of the file to upload to Box.  <Message warning>    The `attributes` part of the body must come **before** the   `file` part. Requests that do not follow this format when   uploading the file will receive a HTTP `400` error with a   `metadata_after_file_contents` error code.  </Message>

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### content_md5: `str`<a id="content_md5-str"></a>

An optional header containing the SHA1 hash of the file to ensure that the file was not corrupted in transit.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsFileContentUpdateRequest`](./box_python_sdk/type/uploads_file_content_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Files`](./box_python_sdk/pydantic/files.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/content` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads.small_file`<a id="boxuploadssmall_file"></a>

Uploads a small file to Box. For file sizes over 50MB we recommend
using the Chunk Upload APIs.

# Request body order<a id="request-body-order"></a>

The `attributes` part of the body must come **before** the
`file` part. Requests that do not follow this format when
uploading the file will receive a HTTP `400` error with a
`metadata_after_file_contents` error code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
small_file_response = box.uploads.small_file(
    attributes={
        "name": "Photo.png",
        "parent": {
            "id": "124132",
        },
        "content_created_at": "2012-12-12T10:53:43-08:00",
        "content_modified_at": "2012-12-12T10:53:43-08:00",
    },
    file=open('/path/to/file', 'rb'),
    fields=["id", "type", "name"],
    content_md5="134b65991ed521fcfe4724b7d814ab8ded5185dc",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### attributes: [`UploadsSmallFileRequestAttributes`](./box_python_sdk/type/uploads_small_file_request_attributes.py)<a id="attributes-uploadssmallfilerequestattributesbox_python_sdktypeuploads_small_file_request_attributespy"></a>


##### file: `IO`<a id="file-io"></a>

The content of the file to upload to Box.  <Message warning>    The `attributes` part of the body must come **before** the   `file` part. Requests that do not follow this format when   uploading the file will receive a HTTP `400` error with a   `metadata_after_file_contents` error code.  </Message>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### content_md5: `str`<a id="content_md5-str"></a>

An optional header containing the SHA1 hash of the file to ensure that the file was not corrupted in transit.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsSmallFileRequest`](./box_python_sdk/type/uploads_small_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Files`](./box_python_sdk/pydantic/files.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/content` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).commit_session`<a id="boxuploads_chunkedcommit_session"></a>

Close an upload session and create a file from the
uploaded chunks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
commit_session_response = box.uploads_(chunked).commit_session(
    parts=[
        {}
    ],
    upload_session_id="D5E3F7A",
    digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
    if_match="1",
    if_none_match="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parts: List[`UploadPart`]<a id="parts-listuploadpart"></a>

The list details for the uploaded parts

##### upload_session_id: `str`<a id="upload_session_id-str"></a>

The ID of the upload session.

##### digest: `str`<a id="digest-str"></a>

The [RFC3230][1] message digest of the whole file.  Only SHA1 is supported. The SHA1 digest must be Base64 encoded. The format of this header is as `sha=BASE64_ENCODED_DIGEST`.  [1]: https://tools.ietf.org/html/rfc3230

##### if_match: `str`<a id="if_match-str"></a>

Ensures this item hasn't recently changed before making changes.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `412 Precondition Failed` if it has changed since.

##### if_none_match: `str`<a id="if_none_match-str"></a>

Ensures an item is only returned if it has changed.  Pass in the item's last observed `etag` value into this header and the endpoint will fail with a `304 Not Modified` if the item has not changed since.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsChunkedCommitSessionRequest`](./box_python_sdk/type/uploads_chunked_commit_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Files`](./box_python_sdk/pydantic/files.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/upload_sessions/{upload_session_id}/commit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).create_session_for_upload`<a id="boxuploads_chunkedcreate_session_for_upload"></a>

Creates an upload session for a new file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_for_upload_response = box.uploads_(chunked).create_session_for_upload(
    folder_id="0",
    file_size=104857600,
    file_name="Project.mov",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The ID of the folder to upload the new file to.

##### file_size: `int`<a id="file_size-int"></a>

The total number of bytes of the file to be uploaded

##### file_name: `str`<a id="file_name-str"></a>

The name of new file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsChunkedCreateSessionForUploadRequest`](./box_python_sdk/type/uploads_chunked_create_session_for_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadSession`](./box_python_sdk/pydantic/upload_session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/upload_sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).create_session_for_upload_0`<a id="boxuploads_chunkedcreate_session_for_upload_0"></a>

Creates an upload session for an existing file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_for_upload_0_response = box.uploads_(chunked).create_session_for_upload_0(
    file_size=104857600,
    file_id="12345",
    file_name="Project.mov",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_size: `int`<a id="file_size-int"></a>

The total number of bytes of the file to be uploaded

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

##### file_name: `str`<a id="file_name-str"></a>

The optional new name of new file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsChunkedCreateSessionForUploadRequest1`](./box_python_sdk/type/uploads_chunked_create_session_for_upload_request1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadSession`](./box_python_sdk/pydantic/upload_session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/upload_sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).file_part_update`<a id="boxuploads_chunkedfile_part_update"></a>

Updates a chunk of an upload session for a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_part_update_response = box.uploads_(chunked).file_part_update(
    body=open('/path/to/file', 'rb'),
    upload_session_id="D5E3F7A",
    digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
    content_range="bytes 8388608-16777215/445856194",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_session_id: `str`<a id="upload_session_id-str"></a>

The ID of the upload session.

##### digest: `str`<a id="digest-str"></a>

The [RFC3230][1] message digest of the chunk uploaded.  Only SHA1 is supported. The SHA1 digest must be base64 encoded. The format of this header is as `sha=BASE64_ENCODED_DIGEST`.  To get the value for the `SHA` digest, use the openSSL command to encode the file part: `openssl sha1 -binary <FILE_PART_NAME> | base64`  [1]: https://tools.ietf.org/html/rfc3230

##### content_range: `str`<a id="content_range-str"></a>

The byte range of the chunk.  Must not overlap with the range of a part already uploaded this session. Each part’s size must be exactly equal in size to the part size specified in the upload session that you created. One exception is the last part of the file, as this can be smaller.  When providing the value for `content-range`, remember that:  * The lower bound of each part's byte range   must be a multiple of the part size. * The higher bound must be a multiple of the part size - 1.

##### requestBody: `IO`<a id="requestbody-io"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UploadedPart`](./box_python_sdk/pydantic/uploaded_part.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/upload_sessions/{upload_session_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).info`<a id="boxuploads_chunkedinfo"></a>

Return information about an upload session.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
info_response = box.uploads_(chunked).info(
    upload_session_id="D5E3F7A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_session_id: `str`<a id="upload_session_id-str"></a>

The ID of the upload session.

#### 🔄 Return<a id="🔄-return"></a>

[`UploadSession`](./box_python_sdk/pydantic/upload_session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/upload_sessions/{upload_session_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).list_parts`<a id="boxuploads_chunkedlist_parts"></a>

Return a list of the chunks uploaded to the upload
session so far.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_parts_response = box.uploads_(chunked).list_parts(
    upload_session_id="D5E3F7A",
    offset=1000,
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_session_id: `str`<a id="upload_session_id-str"></a>

The ID of the upload session.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`UploadParts`](./box_python_sdk/pydantic/upload_parts.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/upload_sessions/{upload_session_id}/parts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.uploads_(chunked).remove_upload_session`<a id="boxuploads_chunkedremove_upload_session"></a>

Abort an upload session and discard all data uploaded.

This cannot be reversed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.uploads_(chunked).remove_upload_session(
    upload_session_id="D5E3F7A",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_session_id: `str`<a id="upload_session_id-str"></a>

The ID of the upload session.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/upload_sessions/{upload_session_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.user_avatars.add_or_update_image`<a id="boxuser_avatarsadd_or_update_image"></a>

Adds or updates a user avatar.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_or_update_image_response = box.user_avatars.add_or_update_image(
    user_id="12345",
    pic=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### pic: `IO`<a id="pic-io"></a>

The image file to be uploaded to Box. Accepted file extensions are `.jpg` or `.png`. The maximum file size is 1MB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserAvatarsAddOrUpdateImageRequest`](./box_python_sdk/type/user_avatars_add_or_update_image_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserAvatar`](./box_python_sdk/pydantic/user_avatar.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/avatar` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.user_avatars.get_image`<a id="boxuser_avatarsget_image"></a>

Retrieves an image of a the user's avatar.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_image_response = box.user_avatars.get_image(
    user_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/avatar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.user_avatars.remove_existing`<a id="boxuser_avatarsremove_existing"></a>

Removes an existing user avatar.
You cannot reverse this operation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.user_avatars.remove_existing(
    user_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}/avatar` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.users.delete_user`<a id="boxusersdelete_user"></a>

Deletes a user. By default this will fail if the user
still owns any content. Move their owned content first
before proceeding, or use the `force` field to delete
the user and their files.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.users.delete_user(
    user_id="12345",
    notify=True,
    force=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### notify: `bool`<a id="notify-bool"></a>

Whether the user will receive email notification of the deletion

##### force: `bool`<a id="force-bool"></a>

Whether the user should be deleted even if this user still own files

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.users.get_current_user`<a id="boxusersget_current_user"></a>

Retrieves information about the user who is currently authenticated.

In the case of a client-side authenticated OAuth 2.0 application
this will be the user who authorized the app.

In the case of a JWT, server-side authenticated application
this will be the service account that belongs to the application
by default.

Use the `As-User` header to change who this API call is made on behalf of.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_user_response = box.users.get_current_user(
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`UserFull`](./box_python_sdk/pydantic/user_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.users.get_user_info`<a id="boxusersget_user_info"></a>

Retrieves information about a user in the enterprise.

The application and the authenticated user need to
have the permission to look up users in the entire
enterprise.

This endpoint also returns a limited set of information
for external users who are collaborated on content
owned by the enterprise for authenticated users with the
right scopes. In this case, disallowed fields will return
null instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_info_response = box.users.get_user_info(
    user_id="12345",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### 🔄 Return<a id="🔄-return"></a>

[`UserFull`](./box_python_sdk/pydantic/user_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.users.update_managed_user`<a id="boxusersupdate_managed_user"></a>

Updates a managed or app user in an enterprise. This endpoint
is only available to users and applications with the right
admin permissions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_managed_user_response = box.users.update_managed_user(
    user_id="12345",
    enterprise="string_example",
    notify=True,
    name="Aaron Levie",
    login="somename@box.com",
    role="user",
    language="en",
    is_sync_enabled=True,
    job_title="CEO",
    phone="6509241374",
    address="900 Jefferson Ave, Redwood City, CA 94063",
    tracking_codes=[
        {
            "type": "tracking_code",
            "name": "department",
            "value": "Sales",
        }
    ],
    can_see_managed_users=True,
    timezone="Africa/Bujumbura",
    is_external_collab_restricted=True,
    is_exempt_from_device_limits=True,
    is_exempt_from_login_verification=True,
    is_password_reset_required=True,
    status="active",
    space_amount=11345156112,
    notification_email={
        "email": "notifications@example.com",
    },
    external_app_user_id="my-user-1234",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The ID of the user.

##### enterprise: `Optional[str]`<a id="enterprise-optionalstr"></a>

Set this to `null` to roll the user out of the enterprise and make them a free user

##### notify: `bool`<a id="notify-bool"></a>

Whether the user should receive an email when they are rolled out of an enterprise

##### name: `str`<a id="name-str"></a>

The name of the user

##### login: `str`<a id="login-str"></a>

The email address the user uses to log in  Note: If the target user's email is not confirmed, then the primary login address cannot be changed.

##### role: `str`<a id="role-str"></a>

The user’s enterprise role

##### language: `str`<a id="language-str"></a>

The language of the user, formatted in modified version of the [ISO 639-1](https://raw.githubusercontent.com) format.

##### is_sync_enabled: `bool`<a id="is_sync_enabled-bool"></a>

Whether the user can use Box Sync

##### job_title: `str`<a id="job_title-str"></a>

The user’s job title

##### phone: `str`<a id="phone-str"></a>

The user’s phone number

##### address: `str`<a id="address-str"></a>

The user’s address

##### tracking_codes: List[`TrackingCode`]<a id="tracking_codes-listtrackingcode"></a>

Tracking codes allow an admin to generate reports from the admin console and assign an attribute to a specific group of users. This setting must be enabled for an enterprise before it can be used.

##### can_see_managed_users: `bool`<a id="can_see_managed_users-bool"></a>

Whether the user can see other enterprise users in their contact list

##### timezone: `str`<a id="timezone-str"></a>

The user's timezone

##### is_external_collab_restricted: `bool`<a id="is_external_collab_restricted-bool"></a>

Whether the user is allowed to collaborate with users outside their enterprise

##### is_exempt_from_device_limits: `bool`<a id="is_exempt_from_device_limits-bool"></a>

Whether to exempt the user from enterprise device limits

##### is_exempt_from_login_verification: `bool`<a id="is_exempt_from_login_verification-bool"></a>

Whether the user must use two-factor authentication

##### is_password_reset_required: `bool`<a id="is_password_reset_required-bool"></a>

Whether the user is required to reset their password

##### status: `str`<a id="status-str"></a>

The user's account status

##### space_amount: `int`<a id="space_amount-int"></a>

The user’s total available space in bytes. Set this to `-1` to indicate unlimited storage.

##### notification_email: [`UsersUpdateManagedUserRequestNotificationEmail`](./box_python_sdk/type/users_update_managed_user_request_notification_email.py)<a id="notification_email-usersupdatemanageduserrequestnotificationemailbox_python_sdktypeusers_update_managed_user_request_notification_emailpy"></a>


##### external_app_user_id: `str`<a id="external_app_user_id-str"></a>

An external identifier for an app user, which can be used to look up the user. This can be used to tie user IDs from external identity providers to Box users.  Note: In order to update this field, you need to request a token using the application that created the app user.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateManagedUserRequest`](./box_python_sdk/type/users_update_managed_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserFull`](./box_python_sdk/pydantic/user_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.users.users`<a id="boxusersusers"></a>

Returns a list of all users for the Enterprise along with their `user_id`,
`public_name`, and `login`.

The application and the authenticated user need to
have the permission to look up users in the entire
enterprise.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
users_response = box.users.users(
    filter_term="john",
    user_type="managed",
    external_app_user_id="my-user-1234",
    fields=["id", "type", "name"],
    offset=1000,
    limit=1000,
    usemarker=True,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter_term: `str`<a id="filter_term-str"></a>

Limits the results to only users who's `name` or `login` start with the search term.  For externally managed users, the search term needs to completely match the in order to find the user, and it will only return one user at a time.

##### user_type: `str`<a id="user_type-str"></a>

Limits the results to the kind of user specified.  * `all` returns every kind of user for whom the   `login` or `name` partially matches the   `filter_term`. It will only return an external user   if the login matches the `filter_term` completely,   and in that case it will only return that user. * `managed` returns all managed and app users for whom   the `login` or `name` partially matches the   `filter_term`. * `external` returns all external users for whom the   `login` matches the `filter_term` exactly.

##### external_app_user_id: `str`<a id="external_app_user_id-str"></a>

Limits the results to app users with the given `external_app_user_id` value.  When creating an app user, an `external_app_user_id` value can be set. This value can then be used in this endpoint to find any users that match that `external_app_user_id` value.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

##### offset: `int`<a id="offset-int"></a>

The offset of the item at which to begin the response.  Queries with offset parameter value exceeding 10000 will be rejected with a 400 response.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### usemarker: `bool`<a id="usemarker-bool"></a>

Specifies whether to use marker-based pagination instead of offset-based pagination. Only one pagination method can be used at a time.  By setting this value to true, the API will return a `marker` field that can be passed as a parameter to this endpoint to get the next page of the response.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./box_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.users.users_0`<a id="boxusersusers_0"></a>

Creates a new managed user in an enterprise. This endpoint
is only available to users and applications with the right
admin permissions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
users_0_response = box.users.users_0(
    name="Aaron Levie",
    login="boss@box.com",
    is_platform_access_only=True,
    role="user",
    language="en",
    is_sync_enabled=True,
    job_title="CEO",
    phone="6509241374",
    address="900 Jefferson Ave, Redwood City, CA 94063",
    space_amount=11345156112,
    tracking_codes=[
        {
            "type": "tracking_code",
            "name": "department",
            "value": "Sales",
        }
    ],
    can_see_managed_users=True,
    timezone="Africa/Bujumbura",
    is_external_collab_restricted=True,
    is_exempt_from_device_limits=True,
    is_exempt_from_login_verification=True,
    status="active",
    external_app_user_id="my-user-1234",
    fields=["id", "type", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the user

##### login: `str`<a id="login-str"></a>

The email address the user uses to log in  Required, unless `is_platform_access_only` is set to `true`.

##### is_platform_access_only: `bool`<a id="is_platform_access_only-bool"></a>

Specifies that the user is an app user.

##### role: `str`<a id="role-str"></a>

The user’s enterprise role

##### language: `str`<a id="language-str"></a>

The language of the user, formatted in modified version of the [ISO 639-1](https://raw.githubusercontent.com) format.

##### is_sync_enabled: `bool`<a id="is_sync_enabled-bool"></a>

Whether the user can use Box Sync

##### job_title: `str`<a id="job_title-str"></a>

The user’s job title

##### phone: `str`<a id="phone-str"></a>

The user’s phone number

##### address: `str`<a id="address-str"></a>

The user’s address

##### space_amount: `int`<a id="space_amount-int"></a>

The user’s total available space in bytes. Set this to `-1` to indicate unlimited storage.

##### tracking_codes: List[`TrackingCode`]<a id="tracking_codes-listtrackingcode"></a>

Tracking codes allow an admin to generate reports from the admin console and assign an attribute to a specific group of users. This setting must be enabled for an enterprise before it can be used.

##### can_see_managed_users: `bool`<a id="can_see_managed_users-bool"></a>

Whether the user can see other enterprise users in their contact list

##### timezone: `str`<a id="timezone-str"></a>

The user's timezone

##### is_external_collab_restricted: `bool`<a id="is_external_collab_restricted-bool"></a>

Whether the user is allowed to collaborate with users outside their enterprise

##### is_exempt_from_device_limits: `bool`<a id="is_exempt_from_device_limits-bool"></a>

Whether to exempt the user from enterprise device limits

##### is_exempt_from_login_verification: `bool`<a id="is_exempt_from_login_verification-bool"></a>

Whether the user must use two-factor authentication

##### status: `str`<a id="status-str"></a>

The user's account status

##### external_app_user_id: `str`<a id="external_app_user_id-str"></a>

An external identifier for an app user, which can be used to look up the user. This can be used to tie user IDs from external identity providers to Box users.

##### fields: List[`str`]<a id="fields-liststr"></a>

A comma-separated list of attributes to include in the response. This can be used to request fields that are not normally returned in a standard response.  Be aware that specifying this parameter will have the effect that none of the standard fields are returned in the response unless explicitly specified, instead only fields for the mini representation are returned, additional to the fields requested.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostUsersRequest`](./box_python_sdk/type/post_users_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserFull`](./box_python_sdk/pydantic/user_full.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.watermarks_(files).apply_watermark_to_file`<a id="boxwatermarks_filesapply_watermark_to_file"></a>

Applies or update a watermark on a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apply_watermark_to_file_response = box.watermarks_(files).apply_watermark_to_file(
    watermark={
        "imprint": "default",
    },
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### watermark: [`WatermarksFilesApplyWatermarkToFileRequestWatermark`](./box_python_sdk/type/watermarks_files_apply_watermark_to_file_request_watermark.py)<a id="watermark-watermarksfilesapplywatermarktofilerequestwatermarkbox_python_sdktypewatermarks_files_apply_watermark_to_file_request_watermarkpy"></a>


##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WatermarksFilesApplyWatermarkToFileRequest`](./box_python_sdk/type/watermarks_files_apply_watermark_to_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Watermark`](./box_python_sdk/pydantic/watermark.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/watermark` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.watermarks_(files).get`<a id="boxwatermarks_filesget"></a>

Retrieve the watermark for a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = box.watermarks_(files).get(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🔄 Return<a id="🔄-return"></a>

[`Watermark`](./box_python_sdk/pydantic/watermark.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/watermark` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.watermarks_(files).remove_watermark`<a id="boxwatermarks_filesremove_watermark"></a>

Removes the watermark from a file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.watermarks_(files).remove_watermark(
    file_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

The unique identifier that represents a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/files/{file_id}/watermark` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.watermarks_(folders).apply_to_folder`<a id="boxwatermarks_foldersapply_to_folder"></a>

Applies or update a watermark on a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apply_to_folder_response = box.watermarks_(folders).apply_to_folder(
    watermark={
        "imprint": "default",
    },
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### watermark: [`WatermarksFoldersApplyToFolderRequestWatermark`](./box_python_sdk/type/watermarks_folders_apply_to_folder_request_watermark.py)<a id="watermark-watermarksfoldersapplytofolderrequestwatermarkbox_python_sdktypewatermarks_folders_apply_to_folder_request_watermarkpy"></a>


##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WatermarksFoldersApplyToFolderRequest`](./box_python_sdk/type/watermarks_folders_apply_to_folder_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Watermark`](./box_python_sdk/pydantic/watermark.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/watermark` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.watermarks_(folders).get_folder_watermark`<a id="boxwatermarks_foldersget_folder_watermark"></a>

Retrieve the watermark for a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_folder_watermark_response = box.watermarks_(folders).get_folder_watermark(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🔄 Return<a id="🔄-return"></a>

[`Watermark`](./box_python_sdk/pydantic/watermark.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/watermark` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.watermarks_(folders).remove_folder_watermark`<a id="boxwatermarks_foldersremove_folder_watermark"></a>

Removes the watermark from a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.watermarks_(folders).remove_folder_watermark(
    folder_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_id}/watermark` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.web_links.create_object`<a id="boxweb_linkscreate_object"></a>

Creates a web link object within a folder.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_object_response = box.web_links.create_object(
    url="https://box.com",
    parent={
        "id": "0",
    },
    description="Cloud Content Management",
    name="Box Website",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

The URL that this web link links to. Must start with `\\\"http://\\\"` or `\\\"https://\\\"`.

##### parent: [`WebLinksCreateObjectRequestParent`](./box_python_sdk/type/web_links_create_object_request_parent.py)<a id="parent-weblinkscreateobjectrequestparentbox_python_sdktypeweb_links_create_object_request_parentpy"></a>


##### description: `str`<a id="description-str"></a>

Description of the web link.

##### name: `str`<a id="name-str"></a>

Name of the web link. Defaults to the URL if not set.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebLinksCreateObjectRequest`](./box_python_sdk/type/web_links_create_object_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.web_links.get_information`<a id="boxweb_linksget_information"></a>

Retrieve information about a web link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = box.web_links.get_information(
    web_link_id="12345",
    boxapi="shared_link=[link]&shared_link_password=[password]",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### boxapi: `str`<a id="boxapi-str"></a>

The URL, and optional password, for the shared link of this item.  This header can be used to access items that have not been explicitly shared with a user.  Use the format `shared_link=[link]` or if a password is required then use `shared_link=[link]&shared_link_password=[password]`.  This header can be used on the file or folder shared, as well as on any files or folders nested within the item.

#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.web_links.remove_link`<a id="boxweb_linksremove_link"></a>

Deletes a web link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.web_links.remove_link(
    web_link_id="12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.web_links.update_object`<a id="boxweb_linksupdate_object"></a>

Updates a web link object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_object_response = box.web_links.update_object(
    web_link_id="12345",
    description="Cloud Content Management",
    url="https://box.com",
    parent=None,
    name="Box Website",
    shared_link={
        "access": "open",
        "password": "do-not-use-this-password",
        "vanity_name": "my-shared-link",
        "unshared_at": "2012-12-12T10:53:43-08:00",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### web_link_id: `str`<a id="web_link_id-str"></a>

The ID of the web link.

##### description: `str`<a id="description-str"></a>

A new description of the web link.

##### url: `str`<a id="url-str"></a>

The new URL that the web link links to. Must start with `\\\"http://\\\"` or `\\\"https://\\\"`.

##### parent: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./box_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="parent-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-nonebox_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### name: `str`<a id="name-str"></a>

A new name for the web link. Defaults to the URL if not set.

##### shared_link: [`WebLinksUpdateObjectRequestSharedLink`](./box_python_sdk/type/web_links_update_object_request_shared_link.py)<a id="shared_link-weblinksupdateobjectrequestsharedlinkbox_python_sdktypeweb_links_update_object_request_shared_linkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebLinksUpdateObjectRequest`](./box_python_sdk/type/web_links_update_object_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebLink`](./box_python_sdk/pydantic/web_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/web_links/{web_link_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.webhooks.get_specific_webhook`<a id="boxwebhooksget_specific_webhook"></a>

Retrieves a specific webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_webhook_response = box.webhooks.get_specific_webhook(
    webhook_id="3321123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

The ID of the webhook.

#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./box_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhook_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.webhooks.remove`<a id="boxwebhooksremove"></a>

Deletes a webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.webhooks.remove(
    webhook_id="3321123",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

The ID of the webhook.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhook_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.webhooks.update_webhook`<a id="boxwebhooksupdate_webhook"></a>

Updates a webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_response = box.webhooks.update_webhook(
    webhook_id="3321123",
    target={
        "id": "1231232",
        "type": "file",
    },
    address="https://example.com/webhooks",
    triggers=["FILE.UPLOADED"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

The ID of the webhook.

##### target: [`WebhooksUpdateWebhookRequestTarget`](./box_python_sdk/type/webhooks_update_webhook_request_target.py)<a id="target-webhooksupdatewebhookrequesttargetbox_python_sdktypewebhooks_update_webhook_request_targetpy"></a>


##### address: `str`<a id="address-str"></a>

The URL that is notified by this webhook

##### triggers: [`WebhooksUpdateWebhookRequestTriggers`](./box_python_sdk/type/webhooks_update_webhook_request_triggers.py)<a id="triggers-webhooksupdatewebhookrequesttriggersbox_python_sdktypewebhooks_update_webhook_request_triggerspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateWebhookRequest`](./box_python_sdk/type/webhooks_update_webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./box_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhook_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.webhooks.webhooks`<a id="boxwebhookswebhooks"></a>

Returns all defined webhooks for the requesting application.

This API only returns webhooks that are applied to files or folders that are
owned by the authenticated user. This means that an admin can not see webhooks
created by a service account unless the admin has access to those folders, and
vice versa.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhooks_response = box.webhooks.webhooks(
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
    limit=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

#### 🔄 Return<a id="🔄-return"></a>

[`Webhooks`](./box_python_sdk/pydantic/webhooks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.webhooks.webhooks_0`<a id="boxwebhookswebhooks_0"></a>

Creates a webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webhooks_0_response = box.webhooks.webhooks_0(
    target={
        "id": "1231232",
        "type": "file",
    },
    address="https://example.com/webhooks",
    triggers=["FILE.UPLOADED"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target: [`PostWebhooksRequestTarget`](./box_python_sdk/type/post_webhooks_request_target.py)<a id="target-postwebhooksrequesttargetbox_python_sdktypepost_webhooks_request_targetpy"></a>


##### address: `str`<a id="address-str"></a>

The URL that is notified by this webhook

##### triggers: [`PostWebhooksRequestTriggers`](./box_python_sdk/type/post_webhooks_request_triggers.py)<a id="triggers-postwebhooksrequesttriggersbox_python_sdktypepost_webhooks_request_triggerspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostWebhooksRequest`](./box_python_sdk/type/post_webhooks_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./box_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.workflows.start_based_on_request`<a id="boxworkflowsstart_based_on_request"></a>

Initiates a flow with a trigger type of `WORKFLOW_MANUAL_START`.

You application must be authorized to use the `Manage Box Relay` application
scope within the developer console.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
box.workflows.start_based_on_request(
    flow={
        "type": "flow",
        "id": "123456789",
    },
    files=[
        {
            "type": "file",
            "id": "12345678",
        }
    ],
    folder={
        "type": "folder",
        "id": "87654321",
    },
    workflow_id="12345",
    type="workflow_parameters",
    outcomes=[
        {
            "id": "17363629",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flow: [`WorkflowsStartBasedOnRequestRequestFlow`](./box_python_sdk/type/workflows_start_based_on_request_request_flow.py)<a id="flow-workflowsstartbasedonrequestrequestflowbox_python_sdktypeworkflows_start_based_on_request_request_flowpy"></a>


##### files: [`WorkflowsStartBasedOnRequestRequestFiles`](./box_python_sdk/type/workflows_start_based_on_request_request_files.py)<a id="files-workflowsstartbasedonrequestrequestfilesbox_python_sdktypeworkflows_start_based_on_request_request_filespy"></a>

##### folder: [`WorkflowsStartBasedOnRequestRequestFolder`](./box_python_sdk/type/workflows_start_based_on_request_request_folder.py)<a id="folder-workflowsstartbasedonrequestrequestfolderbox_python_sdktypeworkflows_start_based_on_request_request_folderpy"></a>


##### workflow_id: `str`<a id="workflow_id-str"></a>

The ID of the workflow.

##### type: `str`<a id="type-str"></a>

The type of the parameters object

##### outcomes: List[`Outcome`]<a id="outcomes-listoutcome"></a>

A configurable outcome the workflow should complete.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowsStartBasedOnRequestRequest`](./box_python_sdk/type/workflows_start_based_on_request_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflows/{workflow_id}/start` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.workflows.workflows`<a id="boxworkflowsworkflows"></a>

Returns list of workflows that act on a given `folder ID`, and
have a flow with a trigger type of `WORKFLOW_MANUAL_START`.

You application must be authorized to use the `Manage Box Relay` application
scope within the developer console in to use this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workflows_response = box.workflows.workflows(
    folder_id="12345",
    trigger_type="WORKFLOW_MANUAL_START",
    limit=1000,
    marker="JV9IRGZmieiBasejOG9yDCRNgd2ymoZIbjsxbJMjIs3kioVii",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_id: `str`<a id="folder_id-str"></a>

The unique identifier that represent a folder.  The ID for any folder can be determined by visiting this folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folder/123` the `folder_id` is `123`.  The root folder of a Box account is always represented by the ID `0`.

##### trigger_type: `str`<a id="trigger_type-str"></a>

Type of trigger to search for.

##### limit: `int`<a id="limit-int"></a>

The maximum number of items to return per page.

##### marker: `str`<a id="marker-str"></a>

Defines the position marker at which to begin returning results. This is used when paginating using marker-based pagination.  This requires `usemarker` to be set to `true`.

#### 🔄 Return<a id="🔄-return"></a>

[`Workflows`](./box_python_sdk/pydantic/workflows.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workflows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.zip_downloads.create_request`<a id="boxzip_downloadscreate_request"></a>

Creates a request to download multiple files and folders as a single `zip`
archive file. This API does not return the archive but instead performs all
the checks to ensure that the user has access to all the items, and then
returns a `download_url` and a `status_url` that can be used to download the
archive.

The limit for an archive is either the Account's upload limit or
10,000 files, whichever is met first.

**Note**: Downloading a large file can be
affected by various
factors such as distance, network latency,
bandwidth, and congestion, as well as packet loss
ratio and current server load.
For these reasons we recommend that a maximum ZIP archive
total size does not exceed 25GB.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = box.zip_downloads.create_request(
    items=[
        {
            "type": "file",
            "id": "12345",
        }
    ],
    download_file_name="January Financials",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: [`ZipDownloadRequestItems`](./box_python_sdk/type/zip_download_request_items.py)<a id="items-zipdownloadrequestitemsbox_python_sdktypezip_download_request_itemspy"></a>

##### download_file_name: `str`<a id="download_file_name-str"></a>

The optional name of the `zip` archive. This name will be appended by the `.zip` file extension, for example `January Financials.zip`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ZipDownloadRequest`](./box_python_sdk/type/zip_download_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ZipDownload`](./box_python_sdk/pydantic/zip_download.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/zip_downloads` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.zip_downloads.get_content_by_id`<a id="boxzip_downloadsget_content_by_id"></a>

Returns the contents of a `zip` archive in binary format. This URL does not
require any form of authentication and could be used in a user's browser to
download the archive to a user's device.

By default, this URL is only valid for a few seconds from the creation of
the request for this archive. Once a download has started it can not be
stopped and resumed, instead a new request for a zip archive would need to
be created.

The URL of this endpoint should not be considered as fixed. Instead, use
the [Create zip download](e://post_zip_downloads) API to request to create a
`zip` archive, and then follow the `download_url` field in the response to
this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_by_id_response = box.zip_downloads.get_content_by_id(
    zip_download_id="Lu6fA9Ob-jyysp3AAvMF4AkLEwZwAYbL=tgj2zIC=eK9RvJnJbjJl9rNh2qBgHDpyOCAOhpM=vajg2mKq8Mdd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zip_download_id: `str`<a id="zip_download_id-str"></a>

The unique identifier that represent this `zip` archive.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/zip_downloads/{zip_download_id}/content` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `box.zip_downloads.get_status`<a id="boxzip_downloadsget_status"></a>

Returns the download status of a `zip` archive, allowing an application to
inspect the progress of the download as well as the number of items that
might have been skipped.

This endpoint can only be accessed once the download has started.
Subsequently this endpoint is valid for 12 hours from the start of the
download.

The URL of this endpoint should not be considered as fixed. Instead, use
the [Create zip download](e://post_zip_downloads) API to request to create a
`zip` archive, and then follow the `status_url` field in the response to
this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_response = box.zip_downloads.get_status(
    zip_download_id="Lu6fA9Ob-jyysp3AAvMF4AkLEwZwAYbL=tgj2zIC=eK9RvJnJbjJl9rNh2qBgHDpyOCAOhpM=vajg2mKq8Mdd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zip_download_id: `str`<a id="zip_download_id-str"></a>

The unique identifier that represent this `zip` archive.

#### 🔄 Return<a id="🔄-return"></a>

[`ZipDownloadStatus`](./box_python_sdk/pydantic/zip_download_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/zip_downloads/{zip_download_id}/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
