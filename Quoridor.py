import pyxel


#2024/01/13_07:0 更新

class Quoridor :
    def __init__(self) :
        pyxel.init(349, 359 , fps=60)
        self.player1_x = 0 #プレイヤー1のx座標(0-8で変動)
        self.player1_y = 4 #プレイヤー1のx座標(0-8で変動)
        self.player2_x = 8 #プレイヤー1のx座標(0-8で変動)
        self.player2_y = 4 #プレイヤー1のx座標(0-8で変動)

        self.player1_vector = 0 #1:上 2:右 3:下 4:左
        self.player1_vector_dia = 0 #1:反時計側 2:時計側
        self.player2_vector = 0 #1:上 2:右 3:下 4:左
        self.player2_vector_dia = 0 #1:反時計側 2:時計側

        self.arrow_color = 0 #矢印の色
        self.arrow_color_player1 = 5 #プレイヤー1の矢印の色
        self.arrow_color_player2 = 8 #プレイヤー2の矢印の色
        self.arrow_color_cant = 13 #不可能時の矢印の色

        self.player_now = pyxel.rndi(1,2) #現在のプレイヤー
        self.player_before = self.player_now #1f前のプレイヤー

        self.install_mode = 0 #0:移動モード 1:縦壁配置 2:横壁配置
        self.wall_x = 1 #設置予定壁のx座標(1-8で変動)
        self.wall_y = 1 #設置予定壁のy座標(1-8で変動)

        self.wallnum_player1 = 10 #プレイヤー1の壁の所持数
        self.wallnum_player2 = 10 #プレイヤー2の壁の所持数

        self.gamemode = 0 #0:タイトル画面表示 1:ゲームプレイ画面 2:ゲーム終了
        self.first_player = 1 #0:player1 1:ランダム 2:player2

        self.turn_count = 1 #現在のターン数(100ターンで一周)
        self.first_judge = True #先攻プレイヤーならTrue、後攻プレイヤーならFalse
        self.player1_time = 0 #プレイヤー1の経過時間(単位:f、100分=6000秒=360000fで一周)
        self.player2_time = 0 #プレイヤー2の経過時間(単位:f、100分=6000秒=360000fで一周)

        self.count = 0

        #self.wall_make_can = False #wall_can関数の戻り値として使う変数
        self.wall_make_can_player1 = False #wall_can関数の戻り値に利用する変数
        self.wall_make_can_player2 = False #wall_can関数の戻り値に利用する変数

        self.search_algorithm = True #探索アルゴリズムのレベル True:High False:low
        self.search_algorithm_mode = "ON"
        
        #1:縦 2:横
        self.wall_list = [[2,2,2,2,2,2,2,2,2,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,2,2,2,2,2,2,2,2,2]
                          ]
        
        self.wall_list_tent = [[2,2,2,2,2,2,2,2,2,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,2,2,2,2,2,2,2,2,2]
                          ]
        
        self.player1_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player1_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]

        pyxel.run(self.update, self.draw)

    
    def wall_can(self,y,x,dir,search_mode=True):
      if search_mode or self.search_algorithm:
        for xs in range(10):
            for ys in range(10):
                self.wall_list_tent[ys][xs] = self.wall_list[ys][xs]
        self.wall_list_tent[y][x] = dir
        self.wall_make_can_player1 = False
        self.wall_make_can_player2 = False

        self.player1_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player1_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player1_can_move_list[self.player1_y][self.player1_x] = 1
        self.player2_can_move_list[self.player2_y][self.player2_x] = 1

        while True:
            #self.player1_can_move_list_before = self.player1_can_move_list
            #self.player2_can_move_list_before = self.player2_can_move_list
            for xs in range (9):
                for ys in range(9):
                    self.player1_can_move_list_before[ys][xs] = self.player1_can_move_list[ys][xs]
                    self.player2_can_move_list_before[ys][xs] = self.player2_can_move_list[ys][xs]
            for xs in range(9):
                for ys in range(9):
                    if self.player1_can_move_list[ys][xs] == 1:
                        if ys > 0:
                            if not(self.wall_list_tent[ys][xs] == 2 or self.wall_list_tent[ys][xs+1] == 2):
                                self.player1_can_move_list[ys-1][xs] = 1
                        if xs < 8:
                            if not(self.wall_list_tent[ys][xs+1] == 1 or self.wall_list_tent[ys+1][xs+1] == 1):
                                self.player1_can_move_list[ys][xs+1] = 1
                        if ys < 8:
                            if not(self.wall_list_tent[ys+1][xs] == 2 or self.wall_list_tent[ys+1][xs+1] == 2):
                                self.player1_can_move_list[ys+1][xs] = 1
                        if xs > 0:
                            if not(self.wall_list_tent[ys][xs] == 1 or self.wall_list_tent[ys+1][xs] == 1):
                                self.player1_can_move_list[ys][xs-1] = 1
                    if self.player2_can_move_list[ys][xs] == 1:
                        if ys > 0:
                            if not(self.wall_list_tent[ys][xs] == 2 or self.wall_list_tent[ys][xs+1] == 2):
                                self.player2_can_move_list[ys-1][xs] = 1
                        if xs < 8:
                            if not(self.wall_list_tent[ys][xs+1] == 1 or self.wall_list_tent[ys+1][xs+1] == 1):
                                self.player2_can_move_list[ys][xs+1] = 1
                        if ys < 8:
                            if not(self.wall_list_tent[ys+1][xs] == 2 or self.wall_list_tent[ys+1][xs+1] == 2):
                                self.player2_can_move_list[ys+1][xs] = 1
                        if xs > 0:
                            if not(self.wall_list_tent[ys][xs] == 1 or self.wall_list_tent[ys+1][xs] == 1):
                                self.player2_can_move_list[ys][xs-1] = 1
            if self.player1_can_move_list == self.player1_can_move_list_before and self.player2_can_move_list == self.player2_can_move_list_before:
                break
            
        for ys in range(9):
            if self.player1_can_move_list_before[ys][8] == 1:
                self.wall_make_can_player1 = True
            if self.player2_can_move_list_before[ys][0] == 1:
                self.wall_make_can_player2 = True
        
        if self.wall_make_can_player1 and self.wall_make_can_player2:
            return True
        else:
            return False
      else:
          return True

        


    def update(self):
      if self.gamemode == 0:
          self.count += 1
          if self.count >= 60:
              self.count -= 60
          if pyxel.btnp(pyxel.KEY_SHIFT):
              if self.search_algorithm:
                  self.search_algorithm = False
                  self.search_algorithm_mode = "OFF"
              else:
                  self.search_algorithm = True
                  self.search_algorithm_mode = "ON"
      else:
          self.count = 0


      if self.install_mode == 0 and self.gamemode == 1:
        if self.player_now == 1:
            if pyxel.btnp(pyxel.KEY_W): # WASDキーで方向指定
                self.player1_vector = 1
                self.player1_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_A):
                self.player1_vector = 4
                self.player1_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_S):
                self.player1_vector = 3
                self.player1_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_D):
                self.player1_vector = 2
                self.player1_vector_dia = 0


            #斜め方向を確定させる
            if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y:
              if self.wall_list[self.player1_y-1][self.player1_x] == 2 or self.wall_list[self.player1_y-1][self.player1_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 1
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_D)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_D)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 1

            if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y:
              if self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1:
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_D)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_D)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 2
                if (pyxel.btnp(pyxel.KEY_D) and pyxel.btn(pyxel.KEY_S)) or (pyxel.btn(pyxel.KEY_D) and pyxel.btnp(pyxel.KEY_S)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 2

            if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y:
              if self.wall_list[self.player1_y+2][self.player1_x] == 2 or self.wall_list[self.player1_y+2][self.player1_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_D)) or (pyxel.btn(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_D)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 3
                if (pyxel.btnp(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 3

            if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y:
              if self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1:
                if (pyxel.btnp(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 4
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 4

            #移動
            if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 1: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y-1][self.player1_x] == 2) and (not self.wall_list[self.player1_y-1][self.player1_x+1] == 2):
                        self.player1_y -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y-1][self.player1_x] == 1 or self.wall_list[self.player1_y][self.player1_x] == 1)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y-1][self.player1_x+1] == 1 or self.wall_list[self.player1_y][self.player1_x+1] == 1)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2):
                    self.player1_y -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0

                

            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 2: #and self.player1_y >= 1:
                if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1):
                        self.player1_x += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y][self.player1_x+1] == 2 or self.wall_list[self.player1_y][self.player1_x+2] == 2)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 2 or self.wall_list[self.player1_y+1][self.player1_x+2] == 2)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1):
                    self.player1_x += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 3: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y and(not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y+2][self.player1_x] == 2) and (not self.wall_list[self.player1_y+2][self.player1_x+1] == 2):
                        self.player1_y += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 1 or self.wall_list[self.player1_y+2][self.player1_x+1] == 1)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 1 or self.wall_list[self.player1_y+2][self.player1_x] == 1)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2):
                    self.player1_y += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 4: #and self.player1_y >= 1:
                if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y and(not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1):
                        self.player1_x -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x-1] == 2)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x-1] == 2)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1):
                    self.player1_x -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0

                
        elif self.player_now == 2:
            if pyxel.btnp(pyxel.KEY_UP): # 矢印キーで方向指定
                self.player2_vector = 1
                self.player2_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.player2_vector = 4
                self.player2_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.player2_vector = 3
                self.player2_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.player2_vector = 2
                self.player2_vector_dia = 0


            #斜め方向を確定させる
            if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y:
              if self.wall_list[self.player2_y-1][self.player2_x] == 2 or self.wall_list[self.player2_y-1][self.player2_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 1
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_RIGHT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_RIGHT)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 1

            if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y:
              if self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1:
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_RIGHT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_RIGHT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 2
                if (pyxel.btnp(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_DOWN)) or (pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btnp(pyxel.KEY_DOWN)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 2

            if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y:
              if self.wall_list[self.player2_y+2][self.player2_x] == 2 or self.wall_list[self.player2_y+2][self.player2_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_RIGHT)) or (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btnp(pyxel.KEY_RIGHT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 3
                if (pyxel.btnp(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 32

            if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y:
              if self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1:
                if (pyxel.btnp(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 4
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 4

            #移動
            if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 1: #and self.player1_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y-1][self.player2_x] == 2) and (not self.wall_list[self.player2_y-1][self.player2_x+1] == 2):
                        self.player2_y -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y-1][self.player2_x] == 1 or self.wall_list[self.player2_y][self.player2_x] == 1)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y-1][self.player2_x+1] == 1 or self.wall_list[self.player2_y][self.player2_x+1] == 1)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2):
                    self.player2_y -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0

                

            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 2: #and self.player2_y >= 1:
                if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1):
                        self.player2_x += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y][self.player2_x+1] == 2 or self.wall_list[self.player2_y][self.player2_x+2] == 2)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 2 or self.wall_list[self.player2_y+1][self.player2_x+2] == 2)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1):
                    self.player2_x += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 3: #and self.player2_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y+2][self.player2_x] == 2) and (not self.wall_list[self.player2_y+2][self.player2_x+1] == 2):
                        self.player2_y += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 1 or self.wall_list[self.player2_y+2][self.player2_x+1] == 1)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 1 or self.wall_list[self.player2_y+2][self.player2_x] == 1)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2):
                    self.player2_y += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 4: #and self.player2_y >= 1:
                if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1):
                        self.player2_x -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x-1] == 2)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x-1] == 2)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1):
                    self.player2_x -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0

    
      if (self.install_mode == 1 or self.install_mode == 2) and self.gamemode == 1:
          if self.player_now == 1:
              if pyxel.btnp(pyxel.KEY_W):
                  self.wall_y -= 1
              if pyxel.btnp(pyxel.KEY_D):
                  self.wall_x += 1
              if pyxel.btnp(pyxel.KEY_S):
                  self.wall_y += 1
              if pyxel.btnp(pyxel.KEY_A):
                  self.wall_x -= 1
          elif self.player_now == 2:
              if pyxel.btnp(pyxel.KEY_UP):
                  self.wall_y -= 1
              if pyxel.btnp(pyxel.KEY_RIGHT):
                  self.wall_x += 1
              if pyxel.btnp(pyxel.KEY_DOWN):
                  self.wall_y += 1
              if pyxel.btnp(pyxel.KEY_LEFT):
                  self.wall_x -= 1 

          if self.wall_x >= 9:
              self.wall_x = 8
          elif self.wall_x <= 0:        
              self.wall_x = 1
          if self.wall_y >= 9:
              self.wall_y = 8
          elif self.wall_y <= 0:        
              self.wall_y = 1
        
      if self.install_mode == 1 and (pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE)) and self.gamemode == 1:
          if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y-1][self.wall_x] == 1 or self.wall_list[self.wall_y+1][self.wall_x] == 1)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
              self.wall_list[self.wall_y][self.wall_x] = 1
              if self.player_now == 1:
                  self.player_now = 2
                  self.wallnum_player1 -= 1
              else:
                  self.player_now = 1
                  self.wallnum_player2 -= 1
      elif self.install_mode == 2 and (pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE)) and self.gamemode == 1:
          if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y][self.wall_x-1] == 2 or self.wall_list[self.wall_y][self.wall_x+1] == 2)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
              self.wall_list[self.wall_y][self.wall_x] = 2
              if self.player_now == 1:
                  self.player_now = 2
                  self.wallnum_player1 -= 1
              else:
                  self.player_now = 1
                  self.wallnum_player2 -= 1
              


        
      if self.player_now == self.player_before:
            if pyxel.btnp(pyxel.KEY_SHIFT) and ((self.player_now == 1 and self.wallnum_player1 >= 1) or (self.player_now == 2 and self.wallnum_player2 >= 1)):
                self.install_mode += 1
                self.player1_vector = 0 #1:上 2:右 3:下 4:左
                self.player1_vector_dia = 0 #1:反時計側 2:時計側
                self.player2_vector = 0 #1:上 2:右 3:下 4:左
                self.player2_vector_dia = 0 #1:反時計側 2:時計側
                if self.install_mode >= 3:
                    self.install_mode = 0
                #if self.install_mode == 1:
                    #for y in range(8):
                        #for x in range(8):
                            #if self.wall_list[8-y][8-x] == 0 and (not(self.wall_list[7-y][8-x] == 1 or self.wall_list[9-y][8-x] == 1)):
                                #self.wall_x = 8-x
                                #self.wall_y = 8-y
                #if self.install_mode == 2:
                    #for y in range(8):
                        #for x in range(8):
                            #if self.wall_list[8-y][8-x] == 0 and (not(self.wall_list[8-y][7-x] == 2 or self.wall_list[8-y][9-x] == 2)):
                                #self.wall_x = 8-x
                                #self.wall_y = 8-y

      else:
            self.install_mode = 0
            self.player1_vector = 0 #1:上 2:右 3:下 4:左
            self.player1_vector_dia = 0 #1:反時計側 2:時計側
            self.player2_vector = 0 #1:上 2:右 3:下 4:左
            self.player2_vector_dia = 0 #1:反時計側 2:時計側

            if self.player1_x < 8 and self.player2_x > 0:

                if self.first_judge:
                    self.first_judge = False
                else:
                    self.first_judge = True
                    self.turn_count += 1
                    if self.turn_count >= 100:
                        self.turn_count -= 100

        
      

      if self.gamemode == 0:
        self.player1_x = 0 #プレイヤー1のx座標(0-8で変動)
        self.player1_y = 4 #プレイヤー1のx座標(0-8で変動)
        self.player2_x = 8 #プレイヤー1のx座標(0-8で変動)
        self.player2_y = 4 #プレイヤー1のx座標(0-8で変動)

        self.player1_vector = 0 #1:上 2:右 3:下 4:左
        self.player1_vector_dia = 0 #1:反時計側 2:時計側
        self.player2_vector = 0 #1:上 2:右 3:下 4:左
        self.player2_vector_dia = 0 #1:反時計側 2:時計側

        self.arrow_color = 0 #矢印の色
        self.arrow_color_player1 = 5 #プレイヤー1の矢印の色
        self.arrow_color_player2 = 8 #プレイヤー2の矢印の色
        self.arrow_color_cant = 13 #不可能時の矢印の色

        #self.player_now = pyxel.rndi(1,2) #現在のプレイヤー
        self.player_before = self.player_now #1f前のプレイヤー

        self.install_mode = 0 #0:移動モード 1:縦壁配置 2:横壁配置
        self.wall_x = 1 #設置予定壁のx座標(1-8で変動)
        self.wall_y = 1 #設置予定壁のy座標(1-8で変動)

        self.wallnum_player1 = 10 #プレイヤー1の壁の所持数
        self.wallnum_player2 = 10 #プレイヤー2の壁の所持数

        self.gamemode = 0 #0:タイトル画面表示 1:ゲームプレイ画面 2:ゲーム終了
        #self.first_player = 1 #0:player1 1:ランダム 2:player2

        self.turn_count = 1 #現在のターン数(100ターンで一周)
        self.first_judge = True #先攻プレイヤーならTrue、後攻プレイヤーならFalse
        self.player1_time = 0 #プレイヤー1の経過時間(単位:f、100分=6000秒=360000fで一周)
        self.player2_time = 0 #プレイヤー2の経過時間(単位:f、100分=6000秒=360000fで一周)
        
        #1:縦 2:横
        self.wall_list = [[2,2,2,2,2,2,2,2,2,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,2,2,2,2,2,2,2,2,2]
                          ]



        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
              self.gamemode = 1
              if self.first_player == 0:
                  self.player_now = 1
              elif self.first_player == 2:
                  self.player_now = 2
              else:
                  self.player_now = pyxel.rndi(1,2)
        else:
              if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.KEY_LEFT):
                  self.first_player -= 1
              if pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_RIGHT):
                  self.first_player += 1
              if self.first_player < 0:
                  self.first_player = 2
              elif self.first_player > 2:
                  self.first_player = 0
      elif self.gamemode == 1:
          if self.player_now == 1:
              self.player1_time += 1
              if self.player1_time >= 360000:
                  self.player1_time -= 360000
          elif self.player_now == 2:
              self.player2_time += 1
              if self.player2_time >= 360000:
                  self.player2_time -= 360000


          if self.player1_x == 8:
              self.gamemode = 2
              self.player_now = 1
          elif self.player2_x == 0:
              self.gamemode = 2
              self.player_now = 2
      elif self.gamemode == 2:
          if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
              self.gamemode = 0
              



      self.player_before = self.player_now




        

    #矢印マークの上にバツマークを描画する     
    def cross__arrow_draw(self,x,y):
        if self.arrow_color == self.arrow_color_cant:
            pyxel.tri(x-7,y-9,x-9,y-7,x+9,y+7,8)
            pyxel.tri(x+7,y+9,x-9,y-7,x+9,y+7,8)

            pyxel.tri(x+7,y-9,x+9,y-7,x-9,y+7,8)
            pyxel.tri(x-7,y+9,x+9,y-7,x-9,y+7,8)

    def cross__wall_draw(self,x,y):
        #if self.arrow_color == self.arrow_color_cant:
            pyxel.tri(x-7,y-9,x-9,y-7,x+9,y+7,8)
            pyxel.tri(x+7,y+9,x-9,y-7,x+9,y+7,8)

            pyxel.tri(x+7,y-9,x+9,y-7,x-9,y+7,8)
            pyxel.tri(x-7,y+9,x+9,y-7,x-9,y+7,8)

    def box_color(self,x,y):
      if self.install_mode == 0 and self.gamemode == 1:
        pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,11)
        if self.player_now == 1:
            pyxel.rectb(8 + x * 38, 8 + y * 38 ,29,29,12)
        elif self.player_now == 2:
            pyxel.rectb(8 + x * 38, 8 + y * 38 ,29,29,14)


    #任意文字関数
    def text(self,x,y,size,a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3,e1,e2,e3,color=0,count=0):
        if a1 == 1:
            pyxel.rect(count*4*size+ x,y,size,size,color)
        if a2 == 1:
            pyxel.rect(count*4*size+ x+size,y,size,size,color)
        if a3 == 1:
            pyxel.rect(count*4*size+ x+size*2,y,size,size,color)

        if b1 == 1:
            pyxel.rect(count*4*size+ x,y+size,size,size,color)
        if b2 == 1:
            pyxel.rect(count*4*size+ x+size,y+size,size,size,color)
        if b3 == 1:
            pyxel.rect(count*4*size+ x+size*2,y+size,size,size,color)
        
        if c1 == 1:
            pyxel.rect(count*4*size+ x,y+size*2,size,size,color)
        if c2 == 1:
            pyxel.rect(count*4*size+ x+size,y+size*2,size,size,color)
        if c3 == 1:
            pyxel.rect(count*4*size+ x+size*2,y+size*2,size,size,color)

        if d1 == 1:
            pyxel.rect(count*4*size+ x,y+size*3,size,size,color)
        if d2 == 1:
            pyxel.rect(count*4*size+ x+size,y+size*3,size,size,color)
        if d3 == 1:
            pyxel.rect(count*4*size+ x+size*2,y+size*3,size,size,color)

        if e1 == 1:
            pyxel.rect(count*4*size+ x,y+size*4,size,size,color)
        if e2 == 1:
            pyxel.rect(count*4*size+ x+size,y+size*4,size,size,color)
        if e3 == 1:
            pyxel.rect(count*4*size+ x+size*2,y+size*4,size,size,color)
        

        

        




    def draw(self) :
      pyxel.cls(7)

      if self.gamemode == 0:
        #pyxel.text(159,120,"Quoridor",11)
        #self.text(81,70,6, 0,1,0, 1,0,1, 1,0,1, 1,1,1, 0,1,1, 11) #Q
        #self.text(81,70,6, 0,0,0, 1,0,1, 1,0,1, 1,0,1, 0,1,1, 11,1) #u
        #self.text(81,70,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 11,2) #o
        #self.text(81,70,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 11,3) #r
        #self.text(81,70,6, 0,1,0, 0,0,0, 0,1,0, 0,1,0, 0,1,0, 11,4) #i
        #self.text(81,70,6, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 11,5) #d
        #self.text(81,70,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 11,6) #o
        #self.text(81,70,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 11,7) #r
         
        self.text(97,150,2, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,1,1, 0,0) #C
        self.text(97,150,2, 1,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 0,1) #h
        self.text(97,150,2, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 0,2) #o
        self.text(97,150,2, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 0,3) #o
        self.text(97,150,2, 0,0,0, 0,1,1, 1,1,0, 0,1,1, 1,1,0, 0,4) #s
        self.text(97,150,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 0,5) #e
        self.text(97,150,2, 1,1,1, 1,0,0, 1,1,1, 1,0,0, 1,0,0, 0,7) #F
        self.text(97,150,2, 0,1,0, 0,0,0, 0,1,0, 0,1,0, 0,1,0, 0,8) #i
        self.text(97,150,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,9) #r
        self.text(97,150,2, 0,0,0, 0,1,1, 1,1,0, 0,1,1, 1,1,0, 0,10) #s
        self.text(97,150,2, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 0,11) #t
        self.text(97,150,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 0,13) #P
        self.text(97,150,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 0,14) #l
        self.text(97,150,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,15) #a
        self.text(97,152,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 0,16) #y
        self.text(97,150,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 0,17) #e
        self.text(97,150,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,18) #r

        pyxel.text(10,349,"Deep Search Algorithm:"+self.search_algorithm_mode,0)
        pyxel.text(19,339,"SHIFT to change mode",0)

        if self.first_player == 1:
            pyxel.rectb(54,190,60,60,0)
            pyxel.rectb(139,185,70,70,11)
            pyxel.rectb(234,190,60,60,0)

            pyxel.tri(0,0,0,70,70,0,11)
            pyxel.tri(0,0,0,55,55,0,7)

            pyxel.tri(348,358,348,288,278,358,11)
            pyxel.tri(348,358,348,303,293,358,7)

            self.text(57,234,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 0,0) #P
            self.text(57,234,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 0,1) #l
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,2) #a
            self.text(57,234,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 0,3) #y
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 0,4) #e
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,5) #r
            self.text(57,234,2, 0,1,0, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 0,6) #1

            pyxel.rectb(74,200,20,20,12) #箱1

            self.text(237,234,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 0,0) #P
            self.text(237,234,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 0,1) #l
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,2) #a
            self.text(237,234,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 0,3) #y
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 0,4) #e
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,5) #r
            self.text(237,234,2, 1,1,0, 0,0,1, 0,1,0, 1,0,0, 1,1,1, 0,6) #2

            pyxel.rectb(254,200,20,20,14) #箱2

            self.text(151,234,2, 1,1,0, 1,0,1, 1,1,1, 1,1,0, 1,0,1, 11,0) #R
            self.text(151,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 11,1) #a
            self.text(151,234,2, 0,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 11,2) #n
            self.text(151,234,2, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 11,3) #d
            self.text(151,234,2, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 11,4) #o
            self.text(151,234,2, 0,0,0, 1,1,1, 1,1,1, 1,1,1, 1,0,1, 11,5) #m

            self.text(168,200,4, 1,1,1, 0,0,1, 0,1,0, 0,0,0, 0,1,0, 11,0) #?

           


    
            self.text(81,60,6, 0,1,0, 1,0,1, 1,0,1, 1,1,1, 0,1,1, 11) #Q
            self.text(81,60,6, 0,0,0, 1,0,1, 1,0,1, 1,0,1, 0,1,1, 11,1) #u
            self.text(81,60,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 11,2) #o
            self.text(81,60,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 11,3) #r
            self.text(81,60,6, 0,1,0, 0,0,0, 0,1,0, 0,1,0, 0,1,0, 11,4) #i
            self.text(81,60,6, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 11,5) #d
            self.text(81,60,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 11,6) #o
            self.text(81,60,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 11,7) #r

            if self.count >=30:
                self.text(92,290,3, 1,1,1, 1,0,0, 1,1,1, 1,0,0, 1,1,1, 11,0) #E
                self.text(92,290,3, 0,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 11,1) #n
                self.text(92,290,3, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 11,2) #t
                self.text(92,290,3, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 11,3) #e
                self.text(92,290,3, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 11,4) #r
                self.text(92,290,3, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 11,6) #t
                self.text(92,290,3, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 11,7) #o
                self.text(92,290,3, 0,1,1, 1,0,0, 0,1,0, 0,0,1, 1,1,0, 11,9) #S
                self.text(92,290,3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 0,1,0, 11,10) #T
                self.text(92,290,3, 0,1,0, 1,0,1, 1,1,1, 1,0,1, 1,0,1, 11,11) #A
                self.text(92,290,3, 1,1,0, 1,0,1, 1,1,1, 1,1,0, 1,0,1, 11,12) #R
                self.text(92,290,3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 0,1,0, 11,13) #T

        elif self.first_player == 0:
            pyxel.rectb(49,185,70,70,12)
            pyxel.rectb(144,190,60,60,0)
            pyxel.rectb(234,190,60,60,0)

            pyxel.tri(0,0,0,70,70,0,12)
            pyxel.tri(0,0,0,55,55,0,7)

            pyxel.tri(348,358,348,288,278,358,12)
            pyxel.tri(348,358,348,303,293,358,7)

            self.text(57,234,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 12,0) #P
            self.text(57,234,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 12,1) #l
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 12,2) #a
            self.text(57,234,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 12,3) #y
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 12,4) #e
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 12,5) #r
            self.text(57,234,2, 0,1,0, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 12,6) #1

            pyxel.rect(74,200,20,20,12) #箱1

            self.text(237,234,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 0,0) #P
            self.text(237,234,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 0,1) #l
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,2) #a
            self.text(237,234,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 0,3) #y
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 0,4) #e
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,5) #r
            self.text(237,234,2, 1,1,0, 0,0,1, 0,1,0, 1,0,0, 1,1,1, 0,6) #2

            pyxel.rectb(254,200,20,20,14) #箱2

            self.text(151,234,2, 1,1,0, 1,0,1, 1,1,1, 1,1,0, 1,0,1, 0,0) #R
            self.text(151,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,1) #a
            self.text(151,234,2, 0,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 0,2) #n
            self.text(151,234,2, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,3) #d
            self.text(151,234,2, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 0,4) #o
            self.text(151,234,2, 0,0,0, 1,1,1, 1,1,1, 1,1,1, 1,0,1, 0,5) #m

            self.text(168,200,4, 1,1,1, 0,0,1, 0,1,0, 0,0,0, 0,1,0, 0,0) #?

           


    
            self.text(81,60,6, 0,1,0, 1,0,1, 1,0,1, 1,1,1, 0,1,1, 12) #Q
            self.text(81,60,6, 0,0,0, 1,0,1, 1,0,1, 1,0,1, 0,1,1, 12,1) #u
            self.text(81,60,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 12,2) #o
            self.text(81,60,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 12,3) #r
            self.text(81,60,6, 0,1,0, 0,0,0, 0,1,0, 0,1,0, 0,1,0, 12,4) #i
            self.text(81,60,6, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 12,5) #d
            self.text(81,60,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 12,6) #o
            self.text(81,60,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 12,7) #r

            if self.count >=30:
                self.text(92,290,3, 1,1,1, 1,0,0, 1,1,1, 1,0,0, 1,1,1, 12,0) #E
                self.text(92,290,3, 0,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 12,1) #n
                self.text(92,290,3, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 12,2) #t
                self.text(92,290,3, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 12,3) #e
                self.text(92,290,3, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 12,4) #r
                self.text(92,290,3, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 12,6) #t
                self.text(92,290,3, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 12,7) #o
                self.text(92,290,3, 0,1,1, 1,0,0, 0,1,0, 0,0,1, 1,1,0, 12,9) #S
                self.text(92,290,3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 0,1,0, 12,10) #T
                self.text(92,290,3, 0,1,0, 1,0,1, 1,1,1, 1,0,1, 1,0,1, 12,11) #A
                self.text(92,290,3, 1,1,0, 1,0,1, 1,1,1, 1,1,0, 1,0,1, 12,12) #R
                self.text(92,290,3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 0,1,0, 12,13) #T

        elif self.first_player == 2:
            pyxel.rectb(54,190,60,60,0)
            pyxel.rectb(144,190,60,60,0)
            pyxel.rectb(229,185,70,70,14)

            pyxel.tri(0,0,0,70,70,0,14)
            pyxel.tri(0,0,0,55,55,0,7)

            pyxel.tri(348,358,348,288,278,358,14)
            pyxel.tri(348,358,348,303,293,358,7)

            self.text(57,234,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 0,0) #P
            self.text(57,234,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 0,1) #l
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,2) #a
            self.text(57,234,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 0,3) #y
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 0,4) #e
            self.text(57,234,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 0,5) #r
            self.text(57,234,2, 0,1,0, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 0,6) #1

            pyxel.rectb(74,200,20,20,12) #箱1

            self.text(237,234,2, 1,1,0, 1,0,1, 1,1,0, 1,0,0, 1,0,0, 14,0) #P
            self.text(237,234,2, 1,1,0, 0,1,0, 0,1,0, 0,1,0, 1,1,1, 14,1) #l
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 14,2) #a
            self.text(237,234,2, 1,0,1, 1,0,1, 0,1,1, 0,0,1, 0,1,0, 14,3) #y
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 14,4) #e
            self.text(237,234,2, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 14,5) #r
            self.text(237,234,2, 1,1,0, 0,0,1, 0,1,0, 1,0,0, 1,1,1, 14,6) #2

            pyxel.rect(254,200,20,20,14) #箱2

            self.text(151,234,2, 1,1,0, 1,0,1, 1,1,1, 1,1,0, 1,0,1, 0,0) #R
            self.text(151,234,2, 0,0,0, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,1) #a
            self.text(151,234,2, 0,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 0,2) #n
            self.text(151,234,2, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 0,3) #d
            self.text(151,234,2, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 0,4) #o
            self.text(151,234,2, 0,0,0, 1,1,1, 1,1,1, 1,1,1, 1,0,1, 0,5) #m

            self.text(168,200,4, 1,1,1, 0,0,1, 0,1,0, 0,0,0, 0,1,0, 0,0) #?

           


    
            self.text(81,60,6, 0,1,0, 1,0,1, 1,0,1, 1,1,1, 0,1,1, 14) #Q
            self.text(81,60,6, 0,0,0, 1,0,1, 1,0,1, 1,0,1, 0,1,1, 14,1) #u
            self.text(81,60,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 14,2) #o
            self.text(81,60,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 14,3) #r
            self.text(81,60,6, 0,1,0, 0,0,0, 0,1,0, 0,1,0, 0,1,0, 14,4) #i
            self.text(81,60,6, 0,0,1, 0,1,1, 1,0,1, 1,0,1, 0,1,1, 14,5) #d
            self.text(81,60,6, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 14,6) #o
            self.text(81,60,6, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 14,7) #r

            if self.count >=30:
                self.text(92,290,3, 1,1,1, 1,0,0, 1,1,1, 1,0,0, 1,1,1, 14,0) #E
                self.text(92,290,3, 0,0,0, 1,1,0, 1,0,1, 1,0,1, 1,0,1, 14,1) #n
                self.text(92,290,3, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 14,2) #t
                self.text(92,290,3, 0,0,0, 0,1,1, 1,0,1, 1,1,0, 0,1,1, 14,3) #e
                self.text(92,290,3, 0,0,0, 0,1,1, 1,0,0, 1,0,0, 1,0,0, 14,4) #r
                self.text(92,290,3, 0,1,0, 1,1,1, 0,1,0, 0,1,0, 0,1,1, 14,6) #t
                self.text(92,290,3, 0,0,0, 0,1,0, 1,0,1, 1,0,1, 0,1,0, 14,7) #o
                self.text(92,290,3, 0,1,1, 1,0,0, 0,1,0, 0,0,1, 1,1,0, 14,9) #S
                self.text(92,290,3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 0,1,0, 14,10) #T
                self.text(92,290,3, 0,1,0, 1,0,1, 1,1,1, 1,0,1, 1,0,1, 14,11) #A
                self.text(92,290,3, 1,1,0, 1,0,1, 1,1,1, 1,1,0, 1,0,1, 14,12) #R
                self.text(92,290,3, 1,1,1, 0,1,0, 0,1,0, 0,1,0, 0,1,0, 14,13) #T
        


      else:

        if self.player_now == 1:
            pyxel.rectb(0,0,349,359,12)
            pyxel.rectb(1,1,347,357,12)
        elif self.player_now == 2:
            pyxel.rectb(0,0,349,359,14)
            pyxel.rectb(1,1,347,357,14)
   
        for x in range(9):
            for y in range(9):
                if self.gamemode == 1:
                    pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,0) #マス目表示
                elif self.player_now == 1:
                    pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,12) #マス目表示
                elif self.player_now == 2:
                    pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,14) #マス目表示
        pyxel.rect(7 + self.player1_x * 38, 7 + self.player1_y * 38 ,31,31,12)
        pyxel.rect(7 + self.player2_x * 38, 7 + self.player2_y * 38 ,31,31,14)
        pyxel.rect(7,344,11,11,12)
        pyxel.text(18,347," x "+str(self.wallnum_player1),12)
        pyxel.rect(311,344,11,11,14)
        pyxel.text(322,347," x "+str(self.wallnum_player2),14)
        pyxel.text(162,347,"TURN "+str(self.turn_count),0)
        if self.player_now == 1:
            pyxel.text(132,347,str(self.player1_time // 3600).zfill(2)+":"+str((self.player1_time % 3600)//60).zfill(2),12)
            pyxel.text(199,347,str(self.player2_time // 3600).zfill(2)+":"+str((self.player2_time % 3600)//60).zfill(2),0)
        elif self.player_now == 2:
            pyxel.text(132,347,str(self.player1_time // 3600).zfill(2)+":"+str((self.player1_time % 3600)//60).zfill(2),0)
            pyxel.text(199,347,str(self.player2_time // 3600).zfill(2)+":"+str((self.player2_time % 3600)//60).zfill(2),14)

        if self.gamemode == 1:
            if self.player_now == 1:
                pyxel.text(45,347,"Player1 TURN",12)
            if self.player_now == 2:
                pyxel.text(257,347,"Player2 TURN",14)
        elif self.gamemode == 2:
            if self.player_now == 1:
                pyxel.text(45,347,"Player1 WIN!",12)
                pyxel.text(249,347,"Enter to retry",0)
            if self.player_now == 2:
                pyxel.text(45,347,"Enter to retry",0)
                pyxel.text(257,347,"Player2 WIN!",14)
        
        

        if self.player_now == 1:

            #マスのカラー変更-上
            if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y and(not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y-1][self.player1_x] == 2) and (not self.wall_list[self.player1_y-1][self.player1_x+1] == 2):
                        self.box_color(self.player1_x,self.player1_y-2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y-1][self.player1_x] == 1 or self.wall_list[self.player1_y][self.player1_x] == 1):
                            self.box_color(self.player1_x-1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y-1][self.player1_x+1] == 1 or self.wall_list[self.player1_y][self.player1_x+1] == 1):
                            self.box_color(self.player1_x+1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2):
                    self.box_color(self.player1_x,self.player1_y-1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-右
            if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y and(not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1):
                        self.box_color(self.player1_x+2,self.player1_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y][self.player1_x+1] == 2 or self.wall_list[self.player1_y][self.player1_x+2] == 2):
                            self.box_color(self.player1_x+1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y+1][self.player1_x+1] == 2 or self.wall_list[self.player1_y+1][self.player1_x+2] == 2):
                            self.box_color(self.player1_x+1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1):
                    self.box_color(self.player1_x+1,self.player1_y) #プレイヤー飛び越えを行わない

            #マスのカラー変更-下
            if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y+2][self.player1_x] == 2) and (not self.wall_list[self.player1_y+2][self.player1_x+1] == 2):
                        self.box_color(self.player1_x,self.player1_y+2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y+1][self.player1_x+1] == 1 or self.wall_list[self.player1_y+2][self.player1_x+1] == 1):
                            self.box_color(self.player1_x+1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y+1][self.player1_x] == 1 or self.wall_list[self.player1_y+2][self.player1_x] == 1):
                            self.box_color(self.player1_x-1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2):
                    self.box_color(self.player1_x,self.player1_y+1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-左
            if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1):
                        self.box_color(self.player1_x-2,self.player1_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x-1] == 2):
                            self.box_color(self.player1_x-1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x-1] == 2):
                            self.box_color(self.player1_x-1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1):
                    self.box_color(self.player1_x-1,self.player1_y) #プレイヤー飛び越えを行わない

            
            

            #矢印のカラー変更
            if self.player1_vector == 1: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y-1][self.player1_x] == 2) and (not self.wall_list[self.player1_y-1][self.player1_x+1] == 2):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y-1][self.player1_x] == 1 or self.wall_list[self.player1_y][self.player1_x] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y-1][self.player1_x+1] == 1 or self.wall_list[self.player1_y][self.player1_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない

                else:
                    self.arrow_color = self.arrow_color_cant


                

            elif self.player1_vector == 2: #and self.player1_y >= 1:
                if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y][self.player1_x+1] == 2 or self.wall_list[self.player1_y][self.player1_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 2 or self.wall_list[self.player1_y+1][self.player1_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant
            elif self.player1_vector == 3: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y+2][self.player1_x] == 2) and (not self.wall_list[self.player1_y+2][self.player1_x+1] == 2):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 1 or self.wall_list[self.player1_y+2][self.player1_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 1 or self.wall_list[self.player1_y+2][self.player1_x] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant
            elif self.player1_vector == 4: #and self.player1_y >= 1:
                if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

                
        elif self.player_now == 2:


            #マスのカラー変更-上
            if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y-1][self.player2_x] == 2) and (not self.wall_list[self.player2_y-1][self.player2_x+1] == 2):
                        self.box_color(self.player2_x,self.player2_y-2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y-1][self.player2_x] == 1 or self.wall_list[self.player2_y][self.player2_x] == 1):
                            self.box_color(self.player2_x-1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y-1][self.player2_x+1] == 1 or self.wall_list[self.player2_y][self.player2_x+1] == 1):
                            self.box_color(self.player2_x+1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2):
                    self.box_color(self.player2_x,self.player2_y-1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-右
            if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1):
                        self.box_color(self.player2_x+2,self.player2_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y][self.player2_x+1] == 2 or self.wall_list[self.player2_y][self.player2_x+2] == 2):
                            self.box_color(self.player2_x+1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y+1][self.player2_x+1] == 2 or self.wall_list[self.player2_y+1][self.player2_x+2] == 2):
                            self.box_color(self.player2_x+1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1):
                    self.box_color(self.player2_x+1,self.player2_y) #プレイヤー飛び越えを行わない

            #マスのカラー変更-下
            if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y+2][self.player2_x] == 2) and (not self.wall_list[self.player2_y+2][self.player2_x+1] == 2):
                        self.box_color(self.player2_x,self.player2_y+2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y+1][self.player2_x+1] == 1 or self.wall_list[self.player2_y+2][self.player2_x+1] == 1):
                            self.box_color(self.player2_x+1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y+1][self.player2_x] == 1 or self.wall_list[self.player2_y+2][self.player2_x] == 1):
                            self.box_color(self.player2_x-1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2):
                    self.box_color(self.player2_x,self.player2_y+1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-左
            if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1):
                        self.box_color(self.player2_x-2,self.player2_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x-1] == 2):
                            self.box_color(self.player2_x-1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x-1] == 2):
                            self.box_color(self.player2_x-1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1):
                    self.box_color(self.player2_x-1,self.player2_y) #プレイヤー飛び越えを行わない
            

            #矢印のカラー変更
            if self.player2_vector == 1: #and self.player1_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y-1][self.player2_x] == 2) and (not self.wall_list[self.player2_y-1][self.player2_x+1] == 2):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y-1][self.player2_x] == 1 or self.wall_list[self.player2_y][self.player2_x] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y-1][self.player2_x+1] == 1 or self.wall_list[self.player2_y][self.player2_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

                

            elif self.player2_vector == 2: #and self.player2_y >= 1:
                if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y][self.player2_x+1] == 2 or self.wall_list[self.player2_y][self.player2_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 2 or self.wall_list[self.player2_y+1][self.player2_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

            elif self.player2_vector == 3: #and self.player2_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y+2][self.player2_x] == 2) and (not self.wall_list[self.player2_y+2][self.player2_x+1] == 2):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 1 or self.wall_list[self.player2_y+2][self.player2_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 1 or self.wall_list[self.player2_y+2][self.player2_x] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant
            elif self.player2_vector == 4: #and self.player2_y >= 1:
                if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

        for x in range(8):
            for y in range(8):
                if self.wall_list[y+1][x+1] == 1:
                    pyxel.rect(39+x*38,7+y*38,5,69,10)
                elif self.wall_list[y+1][x+1] == 2:
                    pyxel.rect(7+x*38,39+y*38,69,5,10)

        if self.player_now == 1:
            
            if self.player1_vector == 1:
                if self.player1_vector_dia == 0:
                    #上矢印    
                    pyxel.rect(18 + self.player1_x * 38,-5 + self.player1_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player1_x * 38,-4 + self.player1_y * 38,31 + self.player1_x * 38,-4 + self.player1_y * 38,22 + self.player1_x * 38,-13 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player1_x * 38,-4 + self.player1_y * 38,7,14,7)
                    pyxel.tri(16 + self.player1_x * 38,-5 + self.player1_y * 38,28 + self.player1_x * 38,-5 + self.player1_y * 38,22 + self.player1_x * 38,-11 + self.player1_y * 38,7)
                    self.cross__arrow_draw(22 + self.player1_x * 38,2 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #左上矢印    
                    pyxel.tri(-3 + self.player1_x * 38,3 + self.player1_y * 38,3 + self.player1_x * 38,-3 + self.player1_y * 38,7+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,-3 + self.player1_y * 38,13 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,-6 + self.player1_y * 38,-6 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,1 + self.player1_y * 38,1 + self.player1_x * 38,-3 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,-3 + self.player1_y * 38,11 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,4 + self.player1_y * 38,4 + self.player1_x * 38,-5 + self.player1_y * 38,-5 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,5 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #右上矢印    
                    pyxel.tri(47 + self.player1_x * 38,3 + self.player1_y * 38,41 + self.player1_x * 38,-3 + self.player1_y * 38,37+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,-3 + self.player1_y * 38,31 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,-6 + self.player1_y * 38,50 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,1 + self.player1_y * 38,43 + self.player1_x * 38,-3 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,-3 + self.player1_y * 38,33 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,4 + self.player1_y * 38,40 + self.player1_x * 38,-5 + self.player1_y * 38,49 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,5 + self.player1_y * 38)
            elif self.player1_vector == 2:
                if self.player1_vector_dia == 0:
                    #右矢印    
                    pyxel.rect(34 + self.player1_x * 38,18 + self.player1_y * 38,16,9,self.arrow_color)
                    pyxel.tri(48 + self.player1_x * 38,13 + self.player1_y * 38,48 + self.player1_x * 38,31 + self.player1_y * 38,57 + self.player1_x * 38,22 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(35 + self.player1_x * 38,19 + self.player1_y * 38,14,7,7)
                    pyxel.tri(49 + self.player1_x * 38,16 + self.player1_y * 38,49 + self.player1_x * 38,28 + self.player1_y * 38,55 + self.player1_x * 38,22 + self.player1_y * 38,7)
                    self.cross__arrow_draw(42 + self.player1_x * 38,22 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #右上矢印    
                    pyxel.tri(47 + self.player1_x * 38,3 + self.player1_y * 38,41 + self.player1_x * 38,-3 + self.player1_y * 38,37+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,-3 + self.player1_y * 38,31 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,-6 + self.player1_y * 38,50 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,1 + self.player1_y * 38,43 + self.player1_x * 38,-3 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,-3 + self.player1_y * 38,33 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,4 + self.player1_y * 38,40 + self.player1_x * 38,-5 + self.player1_y * 38,49 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,5 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #右下矢印    
                    pyxel.tri(47 + self.player1_x * 38,41 + self.player1_y * 38,41 + self.player1_x * 38,47 + self.player1_y * 38,37+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,47 + self.player1_y * 38,31 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,50 + self.player1_y * 38,50 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,43 + self.player1_y * 38,43 + self.player1_x * 38,47 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,47 + self.player1_y * 38,33 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,40 + self.player1_y * 38,40 + self.player1_x * 38,49 + self.player1_y * 38,49 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,39 + self.player1_y * 38)
            elif self.player1_vector == 3:
                if self.player1_vector_dia == 0:
                    #下矢印    
                    pyxel.rect(18 + self.player1_x * 38,34 + self.player1_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player1_x * 38,48 + self.player1_y * 38,31 + self.player1_x * 38,48 + self.player1_y * 38,22 + self.player1_x * 38,57 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player1_x * 38,35 + self.player1_y * 38,7,14,7)
                    pyxel.tri(16 + self.player1_x * 38,49 + self.player1_y * 38,28 + self.player1_x * 38,49 + self.player1_y * 38,22 + self.player1_x * 38,55 + self.player1_y * 38,7)
                    self.cross__arrow_draw(22 + self.player1_x * 38,42 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #右下矢印    
                    pyxel.tri(47 + self.player1_x * 38,41 + self.player1_y * 38,41 + self.player1_x * 38,47 + self.player1_y * 38,37+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,47 + self.player1_y * 38,31 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,50 + self.player1_y * 38,50 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,43 + self.player1_y * 38,43 + self.player1_x * 38,47 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,47 + self.player1_y * 38,33 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,40 + self.player1_y * 38,40 + self.player1_x * 38,49 + self.player1_y * 38,49 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,39 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #左下矢印    
                    pyxel.tri(-3 + self.player1_x * 38,41 + self.player1_y * 38,3 + self.player1_x * 38,47 + self.player1_y * 38,7+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,47 + self.player1_y * 38,13 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,50 + self.player1_y * 38,-6 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,43 + self.player1_y * 38,1 + self.player1_x * 38,47 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,47 + self.player1_y * 38,11 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,40 + self.player1_y * 38,4 + self.player1_x * 38,49 + self.player1_y * 38,-5 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,39 + self.player1_y * 38)
            elif self.player1_vector == 4:
                if self.player1_vector_dia == 0:
                    #左矢印    
                    pyxel.rect(-5 + self.player1_x * 38,18 + self.player1_y * 38,16,9,self.arrow_color)
                    pyxel.tri(-4 + self.player1_x * 38,13 + self.player1_y * 38,-4 + self.player1_x * 38,31 + self.player1_y * 38,-13 + self.player1_x * 38,22 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(-4 + self.player1_x * 38,19 + self.player1_y * 38,14,7,7)
                    pyxel.tri(-5 + self.player1_x * 38,16 + self.player1_y * 38,-5 + self.player1_x * 38,28 + self.player1_y * 38,-11 + self.player1_x * 38,22 + self.player1_y * 38,7)
                    self.cross__arrow_draw(2 + self.player1_x * 38,22 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #左下矢印    
                    pyxel.tri(-3 + self.player1_x * 38,41 + self.player1_y * 38,3 + self.player1_x * 38,47 + self.player1_y * 38,7+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,47 + self.player1_y * 38,13 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,50 + self.player1_y * 38,-6 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,43 + self.player1_y * 38,1 + self.player1_x * 38,47 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,47 + self.player1_y * 38,11 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,40 + self.player1_y * 38,4 + self.player1_x * 38,49 + self.player1_y * 38,-5 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,39 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #左上矢印    
                    pyxel.tri(-3 + self.player1_x * 38,3 + self.player1_y * 38,3 + self.player1_x * 38,-3 + self.player1_y * 38,7+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,-3 + self.player1_y * 38,13 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,-6 + self.player1_y * 38,-6 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,1 + self.player1_y * 38,1 + self.player1_x * 38,-3 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,-3 + self.player1_y * 38,11 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,4 + self.player1_y * 38,4 + self.player1_x * 38,-5 + self.player1_y * 38,-5 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,5 + self.player1_y * 38)

        elif self.player_now == 2:
            
            if self.player2_vector == 1:
                if self.player2_vector_dia == 0:
                    #上矢印    
                    pyxel.rect(18 + self.player2_x * 38,-5 + self.player2_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player2_x * 38,-4 + self.player2_y * 38,31 + self.player2_x * 38,-4 + self.player2_y * 38,22 + self.player2_x * 38,-13 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player2_x * 38,-4 + self.player2_y * 38,7,14,7)
                    pyxel.tri(16 + self.player2_x * 38,-5 + self.player2_y * 38,28 + self.player2_x * 38,-5 + self.player2_y * 38,22 + self.player2_x * 38,-11 + self.player2_y * 38,7)
                    self.cross__arrow_draw(22 + self.player2_x * 38,2 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #左上矢印    
                    pyxel.tri(-3 + self.player2_x * 38,3 + self.player2_y * 38,3 + self.player2_x * 38,-3 + self.player2_y * 38,7+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,-3 + self.player2_y * 38,13 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,-6 + self.player2_y * 38,-6 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,1 + self.player2_y * 38,1 + self.player2_x * 38,-3 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,-3 + self.player2_y * 38,11 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,4 + self.player2_y * 38,4 + self.player2_x * 38,-5 + self.player2_y * 38,-5 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,5 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #右上矢印    
                    pyxel.tri(47 + self.player2_x * 38,3 + self.player2_y * 38,41 + self.player2_x * 38,-3 + self.player2_y * 38,37+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,-3 + self.player2_y * 38,31 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,-6 + self.player2_y * 38,50 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,1 + self.player2_y * 38,43 + self.player2_x * 38,-3 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,-3 + self.player2_y * 38,33 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,4 + self.player2_y * 38,40 + self.player2_x * 38,-5 + self.player2_y * 38,49 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,5 + self.player2_y * 38)
            elif self.player2_vector == 2:
                if self.player2_vector_dia == 0:
                    #右矢印    
                    pyxel.rect(34 + self.player2_x * 38,18 + self.player2_y * 38,16,9,self.arrow_color)
                    pyxel.tri(48 + self.player2_x * 38,13 + self.player2_y * 38,48 + self.player2_x * 38,31 + self.player2_y * 38,57 + self.player2_x * 38,22 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(35 + self.player2_x * 38,19 + self.player2_y * 38,14,7,7)
                    pyxel.tri(49 + self.player2_x * 38,16 + self.player2_y * 38,49 + self.player2_x * 38,28 + self.player2_y * 38,55 + self.player2_x * 38,22 + self.player2_y * 38,7)
                    self.cross__arrow_draw(42 + self.player2_x * 38,22 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #右上矢印    
                    pyxel.tri(47 + self.player2_x * 38,3 + self.player2_y * 38,41 + self.player2_x * 38,-3 + self.player2_y * 38,37+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,-3 + self.player2_y * 38,31 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,-6 + self.player2_y * 38,50 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,1 + self.player2_y * 38,43 + self.player2_x * 38,-3 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,-3 + self.player2_y * 38,33 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,4 + self.player2_y * 38,40 + self.player2_x * 38,-5 + self.player2_y * 38,49 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,5 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #右下矢印    
                    pyxel.tri(47 + self.player2_x * 38,41 + self.player2_y * 38,41 + self.player2_x * 38,47 + self.player2_y * 38,37+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,47 + self.player2_y * 38,31 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,50 + self.player2_y * 38,50 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,43 + self.player2_y * 38,43 + self.player2_x * 38,47 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,47 + self.player2_y * 38,33 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,40 + self.player2_y * 38,40 + self.player2_x * 38,49 + self.player2_y * 38,49 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,39 + self.player2_y * 38)
            elif self.player2_vector == 3:
                if self.player2_vector_dia == 0:
                    #下矢印    
                    pyxel.rect(18 + self.player2_x * 38,34 + self.player2_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player2_x * 38,48 + self.player2_y * 38,31 + self.player2_x * 38,48 + self.player2_y * 38,22 + self.player2_x * 38,57 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player2_x * 38,35 + self.player2_y * 38,7,14,7)
                    pyxel.tri(16 + self.player2_x * 38,49 + self.player2_y * 38,28 + self.player2_x * 38,49 + self.player2_y * 38,22 + self.player2_x * 38,55 + self.player2_y * 38,7)
                    self.cross__arrow_draw(22 + self.player2_x * 38,42 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #右下矢印    
                    pyxel.tri(47 + self.player2_x * 38,41 + self.player2_y * 38,41 + self.player2_x * 38,47 + self.player2_y * 38,37+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,47 + self.player2_y * 38,31 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,50 + self.player2_y * 38,50 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,43 + self.player2_y * 38,43 + self.player2_x * 38,47 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,47 + self.player2_y * 38,33 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,40 + self.player2_y * 38,40 + self.player2_x * 38,49 + self.player2_y * 38,49 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,39 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #左下矢印    
                    pyxel.tri(-3 + self.player2_x * 38,41 + self.player2_y * 38,3 + self.player2_x * 38,47 + self.player2_y * 38,7+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,47 + self.player2_y * 38,13 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,50 + self.player2_y * 38,-6 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,43 + self.player2_y * 38,1 + self.player2_x * 38,47 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,47 + self.player2_y * 38,11 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,40 + self.player2_y * 38,4 + self.player2_x * 38,49 + self.player2_y * 38,-5 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,39 + self.player2_y * 38)
            elif self.player2_vector == 4:
                if self.player2_vector_dia == 0:
                    #左矢印    
                    pyxel.rect(-5 + self.player2_x * 38,18 + self.player2_y * 38,16,9,self.arrow_color)
                    pyxel.tri(-4 + self.player2_x * 38,13 + self.player2_y * 38,-4 + self.player2_x * 38,31 + self.player2_y * 38,-13 + self.player2_x * 38,22 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(-4 + self.player2_x * 38,19 + self.player2_y * 38,14,7,7)
                    pyxel.tri(-5 + self.player2_x * 38,16 + self.player2_y * 38,-5 + self.player2_x * 38,28 + self.player2_y * 38,-11 + self.player2_x * 38,22 + self.player2_y * 38,7)
                    self.cross__arrow_draw(2 + self.player2_x * 38,22 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #左下矢印    
                    pyxel.tri(-3 + self.player2_x * 38,41 + self.player2_y * 38,3 + self.player2_x * 38,47 + self.player2_y * 38,7+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,47 + self.player2_y * 38,13 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,50 + self.player2_y * 38,-6 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,43 + self.player2_y * 38,1 + self.player2_x * 38,47 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,47 + self.player2_y * 38,11 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,40 + self.player2_y * 38,4 + self.player2_x * 38,49 + self.player2_y * 38,-5 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,39 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #左上矢印    
                    pyxel.tri(-3 + self.player2_x * 38,3 + self.player2_y * 38,3 + self.player2_x * 38,-3 + self.player2_y * 38,7+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,-3 + self.player2_y * 38,13 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,-6 + self.player2_y * 38,-6 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,1 + self.player2_y * 38,1 + self.player2_x * 38,-3 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,-3 + self.player2_y * 38,11 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,4 + self.player2_y * 38,4 + self.player2_x * 38,-5 + self.player2_y * 38,-5 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,5 + self.player2_y * 38)

        if self.install_mode == 1:
            for x in range(8):
                for y in range(8):
                    if self.wall_list[y+1][x+1] == 0 and (not(self.wall_list[y][x+1] == 1 or self.wall_list[y+2][x+1] == 1)) and (not(x+1==self.wall_x and y+1==self.wall_y)) and self.wall_can(y+1,x+1,self.install_mode,False):
                        pyxel.rectb(38+x*38,38+y*38,7,7,11)

            if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y-1][self.wall_x] == 1 or self.wall_list[self.wall_y+1][self.wall_x] == 1)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
                if self.player_now == 1:
                    pyxel.rectb(0+self.wall_x*38,-31+self.wall_y*38,7,69,12)
                    pyxel.rectb(1+self.wall_x*38,-30+self.wall_y*38,5,67,12)
                elif self.player_now == 2:
                    pyxel.rectb(0+self.wall_x*38,-31+self.wall_y*38,7,69,14)
                    pyxel.rectb(1+self.wall_x*38,-30+self.wall_y*38,5,67,14)
            else:
                pyxel.rectb(0+self.wall_x*38,-31+self.wall_y*38,7,69,13)
                pyxel.rectb(1+self.wall_x*38,-30+self.wall_y*38,5,67,13)
                self.cross__wall_draw(3+self.wall_x*38,3+self.wall_y*38)

            
        elif self.install_mode == 2:
            for x in range(8):
                for y in range(8):
                    if self.wall_list[y+1][x+1] == 0 and (not(self.wall_list[y+1][x] == 2 or self.wall_list[y+1][x+2] == 2)) and (not(x+1==self.wall_x and y+1==self.wall_y)) and self.wall_can(y+1,x+1,self.install_mode,False):
                        pyxel.rectb(38+x*38,38+y*38,7,7,9)

            if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y][self.wall_x-1] == 2 or self.wall_list[self.wall_y][self.wall_x+1] == 2)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
                if self.player_now == 1:
                    pyxel.rectb(-31+self.wall_x*38,0+self.wall_y*38,69,7,12)
                    pyxel.rectb(-30+self.wall_x*38,1+self.wall_y*38,67,5,12)
                elif self.player_now == 2:
                    pyxel.rectb(-31+self.wall_x*38,0+self.wall_y*38,69,7,14)
                    pyxel.rectb(-30+self.wall_x*38,1+self.wall_y*38,67,5,14)
            else:
                pyxel.rectb(-31+self.wall_x*38,0+self.wall_y*38,69,7,13)
                pyxel.rectb(-30+self.wall_x*38,1+self.wall_y*38,67,5,13)
                self.cross__wall_draw(3+self.wall_x*38,3+self.wall_y*38)
    
      #pyxel.text(100,100,str(self.wall_list_tent[4]),0)
      #pyxel.text(100,110,str(self.wall_list[4]),0)
      #デバッグ用


        

        

        

          
        

        

Quoridor()