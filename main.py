import pygame

from const import *

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# 변수

while True:
    # 화면 색 채우기 -> 기본 단색 0,0,0
    screen.fill(BLACK)

    # 변수 업데이트
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # 화면 그리기

    # 모든 화면 그리기 업데이트
    pygame.display.update()
    # 30 FPS(초당 프레임) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값
    clock.tick(30)

pygame.quit()
