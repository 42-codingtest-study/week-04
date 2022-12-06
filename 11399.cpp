//atm

#include <algorithm>
#include <iostream>// 입출력 가능하게 하는 헤더
using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c

int	main()
{
	ios::sync_with_stdio(false);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(nullptr); //cin 전에 cout 버퍼 비우지 않게

	int	n, res = 0;

	cin >> n;
	int arr[n];
	for (int i = 0; i < n; i++) // 싹다 어레이에 넣어주고 정렬
		cin >> arr[i];
	sort(arr, arr + n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= i; j++)
			res += arr[j];
	}
	cout << res;
}
