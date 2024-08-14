# from pydantic import BaseModel, EmailStr, Field, HttpUrl
# from typing import Optional, Any
# # from datetime import datetime
# # from beanie import PydanticObjectId


# class Response(BaseModel):
#     status_code: int
#     status: str
#     message: str
#     data: Optional[Any]

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "status_code": 200,
#                 "status": "ok",
#                 "message": "Leadsource record(s) found",
#                 "data": [
#                     {
#                         "leadStatus": "NEW",
#                         "displayIndex": "1",
#                         "status": "ACTIVE"
#                     }
#                 ]
#             }
#         }


# # class UpdateTasks(BaseModel):
# #     leadName:str
# #     subject:str
# #     relatedTo:str
# #     contactPerson:str
# #     startDate:datetime
# #     dueDate:datetime
# #     priority:str
# #     description:str
# #     assignedTo:Optional[PydanticObjectId]


# #     class Config:
# #         arbitrary_types_allowed = True
# #         json_schema_extra = {
# #             "example": {
# #                 "leadName":"leadName",
# #                 "subject":"subject",
# #                 "relatedTo":"relatedTo",
# #                 "contactPerson":"contactPerson",
# #                 "startDate":"startDate",
# #                 "dueDate":"dueDate",
# #                 "priority":"priority",
# #                 "description":"description",
# #                 "assignedTo":"assignedTo",
# #             }
# #         }