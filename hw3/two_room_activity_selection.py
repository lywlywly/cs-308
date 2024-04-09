class Activity:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def two_room_activity_selection(activities: list[Activity]):
    activities.sort(key=lambda x: x.end)  # Sort activities by ending time
    A1 = [Activity(-100, -100)]  # Activities assigned to room 1
    A2 = [Activity(-100, -100)]  # Activities assigned to room 2
    for activity in activities:
        if activity.start < A1[-1].end and activity.start < A2[-1].end:
            continue
        elif activity.start >= A1[-1].end and activity.start < A2[-1].end:
            A1.append(activity)
        elif activity.start < A1[-1].end and activity.start >= A2[-1].end:
            A2.append(activity)
        elif activity.start >= A1[-1].end and activity.start >= A2[-1].end:
            if A1[-1].end >= A2[-1].end:
                A1.append(activity)
            else:
                A2.append(activity)

    return A1[1:], A2[1:]  # return activities after the dummy activity


# Example usage:
activities = [
    Activity(1, 4),
    Activity(3, 5),
    Activity(0, 6),
    Activity(5, 7),
    Activity(3, 9),
    Activity(5, 9),
    Activity(6, 10),
    Activity(8, 11),
    Activity(8, 12),
    Activity(2, 14),
    Activity(12, 16),
]
A1, A2 = two_room_activity_selection(activities)
# Print the selected activities for each room
print("Activities for Room 1 (A1):")
for activity in A1:
    print(f"Start: {activity.start}, End: {activity.end}")
print("\nActivities for Room 2 (A2):")
for activity in A2:
    print(f"Start: {activity.start}, End: {activity.end}")
