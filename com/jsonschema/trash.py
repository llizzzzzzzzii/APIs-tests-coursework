class ResponseTrash:
    schema = {"type": "object",
              "properties": {
                "kind": {"type": "string"},
                "userPermission": {"type": "object",
                                   "properties": {
                                      "id": {"type": "string"},
                                      "type": {"type": "string"},
                                      "role": {"type": "string"},
                                      "kind": {"type": "string"},
                                      "selfLink": {"type": "string"},
                                      "etag": {"type": "string"},
                                      "pendingOwner": {"type": "boolean"}
                                    }
                                   },
                "fileExtension": {"type": "string"},
                "md5Checksum": {"type": "string"},
                "selfLink": {"type": "string"},
                "ownerNames": {"type": "array",
                               "items": {"type": "string"}},
                "lastModifyingUserName": {"type": "string"},
                "editable": {"type": "boolean"},
                "writersCanShare": {"type": "boolean"},
                "downloadUrl": {"type": "string"},
                "mimeType": {"type": "string"},
                "parents": {"type": "array",
                            "items": {"type": "object",
                                      "properties": {
                                        "selfLink": {"type": "string"},
                                        "id": {"type": "string"},
                                        "isRoot": {"type": "boolean"},
                                        "kind": {"type": "string"},
                                        "parentLink": {"type": "string"}
                                        }
                                    }},
                "thumbnailLink": {"type": "string"},
                "appDataContents": {"type": "boolean"},
                "iconLink": {"type": "string"},
                "shared": {"type": "boolean"},
                "lastModifyingUser": {
                    "type": "object",
                    "properties": {
                        "displayName": {"type": "string"},
                        "kind": {"type": "string"},
                        "isAuthenticatedUser": {"type": "boolean"},
                        "permissionId": {"type": "string"},
                        "emailAddress": {"type": "string"},
                        "picture": {
                          "url": {"type": "string"}
                        }
                      }
                    },
                "owners": {"type": "array",
                           "items":{
                               "type": "object",
                               "properties": {
                                    "displayName": {"type": "string"},
                                    "kind": {"type": "string"},
                                    "isAuthenticatedUser": {"type": "boolean"},
                                    "permissionId": {"type": "string"},
                                    "emailAddress": {"type": "string"},
                                    "picture": {
                                      "url": {"type": "string"}
                                    }
                                  }
                                }
                           },
                "headRevisionId": {"type": "string"},
                "copyable": {"type": "boolean"},
                "etag": {"type": "string"},
                "alternateLink": {"type": "string"},
                "embedLink": {"type": "string"},
                "webContentLink": {"type": "string"},
                "fileSize": {"type": "string"},
                "copyRequiresWriterPermission": {"type": "boolean"},
                "spaces": {"type": "array",
                           "items": {"type": "string"}},
                "id": {"type": "string"},
                "title": {"type": "string"},
                "labels": {
                  "viewed": {"type": "boolean"},
                  "restricted": {"type": "boolean"},
                  "starred": {"type": "boolean"},
                  "hidden": {"type": "boolean"},
                  "trashed": {"type": "boolean"},
                  "modified": {"type": "boolean"}
                },
                "explicitlyTrashed": {"type": "boolean"},
                "createdDate": {"type": "string"},
                "modifiedDate": {"type": "string"},
                "modifiedByMeDate": {"type": "string"},
                "lastViewedByMeDate": {"type": "string"},
                "markedViewedByMeDate": {"type": "string"},
                "sharedWithMeDate": {"type": "string"},
                "quotaBytesUsed": {"type": "string"},
                "version": {"type": "string"},
                "originalFilename": {"type": "string"},
                "capabilities": {
                  "canChangeRestrictedDownload": {"type": "boolean"},
                  "canMoveChildrenOutOfDrive": {"type": "boolean"},
                  "canReadDrive": {"type": "boolean"},
                  "canEdit": {"type": "boolean"},
                  "canCopy": {"type": "boolean"},
                  "canComment": {"type": "boolean"},
                  "canAddChildren": {"type": "boolean"},
                  "canDelete": {"type": "boolean"},
                  "canDownload": {"type": "boolean"},
                  "canListChildren": {"type": "boolean"},
                  "canRemoveChildren": {"type": "boolean"},
                  "canRename": {"type": "boolean"},
                  "canTrash": {"type": "boolean"},
                  "canReadRevisions": {"type": "boolean"},
                  "canReadTeamDrive": {"type": "boolean"},
                  "canMoveTeamDriveItem": {"type": "boolean"},
                  "canChangeCopyRequiresWriterPermission": {"type": "boolean"},
                  "canMoveItemIntoTeamDrive": {"type": "boolean"},
                  "canUntrash": {"type": "boolean"},
                  "canModifyContent": {"type": "boolean"},
                  "canMoveItemWithinTeamDrive": {"type": "boolean"},
                  "canMoveItemOutOfTeamDrive": {"type": "boolean"},
                  "canDeleteChildren": {"type": "boolean"},
                  "canMoveChildrenOutOfTeamDrive": {"type": "boolean"},
                  "canMoveChildrenWithinTeamDrive": {"type": "boolean"},
                  "canTrashChildren": {"type": "boolean"},
                  "canMoveItemOutOfDrive": {"type": "boolean"},
                  "canAddMyDriveParent": {"type": "boolean"},
                  "canRemoveMyDriveParent": {"type": "boolean"},
                  "canMoveItemWithinDrive": {"type": "boolean"},
                  "canShare": {"type": "boolean"},
                  "canMoveChildrenWithinDrive": {"type": "boolean"},
                  "canModifyContentRestriction": {"type": "boolean"},
                  "canAddFolderFromAnotherDrive": {"type": "boolean"},
                  "canChangeSecurityUpdateEnabled": {"type": "boolean"},
                  "canAcceptOwnership": {"type": "boolean"},
                  "canReadLabels": {"type": "boolean"},
                  "canModifyLabels": {"type": "boolean"}
                },
              }
              }
