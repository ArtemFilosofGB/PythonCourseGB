#Write the function collinearity(x1, y1, x2, y2), which returns a Boolean type depending on whether the vectors are collinear or not.
#Be careful when handling cases where x1, x2, y1, or y2 are zero to avoid division by zero errors.
#A vector with coordinates (0, 0) is collinear to all vectors.
def collinearity(x1, y1, x2, y2):
    if(x1*y2==y1*x2):
        return True
    return False