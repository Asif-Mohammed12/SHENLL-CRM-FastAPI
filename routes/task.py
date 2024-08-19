from fastapi import APIRouter, Body, Query
from database.database import *
from schemas.task import Response, UpdateTasks


router = APIRouter()

@router.get("/by", response_description="Tasks retrieved", response_model=Response)
async def get_tasks():
    task = await retrieve_tasks()
    return Response(
        status_code=200,
        status="ok",
        message="Tasks record(s) found",
        data=task
    )

@router.get("/{id}", response_description="Task data retrieved", response_model=Response)
async def get_task_data(id: PydanticObjectId):
    task = await retrieve_task(id)
    if task:
        return Response(
        status_code=200,
        status="ok",
        message="Tasks record(s) found",
        data=task
    )
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Task doesn't exist",
    }



@router.post("/", response_description="Task created", response_model=Response)
async def add_new_task(new_task: TaskModel = Body(...)):
    task = await add_task(new_task)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Task record(s) created",
        "data": {
            "_id": str(task.id),
            "createdAt": task.createdAt
        
        },
    }

@router.put("/{id}", response_model=Response)
async def update_task(id: PydanticObjectId, req: UpdateTasks = Body(...)):
    updated_task = await update_task_data(id, req.dict())
    if updated_task:
        return {
            "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Task record(s) created",
        "data": {
            "_id": str(updated_task.id),
            "updatedAt": updated_task.updatedAt
        
        },
        }
    return Response(
            status_code=400,
            status="error",
            message="Bad request"       
    )

@router.delete("/{id}", response_description="Task data deleted from the database")
async def delete_task_data(id: PydanticObjectId):
    deleted_task = await delete_task(id)
    if deleted_task:
        return {
            "status_code": 200,
            "status": "ok",
            "message": "Task data retrieved successfully",
            "data": deleted_task,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Leads with id {0} doesn't exist".format(id),
        "data": False,
    }

@router.get("/", response_description="Task retrieved", response_model=Response)
async def get_task(
    page: int = Query(1), limit: int = Query(5),
    leadName: Optional[str] = Query(None, description="Filter by task leadName"),
    priority: Optional[str] = Query(None, description="Filter by task priority"),
    startDate: Optional[str] = Query(None, description="Filter by task startDate"),
    dueDate: Optional[str] = Query(None, description="Filter by task dueDate"),
    status: Optional[str] = Query(None, description="Filter by task status"),
    description: Optional[str] = Query(None, description="Filter by task description")
):
    task = await retrieve_taskq(leadName=leadName, priority = priority, startDate =startDate, dueDate=dueDate, status=status,
                                 description=description,page=page,limit=limit)
    return {
        "status_code": 200,
        "status": "ok",
        "response_type": "success",
        "message": "Task record(s) found",
        "data": task,
    }