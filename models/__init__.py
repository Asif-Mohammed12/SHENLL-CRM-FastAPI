from models.admin import Admin
from models.student import Student
from models.user import User
from models.opts import OTP
from models.staff import Staffs
from models.lead import Leads
from models.lead_status import LeadStatus
from models.leadsours import LeadSource
from models.organizations import Organizations
# from models.task import Tasks

__all__ = [Student, Admin, User, OTP, Staffs, Leads,
            Organizations, LeadStatus, LeadSource]
