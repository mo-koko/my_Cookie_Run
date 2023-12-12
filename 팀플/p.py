import arcade
import random
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Run Game"







class hero(arcade.Sprite):
    
    def __init__(self, character_img):
        super().__init__(character_img)
        
        self.center_x = self.width      # center_x, center_y는 내장 인스턴스
        self.center_y = 100
        self.to_x = 0
        self.to_y = 0
        self.jump_count = 0
        self.character_stand_img = "character.png"
        
        
    def update(self): # 움직일 때 위치값 설정
        self.center_x += self.to_x      #to_x or to_y = parameter
        self.center_y += self.to_y



    def jump(self):     # jump count, y_pos
        
        if self.jump_count < 2:
            self.to_y = 26
            self.jump_count += 1
            
    
    def rotate(self):       # 점프 시 회전
        self.angle = 0

    def fly(self):
        self.to_y = 0


class huddle(arcade.Sprite):
    
    
    def __init__(self, wall):
        super().__init__(wall)
        
        self.speed = 8
        self.center_x = SCREEN_WIDTH + 500
        self.center_y = SCREEN_HEIGHT - (self.height // 2)
        self.to_x = self.speed 
    

    def update(self):
        self.center_x -= self.to_x
    
    def rotate(self):
        self.angle = -20






class fast(arcade.Sprite):
    
    def __init__(self, fast_item):
        super().__init__(fast_item)
        
        self.speed = 4
        self.center_x = SCREEN_WIDTH * random.randrange(4,6)      # item_pos
        self.center_y = 200
        self.to_y = 2
    
    
    def update(self):
        self.center_y += self.to_y
        self.center_x -= self.speed     #speed
    


class big(arcade.Sprite):
    def __init__(self, big_item):
        super().__init__(big_item)
        
        self.speed = 4
        self.center_x = SCREEN_WIDTH //2 #* random.randrange(4,7)        # item_pos
        self.center_y = 200
        self.to_y = 2
        

    def update(self):
        self.center_y += self.to_y
        self.center_x -= self.speed      #speed



class vatility(arcade.Sprite):      # life item
    def __init__(self, vatility_item):
        super().__init__(vatility_item)
        
        self.speed = 4
        self.center_x = SCREEN_WIDTH * random.randrange(4,7)
        self.center_y = 200
        self.to_y = 2
    
    
    def update(self):
        self.center_y += self.to_y
        self.center_x -= self.speed      #speed



class heart(arcade.Sprite):
    def __init__(self, life):
        super().__init__(life)
        
        
        self.center_x = 0 + self.width // 2
        self.center_y = SCREEN_HEIGHT - (self.height )
        self.to_x = 0.1
    
    
    def update(self):
        self.center_x -= self.to_x




class Game(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    
    
    def setup(self):


        # img load
        
        # character
        self.character_img = "character.png"       
        self.character = hero(self.character_img)
        
        self.ga = 0.6
        self.gravity = 1.2
        self.gravity += self.ga
        
        
        # obstacle
        self.wall_img = "기둥 장애물.png"
        self.wall = huddle(self.wall_img)
        
        
        
        
        # fast_item
        self.fast_item_img = "heart.png"
        self.fast_item = fast(self.fast_item_img)
        
        
        # big_item
        self.big_item_img = "sky_item.png"
        self.big_item = big(self.big_item_img)
        
        
        # vitality_item
        self.vitality_item_img = "sky_heart.png"
        self.vitality_item = vatility(self.vitality_item_img)
        
        
        # life
        self.life_img = "생명력.png"
        self.life = heart(self.life_img)




        # background        img object
        background_image = "맵.jpg"
        self.background = arcade.load_texture(background_image)
        self.back_x1 = SCREEN_WIDTH // 2
        self.back_move = 8
        self.back_x1 -= self.back_move
        self.back_y1 = SCREEN_HEIGHT // 2
        

        self.background2 = arcade.load_texture(background_image)
        self.back_x2 = SCREEN_WIDTH *1.5
        self.back_y2 = SCREEN_HEIGHT // 2

        self.acc = 1
        self.acc += self.acc        
        
        
        # ground        img object
        ground_image = "ground.png"
        self.ground_texture = arcade.load_texture(ground_image)       
        self.ground_y = SCREEN_HEIGHT // 2  
        
        
        
        # bgm
        self.bgm = None
        self.is_playing_bgm = False

        self.is_fast = 0
        self.is_large = 0
        self.flying = 20

    def on_draw(self):      #draw object
        arcade.start_render()

        
        # background        self.x, self.y, width, height, object
        arcade.draw_texture_rectangle(self.back_x1, self.back_y1 , SCREEN_WIDTH + 40, SCREEN_HEIGHT, self.background)
        arcade.draw_texture_rectangle(self.back_x2, self.back_y2 , SCREEN_WIDTH + 40, SCREEN_HEIGHT, self.background2)
        
        
        
        # ground
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, self.ground_y , SCREEN_WIDTH, SCREEN_HEIGHT, self.ground_texture)
        
        
        # score
        self.init = 0
        self.timer = 0.6666
        self.score_point = self.timer * 500
        arcade.draw_text("SCORE : %d" % self.score_point, 1000, 650, arcade.color.WHITE, 14)
        



        # sprite object draw
        self.character.draw()
        self.big_item.draw()
        self.fast_item.draw()
        self.wall.draw()
        self.life.draw()
        self.vitality_item.draw()
        
        
    
    def sound(self):        #bgm
        
        if self.is_playing_bgm:
            return
        
        if self.bgm:
            arcade.stop_sound(self.bgm)
                
        self.bgm = arcade.load_sound("bgm.mp3")
        
   
        arcade.play_sound(self.bgm)
        self.is_playing_bgm = True


    def gameover(self):     #game over
        arcade.close_window()

    

    
    
    
    
    def on_key_press(self, key, parameter):
        
        if key == arcade.key.SPACE:
            self.character.jump()
            
            if key == arcade.key.UP:
                self.character.to_y = 0
            
            if self.character.jump_count == 2:
                self.character.rotate()
                
                
                
                
    def on_key_release(self, key, parameter):

        if key == arcade.key.UP:
            self.character.to_y = -self.gravity
                

            

    def speed_down(self, parameter):
        self.wall.speed = 4
        self.back_move = self.speed_save
        self.is_fast = 0
        
        
       
                    
    def restore(self, parameter):
        print("call restore")               
        self.wall.angle = 0
        self.wall.center_x += SCREEN_WIDTH * random.randrange(3,5)
        self.wall.center_y = SCREEN_HEIGHT - (self.height // 2)
        return
        
    

        
    def large(self):
        print("large")
        for _ in range(10):
            self.character.width += 15
            self.character.height += 15
        arcade.schedule(self.small, 3.0)  

    
    
    def collision(self):
          
        self.wall.center_x += self.flying
        self.wall.center_y -= 12
        self.wall.rotate()
        arcade.schedule(self.restore, 1.0)
        
    
                
    
    def small(self, parameter):
        self.character.width = 116
        self.character.height = 125
        self.is_large = 0
        return





    def speed_up(self):
        
        if self.character.collides_with_sprite(self.fast_item):
            
            self.speed_save = self.back_move
            self.wall.speed += 5
            self.back_move += 20
            
            arcade.schedule(self.speed_down, 3.0)        
            return


    
    

    def on_update(self, key):
         
            
        # character
        self.character.update()                 
        self.character.to_y -= self.gravity      # gravity


        # 2단 점프 시 회전
        if self.character.jump_count == 2:
            self.character.angle -= 10
            

        # 착지 시 각도 0으로       
        if self.character.jump_count == 0:
            self.character.angle = 0
        
         
        # 바닥에 닿았을 때 설정
        if self.character.bottom <= 0:
            self.character.bottom = 0
            self.character.jump_count = 0



        # bgm
        if not self.is_playing_bgm:
            self.sound()
        
        
        
        # obstacle
        self.wall.update()
        
      
        
        if self.character.collides_with_sprite(self.wall):
            
            if self.is_fast == 1 or self.is_large == 1:
                self.collision()
                self.is_fast = 0
                self.is_large = 0
                
            else:
                self.wall.center_x = SCREEN_WIDTH * random.randint(3,5)
                self.life.center_x -= 50
        
        
        if self.wall.center_x <= - 50:
            self.wall.center_x = SCREEN_WIDTH * random.randint(3,5)
        
        
        
        
        
        # item
        
        
        # fast_item
        self.fast_item.update()
        
        
        if self.character.collides_with_sprite(self.fast_item):
            
            self.is_fast = 1
            self.speed_up()
            self.fast_item.center_x += SCREEN_WIDTH * random.randrange(4,6)
        
        if self.fast_item.center_x < - 50:
            self.fast_item.center_x += SCREEN_WIDTH * random.randrange(4,6)


        print(self.wall.center_x)

        # big_item
        self.big_item.update()
        
        
        if self.character.collides_with_sprite(self.big_item):
            
            self.is_large = 1
            self.large()
            self.big_item.center_x += SCREEN_WIDTH * random.randrange(4,6)
                    
        if self.big_item.center_x < - 50:
            self.big_item.center_x += SCREEN_WIDTH * random.randrange(4,6)
        
        
        
        
        
        
        # vitality_item
        self.vitality_item.update()
        if self.character.collides_with_sprite(self.vitality_item):
            self.life.center_x += 50
            self.vitality_item.center_x += SCREEN_WIDTH * random.randrange(4,6)
        
        if self.vitality_item.center_x < -50:
            self.vitality_item.center_x += SCREEN_WIDTH * random.randrange(4,6)
            


        # item fly
        if self.fast_item.center_y <= 200:
            self.fast_item.to_y = 2
            
        if self.fast_item.center_y >= 400:
            self.fast_item.to_y = -2

        if self.big_item.center_y <= 200:
            self.big_item.to_y = 2
            
        if self.big_item.center_y >= 400:
            self.big_item.to_y = -2

        if self.vitality_item.center_y <= 200:
            self.vitality_item.to_y = 2
            
        if self.vitality_item.center_y >= 400:
            self.vitality_item.to_y = -2
        
        
        # avoid overlap
        if self.big_item.center_x == self.fast_item.center_x:
            self.big_item.center_x += SCREEN_WIDTH
        if self.big_item.center_x == self.vitality_item.center_x:
            self.vitality_item.center_x += SCREEN_WIDTH + 300
        if self.fast_item.center_x == self.vitality_item.center_x:
            self.fast_item.center_x += SCREEN_WIDTH - 200
        
        
        
        
        # life
        self.life.update()
        
        if self.character.collides_with_sprite(self.life):
            self.life.center_x += 15
        
        if self.life.center_x > self.width // 2:
            self.life.center_x = self.width
            

        # background
        self.back_move += self.acc * 0.001
        
        self.back_x1 -= self.back_move
        self.back_x2 -= self.back_move
        
        if self.back_x1 <= -SCREEN_WIDTH // 2:      #배경이 계속 이어지도록
            self.back_x1 = SCREEN_WIDTH*1.5
        if self.back_x2 <= -SCREEN_WIDTH // 2:
            self.back_x2 = SCREEN_WIDTH*1.5

         
        
def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    