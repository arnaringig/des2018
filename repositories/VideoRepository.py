#This is the VideoRepository class
#It has a constructor and method that knows how to write a Video object to a file
import sys
sys.path.append("..")
from models.Video import Video

class VideoRepository:
	def __init__(self):
		self.__videos = []

	def add_video(self, video):
		with open("./data.videos.txt", "a+") as videos_file:
			title = video.get_title()
			genre = video.get_genre()
			length = video.get_length()
			videos_file.write("{},{},{}\n".format(title, genre, length))

	def get_videos(self):
		videos = []
		with open(".././data/videos.txt", "r") as video_file:
				for line in video_file.readlines():
					title, genre, length = line.split(",")
					new_video = Video(title, genre, length)
					videos.append(new_video)

		return videos

def main():
	video_repo = VideoRepository()
	videos = video_repo.get_videos()
	print("jkh")
	print(videos)

main()


