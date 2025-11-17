def is_valid(id1, id2):
  if len(id1) != len(id2):
    return False
  return all(id1[i] == id2[i] or id2[i] == '*' for i in range(len(id1)))

def recursion_64064(user_id, banned_id, user_sel, ban_idx, result):
  if ban_idx == len(banned_id):
    result.add(frozenset(user_sel))
    return

  for user in user_id:
    if user not in user_sel and is_valid(user, banned_id[ban_idx]):
      user_sel.add(user)
      recursion_64064(user_id, banned_id, user_sel, ban_idx + 1, result)
      user_sel.remove(user)

def solution(user_id, banned_id):
  result = set()
  recursion_64064(user_id, banned_id, set(), 0, result)
  return len(result)
