from .Approval import ApprovalInterface
from .BusinessObject import BusinessObjectInterface
from .Core import CoreInterface
from .Forms import FormsInterface
from .Lifecycle import LifecycleInterface
from .OneStepActions import OneStepActionsInterface
from .Queues import QueuesInterface
from .Searches import SearchesInterface
from .Security import SecurityInterface
from .Service import ServiceInterface
from .Teams import TeamsInterface
from .Users import UsersInterface


class GeneratedInterfaces(
    ApprovalInterface,
    BusinessObjectInterface,
    CoreInterface,
    FormsInterface,
    LifecycleInterface,
    OneStepActionsInterface,
    QueuesInterface,
    SearchesInterface,
    SecurityInterface,
    ServiceInterface,
    TeamsInterface,
    UsersInterface,
):
    pass
