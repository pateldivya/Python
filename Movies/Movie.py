import webbrowser
class Movie():
    def __init__(self, title, story, image, trailer):
        self.title = title
        self.story = story
        self.image = image
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
