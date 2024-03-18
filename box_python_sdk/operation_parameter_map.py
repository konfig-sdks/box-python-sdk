operation_parameter_map = {
    '/authorize-GET': {
        'parameters': [
            {
                'name': 'response_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'state'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/oauth2/token#refresh-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'refresh_token'
            },
        ]
    },
    '/oauth2/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'code'
            },
            {
                'name': 'refresh_token'
            },
            {
                'name': 'assertion'
            },
            {
                'name': 'subject_token'
            },
            {
                'name': 'subject_token_type'
            },
            {
                'name': 'actor_token'
            },
            {
                'name': 'actor_token_type'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'resource'
            },
            {
                'name': 'box_subject_type'
            },
            {
                'name': 'box_subject_id'
            },
            {
                'name': 'box_shared_link'
            },
        ]
    },
    '/oauth2/revoke-POST': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#add-PUT': {
        'parameters': [
        ]
    },
    '/metadata_templates/schema#classifications-POST': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'templateKey'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'hidden'
            },
            {
                'name': 'copyInstanceOnItemCopy'
            },
        ]
    },
    '/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema-GET': {
        'parameters': [
        ]
    },
    '/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema#update-PUT': {
        'parameters': [
        ]
    },
    '/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo-POST': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'Box__Security__Classification__Key'
            },
        ]
    },
    '/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo-POST': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'Box__Security__Classification__Key'
            },
        ]
    },
    '/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo-PUT': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/collaborations-POST': {
        'parameters': [
            {
                'name': 'item'
            },
            {
                'name': 'accessible_by'
            },
            {
                'name': 'role'
            },
            {
                'name': 'is_access_only'
            },
            {
                'name': 'can_view_path'
            },
            {
                'name': 'expires_at'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'notify'
            },
        ]
    },
    '/collaborations/{collaboration_id}-GET': {
        'parameters': [
            {
                'name': 'collaboration_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/collaborations/{collaboration_id}-DELETE': {
        'parameters': [
            {
                'name': 'collaboration_id'
            },
        ]
    },
    '/collaborations/{collaboration_id}-PUT': {
        'parameters': [
            {
                'name': 'role'
            },
            {
                'name': 'collaboration_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'expires_at'
            },
            {
                'name': 'can_view_path'
            },
        ]
    },
    '/collaborations-GET': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/files/{file_id}/collaborations-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/folders/{folder_id}/collaborations-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/groups/{group_id}/collaborations-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/collections-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/collections/{collection_id}/items-GET': {
        'parameters': [
            {
                'name': 'collection_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/comments-POST': {
        'parameters': [
            {
                'name': 'message'
            },
            {
                'name': 'item'
            },
            {
                'name': 'tagged_message'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/comments/{comment_id}-GET': {
        'parameters': [
            {
                'name': 'comment_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}/comments-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/comments/{comment_id}-DELETE': {
        'parameters': [
            {
                'name': 'comment_id'
            },
        ]
    },
    '/comments/{comment_id}-PUT': {
        'parameters': [
            {
                'name': 'comment_id'
            },
            {
                'name': 'message'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/device_pinners/{device_pinner_id}-GET': {
        'parameters': [
            {
                'name': 'device_pinner_id'
            },
        ]
    },
    '/enterprises/{enterprise_id}/device_pinners-GET': {
        'parameters': [
            {
                'name': 'enterprise_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'direction'
            },
        ]
    },
    '/device_pinners/{device_pinner_id}-DELETE': {
        'parameters': [
            {
                'name': 'device_pinner_id'
            },
        ]
    },
    '/collaboration_whitelist_exempt_targets-POST': {
        'parameters': [
            {
                'name': 'user'
            },
        ]
    },
    '/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}-GET': {
        'parameters': [
            {
                'name': 'collaboration_whitelist_exempt_target_id'
            },
        ]
    },
    '/collaboration_whitelist_exempt_targets-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}-DELETE': {
        'parameters': [
            {
                'name': 'collaboration_whitelist_exempt_target_id'
            },
        ]
    },
    '/collaboration_whitelist_entries-POST': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'direction'
            },
        ]
    },
    '/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}-GET': {
        'parameters': [
            {
                'name': 'collaboration_whitelist_entry_id'
            },
        ]
    },
    '/collaboration_whitelist_entries-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}-DELETE': {
        'parameters': [
            {
                'name': 'collaboration_whitelist_entry_id'
            },
        ]
    },
    '/files/{file_id}/content-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'range'
            },
            {
                'name': 'boxapi'
            },
            {
                'name': 'version'
            },
            {
                'name': 'access_token'
            },
        ]
    },
    '/users/{user_id}/email_aliases-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/email_aliases-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/email_aliases/{email_alias_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'email_alias_id'
            },
        ]
    },
    '/events-GET': {
        'parameters': [
            {
                'name': 'stream_type'
            },
            {
                'name': 'stream_position'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'event_type'
            },
            {
                'name': 'created_after'
            },
            {
                'name': 'created_before'
            },
        ]
    },
    '/events-OPTIONS': {
        'parameters': [
        ]
    },
    '/file_activities-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'activity_types'
            },
            {
                'name': 'comment_fields'
            },
            {
                'name': 'versions_fields'
            },
            {
                'name': 'annotation_fields'
            },
            {
                'name': 'task_fields'
            },
            {
                'name': 'app_activity_fields'
            },
            {
                'name': 'reply_limit'
            },
            {
                'name': 'status'
            },
            {
                'name': 'enable_replies'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/file_requests/{file_request_id}/copy-POST': {
        'parameters': [
            {
                'name': 'folder'
            },
            {
                'name': 'file_request_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'status'
            },
            {
                'name': 'is_email_required'
            },
            {
                'name': 'is_description_required'
            },
            {
                'name': 'expires_at'
            },
        ]
    },
    '/file_requests/{file_request_id}-DELETE': {
        'parameters': [
            {
                'name': 'file_request_id'
            },
        ]
    },
    '/file_requests/{file_request_id}-GET': {
        'parameters': [
            {
                'name': 'file_request_id'
            },
        ]
    },
    '/file_requests/{file_request_id}-PUT': {
        'parameters': [
            {
                'name': 'file_request_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'status'
            },
            {
                'name': 'is_email_required'
            },
            {
                'name': 'is_description_required'
            },
            {
                'name': 'expires_at'
            },
            {
                'name': 'if-match'
            },
        ]
    },
    '/file_version_legal_holds/{file_version_legal_hold_id}-GET': {
        'parameters': [
            {
                'name': 'file_version_legal_hold_id'
            },
        ]
    },
    '/file_version_legal_holds-GET': {
        'parameters': [
            {
                'name': 'policy_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/file_version_retentions/{file_version_retention_id}-GET': {
        'parameters': [
            {
                'name': 'file_version_retention_id'
            },
        ]
    },
    '/file_version_retentions-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'file_version_id'
            },
            {
                'name': 'policy_id'
            },
            {
                'name': 'disposition_action'
            },
            {
                'name': 'disposition_before'
            },
            {
                'name': 'disposition_after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/files/{file_id}/versions/{file_version_id}-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'file_version_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}/versions-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/files/{file_id}/versions/{file_version_id}-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'file_version_id'
            },
            {
                'name': 'if-match'
            },
        ]
    },
    '/files/{file_id}/versions/current-POST': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}/versions/{file_version_id}-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'file_version_id'
            },
            {
                'name': 'trashed_at'
            },
        ]
    },
    '/files/{file_id}/copy-POST': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'file_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'name'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'if-match'
            },
        ]
    },
    '/files/{file_id}-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'if-none-match'
            },
            {
                'name': 'boxapi'
            },
            {
                'name': 'x-rep-hints'
            },
        ]
    },
    '/files/{file_id}/thumbnail.{extension}-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'extension'
            },
            {
                'name': 'min_height'
            },
            {
                'name': 'min_width'
            },
            {
                'name': 'max_height'
            },
            {
                'name': 'max_width'
            },
        ]
    },
    '/files/content-OPTIONS': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'size'
            },
            {
                'name': 'parent'
            },
        ]
    },
    '/files/{file_id}-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'shared_link'
            },
            {
                'name': 'lock'
            },
            {
                'name': 'disposition_at'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'collections'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'if-match'
            },
        ]
    },
    '/folder_locks-POST': {
        'parameters': [
            {
                'name': 'folder'
            },
            {
                'name': 'locked_operations'
            },
        ]
    },
    '/folder_locks/{folder_lock_id}-DELETE': {
        'parameters': [
            {
                'name': 'folder_lock_id'
            },
        ]
    },
    '/folder_locks-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}/copy-POST': {
        'parameters': [
            {
                'name': 'parent'
            },
            {
                'name': 'folder_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/{folder_id}-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'if-match'
            },
            {
                'name': 'recursive'
            },
        ]
    },
    '/folders-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'folder_upload_email'
            },
            {
                'name': 'sync_state'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/{folder_id}-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'if-none-match'
            },
            {
                'name': 'boxapi'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/folders/{folder_id}/items-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'usemarker'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'boxapi'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'direction'
            },
        ]
    },
    '/folders/{folder_id}-PUT': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sync_state'
            },
            {
                'name': 'can_non_owners_invite'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'shared_link'
            },
            {
                'name': 'folder_upload_email'
            },
            {
                'name': 'is_collaboration_restricted_to_enterprise'
            },
            {
                'name': 'collections'
            },
            {
                'name': 'can_non_owners_view_collaborators'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'if-match'
            },
        ]
    },
    '/group_memberships-POST': {
        'parameters': [
            {
                'name': 'user'
            },
            {
                'name': 'group'
            },
            {
                'name': 'role'
            },
            {
                'name': 'configurable_permissions'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/users/{user_id}/memberships-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/group_memberships/{group_membership_id}-GET': {
        'parameters': [
            {
                'name': 'group_membership_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/groups/{group_id}/memberships-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/group_memberships/{group_membership_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_membership_id'
            },
        ]
    },
    '/group_memberships/{group_membership_id}-PUT': {
        'parameters': [
            {
                'name': 'group_membership_id'
            },
            {
                'name': 'role'
            },
            {
                'name': 'configurable_permissions'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/groups/{group_id}-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/groups-GET': {
        'parameters': [
            {
                'name': 'filter_term'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/groups-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'provenance'
            },
            {
                'name': 'external_sync_identifier'
            },
            {
                'name': 'invitability_level'
            },
            {
                'name': 'member_viewability_level'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/groups/{group_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
        ]
    },
    '/groups/{group_id}-PUT': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'provenance'
            },
            {
                'name': 'external_sync_identifier'
            },
            {
                'name': 'invitability_level'
            },
            {
                'name': 'member_viewability_level'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/integration_mappings/slack-POST': {
        'parameters': [
            {
                'name': 'partner_item'
            },
            {
                'name': 'box_item'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/integration_mappings/slack/{integration_mapping_id}-DELETE': {
        'parameters': [
            {
                'name': 'integration_mapping_id'
            },
        ]
    },
    '/integration_mappings/slack-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'partner_item_type'
            },
            {
                'name': 'partner_item_id'
            },
            {
                'name': 'box_item_id'
            },
            {
                'name': 'box_item_type'
            },
            {
                'name': 'is_manually_created'
            },
        ]
    },
    '/integration_mappings/slack/{integration_mapping_id}-PUT': {
        'parameters': [
            {
                'name': 'integration_mapping_id'
            },
            {
                'name': 'box_item'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/invites/{invite_id}-GET': {
        'parameters': [
            {
                'name': 'invite_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/invites-POST': {
        'parameters': [
            {
                'name': 'enterprise'
            },
            {
                'name': 'actionable_by'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/legal_hold_policies-POST': {
        'parameters': [
            {
                'name': 'policy_name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'filter_started_at'
            },
            {
                'name': 'filter_ended_at'
            },
            {
                'name': 'is_ongoing'
            },
        ]
    },
    '/legal_hold_policies/{legal_hold_policy_id}-GET': {
        'parameters': [
            {
                'name': 'legal_hold_policy_id'
            },
        ]
    },
    '/legal_hold_policies-GET': {
        'parameters': [
            {
                'name': 'policy_name'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/legal_hold_policies/{legal_hold_policy_id}-DELETE': {
        'parameters': [
            {
                'name': 'legal_hold_policy_id'
            },
        ]
    },
    '/legal_hold_policies/{legal_hold_policy_id}-PUT': {
        'parameters': [
            {
                'name': 'legal_hold_policy_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'policy_name'
            },
            {
                'name': 'release_notes'
            },
        ]
    },
    '/legal_hold_policy_assignments-POST': {
        'parameters': [
            {
                'name': 'policy_id'
            },
            {
                'name': 'assign_to'
            },
        ]
    },
    '/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}-GET': {
        'parameters': [
            {
                'name': 'legal_hold_policy_assignment_id'
            },
        ]
    },
    '/legal_hold_policy_assignments-GET': {
        'parameters': [
            {
                'name': 'policy_id'
            },
            {
                'name': 'assign_to_type'
            },
            {
                'name': 'assign_to_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold-GET': {
        'parameters': [
            {
                'name': 'legal_hold_policy_assignment_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/file_versions_on_hold-GET': {
        'parameters': [
            {
                'name': 'legal_hold_policy_assignment_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}-DELETE': {
        'parameters': [
            {
                'name': 'legal_hold_policy_assignment_id'
            },
        ]
    },
    '/metadata_cascade_policies/{metadata_cascade_policy_id}/apply-POST': {
        'parameters': [
            {
                'name': 'conflict_resolution'
            },
            {
                'name': 'metadata_cascade_policy_id'
            },
        ]
    },
    '/metadata_cascade_policies-POST': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'templateKey'
            },
        ]
    },
    '/metadata_cascade_policies/{metadata_cascade_policy_id}-GET': {
        'parameters': [
            {
                'name': 'metadata_cascade_policy_id'
            },
        ]
    },
    '/metadata_cascade_policies-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'owner_enterprise_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/metadata_cascade_policies/{metadata_cascade_policy_id}-DELETE': {
        'parameters': [
            {
                'name': 'metadata_cascade_policy_id'
            },
        ]
    },
    '/files/{file_id}/metadata/{scope}/{template_key}-POST': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/files/{file_id}/metadata/{scope}/{template_key}-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/files/{file_id}/metadata-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/metadata/{scope}/{template_key}-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/files/{file_id}/metadata/{scope}/{template_key}-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/folders/{folder_id}/metadata/{scope}/{template_key}-POST': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/folders/{folder_id}/metadata/{scope}/{template_key}-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/folders/{folder_id}/metadata-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}/metadata/{scope}/{template_key}-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/folders/{folder_id}/metadata/{scope}/{template_key}-PUT': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/metadata_templates/schema-POST': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'templateKey'
            },
            {
                'name': 'hidden'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'copyInstanceOnItemCopy'
            },
        ]
    },
    '/metadata_templates/{scope}/{template_key}/schema-DELETE': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/metadata_templates-GET': {
        'parameters': [
            {
                'name': 'metadata_instance_id'
            },
        ]
    },
    '/metadata_templates/{template_id}-GET': {
        'parameters': [
            {
                'name': 'template_id'
            },
        ]
    },
    '/metadata_templates/{scope}/{template_key}/schema-GET': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/metadata_templates/enterprise-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/metadata_templates/global-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/metadata_templates/{scope}/{template_key}/schema-PUT': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'template_key'
            },
        ]
    },
    '/recent_items-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/retention_policies-POST': {
        'parameters': [
            {
                'name': 'policy_name'
            },
            {
                'name': 'policy_type'
            },
            {
                'name': 'disposition_action'
            },
            {
                'name': 'description'
            },
            {
                'name': 'retention_length'
            },
            {
                'name': 'retention_type'
            },
            {
                'name': 'can_owner_extend_retention'
            },
            {
                'name': 'are_owners_notified'
            },
            {
                'name': 'custom_notification_recipients'
            },
        ]
    },
    '/retention_policies/{retention_policy_id}-DELETE': {
        'parameters': [
            {
                'name': 'retention_policy_id'
            },
        ]
    },
    '/retention_policies/{retention_policy_id}-GET': {
        'parameters': [
            {
                'name': 'retention_policy_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/retention_policies-GET': {
        'parameters': [
            {
                'name': 'policy_name'
            },
            {
                'name': 'policy_type'
            },
            {
                'name': 'created_by_user_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/retention_policies/{retention_policy_id}-PUT': {
        'parameters': [
            {
                'name': 'retention_policy_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'policy_name'
            },
            {
                'name': 'disposition_action'
            },
            {
                'name': 'retention_type'
            },
            {
                'name': 'retention_length'
            },
            {
                'name': 'status'
            },
            {
                'name': 'can_owner_extend_retention'
            },
            {
                'name': 'are_owners_notified'
            },
            {
                'name': 'custom_notification_recipients'
            },
        ]
    },
    '/retention_policy_assignments-POST': {
        'parameters': [
            {
                'name': 'policy_id'
            },
            {
                'name': 'assign_to'
            },
            {
                'name': 'filter_fields'
            },
            {
                'name': 'start_date_field'
            },
        ]
    },
    '/retention_policy_assignments/{retention_policy_assignment_id}-GET': {
        'parameters': [
            {
                'name': 'retention_policy_assignment_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/retention_policies/{retention_policy_id}/assignments-GET': {
        'parameters': [
            {
                'name': 'retention_policy_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/retention_policy_assignments/{retention_policy_assignment_id}/file_versions_under_retention-GET': {
        'parameters': [
            {
                'name': 'retention_policy_assignment_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention-GET': {
        'parameters': [
            {
                'name': 'retention_policy_assignment_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/retention_policy_assignments/{retention_policy_assignment_id}-DELETE': {
        'parameters': [
            {
                'name': 'retention_policy_assignment_id'
            },
        ]
    },
    '/metadata_queries/execute_read-POST': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'ancestor_folder_id'
            },
            {
                'name': 'query'
            },
            {
                'name': 'query_params'
            },
            {
                'name': 'order_by'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'file_extensions'
            },
            {
                'name': 'created_at_range'
            },
            {
                'name': 'updated_at_range'
            },
            {
                'name': 'size_range'
            },
            {
                'name': 'owner_user_ids'
            },
            {
                'name': 'recent_updater_user_ids'
            },
            {
                'name': 'ancestor_folder_ids'
            },
            {
                'name': 'content_types'
            },
            {
                'name': 'type'
            },
            {
                'name': 'trash_content'
            },
            {
                'name': 'mdfilters'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'include_recent_shared_links'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'deleted_user_ids'
            },
            {
                'name': 'deleted_at_range'
            },
        ]
    },
    '/users/terminate_sessions-POST': {
        'parameters': [
            {
                'name': 'user_ids'
            },
            {
                'name': 'user_logins'
            },
        ]
    },
    '/groups/terminate_sessions-POST': {
        'parameters': [
            {
                'name': 'group_ids'
            },
        ]
    },
    '/files/{file_id}#add_shared_link-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/shared_items-GET': {
        'parameters': [
            {
                'name': 'boxapi'
            },
            {
                'name': 'if-none-match'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}#get_shared_link-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}#remove_shared_link-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/files/{file_id}#update_shared_link-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/folders/{folder_id}#add_shared_link-PUT': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/shared_items#folders-GET': {
        'parameters': [
            {
                'name': 'boxapi'
            },
            {
                'name': 'if-none-match'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/{folder_id}#get_shared_link-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/{folder_id}#remove_shared_link-PUT': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/folders/{folder_id}#update_shared_link-PUT': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/web_links/{web_link_id}#add_shared_link-PUT': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/shared_items#web_links-GET': {
        'parameters': [
            {
                'name': 'boxapi'
            },
            {
                'name': 'if-none-match'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/web_links/{web_link_id}#get_shared_link-GET': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/web_links/{web_link_id}#remove_shared_link-PUT': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/web_links/{web_link_id}#update_shared_link-PUT': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/shield_information_barrier_reports-POST': {
        'parameters': [
            {
                'name': 'shield_information_barrier'
            },
        ]
    },
    '/shield_information_barrier_reports/{shield_information_barrier_report_id}-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_report_id'
            },
        ]
    },
    '/shield_information_barrier_reports-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/shield_information_barrier_segment_members-POST': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment'
            },
            {
                'name': 'user'
            },
            {
                'name': 'type'
            },
            {
                'name': 'shield_information_barrier'
            },
        ]
    },
    '/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_member_id'
            },
        ]
    },
    '/shield_information_barrier_segment_members-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}-DELETE': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_member_id'
            },
        ]
    },
    '/shield_information_barrier_segment_restrictions-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'shield_information_barrier_segment'
            },
            {
                'name': 'restricted_segment'
            },
            {
                'name': 'shield_information_barrier'
            },
        ]
    },
    '/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_restriction_id'
            },
        ]
    },
    '/shield_information_barrier_segment_restrictions-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}-DELETE': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_restriction_id'
            },
        ]
    },
    '/shield_information_barrier_segments-POST': {
        'parameters': [
            {
                'name': 'shield_information_barrier'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/shield_information_barrier_segments/{shield_information_barrier_segment_id}-DELETE': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_id'
            },
        ]
    },
    '/shield_information_barrier_segments/{shield_information_barrier_segment_id}-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_id'
            },
        ]
    },
    '/shield_information_barrier_segments-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_id'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/shield_information_barrier_segments/{shield_information_barrier_segment_id}-PUT': {
        'parameters': [
            {
                'name': 'shield_information_barrier_segment_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/shield_information_barriers/change_status-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/shield_information_barriers-POST': {
        'parameters': [
            {
                'name': 'enterprise'
            },
        ]
    },
    '/shield_information_barriers/{shield_information_barrier_id}-GET': {
        'parameters': [
            {
                'name': 'shield_information_barrier_id'
            },
        ]
    },
    '/shield_information_barriers-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/sign_requests/{sign_request_id}/cancel-POST': {
        'parameters': [
            {
                'name': 'sign_request_id'
            },
        ]
    },
    '/sign_requests-POST': {
        'parameters': [
            {
                'name': 'signers'
            },
            {
                'name': 'is_document_preparation_needed'
            },
            {
                'name': 'redirect_url'
            },
            {
                'name': 'declined_redirect_url'
            },
            {
                'name': 'are_text_signatures_enabled'
            },
            {
                'name': 'email_subject'
            },
            {
                'name': 'email_message'
            },
            {
                'name': 'are_reminders_enabled'
            },
            {
                'name': 'name'
            },
            {
                'name': 'prefill_tags'
            },
            {
                'name': 'days_valid'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'is_phone_verification_required_to_view'
            },
            {
                'name': 'template_id'
            },
            {
                'name': 'source_files'
            },
            {
                'name': 'signature_color'
            },
            {
                'name': 'parent_folder'
            },
        ]
    },
    '/sign_requests/{sign_request_id}-GET': {
        'parameters': [
            {
                'name': 'sign_request_id'
            },
        ]
    },
    '/sign_requests-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/sign_requests/{sign_request_id}/resend-POST': {
        'parameters': [
            {
                'name': 'sign_request_id'
            },
        ]
    },
    '/sign_templates/{template_id}-GET': {
        'parameters': [
            {
                'name': 'template_id'
            },
        ]
    },
    '/sign_templates-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/files/{file_id}/metadata/global/boxSkillsCards-POST': {
        'parameters': [
            {
                'name': 'cards'
            },
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/metadata/global/boxSkillsCards-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/metadata/global/boxSkillsCards-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/skill_invocations/{skill_id}-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'file'
            },
            {
                'name': 'skill_id'
            },
            {
                'name': 'file_version'
            },
            {
                'name': 'usage'
            },
        ]
    },
    '/files/{file_id}/metadata/global/boxSkillsCards-PUT': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/storage_policies/{storage_policy_id}-GET': {
        'parameters': [
            {
                'name': 'storage_policy_id'
            },
        ]
    },
    '/storage_policies-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/storage_policy_assignments-POST': {
        'parameters': [
            {
                'name': 'storage_policy'
            },
            {
                'name': 'assigned_to'
            },
        ]
    },
    '/storage_policy_assignments/{storage_policy_assignment_id}-GET': {
        'parameters': [
            {
                'name': 'storage_policy_assignment_id'
            },
        ]
    },
    '/storage_policy_assignments-GET': {
        'parameters': [
            {
                'name': 'resolved_for_type'
            },
            {
                'name': 'resolved_for_id'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/storage_policy_assignments/{storage_policy_assignment_id}-DELETE': {
        'parameters': [
            {
                'name': 'storage_policy_assignment_id'
            },
        ]
    },
    '/storage_policy_assignments/{storage_policy_assignment_id}-PUT': {
        'parameters': [
            {
                'name': 'storage_policy'
            },
            {
                'name': 'storage_policy_assignment_id'
            },
        ]
    },
    '/task_assignments-POST': {
        'parameters': [
            {
                'name': 'task'
            },
            {
                'name': 'assign_to'
            },
        ]
    },
    '/task_assignments/{task_assignment_id}-DELETE': {
        'parameters': [
            {
                'name': 'task_assignment_id'
            },
        ]
    },
    '/task_assignments/{task_assignment_id}-GET': {
        'parameters': [
            {
                'name': 'task_assignment_id'
            },
        ]
    },
    '/tasks/{task_id}/assignments-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
        ]
    },
    '/task_assignments/{task_assignment_id}-PUT': {
        'parameters': [
            {
                'name': 'task_assignment_id'
            },
            {
                'name': 'message'
            },
            {
                'name': 'resolution_state'
            },
        ]
    },
    '/tasks/{task_id}-GET': {
        'parameters': [
            {
                'name': 'task_id'
            },
        ]
    },
    '/files/{file_id}/tasks-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/tasks/{task_id}-DELETE': {
        'parameters': [
            {
                'name': 'task_id'
            },
        ]
    },
    '/tasks-POST': {
        'parameters': [
            {
                'name': 'item'
            },
            {
                'name': 'action'
            },
            {
                'name': 'message'
            },
            {
                'name': 'due_at'
            },
            {
                'name': 'completion_rule'
            },
        ]
    },
    '/tasks/{task_id}-PUT': {
        'parameters': [
            {
                'name': 'task_id'
            },
            {
                'name': 'action'
            },
            {
                'name': 'message'
            },
            {
                'name': 'due_at'
            },
            {
                'name': 'completion_rule'
            },
        ]
    },
    '/terms_of_services-POST': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'text'
            },
            {
                'name': 'tos_type'
            },
        ]
    },
    '/terms_of_services-GET': {
        'parameters': [
            {
                'name': 'tos_type'
            },
        ]
    },
    '/terms_of_services/{terms_of_service_id}-GET': {
        'parameters': [
            {
                'name': 'terms_of_service_id'
            },
        ]
    },
    '/terms_of_services/{terms_of_service_id}-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'text'
            },
            {
                'name': 'terms_of_service_id'
            },
        ]
    },
    '/terms_of_service_user_statuses-POST': {
        'parameters': [
            {
                'name': 'tos'
            },
            {
                'name': 'user'
            },
            {
                'name': 'is_accepted'
            },
        ]
    },
    '/terms_of_service_user_statuses-GET': {
        'parameters': [
            {
                'name': 'tos_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/terms_of_service_user_statuses/{terms_of_service_user_status_id}-PUT': {
        'parameters': [
            {
                'name': 'is_accepted'
            },
            {
                'name': 'terms_of_service_user_status_id'
            },
        ]
    },
    '/users/{user_id}/folders/0-PUT': {
        'parameters': [
            {
                'name': 'owned_by'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'notify'
            },
        ]
    },
    '/files/{file_id}/trash-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}/trash-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}-POST': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/{folder_id}/trash-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/{folder_id}/trash-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}-POST': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/folders/trash/items-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'usemarker'
            },
            {
                'name': 'marker'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'sort'
            },
        ]
    },
    '/web_links/{web_link_id}/trash-GET': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/web_links/{web_link_id}/trash-DELETE': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
        ]
    },
    '/web_links/{web_link_id}-POST': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}/content-POST': {
        'parameters': [
            {
                'name': 'file_id'
            },
            {
                'name': 'attributes'
            },
            {
                'name': 'file'
            },
            {
                'name': 'if-match'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'content-md5'
            },
        ]
    },
    '/files/content-POST': {
        'parameters': [
            {
                'name': 'attributes'
            },
            {
                'name': 'file'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'content-md5'
            },
        ]
    },
    '/files/upload_sessions/{upload_session_id}/commit-POST': {
        'parameters': [
            {
                'name': 'parts'
            },
            {
                'name': 'upload_session_id'
            },
            {
                'name': 'digest'
            },
            {
                'name': 'if-match'
            },
            {
                'name': 'if-none-match'
            },
        ]
    },
    '/files/upload_sessions-POST': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'file_size'
            },
            {
                'name': 'file_name'
            },
        ]
    },
    '/files/{file_id}/upload_sessions-POST': {
        'parameters': [
            {
                'name': 'file_size'
            },
            {
                'name': 'file_id'
            },
            {
                'name': 'file_name'
            },
        ]
    },
    '/files/upload_sessions/{upload_session_id}-PUT': {
        'parameters': [
            {
                'name': 'upload_session_id'
            },
            {
                'name': 'digest'
            },
            {
                'name': 'content-range'
            },
        ]
    },
    '/files/upload_sessions/{upload_session_id}-GET': {
        'parameters': [
            {
                'name': 'upload_session_id'
            },
        ]
    },
    '/files/upload_sessions/{upload_session_id}/parts-GET': {
        'parameters': [
            {
                'name': 'upload_session_id'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/files/upload_sessions/{upload_session_id}-DELETE': {
        'parameters': [
            {
                'name': 'upload_session_id'
            },
        ]
    },
    '/users/{user_id}/avatar-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'pic'
            },
        ]
    },
    '/users/{user_id}/avatar-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}/avatar-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/users/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'notify'
            },
            {
                'name': 'force'
            },
        ]
    },
    '/users/me-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
        ]
    },
    '/users/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/users/{user_id}-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'enterprise'
            },
            {
                'name': 'notify'
            },
            {
                'name': 'name'
            },
            {
                'name': 'login'
            },
            {
                'name': 'role'
            },
            {
                'name': 'language'
            },
            {
                'name': 'is_sync_enabled'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'address'
            },
            {
                'name': 'tracking_codes'
            },
            {
                'name': 'can_see_managed_users'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'is_external_collab_restricted'
            },
            {
                'name': 'is_exempt_from_device_limits'
            },
            {
                'name': 'is_exempt_from_login_verification'
            },
            {
                'name': 'is_password_reset_required'
            },
            {
                'name': 'status'
            },
            {
                'name': 'space_amount'
            },
            {
                'name': 'notification_email'
            },
            {
                'name': 'external_app_user_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'filter_term'
            },
            {
                'name': 'user_type'
            },
            {
                'name': 'external_app_user_id'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'usemarker'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/users-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'login'
            },
            {
                'name': 'is_platform_access_only'
            },
            {
                'name': 'role'
            },
            {
                'name': 'language'
            },
            {
                'name': 'is_sync_enabled'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'address'
            },
            {
                'name': 'space_amount'
            },
            {
                'name': 'tracking_codes'
            },
            {
                'name': 'can_see_managed_users'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'is_external_collab_restricted'
            },
            {
                'name': 'is_exempt_from_device_limits'
            },
            {
                'name': 'is_exempt_from_login_verification'
            },
            {
                'name': 'status'
            },
            {
                'name': 'external_app_user_id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/files/{file_id}/watermark-PUT': {
        'parameters': [
            {
                'name': 'watermark'
            },
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/watermark-GET': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/files/{file_id}/watermark-DELETE': {
        'parameters': [
            {
                'name': 'file_id'
            },
        ]
    },
    '/folders/{folder_id}/watermark-PUT': {
        'parameters': [
            {
                'name': 'watermark'
            },
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}/watermark-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/folders/{folder_id}/watermark-DELETE': {
        'parameters': [
            {
                'name': 'folder_id'
            },
        ]
    },
    '/web_links-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/web_links/{web_link_id}-GET': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'boxapi'
            },
        ]
    },
    '/web_links/{web_link_id}-DELETE': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
        ]
    },
    '/web_links/{web_link_id}-PUT': {
        'parameters': [
            {
                'name': 'web_link_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'url'
            },
            {
                'name': 'parent'
            },
            {
                'name': 'name'
            },
            {
                'name': 'shared_link'
            },
        ]
    },
    '/webhooks/{webhook_id}-GET': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/webhooks/{webhook_id}-DELETE': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
        ]
    },
    '/webhooks/{webhook_id}-PUT': {
        'parameters': [
            {
                'name': 'webhook_id'
            },
            {
                'name': 'target'
            },
            {
                'name': 'address'
            },
            {
                'name': 'triggers'
            },
        ]
    },
    '/webhooks-GET': {
        'parameters': [
            {
                'name': 'marker'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/webhooks-POST': {
        'parameters': [
            {
                'name': 'target'
            },
            {
                'name': 'address'
            },
            {
                'name': 'triggers'
            },
        ]
    },
    '/workflows/{workflow_id}/start-POST': {
        'parameters': [
            {
                'name': 'flow'
            },
            {
                'name': 'files'
            },
            {
                'name': 'folder'
            },
            {
                'name': 'workflow_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'outcomes'
            },
        ]
    },
    '/workflows-GET': {
        'parameters': [
            {
                'name': 'folder_id'
            },
            {
                'name': 'trigger_type'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'marker'
            },
        ]
    },
    '/zip_downloads-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'download_file_name'
            },
        ]
    },
    '/zip_downloads/{zip_download_id}/content-GET': {
        'parameters': [
            {
                'name': 'zip_download_id'
            },
        ]
    },
    '/zip_downloads/{zip_download_id}/status-GET': {
        'parameters': [
            {
                'name': 'zip_download_id'
            },
        ]
    },
};