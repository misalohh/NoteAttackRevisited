import pygame
from UI.Button import Button
from colours import BACKGROUND, TEXT

class Leaderboard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 105)
        self.smaller_font = pygame.font.Font('assets/Handwriting-Regular.ttf', 70)
        self.score_font = pygame.font.Font('assets/JMH Typewriter-Thin.ttf', 45)
        self.back_button = Button(35, 35, 120, 60, "Back")

    def update(self):
        self.highscores = self.load_highscores()  # Refresh the highscores each time the screen is updated

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        leaderboard_title = self.font.render("Leaderboard", True, TEXT)
        text_rect = leaderboard_title.get_rect(midtop=(self.width // 2, 50))
        surface.blit(leaderboard_title, text_rect)
        self.back_button.draw(surface, mouse_pos)

        if not self.highscores:
            no_scores_text = self.smaller_font.render("No scores yet!", True, TEXT)
            text_rect = no_scores_text.get_rect(midtop=(self.width // 2, 200))
            surface.blit(no_scores_text, text_rect)
            return

        height = 150
        for i, score in enumerate(self.highscores):
            score_text = self.score_font.render(f"{i + 1}.  {score}", True, TEXT)
            text_rect = score_text.get_rect(midtop=(self.width // 2 - 120, height))
            surface.blit(score_text, text_rect)
            height += 60

    
    def handle_click(self, mouse_pos):
        if self.back_button.is_clicked(mouse_pos):
            return "menu"

    def load_highscores(self):
        try:
            with open("leaderboard.txt", "r") as file:
                highscores = [int(line.strip()) for line in file.readlines()]
                return sorted(highscores, reverse=True)[:5]  # Return top 5 scores
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist