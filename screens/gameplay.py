import pygame
import random

from colours import BACKGROUND, TEXT
from sprites.Laser import Laser
from sprites.Player import Player
from sprites.Enemies import Enemy
from UI.Button import Button

class Gameplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.centre = (width // 2, height // 2)
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 170)
        self.score_text_font = pygame.font.Font('assets/Handwriting-Regular.ttf', 80)
        self.score_font = pygame.font.Font('assets/JMH Typewriter-Thin.ttf', 45)

        self.back_button = Button(35, 35, 120, 60, "Back")
        self.player = Player(width // 2, height // 2) 
        self.lasers = []
        self.score = 0

        self.enemies = pygame.sprite.Group()
        self.spawn_timer = 0
        self.spawn_interval = 150
        self.spawn_buffer = 0.3 # a buffer to prevent spamming lasers, in seconds
        self.last_spawn_time = 0

        self.game_over = False

        self.midi_input = None  # This will be set externally if MIDI input is available

        self.MIDI_NOTE_TO_LETTER = {
            0: 'C', 1: 'C', 2: 'D', 3: 'D', 4: 'E', 5: 'F',
            6: 'F', 7: 'G', 8: 'G', 9: 'A', 10: 'A', 11: 'B',
        }

        self.KEY_TO_NOTE = {
            pygame.K_a: 'A',
            pygame.K_b: 'B',
            pygame.K_c: 'C',
            pygame.K_d: 'D',
            pygame.K_e: 'E',
            pygame.K_f: 'F',
            pygame.K_g: 'G',
        }

    def end_game(self):
        self.enemies.empty()
        self.lasers.clear()
        self.spawn_timer = 0
        self.game_over = True

    def start_game(self):
        self.enemies.empty()
        self.lasers.clear()
        self.spawn_timer = 0
        self.game_over = False
        self.score = 0

    def update(self):
        if self.game_over:
            return

        if self.last_spawn_time > 0:
            self.last_spawn_time -= 1 / 60
        
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            note = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
            enemy = Enemy(self.width, self.height, target_pos=self.centre, note=note)
            self.enemies.add(enemy)

        self.enemies.update()

        for enemy in self.enemies:
            if enemy.check_collision(self.player):
                if self.is_highscore(self.score):
                    self.save_highscore(self.score)
                self.end_game()
                break  # Exit the loop if the game is over

        for laser in self.lasers:
            laser.update()

        enemies_to_remove = []
        lasers_to_remove = []

        for laser in self.lasers:
            for enemy in self.enemies:
                if enemy not in enemies_to_remove and enemy.check_collision(laser) and enemy.note == laser.note:
                    enemies_to_remove.append(enemy)
                    lasers_to_remove.append(laser)
                    self.score += 1
                    break   # this laser already matched an enemy, stop checking others

        for enemy in enemies_to_remove:
            self.enemies.remove(enemy)
        for laser in lasers_to_remove:
            self.lasers.remove(laser)
           
        self.lasers = [laser for laser in self.lasers if not laser.finished]

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        self.back_button.draw(surface, mouse_pos)

        if not self.game_over:
            self.player.draw(surface)
            
            for laser in self.lasers:
                laser.draw(surface)

            for enemy in self.enemies:
                enemy.draw(surface)

        score_text = self.score_text_font.render("Score:", True, TEXT)
        text_rect = score_text.get_rect(topright=(self.width - 100, 50))
        surface.blit(score_text, text_rect)

        actual_score = self.score_font.render(str(self.score), True, TEXT)
        surface.blit(actual_score, (self.width - 50 - actual_score.get_width(), 50))

        if self.game_over:
            if self.is_highscore(self.score):
                highscore_text = self.score_text_font.render("New Highscore!" , True, TEXT)
                text_rect2 = highscore_text.get_rect(center=(self.width // 2, self.height // 2 + 100))
                surface.blit(highscore_text, text_rect2)
            game_over_text = self.font.render("Game Over!" , True, TEXT)
            text_rect1 = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            surface.blit(game_over_text, text_rect1)

    def handle_click(self, mouse_pos):
            if self.back_button.is_clicked(mouse_pos):
                self.end_game()
                return "menu"

    def midi_note_to_letter(self, note_number):
        return self.MIDI_NOTE_TO_LETTER[note_number % 12]

    def poll_midi(self):
        if self.midi_input and self.midi_input.poll():
            for event in self.midi_input.read(10):  # Read up to 10 events at once
                status, note_number, velocity, _ = event[0]
                if status == 144 and velocity > 0:  # Note on event
                    note_letter = self.midi_note_to_letter(note_number)
                    self.handle_midi_note_on(note_letter)

    def fire_laser(self, note):
        if self.last_spawn_time <= 0:
            self.lasers.append(Laser(self.centre[0], self.centre[1], note=note))
            self.last_spawn_time = self.spawn_buffer

    def handle_key(self, key):
        if key in self.KEY_TO_NOTE:
            self.fire_laser(self.KEY_TO_NOTE[key])

    def handle_midi_note_on(self, note_letter):
        self.fire_laser(note_letter)

    def is_highscore(self, score):
        try:
            with open("leaderboard.txt", "r") as f:
                highscores = [int(line.strip()) for line in f.readlines()]
        except FileNotFoundError:
            highscores = []

        if len(highscores) < 5 or score > min(highscores):
            return True
        return False

    def save_highscore(self, score):
        try:
            with open("leaderboard.txt", "r") as f:
                highscores = [int(line.strip()) for line in f.readlines()]
        except FileNotFoundError:
            highscores = []

        highscores.append(score)
        highscores = sorted(highscores, reverse=True)[:10]

        with open("leaderboard.txt", "w") as f:
            for score in highscores:
                f.write(f"{score}\n")
