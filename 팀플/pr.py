import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Run Game"


class Cookie(arcade.Sprite): #캐릭터 설정 (이미지를 sprite로 불러오기 때문에 매개변수가 arcade.sprite)
    
    def __init__(self, cookie_stand): #CookieRun 클래스에서 cookie_stand 정의
        super().__init__(cookie_stand)
        self.center_x = self.width      #sprite의 객체는 center_X,Y를 씀, width는 sprite에 원래 들어있는 거 같음
        self.center_y = 100
        self.to_x = 0
        self.to_y = 0
        self.jump_count = 0
        self.cookie_sliding = "character_sliding.png"
        self.cookie_stand_img = "character.png"
        

            
    def update(self): # 움직일 때 위치값 설정
        self.center_x += self.to_x      #to_x or to_y = parameter
        self.center_y += self.to_y
        
        
    def jump(self):
        
        if self.jump_count < 2:
            self.to_y = 23
            self.jump_count += 1
        
               
    def rotate(self): # 점프 시 회전
        self.angle = 0
    



class item(arcade.Sprite):
    def __init__(self, heart_item): 
        super().__init__(heart_item)
        self.center_x = SCREEN_WIDTH * random.randint(3,5)
        self.center_y = 200
        self.to_y = 2

    
    def update(self):
        self.center_y += self.to_y
        self.center_x -= 5




class sky(arcade.Sprite):       #sky heart item
    def __init__(self, sky_item): 
        super().__init__(sky_item)
        self.center_x = SCREEN_WIDTH * random.randrange(3,5)
        self.center_y = 200
        self.to_y = 2
        
        
    
    def update(self):
        self.center_y += self.to_y
        self.center_x -= 5




class heart(arcade.Sprite):     #heart item
    def __init__(self, sky_heart): 
        super().__init__(sky_heart)
        self.center_x = 0
        self.center_y = SCREEN_HEIGHT * 2
        self.to_y = 0
    
    
    def update(self):
        self.center_x -= 8
        self.center_y -= self.to_y
        
      
            

class CookieRun(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
        
  


    def setup(self):
        
        
        self.cookie_stand = "character.png"
        self.cookie_stand_img = "character.png"
        
        self.cookie_run = "character_run.png"
        self.cookie_run_img = "character_run.png"
        
        
        self.cookie_sliding = "character_sliding.png"
        self.cookie_sliding_img = "character_sliding.png"
        
        
        self.cookie_gameover = "character_gameover.png"
        
        
        self.tick = 0
        self.timer = 0
        self.timer += self.tick
        self.life = self.timer + 300
        self.life_width = 600
        self.acc = 1
        self.acc += self.acc
         

            
        self.cookie = Cookie(self.cookie_stand)
        
        
        # 아이템
        
        # 기본 heart item
        self.item_img = "heart.png"
        
        self.heart_item = item(self.item_img)
        
        
        # sky_item
        self.sky_item_img = "sky_item.png"
        self.sky_item = sky(self.sky_item_img)
        self.sky_count = 0
        
        
        # sky_heart
        self.sky_heart_img = "sky_heart.png"
        self.sky_heart = heart(self.sky_heart_img)
        

        #배경화면
        background_image = "맵.jpg"
        self.background = arcade.load_texture(background_image)
        self.back_x1 = SCREEN_WIDTH // 2
        self.back_move = 8
        self.back_x1 -= self.back_move
        self.back_y1 = SCREEN_HEIGHT // 2
        
        
        self.up_finish = 0
        
        # sky 배경화면
        sky_back_img = "sky_background.jpg"
        self.sky_background_1 = arcade.load_texture(sky_back_img)
        self.sky_background_2 = arcade.load_texture(sky_back_img)
        self.sky_back_x1 = SCREEN_WIDTH // 2
        self.sky_back_x2 = SCREEN_WIDTH *1.5
        self.sky_move = 8
        self.sky_back_y = SCREEN_HEIGHT * 1.5
        self.sky_heart_count = 0
        
        
        
        # bgm
        self.bgm = None
        self.is_playing_bgm = False
        
        
        
        # 땅
        self.ground_y = SCREEN_HEIGHT // 2
        
        
        #장애물
        up_wall = "기둥 장애물.png"
        down_wall = "바닥 장애물.png"
        self.up = arcade.load_texture(up_wall)
        self.down = arcade.load_texture(down_wall)
        self.up_2 = arcade.load_texture(up_wall)
        
        self.up_pos = SCREEN_WIDTH*1.4 + random.randint(1, SCREEN_WIDTH // 4)
        self.up_pos -= self.back_move
        
        self.up_2_pos = SCREEN_WIDTH*1.3 + random.randint(1, SCREEN_WIDTH // 2)
        self.up_2_pos -= self.back_move
        
        self.down_pos = SCREEN_WIDTH*1.2 + random.randint(1, SCREEN_WIDTH // 3)
        self.down_pos -= self.back_move
        
        
        self.up_y = 420
        self.down_y = 150
        
        
        #배경2
        background2_image = "맵.jpg"
        self.background2 = arcade.load_texture(background2_image)
        self.back_x2 = SCREEN_WIDTH *1.5
        self.back_y2 = SCREEN_HEIGHT // 2
        
        

        # 바닥
        ground_image = "ground.png"
        self.ground_texture = arcade.load_texture(ground_image)
    

        
        
        
    def sound(self):
        if self.is_playing_bgm:
            return
        
        if self.bgm:
            arcade.stop_sound(self.bgm)
            
            
            
        self.bgm = arcade.load_sound("bgm.mp3")
        

        
        arcade.play_sound(self.bgm)
        self.is_playing_bgm = True
        
        
    
    def gameover(self):
        arcade.close_window()
        
        
            

    def on_draw(self):   #화면에 객체들이 나오게 함
        arcade.start_render()
        
        
        
        # 배경1
        arcade.draw_texture_rectangle(self.back_x1, self.back_y1 , SCREEN_WIDTH + 40, SCREEN_HEIGHT, self.background)
        # 배경2
        arcade.draw_texture_rectangle(self.back_x2, self.back_y2 , SCREEN_WIDTH + 40, SCREEN_HEIGHT, self.background2)
        
        # sky 배경 1
        arcade.draw_texture_rectangle(self.sky_back_x1, self.sky_back_y , SCREEN_WIDTH + 20, SCREEN_HEIGHT, self.sky_background_1)
        # sky 배경 2
        arcade.draw_texture_rectangle(self.sky_back_x2, self.sky_back_y , SCREEN_WIDTH + 20, SCREEN_HEIGHT, self.sky_background_2)
        
        
        #생명력
        heart_image = "생명력.png"
        self.heart = arcade.load_texture(heart_image)
        arcade.draw_texture_rectangle(self.life, 650 ,self.life_width , 40, self.heart)
        
        # 장애물
        arcade.draw_texture_rectangle(self.up_pos, self.up_y , 200, SCREEN_HEIGHT - 90, self.up)
        arcade.draw_texture_rectangle(self.up_2_pos, self.up_y , 200, SCREEN_HEIGHT - 90, self.up_2)
        arcade.draw_texture_rectangle(self.down_pos, self.down_y , 150, SCREEN_HEIGHT // 4, self.down)
        
        
        # 땅
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, self.ground_y , SCREEN_WIDTH, SCREEN_HEIGHT, self.ground_texture)
        
        
        # 점수
        self.score_point = -self.tick*500
        arcade.draw_text("SCORE : %d" % self.score_point, 1000, 650, arcade.color.WHITE, 14)

        
        # 게임오버
        if self.timer <= -self.life_width:
            self.cookie = Cookie(self.cookie_gameover)
            
            arcade.draw_text("GAME OVER" ,400, SCREEN_HEIGHT // 2 , arcade.color.WHITE, 40)
            arcade.draw_text("SCORE : %d" % self.score_point ,380, SCREEN_HEIGHT // 2 + 150, arcade.color.BLUE, 40)
            
            arcade.schedule(self.gameover, 3.0)      # gameover 함수를 3초 뒤 실행
        
        
        
            
        # sky_count
        arcade.draw_text("count = %d"% self.sky_count, 1000, 600, arcade.color.WHITE, 15)
         
        
        
        # sprite 객체
        self.cookie.draw()
        self.heart_item.draw()
        self.sky_item.draw()
        self.sky_heart.draw()

            



    def on_key_press(self, key, modifiers):
        
        
        
        if self.cookie.center_x == 125:      # 슬라이딩 상태에서는 점프를 못 하게
            pass
        else:    
            if key == arcade.key.SPACE:
                self.cookie.jump()
                if self.cookie.jump_count == 2:
                    self.cookie.rotate()
        

            
        
        
        # 점프 하는 동안 DOWN 키를 누를 시 self.cookie가 바뀌는 걸 방지
        if self.cookie.jump_count >= 1:
            if key == arcade.key.DOWN:
                pass
        
        
        
        elif key == arcade.key.DOWN:          
            self.cookie = Cookie(self.cookie_sliding_img)
            
        


    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.DOWN:
            if self.cookie.jump_count >= 1:
                pass
            else:
                self.cookie = Cookie(self.cookie_stand)

     
    def collision(self):
        
        if self.back_y1 == SCREEN_HEIGHT // 2:
            if abs(self.up_pos - self.cookie.center_x) <= self.width/8 and self.cookie.center_x == 116:
                self.timer -= 0.5

        
            if abs(self.up_2_pos - self.cookie.center_x) <= self.width/8 and self.cookie.center_x == 116:
                self.timer -= 0.5

        
            if abs(self.down_pos - self.cookie.center_x) <= self.width/8 and self.cookie.center_y <= 200:
                self.timer -= 0.5
        else:
            pass
     


    
    def screen_down(self):
        #화면 내림
        
        # 기본 배경화면
        self.back_y1 -= 5
        self.back_y2 -= 5
        
        # 땅
        self.ground_y -= 5
        
        # 하늘 배경
        self.sky_back_y -= 5

        
        # 장애물
        self.up_y -= 5
        self.down_y -= 5
        
        
        # 다 내려갔다면
        if self.back_y1 <= -SCREEN_HEIGHT * 0.5:
            
            # 이동 정지
            self.back_y1 = 0
            self.back_y2 = 0
            self.ground_y = 0
            self.sky_back_y = 0
            self.up_y = 0
            self.down_y = 0
            
            
            self.sky_count = 0
            
                        
            
            
            # 위치 고정 ( 사실 필요 x )
            self.back_y1 = -SCREEN_HEIGHT * 0.5
            self.back_y2 = -SCREEN_HEIGHT * 0.5
            self.ground_y = -SCREEN_HEIGHT * 0.5
            self.sky_back_y = SCREEN_HEIGHT * 0.5
            self.up_y = -SCREEN_HEIGHT * 0.5
            self.down_y = -SCREEN_HEIGHT * 0.5
            
            
            
            
            # 화면 이동 완료 후 하트 생성

            self.sky_heart.center_y = SCREEN_HEIGHT * 0.5
            
            
            
            # 하트 3개 먹으면 함수 종료
            if self.sky_heart_count == 3:
                return
     


    def screen_up(self):
        
        # 화면 올리기
        self.back_y1 += 5
        self.back_y2 += 5
        self.ground_y += 5
        self.sky_back_y += 5
        self.up_y += 5
        self.down_y += 5
        
        
        
        # 화면이 다 올라가면
        if self.back_y1 >= SCREEN_HEIGHT // 2:
            
            
            
            self.back_y1 = 0
            self.back_y2 = 0
            self.ground_y = 0
            self.sky_back_y = 0
            self.up_y = 0
            self.down_y = 0
            
            self.sky_count = 0
            self.sky_heart_count = 0
            
            # 원 위치 복귀
            self.back_y1 = SCREEN_HEIGHT // 2
            self.back_y2 = SCREEN_HEIGHT // 2
            self.ground_y = SCREEN_HEIGHT // 2
            self.sky_back_y = SCREEN_HEIGHT * 1.5
            self.up_y = 420
            self.down_y = 150
            self.sky_heart.center_y = SCREEN_HEIGHT * 2
            return    

   
    
    
    def fly(self):
        
        self.screen_down()
        

        
            
    def on_update(self, key):
         

            
        # 캐릭터
        self.cookie.update()                 
        self.cookie.to_y -= 1.5      # 중력 설정


        
        # bgm
        if not self.is_playing_bgm:
            self.sound()
        
        
        
        
        # 아이템
        self.heart_item.update()

        
        if self.cookie.collides_with_sprite(self.heart_item):
            self.heart_item.center_x += SCREEN_WIDTH * random.randint(3,4)
            self.timer += 30
        
        
        # 아이템이 위아래로 움직이도록
        if self.heart_item.center_y <= 200:
            self.heart_item.to_y = 2
            
        if self.heart_item.center_y >= 400:
            self.heart_item.to_y = -2
        

        
        # sky_item
        
        self.sky_item.update()
        
        if self.cookie.collides_with_sprite(self.sky_item):
            self.sky_item.center_x += SCREEN_WIDTH * random.randint(4,5)
            self.sky_count += 1
        
        if self.sky_count < 3 and self.sky_item.center_x < - 50:
            self.sky_item.center_x = SCREEN_WIDTH * random.randint(3,4)
        
        
        
            
        if self.sky_count == 3:
            self.fly()
            
            
                  
        if self.sky_item.center_y <= 200:
            self.sky_item.to_y = 2
            
        if self.sky_item.center_y >= 400:
            self.sky_item.to_y = -2
        
        

               
        # sky_heart
        
        self.sky_heart.update()

        self.sky_heart.center_x -= 8
        
        if self.sky_heart.center_x <= -50:
            self.sky_heart.center_x = SCREEN_WIDTH
        
        
        if self.cookie.collides_with_sprite(self.sky_heart):
            self.sky_heart.center_x += SCREEN_WIDTH + 300
            self.sky_heart_count += 1
            self.timer += 40
              
        if self.sky_heart_count >= 3:
            self.screen_up()
                   
        
        
        
        #배경
        
        self.back_move += self.acc * 0.001         # 가속도
        self.back_x1 -= self.back_move
        self.back_x2 -= self.back_move
        
        if self.back_x1 <= -SCREEN_WIDTH // 2:      #배경이 계속 이어지도록
            self.back_x1 = SCREEN_WIDTH*1.5
        if self.back_x2 <= -SCREEN_WIDTH // 2:
            self.back_x2 = SCREEN_WIDTH*1.5
        
        
        # sky 배경
        self.sky_back_x1 -= self.sky_move
        self.sky_back_x2 -= self.sky_move
        
        if self.sky_back_x1 <= -SCREEN_WIDTH // 2:
            self.sky_back_x1 = SCREEN_WIDTH * 1.5
        if self.sky_back_x2 <= -SCREEN_WIDTH // 2:
            self.sky_back_x2 = SCREEN_WIDTH * 1.5
        
          
        
        #장애물
        self.up_pos -= self.back_move 
        if self.up_pos <= -50:
            self.up_pos = SCREEN_WIDTH*2 + random.randint(1, SCREEN_WIDTH // 4)   
        
        self.up_2_pos -= self.back_move
        if self.up_2_pos <= -50:
            self.up_2_pos = SCREEN_WIDTH*2 + random.randint(1, SCREEN_WIDTH // 3)
        
         
        
        self.down_pos -= self.back_move
        if self.down_pos <= - 50:
            self.down_pos = SCREEN_WIDTH*1.5 +  random.randint(1, SCREEN_WIDTH // 2)
            
        
        # 장애물 사이의 텀 만들기
        
        if self.down_pos >= SCREEN_WIDTH and self.up_pos >= SCREEN_WIDTH:
            if abs(self.down_pos - self.up_pos) <= 400:
                self.up_pos += 500
        
        if self.down_pos >= SCREEN_WIDTH and self.up_2_pos >= SCREEN_WIDTH:
            if abs(self.down_pos - self.up_2_pos) <= 400:
                self.up_2_pos += 500
        
        if self.up_pos >= SCREEN_WIDTH and self.up_2_pos >= SCREEN_WIDTH:
            if abs(self.up_pos - self.up_2_pos) <= 400:
                self.up_pos += 500
        
        
        
        # 충돌              #stand의 center_x = 116, sliding의 center_x = 125
    
        self.collision()
        

                   
        #생명력
        self.tiktik = 0.00004
        self.tick -= self.tiktik
        self.timer += self.tick
        
        self.life = self.timer + 300
        
        if self.timer <= -self.life_width:
            
            self.tick += self.tiktik
        
        
        # 생명력이 오버되지 않게 최대치 설정
        if self.life >= 300:
            self.life = 300
        
       
        
        # 2단 점프 시 회전
        if self.cookie.jump_count == 2:
            self.cookie.angle -= 10
            

        # 착지 시 각도 0으로       
        if self.cookie.jump_count == 0:
            self.cookie.angle = 0
        
         
        # 바닥에 닿았을 때 설정
        if self.cookie.bottom <= 0:
            self.cookie.bottom = 0
            self.cookie.jump_count = 0

               

def main():
    game = CookieRun()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()