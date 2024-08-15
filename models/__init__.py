from models.admin import Admin
from models.student import Student
from models.user import User
from models.opts import OTP
from models.staff import Staffs
from models.lead import Leads
from models.lead_status import LeadStatus
from models.leadsours import LeadSource
from models.organizations import Organizations
from models.tasks import TaskModel
from models.departments import Departments
from models.jobtitles import Jobtitles
from models.industries import Industries
from models.emails import Emails
from models.sms import Sms
from models.reports import Reports
from models.roles import Roles
from models.countries import Countries

__all__ = [Student, Admin, User, OTP, Staffs, Industries, Leads, TaskModel,Sms,
            Organizations, LeadStatus, LeadSource, Departments, Jobtitles, Emails,
            Reports,Roles,Countries]
