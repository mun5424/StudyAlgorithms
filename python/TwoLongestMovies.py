# given a list of movie runtimes and a duration, find two movies that are the longest that does not exceed the duration. 
def findLongestTwoMovies(movies: int, duration: int):
    movies.sort()
    lo = 0
    hi = len(movies) - 1
    while(lo <= hi): 
        if movies[lo] + movies[hi] == duration:
            print('lo is {} and hi is {}'.format(lo,hi)) 
            return
        elif movies[lo] + movies[hi] >= duration: 
            hi -= 1
        else:
            lo += 1


    