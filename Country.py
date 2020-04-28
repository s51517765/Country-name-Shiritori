#!/usr/bin/env python
# -*- coding: utf-8 -*-

country = []
v = []  # 訪れたところ
max = 0
dic = {}  # 頭文字ごとにまとめる


def import_list():
    file = open('countries.dic.txt', 'r', encoding='utf')  # UTFを指定する
    Line = "1"
    while Line != "":
        try:
            Line = file.readline()
            tmp = Line.split(",")[1]
            tmp = tmp.replace("\n", "")
            country.append(tmp)
        except:
            pass
    country.sort()
    print(country)
    print(len(country))
    tmp = []

    for i in range(1, len(country)):
        if country[i][:1] == country[i - 1][:1]:
            tmp.append(country[i])
        else:
            dic[country[i-1][:1]] = tmp
            tmp = []
            tmp.append(country[i])
    print(dic)


def dfs(ctr):  # 現在地
    try:
        global dic
        dic2 = dic[ctr[len(ctr)-1:]]
        for i in range(len(dic2)):
            # 現在地の末尾と頭が一致する国で訪問済みでない
            if dic2[i] not in v:
                v.append(dic2[i])
                count = len(v)
                global max
                if count > max:
                    max = count
                    print(str(count))
                    print(v)
                if dic2[i][len(dic2[i]) - 1:] in dic:
                    dfs(dic2[i])  # 再帰的に実行
                v.remove(dic2[i])  # 指定して最後の国名を消す

    except Exception as e:
        print(e)


def main():
    for i in range(len(country)):
        global v
        v = []
        v.append(country[i])
        dfs(country[i])


if __name__ == '__main__':
    import_list()
    main()
    print("Complete!")
