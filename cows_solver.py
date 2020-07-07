cells = [1,2,5,7,9,15,25,26,35,40,50,55,60,61,65,75]
has_red_color = [7,9,25,26,50,61]
has_red_word = [1,5,25,60,65]
has_green_color = [60]
has_green_word = [1,2,5,25,40,65]
has_word_word = [2,5,35]
begins_with_if = [26,61,65]
search_space = []

def effect(this, other, is_cur):
    if this == 1:
        return

def move_cur(cur, prev, ignore_red):

def move_prev(cur, prev, ignore_red):

def search(cur, prev, ignore_red):
    search_space.append((cur, prev, ignore_red))
    if cur == 50 and prev == 50:
        return [50]
    else if ignore_red and (cur == 50 or prev == 50):
        return [50]
    else if ((cur == 50 and prev == 61) or (cur == 61 and prev == 50)) and not ignore_red:
        return [61]
    # Move cur
    new_cur, new_prev, new_ir = move_cur(cur, prev, ignore_red)
    if not (new_cur, new_prev, new_ir) in search_space:
        res = search(new_cur, new_prev, new_ir)
        if res:
            return res.append(cur)
    # Move prev
    new_cur, new_prev, new_ir = move_prev(cur, prev, ignore_red)
    if not (new_cur, new_prev, new_ir) in search_space:
        res = search(new_cur, new_prev, new_ir)
        if res:
            return res.append(cur)


print(search(1,7,False))
