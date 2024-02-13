class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j-1] + row[j]

            row.append(1)

        return row

solution_instance = Solution()
rowIndex = int(input("Enter the row index to retrieve from Pascal's triangle: "))
print(solution_instance.getRow(rowIndex))
