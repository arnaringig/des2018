from services.VideoService import videoService
from models.Video import Video

class SalesmanUi:

	def __init__(self):

		action = ""
		while(action != "a"):
			print("You can do the following: ")
			print("2. Add a video")
			print("press q to quit")

			action = input("Choose an option: ").lower()

			if action == "1":
				title = input("Movie title: ")
				genre = input("Genre: ")
				length = input("Length in minutes: ")
				new_video = Video(title, genre, length)
				self.__video_service.add_video(new_video)