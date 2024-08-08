from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.student import Student
from models.user import User
from models.organizations import Organizations
from models.leads import Leads

admin_collection = Admin
student_collection = Student
user_collection = User
organization_collection =Organizations
lead_collection = Leads

async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


async def retrieve_students() -> List[Student]:
    students = await student_collection.all().to_list()
    return students

async def retrieve_users() -> List[User]:
    users = await user_collection.all().to_list()
    return users

async def retrieve_leads() -> List[Leads]:
    leads = await lead_collection.all().to_list()
    return leads

async def add_student(new_student: Student) -> Student:
    student = await new_student.create()
    return student


async def retrieve_student(id: PydanticObjectId) -> Student:
    student = await student_collection.get(id)
    if student:
        return student


async def delete_student(id: PydanticObjectId) -> bool:
    student = await student_collection.get(id)
    if student:
        await student.delete()
        return True


async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    student = await student_collection.get(id)
    if student:
        await student.update(update_query)
        return student
    return False

# Organizations

async def add_organizations(new_organizations: Organizations) -> Organizations:
    organization = await new_organizations.create()
    return organization


async def retrieve_organizations() -> list[Organizations]:
    organization = await organization_collection.all().to_list()
    return organization


async def update_organization_data(id: PydanticObjectId, data: dict) -> Union[bool, Organizations]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    organization = await organization_collection.get(id)
    if organization:
        await organization.update(update_query)
        return organization
    return False

async def delete_organization(id: PydanticObjectId) -> bool:
    organization = await organization_collection.get(id)
    if organization:
        await organization.delete()
        return True

# leads
# async def retrieve_leads(skip: int, limit: int) -> List[Leads]:
#     cursor = lead_collection.find().skip(skip).limit(limit)
#     leads = await cursor.to_list(length=limit)
#     return leads

# async def retrieve_leads() -> list[Leads]:
#     leads = await lead_collection.all().to_list()
#     if leads:
#         return leads

