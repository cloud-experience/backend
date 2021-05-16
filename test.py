import checkPage

testURL = "bit.ly/334DlJS"

data = checkPage.checkPage(testURL, ["이용약관"])
print(data)
