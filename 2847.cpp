//게임을 많든 동준이

#include <algorithm>
#include <iostream>// 입출력 가능하게 하는 헤더
using namespace	std;

int	no_sort(int cur, int next) //다음 점수보다 크거나 같으면 1
{
	if (cur < next)
		return (0);
	return (1);
}


int	main()
{
	ios::sync_with_stdio(false);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(nullptr); //cin 전에 cout 버퍼 비우지 않게

	int	n, res = 0;
	cin >> n;
	int arr[n];

	for (int i = 0; i < n; i++)
		cin >> arr[i];
	for (int i = n - 2; i >= 0; i--)
	{
		while (no_sort(arr[i], arr[i + 1]))
		{
			res++;
			arr[i]--;
		}
	}
	cout << res;
}
