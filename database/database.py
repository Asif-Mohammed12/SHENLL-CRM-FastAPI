from typing import List, Union
from pydantic import EmailStr
from beanie import PydanticObjectId
from typing import Optional
from models.admin import Admin
from models.student import Student
from models.user import User
from models.staff import Staffs
from models.lead import Leads
from models.lead_status import LeadStatus
from models.leadsours import LeadSource
from models.organizations import Organizations
# from models.task import Tasks

admin_collection = Admin
student_collection = Student
user_collection = User
staff_collection = Staffs
lead_collection = Leads
leadstatus_collection = LeadStatus
leadsource_collection = LeadSource
organization_collection =Organizations

async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


async def retrieve_students() -> List[Student]:
    students = await student_collection.all().to_list()
    return students

async def retrieve_leads() -> List[Leads]:
    leads = await lead_collection.all().to_list()
    return leads

async def retrieve_leadstatus() -> List[LeadStatus]:
    leadstatus = await leadstatus_collection.all().to_list()
    return leadstatus

async def retrieve_leadsource() -> List[LeadSource]:
    leadsource = await leadsource_collection.all().to_list()
    return leadsource

async def retrieve_users() -> List[User]:
    users = await user_collection.all().to_list()
    return users

async def retrieve_user(id: PydanticObjectId) -> User:
    user = await user_collection.get(id)
    if user:
        return user

async def add_user(new_user: User) -> User:
    new_user = await new_user.create()
    return new_user

async def update_user_data(id: PydanticObjectId, data: dict) -> Union[bool, User]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    user = await user_collection.get(id)
    if user:
        await user.update(update_query)
        return user
    return False

async def delete_user(id: PydanticObjectId) -> bool:
    user = await user_collection.get(id)
    if user:
        await user.delete()
        return True

async def retrieve_staff() -> List[Staffs]:
    staff = await staff_collection.all().to_list()
    return staff

async def add_staff(new_staff: Staffs) -> Staffs:
    new_staff = await new_staff.create()
    return new_staff

async def update_staff_data(id: PydanticObjectId, data: dict) -> Union[bool, Staffs]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    staff = await staff_collection.get(id)
    if staff:
        await staff.update(update_query)
        return staff
    return False

async def delete_staff(id: PydanticObjectId) -> bool:
    staff = await staff_collection.get(id)
    if staff:
        await staff.delete()
        return True

async def retrieve_staffs(id: PydanticObjectId) -> Staffs:
    staff = await staff_collection.get(id)
    if staff:
        return staff
    
async def add_lead(new_lead: Leads) -> Leads:
    new_lead = await new_lead.create()
    return new_lead

async def add_leadstatus(new_leadstatus: LeadStatus) -> LeadStatus:
    new_leadstatus = await new_leadstatus.create()
    return new_leadstatus

async def add_leadsource(new_leadsource: LeadSource) -> LeadSource:
    new_leadsource = await new_leadsource.create()
    return new_leadsource

async def add_student(new_student: Student) -> Student:
    student = await new_student.create()
    return student

async def retrieve_student(id: PydanticObjectId) -> Student:
    student = await student_collection.get(id)
    if student:
        return student
    
async def retrieve_lead(id: PydanticObjectId) -> Leads:
    lead = await lead_collection.get(id)
    if lead:
        return lead


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

async def update_lead_data(id: PydanticObjectId, data: dict) -> Union[bool, Leads]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    lead = await lead_collection.get(id)
    if lead:
        await lead.update(update_query)
        return lead
    return False

async def update_leadstatus_data(id: PydanticObjectId, data: dict) -> Union[bool, LeadStatus]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    leadstatus = await leadstatus_collection.get(id)
    if leadstatus:
        await leadstatus.update(update_query)
        return leadstatus
    return False

async def update_leadsource_data(id: PydanticObjectId, data: dict) -> Union[bool, LeadSource]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    leadsource = await leadsource_collection.get(id)
    if leadsource:
        await leadsource.update(update_query)
        return leadsource
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
    
async def delete_leads(id: PydanticObjectId) -> bool:
    lead = await lead_collection.get(id)
    if lead:
        await lead.delete()
        return True

async def retrieve_staffsq(name: Optional[str] = None, email: Optional[str] = None, mobile_number: Optional[str] = None) -> List[Staffs]:
    query = {}

    if name:
        query['name'] = {'$regex': name, '$options': 'i'}  # Case-insensitive search
    
    if email:
        query['emailId'] = email
    
    if mobile_number:
        query['mobileNumber'] = mobile_number

    staff = await Staffs.find(query).to_list()
    return staff

# -------------------tasks----------------------------------

# task_collection = Tasks

# async def add_task(new_task: Tasks) -> Tasks:
#     task = await new_task.create()
#     return task


# async def retrieve_tasks() -> list[Tasks]:
#     task = await task_collection.all().to_list()
#     return task