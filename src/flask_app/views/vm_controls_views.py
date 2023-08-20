from controllers import vm_controls_controllers
from flask import Blueprint, abort, jsonify, request, send_file, send_from_directory

vm_controls_page = Blueprint('vm_controls_page', __name__)

rabbit_controller = vm_controls_controllers.SendMessageRabbitController()


@vm_controls_page.route("/createVm", methods=['POST'])
def createVm():
    print("creatVm called")

    try:
        rabbit_controller.create_vm()
        print("message was sent")
    except Exception as exception:
        print("error sending message: {}".format(exception))

    return "200"


# старт конкретной машины пока невозможен тк на фронте такое не реализовано и не будет без Vue.js
@vm_controls_page.route("/startVm", methods=['POST'])
def startVm():
    print("starVm called")

    try:
        rabbit_controller.start_vm()
        print("message was sent")
    except Exception as exception:
        print("error sending message: {}".format(exception))

    return "200"


# аналогично старту
@vm_controls_page.route("/stopVm", methods=['POST'])
def stopVm():
    print("stopVm called")

    try:
        rabbit_controller.stop_vm()
        print("message was sent")
    except Exception as exception:
        print("error sending message: {}".format(exception))

    return "200"


# аналогично старту
@vm_controls_page.route("/snapshotVm", methods=['POST'])
def snapshotVm():
    print("snapshotVm called")

    try:
        rabbit_controller.stop_vm()
        print("message was sent")
    except Exception as exception:
        print("error sending message: {}".format(exception))

    return "200"
