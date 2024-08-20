from typing import List, Union
from fastapi import APIRouter, Body, File, UploadFile, HTTPException
from routes.common import UPLOAD_DIRECTORY
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
from models.tasks import TaskModel
from models.jobtitles import Jobtitles
from models.emails import Emails
from models.departments import Departments
from models.industries import Industries
from models.sms import Sms
from models.reports import Reports
from models.roles import Roles
from models.countries import Countries
# from pymongo import ASCENDING
import os
import shutil
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
# List[Leads] and Page[Leads]
# async def retrieve_leads() -> List[Leads]:
#     leads = await lead_collection.all().to_list()
#     return leads


async def retrieve_leads(page: int = 1, limit: int = 5) -> List[Leads]:
    skip = (page - 1) * limit
    leads_cursor = lead_collection.find().sort([("createdAt", 1), ("_id", 1)]).skip(skip).limit(limit)
    leads = await leads_cursor.to_list(length=limit)
    return leads

# async def retrieve_leads(page: int = 1, limit: int = 5) -> List[Leads]:
#     skip = (page - 1) * limit
#     leads = await lead_collection.find().skip(skip).limit(limit).to_list(length=limit)
#     return leads

async def retrieve_leadsq(firstName: Optional[str] = None,
                            department: Optional[str] = None,
                            organization: Optional[str] = None,
                            website: Optional[str] = None,
                            email: Optional[str] = None,
                            mobileNumber: Optional[str] = None,
                            status: Optional[str] = None,
                            page: int = 1,
                            limit: int = 0 or 20) -> List[Leads]:
    query = {}

    if firstName:
        query['name'] = {'$regex': firstName, '$options': 'i'}  # Case-insensitive search
    
    if email:
        query['emailId'] = email

    if department:
        query['department'] = department

    if website:
        query['website'] = website

    if organization:
        query['organization'] = organization
    
    if status:
        query['status'] = status
    
    if mobileNumber:
        query['mobileNumber'] = mobileNumber

    skip = (page - 1) * limit
    lead_cursor = lead_collection.find(query).sort([("createdAt", 1), ("_id", 1)]).skip(skip).limit(limit)
    lead = await lead_cursor.to_list(length=limit)
    
    return lead
    

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

# async def add_staff(new_staff: Staffs) -> Staffs:
#     new_staff = await new_staff.create()
#      return new_staff
# async def add_staff(new_staff: Staffs) -> Staffs:
#     created_staff = await new_staff.create()
#     pipeline = [
#         {
#             "$lookup": {
#                 "from": "reports",  # Collection name as a string
#                 "localField": "reportTo",  # Field in the Staffs collection
#                 "foreignField": "_id",  # Field in the Leads collection
#                 "as": "report"
#             }
#         },
#         {
#             "$unwind": "$reports"  # Unwind if `lead` is an array
#         },
#         {
#             "$project": {
#                 "_id": 1,
#                 "reports_info": "$reports.info"  # Adjust as needed based on your document structure
#             }
#         }
#     ]
#     return created_staff
async def add_staff(new_staff: Staffs, profile_image: Optional[UploadFile] = None) -> Staffs:
    # Handle image upload if provided
    if profile_image:
        # Save the uploaded image to the specified directory
        image_path = os.path.join(UPLOAD_DIRECTORY, profile_image.filename)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(profile_image.file, buffer)
        # Store the image path in the staff's profileImage field
        new_staff.profileImage = image_path

    # Create the new staff member in the database
    created_staff = await new_staff.create()

    # Aggregation pipeline to look up and project fields
    pipeline = [
        {
            "$lookup": {
                "from": "reports",  # Collection name as a string
                "localField": "reportTo",  # Field in the Staffs collection
                "foreignField": "_id",  # Field in the Reports collection
                "as": "reports"
            }
        },
        {
            "$unwind": "$reports"  # Unwind if `reports` is an array
        },
        {
            "$project": {
                "_id": 1,
                "reports_info": "$reports.info"  # Adjust as needed based on your document structure
            }
        }
    ]

    # Execute the aggregation on the staff collection
    staff_collection = Staffs.get_motor_collection()
    aggregation_result = staff_collection.aggregate(pipeline)
    
    async for result in aggregation_result:
        print(result)  # Handle the aggregation results as needed
    
    return created_staff

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

# async def retrieve_staffsq(name: Optional[str] = None, email: Optional[str] = None, mobile_number: Optional[str] = None) -> List[Staffs]:
#     query = {}

#     if name:
#         query['name'] = {'$regex': name, '$options': 'i'}  # Case-insensitive search
    
#     if email:
#         query['emailId'] = email
    
#     if mobile_number:
#         query['mobileNumber'] = mobile_number

#     staff = await Staffs.find(query).to_list()
#     return staff
# async def retrieve_staffsq(name: Optional[str] = None,
#                             email: Optional[str] = None,
#                             mobile_number: Optional[str] = None,
#                             page: int = 0,
#                             limit: int = 0 or 20) -> List[Staffs]:
#     query = {}

#     if name:
#         query['name'] = {'$regex': name, '$options': 'i'}  # Case-insensitive search
    
#     if email:
#         query['emailId'] = email
    
#     if mobile_number:
#         query['mobileNumber'] = mobile_number

#     page = max(1, page)
#     limit = max(1, limit)

#     skip = (page - 1) * limit if page > 0 else 0
#     staff_cursor = staff_collection.find(query).sort([("createdAt", 1), ("_id", 1)]).skip(skip).limit(limit)
#     staff = await staff_cursor.to_list(length=limit)
    
#     return staff
async def retrieve_staffsq(name: Optional[str] = None,
                           email: Optional[str] = None,
                           mobile_number: Optional[str] = None,
                           page: int = 0,
                           limit: int = 0 or 20) -> List[dict]:  # Returning list of dictionaries
    query = {}

    if name:
        query['name'] = {'$regex': name, '$options': 'i'}  # Case-insensitive search
    
    if email:
        query['emailId'] = email
    
    if mobile_number:
        query['mobileNumber'] = mobile_number

    page = max(1, page)
    limit = max(1, limit)

    skip = (page - 1) * limit if page > 0 else 0
    staff_cursor = staff_collection.find(query).sort([("createdAt", 1), ("_id", 1)]).skip(skip).limit(limit)
    staff_list = await staff_cursor.to_list(length=limit)

    # Process staff data to include image URLs
    for staff in staff_list:
        if 'profileImage' in staff and staff['profileImage']:
            image_path = staff['profileImage']
            # Convert file path to URL (you may need to adjust this based on your server setup)
            staff['profileImageUrl'] = f"/staff-images/{os.path.basename(image_path)}"

    return staff_list




# -------------------tasks----------------------------------

task_collection = TaskModel

async def add_task(new_task: TaskModel) -> TaskModel:
    task = await new_task.create()
    return task

async def retrieve_task(id: PydanticObjectId) -> TaskModel:
    task = await task_collection.get(id)
    if task:
        return task
    
async def retrieve_tasks() -> list[TaskModel]:
    task = await task_collection.all().to_list()
    return task

async def delete_task(id: PydanticObjectId) -> bool:
    task = await task_collection.get(id)
    if task:
        await task.delete()
        return True
    
async def update_task_data(id: PydanticObjectId, data: dict) -> Union[bool, TaskModel]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    task = await task_collection.get(id)
    if task:
        await task.update(update_query)
        return task
    return False

# async def retrieve_taskq(leadName: Optional[str] = None, priority: Optional[str] = None,
#                          startDate:Optional[str]= None,dueDate:Optional[str]= None,status:Optional[str]= None,
#                           description: Optional[str] = None) -> List[TaskModel]:
#     query = {}

#     if leadName:
#         query['leadName'] = {'$regex': leadName, '$options': 'i'}  # Case-insensitive search
    
#     if priority:
#         query['priority'] = priority

#     if startDate:
#         query['startDate'] = startDate

#     if dueDate:
#         query['dueDate'] = dueDate
    
#     if description:
#         query['description'] = description

#     if status:
#         query['status'] = status

#     task = await TaskModel.find(query).to_list()
#     return task

async def retrieve_taskq(leadName: Optional[str] = None, priority: Optional[str] = None,
                        startDate:Optional[str]= None,dueDate:Optional[str]= None,status:Optional[str]= None,
                        description: Optional[str] = None,
                        page: int = 1,
                        limit: int = 0 or 10) -> List[TaskModel]:
    query = {}

    if leadName:
        query['leadName'] = {'$regex': leadName, '$options': 'i'}  # Case-insensitive search
    
    if priority:
        query['priority'] = priority

    if startDate:
        query['startDate'] = startDate

    if dueDate:
        query['dueDate'] = dueDate
    
    if description:
        query['description'] = description

    if status:
        query['status'] = status

    skip = (page - 1) * limit
    task_cursor = task_collection.find(query).sort([("createdAt", 1), ("_id", 1)]).skip(skip).limit(limit)
    task = await task_cursor.to_list(length=limit)
    return task

# ==================department------------------------------

department_collection =Departments

async def add_department(new_department: Departments) -> Departments:
    department = await new_department.create()
    return department

async def retrieve_department(id: PydanticObjectId) -> Departments:
    department = await department_collection.get(id)
    if department:
        return department
    
async def retrieve_departments() -> list[Departments]:
    department = await department_collection.all().to_list()
    return department

async def delete_department(id: PydanticObjectId) -> bool:
    department = await department_collection.get(id)
    if department:
        await department.delete()
        return True
    
async def update_department_data(id: PydanticObjectId, data: dict) -> Union[bool, Departments]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    department = await department_collection.get(id)
    if department:
        await department.update(update_query)
        return department
    return False

# ------------------Jobtitles------------------------------

jobtitles_collection =Jobtitles

async def add_jobtitles(new_jobtitles: Jobtitles) -> Jobtitles:
    jobtitles = await new_jobtitles.create()
    return jobtitles

async def retrieve_jobtitle(id: PydanticObjectId) -> Jobtitles:
    jobtitles = await jobtitles_collection.get(id)
    if jobtitles:
        return jobtitles
    
async def retrieve_jobtitles() -> list[Jobtitles]:
    job = await jobtitles_collection.all().to_list()
    return job

async def delete_jobtitles(id: PydanticObjectId) -> bool:
    jobtitles = await jobtitles_collection.get(id)
    if jobtitles:
        await jobtitles.delete()
        return True
    
async def update_jobtitles_data(id: PydanticObjectId, data: dict) -> Union[bool, Jobtitles]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    jobtitles = await jobtitles_collection.get(id)
    if jobtitles:
        await jobtitles.update(update_query)
        return jobtitles
    return False

# -------------------industries--------------------------

industries_collection =Industries

async def add_industries(new_industries: Industries) -> Industries:
    industries = await new_industries.create()
    return industries

async def retrieve_industrie(id: PydanticObjectId) -> Industries:
    industries = await industries_collection.get(id)
    if industries:
        return industries
    
async def retrieve_industries() -> list[Industries]:
    industries = await industries_collection.all().to_list()
    return industries

async def delete_industrie(id: PydanticObjectId) -> bool:
    industries = await industries_collection.get(id)
    if industries:
        await industries.delete()
        return True
    
async def update_industries_data(id: PydanticObjectId, data: dict) -> Union[bool, Industries]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    industries = await industries_collection.get(id)
    if industries:
        await industries.update(update_query)
        return industries
    return False

# ---------------------emails-----------------------------

email_collection =Emails

async def add_email(new_email: Emails) -> Emails:
    email = await new_email.create()
    return email

async def retrieve_email(id: PydanticObjectId) -> Emails:
    email = await email_collection.get(id)
    if email:
        return email
    
async def retrieve_emails() -> list[Emails]:
    email = await email_collection.all().to_list()
    return email

async def delete_email(id: PydanticObjectId) -> bool:
    email = await email_collection.get(id)
    if email:
        await email.delete()
        return True
    
async def update_email_data(id: PydanticObjectId, data: dict) -> Union[bool, Emails]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    email = await email_collection.get(id)
    if email:
        await email.update(update_query)
        return email
    return False

# --------------------------sms------------------------------
sms_collection =Sms

async def add_sms(new_sms: Sms) -> Sms:
    sms = await new_sms.create()
    return sms

async def retrieve_sms(id: PydanticObjectId) -> Sms:
    sms = await sms_collection.get(id)
    if sms:
        return sms
    
async def retrieve_smses() -> list[Sms]:
    sms = await sms_collection.all().to_list()
    return sms

async def delete_sms(id: PydanticObjectId) -> bool:
    sms = await sms_collection.get(id)
    if sms:
        await sms.delete()
        return True
    
async def update_sms_data(id: PydanticObjectId, data: dict) -> Union[bool, Sms]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    sms = await sms_collection.get(id)
    if sms:
        await sms.update(update_query)
        return sms
    return False

# -------------------------reports------------------------------

reports_collection =Reports

async def add_reports(new_reports: Reports) -> Reports:
    reports = await new_reports.create()
    return reports

async def retrieve_report(id: PydanticObjectId) -> Reports:
    reports = await reports_collection.get(id)
    if reports:
        return reports
    
async def retrieve_reports() -> list[Reports]:
    reports = await reports_collection.all().to_list()
    return reports

async def delete_reports(id: PydanticObjectId) -> bool:
    reports = await reports_collection.get(id)
    if reports:
        await reports.delete()
        return True
    
async def update_reports_data(id: PydanticObjectId, data: dict) -> Union[bool, Reports]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    reports = await reports_collection.get(id)
    if reports:
        await reports.update(update_query)
        return reports
    return False

# ---------------------------roles------------------------------

roles_collection =Roles

async def add_role(new_role: Roles) -> Roles:
    role = await new_role.create()
    return role

async def retrieve_role(id: PydanticObjectId) -> Roles:
    role = await roles_collection.get(id)
    if role:
        return role
    
async def retrieve_roles() -> list[Roles]:
    role = await roles_collection.all().to_list()
    return role

async def delete_roles(id: PydanticObjectId) -> bool:
    role = await roles_collection.get(id)
    if role:
        await role.delete()
        return True
    
async def update_roles_data(id: PydanticObjectId, data: dict) -> Union[bool, Roles]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    role = await roles_collection.get(id)
    if role:
        await role.update(update_query)
        return role
    return False

# -----------------Countries----------------------
countries_collection =Countries

# async def add_countries(new_countries: Countries) -> Countries:
#     countries = await new_countries.create()
#     return countries

    
async def retrieve_countries() -> list[Countries]:
    countries = await countries_collection.all().to_list()
    return countries

