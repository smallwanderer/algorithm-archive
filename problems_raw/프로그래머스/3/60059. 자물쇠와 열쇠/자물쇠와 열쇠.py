def rotation(key):
    m = len(key)-1
    rotation_90 = [[None for _ in range(m+1)] for _ in range(m+1)]
    rotation_180 = [[None for _ in range(m+1)] for _ in range(m+1)]
    rotation_270 = [[None for _ in range(m+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(m+1):
            rotation_90[i][j] = (key[m-j][i])
            rotation_180[i][j] = (key[m-i][m-j])
            rotation_270[i][j] = (key[j][m-i])
    return [key, rotation_90, rotation_180, rotation_270]

def _is_valid(key, lock, valid_cnt):
    result = []
    for i in range(len(key)):
        for j in range(len(key)):
            if lock[i][j] == -1:
                continue
            if key[i][j] == 1 and lock[i][j] == 1:
                return None
            elif key[i][j] == 0 and lock[i][j] == 0:
                return None
            elif key[i][j] == 1 and lock[i][j] == 0:
                result.append((i, j))
    return True if len(result) == valid_cnt else False
            

def solution(key, lock):
    len_key, len_lock = len(key), len(lock)
    new_len = 2 * (len_key-1) + len_lock
    new_lock = [[-1 for _ in range(new_len)] for _ in range(new_len)]
    unlock = []
    for i in range(len_lock):
        for j in range(len_lock):
            new_lock[i+len_key-1][j+len_key-1] = lock[i][j]
            if lock[i][j] == 0:
                unlock.append((i+len_key-1, j+len_key-1))
    rotations = rotation(key)

    def _subarray(start_i, start_j, m):
        temp = [[None for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                temp[i][j] = new_lock[start_i+i][start_j+j]
        return temp
    
    for i in range(new_len-len_key+1):
        for j in range(new_len-len_key+1):
            for rot in rotations:
                if _is_valid(rot, _subarray(i, j, len_key), len(unlock)):
                    return True

    return False
            
    
    