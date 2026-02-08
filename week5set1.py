# Problem Set Version 1
# Problem 1: Festival Lineup
def lineup(artists, set_times):
    d={}
    for _ in range(len(artists)):
        d[artists[_]]=set_times[_]
    return d

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

# Problem 3: Ticket Sales
def total_sales(ticket_sales):
    s=0
    for v in ticket_sales.values():
        s+=v
    return s

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))


# Problem 5: Best Set
def best_set(votes):
    l=[]
    for v in votes.values():
        l.append(v)
    d={}
    for i in range(1,len(votes)+1):
        d[i]=set()
    for i in l:
        if l.count(i) in d:
            d[l.count(i)].add(i)
    for key in range(len(votes), 0, -1):
        if d[key]:
            return ', '.join((d[key]))


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))


# Problem 7: Performances with Maximum Audience II
def max_audience_performances(audiences):
    high=max(audiences)
    d={}
    d[high]=audiences.count(high)*high
    return d[high]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

# Problem 9: Stage Arrangement Difference Between Two Performances
def find_stage_arrangement_difference(s, t):
    pos_map = {p: i for i, p in enumerate(s)}
    total_diff = 0

    for i, p in enumerate(t):
        total_diff += abs(pos_map[p] - i)

    return total_diff

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))

# Problem 11: Performer Schedule Pattern
def schedule_pattern(pattern, schedule):
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))
