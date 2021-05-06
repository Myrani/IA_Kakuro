def mapping_Row(kakuro,weigth):
    
    for i in range(0,len(kakuro)):
        free_spots = []
        
        for j in range(0,len(kakuro[i])):
            if kakuro[i][j][0] == "   ":
                free_spots.append([i,j])
        
        for spot in free_spots:
            kakuro[spot[0]][spot[1]][1] += weigth/len(free_spots) #à opti

    return kakuro    


def mapping_Collumn(kakuro,weigth):
    
    for i in range(0,len(kakuro)):
        free_spots = []
        
        for j in range(0,len(kakuro[i])):
            if kakuro[j][i][0] == "   ":
                free_spots.append([j,i])
        
        for spot in free_spots:
            kakuro[spot[0]][spot[1]][1] += weigth/len(free_spots) #à opti

    return kakuro    


def set_Heat_Mapping(kakuro):
    default_Weigth = 100 
    
    mapped_kakuro = mapping_Row(kakuro,default_Weigth)
    mapped_kakuro = mapping_Collumn(kakuro,default_Weigth)

    return mapped_kakuro





