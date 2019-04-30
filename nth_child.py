# do it 20 times
for x in range(20):
    # click the nth-child button from 1 to 4
    num = (x % 4) + 1
    print('[class="edit-setting-profile ui"] a[class="item"]:nth-child(\"%s\")' % num)
