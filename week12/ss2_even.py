# # Problem 2: Finding Tour Dates (Set Version 2)
# def can_attend(tour_dates, available):
#     def helper(low, high):
#         if low > high:
#             return False
        
#         mid = (low + high) // 2
        
#         if tour_dates[mid] == available:
#             return True
#         elif tour_dates[mid] > available:
#             return helper(low, mid - 1)
#         else:
#             return helper(mid + 1, high)

#     return helper(0, len(tour_dates) - 1)

# print(can_attend([1, 3, 7, 10, 12], 12))
# print(can_attend([1, 3, 7, 10, 12], 5))














# # Problem 4: Granting Backstage Access (Set Version 2)
# def get_group_sum(group_sizes, room_capacity):
#     group_sizes.sort()
#     max_sum = -1
#     n = len(group_sizes)

#     for i in range(n):
#         current_group = group_sizes[i]
        
#         target = room_capacity - current_group - 1
        
#         low, high = 0, n - 1
#         best_partner_idx = -1
        
#         while low <= high:
#             mid = (low + high) // 2
#             if group_sizes[mid] <= target:
#                 if mid != i:
#                     best_partner_idx = mid
#                 low = mid + 1
#             else:
#                 high = mid - 1
        
#         if best_partner_idx != -1:
#             max_sum = max(max_sum, current_group + group_sizes[best_partner_idx])
            
#     return max_sum
# print(get_group_sum([1,20,10,14,3,5,4,2], 12))
# print(get_group_sum([10,20,30], 15))









# # Problem 6: Merge Sort Playlist (Set Version 2)
# def merge_sort_helper(left_arr, right_arr):
#     result = []
#     i = 0  
#     j = 0 
    
#     while i < len(left_arr) and j < len(right_arr):
#         if left_arr[i] < right_arr[j]:
#             result.append(left_arr[i])
#             i += 1
#         else:
#             result.append(right_arr[j])
#             j += 1
            
#     result.extend(left_arr[i:])
#     result.extend(right_arr[j:])
    
#     return result

# def merge_sort_playlist(playlist):
#     if len(playlist) <= 1:
#         return playlist

#     mid = len(playlist) // 2
#     left_half = playlist[:mid]
#     right_half = playlist[mid:]
    
#     sorted_left = merge_sort_playlist(left_half)
#     sorted_right = merge_sort_playlist(right_half)
    
#     return merge_sort_helper(sorted_left, sorted_right)

# print(merge_sort_playlist(["Formation", "Crazy in Love", "Halo"]))
# print(merge_sort_playlist(["Single Ladies", "Love on Top", "Irreplaceable"]))
