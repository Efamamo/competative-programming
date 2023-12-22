class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            for column in range(len(image[row])):
                if image[row][column]:
                    image[row][column]=0
                else:
                    image[row][column]=1
            image[row].reverse()
        return image
