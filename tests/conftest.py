import dramatiq
import pytest
from dramatiq import Worker


@pytest.fixture
def broker():
    broker = dramatiq.get_broker()
    yield broker
    broker.flush_all()


@pytest.fixture
def worker(broker):
    worker = Worker(broker, worker_timeout=100)
    worker.start()
    yield worker
    worker.stop()
