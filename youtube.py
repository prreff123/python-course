from pytube import YouTube

video_link = 'https://youtu.be/BddP6PYo2gs'
video = YouTube(video_link)

video.streams.filter(res='720p').first().download('E:\\Videos')

# def find_max(nums):
#     max_num = float("-inf")
#     for num in nums:
#         if num > max_num:
#           max_num += num 
#     return max_num        