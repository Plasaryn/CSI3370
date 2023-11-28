from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    @abstractmethod
    def updaye(self, subject: Subject) -> None:
        pass
