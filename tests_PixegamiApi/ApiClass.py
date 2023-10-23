import uuid
import requests

# Class definition of api endpoints.
# If somthing change in API structure its one point change wihout need to refactor whole code


class Pixegami:
    def __init__(self) -> None:
        self.root = 'https://todo.pixegami.io/'
        self.createTask = self.root + 'create-task'
        self.getTask = self.root + 'get-task/'  # + task_id
        self.getTaskList = self.root + 'list-tasks/'  # + user_id
        self.updateTask = self.root + 'update-task'
        self.deleteTask = self.root + 'delete-task/'  # + task_id

        # Json Locators
        self.taskBody = 'task'
        self.taskID = 'task_id'
        self.content = 'content'
        self.userID = 'user_id'
        self.tasksList = 'tasks'

# Method used to generate uniqe test data

    @staticmethod
    def newPayload():
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"content_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False,
        }

    def get_root(self):
        response = requests.get(self.root)
        return response

    def create_task(self, payload):
        create_response = requests.put(
            self.createTask, json=payload)
        return create_response

    def get_task(self, task_id):
        get_response = requests.get(self.getTask+task_id)
        return get_response

    def get_task_list(self, user_id):
        get_list_response = requests.get(self.getTaskList+user_id)
        return get_list_response

    def update_task(self, task_id, user_id):
        new_payload = Pixegami.newPayload()
        update_response = requests.put(self.updateTask, json={
            "content": new_payload["content"],
            "user_id": user_id,
            "task_id": task_id,
            "is_done": False
        })
        return update_response

    def delete_task(self, task_id):
        delete_response = requests.delete(self.deleteTask+task_id)
        return delete_response
