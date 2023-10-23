from ApiClass import Pixegami
import pytest

api = Pixegami()


@pytest.fixture
def bulid_up():
    payload = Pixegami.newPayload()
    data = api.create_task(payload)
    return data


def test_can_open():
    data = api.get_root()
    assert data.status_code == 200


def test_can_create_task(bulid_up):
    assert bulid_up.status_code == 200
    task_id = bulid_up.json()[api.taskBody][api.taskID]
    response = api.get_task(task_id)
    assert response.status_code == 200


def test_can_get_task_list():
    n = 3
    payload = Pixegami.newPayload()
    create_response = None
    for i in range(n):
        create_response = api.create_task(payload)
        assert create_response.status_code == 200
    data = api.get_task_list(create_response.json()[api.taskBody][api.userID])
    assert len(data.json()[api.tasksList]) == n


def test_can_update_task(bulid_up):
    assert bulid_up.status_code == 200
    userid = bulid_up.json()[api.taskBody][api.userID]
    taskid = bulid_up.json()[api.taskBody][api.taskID]
    response = api.update_task(taskid, userid)
    assert response.status_code == 200
    updated_data = api.get_task(taskid)
    assert updated_data.status_code == 200
    assert bulid_up.json()[api.taskBody][api.content] != updated_data.json()[
        api.content]
    assert bulid_up.json()[api.taskBody][api.userID] == updated_data.json()[
        api.userID]


def test_can_delete_task(bulid_up):
    assert bulid_up.status_code == 200
    taskId = bulid_up.json()[api.taskBody][api.taskID]
    del_response = api.delete_task(taskId)
    assert del_response.status_code == 200
    get_response = api.get_task(taskId)
    assert get_response.status_code == 404
