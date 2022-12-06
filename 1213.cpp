//펠린드롬만들기

#include <algorithm>
#include <cstring>
#include <iostream>// 입출력 가능하게 하는 헤더
using namespace	std;
//파일 입력 : cin >> 변수명;
//파일 출력 : cout << "a + "<< 변수 << " = c";
//출력) a + 변수 = c

int	oddstring(char	*arr) //홀수면 1반환
{
	if (strlen(arr) % 2)
		return (1);
	return (0);
}

int	oddpalindrome(int *alph) //홀수 펠린드롬이면 1반환
{
	int oddsignal = 0, i = -1;

	while (++i < 26)
		if (alph[i] % 2)
			oddsignal++;
	if (oddsignal == 1)
		return (1);
	return (0);
}

int	evenpalindrome(int *alph) //짝수 펠린드롬이면 1반환
{
	int oddsignal = 0, i = -1;

	while (++i < 26)
		if (alph[i] % 2)
			oddsignal++;
	if (oddsignal == 0)
		return (1);
	return (0);
}

char *get_odd_palindromearr(int *alph, char res[], int reslen) //reslen 만들기
{
	int i = 0, residx = 0;
	char middle_c;
	while (i < 26)
	{
		if (alph[i] == 0) //alph배열의 각자릿값 문자 다썼으면
		{
			i++;
			continue;
		}
		if (alph[i] == 1) //중간글자면
		{
			middle_c = i + 'A';
			alph[i]--;
			continue;
		}
		res[residx] = i + 'A';
		res[reslen - residx - 1] = i + 'A';
		residx++;
		alph[i] -= 2;
	}
	res[reslen / 2] = middle_c;
	res[reslen] = '\0';
	return (res);
}

char *get_even_palindromearr(int *alph, char res[], int reslen) //reslen 만들기
{
	int i = 0, residx = 0;
	while (i < 26)
	{
		if (alph[i] == 0) //alph배열의 각자릿값 문자 다썼으면
		{
			i++;
			continue;
		}
		res[residx] = i + 'A';
		res[reslen - residx - 1] = i + 'A';
		residx++;
		alph[i] -= 2;
	}
	res[reslen] = '\0';
	return (res);
}

int	main()
{
	ios::sync_with_stdio(false);//c++stream과 cstream의 연결 끊기 : 시간 단축
	cin.tie(nullptr); //cin 전에 cout 버퍼 비우지 않게

	int	i = 0, mididx;
	char	arr[51], res[51];
	cin >> arr;
	int	alph[26] = { 0 };

	while (arr[i])
		alph[arr[i++] - 'A']++;
	if (oddstring(arr) && oddpalindrome(alph)) //홀수고 펠린드롬이면
		cout << get_odd_palindromearr(alph, res, strlen(arr));
	else if(!oddstring(arr) && evenpalindrome(alph))//짝수고 펠린드롬이면
		cout << get_even_palindromearr(alph, res,strlen(arr));
	else
		cout << "I'm Sorry Hansoo";
}
