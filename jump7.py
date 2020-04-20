# 遇“7”跳过游戏



def main():
    for i in range(100):
        if i % 10 == 7:
            pass
        elif i % 7 == 0:
            pass
        elif i // 10 == 7:
            pass
        else:
            print(i)


if __name__ == "__main__":
	main()