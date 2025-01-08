class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = (image[i][::-1])
        for j in range(0, len(image)):
            for k in range(0, len(image[j])):
                if image[j][k] == 0:
                    image[j][k] = 1 
                else:
                    image[j][k] = 0
        return image