def rotate_matrix_clockwise(matrix):
    # 3x3 행렬을 시계 방향으로 90도 회전
    new_matrix = [['' for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            new_matrix[c][2 - r] = matrix[r][c]
    return new_matrix

def rotate_matrix_counter_clockwise(matrix):
    # 3x3 행렬을 반시계 방향으로 90도 회전
    new_matrix = [['' for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            new_matrix[2 - c][r] = matrix[r][c]
    return new_matrix

def solve():
    # 큐브 초기 상태 설정
    # U: 윗면(흰색), D: 아랫면(노란색), F: 앞면(빨간색), B: 뒷면(오렌지색), L: 왼쪽면(초록색), R: 오른쪽면(파란색)
    cube = {
        'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)],
    }

    n = int(input())
    moves = input().split()

    for move in moves:
        face = move[0]
        direction = move[1]

        if face == 'U':
            if direction == '+':
                cube['U'] = rotate_matrix_clockwise(cube['U'])
                # 인접 면 회전
                temp_row = cube['F'][0][:] # F의 첫 번째 행
                cube['F'][0] = cube['R'][0][:] # R의 첫 번째 행 -> F의 첫 번째 행
                cube['R'][0] = cube['B'][0][:] # B의 첫 번째 행 -> R의 첫 번째 행
                cube['B'][0] = cube['L'][0][:] # L의 첫 번째 행 -> B의 첫 번째 행
                cube['L'][0] = temp_row[:]     # 이전 F의 첫 번째 행 -> L의 첫 번째 행
            else: # direction == '-'
                cube['U'] = rotate_matrix_counter_clockwise(cube['U'])
                # 인접 면 회전
                temp_row = cube['F'][0][:] # F의 첫 번째 행
                cube['F'][0] = cube['L'][0][:] # L의 첫 번째 행 -> F의 첫 번째 행
                cube['L'][0] = cube['B'][0][:] # B의 첫 번째 행 -> L의 첫 번째 행
                cube['B'][0] = cube['R'][0][:] # R의 첫 번째 행 -> B의 첫 번째 행
                cube['R'][0] = temp_row[:]     # 이전 F의 첫 번째 행 -> R의 첫 번째 행
        
        elif face == 'D':
            if direction == '+':
                cube['D'] = rotate_matrix_clockwise(cube['D'])
                # 인접 면 회전 (F, L, B, R의 세 번째 행)
                temp_row = cube['F'][2][:]
                cube['F'][2] = cube['L'][2][:]
                cube['L'][2] = cube['B'][2][:]
                cube['B'][2] = cube['R'][2][:]
                cube['R'][2] = temp_row[:]
            else: # direction == '-'
                cube['D'] = rotate_matrix_counter_clockwise(cube['D'])
                # 인접 면 회전 (F, R, B, L의 세 번째 행)
                temp_row = cube['F'][2][:]
                cube['F'][2] = cube['R'][2][:]
                cube['R'][2] = cube['B'][2][:]
                cube['B'][2] = cube['L'][2][:]
                cube['L'][2] = temp_row[:]

        elif face == 'F':
            if direction == '+':
                cube['F'] = rotate_matrix_clockwise(cube['F'])
                # 인접 면 회전
                # U의 세 번째 행, R의 첫 번째 열, D의 첫 번째 행 (뒤집어서), L의 세 번째 열 (뒤집어서)
                temp_row_U = cube['U'][2][:]
                
                # U의 2행을 R의 0열로
                for i in range(3): cube['U'][2][i] = cube['L'][2-i][2] # L의 2열 역순
                
                # R의 0열을 D의 0행으로
                for i in range(3): cube['L'][i][2] = cube['D'][0][i] # D의 0행
                
                # D의 0행을 L의 2열로
                for i in range(3): cube['D'][0][i] = cube['R'][2-i][0] # R의 0열 역순
                
                # L의 2열을 U의 2행으로
                for i in range(3): cube['R'][i][0] = temp_row_U[i]
                
            else: # direction == '-'
                cube['F'] = rotate_matrix_counter_clockwise(cube['F'])
                # 인접 면 회전 (역방향)
                temp_row_U = cube['U'][2][:]
                
                # U의 2행을 L의 2열로
                for i in range(3): cube['U'][2][i] = cube['R'][i][0]
                
                # R의 0열을 D의 0행으로
                for i in range(3): cube['R'][i][0] = cube['D'][0][2-i]
                
                # D의 0행을 L의 2열로
                for i in range(3): cube['D'][0][i] = cube['L'][i][2]
                
                # L의 2열을 U의 2행으로
                for i in range(3): cube['L'][i][2] = temp_row_U[2-i]

        elif face == 'B':
            if direction == '+':
                cube['B'] = rotate_matrix_clockwise(cube['B'])
                # 인접 면 회전
                temp_row_U = cube['U'][0][:]

                for i in range(3): cube['U'][0][i] = cube['R'][i][2]
                for i in range(3): cube['R'][i][2] = cube['D'][2][2-i]
                for i in range(3): cube['D'][2][i] = cube['L'][i][0]
                for i in range(3): cube['L'][i][0] = temp_row_U[2-i]
            else: # direction == '-'
                cube['B'] = rotate_matrix_counter_clockwise(cube['B'])
                # 인접 면 회전 (역방향)
                temp_row_U = cube['U'][0][:]

                for i in range(3): cube['U'][0][i] = cube['L'][2-i][0]
                for i in range(3): cube['L'][i][0] = cube['D'][2][i]
                for i in range(3): cube['D'][2][i] = cube['R'][2-i][2]
                for i in range(3): cube['R'][i][2] = temp_row_U[i]

        elif face == 'L':
            if direction == '+':
                cube['L'] = rotate_matrix_clockwise(cube['L'])
                # 인접 면 회전
                temp_col_U = [cube['U'][i][0] for i in range(3)]

                for i in range(3): cube['U'][i][0] = cube['B'][2-i][2] # B의 2열 역순
                for i in range(3): cube['B'][i][2] = cube['D'][2-i][0] # D의 0열 역순
                for i in range(3): cube['D'][i][0] = cube['F'][i][0]
                for i in range(3): cube['F'][i][0] = temp_col_U[i]
            else: # direction == '-'
                cube['L'] = rotate_matrix_counter_clockwise(cube['L'])
                # 인접 면 회전 (역방향)
                temp_col_U = [cube['U'][i][0] for i in range(3)]

                for i in range(3): cube['U'][i][0] = cube['F'][i][0]
                for i in range(3): cube['F'][i][0] = cube['D'][i][0]
                for i in range(3): cube['D'][i][0] = cube['B'][2-i][2] # B의 2열 역순
                for i in range(3): cube['B'][i][2] = temp_col_U[2-i]

        elif face == 'R':
            if direction == '+':
                cube['R'] = rotate_matrix_clockwise(cube['R'])
                # 인접 면 회전
                temp_col_U = [cube['U'][i][2] for i in range(3)]

                for i in range(3): cube['U'][i][2] = cube['F'][i][2]
                for i in range(3): cube['F'][i][2] = cube['D'][i][2]
                for i in range(3): cube['D'][i][2] = cube['B'][2-i][0] # B의 0열 역순
                for i in range(3): cube['B'][i][0] = temp_col_U[2-i]
            else: # direction == '-'
                cube['R'] = rotate_matrix_counter_clockwise(cube['R'])
                # 인접 면 회전 (역방향)
                temp_col_U = [cube['U'][i][2] for i in range(3)]

                for i in range(3): cube['U'][i][2] = cube['B'][2-i][0]
                for i in range(3): cube['B'][i][0] = cube['D'][2-i][2]
                for i in range(3): cube['D'][i][2] = cube['F'][i][2]
                for i in range(3): cube['F'][i][2] = temp_col_U[i]
                
    # 결과 출력
    for row in cube['U']:
        print("".join(row))

# 여러 테스트 케이스 처리
T = int(input())
for _ in range(T):
    solve()