import time
import random
from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Task

logger = get_task_logger(__name__)

@shared_task(bind=True)
def process_task(self, task_id):
    """
    Generic function to process tasks
    """
    try:
        # Get the task from database
        db_task = Task.objects.get(id=task_id)
        
        # Update task with celery task id
        db_task.celery_task_id = self.request.id
        db_task.save()
        
        # Mark task as started
        db_task.mark_as_started()
        logger.info(f"Started processing task {task_id}")
        
        # Switch based on task type for specific processing
        result = None
        if db_task.task_type == 'data_processing':
            result = process_data(db_task)
        elif db_task.task_type == 'email_campaign':
            result = send_email_campaign(db_task)
        elif db_task.task_type == 'report_generation':
            result = generate_report(db_task)
        else:
            # Default processing for other task types
            result = generic_processing(db_task)
        
        # Mark task as completed
        db_task.mark_as_completed(result=result)
        logger.info(f"Successfully completed task {task_id}")
        return result
        
    except Exception as e:
        logger.error(f"Error processing task {task_id}: {str(e)}")
        try:
            db_task = Task.objects.get(id=task_id)
            db_task.mark_as_failed(error=str(e))
        except:
            pass
        raise

def process_data(task):
    """
    Simulate data processing
    """
    logger.info(f"Processing data for task {task.id}")
    processing_time = random.randint(5, 15)
    time.sleep(processing_time)
    return f"Data processed successfully in {processing_time} seconds"

def send_email_campaign(task):
    """
    Simulate sending email campaign
    """
    logger.info(f"Sending email campaign for task {task.id}")
    num_emails = random.randint(10, 100)
    processing_time = random.randint(5, 20)
    time.sleep(processing_time)
    return f"Email campaign sent to {num_emails} recipients in {processing_time} seconds"

def generate_report(task):
    """
    Simulate report generation
    """
    logger.info(f"Generating report for task {task.id}")
    processing_time = random.randint(10, 30)
    time.sleep(processing_time)
    return f"Report generated successfully in {processing_time} seconds"

def generic_processing(task):
    """
    Generic task processing
    """
    logger.info(f"Generic processing for task {task.id}")
    processing_time = random.randint(3, 10)
    time.sleep(processing_time)
    return f"Generic task processed in {processing_time} seconds"