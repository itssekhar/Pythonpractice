def find1(ordered_list,ele_find):
    for ele in ordered_list:
        if ele == ele_find:
            return True
        
    return False
if __name__ == "__main__":
    l = [2,4,6,7]
    print(find1(l,9))
            