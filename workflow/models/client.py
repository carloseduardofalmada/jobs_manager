from clients.models.client import Client as BaseClient, Supplier as BaseSupplier


class Client(BaseClient):
    class Meta:
        proxy = True

class Supplier(BaseSupplier):
    """
    A Supplier is simply a Client with additional semantics.
    """

    class Meta:
        proxy = True
