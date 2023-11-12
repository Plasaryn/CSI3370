from CalendarEvent import CalendarEvent

class PtoCalendar:
  def __init__(self) -> None:
    self.events = [] #list[CalendarEvent]

  def getCalendarEvents(self) -> list[CalendarEvent]:
    return self.events

  def getCalendarEvent(self, id: int) -> CalendarEvent:
    event_ids = self.__get_event_ids()
    for event_id, event in zip(event_ids, self.events):
      if event_id == id: 
        return event

  def addEvent(self, event: CalendarEvent) -> None:
    self.events.append(event)

  def removeEvent(self, id:int):
    event_ids = self.__get_event_ids()
    for event_id, event in zip(event_ids, self.events):
      if event_id == id: 
        self.events.remove(event)


  def __get_event_ids(self) -> list[int]:
    return [x.getId() for x in self.events]

  