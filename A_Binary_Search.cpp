#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define el '\n'

const int MOD = 1e9 + 7;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n,x; cin >> n >> x;
  int ar[n];
  for(int i = 0; i < n; i++){
    cin >> ar[i];
  }
  sort(ar, ar + n);
  while(x--){
    int q; cin >> q;
    int l = 0, r = n - 1, answ = -1;
    while(l <= r){
      int mid = l + (r - l) / 2;
      if (ar[mid] == q){
        answ = mid + 1;
        break;
      }else if(ar[mid] < q){
        l = mid + 1;
      }else{
        r = mid - 1;
      }
    }
    cout << answ << el;
  }
  
  return 0;
}