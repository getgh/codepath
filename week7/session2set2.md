# Problem Set Version 2
# Problem 2: Identify Longest Episode
# Space Complexity: O(1) : only storing variable (longest) to keep track of the current maximum
# Time Complexity: O(n) : The function iterates through the list
def identify_longest_episode(durations):
    if not durations:
        return None
    
    longest = durations[0]
    
    for duration in durations:
        if duration > longest:
            longest = duration
            
    return longest

print(identify_longest_episode([30, 45, 60, 45, 30]))
print(identify_longest_episode([20, 30, 40, 40, 30, 20]))  
print(identify_longest_episode([55, 60, 55, 60, 60])) 


# Problem 4: Find Median Episode Length
# Space Complexity: O(n) : needed a new list to store the ordered elements
# Time Complexity: O(nlogn) :  Used python’s built-in sorted() function which has a time complexity of O(n log n)

def find_median_episode_length(durations):
    if not durations:
        return 0
    
    sorted_durations = sorted(durations)
    n = len(sorted_durations)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_durations[mid - 1] + sorted_durations[mid]) / 2.0
    else:
        return sorted_durations[mid]

print(find_median_episode_length([45, 30, 60, 30, 90])) 
print(find_median_episode_length([90, 80, 60, 70, 50]))
print(find_median_episode_length([30, 10, 20, 40, 30, 50])) 

# Problem 6: Find Recent Podcast Episodes
# Space Complexity: O(n) : a new list containing n elements
# Time Complexity: O(n) : The function iterates through the list

def get_recent_episodes(episodes, n):
    count = min(len(episodes), n)
    return episodes[-count:][::-1]

episodes1 = ['episode1', 'episode2', 'episode3', 'episode4']
n = 3
print(get_recent_episodes(episodes1, n))

episodes2 = ['ep1', 'ep2', 'ep3']
n = 2
print(get_recent_episodes(episodes2, n))

episodes3 = ['a', 'b', 'c', 'd']
n = 5
print(get_recent_episodes(episodes3, n))




# Problem 8: Find Longest Consecutive Listen Gaps
# Space Complexity: O(1) : needed fixed amount of extra space to store the max_gap and the loop index i
# Time Complexity: O(n) : The function iterates through the list
def find_longest_gap(timestamps):
    if len(timestamps) < 2:
        return 0
    
    max_gap = 0
    
    for i in range(1, len(timestamps)):
        current_gap = timestamps[i] - timestamps[i-1]        
        if current_gap > max_gap:
            max_gap = current_gap
            
    return max_gap

timestamps1 = [30, 50, 70, 100, 120, 150]
print(find_longest_gap(timestamps1))

timestamps2 = [10, 20, 30, 50, 60, 90]
print(find_longest_gap(timestamps2))

timestamps3 = [5, 10, 15, 25, 35, 45]
print(find_longest_gap(timestamps3))
