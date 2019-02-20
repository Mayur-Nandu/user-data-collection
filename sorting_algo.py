##sorting and creating list of non repetative array

def remove_duplicate(total_id):
    for i in range(len(total_id)):
        if i < len(total_id)-1: 
            if total_id[i]==total_id[i+1]:
                total_id.pop(i)
    return total_id




    
