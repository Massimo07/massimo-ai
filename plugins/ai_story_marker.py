# ai_story_marker.py
"""
Story Marker AI: segna, evidenzia, archivia e narra eventi chiave della vita/azienda/brand.
Timeline, milestone, highlight, storie e archivi digitali.
"""

class StoryMarkerAI:
    def __init__(self):
        self.stories = []

    def add_event(self, title, description, date):
        self.stories.append({"title": title, "desc": description, "date": date})

    def get_timeline(self):
        return sorted(self.stories, key=lambda x: x["date"])
