num = "1321"
#http://www.ardendertat.com/2011/12/01/programming-interview-questions-19-find-next-palindrome-number/
#Need to do this on own soon...
def getNextPalindrome(num):
    num = str(num)
    tempNum = ""
    if num == "":
        return -1
    if len(num) % 2 == 0:
        firstHalf = num[:len(num)/2]
        tempNum = firstHalf + firstHalf[::-1]
        if int(tempNum) > int(num):
            return tempNum
        else:
            if getNextPalindrome(num[1:-1]) != -1:
                return int(num[0])*100 + getNextPalindrome(num[1:-1])*10 + int(num[0])
            else:
                newDigit = int(num[0]) + 1
                return newDigit*11

print getNextPalindrome('2345')
