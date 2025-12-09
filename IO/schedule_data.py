import csv
from Models.models import Schedule


class ScheduleData:
    def __init__(self) -> None:
        self.schedule_file_path = "Data/schedule.csv"

    def get_schedule_data(self):  # ->  LIST AF SCHEDULE
        """Returns list of all schedule data."""
        schedules = []

        # TODO

        # with open(self.schedule_file_path, "r", encoding = "utf-8") as file:
        #     reader = csv.reader(file)
        #     # skip header row if present
        #     next(reader, None)
        #
        #     for line in reader:
        #         schedule_id = int(line[0])
        #         match_id = int(line[1])
        #         start_time = datetime.fromisoformat(line[2])
        #         venue = line[3]
        #
        #         schedule = Schedule(
        #             id = schedule_id,
        #             match_id = match_id,
        #             start_time = start_time,
        #             venue = venue
        #         )
        #         schedules.append(schedule)
        #
        #     return schedules

    def store_schedule_data(self, matches: list[Schedule]) -> list[Schedule]:
        """Stores all schedule data to CSV and returns the list that was stored."""
        with open(self.schedule_file_path, "w", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["id", "match_id", "start_time", "venue"])

            # TODO
            # for schedule in matches:
            #     writer.writerow(
            #         [
            #             schedule.id,
            #             schedule.match_id,
            #             schedule.start_time.isoformat(),
            #             schedule.venue,
            #         ]
            #     )

        return matches

